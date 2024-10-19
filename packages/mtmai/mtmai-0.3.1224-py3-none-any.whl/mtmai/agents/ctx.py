import asyncio
import json
import os
import re
import uuid
from functools import lru_cache
from mailbox import BabylMessage
from typing import Type

import httpx
import orjson
from attr import make_class
from json_repair import repair_json
from langchain_core.messages import AIMessage, ToolCall
from langchain_core.prompts import ChatPromptTemplate, PromptTemplate
from langchain_core.tools import StructuredTool
from langchain_core.utils.function_calling import (
    convert_to_openai_function,
)
from langchain_openai import ChatOpenAI
from langgraph.checkpoint.postgres.aio import AsyncPostgresSaver
from lazify import LazyProxy
from psycopg_pool import AsyncConnectionPool
from pydantic import BaseModel
from sqlalchemy import Engine
from sqlmodel import Session

from mtmai.agents.graphutils import ensure_valid_llm_response_v2
from mtmai.agents.tools.mtmdoc import MtmDocStore
from mtmai.core.config import settings
from mtmai.core.db import get_engine
from mtmai.core.logging import get_logger
from mtmai.crewai import LLM
from mtmai.llm.embedding import get_default_embeddings
from mtmai.models.graph_config import GraphConfig
from mtmai.mtlibs import yaml
from mtmai.mtlibs.kv.mtmkv import MtmKvStore

logger = get_logger()


class LoggingTransport(httpx.AsyncHTTPTransport):
    async def handle_async_request(self, request):
        response = await super().handle_async_request(request)
        # 提示： 不要读取 body，因为一般 是stream，读取了会破环状态
        logger.info(
            f"OPENAI Response: {response.status_code}\n {request.url}\nreq:\n{str(request.content)}\n"
        )
        return response


@lru_cache(maxsize=1)
def get_graph_config() -> GraphConfig:
    if not os.path.exists(settings.graph_config_path):
        raise Exception(f"未找到graph_config配置文件: {settings.graph_config_path}")
    config_dict = yaml.load_yaml_file(settings.graph_config_path) or {}

    sub = config_dict.get("mtmai_config")
    return GraphConfig.model_validate(sub)


