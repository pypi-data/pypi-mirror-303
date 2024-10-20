import logging

from psycopg_pool import AsyncConnectionPool
from sqlmodel import SQLModel, select
from sqlmodel.ext.asyncio.session import AsyncSession

from mtmai.core.config import settings
from mtmai.core.db import get_async_session, get_engine
from mtmai.crud.crud import create_user, get_user_by_email
from mtmai.models.models import SysItem, UserCreate
from mtmai.models.search_index import SearchIndex  # 搜索索引

SearchIndex
logger = logging.getLogger()


async def _seed_users(db: AsyncSession):
    # count = db.exec(select(func.count()).select_from(Agent)).one()
    # if count > 0:
    #     return

    super_user = await get_user_by_email(
        session=db, email=settings.FIRST_SUPERUSER_EMAIL
    )
    if not super_user:
        await create_user(
            session=db,
            user_create=UserCreate(
                email=settings.FIRST_SUPERUSER_EMAIL,
                username=settings.FIRST_SUPERUSER,
                password=settings.FIRST_SUPERUSER_PASSWORD,
                is_superuser=True,
            ),
        )


async def seed_db(session: AsyncSession):
    await _seed_users(session)


async def setup_checkpointer():
    from langgraph.checkpoint.postgres.aio import AsyncPostgresSaver

    connection_kwargs = {
        "autocommit": True,
        "prepare_threshold": 0,
    }
    pool = AsyncConnectionPool(
        conninfo=settings.DATABASE_URL,
        max_size=20,
        kwargs=connection_kwargs,
    )
    logger.info("database connecting ...")
    await pool.open()
    checkpointer = AsyncPostgresSaver(pool)
    await checkpointer.setup()
    await pool.close()


async def init_database():
    """初始化数据库
    确保在空数据库的情况下能启动系统
    """
    logger.warning("⚠️ ⚠️ ⚠️ SEDDING DB  ⚠️ ⚠️⚠️")

    engine = get_engine()

    # try:
    #     with engine.connect() as connection:
    #         connection.execute(text("CREATE EXTENSION IF NOT EXISTS vector;"))
    #         # connection.execute(text("CREATE EXTENSION IF NOT EXISTS pgmq;"))
    #         connection.commit()
    # except Exception:
    #     logger.exception("error create postgresql extensions ")

    SQLModel.metadata.create_all(engine)
    # async with AsyncSession(engine) as session:
    async with get_async_session() as session:
        await seed_db(session)

    await setup_checkpointer()
    await seed_sys_items(session)
    logger.info("🟢 Seeding database finished")


async def seed_sys_items(session: AsyncSession):
    all_sys_items = [
        SysItem(
            type="task_type",
            key="articleGen",
            value="articleGen",
            description="生成站点文章",
        ),
        SysItem(
            type="task_type",
            key="siteAnalysis",
            value="siteAnalysis",
            description="流量分析(功能未实现)",
        ),
    ]
    for item in all_sys_items:
        existing_item = await session.exec(
            select(SysItem).where(SysItem.type == item.type, SysItem.key == item.key)
        )
        existing_item = existing_item.first()

        if existing_item:
            # Update existing item
            for key, value in item.items():
                setattr(existing_item, key, value)
        else:
            # Create new item
            new_item = SysItem(**item.dict())
            session.add(new_item)

    await session.commit()
