import json

import pytest
import pytest_cases
from connector.generated import (
    ErrorResponse,
    FindEntitlementAssociationsRequest,
    FindEntitlementAssociationsResponse,
)
from connector.oai.capability import CapabilityName, get_oauth
from {name}.integration import integration

from tests.conftest import ClientContextManager, ResponseBodyMap


@pytest.mark.skip(
    reason="Function not implemented yet, remove after implementation of tested function."
)
@pytest_cases.parametrize_with_cases(
    ["args", "response_body_map", "expected_response"],
    cases=[
        "tests.test_basic_object_association.test_find_entitlement_association_cases",
    ],
)
async def test_find_entitlement_association(
    httpx_async_client: ClientContextManager,
    args: FindEntitlementAssociationsRequest,
    response_body_map: ResponseBodyMap,
    expected_response: FindEntitlementAssociationsResponse | ErrorResponse,
) -> None:
    """Test ``find_entitlement_associations`` operation."""
    with httpx_async_client(get_oauth(args).access_token, response_body_map):
        response = await integration.dispatch(
            CapabilityName.FIND_ENTITLEMENT_ASSOCIATIONS, args.model_dump_json()
        )

    assert json.loads(response) == expected_response.model_dump()
