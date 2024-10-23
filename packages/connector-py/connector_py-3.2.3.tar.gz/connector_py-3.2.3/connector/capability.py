"""Utilities for describing capabilities.

Each known capability is assigned a base class for request and response.
The actual request and response types in a integration implementation
can either use the base classes directly or create subclasses, however,
those bases are enforced to be used.
"""

import enum
import inspect
import json
import typing as t

from connector.generated import (
    AuthorizationUrl,
    GetAuthorizationUrl,
    HandleAuthorizationCallback,
    OauthCredentials as GenOauthCredentials,
    RefreshAccessToken,
)
from connector.serializers.abstract import CommandTypes
from connector.serializers.request import (
    ActivateAccountRequest,
    AssignEntitlementRequest,
    ConnectorSettings,
    CreateAccountRequest,
    DeactivateAccountRequest,
    DeleteAccountRequest,
    FindEntitlementAssociationsRequest,
    GetLastActivityRequest,
    ListAccountsRequest,
    ListCustomAttributesSchemaRequest,
    ListEntitlementsRequest,
    ListResourcesRequest,
    Request,
    RequestData,
    UnassignEntitlementRequest,
    ValidateCredentialsRequest,
)
from connector.serializers.response import (
    ActivateAccountResponse,
    AssignEntitlementResponse,
    CreateAccountResponse,
    DeactivateAccountResponse,
    DeleteAccountResponse,
    FindEntitlementAssociationsResponse,
    GetLastActivityResponse,
    ListAccountsResponse,
    ListCustomAttributesSchemaResponse,
    ListEntitlementsResponse,
    ListResourcesResponse,
    Response,
    ResponseData,
    UnassignEntitlementResponse,
    ValidateCredentialsResponse,
)


class CapabilityName(str, enum.Enum):
    """Enumeration of known capabilities."""

    ACTIVATE_ACCOUNT = "activate_account"
    ASSIGN_ENTITLEMENT = "assign-entitlement"
    CREATE_ACCOUNT = "create_account"
    DEACTIVATE_ACCOUNT = "deactivate_account"
    DELETE_ACCOUNT = "delete_account"
    FIND_ENTITLEMENT_ASSOCIATIONS = "find-entitlement-associations"
    GET_LAST_ACTIVITY = "get-last-activity"
    GET_AUTHORIZATION_URL = "get_authorization_url"
    LIST_ACCOUNTS = "list-accounts"
    HANDLE_AUTHORIZATION_CALLBACK = "handle_authorization_callback"
    LIST_CUSTOM_ATTRIBUTES_SCHEMA = "list-custom-attributes-schema"
    LIST_ENTITLEMENTS = "list-entitlements"
    LIST_RESOURCES = "list-resources"
    REFRESH_ACCESS_TOKEN = "refresh_access_token"
    UNASSIGN_ENTITLEMENT = "unassign-entitlement"
    VALIDATE_CREDENTIALS = "validate-credentials"


