from fastapi import APIRouter, Depends, HTTPException, Query
from pydantic import BaseModel
from sqlmodel import Session, func, select

from mtmai.core.db import get_session
from mtmai.core.event import emit_flow_event
from mtmai.core.logging import get_logger
from mtmai.crud import crud_task
from mtmai.deps import AsyncSessionDep, CurrentUser
from mtmai.models.base_model import CommonResultResponse
from mtmai.models.listview import ListVieweRsponse, ListviewItemPublic
from mtmai.models.task import (
    MtTask,
    TaskCreateRequest,
    TaskCreateResponse,
    TaskListResponse,
)

router = APIRouter()
logger = get_logger()


@router.get("/tasks", response_model=TaskListResponse)
async def task_list(
    *,
    session: Session = Depends(get_session),
    query: str = Query(default=""),
    skip: int = 0,
    user: CurrentUser,
    limit: int = Query(default=100, le=100),
):
    if user.is_superuser:
        count_statement = select(func.count()).select_from(MtTask)
        count = session.exec(count_statement).one()
        statement = select(MtTask).offset(skip).limit(limit)
        items = session.exec(statement).all()
    else:
        count_statement = (
            select(func.count()).select_from(MtTask).where(MtTask.owner_id == user.id)
        )
        count = session.exec(count_statement).one()
        statement = (
            select(MtTask).where(MtTask.owner_id == user.id).offset(skip).limit(limit)
        )
        items = session.exec(statement).all()

    return TaskListResponse(data=items, count=count)


@router.get("/{mttask_id}", response_model=MtTask)
async def get_mttask(
    *,
    session: AsyncSessionDep,
    current_user: CurrentUser,
    mttask_id: str,
):
    """
    Get task by id.
    """
    item = await crud_task.mttask_get_by_id(session=session, mttask_id=mttask_id)
    if not item or item.owner_id != current_user.id:
        raise HTTPException(status_code=404, detail="not found")
    return item


@router.post("/", response_model=TaskCreateResponse)
async def create_task(
    *,
    session: AsyncSessionDep,
    current_user: CurrentUser,
    item_in: TaskCreateRequest,
):
    """
    Create new task.
    """

    try:
        task = await crud_task.create_task(
            session=session, task_create=item_in, owner_id=current_user.id
        )
        return TaskCreateResponse(id=task.id)
    except Exception as e:
        logger.error(e)
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/task_types", response_model=ListVieweRsponse)
async def task_types(
    *,
    session: AsyncSessionDep,
    current_user: CurrentUser,
    # item_in: TaskCreateRequest,
):
    """
    Get task types.
    """
    items = [
        ListviewItemPublic(
            id="1",
            title="articleGen",
            description="生成站点文章",
            payload={},
        ),
        ListviewItemPublic(
            id="1",
            title="siteAnalysis",
            description="流量分析(功能未实现)",
            payload={},
        ),
    ]
    return ListVieweRsponse(count=len(items), items=items)


class MttaskUpdateStatusRequest(BaseModel):
    mttask_id: str
    status: str


@router.post("/mttask_update_status", response_model=CommonResultResponse)
async def mttask_update_status(
    *,
    session: AsyncSessionDep,
    current_user: CurrentUser,
    item_in: MttaskUpdateStatusRequest,
):
    """
    更新任务状态
    """
    mttask = await crud_task.mttask_get_by_id(
        session=session, mttask_id=item_in.mttask_id
    )
    if not mttask:
        raise HTTPException(status_code=404, detail="not found")
    if mttask.owner_id != current_user.id:
        raise HTTPException(status_code=403, detail="forbidden")

    # 状态对比
    if mttask.status == item_in.status:
        # 没有变化，就不需要后续操作
        return CommonResultResponse(
            data={"status": "success"}, message="更新任务状态成功"
        )

    # 如果状态不一样
    if mttask.status == "pending":
        if item_in.status == "running":
            event_result = await emit_flow_event(
                "mtmai.mttask.update_status",
                {"mttask_id": str(mttask.id), "status": str(item_in.status)},
            )
            # event = emit_event(
            #     event="mtmai.mttask.update_status",
            #     resource={
            #         "prefect.resource.id": "my.external.resource",
            #         "mttask_id": str(mttask.id),
            #         # "status": str(item_in.status),
            #         # "site_id": str(new_site.id),
            #     },
            # )
            logger.info(event_result)
        elif item_in.status == "success":
            pass
        elif item_in.status == "failed":
            pass
        else:
            raise HTTPException(status_code=400, detail="invalid status")
    # await crud_task.mttask_update_state(
    #     session=session, mttask_id=item_in.mttask_id, status=item_in.status
    # )
    return CommonResultResponse(data={"status": "success"}, message="更新任务状态成功")
