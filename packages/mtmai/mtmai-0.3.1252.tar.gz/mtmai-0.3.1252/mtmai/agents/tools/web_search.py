import logging
from textwrap import dedent

import httpx
from langchain_community.utilities.duckduckgo_search import DuckDuckGoSearchAPIWrapper
from langchain_core.tools import tool

from mtmai.core.config import settings

logger = logging.getLogger()


async def search_web_by_keywords(keywords: str, search_result_limit=3):
    searxng_url = f"{settings.SEARXNG_URL_BASE}/search"
    logger.info("调用 search ( %s ), %s", searxng_url, keywords)

    with httpx.Client() as client:
        params = {"q": keywords, "format": "json"}
        r = client.get(searxng_url, params=params)
        r.raise_for_status()

        search_results = r.json()

        result_list2 = search_results.get("results", [])[:search_result_limit]

        result_list3 = [
            {
                "title": x.get("title", ""),
                "url": x.get("url", ""),
                "content": x.get("content", ""),
            }
            for x in result_list2
        ]

        content_lines = ["搜索结果:"]
        for x in result_list3:
            content_lines.append(
                dedent(f"""title: {x.get("title")}
                      content: {x.get("content")}
                      """)
            )

        return (
            "\n".join(content_lines),
            {
                "artifaceType": "ArtifactSearchResults",
                "props": {
                    "title": f"{keywords}的搜索结果",
                    "results": result_list3,
                    "suggestions": search_results.get("suggestions", []),
                    # "infoboxes": search_results.get("infoboxes", []),
                },
            },
        )


@tool
def search_engine(query: str, results_limit: int = 3, search_engine: str = "ddg"):
    """Search engine to the internet."""

    logger.info(f"调用搜索: {query}")
    search_engine = DuckDuckGoSearchAPIWrapper()
    results = search_engine._ddgs_text(query)
    return [{"content": r["body"], "url": r["href"]} for r in results]
