import typing as t
from enum import Enum

import pydantic


class ConnectorSettingsBase(pydantic.BaseModel):
    """
    Base class for connector settings that are applicable across all capabilities.
    These settings are configured by users during the connector setup process in Lumos.
    """

    pass


# TODO: use `RequestDataBase` which will forbid extra parameters
RequestData = t.TypeVar("RequestData", bound=pydantic.BaseModel)
ConnectorSettings = t.TypeVar("ConnectorSettings", bound=ConnectorSettingsBase | None)


class FieldType(str, Enum):
    SECRET = "SECRET"
    HIDDEN = "HIDDEN"
    MULTI_LINES = "MULTI_LINES"


def _extract_json_schema_extra(**kwargs) -> dict[str, t.Any]:
    json_schema_extra = (
        kwargs.pop("json_schema_extra") if "json_schema_extra" in kwargs else {}
    ) or {}
    return json_schema_extra


def SecretField(*args, **kwargs):
    json_schema_extra = _extract_json_schema_extra(**kwargs)
    json_schema_extra["x-field_type"] = FieldType.SECRET
    return pydantic.Field(*args, json_schema_extra=json_schema_extra, **kwargs)


def HiddenField(*args, **kwargs):
    """
    A field we don't want a user to see + fill out, but not a secret.
    """
    json_schema_extra = _extract_json_schema_extra(**kwargs)
    json_schema_extra["x-field_type"] = FieldType.HIDDEN
    return pydantic.Field(*args, json_schema_extra=json_schema_extra, **kwargs)


def MultiLinesField(*args, **kwargs):
    json_schema_extra = _extract_json_schema_extra(**kwargs)
    json_schema_extra["x-field_type"] = FieldType.MULTI_LINES
    return pydantic.Field(*args, json_schema_extra=json_schema_extra, **kwargs)


class AuthModelName(str, Enum):
    OAUTH = "oauth"
    BASIC = "basic"


class AuthModel(pydantic.BaseModel):
    model: AuthModelName


class OAuthCredentials(AuthModel):
    model: t.Literal[AuthModelName.OAUTH] = HiddenField(
        default=AuthModelName.OAUTH,
    )
    access_token: str = pydantic.Field(title="Access Token", description="OAuth access token")
    refresh_token: str | None = pydantic.Field(
        title="Refresh Token", description="OAuth refresh token", default=None
    )
    scope: str | None = pydantic.Field(title="Scope", description="OAuth scopes", default=None)
    # Potentially URLs


class BasicCredentials(AuthModel):
    model: t.Literal[AuthModelName.BASIC] = HiddenField(
        default=AuthModelName.BASIC,
    )
    username: str = pydantic.Field(title="Username", description="Username")
    password: str = SecretField(title="Password", description="Password")


class PaginationArgs(pydantic.BaseModel):
    token: str | None = None
    size: int | None = None


class Request(pydantic.BaseModel, t.Generic[RequestData, ConnectorSettings]):
    request: RequestData
    settings: ConnectorSettings = pydantic.Field(default=None)
    auth: OAuthCredentials | BasicCredentials = pydantic.Field(discriminator="model")
    page: PaginationArgs | None = None
    include_raw_data: bool = False
    request_id: str | None = None

    @property
    def pagination_token(self) -> str | None:
        if self.page is None:
            return None

        return self.page.token

    @property
    def pagination_size(self) -> int | None:
        if self.page is None:
            return None

        return self.page.size

    def get_oauth(self) -> OAuthCredentials:
        if self.auth.model == AuthModelName.OAUTH:
            return self.auth
        raise ValueError(f"Invalid authentication schema: {self.auth.model}")

    def get_basic_auth(self) -> BasicCredentials:
        if self.auth.model == AuthModelName.BASIC:
            return self.auth
        raise ValueError(f"Invalid authentication schema: {self.auth.model}")

    def get_arg(self, key: str) -> t.Any:
        return getattr(self.request, key)


class ListAccountsRequest(pydantic.BaseModel):
    custom_attributes: list[str] | None = None


class ListCustomAttributesSchemaRequest(pydantic.BaseModel):
    pass


class ValidateCredentialsRequest(pydantic.BaseModel):
    pass


class ListResourcesRequest(pydantic.BaseModel):
    resource_type: str


class ListEntitlementsRequest(pydantic.BaseModel):
    resource_type: str
    resource_integration_specific_id: str


class FindEntitlementAssociationsRequest(pydantic.BaseModel):
    pass


class AssignEntitlementRequest(pydantic.BaseModel):
    account_integration_specific_id: str
    resource_integration_specific_id: str
    resource_type: str
    entitlement_integration_specific_id: str
    entitlement_type: str


class UnassignEntitlementRequest(pydantic.BaseModel):
    account_integration_specific_id: str
    resource_integration_specific_id: str
    resource_type: str
    entitlement_integration_specific_id: str
    entitlement_type: str


class CreateAccount(pydantic.BaseModel):
    email: str | None = None
    username: str | None = None
    given_name: str | None = None
    family_name: str | None = None
    user_status: str | None = None
    extra_data: dict[str, t.Any] | None = None


class CreateAccountEntitlement(pydantic.BaseModel):
    integration_specific_id: str
    integration_specific_resource_id: str | None = None
    entitlement_type: str
    is_assignable: bool | None = None
    label: str | None = None
    extra_data: dict[str, t.Any] | None = None


class CreateAccountRequest(pydantic.BaseModel):
    account: CreateAccount
    entitlements: t.Sequence[CreateAccountEntitlement]


class DeleteAccountRequest(pydantic.BaseModel):
    account_id: str


class ActivateAccountRequest(pydantic.BaseModel):
    account_id: str


class DeactivateAccountRequest(pydantic.BaseModel):
    account_id: str


class GetLastActivityRequest(pydantic.BaseModel):
    account_ids: list[str]
