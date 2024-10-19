from aiocache import cached
from sqlmodel import select

from mtmai.core.db import get_async_session
from mtmai.models.models import User


@cached(ttl=300)
async def get_user_by_id2(user_id: str) -> User | None:
    if not user_id:
        return None
    async with get_async_session() as session:
        statement = select(User).where(User.id == user_id)
        result = await session.exec(statement)
        return result.first()
