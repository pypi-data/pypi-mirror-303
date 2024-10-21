from mtmai.core.logging import get_logger
from mtmai.mtlibs.mq.pq_queue import AsyncPGMQueue

logger = get_logger()


async def send_message(mq: AsyncPGMQueue, queue: str, message: str):
    await mq.send(queue=queue, message=message)


# ------------------------------------------------------------------------------------------
# 新函数
async def send_chat_event(mq: AsyncPGMQueue, thread_id: str, message: str):
    queue = f"chat_event_{thread_id}"
    await mq.send(queue=queue, message=message)


async def read_chat_event(mq: AsyncPGMQueue, thread_id: str):
    queue = f"chat_event_{thread_id}"
    return await mq.pop(queue)
