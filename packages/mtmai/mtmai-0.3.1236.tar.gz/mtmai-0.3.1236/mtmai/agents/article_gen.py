import asyncio
from textwrap import dedent

from fastapi import APIRouter
from pydantic import BaseModel

from mtmai.agents.ctx import mtmai_context
from mtmai.core.logging import get_logger
from mtmai.crewai import Agent, Crew, Process, Task
from mtmai.models.book_gen import BookOutline, Chapter, ChapterOutline

router = APIRouter()

logger = get_logger()


# class WriteOutlineRequest(BaseModel):
#     """参数: 生成文章大纲"""

#     topic: str
#     goal: str


# @router.get("/article_gen_outline")
# async def article_gen_outline(*, req: WriteOutlineRequest):
#     """生成文章大纲"""
#     llm = await mtmai_context.get_crawai_llm()

#     researcher_agent = Agent(
#         role="Research Agent",
#         goal=dedent("""Gather comprehensive information about {topic} that will be used to create an organized and well-structured book outline.
# Here is some additional information about the author's desired goal for the book:\n\n {goal}"""),
#         backstory=dedent("""You're a seasoned researcher, known for gathering the best sources and understanding the key elements of any topic.
# You aim to collect all relevant information so the book outline can be accurate and informative."""),
#         # tools=[search_tool],
#         tools=[],
#         llm=llm,
#         verbose=True,
#     )
#     outliner_agent = Agent(
#         role="Book Outlining Agent",
#         goal=dedent("""Based on the research, generate a book outline about the following topic: {topic}
# The generated outline should include all chapters in sequential order and provide a title and description for each chapter.
# Here is some additional information about the author's desired goal for the book:\n\n {goal}"""),
#         backstory=dedent("""You are a skilled organizer, great at turning scattered information into a structured format.
# Your goal is to create clear, concise chapter outlines with all key topics and subtopics covered."""),
#         llm=llm,
#         verbose=True,
#     )

#     research_topic_task = Task(
#         description=dedent("""Research the provided topic of {topic} to gather the most important information that will
# be useful in creating a book outline. Ensure you focus on high-quality, reliable sources.

# Here is some additional information about the author's desired goal for the book:\n\n {goal}
#         """),
#         expected_output="A set of key points and important information about {topic} that will be used to create the outline.",
#         agent=researcher_agent,
#     )
#     generate_outline_task = Task(
#         description=dedent("""Create a book outline with chapters in sequential order based on the research findings.
# Ensure that each chapter has a title and a brief description that highlights the topics and subtopics to be covered.
# It's important to note that each chapter is only going to be 3,000 words or less.
# Also, make sure that you do not duplicate any chapters or topics in the outline.

# Here is some additional information about the author's desired goal for the book:\n\n {goal}"""),
#         expected_output="An outline of chapters, with titles and descriptions of what each chapter will contain. Maximum of 3 chapters.",
#         output_pydantic=BookOutline,
#         agent=outliner_agent,
#     )
#     crew = Crew(
#         agents=[researcher_agent, outliner_agent],
#         tasks=[research_topic_task, generate_outline_task],
#         process=Process.sequential,
#         verbose=True,
#     )
#     output = await crew.kickoff_async(inputs=req.model_dump())
#     return output





# async def gen_book(req: GenBookState = None):
#     """crewai 生成书 例子修改"""
#     logger.info("Kickoff the Book Outline Crew")
#     state = req or GenBookState()
#     outlines = await article_gen_outline(
#         req=WriteOutlineRequest(
#             topic=state.topic,
#             goal=state.goal,
#         )
#     )
#     chapters = outlines["chapters"]
#     state.book_outline = chapters
#     tasks = []

#     async def write_single_chapter(chapter_outline):
#         output = await write_book_chapter_crew(
#             req=WriteSingleChapterRequest(
#                 goal=state.goal,
#                 topic=state.topic,
#                 chapter_title=chapter_outline.title,
#                 chapter_description=chapter_outline.description,
#                 # BookOutline=[
#                 #     chapter_outline.model_dump_json()
#                 #     for chapter_outline in state.book_outline
#                 # ],
#                 book_outlines=outlines,
#             )
#         )
#         title = output["title"]
#         content = output["content"]
#         chapter = Chapter(title=title, content=content)
#         return chapter

