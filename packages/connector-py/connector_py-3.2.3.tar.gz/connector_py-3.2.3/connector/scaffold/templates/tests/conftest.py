import contextlib
import typing as t
from unittest.mock import patch

import httpx
import pytest
from connector.generated import (
    AuthCredential,
    OAuthCredential,
)

from tests.type_definitions import ClientContextManager, MockedResponse, ResponseBodyMap
from {name}.auth import Auth
from {name}.integration import BASE_URL
from {name}.serializers.request import {pascal}Settings

from tests.type_definitions import ClientContextManager, MockedResponse, ResponseBodyMap

VALID_AUTH = AuthCredential(
    oauth=OAuthCredential(access_token="valid"),  # noqa: S105
)
INVALID_AUTH = AuthCredential(
    oauth=OAuthCredential(access_token="invalid"),  # noqa: S105
)

# We dump this to a plain ol dict because that's how we expect
# to deserialize it in handlers
SETTINGS = {pascal}Settings(account_id="test-account-id").model_dump()


@pytest.fixture(name="httpx_async_client")
def fixture_httpx_async_client() -> ClientContextManager:
    @contextlib.contextmanager
    def factory(token: str, response_body_map: ResponseBodyMap) -> t.Iterator[None]:
        def handler(request: httpx.Request) -> httpx.Response:
            full_path = f"{{request.url.path}}?{{request.url.params!s}}".rstrip("?")  # fix f-string
            response_body = response_body_map[request.method][full_path]
            match response_body:
                case MockedResponse(status_code, None):
                    return httpx.Response(status_code)
                case MockedResponse(status_code, body):
                    return httpx.Response(status_code, json=body)

        with patch("{name}.integration.build_client") as mocked_build_client:
            mocked_build_client.return_value = httpx.AsyncClient(
                base_url=BASE_URL,
                auth=Auth(token),
                transport=httpx.MockTransport(handler),
            )
            yield

    return factory
