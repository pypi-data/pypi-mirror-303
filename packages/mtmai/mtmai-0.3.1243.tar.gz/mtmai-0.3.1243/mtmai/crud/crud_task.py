import json
import uuid

from fastapi.encoders import jsonable_encoder
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from mtmai.crud.curd_search import generate_search_vector
from mtmai.crud.curd_site import get_site_by_id
from mtmai.models.search_index import SearchIndex
from mtmai.models.task import MtTask, TaskCreateRequest


async def create_task(
    *, session: AsyncSession, task_create: TaskCreateRequest, owner_id: str | uuid.UUID
):
    if isinstance(owner_id, str):
        owner_id = uuid.UUID(owner_id)
    db_item = MtTask(
        name=task_create.taskType,
        site_id=task_create.siteId,
        owner_id=owner_id,
        status="pending",
        description="",
        state={},
        priority=3,
    )
    session.add(db_item)
    await session.commit()
    await session.refresh(db_item)
    await mttask_search_index(session, db_item)
    await session.refresh(db_item)
    return db_item


async def mttask_search_index(session: AsyncSession, mttask: MtTask):
    if not mttask.title:
        mttask.title = "no title task"
    if not mttask.description:
        mttask.description = ""
    content_summary = (
        mttask.title + " " + mttask.description + " " + json.dumps(mttask.payload)
    )
    search_index = SearchIndex(
        content_type="mttask",
        content_id=mttask.id,
        title=mttask.title or "no_title",
        owner_id=mttask.owner_id,
        content_summary=content_summary,
        meta={},
        search_vector=await generate_search_vector(session, content_summary),
    )
    session.add(search_index)
    await session.commit()
    await session.refresh(search_index)


async def get_tasks_to_run(*, session: AsyncSession, site_id: str | uuid.UUID, limit=1):
    """获取一个需要运行的任务"""
    if isinstance(site_id, str):
        site_id = uuid.UUID(site_id)

    statement = (
        select(MtTask)
        .where(MtTask.status == "pending", MtTask.site_id == site_id)
        .order_by(MtTask.priority.desc())
        .limit(limit)
    )
    result = await session.exec(statement)
    return result.all()


async def mttask_get_by_id(*, session: AsyncSession, mttask_id: str | uuid.UUID):
    """根据 id 获取一个任务"""
    if isinstance(mttask_id, str):
        mttask_id = uuid.UUID(mttask_id)
    statement = select(MtTask).where(MtTask.id == mttask_id)
    result = await session.exec(statement)
    return result.first()


async def mttask_update_state(
    *, session: AsyncSession, mttask_id: str | uuid.UUID, state: dict
):
    """更新任务 state"""
    if isinstance(mttask_id, str):
        mttask_id = uuid.UUID(mttask_id)
    statement = select(MtTask).where(MtTask.id == mttask_id)
    result = await session.exec(statement)
    db_item = result.first()
    if db_item:
        db_item.state = jsonable_encoder(state)
        await session.commit()
        await session.refresh(db_item)


async def mttask_create(
    *, session: AsyncSession, site_id: uuid.UUID | str, name=str, init_state: dict = {}
):
    if not name:
        raise ValueError("mttask_create name is required")
    if isinstance(site_id, str):
        site_id = uuid.UUID(site_id)

    site = await get_site_by_id(session=session, site_id=site_id)
    if not site:
        raise ValueError("mttask_create site_id not found")
    new_mttask = MtTask(
        name=name,
        site_id=site_id,
        owner_id=site.owner_id,
        status="pending",
        state=init_state,
        priority=3,
    )
    session.add(new_mttask)
    await session.commit()
    await session.refresh(new_mttask)
    return new_mttask
