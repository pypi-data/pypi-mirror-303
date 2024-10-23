import logging
from abc import abstractmethod
from enum import Enum
from typing import Any, Awaitable, Callable, List, Tuple, TypeAlias

from connector.serializers.lumos import EncounteredErrorResponse
from connector.serializers.request import ConnectorSettings, Request, RequestData
from connector.serializers.response import Response, ResponseData

CapabilityCallable: TypeAlias = (
    Callable[[Request[RequestData, ConnectorSettings]], Response[ResponseData]]
    | Callable[[Request[RequestData, ConnectorSettings]], Awaitable[Response[ResponseData]]]
)

LOGGER = logging.getLogger(__name__)


class ErrorCodes(str, Enum):
    """
    Error codes for Lumos connector.
    """

    NOT_FOUND = "not_found"
    INTERNAL_ERROR = "internal_error"
    API_ERROR = "api_error"
    UNAUTHORIZED = "unauthorized"
    BAD_REQUEST = "bad_request"
    PERMISSION_DENIED = "permission_denied"
    NOT_IMPLEMENTED = "not_implemented"
    UNEXPECTED = "unexpected_error"
    UNSUPPORTED = "unsupported_operation"
    UNKNOWN_PARAM = "unknown_parameter"
    UNKNOWN_VALUE = "unknown_value"
    INVALID_VALUE = "invalid_value"

    def __str__(self) -> str:
        return self.value


class ConnectorError(Exception):
    """
    Base exception class for Lumos connectors.
    Preferred way to raise exceptions inside the conenctors.
    `raise ConnectorError(message, error_code)`

    message: str (Custom error message)
    error_code: str | ErrorCodes (The actual error code, eg. "internal_error")
    """

    def __init__(self, message: str, error_code: str | ErrorCodes):
        self.error_code = error_code.value if isinstance(error_code, ErrorCodes) else error_code
        self.message = message


ExceptionHandlerCallable: TypeAlias = Callable[
    [
        Exception,
        (
            Callable[[Request[RequestData, ConnectorSettings]], Response[ResponseData]]
            | Callable[[Request[RequestData, ConnectorSettings]], Awaitable[Response[ResponseData]]]
        ),
        Response[ResponseData],
        str | ErrorCodes | None,
    ],
    Response[ResponseData],
]


class ExceptionHandler:
    """
    Abstract class for handling exceptions. You can subclass this to create your own exception handler.
    """

    def __init__(self):
        pass

    @staticmethod
    @abstractmethod
    def handle(
        e: Exception,
        original_func: Any,
        response: Response[EncounteredErrorResponse],
        error_code: str | ErrorCodes | None = None,
    ) -> Response[EncounteredErrorResponse]:
        """
        Handle an exception. (ErrorHandler signature typing)

        e: Exception (An exception that was raised)
        original_func: FunctionType (The original method that was called, eg. validate_credentials)
        response: ErrorResp (The output of the connector call)
        error_code: str | ErrorCodes | None (The actual error code, eg. "internal_error")
        """
        return response


class DefaultHandler(ExceptionHandler):
    """
    Default exception handler that handles the basic HTTPX/GQL extraction (etc.) and chains onto the global handler.
    These are operations that are always done on the raised error.
    """

    @staticmethod
    def handle(
        e: Exception,
        original_func: Any,
        response: Response[EncounteredErrorResponse],
        error_code: str | ErrorCodes | None = None,
    ) -> Response[EncounteredErrorResponse]:
        status_code: int | None = None

        # HTTPX HTTP Status code
        if hasattr(e, "response") and hasattr(e.response, "status_code"):
            status_code = e.response.status_code
        # GraphQL error code
        if hasattr(e, "code"):
            status_code = e.code

        # Populating some base info
        response.response.message = e.message if hasattr(e, "message") else str(e)
        response.response.status_code = status_code
        # TODO: add line number
        response.response.raised_in = f"{original_func.__module__}:{original_func.__name__}"
        response.response.raised_by = f"{e.__class__.__name__}"

        # ConnectorError already has an error code attached, so we need to chain
        if isinstance(e, ConnectorError):
            response.response.error_code = (
                f"{error_code}.{e.error_code}" if error_code else f"{e.error_code}"
            )
        else:
            # Otherwise, it is an unexpected error from an app_id
            response.response.error_code = (
                f"{error_code}.{ErrorCodes.UNEXPECTED}"
                if error_code
                else f"{ErrorCodes.UNEXPECTED}"
            )

        LOGGER.debug("Method %s failed", original_func.__name__, exc_info=True)
        return response


class HTTPHandler(ExceptionHandler):
    """
    Default exception handler for simple HTTP exceptions.
    If you want to handle more complicated exceptions, you can create your own instead.
    """

    @staticmethod
    def handle(
        e: Exception,
        original_func: Any,
        response: Response[EncounteredErrorResponse],
        error_code: str | ErrorCodes | None = None,
    ) -> Response[EncounteredErrorResponse]:
        if error_code:
            app_id = error_code.split(".")[0]
        else:
            app_id = "sdk"

        match response.response.status_code:
            case 400:
                response.response.error_code = f"{app_id}.{ErrorCodes.BAD_REQUEST}"
            case 401:
                response.response.error_code = f"{app_id}.{ErrorCodes.UNAUTHORIZED}"
            case 403:
                response.response.error_code = f"{app_id}.{ErrorCodes.PERMISSION_DENIED}"
            case 404:
                response.response.error_code = f"{app_id}.{ErrorCodes.NOT_FOUND}"
            case _:
                response.response.error_code = f"{app_id}.{ErrorCodes.API_ERROR}"

        return response


ErrorMap = List[Tuple[type[Exception], type[ExceptionHandler], str | ErrorCodes | None]]
