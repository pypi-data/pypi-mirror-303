from fastapi import APIRouter, Depends, HTTPException, Query
from pydantic import BaseModel
from sqlmodel import Session, func, select

from mtmai.core.db import get_session
from mtmai.core.event import emit_flow_event
from mtmai.core.logging import get_logger
from mtmai.crud import crud_sysitem, crud_task
from mtmai.deps import AsyncSessionDep, CurrentUser
from mtmai.models.base_model import CommonResultResponse
from mtmai.models.task import (
    MtTask,
    MtTaskStatus,
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


class DrowndownSelectItem(BaseModel):
    id: str
    value: str
    title: str
    description: str


class SelectItemsResponse(BaseModel):
    items: list[DrowndownSelectItem]
    count: int


@router.post("/task_types", response_model=SelectItemsResponse)
async def task_types(
    *,
    session: AsyncSessionDep,
    current_user: CurrentUser,
    # item_in: TaskCreateRequest,
):
    """
    Get task types.
    """

    sysitems = await crud_sysitem.get_sys_items(session=session, type="task_type")
    if sysitems:
        items = []
        for sysitem in sysitems:
            items.append(
                DrowndownSelectItem(
                    id=sysitem.key,
                    title=sysitem.description,
                    description=sysitem.description,
                    value=sysitem.value,
                )
            )
        return SelectItemsResponse(items=items, count=len(items))

    raise HTTPException(status_code=404, detail="Task types not found")


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
        return CommonResultResponse(
            data={"status": "success"}, message="更新任务状态成功"
        )

    # 如果状态不一样
    if mttask.status == MtTaskStatus.NEW:
        if item_in.status == "pending":
            event_result = await emit_flow_event(
                event="mtmai.mttask.update_status",
                resource_id=str(mttask.id),
                # data={"mttask_id": str(mttask.id)},
            )
            logger.info(event_result)
    if mttask.status == "pending":
        if item_in.status == "running":
            await emit_flow_event(
                event="mtmai.mttask.update_status",
                resource_id=str(mttask.id),
                # data={"mttask_id": str(mttask.id)},
            )
            session.add(mttask)
            await session.commit()
            return CommonResultResponse(
                data={"status": "success"}, message="更新任务状态成功"
            )

        elif item_in.status == "success":
            pass
        elif item_in.status == "failed":
            pass
        # else:
        #     raise HTTPException(status_code=400, detail="invalid status")
    # await crud_task.mttask_update_state(
    #     session=session, mttask_id=item_in.mttask_id, status=item_in.status
    # )
    raise HTTPException(status_code=400, detail="invalid status")
