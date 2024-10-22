import asyncio
import os
import threading

from fastapi import APIRouter, FastAPI, Request
from fastapi.concurrency import asynccontextmanager
from fastapi.responses import JSONResponse
from fastapi.routing import APIRoute
from starlette.templating import Jinja2Templates

from mtmai.api import (
    agent,
    auth,
    blog,
    chat,
    form,
    image,
    listview,
    logs,
    metrics,
    openai,
    site,
    tasks,
    train,
    users,
    webpage,
    workbench,
)
from mtmai.core import coreutils
from mtmai.core.__version__ import version
from mtmai.core.config import settings
from mtmai.core.coreutils import is_in_dev, is_in_vercel
from mtmai.core.logging import get_logger
from mtmai.middleware import AuthMiddleware
from mtmlib import mtutils
from mtmlib.env import is_in_docker, is_in_huggingface, is_in_testing, is_in_windows

logger = get_logger()

api_router = APIRouter()

api_router.include_router(auth.router, tags=["auth"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(blog.router, prefix="/posts", tags=["posts"])
api_router.include_router(image.router, prefix="/image", tags=["image"])
api_router.include_router(train.router, prefix="/train", tags=["train"])
api_router.include_router(metrics.router, prefix="/metrics", tags=["metrics"])
api_router.include_router(agent.router, prefix="/agent", tags=["agent"])
api_router.include_router(chat.router, prefix="/chat", tags=["chat"])
api_router.include_router(form.router, prefix="/form", tags=["form"])
api_router.include_router(site.router, prefix="/site", tags=["site"])
api_router.include_router(webpage.router, prefix="/webpage", tags=["webpage"])
api_router.include_router(tasks.router, prefix="/tasks", tags=["tasks"])
api_router.include_router(openai.router, tags=["openai"])
api_router.include_router(listview.router, prefix="/listview", tags=["listview"])
api_router.include_router(workbench.router, prefix="/workbench", tags=["workbench"])
api_router.include_router(logs.router, prefix="/logs", tags=["logs"])


def build_app():
    @asynccontextmanager
    async def lifespan(app: FastAPI):
        # from mtmai.mtlibs.mq.pq_queue import AsyncPGMQueue

        if not is_in_testing():
            # mq = await AsyncPGMQueue.create(settings.DATABASE_URL)
            # worker = CrawlWorker(mq=mq, engine=get_async_engine())
            # app.state.crawl_worker = worker
            # await worker.start()
            # yield
            # await worker.stop()
            pass
        else:
            yield

    def custom_generate_unique_id(route: APIRoute) -> str:
        if len(route.tags) > 0:
            return f"{route.tags[0]}-{route.name}"
        return f"{route.name}"

    openapi_tags = [
        {
            "name": "admin",
            "description": "管理专用 ",
        },
        {
            "name": "train",
            "description": "模型训练及数据集",
        },
        {
            "name": "mtmcrawler",
            "description": "爬虫数据采集 ",
        },
        {
            "name": "openai",
            "description": "提供兼容 OPEN AI 协议 , 外置工作流 例如 langflow 可以通过此endpoint调用内部的工作流和模型",
        },
    ]

    app = FastAPI(
        # docs_url=None,
        # redoc_url=None,
        title=settings.PROJECT_NAME,
        description="mtmai description(group)",
        version=version,
        lifespan=lifespan,
        generate_unique_id_function=custom_generate_unique_id,
        openapi_url=f"{settings.API_V1_STR}/openapi.json",
        swagger_ui_parameters={
            "syntaxHighlight": True,
            "syntaxHighlight.theme": "obsidian",
        },
        openapi_tags=openapi_tags,
    )
    templates = Jinja2Templates(directory="templates")

    if is_in_dev():
        from mtmai.api import admin

        api_router.include_router(
            admin.router,
            prefix="/admin",
            tags=["admin"],
        )
        from mtmai.api import demos

        api_router.include_router(
            demos.router, prefix="/demos/demos", tags=["demos_demos"]
        )

    # app.openapi_schema = {
    #     "components": {
    #         "schemas": {
    #             "MessagePayload": MessagePayload.model_json_schema(),
    #             "AudioChunkPayload": AudioChunkPayload.model_json_schema(),
    #         }
    #     }
    # }

    @app.exception_handler(Exception)
    async def generic_exception_handler(request: Request, exc: Exception):  # noqa: ARG001
        return JSONResponse(status_code=500, content={"detail": str(exc)})

    def setup_main_routes():
        from mtmai.api import home

        app.include_router(home.router)
        app.include_router(api_router, prefix=settings.API_V1_STR)

    setup_main_routes()

    if settings.OTEL_ENABLED:
        from mtmai.mtlibs import otel

        otel.setup_otel(app)

    if settings.BACKEND_CORS_ORIGINS:
        from fastapi.middleware.cors import CORSMiddleware

        app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"]
            if settings.BACKEND_CORS_ORIGINS == "*"
            else [str(origin).strip("/") for origin in settings.BACKEND_CORS_ORIGINS],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*", "x-chainlit-client-type"],
        )
        app.add_middleware(AuthMiddleware)

    def mount_chainlit_router():
        from mtmai.chainlit.utils import mount_chainlit

        chainit_app_path = os.path.join(os.path.dirname(__file__), "api/chat.py")
        logger.info("chainit_app_path: %s", chainit_app_path)
        mount_chainlit(
            app=app,
            target=chainit_app_path,
            path=settings.API_V1_STR + "/chat",
        )

    mount_chainlit_router()
    return app


async def serve():
    import uvicorn

    app = build_app()
    start_deamon_serve()

    config = uvicorn.Config(
        app,
        host=settings.SERVE_IP,
        port=settings.PORT,
        log_level="info",
        reload=not settings.is_production,
        # !!! bug 当 使用了prefect 后，使用了这个指令： @flow，程序会被卡在： .venv/lib/python3.12/site-packages/uvicorn/config.py
        # !!!365行：logging.config.dictConfig(self.log_config)
        # !!! 原因未知，但是 log_config=None 后，问题消失
        log_config=None,
    )
    host = (
        "127.0.0.1"
        if settings.SERVE_IP == "0.0.0.0"
        else settings.server_host.split("://")[-1]
    )
    server_url = f"{settings.server_host.split('://')[0]}://{host}:{settings.PORT}"

    logger.info("🚀 mtmai api serve on : %s", server_url)
    server = uvicorn.Server(config)
    await server.serve()


def start_deamon_serve():
    """
    启动后台独立服务
    根据具体环境自动启动
    """
    logger.info("start_deamon_serve")

    if is_in_dev():
        from mtmai.flows.deployments import start_prefect_deployment

        start_prefect_deployment(asThreading=True)

    if (
        not settings.is_in_vercel
        and not settings.is_in_gitpod
        and settings.CF_TUNNEL_TOKEN
        and not is_in_huggingface()
        and not is_in_windows()
    ):
        from mtmlib import tunnel

        threading.Thread(target=lambda: asyncio.run(tunnel.start_cloudflared())).start()

        if not is_in_vercel() and not settings.is_in_gitpod:
            from mtmai.mtlibs.server.searxng import run_searxng_server

            threading.Thread(target=run_searxng_server).start()
        if (
            not settings.is_in_vercel
            and not settings.is_in_gitpod
            and not is_in_windows()
        ):

            def start_front_app():
                mtmai_url = coreutils.backend_url_base()
                if not mtutils.command_exists("mtmaiweb"):
                    logger.warning("⚠️ mtmaiweb 命令未安装,跳过前端的启动")
                    return
                mtutils.bash(
                    f"PORT={settings.FRONT_PORT} MTMAI_API_BASE={mtmai_url} mtmaiweb serve"
                )

            threading.Thread(target=start_front_app).start()

            def start_prefect_server():
                logger.info("启动 prefect server")

                sqlite_db_path = "/app/storage/prefect.db"
                sql_connect_str = f"sqlite+aiosqlite:///{sqlite_db_path}"
                mtutils.bash(
                    f"PREFECT_UI_STATIC_DIRECTORY=/app/storage PREFECT_API_DATABASE_CONNECTION_URL={sql_connect_str} prefect server start"
                )

            threading.Thread(target=start_prefect_server).start()

        if not is_in_vercel() and not settings.is_in_gitpod and not is_in_windows():
            from mtmai.mtlibs.server.kasmvnc import run_kasmvnc

            threading.Thread(target=run_kasmvnc).start()

        if is_in_docker():
            from mtmai.mtlibs.server.easyspider import run_easy_spider_server

            threading.Thread(target=run_easy_spider_server).start()

    logger.info("start_deamon_serve end")
