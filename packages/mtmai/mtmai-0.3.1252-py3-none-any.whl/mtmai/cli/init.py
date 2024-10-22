"""部署相关的子命令"""

import asyncio

from mtmai.core.logging import get_logger

logger = get_logger()


def register_init_commands(cli):
    @cli.command()
    def init():
        from mtmai.mtlibs import dev_helper
        from mtmlib.mtutils import is_in_gitpod

        dev_helper.init_project()

        if is_in_gitpod():
            import threading

            from mtmlib import tunnel

            threading.Thread(
                target=lambda: asyncio.run(tunnel.start_cloudflared())
            ).start()

            from mtmai.mtlibs.server.kasmvnc import run_kasmvnc

            threading.Thread(target=run_kasmvnc).start()
