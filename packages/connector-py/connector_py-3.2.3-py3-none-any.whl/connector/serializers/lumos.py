from datetime import datetime
from enum import Enum
from typing import Any, Dict, Generic, NewType, Optional, TypeVar

from pydantic import BaseModel, ConfigDict, Field

from connector.enums import AccountStatus
from connector.shared_types import OptionalRawDataType

NextPageTokenType = NewType("NextPageTokenType", str)


class AccountType(str, Enum):
    SERVICE_ACCOUNT = "SERVICE_ACCOUNT"


class FoundAccountData(BaseModel):
    integration_specific_id: str
    email: Optional[str] = None
    given_name: Optional[str] = None
    family_name: Optional[str] = None
    username: Optional[str] = None
    user_status: Optional[AccountStatus] = None
    extra_data: Optional[Dict[str, Any]] = None
    custom_attributes: Optional[Dict[str, str]] = None
    account_type: Optional[AccountType] = None


class CustomAttributeType(str, Enum):
    """Indicates the type of the attribute"""

    STRING = "STRING"
    USER = "USER"


class CustomAttributeCustomizedType(str, Enum):
    """Indicates the type of the entity that would own the attribue"""

    ACCOUNT = "ACCOUNT"
    ENTITLEMENMT = "ENTITLEMENT"
    RESOURCE = "RESOURCE"


class CustomAttributeSchema(BaseModel):
    customized_type: CustomAttributeCustomizedType
    name: str
    attribute_type: CustomAttributeType


class FoundResourceData(BaseModel):
    integration_specific_id: str
    label: str
    resource_type: str
    extra_data: Optional[Dict[str, Any]] = None


class FoundEntitlementData(BaseModel):
    integration_specific_id: str
    integration_specific_resource_id: str
    entitlement_type: str
    is_assignable: Optional[bool] = None
    label: Optional[str] = None
    extra_data: Optional[Dict[str, Any]] = None


class FoundEntitlementAssociation(BaseModel):
    integration_specific_entitlement_id: str
    account: FoundAccountData
    integration_specific_resource_id: str


class EncounteredErrorResponse(BaseModel):
    message: str
    status_code: Optional[int] = None
    error_code: Optional[str] = None
    raised_by: Optional[str] = None
    raised_in: Optional[str] = None

    model_config = ConfigDict(
        arbitrary_types_allowed=True,
    )


Response = TypeVar("Response")


class PageCursor(BaseModel):
    next: NextPageTokenType | None


class PaginationPageArgs(BaseModel):
    """Schema of request page parameters."""

    model_config = ConfigDict(extra="forbid")

    token: NextPageTokenType | None = Field(
        default=None,
        description=(
            "Next page token returned from previous method call in ``page.token``. The value of the next page token is "
            "opaque to the caller and should not be modified by any means."
        ),
    )
    size: int | None = Field(
        default=None,
        gt=0,
        description="Prefered size of result page. Connector can decrease the requested size if needed.",
    )


class PaginationPageResp(BaseModel):
    """Schema of request page parameters."""

    model_config = ConfigDict(extra="forbid")

    token: NextPageTokenType = Field(
        default=None,
        description=(
            "Next page token returned from previous method call in ``page.token``. The value of the next page token is "
            "opaque to the caller and should not be modified by any means."
        ),
    )
    size: int | None = Field(
        default=None,
        gt=0,
        description="Prefered size of result page. Connector can decrease the requested size if needed.",
    )


class PaginationArgs(BaseModel):
    """Definition of pagination schema for requests.

    To add pagination support to your request schema, simply inherit
    from this class, e.g.: ::

        class ListUserArgs(PaginationArgs, DefaultListUserArgs):
            pass
    """

    page: PaginationPageArgs | None = None

    @property
    def pagination_token(self) -> NextPageTokenType | None:
        if self.page is None:
            return None

        return self.page.token

    @property
    def pagination_size(self) -> int | None:
        if self.page is None:
            return None

        return self.page.size


class ResponseWrapper(BaseModel, Generic[Response]):
    response: Response
    raw_data: OptionalRawDataType = None
    cursor: PageCursor | None = Field(
        default=None,
        deprecated="cursor attribute is deprecated, use `page` instead",
    )
    page: PaginationPageResp | None = None


class BaseArgs(BaseModel):
    include_raw_data: bool = Field(default=False)


class ListAccountsArgsBase(BaseArgs):
    custom_attributes: Optional[list[str]] = Field(None)


class ListCustomAttributesSchemaArgsBase(BaseArgs):
    pass


class ListCustomAttributesSchemaResp(ResponseWrapper[list[CustomAttributeSchema]]):
    pass


class ListAccountsResp(ResponseWrapper[list[FoundAccountData]]):
    pass


class ValidateCredentialsArgsBase(BaseArgs):
    pass


class ValidateCredentialsResp(ResponseWrapper[bool]):
    pass


class GetAccountArgsBase(BaseArgs):
    pass


class GetAccountResp(ResponseWrapper[FoundAccountData]):
    pass


class ListResourcesArgsBase(BaseArgs):
    resource_type: str


class ListResourcesResp(ResponseWrapper[list[FoundResourceData]]):
    pass


class GetResourceArgsBase(BaseArgs):
    resource_type: str
    integration_specific_id: str


class GetResourceResp(ResponseWrapper[FoundResourceData]):
    pass


class ListEntitlementsArgsBase(BaseArgs):
    resource_type: str
    resource_integration_specific_id: str


class ListEntitlementsResp(ResponseWrapper[list[FoundEntitlementData]]):
    pass


class FindEntitlementAssociationsArgsBase(BaseArgs, PaginationArgs):
    pass


class FindEntitlementAssociationsResp(ResponseWrapper[list[FoundEntitlementAssociation]]):
    pass


class AssignEntitlementArgsBase(BaseArgs):
    account: FoundAccountData
    entitlement: FoundEntitlementData


class AssignEntitlementResp(ResponseWrapper[bool]):
    pass


class UnassignEntitlementArgsBase(BaseArgs):
    account: FoundAccountData
    entitlement: FoundEntitlementData


class UnassignEntitlementResp(ResponseWrapper[bool]):
    pass


class CreateAccount(BaseModel):
    email: str | None = None
    username: str | None = None
    given_name: str | None = None
    family_name: str | None = None
    user_status: str | None = None
    extra_data: Dict[str, Any] | None = None


class CreateAccountArgsBase(BaseArgs):
    account: CreateAccount
    entitlements: list[FoundEntitlementData]


class CreateAccountResp(ResponseWrapper[bool]):
    pass


class DeleteAccountArgsBase(BaseArgs):
    account_id: str


class DeleteAccountResp(ResponseWrapper[bool]):
    pass


class ActivateAccountArgsBase(BaseArgs):
    account_id: str


class ActivateAccountResp(ResponseWrapper[bool]):
    pass


class DeactivateAccountArgsBase(BaseArgs):
    account_id: str


class DeactivateAccountResp(ResponseWrapper[bool]):
    pass


class LastActivityData(BaseModel):
    account_id: str
    event_type: str
    happened_at: datetime


class GetLastActivityArgsBase(BaseArgs):
    account_ids: list[str]


class GetLastActivityResp(ResponseWrapper[list[LastActivityData]]):
    pass


class ErrorResp(ResponseWrapper[EncounteredErrorResponse]):
    error: bool = True
    pass
