import pytest
import pytest_cases
from connector.generated import (
    GetLastActivityRequest,
    GetLastActivityResponse,
)
from connector.oai.capability import CapabilityName, get_oauth
from {name}.integration import integration

from tests.type_definitions import ClientContextManager, ResponseBodyMap

@pytest.mark.skip(
    reason="Function not implemented yet, remove after implementation of tested function."
)
@pytest_cases.parametrize_with_cases(
    ["args", "response_body_map", "expected_response"],
    cases=[
        "tests.test_get_last_activity.test_get_last_activity_cases",
    ],
)
async def test_get_last_activity(
    httpx_async_client: ClientContextManager,
    args: GetLastActivityRequest,
    response_body_map: ResponseBodyMap,
    expected_response: GetLastActivityResponse,
) -> None:
    with httpx_async_client(get_oauth(args).access_token, response_body_map):
        response = await integration.dispatch(CapabilityName.GET_LAST_ACTIVITY, args.model_dump_json())

    assert response == expected_response.model_dump_json()
