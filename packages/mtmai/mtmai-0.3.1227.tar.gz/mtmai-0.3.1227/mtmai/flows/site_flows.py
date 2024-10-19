from typing import Any

import httpx
import litellm
from bs4 import BeautifulSoup
from prefect import flow, get_run_logger, task
from pydantic import BaseModel

from mtmai.core.db import get_async_session
from mtmai.crud.crud_task import (
    get_tasks_to_run,
    mttask_create,
    mttask_get_by_id,
    mttask_update_state,
)
from mtmai.crud.curd_search import create_site_search_index
from mtmai.crud.curd_site import get_site_by_id, get_sites_enabled_automation
from mtmai.deps import AsyncSessionDep
from mtmai.flows import FlowBase, mtflow
from mtmai.flows.article_gen import (
    WriteSingleChapterRequest,
    article_gen_outline,
    write_book_chapter_crew,
)
from mtmai.models.book_gen import (
    Chapter,
    GenBookState,
    WriteOutlineRequest,
)
from mtmai.models.site import (
    SiteCreateRequest,
)


class SiteDetectInfo(BaseModel):
    title: str | None = None
    description: str | None = None

@task()
async def site_info_detect(session: AsyncSessionDep, url: str):
    """获取远程站点基本信息"""
    async with httpx.AsyncClient() as client:
        resp = await client.get(url)

    soup = BeautifulSoup(resp.text, "html.parser")
    title = soup.title.string if soup.title else None
    meta_description = soup.find("meta", attrs={"name": "description"})
    description = meta_description["content"] if meta_description else None
    if description:
        description = description[:100]
    return SiteDetectInfo(title=title, description=description)


@task()
async def create_site_task(
    site_id: str,
    user_id: str,
):
    logger = get_run_logger()
    try:
        logger.info(f"create_site_task 开始，site_id: {site_id}, user_id: {user_id}")
        async with get_async_session() as session:
            site = await get_site_by_id(session, site_id, user_id)
        if not site:
            logger.info(f"site_id: {site_id}, user_id: {user_id} 不存在")

        logger.info(f"工作流开始更新 site 信息 {site_id}")
        target_url = str(site.url)
        site_info = await site_info_detect(session, target_url)

        # Convert item_in to dict, convert url to string, and add owner_id
        site_data = site.model_dump()
        site_data["url"] = str(site_data["url"])  # Convert Url to string
        site_data["owner_id"] = user_id
        site.title = site_info.title
        site.description = site_info.description
        session.add(site)
        await session.commit()
        await session.refresh(site)
        await create_site_search_index(session, site, user_id)
        await session.refresh(site)
        ret = site.model_dump()
        logger.info(f"site_id: {site_id}, user_id: {user_id} 更新完成")
    except Exception as e:
        logger.error(
            f"site_id: {site_id}, user_id: {user_id} create_site_task失败: {e}"
        )
    return ret


@mtflow(SiteCreateRequest)
class CreateSiteFlow(FlowBase):
    @classmethod
    @flow(name="CreateSiteFlow")
    async def execute(cls, site_id: str, user_id: str) -> Any:
        # yield aisdk.AiTextChunck("<mtmai_response>\n")
        logger = get_run_logger()
        logger.info(f"site_id: {site_id}, user_id: {user_id}")
        async with get_async_session() as session:
            site = await get_site_by_id(session, site_id, user_id)
        if not site:
            logger.info(f"site_id: {site_id}, user_id: {user_id} 不存在")

        logger.info("工作流开始更新 site 信息")
        # try:
        #     yield aisdk.AiTextChunck("<mtmai_msg>开始处理</mtmai_msg>\n")
        #     req_model: SiteCreateRequest = cls.form_model
        #     yield aisdk.AiTextChunck("<mtmai_msg>验证数据</mtmai_msg>\n")
        #     item_in = req_model.model_validate(data)
        #     yield aisdk.AiTextChunck("<mtmai_msg>调用工作流</mtmai_msg>\n")
        #     task1_result = await create_site_task(item_in, user_id)
        #     yield aisdk.AiTextChunck("<mtmai_msg>完成</mtmai_msg>\n")
        #     yield aisdk.AiTextChunck(
        #         '<mtmai_action url="https://www.baidu.com">自动跳转</mtmai_action>\n'
        #     )
        # except ValidationError as e:
        #     yield aisdk.AiTextChunck(f"输入不正确: {e}")
        #     # pass
        # yield aisdk.AiTextChunck("</mtmai_response>\n")


@flow
async def create_site_flow(user_id: str, site_id: str):
    logger = get_run_logger()
    logger.info(f"create_site_flow user_id: {user_id}, site_id: {site_id}")

    await create_site_task(site_id, user_id)


