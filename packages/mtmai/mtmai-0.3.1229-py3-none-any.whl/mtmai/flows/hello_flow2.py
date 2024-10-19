"""
工作流： 练习和测试
"""

from prefect import flow, get_run_logger


@flow
async def flow_hello_2(param_1: str):
    logger = get_run_logger()
    logger.info(f"事件触发 flow_hello_2 {param_1}")
