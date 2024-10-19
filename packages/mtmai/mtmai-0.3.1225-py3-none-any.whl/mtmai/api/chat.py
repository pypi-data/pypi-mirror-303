from typing import Union

from fastapi import APIRouter, Depends, Query
from fastapi.responses import JSONResponse
from langchain_core.messages import ChatMessage
from langchain_core.runnables import RunnableConfig
from langgraph.graph.graph import CompiledGraph
from typing_extensions import Annotated

import mtmai.chainlit as cl
import mtmai.chainlit.data as cl_data
from mtmai.agents.chat_profiles.profiles import get_all_profiles, get_chat_agent
from mtmai.auth import get_current_user
from mtmai.chainlit import context
from mtmai.chainlit.config import config
from mtmai.chainlit.context import init_http_context
from mtmai.chainlit.data import get_data_layer
from mtmai.chainlit.markdown import get_markdown_str
from mtmai.chainlit.types import GetThreadsRequest, ThreadDict
from mtmai.chainlit.user import PersistedUser
from mtmai.core.logging import get_logger
from mtmai.crud import curd_chat
from mtmai.deps import AsyncSessionDep, CurrentUser, OptionalUserDep, SessionDep
from mtmai.models.chat import ChatProfilesResponse
from mtmai.models.models import User
from mtmai.mtlibs.chainlit.data_layer import SQLAlchemyDataLayer

# 使用自定义的 sql 存储chainlit数据
cl_data._data_layer = SQLAlchemyDataLayer()

router = APIRouter()
logger = get_logger()


@cl.set_chat_profiles
async def chat_profile(current_user: User):
    logger.info("set_chat_profiles , 当前用户 %s", current_user)
    clChatProfiles = [
        cl.ChatProfile(
            name=profile.name,
            markdown_description=profile.description,
            icon=profile.icon,
            default=profile.default,
            starters=profile.starters,
        )
        for profile in await get_all_profiles()
    ]

    return clChatProfiles


@cl.on_chat_start
async def chat_start():
    chat_profile = cl.user_session.get("chat_profile")
    if not chat_profile:
        chat_profile = "MainCopilotAgent"
    chat_agent = await get_chat_agent(chat_profile)
    if not chat_agent:
        logger.error("没有找到聊天代理 %s", chat_profile)
        return
    cl.user_session.set("chat_agent", chat_agent)
    await chat_agent.chat_start()


@cl.on_chat_resume
async def on_chat_resume(thread: ThreadDict):
    chat_profile = cl.user_session.get("chat_profile")
    if not chat_profile:
        chat_profile = "MainCopilotAgent"
    chat_agent = await get_chat_agent(chat_profile)
    if not chat_agent:
        logger.error("没有找到聊天代理 %s", chat_profile)
        return
    cl.user_session.set("chat_agent", chat_agent)

    # 加载llm 聊天记录
    chat_messages: list[ChatMessage] = []
    for step in thread.get("steps", []):
        if "message" in step["type"]:
            chat_messages.append(
                ChatMessage(role=step.get("name", ""), content=step.get("output"))
            )
    cl.user_session.set("chat_messages", chat_messages)


@cl.on_settings_update
async def setup_agent(settings):
    logger.info("on_settings_update", settings)


@cl.on_chat_end
def end():
    logger.info("goodbye %s", cl.user_session.get("id", ""))


@cl.on_message
async def on_message(message: cl.Message):
    chat_agent = cl.user_session.get("chat_agent")
    if chat_agent:
        await chat_agent.on_message(message)
    else:
        logger.error("没有找到聊天代理")


@router.get("/chat_profiles", response_model=ChatProfilesResponse)
async def chat_profiles(user: OptionalUserDep, db: SessionDep):
    """
    获取 agent 的配置，用于前端加载agent的配置
    """
    all_profiles = await get_all_profiles()
    return ChatProfilesResponse(count=len(all_profiles), data=all_profiles)


router = APIRouter()
_language_pattern = (
    "^[a-zA-Z]{2,3}(-[a-zA-Z]{2,3})?(-[a-zA-Z]{2,8})?(-x-[a-zA-Z0-9]{1,8})?$"
)


@router.post("/threads")
async def get_user_threads(
    req: GetThreadsRequest,
    session: AsyncSessionDep,
    current_user: CurrentUser,
    skip: int = 0,
    limit: int = 100,
):
    """Get the threads page by page."""
    # payload.filter.userId = current_user.id

    user_threads = await curd_chat.get_user_threads(
        session,
        current_user.id,
        # thread_id=req.filter.therad_id,
        limit=limit,
        skip=skip,
    )
    return user_threads


@router.get("/settings")
async def project_settings(
    current_user: Annotated[Union[User, PersistedUser], Depends(get_current_user)],
    language: str = Query(
        default="en-US", description="Language code", pattern=_language_pattern
    ),
):
    """Return project settings. This is called by the UI before the establishing the websocket connection."""

    # Load the markdown file based on the provided language

    markdown = get_markdown_str(config.root, language)

    profiles = []
    if config.code.set_chat_profiles:
        chat_profiles = await config.code.set_chat_profiles(current_user)
        if chat_profiles:
            profiles = [p.to_dict() for p in chat_profiles]

    starters = []
    if config.code.set_starters:
        starters = await config.code.set_starters(current_user)
        if starters:
            starters = [s.to_dict() for s in starters]

    if config.code.on_audio_chunk:
        config.features.audio.enabled = True

    debug_url = None
    data_layer = get_data_layer()

    if data_layer and config.run.debug:
        debug_url = await data_layer.build_debug_url()

    data_resonse = {
        "ui": config.ui.to_dict(),
        "features": config.features.to_dict(),
        "userEnv": config.project.user_env,
        "dataPersistence": get_data_layer() is not None,
        "threadResumable": bool(config.code.on_chat_resume),
        "markdown": markdown,
        "chatProfiles": profiles,
        "starters": starters,
        "debugUrl": debug_url,
    }
    return JSONResponse(content=data_resonse)


@router.get("/graph_image/{thread_id}")
async def graph_image(
    thread_id: str,
    current_user: Annotated[Union[User, PersistedUser], Depends(get_current_user)],
):
    init_http_context(
        user=current_user,
        thread_id=thread_id,
    )
    ctx = context
    await cl.Message(content="Hello, I am a chatbot!").send()

    user_session = cl.user_session
    graph: CompiledGraph = user_session.get("graph")
    # if not graph:
    #     raise ValueError("graph 未初始化")
    thread: RunnableConfig = {
        "configurable": {
            "thread_id": thread_id,
        }
    }
    pre_state = await graph.aget_state(thread, subgraphs=True)

    # await self.run_graph(thread)
    return "threadid:" + thread_id


# @router.post("/chat")
# async def chat():
#     return aisdk.AiSDKStreamResponse(
#         fake_video_streamer(),
#     )
