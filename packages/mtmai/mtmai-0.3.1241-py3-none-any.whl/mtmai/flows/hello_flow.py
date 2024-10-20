"""
工作流： 练习和测试
"""

import asyncio
from datetime import timedelta

from prefect import flow, get_run_logger, task
from prefect.tasks import task_input_hash


@task(cache_key_fn=task_input_hash, cache_expiration=timedelta(days=1))
async def create_outline():
    # 创建大纲的逻辑
    logger = get_run_logger()
    logger.info("Creating outline")
    outline = []
    for i in range(100):
        outline.append(f"Topic {i+1}")
    return outline


@task(cache_key_fn=task_input_hash, cache_expiration=timedelta(days=1))
async def write_section(topic):
    logger = get_run_logger()
    logger.info(f"开始写内容:{topic}")
    await asyncio.sleep(5)
    logger.info(f"写内容完成:{topic}")

    return f"Content for {topic}"


@flow
async def flow_hello(goodbye=False):
    logger = get_run_logger()
    logger.info("开始编写大纲")
    outline = await create_outline()
    logger.info(f"大纲编写完成，开始写内容,数量:{len(outline)}")
    sections = [await write_section(topic) for topic in outline]
    logger.info(f"内容写入完成,数量:{len(sections)}")
