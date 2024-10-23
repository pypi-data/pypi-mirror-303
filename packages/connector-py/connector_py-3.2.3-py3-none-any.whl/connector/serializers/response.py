import typing as t
from datetime import datetime

import pydantic

from connector.enums import (
    AccountStatus,
    ActivityEventType,
    CustomAttributeCustomizedType,
    CustomAttributeType,
)

ResponseData = t.TypeVar("ResponseData", bound=pydantic.BaseModel)


class PaginationData(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(extra="forbid")

    token: str
    size: int | None = None


class FoundAccountData(pydantic.BaseModel):
    integration_specific_id: str
    email: t.Optional[str] = None
    given_name: t.Optional[str] = None
    family_name: t.Optional[str] = None
    username: t.Optional[str] = None
    user_status: t.Optional[AccountStatus] = None
    extra_data: t.Optional[dict[str, t.Any]] = None
    custom_attributes: t.Optional[dict[str, str]] = None


class CustomAttributeSchema(pydantic.BaseModel):
    customized_type: CustomAttributeCustomizedType
    name: str
    attribute_type: CustomAttributeType


class FoundResourceData(pydantic.BaseModel):
    integration_specific_id: str
    label: str
    resource_type: str
    extra_data: t.Optional[dict[str, t.Any]] = None


class FoundEntitlementData(pydantic.BaseModel):
    integration_specific_id: str
    integration_specific_resource_id: str
    entitlement_type: str
    is_assignable: t.Optional[bool] = None
    label: t.Optional[str] = None
    extra_data: t.Optional[dict[str, t.Any]] = None


class FoundEntitlementAssociation(pydantic.BaseModel):
    integration_specific_entitlement_id: str
    account: FoundAccountData
    integration_specific_resource_id: str


class LastActivityData(pydantic.BaseModel):
    account_id: str
    event_type: ActivityEventType
    happened_at: datetime


class EncounteredErrorResponse(pydantic.BaseModel):
    message: str
    status_code: int | None = None
    error_code: str | None = None
    raised_by: str | None = None
    raised_in: str | None = None


class Response(pydantic.BaseModel, t.Generic[ResponseData]):
    response: ResponseData
    raw_data: dict[str, t.Any] | None = None
    page: PaginationData | None = None
    error: EncounteredErrorResponse | None = None

    @classmethod
    def from_response(
        cls,
        response: ResponseData,
        raw_data: dict[str, t.Any] | None,
        page: PaginationData | None = None,
    ) -> "Response":
        return cls(
            response=response,
            raw_data=raw_data,
            page=page,
            error=None,
        )

    @classmethod
    def from_error(cls, error: EncounteredErrorResponse) -> "Response":
        return cls(
            # TODO: this should be None in error case, but for backward compat we put it here, too
            response=error,  # type: ignore[arg-type]
            raw_data=None,
            page=None,
            error=error,
        )


class AssignEntitlementResponse(pydantic.BaseModel):
    assigned: bool


class FindEntitlementAssociationsResponse(pydantic.BaseModel):
    associations: list[FoundEntitlementAssociation]


class ListAccountsResponse(pydantic.BaseModel):
    accounts: list[FoundAccountData]


class ListEntitlementsResponse(pydantic.BaseModel):
    entitlements: list[FoundEntitlementData]


class ListResourcesResponse(pydantic.BaseModel):
    resources: list[FoundResourceData]


class ListCustomAttributesSchemaResponse(pydantic.BaseModel):
    schemas: list[CustomAttributeSchema]


class UnassignEntitlementResponse(pydantic.BaseModel):
    unassigned: bool


class ValidateCredentialsResponse(pydantic.BaseModel):
    valid: bool


class CreateAccountResponse(pydantic.BaseModel):
    """Result of account creation."""

    status: AccountStatus
    created: bool = pydantic.Field(
        deprecated="Attribute 'created' is deprecated, use 'status' instead.",
    )


class DeleteAccountResponse(pydantic.BaseModel):
    status: AccountStatus
    deleted: bool = pydantic.Field(
        deprecated="Attribute 'deleted' is deprecated, use 'status' instead.",
    )


class ActivateAccountResponse(pydantic.BaseModel):
    status: AccountStatus
    activated: bool = pydantic.Field(
        deprecated="Attribute 'activated' is deprecated, use 'status' instead.",
    )


class DeactivateAccountResponse(pydantic.BaseModel):
    status: AccountStatus
    deactivated: bool = pydantic.Field(
        deprecated="Attribute 'deactivated' is deprecated, use 'status' instead.",
    )


class GetLastActivityResponse(pydantic.BaseModel):
    activities: list[LastActivityData]
