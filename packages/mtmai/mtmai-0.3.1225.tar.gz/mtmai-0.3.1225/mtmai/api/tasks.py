"""
任务调用api
"""

from fastapi import APIRouter, Depends, Query
from sqlmodel import Session, func, select

from mtmai.core.db import get_session
from mtmai.deps import AsyncSessionDep, CurrentUser
from mtmai.models.task import MtTask, TaskCreateRequest, TaskListResponse
from pydantic import BaseModel

router = APIRouter()


@router.get("/tasks", response_model=TaskListResponse)
async def task_list(
    *,
    session: Session = Depends(get_session),
    query: str = Query(default=""),
    skip: int = 0,
    user: CurrentUser,
    limit: int = Query(default=100, le=100),
):
    if user.is_superuser:
        count_statement = select(func.count()).select_from(MtTask)
        count = session.exec(count_statement).one()
        statement = select(MtTask).offset(skip).limit(limit)
        items = session.exec(statement).all()
    else:
        count_statement = (
            select(func.count()).select_from(MtTask).where(MtTask.owner_id == user.id)
        )
        count = session.exec(count_statement).one()
        statement = (
            select(MtTask).where(MtTask.owner_id == user.id).offset(skip).limit(limit)
        )
        items = session.exec(statement).all()

    return TaskListResponse(data=items, count=count)

    # class TaskCreateRequest(BaseModel):
    #     site_id: str
    #     title: str
    #     description: str
    #     payload: dict

class TaskCreateResponse(BaseModel):
    id: str

@router.post("/", response_model=TaskCreateResponse)
async def create_task(
    *,
    session: AsyncSessionDep,
    current_user: CurrentUser,
    item_in: TaskCreateRequest,
) :
    """
    Create new task.
    """
    task = await create_task(session, item_in, current_user.id)
    return TaskCreateResponse(id=task.id)
    # await session.refresh(task)
    # return TaskCreateResponse(id=task.id)


# async def state_change_handler(task, run, state: State):
#     """处理状态变化的钩子函数"""
#     event = {
#         "task_name": task.name,
#         "state_name": state.name,
#         "state_type": state.type.value,
#         "message": state.message,
#     }
#     if run.flow_run_id in workflow_queues:
#         await workflow_queues[run.flow_run_id].put(event)


# @task(on_completion=[state_change_handler], on_failure=[state_change_handler])
# async def task1():
#     await asyncio.sleep(2)
#     return "Task 1 result"


# @task(on_completion=[state_change_handler], on_failure=[state_change_handler])
# async def task2():
#     await asyncio.sleep(3)
#     return "Task 2 result"


# @flow(on_completion=[state_change_handler], on_failure=[state_change_handler])
# async def my_workflow():
#     result1 = await task1()
#     result2 = await task2()
#     return f"{result1}, {result2}"


# async def event_generator(flow_run_id: str):
#     async with get_client() as client:
#         flow_run = await client.read_flow_run(flow_run_id)

#         if flow_run.state.is_final():
#             yield f"data: {json.dumps({'task_name': 'my_workflow', 'state_name': flow_run.state.name, 'result': flow_run.state.result()})}\n\n"
#             return

#         queue = asyncio.Queue()
#         workflow_queues[flow_run_id] = queue

#         try:
#             # 在后台运行工作流（如果尚未运行）
#             if not flow_run.state.is_running():
#                 workflow_task = asyncio.create_task(
#                     get_workflow(flow_run_id=flow_run_id)
#                 )

#             while True:
#                 event = await queue.get()
#                 yield f"data: {json.dumps(event)}\n\n"

#                 if event["task_name"] == "my_workflow" and event["state_type"] in [
#                     "COMPLETED",
#                     "FAILED",
#                 ]:
#                     break
#         finally:
#             del workflow_queues[flow_run_id]


# @flow(cache_result_in_memory=False)
# @router.post("/workflow/article_gen/start")
# async def start_workflow_article_gen(
#     user: OptionalUserDep, req: ArticleGenStateRequest
# ):
#     if not user:
#         raise HTTPException(status_code=400, detail="User not found")
#     req.user_id = str(user.id)
#     result = await flow_article_gen(req=req)
#     return result


# @router.get("/workflow/stream/{flow_run_id}")
# async def stream_workflow(flow_run_id: str, request: Request):
#     if flow_run_id not in workflow_queues:
#         # 检查工作流是否存在
#         async with get_client() as client:
#             try:
#                 await client.read_flow_run(flow_run_id)
#             except Exception:
#                 raise HTTPException(status_code=404, detail="Flow run not found")

#     return StreamingResponse(
#         event_generator(flow_run_id),
#         media_type="text/event-stream",
#         headers={
#             "Content-Type": "text/event-stream",
#             "Cache-Control": "no-cache",
#             "Connection": "keep-alive",
#         },
#     )


# @flow
# @router.get("/workflow/flow_example1")
# async def flow_example1(request: Request):
#     return await flow_hello()