class AgentContext:
    def __init__(self, db_engine: Engine):
        self.httpx_session: httpx.Client = None
        self.db: Engine = db_engine
        self.session: Session = Session(db_engine)
        embedding = get_default_embeddings()

        self.vectorstore = MtmDocStore(session=Session(db_engine), embedding=embedding)
        self.kvstore = MtmKvStore(db_engine)

        self.graph_config = get_graph_config()

    def retrive_graph_config(self):
        return self.graph_config

    def load_doc(self):
        return self.vectorstore

    async def get_llm_config(self, llm_config_name: str):
        llm_item = None
        for item in self.graph_config.llms:
            if item.id == llm_config_name:
                llm_item = item
                break
        if not llm_item:
            raise ValueError(f"未找到 {llm_config_name} 对应的 llm 配置")
        return llm_item

    async def get_crawai_llm(self, name: str = "chat"):
        llm_item = await self.get_llm_config(name)
        return LLM(
            model=llm_item.model,
            temperature=llm_item.temperature or None,
            base_url=llm_item.base_url,
            api_key=llm_item.api_key,
        )

    async def get_llm_openai(self, llm_config_name: str):
        llm_item = await self.get_llm_config(llm_config_name)

        base_url = llm_item.base_url
        model = llm_item.model

        all_llm_providers_prefix = ["together_ai/", "groq/"]
        for prefix in all_llm_providers_prefix:
            if model.startswith(prefix):
                model = model[len(prefix) :]
                break
        return ChatOpenAI(
            base_url=base_url,
            api_key=llm_item.api_key,
            model=model,
            temperature=llm_item.temperature or None,
            max_tokens=llm_item.max_tokens or None,
            # 使用自定义 httpx 客户端 方便日志查看
            http_client=httpx.Client(transport=LoggingTransport()),
            http_async_client=httpx.AsyncClient(transport=LoggingTransport()),
        )

    async def ainvoke_model(
        self,
        tpl: PromptTemplate,
        inputs: dict | BaseModel | None,
        *,
        tools: list[StructuredTool | dict] = None,
        structured_output: BaseModel = None,
        llm_config_name: str = "chat",
        max_retries: int = 5,
        sleep_time: int = 3,
    ):
        llm_item = await self.get_llm_config(llm_config_name)
        llm_inst = await self.get_crawai_llm(llm_config_name)

        formatted_tools = [
            convert_to_openai_function(tool, strict=True) for tool in tools
        ]
        all_tool_names = [t["name"] for t in formatted_tools]
        all_tool_names_str = ", ".join(all_tool_names)
        if tools and llm_item.llm_type == "llama3.1":
            # for openai_fun in openai_functions:
            #     tool_call_prompts.append(f"""\nUse the function '{openai_fun["name"]}' to '{openai_fun["description"]}':\n{json.dumps(openai_fun)}\n""")
            # llama3.1 模型工具调用专用提示词，确保工具调用的准确性和一致性
            toolPrompt = f"""
all tools: {all_tool_names_str}
[IMPORTANT] When calling a function, adhere strictly to the following guidelines:
1. Use the exact OpenAI ChatGPT function calling format.
2. Function calls must be in this format: {{\"name\": \"function_name\", \"arguments\": {{\"arg1\": \"value1\", \"arg2\": \"value2\"}}}}
3. Only call one function at a time.
4. Do not include any additional text with the function call.
5. If no function call is needed, respond normally without mentioning functions.
6. Only use functions from the provided list of tools.
7. Function names must consist solely of lowercase letters (a-z), numbers (0-9), and underscores (_).
8. Ensure all required parameters for the function are included.
9. Double-check that the function name and all parameter names exactly match those provided in the function description.

If you're unsure about making a function call, respond to the user's query using your general knowledge instead.
"""
            if "additional_instructions" in tpl.input_variables:
                tpl = tpl.partial(additional_instructions=toolPrompt)
            else:
                tpl.messages.append(
                    ChatPromptTemplate.from_messages([("system", toolPrompt)])
                )

        messages = await tpl.ainvoke(inputs.model_dump())
        llm_chain = llm_inst
        if structured_output:
            llm_chain = llm_chain.with_structured_output(
                structured_output, include_raw=True
            )
        if tools:
            llm_chain = llm_chain.bind_tools(tools)
        llm_chain = llm_chain.with_retry(stop_after_attempt=5)

        message_to_post = messages.to_messages()

        for attempt in range(max_retries):
            try:
                ai_msg = await ensure_valid_llm_response_v2(llm_chain, message_to_post)
                if tools:
                    ai_msg = fix_tool_calls(ai_msg)

                # 函数名必须是 tools 内，否则必定是不正确的调用，自动重试
                for tc in ai_msg.tool_calls:
                    if tc["name"] not in all_tool_names:
                        raise ValueError(
                            f"函数名 {tc['name']} 必须是 tools 内，否则必定是错误的，自动重试"
                        )
                return ai_msg
            except Exception as e:
                if attempt < max_retries - 1:
                    logger.warning(
                        f"Attempt {attempt + 1} failed. Retrying in 5 seconds..."
                    )
                    await asyncio.sleep(sleep_time)
                else:
                    logger.error(f"All {max_retries} attempts failed.")
                    raise e

    async def stream_messages(
        self, tpl: ChatPromptTemplate, messages: list[BabylMessage]
    ):
        messages2 = await tpl.ainvoke({"messages": messages})
        # config = {"configurable": {"thread_id": "abc123"}}
        logger.info(f"stream_messages: {messages2}")
        llm_inst = await self.get_llm_openai("chat")
        async for chunk in llm_inst.astream(
            messages2,
            # config,
        ):
            if chunk.content:
                yield chunk.content

    def load_json_response(
        self, ai_json_resonse_text: str, model_class: Type[BaseModel]
    ) -> Type[BaseModel]:
        repaired_json = self.repair_json(ai_json_resonse_text)
        try:
            loaded_data = orjson.loads(repaired_json)
            return make_class(**loaded_data)
        except Exception as e:
            logger.error(f"Error parsing JSON: {str(e)}")
            raise ValueError(
                f"Failed to parse JSON and create {model_class.__name__} instance"
            ) from e

    async def get_db_pool(self):
        connection_kwargs = {
            "autocommit": True,
            "prepare_threshold": 0,
        }
        pool = AsyncConnectionPool(
            conninfo=settings.DATABASE_URL,
            max_size=20,
            kwargs=connection_kwargs,
        )
        await pool.open()
        return pool

    async def get_graph_checkpointer(self):
        return AsyncPostgresSaver(await mtmai_context.get_db_pool())

    async def get_graph_by_name(self, name: str):
        if name == "storm":
            from mtmai.agents.storm import StormGraph

            return StormGraph()

        return None


