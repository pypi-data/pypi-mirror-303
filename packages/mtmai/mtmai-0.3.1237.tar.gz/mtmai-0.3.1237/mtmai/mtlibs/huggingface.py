import logging
from pathlib import Path

from fastapi import APIRouter
from mtmlib.mtutils import bash

from mtmai.core.config import settings

router = APIRouter()
logger = logging.getLogger()


def hf_trans1_clone():
    target_dir = (
        Path(settings.storage_dir)
        .joinpath(settings.gitsrc_dir)
        .joinpath(settings.HUGGINGFACEHUB_DEFAULT_WORKSPACE)
    )
    if not Path(target_dir).exists():
        cmd = f"git clone --depth=1 https://{settings.HUGGINGFACEHUB_USER}:{settings.HUGGINGFACEHUB_API_TOKEN}@huggingface.co/spaces/{settings.HUGGINGFACEHUB_USER}/{settings.HUGGINGFACEHUB_DEFAULT_WORKSPACE} {target_dir}"
        bash(cmd)
