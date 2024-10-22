import logging

from fastapi import APIRouter
from langgraph.graph.state import CompiledStateGraph
from sqlmodel import SQLModel, func, select

from mtmai.deps import OptionalUserDep, SessionDep
from mtmai.models.agent import AgentBootstrap, AgentMeta, UiMessage, UiMessageBase

router = APIRouter()

logger = logging.getLogger()
graphs: dict[str, CompiledStateGraph] = {}


class AgentsPublic(SQLModel):
    data: list[AgentMeta]
    count: int


@router.get("/agent_bootstrap", response_model=AgentBootstrap)
async def agent_bootstrap(user: OptionalUserDep, db: SessionDep):
    """
    获取 agent 的配置，用于前端加载agent的配置
    """
    logger.info("agent_bootstrap")
    return AgentBootstrap(is_show_fab=True)


@router.get(
    "",
    summary="获取 Agent 列表",
    description=(
        "此端点用于获取 agent 列表。支持分页功能"
        "可以通过 `skip` 和 `limit` 参数控制返回的 agent 数量。"
    ),
    response_description="返回包含所有 agent 的列表及总数。",
    response_model=AgentsPublic,
    responses={
        200: {
            "description": "成功返回 agent 列表",
            "content": {
                "application/json": {
                    "example": {
                        "data": [
                            {"name": "agent1", "status": "active"},
                            {"name": "agent2", "status": "inactive"},
                        ],
                        "count": 2,
                    }
                }
            },
        },
        401: {"description": "未经授权的请求"},
        500: {"description": "服务器内部错误"},
    },
)
@router.get(
    "/image/{agent}",
    summary="获取工作流图像",
    description="此端点通过给定的 agent ID，生成工作流的图像并返回 PNG 格式的数据。",
    response_description="返回 PNG 格式的工作流图像。",
    responses={
        200: {"content": {"image/png": {}}},
        404: {"description": "Agent 未找到"},
    },
)

class ChatMessagesItem(UiMessageBase):
    id: str


class ChatMessagesResponse(SQLModel):
    data: list[ChatMessagesItem]
    count: int


class AgentChatMessageRequest(SQLModel):
    chat_id: str
    skip: int = 0
    limit: int = 100


@router.post("/chat_messages", response_model=ChatMessagesResponse)
async def messages(session: SessionDep, req: AgentChatMessageRequest):
    """获取聊天消息"""
    count_statement = (
        select(func.count())
        .select_from(UiMessage)
        .where(UiMessage.chatbot_id == req.chat_id)
    )
    count = session.exec(count_statement).one()
    statement = (
        select(UiMessage)
        .where(UiMessage.chatbot_id == req.chat_id)
        .offset(req.skip)
        .limit(req.limit)
    )
    items = session.exec(statement).all()
    return ChatMessagesResponse(data=items, count=count)
