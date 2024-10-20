import glob
import mimetypes
import os
from typing import Optional

from fastapi import APIRouter, HTTPException, Query
from fastapi.responses import FileResponse

from mtmai.core.config import APP_ROOT
from mtmai.core.logging import get_logger
from mtmai.types.types import Theme

logger = get_logger()

router = APIRouter()

mimetypes.add_type("application/javascript", ".js")
mimetypes.add_type("text/css", ".css")


# @router.get("/", include_in_schema=False)
# def home():
#     # return RedirectResponse("/docs")
#     return FileResponse(os.path.join(APP_ROOT, "public", "index.html"))


@router.get("/logo")
async def get_logo(theme: Optional[Theme] = Query(Theme.light)):
    """Get the default logo for the UI."""
    theme_value = theme.value if theme else Theme.light.value
    logo_path = None

    for path in [
        os.path.join(APP_ROOT, "public", f"logo_{theme_value}.*"),
        os.path.join(APP_ROOT, "mtmai/mtmai/public", f"logo_{theme_value}.*"),
        # os.path.join(build_dir, "assets", f"logo_{theme_value}*.*"),
    ]:
        files = glob.glob(path)

        if files:
            logo_path = files[0]
            break

    if not logo_path:
        raise HTTPException(status_code=404, detail="Missing default logo")

    media_type, _ = mimetypes.guess_type(logo_path)

    return FileResponse(logo_path, media_type=media_type)

    # merge_gauge_data(filename)


# @router.get("/flow_hello")
# async def flow_hello():
#     from mtmai.flows.hello_flow import flow_hello

#     flow_hello()
