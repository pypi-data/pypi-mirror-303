import functools
import inspect
import logging
from typing import (
    Any,
    Callable,
)

from connector.async_.lumos import LumosCommandsMixin
from connector.errors import (
    ConnectorError,
    DefaultHandler,
    ErrorMap,
)
from connector.serializers.lumos import (
    EncounteredErrorResponse,
)
from connector.serializers.response import Response

logger = logging.getLogger(__name__)


def connector_handler(
    exception_classes: ErrorMap,
):
    """
    Decorator that adds default exception handlers to a class. Iterates over its methods and attaches a exception_handler decorator (below).

    Example:
    ```python
    @connector_handler([
        (httpx.HTTPStatusError, ExceptionHandler, "error.code"),
    ])
    class AsyncCommands(LumosCommandsMixin):
        def verify_credentials(self, args: ValidateCredentialsArgs) -> ValidateCredentialsResp:
            pass
    ```

    Args:
        exception_classes (tuple): Tuple of exception classes to be handled. Map of exception class to handler function.

    Returns
    -------
        class_decorator (function): Decorator that adds exception handlers to a class.
    """
    default_classes: ErrorMap = []  # TODO: potentially add defaults in some latter PR
    exception_classes.extend(default_classes)

    def class_decorator(cls: LumosCommandsMixin):
        app_id = None
        attrs = inspect.getmembers(cls, lambda a: not inspect.isroutine(a))
        for name, value in attrs:
            if name == "app_id":
                app_id = value

        for attr_name, attr_value in cls.__dict__.items():
            if callable(attr_value):
                decorated_func = exception_handler(exception_classes, app_id)(attr_value)
                setattr(cls, attr_name, decorated_func)
        return cls

    return class_decorator


def exception_handler(
    exception_classes: ErrorMap,
    app_id: str | None = None,
):
    """
    Decorator that adds error handling to a method. Uses the default Lumos error handler if no exception handler is provided.

    Example:
    ```python
    @exception_handler(
        (httpx.HTTPStatusError, ExceptionHandler, "error.code"),
    )
    async def verify_credentials(self, args: ValidateCredentialsArgs) -> ValidateCredentialsResp:
        pass
    ```

    Args:
        exception_classes (tuple): Tuple of exception classes to be handled. Map of exception class to handler function.

    Returns
    -------
        function: Decorated function.
    """

    def exception_handler_decorator(func: Callable[[Any], Any]):
        @functools.wraps(func)
        async def wrapper(*args, **kwargs):
            try:
                return await func(*args, **kwargs)
            except Exception as e:
                resp = DefaultHandler.handle(
                    e,
                    func,
                    Response(response=EncounteredErrorResponse(message=str(e))),
                    app_id if app_id else None,
                )

                if not isinstance(e, ConnectorError):
                    for exception_class, handler, code in exception_classes:
                        if isinstance(e, exception_class) and handler:
                            if code:
                                resp.response.error_code = f"{app_id}.{code}" if app_id else code
                            else:
                                code = app_id if app_id else "lumos"

                            resp = handler.handle(e, func, resp, code)

                logger.error(f"{resp.response.error_code}: {resp.response.message}")
                return resp

        return wrapper

    return exception_handler_decorator
