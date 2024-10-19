import logging

import httpx
from fastapi import APIRouter, Depends
from fastapi.openapi.docs import get_redoc_html, get_swagger_ui_oauth2_redirect_html
from opentelemetry import trace
from pydantic import BaseModel
from pydantic.networks import EmailStr

from mtmai.core.config import settings
from mtmai.deps import get_current_active_superuser
from mtmai.models.agent import ChatBotUiStateResponse
from mtmai.models.chat import ChatProfile, ListViewProps, ThreadUIState
from mtmai.models.models import Message
from mtmai.mtlibs.inputs.input_widget import ThreadForm
from mtmai.utils import generate_test_email, send_email
from mtmlib.decorators.mtform.mtform import MtForm

tracer = trace.get_tracer_provider().get_tracer(__name__)
logger = logging.getLogger()


router = APIRouter()


@router.get("/health", include_in_schema=False)
async def health_check():
    with tracer.start_as_current_span("health-span"):
        logger.info("get /health")
        current_span = trace.get_current_span()
        current_span.add_event("This is a span event")
        logger.warning("This is a log message")
        return {"health": True}


@router.get("/swagger-ui-oauth2-redirect", include_in_schema=False)
async def swagger_ui_redirect():
    return get_swagger_ui_oauth2_redirect_html()


@router.get("/redoc", include_in_schema=False)
async def redoc_html():
    return get_redoc_html(
        openapi_url=router.app().openapi_url,
        title=router.app().title + " - ReDoc",
        redoc_js_url="https://unpkg.com/redoc@next/bundles/redoc.standalone.js",
    )


@router.get("/info", include_in_schema=False)
async def app_info():
    return {
        "app_name": settings.app_name,
        "admin_email": settings.admin_email,
        "items_per_user": settings.items_per_user,
    }


@router.post(
    "/test-email/",
    dependencies=[Depends(get_current_active_superuser)],
    status_code=201,
    include_in_schema=False,
)
def test_email(email_to: EmailStr) -> Message:
    """
    Test emails.
    """
    email_data = generate_test_email(email_to=email_to)
    send_email(
        email_to=email_to,
        subject=email_data.subject,
        html_content=email_data.html_content,
    )
    return Message(message="Test email sent")


class TestUrlReq(BaseModel):
    url: str


@router.post(
    "/test-url/",
    dependencies=[Depends(get_current_active_superuser)],
    status_code=201,
    include_in_schema=False,
)
async def test_url(req: TestUrlReq):
    client = httpx.AsyncClient()
    response = await client.get(req.url)
    content = response.text
    return content


class TypesResponse(BaseModel):
    """
    如果使用openapi 生成前端代码，缺少了某些类型，请在这里补充
    """

    thread_form: ThreadForm | None = None
    uiState: ChatBotUiStateResponse | None = None
    thread_ui_state: ThreadUIState | None = None
    chat_profile: ChatProfile | None = None
    list_view_props: ListViewProps | None = None
    mt_form: MtForm | None = None


@router.get("/types", include_in_schema=True, response_model=TypesResponse)
async def types():
    """
    无实际功能，仅用于openapi生成前端代码
    """
    return TypesResponse()
