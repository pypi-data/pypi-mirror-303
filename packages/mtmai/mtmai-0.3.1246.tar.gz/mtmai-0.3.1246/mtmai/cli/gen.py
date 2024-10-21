"""客户端代码生成"""

import json
import logging
from pathlib import Path

from mtmlib.mtutils import bash


def register_gen_commands(cli):
    logger = logging.getLogger()

    @cli.command()
    def gen():
        from mtmai.core.config import settings
        from mtmai.server import build_app

        app = build_app()
        openapi = app.openapi()
        with Path(settings.OPENAPI_JSON_PATH).open("w") as f:
            logger.info(
                "openapi.json exported %s to %s",
                openapi.get("openapi", "unknown version"),
                settings.OPENAPI_JSON_PATH,
            )
            json.dump(openapi, f, indent=2)
        # 生成python 客户端代码（用不上，暂时去掉此功能）
        # if not mtutils.command_exists("openapi-python-client"):
        #     bash(
        #         "pip install openapi-python-client && openapi-python-client --install-completion"
        #     )

        #     def refresh_path():
        #         # Refresh the PATH to ensure the newly installed command is available
        #         import os
        #         import sys

        #         # Get the current PATH
        #         current_path = os.environ.get("PATH", "")

        #         # Split the PATH into individual directories
        #         path_dirs = current_path.split(os.pathsep)

        #         # Add potential new directories where pip might have installed the package
        #         new_dirs = [
        #             os.path.expanduser("~/.local/bin"),  # For Unix-like systems
        #             os.path.join(sys.prefix, "Scripts"),  # For Windows
        #         ]

        #         # Add new directories to the PATH if they're not already there
        #         for new_dir in new_dirs:
        #             if os.path.exists(new_dir) and new_dir not in path_dirs:
        #                 path_dirs.insert(0, new_dir)

        #         # Join the directories back into a PATH string
        #         new_path = os.pathsep.join(path_dirs)

        #         # Update the system PATH
        #         os.environ["PATH"] = new_path

        #         # If on Windows, also update the PATH for the current process
        #         if sys.platform.startswith("win"):
        #             import win32gui
        #             import win32process

        #             HWND_BROADCAST = 0xFFFF
        #             WM_SETTINGCHANGE = 0x001A
        #             SMTO_ABORTIFHUNG = 0x0002

        #             result = win32gui.SendMessageTimeout(
        #                 HWND_BROADCAST,
        #                 WM_SETTINGCHANGE,
        #                 0,
        #                 "Environment",
        #                 SMTO_ABORTIFHUNG,
        #                 5000,
        #             )
        #             if result[0] != 0:  # Success
        #                 win32process.SetEnvironmentVariable("PATH", new_path)

        #     refresh_path()
        # if mtutils.command_exists("openapi-python-client"):
        #     bash(
        #         "openapi-python-client generate --path mtmai/mtmai/openapi.json --overwrite"
        #     )
        # else:
        #     logger.error(
        #         "Failed to install or locate openapi-python-client. Please try running the command again."
        #     )

        # typescript 客户端库
        bash("cd packages/mtmaiapi && bun run gen")
