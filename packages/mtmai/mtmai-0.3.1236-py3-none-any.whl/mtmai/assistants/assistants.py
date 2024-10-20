

from mtmai.assistants.assisant_webcontainer import WebContainerAssistant
from mtmai.assistants.assistant_article_gen import ArticleGenAssistant
from mtmai.assistants.assistant_site import SiteAssistant


async def get_assistant_agent(chat_profile: str):
    if(chat_profile=="articleGen"):
        return ArticleGenAssistant()
    if(chat_profile=="web_container_developer"):
        return WebContainerAssistant()
    if(chat_profile=="site"):
        return SiteAssistant()
    else:
        raise ValueError(f"Unsupported chat profile: {chat_profile}")
