"""博客系统的 curd 操作"""

from fastapi import HTTPException
from pydantic import BaseModel

from mtmai.core.db import get_async_session
from mtmai.models.logitems import LogItem


class LogItemCreateReq(BaseModel):
    app: str
    text: str
    level: int = 3


async def create_log_item(
    log_item_create: LogItemCreateReq,
) -> LogItem:
    input_data = LogItemCreateReq.model_validate(log_item_create)

    if not input_data.text:
        raise HTTPException(status_code=400, detail="text is required")
    if not input_data.app:
        input_data = "sys"

    async with get_async_session() as session:
        new_log_item = LogItem(**input_data.model_dump(), title="text")
        session.add(new_log_item)
        await session.commit()
        await session.refresh(new_log_item)
    return new_log_item


async def create_context_logger():
    pass
