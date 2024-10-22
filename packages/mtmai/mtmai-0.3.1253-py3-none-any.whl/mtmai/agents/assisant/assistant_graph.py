from langgraph.graph import StateGraph
from langgraph.graph.message import AnyMessage
from langgraph.prebuilt import tools_condition
from pydantic import BaseModel, Field

from mtmai.agents.assisant.assisant_state import AssistantState
from mtmai.agents.assisant.nodes.assisant_node import (
    PrimaryAssistantNode,
    primary_assistant_tools,
    route_assistant,
)
from mtmai.agents.assisant.nodes.entry_node import EntryNode
from mtmai.agents.ctx import mtmai_context
from mtmai.agents.graphutils import (
    create_tool_node_with_fallback,
    pop_dialog_state,
)
from mtmai.core.coreutils import is_in_dev
from mtmai.core.logging import get_logger
from mtmai.mtlibs import aisdk

logger = get_logger()


class ToFlightBookingAssistant(BaseModel):
    """Transfers work to a specialized assistant to handle flight updates and cancellations."""

    request: str = Field(
        description="Any necessary followup questions the update flight assistant should clarify before proceeding."
    )


class ToDevelopAssistant(BaseModel):
    """Transfers work to a specialized assistant to handle development tasks."""

    request: str = Field(
        description="Any necessary followup questions or specific development tasks the developer assistant should address."
    )


class ToBookCarRental(BaseModel):
    """Transfers work to a specialized assistant to handle car rental bookings."""

    location: str = Field(
        description="The location where the user wants to rent a car."
    )
    start_date: str = Field(description="The start date of the car rental.")
    end_date: str = Field(description="The end date of the car rental.")
    request: str = Field(
        description="Any additional information or requests from the user regarding the car rental."
    )

    class Config:
        json_schema_extra = {
            "example": {
                "location": "Basel",
                "start_date": "2023-07-01",
                "end_date": "2023-07-05",
                "request": "I need a compact car with automatic transmission.",
            }
        }


class ToHotelBookingAssistant(BaseModel):
    """Transfer work to a specialized assistant to handle hotel bookings."""

    location: str = Field(
        description="The location where the user wants to book a hotel."
    )
    checkin_date: str = Field(description="The check-in date for the hotel.")
    checkout_date: str = Field(description="The check-out date for the hotel.")
    request: str = Field(
        description="Any additional information or requests from the user regarding the hotel booking."
    )

    class Config:
        json_schema_extra = {
            "example": {
                "location": "Zurich",
                "checkin_date": "2023-08-15",
                "checkout_date": "2023-08-20",
                "request": "I prefer a hotel near the city center with a room that has a view.",
            }
        }


class ToBookExcursion(BaseModel):
    """Transfers work to a specialized assistant to handle trip recommendation and other excursion bookings."""

    location: str = Field(
        description="The location where the user wants to book a recommended trip."
    )
    request: str = Field(
        description="Any additional information or requests from the user regarding the trip recommendation."
    )

    class Config:
        json_schema_extra = {
            "example": {
                "location": "Lucerne",
                "request": "The user is interested in outdoor activities and scenic views.",
            }
        }


class AssistantGraph:
    def __init__(self):
        pass

    # async def get_prompt(self, state: AssistantState):
    #     primary_assistant_prompt = ChatPromptTemplate.from_messages(
    #         [
    #             (
    #                 "system",
    #                 "You are a helpful customer support assistant for Website Helper, assisting users in using this system and answering user questions. "
    #                 "delegate the task to the appropriate specialized assistant by invoking the corresponding tool. You are not able to make these types of changes yourself."
    #                 " Only the specialized assistants are given permission to do this for the user."
    #                 "The user is not aware of the different specialized assistants, so do not mention them; just quietly delegate through function calls. "
    #                 "Provide detailed information to the customer, and always double-check the database before concluding that information is unavailable. "
    #                 " When searching, be persistent. Expand your query bounds if the first search returns no results. "
    #                 " If a search comes up empty, expand your search before giving up."
    #                 "\n 必须使用中文回复用户"
    #                 "\nCurrent time: {time}."
    #                 "{additional_instructions}",
    #             ),
    #             ("placeholder", "{messages}"),
    #         ]
    #     ).partial(time=datetime.now())
    #     return primary_assistant_prompt

    async def build_graph(self):
        wf = StateGraph(AssistantState)

        wf.add_node("entry", EntryNode())
        wf.add_edge("entry", "assistant")
        wf.set_entry_point("entry")

        wf.add_node("assistant", PrimaryAssistantNode())

        wf.add_conditional_edges(
            "assistant",
            tools_condition,
        )

        wf.add_node(
            "tools",
            create_tool_node_with_fallback(primary_assistant_tools),
        )
        wf.add_conditional_edges(
            "tools",
            route_assistant,
            {
                "assistant": "assistant",
                # "error": END,
            },
        )
        wf.add_node("leave_skill", pop_dialog_state)
        wf.add_edge("leave_skill", "assistant")

        return wf

    async def compile_graph(self):
        graph = (await self.build_graph()).compile(
            checkpointer=await mtmai_context.get_graph_checkpointer(),
            # interrupt_after=["human_chat"],
            interrupt_before=[
                # "human_chat",
                # "update_flight_sensitive_tools",
                # "develop_sensitive_tools",
                # "book_car_rental_sensitive_tools",
                # "book_hotel_sensitive_tools",
                # "book_excursion_sensitive_tools",
            ],
            debug=True,
        )

        if is_in_dev():
            image_data = graph.get_graph(xray=1).draw_mermaid_png()
            save_to = "./.vol/assistant_graph.png"
            with open(save_to, "wb") as f:
                f.write(image_data)
        return graph

    async def run_graph(
        self,
        messages: list[AnyMessage] = [],
        thread_id: str | None = None,
        user_id: str | None = None,
        params: dict | None = None,
    ):
        graph = await self.compile_graph()
        inputs = {
            "messages": messages,
            "userId": user_id,
            "params": params,
        }
        await mtmai_context.init_mq()

        async for event in graph.astream_events(
            inputs,
            version="v2",
            config={
                "configurable": {
                    "thread_id": mtmai_context.thread_id,
                }
            },
            subgraphs=True,
        ):
            kind = event["event"]
            node_name = event["name"]
            data = event["data"]

            if kind == "on_chat_model_stream":
                # send_chat_event()
                # content = event["data"]["chunk"].content
                # if content:
                yield aisdk.data(event)
                await mtmai_context.mq.send_event(event)
            else:
                yield aisdk.data(event)
