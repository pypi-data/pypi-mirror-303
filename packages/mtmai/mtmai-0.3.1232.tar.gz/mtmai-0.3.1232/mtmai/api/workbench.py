from fastapi import APIRouter
from pydantic import BaseModel

from mtmai.assistants.assistants import get_assistant_agent
from mtmai.core.logging import get_logger
from mtmai.deps import OptionalUserDep, SessionDep
from mtmai.models.chat import AssisantConfig

router = APIRouter()
logger = get_logger()


class WorkbenchConfigRequest(BaseModel):
    profile: str


@router.post("/workbench/config", response_model=AssisantConfig)
async def workbench_config(
    request: WorkbenchConfigRequest, user: OptionalUserDep, db: SessionDep
):
    assistant_agent = await get_assistant_agent(request.profile)
    config = await assistant_agent.get_config()
    return config
