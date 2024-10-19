from typing import List

from pydantic import BaseModel


class ChapterOutline(BaseModel):
    title: str
    description: str


class BookOutline(BaseModel):
    chapters: List[ChapterOutline]


class Chapter(BaseModel):
    title: str
    content: str


class WriteOutlineRequest(BaseModel):
    """参数: 生成文章大纲"""

    topic: str
    goal: str


class GenBookState(BaseModel):
    title: str | None = (
        "The Current State of AI in September 2024: Trends Across Industries and What's Next"
    )
    book: list[Chapter] | None = []
    book_outline: list[ChapterOutline] | None = []
    topic: str | None = (
        "Exploring the latest trends in AI across different industries as of September 2024"
    )
    goal: str | None = """
        The goal of this book is to provide a comprehensive overview of the current state of artificial intelligence in September 2024.
        It will delve into the latest trends impacting various industries, analyze significant advancements,
        and discuss potential future developments. The book aims to inform readers about cutting-edge AI technologies
        and prepare them for upcoming innovations in the field.
    """
