from mtmai.agents.sitegen_graph.assistant_site import SiteAssistantNode


async def get_assistant_agent(chat_profile: str):
    if chat_profile == "site":
        return SiteAssistantNode()
    else:
        raise ValueError(f"Unsupported chat profile: {chat_profile}")