CAPABILITY_REQUEST_BASES = {
    CapabilityName.ACTIVATE_ACCOUNT: ActivateAccountRequest,
    CapabilityName.ASSIGN_ENTITLEMENT: AssignEntitlementRequest,
    CapabilityName.CREATE_ACCOUNT: CreateAccountRequest,
    CapabilityName.DEACTIVATE_ACCOUNT: DeactivateAccountRequest,
    CapabilityName.DELETE_ACCOUNT: DeleteAccountRequest,
    CapabilityName.FIND_ENTITLEMENT_ASSOCIATIONS: FindEntitlementAssociationsRequest,
    CapabilityName.GET_AUTHORIZATION_URL: GetAuthorizationUrl,
    CapabilityName.GET_LAST_ACTIVITY: GetLastActivityRequest,
    CapabilityName.HANDLE_AUTHORIZATION_CALLBACK: HandleAuthorizationCallback,
    CapabilityName.LIST_ACCOUNTS: ListAccountsRequest,
    CapabilityName.LIST_CUSTOM_ATTRIBUTES_SCHEMA: ListCustomAttributesSchemaRequest,
    CapabilityName.LIST_ENTITLEMENTS: ListEntitlementsRequest,
    CapabilityName.LIST_RESOURCES: ListResourcesRequest,
    CapabilityName.REFRESH_ACCESS_TOKEN: RefreshAccessToken,
    CapabilityName.UNASSIGN_ENTITLEMENT: UnassignEntitlementRequest,
    CapabilityName.VALIDATE_CREDENTIALS: ValidateCredentialsRequest,
}
CAPABILITY_RESPONSE_BASES = {
    CapabilityName.ACTIVATE_ACCOUNT: ActivateAccountResponse,
    CapabilityName.ASSIGN_ENTITLEMENT: AssignEntitlementResponse,
    CapabilityName.CREATE_ACCOUNT: CreateAccountResponse,
    CapabilityName.DEACTIVATE_ACCOUNT: DeactivateAccountResponse,
    CapabilityName.DELETE_ACCOUNT: DeleteAccountResponse,
    CapabilityName.FIND_ENTITLEMENT_ASSOCIATIONS: FindEntitlementAssociationsResponse,
    CapabilityName.GET_AUTHORIZATION_URL: AuthorizationUrl,
    CapabilityName.GET_LAST_ACTIVITY: GetLastActivityResponse,
    CapabilityName.HANDLE_AUTHORIZATION_CALLBACK: GenOauthCredentials,
    CapabilityName.LIST_ACCOUNTS: ListAccountsResponse,
    CapabilityName.LIST_CUSTOM_ATTRIBUTES_SCHEMA: ListCustomAttributesSchemaResponse,
    CapabilityName.LIST_ENTITLEMENTS: ListEntitlementsResponse,
    CapabilityName.LIST_RESOURCES: ListResourcesResponse,
    CapabilityName.REFRESH_ACCESS_TOKEN: GenOauthCredentials,
    CapabilityName.UNASSIGN_ENTITLEMENT: UnassignEntitlementResponse,
    CapabilityName.VALIDATE_CREDENTIALS: ValidateCredentialsResponse,
}


def generate_capability_schema(
    capability_name: str,
    capability: (
        t.Callable[[Request[RequestData, ConnectorSettings]], Response[ResponseData]]
        | t.Callable[[Request[RequestData, ConnectorSettings]], t.Awaitable[Response[ResponseData]]]
    ),
) -> CommandTypes:
    request_annotation, response_annotation = get_capability_annotations(capability)
    return CommandTypes(
        argument=json.dumps(request_annotation.model_json_schema(), sort_keys=True),
        output=json.dumps(response_annotation.model_json_schema(), sort_keys=True),
    )


def get_capability_annotations(
    capability: (
        t.Callable[[Request[RequestData, ConnectorSettings]], Response[ResponseData]]
        | t.Callable[[Request[RequestData, ConnectorSettings]], t.Awaitable[Response[ResponseData]]]
    ),
) -> tuple[type[Request[RequestData, ConnectorSettings]], type[Response[ResponseData]]]:
    """Extract argument and return type annotations."""
    annotations = inspect.get_annotations(capability)
    try:
        response_annotation = annotations["return"]
        request_annotation_name = (set(annotations.keys()) - {"return"}).pop()
    except KeyError:
        raise TypeError(
            f"The capability function {capability.__name__} must have both request and return annotations."
        ) from None

    request_annotation = annotations[request_annotation_name]
    return request_annotation, response_annotation


def validate_capability(
    name: CapabilityName,
    capability: (
        t.Callable[[Request[RequestData, ConnectorSettings]], Response[ResponseData]]
        | t.Callable[[Request[RequestData, ConnectorSettings]], t.Awaitable[Response[ResponseData]]]
    ),
) -> None:
    """Make sure copability implementation is valid.

    Capability is marked as valid when:
        * is fully annotated, i.e., both argument and return value are
        type-hinted
        * type of accepted argument matches the expected one, i.e., is
        exactly the same class or a subclass
        * type of returned value matches the expected one, same
        mechanism as for argument
    """
    request_annotation, response_annotation = get_capability_annotations(capability)
    expected_response_model = CAPABILITY_RESPONSE_BASES[name]
    actual_response_model = t.cast(
        type[ResponseData],
        response_annotation.model_fields["response"].annotation,
    )
    if actual_response_model != expected_response_model:
        raise TypeError(
            f"The function {capability.__name__} for capability {name} must return {expected_response_model.__name__}. "
            f"Actual response model: {actual_response_model.__name__}"
        ) from None

    expected_request_model = CAPABILITY_REQUEST_BASES[name]
    actual_request_model = t.cast(
        type[RequestData],
        request_annotation.model_fields["request"].annotation,
    )
    if not issubclass(actual_request_model, expected_request_model):
        raise TypeError(
            f"The function {capability.__name__} for capability {name} must accept {expected_request_model.__name__} "
            f"or its subclass. Actual request model: {actual_request_model.__name__}"
        ) from None