#     for chapter_outline in state.book_outline:
#         logger.info(f"Writing Chapter: {chapter_outline.title}")
#         logger.info(f"Description: {chapter_outline.description}")
#         # Schedule each chapter writing task
#         task = asyncio.create_task(write_single_chapter(chapter_outline))
#         tasks.append(task)

#     # Await all chapter writing tasks concurrently
#     chapters = await asyncio.gather(*tasks)
#     logger.info("Newly generated chapters:", chapters)
#     state.book.extend(chapters)

#     logger.info("Book Chapters %s", state.book)

#     logger.info("Joining and Saving Book Chapters")
#     # Combine all chapters into a single markdown string
#     book_content = ""

#     for chapter in state.book:
#         # Add the chapter title as an H1 heading
#         book_content += f"# {chapter.title}\n\n"
#         # Add the chapter content
#         book_content += f"{chapter.content}\n\n"

#     # The title of the book from self.state.title
#     book_title = state.title

#     # Create the filename by replacing spaces with underscores and adding .md extension
#     filename = f"./{book_title.replace(' ', '_')}.md"

#     # Save the combined content into the file
#     with open(filename, "w", encoding="utf-8") as file:
#         file.write(book_content)

#     logger.info("Book saved as %s", filename)
#     return book_content


# class WriteSingleChapterRequest(BaseModel):
#     """参数: 生成文章一个章节"""

#     goal: str
#     topic: str
#     chapter_title: str
#     chapter_description: str
#     book_outlines: list[BookOutline]


# @router.get("/write_book_chapter_crew")
# async def write_book_chapter_crew(*, req: WriteSingleChapterRequest):
#     """生成文章一个章节"""
#     llm = await mtmai_context.get_crawai_llm()

#     researcher_agent = Agent(
#         role="Research Agent",
#         goal=dedent("""Gather comprehensive information about {topic} and {chapter_title} that will be used to enhance the content of the chapter.
# Here is some additional information about the author's desired goal for the book and the chapter:\n\n {goal}
# Here is the outline description for the chapter:\n\n {chapter_description}"""),
#         backstory=dedent("""You are an experienced researcher skilled in finding the most relevant and up-to-date information on any given topic.
# Your job is to provide insightful data that supports and enriches the writing process for the chapter."""),
#         tools=[],
#         llm=llm,
#     )

#     writer_agent = Agent(
#         role="Chapter Writer",
#         goal=dedent("""Write a well-structured chapter for the book based on the provided chapter title, goal, and outline.
# The chapter should be written in markdown format and contain around 3,000 words."""),
#         backstory=dedent("""You are an exceptional writer, known for producing engaging, well-researched, and informative content.
# You excel at transforming complex ideas into readable and well-organized chapters."""),
#         llm=llm,
#     )

#     research_chapter_task = Task(
#         description=dedent("""Research the provided chapter topic, title, and outline to gather additional content that will be helpful in writing the chapter.
# Ensure you focus on reliable, high-quality sources of information.

# Here is some additional information about the author's desired goal for the book and the chapter:\n\n {goal}
# Here is the outline description for the chapter:\n\n {chapter_description}

# When researching, consider the following key points:
# - you need to gather enough information to write a 3,000-word chapter
# - The chapter you are researching needs to fit in well with the rest of the chapters in the book.

# Here is the outline of the entire book:\n\n
# {book_outlines}"""),
#         expected_output="A set of additional insights and information that can be used in writing the chapter.",
#         agent=researcher_agent,
#     )

#     write_chapter_task = Task(
#         description=dedent("""Write a well-structured chapter based on the chapter title, goal, and outline description.
# Each chapter should be written in markdown and should contain around 3,000 words.

# Here is the topic for the book: {topic}
# Here is the title of the chapter: {chapter_title}
# Here is the outline description for the chapter:\n\n {chapter_description}

# Important notes:
# - The chapter you are writing needs to fit in well with the rest of the chapters in the book.

# Here is the outline of the entire book:\n\n
# {book_outlines}"""),
#         agent=writer_agent,
#         expected_output="A markdown-formatted chapter of around 3,000 words that covers the provided chapter title and outline description.",
#         output_pydantic=Chapter,
#     )
#     crew = Crew(
#         agents=[researcher_agent, writer_agent],
#         tasks=[research_chapter_task, write_chapter_task],
#         process=Process.sequential,
#         verbose=True,
#     )
#     output = await crew.kickoff_async(inputs=req.model_dump())
#     return output
