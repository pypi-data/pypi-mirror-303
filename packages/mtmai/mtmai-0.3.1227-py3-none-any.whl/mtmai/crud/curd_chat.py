import logging
from typing import Optional

from sqlmodel import desc, select
from sqlmodel.ext.asyncio.session import AsyncSession

from mtmai.models.chat import ChatFeedback, ChatStep, ChatThread

logger = logging.getLogger()


async def get_user_threads(
    session: AsyncSession,
    user_id: str,
    thread_id: str = None,
    limit: int = 100,
    skip: int = 0,
) -> Optional[list[dict]]:
    """
    获取用户的 chat threads , 包含 steps 和 feedbacks
    """
    query = (
        select(ChatThread)
        .where((ChatThread.user_id == user_id) | (ChatThread.id == thread_id))
        .order_by(desc(ChatThread.created_at))
        .limit(limit)
        .offset(skip)
    )

    result = await session.execute(query)
    user_threads = result.scalars().all()

    if not user_threads:
        return None

    thread_ids = [thread.id for thread in user_threads]

    steps_feedbacks_query = (
        select(ChatStep, ChatFeedback)
        .join(ChatFeedback, ChatStep.id == ChatFeedback.for_id, isouter=True)
        .where(ChatStep.thread_id.in_(thread_ids))
        .order_by(ChatStep.created_at)
    )

    steps_feedbacks_result = await session.exec(steps_feedbacks_query)
    steps_feedbacks = steps_feedbacks_result.all()

    threads_dict = []

    # convert to chainlit  user_threads format
    for thread in user_threads:
        thread_dict = {
            "id": str(thread.id),
            "createdAt": thread.created_at.isoformat(),
            "name": thread.name,
            "userId": str(thread.user_id),
            "userIdentifier": thread.user_identifier,
            "tags": thread.tags,
            "metadata": thread.meta,
            "steps": [],
        }

        for step, feedback in steps_feedbacks:
            if str(step.thread_id) == str(thread.id):
                step_dict = {
                    "id": str(step.id),
                    "name": step.name,
                    "type": step.type,
                    "threadId": str(step.thread_id) if step.thread_id else None,
                    "parentId": str(step.parent_id) if step.parent_id else None,
                    "streaming": step.streaming,
                    "waitForAnswer": step.wait_for_answer,
                    "isError": step.is_error,
                    "metadata": step.meta,
                    "tags": step.tags,
                    "input": step.input,
                    "output": step.output,
                    "createdAt": step.created_at.isoformat(),
                    "start": step.start.isoformat() if step.start else None,
                    "end": step.end.isoformat() if step.end else None,
                    "generation": step.generation,
                    "showInput": step.show_input,
                    "language": step.language,
                    "indent": step.indent,
                    "feedback": {
                        "value": feedback.value if feedback else None,
                        "comment": feedback.comment if feedback else None,
                    },
                }
                thread_dict["steps"].append(step_dict)

        threads_dict.append(thread_dict)

    return threads_dict
