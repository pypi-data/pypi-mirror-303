from typing import TypeAlias

import httpx
from connector.generated import (
    ActivateAccountRequest,
    ActivateAccountResponse,
    AssignEntitlementRequest,
    AssignEntitlementResponse,
    CreateAccountRequest,
    CreateAccountResponse,
    DeactivateAccountRequest,
    DeactivateAccountResponse,
    DeleteAccountRequest,
    DeleteAccountResponse,
    FindEntitlementAssociationsRequest,
    FindEntitlementAssociationsResponse,
    FoundAccountData,
    GetLastActivityRequest,
    GetLastActivityResponse,
    ListAccountsRequest,
    ListAccountsResponse,
    ListCustomAttributesSchemaRequest,
    ListCustomAttributesSchemaResponse,
    ListEntitlementsRequest,
    ListEntitlementsResponse,
    ListResourcesRequest,
    ListResourcesResponse,
    OAuthCredential,
    Page,
    UnassignEntitlementRequest,
    UnassignEntitlementResponse,
    ValidateCredentialsRequest,
    ValidateCredentialsResponse,
    ValidatedCredentials,
)
from connector.oai.capability import CapabilityName, get_oauth, get_page, get_settings
from connector.oai.errors import HTTPHandler
from connector.oai.integration import DescriptionData, Integration

from {name}.auth import Auth
from {name}.serializers.pagination import DEFAULT_PAGE_SIZE, NextPageToken, Pagination
from {name}.serializers.request import {pascal}Settings

BASE_URL = "https://scaffold.com"

RequestData: TypeAlias = (
    ActivateAccountRequest
    | AssignEntitlementRequest
    | CreateAccountRequest
    | DeactivateAccountRequest
    | DeleteAccountRequest
    | FindEntitlementAssociationsRequest
    | GetLastActivityRequest
    | ListAccountsRequest
    | ListCustomAttributesSchemaRequest
    | ListEntitlementsRequest
    | ListResourcesRequest
    | UnassignEntitlementRequest
    | ValidateCredentialsRequest
)


def build_client(request: RequestData) -> httpx.AsyncClient:
    """Prepare client context manager for calling {title} API."""
    return httpx.AsyncClient(
        auth=Auth(access_token=get_oauth(request).access_token),
        base_url=BASE_URL,
    )


integration = Integration(
    app_id="{hyphenated_name}",
    auth=OAuthCredential,
    exception_handlers=[
        (httpx.HTTPStatusError, HTTPHandler, None),
    ],
    description_data=DescriptionData(
        logo_url="", user_friendly_name="{pascal}", description="", categories=[]
    ),
    settings_model={pascal}Settings,
)


@integration.register_capability(CapabilityName.VALIDATE_CREDENTIALS)
async def validate_credentials(
    args: ValidateCredentialsRequest,
) -> ValidateCredentialsResponse:
    settings = get_settings(args, {pascal}Settings)
    async with build_client(args) as client:
        r = await client.get("/users", params={{"limit": 1}})
        r.raise_for_status()
        data = r.json()

    return ValidateCredentialsResponse(
        response=ValidatedCredentials(
            unique_tenant_id=settings.account_id,
            valid=True,
        ),
        raw_data={{
            f"{{BASE_URL}}/users?limit=1": data,
        }}
        if args.include_raw_data
        else None,
    )


@integration.register_capability(CapabilityName.LIST_ACCOUNTS)
async def list_accounts(args: ListAccountsRequest) -> ListAccountsResponse:
    endpoint = "/users"
    try:
        current_pagination = NextPageToken(get_page(args).token).paginations()[0]
    except IndexError:
        current_pagination = Pagination.default(endpoint)

    page_size = get_page(args).size or DEFAULT_PAGE_SIZE
    async with build_client(args) as client:
        r = await client.get(
            endpoint,
            params={{"limit": page_size, "offset": current_pagination.offset}},
        )
        r.raise_for_status()
        data = r.json()
        accounts: list[FoundAccountData] = []

        if True:
            next_pagination = [
                Pagination(
                    endpoint=endpoint,
                    offset=current_pagination.offset + len(accounts),
                )
            ]
        else:
            next_pagination = []

        next_page_token = NextPageToken.from_paginations(next_pagination).token

    return ListAccountsResponse(
        response=accounts,
        raw_data={{
            f"{{BASE_URL}}/users?limit=1": data,
        }}
        if args.include_raw_data
        else None,
        page=Page(
            token=next_page_token,
            size=page_size,
        )
        if next_page_token
        else None,
    )


# @integration.register_capability(CapabilityName.LIST_RESOURCES)
async def list_resources(args: ListResourcesRequest) -> ListResourcesResponse:
    raise NotImplementedError


# @integration.register_capability(CapabilityName.LIST_ENTITLEMENTS)
async def list_entitlements(
    args: ListEntitlementsRequest,
) -> ListEntitlementsResponse:
    raise NotImplementedError


# @integration.register_capability(CapabilityName.FIND_ENTITLEMENT_ASSOCIATIONS)
async def find_entitlement_associations(
    args: FindEntitlementAssociationsRequest,
) -> FindEntitlementAssociationsResponse:
    raise NotImplementedError


#@integration.register_capability(CapabilityName.GET_LAST_ACTIVITY)
async def get_last_activity(args: GetLastActivityRequest) -> GetLastActivityResponse:
    raise NotImplementedError


# @integration.register_capability(CapabilityName.ASSIGN_ENTITLEMENT)
async def assign_entitlement(args: AssignEntitlementRequest) -> AssignEntitlementResponse:
    raise NotImplementedError


# @integration.register_capability(CapabilityName.UNASSIGN_ENTITLEMENT)
async def unassign_entitlement(
    args: UnassignEntitlementRequest,
) -> UnassignEntitlementResponse:
    raise NotImplementedError


# @integration.register_capability(CapabilityName.LIST_CUSTOM_ATTRIBUTES_SCHEMA)
async def list_custom_attributes_schema(
    args: ListCustomAttributesSchemaRequest,
) -> ListCustomAttributesSchemaResponse:
    raise NotImplementedError


# @integration.register_capability(CapabilityName.CREATE_ACCOUNT)
async def create_account(
    args: CreateAccountRequest,
) -> CreateAccountResponse:
    raise NotImplementedError


# @integration.register_capability(CapabilityName.DELETE_ACCOUNT)
async def delete_account(
    args: DeleteAccountRequest,
) -> DeleteAccountResponse:
    raise NotImplementedError


# @integration.register_capability(CapabilityName.ACTIVATE_ACCOUNT)
async def activate_account(
    args: ActivateAccountRequest,
) -> ActivateAccountResponse:
    raise NotImplementedError


# @integration.register_capability(CapabilityName.DEACTIVATE_ACCOUNT)
async def deactivate_account(
    args: DeactivateAccountRequest,
) -> DeactivateAccountResponse:
    raise NotImplementedError
