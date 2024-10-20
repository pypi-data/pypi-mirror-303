"""
为指定网站建立页面索引
"""

from datetime import datetime

from sqlmodel import Field, SQLModel


class MTMCrawlPageBase(SQLModel):
    """
    为指定网站建立页面索引
    """

    site_id: str = Field(default=None, max_length=255)
    url: str = Field(default=None, max_length=255)
    depth: int = Field(default=None)
    title: str = Field(default=None, max_length=255)
    description: str = Field(default=None, max_length=255)
    keywords: str = Field(default=None, max_length=255)
    author: str = Field(default=None, max_length=255)
    copyright: str = Field(default=None, max_length=255)
    created_at: datetime = Field(default=datetime.now())
    updated_at: datetime = Field(default=datetime.now())


class MTCrawlPage(MTMCrawlPageBase, table=True):
    """
    为指定网站建立页面索引
    """

    id: int | None = Field(default=None, primary_key=True)
