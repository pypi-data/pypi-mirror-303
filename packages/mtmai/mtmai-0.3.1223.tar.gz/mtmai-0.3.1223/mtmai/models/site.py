import uuid
from datetime import datetime

from pydantic import BaseModel, HttpUrl
from pydantic import Field as PydanticField
from sqlmodel import JSON, Column, Field, SQLModel


class SiteHostBase(SQLModel):
    domain: str = Field(min_length=3, max_length=255)
    is_default: bool = Field(default=False)
    is_https: bool = Field(default=False)
    site_id: uuid.UUID = Field(
        foreign_key="site.id", nullable=False, ondelete="CASCADE"
    )


class SiteHost(SiteHostBase, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)


class SiteBase(SQLModel):
    """
    用户站点基础配置
    """

    title: str | None = Field(default=None, max_length=255)
    description: str | None = Field(default=None, max_length=255)
    created_at: datetime = Field(default=datetime.now())
    updated_at: datetime = Field(default=datetime.now())
    enabled: bool | None = Field(default=True)
    owner_id: uuid.UUID | None = Field(
        foreign_key="user.id", index=True, nullable=False, ondelete="CASCADE"
    )
    ########################################################################################
    # 新设计方式：使用第三方站点的方式，例如可以绑定 wordpress 站点
    url: str | None = Field(default=None, max_length=255)
    # 站点的框架，例如 wordpress, typecho, hexo 等
    framework: str | None = Field(default=None, max_length=255)
    # 站点的认证信息，例如 wordpress 的 username, password,
    credential_type: str | None = Field(default=None, max_length=255)
    credentials: str | None = Field(default=None, max_length=255)
    meta: dict | None = Field(default={}, sa_column=Column(JSON))
    enabled_automation: bool | None = Field(default=False)


# Database model, database table inferred from class name
class Site(SiteBase, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    updated_at: datetime = Field(default=datetime.now())


class SiteCreateRequest(BaseModel):
    url: HttpUrl = PydanticField(
        default=None,
        max_length=255,
        description="网站地址",
        # json_schema_extra={
        #     "label": "网站地址",
        #     "placeholder": "https://example.com",
        #     "icon": "site",
        # },
    )

    class Config:
        json_schema_extra = {
            "title": "站点创建",
        }


class SiteUpdateRequest(SiteBase):
    owner_id: uuid.UUID | None = None


class SiteItemPublic(SiteBase):
    id: uuid.UUID


class ListSiteResponse(SQLModel):
    data: list[SiteItemPublic]
    count: int


class ListSiteHostRequest(SQLModel):
    siteId: uuid.UUID
    q: str | None = Field(default=None, max_length=255)


class SiteHostItemPublic(SiteHostBase):
    id: uuid.UUID


class ListSiteHostsResponse(SQLModel):
    data: list[SiteHostItemPublic]
    count: int


class SiteHostCreateRequest(SiteHostBase):
    site_id: uuid.UUID


class SiteHostCreateResponse(SQLModel):
    id: uuid.UUID


class SiteHostUpdateRequest(SiteHostBase):
    id: uuid.UUID
    host: str = Field(min_length=3, max_length=255)


class SiteHostUpdateResponse(SQLModel):
    id: uuid.UUID


class SiteHostDeleteRequest(SQLModel):
    id: uuid.UUID


class SiteHostDeleteResponse(SQLModel):
    id: uuid.UUID


class SiteGenConfig(BaseModel):
    """
    站点生成配置
    """

    site_url: str | None = Field(default=None, max_length=255)
    site_topic: str | None = Field(default=None, max_length=255)
    description: str | None = Field(default=None, max_length=255)
    keywords: str | None = Field(default=None, max_length=255)
