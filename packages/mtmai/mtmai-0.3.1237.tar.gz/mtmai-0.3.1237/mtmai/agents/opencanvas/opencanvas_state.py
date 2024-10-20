from typing import Annotated

from langgraph.graph.message import add_messages
from pydantic import BaseModel


class Highlight(BaseModel):
    id: str
    startCharIndex: int
    endCharIndex: int


class OpenCanvasState(BaseModel):
    messages: Annotated[list, add_messages] = []
    selectedArtifactId: str | None = None
    highlighted: Highlight | None = None
    next: str | None = None
    siteId: str | None = None
