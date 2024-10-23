import json

import pytest_cases
from connector.generated import (
    ErrorResponse,
    ValidateCredentialsRequest,
    ValidateCredentialsResponse,
)
from connector.oai.capability import CapabilityName, get_oauth
from {name}.integration import integration

from tests.type_definitions import ClientContextManager, ResponseBodyMap


@pytest_cases.parametrize_with_cases(
    ["args", "response_body_map", "expected_response"],
    cases=[
        "tests.test_basic_capabilities.test_validate_credentials_cases",
    ],
)
async def test_validate_credentials(
    httpx_async_client: ClientContextManager,
    args: ValidateCredentialsRequest,
    response_body_map: ResponseBodyMap,
    expected_response: ValidateCredentialsResponse | ErrorResponse,
) -> None:
    with httpx_async_client(get_oauth(args).access_token, response_body_map):
        response = await integration.dispatch(CapabilityName.VALIDATE_CREDENTIALS, args.model_dump_json())

    assert json.loads(response) == expected_response.model_dump()
