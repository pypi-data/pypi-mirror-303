from typing import Literal

from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlmodel import Session, select

from mtmai.core.db import get_session
from mtmai.core.logging import get_logger
from mtmai.deps import AsyncSessionDep, CurrentUser
from mtmai.models.listview import ListviewRequest
from mtmai.models.logitems import LogItem, LogItemListRequest, LogItemListResponse

router = APIRouter()
logger = get_logger()


class ListViewConfigRequest(BaseModel):
    displayAt: Literal["side", "workbench"] | None = None
    appType: Literal["mtmai", "mtmai_copilot"] | None = None
    dataType: Literal["site", "doc", "task", "kb"] | None = None


@router.post("/listview_config", response_model=ListviewRequest)
async def listview_config(
    session: AsyncSessionDep, current_user: CurrentUser, req: ListViewConfigRequest
):
    """
    获取列表视图配置

    """
    result = ListviewRequest()
    return result


@router.post("/logs", response_model=LogItemListResponse)
async def log_list(*, db: Session = Depends(get_session), req: LogItemListRequest):
    async with get_session() as session:
        query = select(LogItem).where(LogItem.app == req.app)
        result = await session.exec(query)
        items = result.all()

    return LogItemListResponse(data=items, count=len(items))
