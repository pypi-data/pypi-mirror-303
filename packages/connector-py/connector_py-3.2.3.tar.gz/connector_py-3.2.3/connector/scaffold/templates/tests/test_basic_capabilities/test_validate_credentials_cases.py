"""Cases for testing ``validate_credentials`` operation."""

import typing as t

import httpx
from connector.generated import (
    Error,
    ErrorCode,
    ErrorResponse,
    ValidateCredentials,
    ValidateCredentialsRequest,
    ValidateCredentialsResponse,
    ValidatedCredentials,
)
from connector.utils.test import http_error_message
from {name}.integration import BASE_URL

from tests.conftest import INVALID_AUTH, SETTINGS, VALID_AUTH
from tests.type_definitions import MockedResponse, ResponseBodyMap

Case: t.TypeAlias = tuple[
    ValidateCredentialsRequest,
    ResponseBodyMap,
    ValidateCredentialsResponse | ErrorResponse,
]


def case_validate_credentials_200() -> Case:
    """Successful request."""
    args = ValidateCredentialsRequest(
        request=ValidateCredentials(),
        auth=VALID_AUTH,
        settings=SETTINGS,
    )
    response_body_map = {{
        "GET": {{
            "/users?limit=1": MockedResponse(
                status_code=httpx.codes.OK,
                response_body={{}},
            )
        }}
    }}
    expected_response = ValidateCredentialsResponse(
        response=ValidatedCredentials(valid=True, unique_tenant_id="test-account-id"),
        raw_data=None,
    )
    return args, response_body_map, expected_response
