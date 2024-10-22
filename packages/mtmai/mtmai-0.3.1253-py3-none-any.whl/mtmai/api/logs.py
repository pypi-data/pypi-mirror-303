from fastapi import APIRouter, Depends
from sqlmodel import Session, select

from mtmai.core.db import get_async_session, get_session
from mtmai.core.logging import get_logger
from mtmai.models.logitems import LogItem, LogItemListRequest, LogItemListResponse

router = APIRouter()
logger = get_logger()


@router.post("/logs", response_model=LogItemListResponse)
async def log_list(*, db: Session = Depends(get_session), req: LogItemListRequest):
    async with get_async_session() as session:
        query = select(LogItem).where(LogItem.app == req.app)
        result = await session.exec(query)
        items = result.all()

    return LogItemListResponse(items=items, total=len(items))
