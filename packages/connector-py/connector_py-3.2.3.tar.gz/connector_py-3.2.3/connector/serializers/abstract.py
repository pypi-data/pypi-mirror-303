import typing as t
from enum import Enum

from pydantic import BaseModel, Field, Json


class EmptyModel(BaseModel):
    pass


class CommandTypes(BaseModel):
    argument: Json[t.Any] = Field(..., description="OpenAPI Component")
    output: Json[t.Any] = Field(..., description="OpenAPI Component")


class AppCategory(str, Enum):
    HR_AND_LEARNING = "HR_AND_LEARNING"
    OFFICE_AND_LEGAL = "OFFICE_AND_LEGAL"
    SALES_AND_SUPPORT = "SALES_AND_SUPPORT"
    COMMERCE_AND_MARKETPLACES = "COMMERCE_AND_MARKETPLACES"
    IT_AND_SECURITY = "IT_AND_SECURITY"
    COMMUNICATION = "COMMUNICATION"
    DESIGN_AND_CREATIVITY = "DESIGN_AND_CREATIVITY"
    OTHER = "OTHER"
    MARKETING_AND_ANALYTICS = "MARKETING_AND_ANALYTICS"
    DEVELOPERS = "DEVELOPERS"
    ACCOUNTING_AND_FINANCE = "ACCOUNTING_AND_FINANCE"
    COLLABORATION = "COLLABORATION"
    CONTENT_AND_SOCIAL_MEDIA = "CONTENT_AND_SOCIAL_MEDIA"
    INTERNAL = "INTERNAL"


class Info(BaseModel):
    app_id: str
    capabilities: list[str]
    authentication_schema: dict[str, t.Any] | None = None
    capability_schema: dict[str, CommandTypes]
    logo_url: str | None = None
    user_friendly_name: str | None = None
    description: str | None = None
    categories: list[AppCategory] | None = None
