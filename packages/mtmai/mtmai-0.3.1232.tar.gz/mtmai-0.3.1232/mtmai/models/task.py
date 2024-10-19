import uuid
from datetime import datetime

from pydantic import BaseModel
from sqlmodel import JSON, Column, Field, SQLModel


class TaskBase(SQLModel):
    name: str = Field(nullable=True)
    title: str = Field(nullable=True)
    description: str | None = Field(nullable=True)
    created_at: datetime = Field(default_factory=datetime.now, nullable=False)
    updated_at: datetime = Field(default_factory=datetime.now, nullable=False)
    fulfilled_at: datetime | None = Field(default=None)
    site_id: uuid.UUID = Field(
        foreign_key="site.id", nullable=False, ondelete="CASCADE"
    )
    status: str = Field(default="pending")
    priority: int = Field(default=3)
    # 任务参数
    payload: dict | None = Field(default={}, sa_column=Column(JSON))
    state: dict | None = Field(default={}, sa_column=Column(JSON))
    # 任务结果
    results: dict | None = Field(default={}, sa_column=Column(JSON))
    finished_at: datetime | None = Field(default=None)
    error: str | None = Field(default=None)


class MtTask(TaskBase, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)

    owner_id: uuid.UUID | None = Field(
        index=True,
        nullable=True,
        foreign_key="user.id",
        ondelete="CASCADE",
    )


class TaskItemPublic(TaskBase):
    pass


class TaskListResponse(SQLModel):
    data: list[TaskItemPublic]
    count: int


class TaskCreateRequest(BaseModel):
    siteId: str
    taskType: str
    payload: dict | None = None


class TaskCreateResponse(BaseModel):
    id: uuid.UUID | str
