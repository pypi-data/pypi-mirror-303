import json

import pytest
import pytest_cases
from connector.generated import (
    ListEntitlementsRequest,
    ListEntitlementsResponse,
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
        "tests.test_basic_object_read.test_list_entitlements_cases",
    ],
)
async def test_list_entitlements(
    httpx_async_client: ClientContextManager,
    args: ListEntitlementsRequest,
    response_body_map: ResponseBodyMap,
    expected_response: ListEntitlementsResponse,
) -> None:
    with httpx_async_client(get_oauth(args).access_token, response_body_map):
        response = await integration.dispatch(CapabilityName.LIST_ENTITLEMENTS, args.model_dump_json())

    assert json.loads(response) == expected_response.model_dump()
