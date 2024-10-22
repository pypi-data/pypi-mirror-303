import uuid
from dataclasses import asdict
from datetime import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Optional, Union

import aiofiles
import aiohttp
from sqlmodel import select

from mtmai.chainlit.context import context
from mtmai.chainlit.data import BaseDataLayer, queue_until_user_message
from mtmai.chainlit.element import ElementDict
from mtmai.chainlit.logger import logger
from mtmai.chainlit.step import StepDict
from mtmai.chainlit.types import (
    Feedback,
    FeedbackDict,
    PageInfo,
    PaginatedResponse,
    Pagination,
    ThreadDict,
    ThreadFilter,
)
from mtmai.chainlit.user import PersistedUser
from mtmai.chainlit.user import User as ClUser
from mtmai.core.db import get_async_session
from mtmai.crud.crud import get_user_by_username
from mtmai.crud.curd_chat import get_user_threads
from mtmai.models.chat import ChatStep, ChatThread
from mtmai.models.models import User

if TYPE_CHECKING:
    from mtmai.chainlit.element import Element, ElementDict
    from mtmai.chainlit.step import StepDict

user_thread_limit = 50


class SQLAlchemyDataLayer(BaseDataLayer):
    def __init__(
        self,
    ):
        pass

    async def build_debug_url(self) -> str:
        return ""

    async def get_current_timestamp(self) -> str:
        return datetime.now().isoformat() + "Z"

    def clean_result(self, obj):
        """Recursively change UUID -> str and serialize dictionaries"""
        if isinstance(obj, dict):
            return {k: self.clean_result(v) for k, v in obj.items()}
        elif isinstance(obj, list):
            return [self.clean_result(item) for item in obj]
        elif isinstance(obj, uuid.UUID):
            return str(obj)
        return obj

    def _convert_dbuser_to_PersistedUser(self, db_user: User):
        return PersistedUser(
            id=db_user.id,
            display_name=db_user.username,
            createdAt=str(db_user.created_at),
            metadata=db_user.meta,
            identifier=db_user.username,
        )

    ###### Elements ######
    async def get_element(
        self, thread_id: str, element_id: str
    ) -> Optional["ElementDict"]:
        if self.show_logger:
            logger.info(
                f"SQLAlchemy: get_element, thread_id={thread_id}, element_id={element_id}"
            )
        query = """SELECT * FROM elements WHERE "threadId" = :thread_id AND "id" = :element_id"""
        parameters = {"thread_id": thread_id, "element_id": element_id}
        element: Union[List[Dict[str, Any]], int, None] = await self.execute_sql(
            query=query, parameters=parameters
        )
        if isinstance(element, list) and element:
            element_dict: Dict[str, Any] = element[0]
            return ElementDict(
                id=element_dict["id"],
                threadId=element_dict.get("threadId"),
                type=element_dict["type"],
                chainlitKey=element_dict.get("chainlitKey"),
                url=element_dict.get("url"),
                objectKey=element_dict.get("objectKey"),
                name=element_dict["name"],
                display=element_dict["display"],
                size=element_dict.get("size"),
                language=element_dict.get("language"),
                page=element_dict.get("page"),
                autoPlay=element_dict.get("autoPlay"),
                playerConfig=element_dict.get("playerConfig"),
                forId=element_dict.get("forId"),
                mime=element_dict.get("mime"),
            )
        else:
            return None

    ###### User ######
    async def get_user(self, identifier: str) -> Optional[PersistedUser]:
        async with get_async_session() as session:
            db_user = await get_user_by_username(session=session, username=identifier)
        if db_user:
            return self._convert_dbuser_to_PersistedUser(db_user)
        return None

    # async def create_user(self, user: User) -> Optional[PersistedUser]:
    #     existing_user: Optional["PersistedUser"] = await self.get_user(user.identifier)
    #     user_dict: Dict[str, Any] = {
    #         "identifier": str(user.identifier),
    #         "metadata": json.dumps(user.metadata) or {},
    #     }
    #     if not existing_user:  # create the user
    #         user_dict["id"] = str(uuid.uuid4())
    #         user_dict["createdAt"] = await self.get_current_timestamp()
    #         query = """INSERT INTO users ("id", "identifier", "createdAt", "metadata") VALUES (:id, :identifier, :createdAt, :metadata)"""
    #         await self.execute_sql(query=query, parameters=user_dict)
    #     else:  # update the user
    #         query = """UPDATE users SET "metadata" = :metadata WHERE "identifier" = :identifier"""
    #         await self.execute_sql(
    #             query=query, parameters=user_dict
    #         )  # We want to update the metadata
    #     return await self.get_user(user.identifier)

    async def create_user(self, user: ClUser) -> Optional[PersistedUser]:
        """注意： 这里似乎 会在聊天用户会话开始时就会被调用，功能更像是 获取用户信息，而不是创建用户"""
        # existing_user: Optional["PersistedUser"] = await self.get_user(user.identifier)
        # user_dict: Dict[str, Any] = {
        #     "identifier": str(user.identifier),
        #     "metadata": json.dumps(user.metadata) or {},
        # }

        # async with Session(self.engine) as session:
        #     if not existing_user:  # create the user
        #         create_user(
        #             session=session,
        #             user_create=UserCreate(password="888888", username=user.identifier),
        #         )
        #         # user_dict["id"] = str(uuid.uuid4())
        #         # user_dict["createdAt"] = await self.get_current_timestamp()
        #         # new_user = User(**user_dict)
        #         # session.add(new_user)
        #     else:  # update the user
        #         # stmt = select(User).where(User.identifier == user.identifier)
        #         # result = await session.execute(stmt)
        #         # db_user = result.scalar_one_or_none()
        #         # if db_user:
        #         #     db_user.metadata = user_dict["metadata"]
        #         update_user(session=session, )
        #     await session.commit()
        return await self.get_user(user.identifier)

    ###### Threads ######
    async def get_thread_author(self, thread_id: str) -> str:
        logger.info(f"get_thread_author thread_id={thread_id}")
        async with get_async_session() as session:
            result = await session.exec(
                select(ChatThread).where(ChatThread.id == thread_id)
            )
            thread = result.one()
            if thread:
                logger.info(
                    f"get_thread_author thread.user_identifier={thread.user_identifier}"
                )
                return thread.user_identifier
            else:
                logger.info("get_thread_author thread not found")
                return None

    async def get_thread(self, thread_id: str) -> Optional[ThreadDict]:
        user_threads: Optional[List[ThreadDict]] = await self.get_all_user_threads(
            thread_id=thread_id
        )
        if user_threads:
            return user_threads[0]
        else:
            return None

    async def update_thread(
        self,
        thread_id: str,
        name: Optional[str] = None,
        user_id: Optional[str] = None,
        metadata: Optional[Dict] = None,
        tags: Optional[List[str]] = None,
    ):
        if context.session.user is None:
            raise ValueError("User not found in session context")
        if context.session.user.id is None:
            raise ValueError("User identifier not found in session context")

        user_id = user_id or context.session.user.id

        async with get_async_session() as session:
            # 首先，获取现有的 thread
            stmt = select(ChatThread).where(ChatThread.id == thread_id)
            result = await session.exec(stmt)
            existing_thread = result.one_or_none()

            # 这里可以考虑 使用 upsert 单个sql 实现数据的更新或插入，但是会将逻辑变得复杂。
            if existing_thread is None:
                # 如果 thread 不存在，创建一个新的
                new_thread = ChatThread(
                    id=thread_id,
                    user_identifier=str(user_id),
                    meta=metadata or {},
                    tags=tags,
                    user_id=user_id,
                    name=name or "no title",
                )
                session.add(new_thread)
            else:
                # 如果 thread 存在，只更新提供的非 None 值
                if name is not None:
                    existing_thread.name = name
                if user_id is not None:
                    existing_thread.user_identifier = str(user_id)
                    existing_thread.user_id = user_id
                if metadata is not None:
                    existing_thread.meta = metadata
                if tags is not None:
                    existing_thread.tags = tags
            await session.commit()

        logger.info(f"update_thread 操作成功, thread_id={thread_id}")

    async def delete_thread(self, thread_id: str):
        # Delete feedbacks/elements/steps/thread
        feedbacks_query = """DELETE FROM feedbacks WHERE "forId" IN (SELECT "id" FROM steps WHERE "threadId" = :id)"""
        elements_query = """DELETE FROM elements WHERE "threadId" = :id"""
        steps_query = """DELETE FROM steps WHERE "threadId" = :id"""
        thread_query = """DELETE FROM threads WHERE "id" = :id"""
        parameters = {"id": thread_id}
        await self.execute_sql(query=feedbacks_query, parameters=parameters)
        await self.execute_sql(query=elements_query, parameters=parameters)
        await self.execute_sql(query=steps_query, parameters=parameters)
        await self.execute_sql(query=thread_query, parameters=parameters)

    async def list_threads(
        self, pagination: Pagination, filters: ThreadFilter
    ) -> PaginatedResponse:
        try:
            if not filters.userId:
                raise ValueError("userId is required")
            all_user_threads: List[ThreadDict] = (
                await self.get_all_user_threads(user_id=filters.userId) or []
            )

            search_keyword = filters.search.lower() if filters.search else None
            feedback_value = int(filters.feedback) if filters.feedback else None

            filtered_threads = []
            for thread in all_user_threads:
                keyword_match = True
                feedback_match = True
                if search_keyword or feedback_value is not None:
                    if search_keyword:
                        keyword_match = any(
                            search_keyword in step["output"].lower()
                            for step in thread["steps"]
                            if "output" in step
                        )
                    if feedback_value is not None:
                        feedback_match = False  # Assume no match until found
                        for step in thread["steps"]:
                            feedback = step.get("feedback")
                            if feedback and feedback.get("value") == feedback_value:
                                feedback_match = True
                                break
                if keyword_match and feedback_match:
                    filtered_threads.append(thread)

            start = 0
            if pagination.cursor:
                for i, thread in enumerate(filtered_threads):
                    if (
                        thread["id"] == pagination.cursor
                    ):  # Find the start index using pagination.cursor
                        start = i + 1
                        break
            end = start + pagination.first
            paginated_threads = filtered_threads[start:end] or []

            has_next_page = len(filtered_threads) > end
            start_cursor = paginated_threads[0]["id"] if paginated_threads else None
            end_cursor = paginated_threads[-1]["id"] if paginated_threads else None

            return PaginatedResponse(
                pageInfo=PageInfo(
                    hasNextPage=has_next_page,
                    startCursor=str(start_cursor),
                    endCursor=str(end_cursor),
                ),
                data=paginated_threads,
            )
        except Exception as e:
            import traceback

            error_stack = traceback.format_exc()
            logger.error(f"Error in list_threads: {str(e)}\n{error_stack}")

    ###### Steps ######
    @queue_until_user_message()
    async def create_step(self, step_dict: "StepDict"):
        """upsert chat step"""
        step_dict["show_input"] = (
            str(step_dict.get("showInput", "")).lower()
            if "showInput" in step_dict
            else None
        )

        chat_step = ChatStep(
            id=step_dict.get("id"),
            name=step_dict.get("name"),
            type=step_dict.get("type"),
            thread_id=step_dict.get("threadId"),
            parent_id=step_dict.get("parentId"),
            disable_feedback=step_dict.get("disableFeedback", False),
            streaming=step_dict.get("streaming", False),
            wait_for_answer=step_dict.get("waitForAnswer"),
            is_error=step_dict.get("isError"),
            meta=step_dict.get("metadata", {}),
            tags=step_dict.get("tags", []),
            input=step_dict.get("input"),
            output=step_dict.get("output"),
            created_at=step_dict.get("createdAt"),
            start=step_dict.get("start"),
            end=step_dict.get("end"),
            generation=step_dict.get("generation", {}),
            show_input=step_dict.get("show_input"),
            language=step_dict.get("language"),
            indent=step_dict.get("indent"),
        )

        # async with AsyncSession(get_async_engine()) as session:
        async with get_async_session() as session:
            await ChatStep.upsert(chat_step, session)
            await session.commit()

        return chat_step

    @queue_until_user_message()
    async def update_step(self, step_dict: "StepDict"):
        await self.create_step(step_dict)

    @queue_until_user_message()
    async def delete_step(self, step_id: str):
        feedbacks_query = """DELETE FROM feedbacks WHERE "forId" = :id"""
        elements_query = """DELETE FROM elements WHERE "forId" = :id"""
        steps_query = """DELETE FROM steps WHERE "id" = :id"""
        parameters = {"id": step_id}
        await self.execute_sql(query=feedbacks_query, parameters=parameters)
        await self.execute_sql(query=elements_query, parameters=parameters)
        await self.execute_sql(query=steps_query, parameters=parameters)

    ###### Feedback ######
    async def upsert_feedback(self, feedback: Feedback) -> str:
        feedback.id = feedback.id or str(uuid.uuid4())
        feedback_dict = asdict(feedback)
        parameters = {
            key: value for key, value in feedback_dict.items() if value is not None
        }

        columns = ", ".join(f'"{key}"' for key in parameters.keys())
        values = ", ".join(f":{key}" for key in parameters.keys())
        updates = ", ".join(
            f'"{key}" = :{key}' for key in parameters.keys() if key != "id"
        )
        query = f"""
            INSERT INTO feedbacks ({columns})
            VALUES ({values})
            ON CONFLICT (id) DO UPDATE
            SET {updates};
        """
        await self.execute_sql(query=query, parameters=parameters)
        return feedback.id

    async def delete_feedback(self, feedback_id: str) -> bool:
        if self.show_logger:
            logger.info(f"SQLAlchemy: delete_feedback, feedback_id={feedback_id}")
        query = """DELETE FROM feedbacks WHERE "id" = :feedback_id"""
        parameters = {"feedback_id": feedback_id}
        await self.execute_sql(query=query, parameters=parameters)
        return True

    ###### Elements ######
    @queue_until_user_message()
    async def create_element(self, element: "Element"):
        if not getattr(context.session.user, "id", None):
            raise ValueError("No authenticated user in context")
        if not self.storage_provider:
            logger.warn(
                "SQLAlchemy: create_element error. No blob_storage_client is configured!"
            )
            return
        if not element.for_id:
            return

        content: Optional[Union[bytes, str]] = None

        if element.path:
            async with aiofiles.open(element.path, "rb") as f:
                content = await f.read()
        elif element.url:
            async with aiohttp.ClientSession() as session:
                async with session.get(element.url) as response:
                    if response.status == 200:
                        content = await response.read()
                    else:
                        content = None
        elif element.content:
            content = element.content
        else:
            raise ValueError("Element url, path or content must be provided")
        if content is None:
            raise ValueError("Content is None, cannot upload file")

        context_user = context.session.user

        user_folder = getattr(context_user, "id", "unknown")
        file_object_key = f"{user_folder}/{element.id}" + (
            f"/{element.name}" if element.name else ""
        )

        if not element.mime:
            element.mime = "application/octet-stream"

        uploaded_file = await self.storage_provider.upload_file(
            object_key=file_object_key, data=content, mime=element.mime, overwrite=True
        )
        if not uploaded_file:
            raise ValueError(
                "SQLAlchemy Error: create_element, Failed to persist data in storage_provider"
            )

        element_dict: ElementDict = element.to_dict()

        element_dict["url"] = uploaded_file.get("url")
        element_dict["objectKey"] = uploaded_file.get("object_key")
        element_dict_cleaned = {k: v for k, v in element_dict.items() if v is not None}

        columns = ", ".join(f'"{column}"' for column in element_dict_cleaned.keys())
        placeholders = ", ".join(f":{column}" for column in element_dict_cleaned.keys())
        query = f"INSERT INTO elements ({columns}) VALUES ({placeholders})"
        await self.execute_sql(query=query, parameters=element_dict_cleaned)

    @queue_until_user_message()
    async def delete_element(self, element_id: str, thread_id: Optional[str] = None):
        if self.show_logger:
            logger.info(f"SQLAlchemy: delete_element, element_id={element_id}")
        query = """DELETE FROM elements WHERE "id" = :id"""
        parameters = {"id": element_id}
        await self.execute_sql(query=query, parameters=parameters)

    async def delete_user_session(self, id: str) -> bool:
        return False  # Not sure why documentation wants this

    async def get_all_user_threads(
        self, user_id: Optional[str] = None, thread_id: Optional[str] = None
    ) -> Optional[List[ThreadDict]]:
        """Fetch all user threads up to self.user_thread_limit, or one thread by id if thread_id is provided."""

        async with get_async_session() as session:
            return await get_user_threads(
                session=session,
                user_id=user_id,
                thread_id=thread_id,
                limit=user_thread_limit,
            )
        # return user_threads_results
        # if not user_threads_results:
        #     return []

        # steps_feedbacks_query = f"""
        #     SELECT
        #         s."id" AS step_id,
        #         s."name" AS step_name,
        #         s."type" AS step_type,
        #         s."threadId" AS step_threadid,
        #         s."parentId" AS step_parentid,
        #         s."streaming" AS step_streaming,
        #         s."waitForAnswer" AS step_waitforanswer,
        #         s."isError" AS step_iserror,
        #         s."metadata" AS step_metadata,
        #         s."tags" AS step_tags,
        #         s."input" AS step_input,
        #         s."output" AS step_output,
        #         s."createdAt" AS step_createdat,
        #         s."start" AS step_start,
        #         s."end" AS step_end,
        #         s."generation" AS step_generation,
        #         s."showInput" AS step_showinput,
        #         s."language" AS step_language,
        #         s."indent" AS step_indent,
        #         f."value" AS feedback_value,
        #         f."comment" AS feedback_comment
        #     FROM steps s LEFT JOIN feedbacks f ON s."id" = f."forId"
        #     WHERE s."threadId" IN {thread_ids}
        #     ORDER BY s."createdAt" ASC
        # """
        # steps_feedbacks = await self.execute_sql(
        #     query=steps_feedbacks_query, parameters={}
        # )
        # async with get_async_session() as session:
        #     thread_ids = await user_threads(
        #         session=session,
        #         user_id=user_id,
        #         thread_id=thread_id,
        #         limit=user_thread_limit,
        #     )

        # elements_query = f"""
        #     SELECT
        #         e."id" AS element_id,
        #         e."threadId" as element_threadid,
        #         e."type" AS element_type,
        #         e."chainlitKey" AS element_chainlitkey,
        #         e."url" AS element_url,
        #         e."objectKey" as element_objectkey,
        #         e."name" AS element_name,
        #         e."display" AS element_display,
        #         e."size" AS element_size,
        #         e."language" AS element_language,
        #         e."page" AS element_page,
        #         e."forId" AS element_forid,
        #         e."mime" AS element_mime
        #     FROM elements e
        #     WHERE e."threadId" IN {thread_ids}
        # """
        # elements = await self.execute_sql(query=elements_query, parameters={})

        # thread_dicts = {}
        # for thread in user_threads:
        #     thread_id = thread["thread_id"]
        #     if thread_id is not None:
        #         thread_dicts[thread_id] = ThreadDict(
        #             id=thread_id,
        #             createdAt=thread["thread_createdat"],
        #             name=thread["thread_name"],
        #             userId=thread["user_id"],
        #             userIdentifier=thread["user_identifier"],
        #             tags=thread["thread_tags"],
        #             metadata=thread["thread_metadata"],
        #             steps=[],
        #             elements=[],
        #         )
        # # Process steps_feedbacks to populate the steps in the corresponding ThreadDict
        # if isinstance(steps_feedbacks, list):
        #     for step_feedback in steps_feedbacks:
        #         thread_id = step_feedback["step_threadid"]
        #         if thread_id is not None:
        #             feedback = None
        #             if step_feedback["feedback_value"] is not None:
        #                 feedback = FeedbackDict(
        #                     forId=step_feedback["step_id"],
        #                     id=step_feedback.get("feedback_id"),
        #                     value=step_feedback["feedback_value"],
        #                     comment=step_feedback.get("feedback_comment"),
        #                 )
        #             step_dict = StepDict(
        #                 id=step_feedback["step_id"],
        #                 name=step_feedback["step_name"],
        #                 type=step_feedback["step_type"],
        #                 threadId=thread_id,
        #                 parentId=step_feedback.get("step_parentid"),
        #                 streaming=step_feedback.get("step_streaming", False),
        #                 waitForAnswer=step_feedback.get("step_waitforanswer"),
        #                 isError=step_feedback.get("step_iserror"),
        #                 metadata=(
        #                     step_feedback["step_metadata"]
        #                     if step_feedback.get("step_metadata") is not None
        #                     else {}
        #                 ),
        #                 tags=step_feedback.get("step_tags"),
        #                 input=(
        #                     step_feedback.get("step_input", "")
        #                     if step_feedback["step_showinput"] == "true"
        #                     else None
        #                 ),
        #                 output=step_feedback.get("step_output", ""),
        #                 createdAt=step_feedback.get("step_createdat"),
        #                 start=step_feedback.get("step_start"),
        #                 end=step_feedback.get("step_end"),
        #                 generation=step_feedback.get("step_generation"),
        #                 showInput=step_feedback.get("step_showinput"),
        #                 language=step_feedback.get("step_language"),
        #                 indent=step_feedback.get("step_indent"),
        #                 feedback=feedback,
        #             )
        #             # Append the step to the steps list of the corresponding ThreadDict
        #             thread_dicts[thread_id]["steps"].append(step_dict)

        # if isinstance(elements, list):
        #     for element in elements:
        #         thread_id = element["element_threadid"]
        #         if thread_id is not None:
        #             element_dict = ElementDict(
        #                 id=element["element_id"],
        #                 threadId=thread_id,
        #                 type=element["element_type"],
        #                 chainlitKey=element.get("element_chainlitkey"),
        #                 url=element.get("element_url"),
        #                 objectKey=element.get("element_objectkey"),
        #                 name=element["element_name"],
        #                 display=element["element_display"],
        #                 size=element.get("element_size"),
        #                 language=element.get("element_language"),
        #                 autoPlay=element.get("element_autoPlay"),
        #                 playerConfig=element.get("element_playerconfig"),
        #                 page=element.get("element_page"),
        #                 forId=element.get("element_forid"),
        #                 mime=element.get("element_mime"),
        #             )
        #             thread_dicts[thread_id]["elements"].append(element_dict)  # type: ignore

        # return list(thread_dicts.values())

    async def get_all_user_feedbacks(
        self, thread_ids: list[str] = None
    ) -> Optional[List[FeedbackDict]]:
        pass
