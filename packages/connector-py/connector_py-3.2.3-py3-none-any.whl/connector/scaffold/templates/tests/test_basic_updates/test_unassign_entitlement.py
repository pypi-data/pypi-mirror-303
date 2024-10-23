import json

import pytest
import pytest_cases
from connector.generated import (
    ErrorResponse,
    UnassignEntitlementRequest,
    UnassignEntitlementResponse,
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
        "tests.test_basic_updates.test_unassign_entitlement_cases",
    ],
)
async def test_validate_unassign_entitlement(
    httpx_async_client: ClientContextManager,
    args: UnassignEntitlementRequest,
    response_body_map: ResponseBodyMap,
    expected_response: UnassignEntitlementResponse | ErrorResponse,
) -> None:
    """Test ``unassign-entitlement`` operation."""
    with httpx_async_client(get_oauth(args).access_token, response_body_map):
        response = await integration.dispatch(CapabilityName.UNASSIGN_ENTITLEMENT, args.model_dump_json())

    assert json.loads(response) == expected_response.model_dump()