def get_mtmai_ctx():
    return AgentContext(
        db_engine=get_engine(),
    )


mtmai_context: AgentContext = LazyProxy(get_mtmai_ctx, enable_cache=False)


def fix_tool_calls(ai_msg: AIMessage):
    if not ai_msg.content or (
        ai_msg.tool_calls and ai_msg.tool_calls[0].type == "tool_call"
    ):
        # 已是正确格式
        return ai_msg
    # 情况1： 以lamma3.1 常见的 <function> 格式回复函数函数调用
    function_regex = r"<function=(\w+)>(.*?)</function>"
    match = re.search(function_regex, ai_msg.content, re.DOTALL)
    if match:
        function_name, args_string = match.groups()

        args = json.loads(args_string)
        ai_msg.tool_calls.append(
            ToolCall(
                name=function_name,
                arguments=args,
                id=str(uuid.uuid4()),
                type="tool_call",
            )
        )
        ai_msg.content = ""
        return ai_msg

    # 情况2 函数调用没有出现在 tool_calls 字段，而是出现在 content 中，json格式
    # 例子： {"name": "ToDevelopAssistant", "parameters": {"request": "I want to edit an article"}}
    loaded_data = orjson.loads(repair_json(ai_msg.content))
    if (
        isinstance(loaded_data, dict)
        and "name" in loaded_data
        and "parameters" in loaded_data
    ):
        ai_msg.tool_calls.append(
            ToolCall(
                name=loaded_data["name"],
                arguments=loaded_data["parameters"],
                id=str(uuid.uuid4()),
                type="tool_call",
            )
        )
        ai_msg.content = ""
        return ai_msg
    return ai_msg


# class MtmaiContext:
#     def __init__(
#         self,
#         thread_id: str,
#         user: User,
#         auth_token: str,
#         user_env: Dict[str, str],
#         client_type: str,
#     ):
#         self.thread_id = thread_id
#         self.user = user
#         self.auth_token = auth_token
#         self.user_env = user_env
#         self.client_type = client_type


# def init_http_context(
#     thread_id: Optional[str] = None,
#     user: Optional[Union[User]] = None,
#     auth_token: Optional[str] = None,
#     user_env: Optional[Dict[str, str]] = None,
#     client_type: str = "webapp",
# ) -> MtmaiContext:
#     session_id = str(uuid.uuid4())
#     thread_id = thread_id or str(uuid.uuid4())

#     ctx = MtmaiContext(thread_id, user, auth_token, user_env, client_type)
#     # session = HTTPSession(
#     #     id=session_id,
#     #     thread_id=thread_id,
#     #     token=auth_token,
#     #     user=user,
#     #     client_type=client_type,
#     #     user_env=user_env,
#     # )
#     # context = ChainlitContext(session)
#     contextvars.set(ctx)

#     # if data_layer := get_data_layer():
#     #     if user_id := getattr(user, "id", None):
#     #         asyncio.create_task(
#     #             data_layer.update_thread(thread_id=thread_id, user_id=user_id)
#     #         )

#     return ctx


# user_id_context: ContextVar[str] = ContextVar("user_id", default=None)


# def get_current_user_id() -> str:
#     return user_id_context.get()


# def set_current_user_id(user_id: str):
#     user_id_context.set(user_id)
