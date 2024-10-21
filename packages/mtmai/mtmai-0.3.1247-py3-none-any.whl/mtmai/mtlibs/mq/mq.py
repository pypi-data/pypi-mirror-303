from mtmai.core.logging import get_logger
from mtmai.mtlibs.mq.pq_queue import AsyncPGMQueue

logger = get_logger()


async def send_message(mq: AsyncPGMQueue, queue: str, message: str):
    await mq.send(queue=queue, message=message)