@flow
async def flow_site_automation():
    """后台检测 site 状态，根据状态自动触发子工作流的运行"""
    logger = get_run_logger()
    logger.info("开始检测 site 状态")
    async with get_async_session() as session:
        sites = await get_sites_enabled_automation(session)

    if not sites or len(sites) == 0:
        logger.info("没有站点启用自动化")
        return

    for site in sites:
        logger.info(f"开始调度 site {site.id} 的任务")
        async with get_async_session() as session:
            tasks_to_run = await get_tasks_to_run(
                session=session, site_id=site.id, limit=1
            )

        if not tasks_to_run or len(tasks_to_run) == 0:
            logger.info("没有任务需要运行, 现在创建一个文章生成任务")
            async with get_async_session() as session:
                # TODO: 这里的参数应该 AI 生成

                # init_state = {
                #     "topic": "AI 在 2024 年 9 月的现状: 各行业的趋势和未来展望",
                #     "goal": "生成一本书，介绍 AI 在 2024 年 9 月的现状，包括各行业的趋势和未来展望。",
                # }
                new_mttask = await mttask_create(
                    session=session,
                    site_id=site.id,
                    name="gen_article",
                    init_state={},
                )
                await flow_run_task(str(new_mttask.id))

        else:
            logger.info(f"有任务需要运行, len={len(tasks_to_run)}")
            for ta in tasks_to_run:
                logger.info(f"开始执行任务: {ta}")
                await flow_run_task(str(ta.id))


@flow
async def flow_run_task(mttask_id: str):
    """根据数据库表 mttask 的值启动对应的工作流"""
    logger = get_run_logger()
    async with get_async_session() as session:
        mttask = await mttask_get_by_id(session=session, mttask_id=mttask_id)
    logger.info(f"开始运行mttask {mttask.id}")

    if not mttask:
        raise ValueError(f"mttask {mttask_id} 不存在")
    if not mttask.name:
        raise ValueError(f"mttask {mttask.id} 没有 name 值")
    if not mttask.site_id:
        raise ValueError(f"mttask {mttask.id} 没有 site_id 值")
    match mttask.name:
        case "gen_article":
            await flow_run_gen_article(mttask_id=str(mttask.id))

    logger.info(f"完成 mttask {mttask.id}")


@flow
async def flow_run_gen_article(mttask_id: str):
    """
    单个站点的自动化工作流
    """
    try:
        logger = get_run_logger()
        logger.info(f"flow_site_gen mttask_id: {mttask_id}")
        async with get_async_session() as session:
            mttask = await mttask_get_by_id(session=session, mttask_id=mttask_id)
            if not mttask:
                raise ValueError(f"mttask {mttask_id} 不存在")
            site = await get_site_by_id(session=session, site_id=mttask.site_id)

        logger.info("生成大纲 ...")
        async with get_async_session() as session:
            mttask = await mttask_get_by_id(session=session, mttask_id=mttask_id)

        _state = mttask.state or {}
        state = GenBookState.model_validate(_state)

        if not state.title and state.topic:
            # state 为全新态
            # TODO: 这里的初始参数应该 由 AI 生成
            state.title = "AI 在 2024 年 9 月的现状: 各行业的趋势和未来展望"
            state.goal = "生成一本书，介绍 AI 在 2024 年 9 月的现状，包括各行业的趋势和未来展望。"

        outlines = await article_gen_outline(
            req=WriteOutlineRequest(
                topic=state.topic,
                goal=state.goal,
            )
        )
        logger.info(f"flow_article_gen end, outlines: {outlines}")

        if not outlines:
            logger.info("大纲编写失败")
            return
        logger.info("大纲编写完成，开始写内容")

        async with get_async_session() as session:
            await mttask_update_state(session=session, mttask_id=mttask_id, state=state)

        chapters = outlines.chapters
        state.book_outline = chapters

        chapters = []
        for index, chapter_outline in enumerate(state.book_outline, start=1):
            logger.info(
                f"开始写章节正文 {index}/{len(state.book_outline)}: {chapter_outline.title}"
            )
            output = await write_book_chapter_crew(
                req=WriteSingleChapterRequest(
                    goal=state.goal,
                    topic=state.topic,
                    chapter_title=chapter_outline.title,
                    chapter_description=chapter_outline.description,
                    book_outlines=state.book_outline,
                )
            )
            if not output:
                logger.info(f"写章节正文失败: {output}")
                continue
            chapters.append(Chapter(title=output.title, content=output.content))

        state.book.extend(chapters)
        # sections = [await write_section(topic) for topic in outline]
        logger.info(f"章节内容写入完成, 章节数量:{len(chapters)}")

        logger.info(f"文章数据转换为markdown 格式:{len(chapters)}")

        book_content = ""
        for chapter in state.book:
            # Add the chapter title as an H1 heading
            book_content += f"# {chapter.title}\n\n"
            # Add the chapter content
            book_content += f"{chapter.content}\n\n"

        # The title of the book from self.state.title
        book_title = state.title

        logger.info("文章生成完成, 开始导出")
        filename = (
            f"./{book_title.replace(' ', '_').replace("'", '_').replace('"', '_')}.md"
        )

        # Save the combined content into the file
        # with open(filename, "w", encoding="utf-8") as file:
        #     file.write(book_content)

        logger.info("Book saved as %s", filename)
        return book_content
    except litellm.RateLimitError as e:
        logger.error(f"调用大模型到达限制，TODO 切换大模型: {e}")
        raise e
    except Exception as e:
        logger.error(f"flow_site_gen 失败: {e}")
        raise e
