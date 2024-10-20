import asyncio

from mtmai.core.config import settings
from mtmai.core.logging import get_logger
from mtmai.server import serve

logger = get_logger()


class CliServe:
    """启动http 服务器"""

    def run(self, *args, **kwargs) -> None:
        """运行子命令"""
        logger.info("🚀 call serve : %s:%s", settings.HOSTNAME, settings.PORT)
        asyncio.run(serve())


def register_serve_commands(cli):
    @cli.command()
    def serve():
        CliServe().run()
