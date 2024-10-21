import logging
import uuid
from contextlib import asynccontextmanager
from typing import Any, Dict, List, Union

from psycopg_pool import AsyncConnectionPool
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine
from sqlmodel import Session, create_engine, select
from sqlmodel.ext.asyncio.session import AsyncSession

from mtmai.core.config import settings
from mtmai.crud import crud
from mtmai.models.models import User, UserCreate


def init_db(session: Session) -> None:
    user = session.exec(
        select(User).where(User.email == settings.FIRST_SUPERUSER)
    ).first()
    if not user:
        user_in = UserCreate(
            email=settings.FIRST_SUPERUSER,
            password=settings.FIRST_SUPERUSER_PASSWORD,
            is_superuser=True,
        )
        user = crud.create_user(session=session, user_create=user_in)


logger = logging.getLogger()
engine = None


def get_engine():
    global engine
    if engine is not None:
        return engine
    env_conn_str = settings.DATABASE_URL
    if env_conn_str is None:
        raise ValueError("DATABASE_URL environment variable is not set")  # noqa: EM101, TRY003
    connection_string = str(env_conn_str).replace("postgresql", "postgresql+psycopg")

    engine = create_engine(
        connection_string, connect_args={"sslmode": "require"}, pool_recycle=300
    )
    return engine


engine = get_engine()

async_engine: AsyncEngine | None = None


def get_async_engine():
    global async_engine
    if async_engine is not None:
        return async_engine
    env_conn_str = settings.DATABASE_URL
    if env_conn_str is None:
        raise ValueError("DATABASE_URL environment variable is not set")  # noqa: EM101, TRY003
    connection_string = str(env_conn_str).replace("postgresql", "postgresql+psycopg")
    async_engine = create_async_engine(
        connection_string,
        #    echo=True,# echo 会打印所有sql语句，影响性能
        future=True,
    )
    return async_engine


def get_session():
    engine = get_engine()
    session = Session(engine)
    try:
        yield session
    finally:
        session.close()


@asynccontextmanager
async def get_async_session():
    engine = get_async_engine()
    async with AsyncSession(engine) as session:
        try:
            yield session
        finally:
            await session.close()


# 全局连接池对象
pool: AsyncConnectionPool | None = None


async def get_checkpointer():
    from langgraph.checkpoint.postgres.aio import AsyncPostgresSaver

    global pool
    if not pool or pool.closed:
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
    yield checkpointer


async def execute_sql(
    query: str, parameters: dict
) -> Union[List[Dict[str, Any]], int, None]:
    parameterized_query = text(query)
    # engine = get_async_engine()

    async with get_async_session() as session:
        try:
            # await session.begin()
            result = await session.exec(parameterized_query, parameters)
            # await session.commit()
            if result.returns_rows:
                json_result = [dict(row._mapping) for row in result.fetchall()]
                clean_json_result = _clean_result(json_result)
                return clean_json_result
            else:
                return result.rowcount
        except SQLAlchemyError as e:
            await session.rollback()
            logger.warn(f"An error occurred: {e}")
            return None
        except Exception as e:
            await session.rollback()
            logger.warn(f"An unexpected error occurred: {e}")
            return None


def _clean_result(obj):
    """Recursively change UUID -> str and serialize dictionaries"""
    if isinstance(obj, dict):
        return {k: _clean_result(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [_clean_result(item) for item in obj]
    elif isinstance(obj, uuid.UUID):
        return str(obj)
    return obj
