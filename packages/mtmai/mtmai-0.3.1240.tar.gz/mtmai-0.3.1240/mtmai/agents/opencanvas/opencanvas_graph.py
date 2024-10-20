import uuid

from langchain_core.runnables import RunnableConfig
from langgraph.graph import StateGraph
from langgraph.graph.message import AnyMessage

from mtmai.agents.ctx import mtmai_context
from mtmai.agents.opencanvas.nodes.generatePath import GeneratePath
from mtmai.agents.opencanvas.opencanvas_state import OpenCanvasState
from mtmai.core.logging import get_logger
from mtmai.mtlibs import aisdk

logger = get_logger()


class OpenCanvasGraph:
    def __init__(self):
        pass

    async def build_graph(self):
        wf = StateGraph(OpenCanvasState)
        # 入口
        wf.add_node("GeneratePath", GeneratePath())
        wf.set_entry_point("GeneratePath")

        return wf

    async def compile_graph(self):
        graph = (await self.build_graph()).compile(
            checkpointer=await mtmai_context.get_graph_checkpointer(),
            # interrupt_after=["human_chat"],
            # interrupt_before=[
            #     "human_chat",
            #     # "update_flight_sensitive_tools",
            #     # "develop_sensitive_tools",
            #     # "book_car_rental_sensitive_tools",
            #     # "book_hotel_sensitive_tools",
            #     # "book_excursion_sensitive_tools",
            # ],
            debug=True,
        )

        image_data = graph.get_graph(xray=1).draw_mermaid_png()
        save_to = "./graph.png"
        with open(save_to, "wb") as f:
            f.write(image_data)
        return graph

    # async def __call__(self, state: OpenCanvasState, config: RunnableConfig):
    #     prompt_tpl = await self.get_prompt(state)
    #     tools = []

    #     dialog_state = state.dialog_state
    #     if dialog_state != "pop":
    #         ai_msg = await mtmai_context.ainvoke_model(prompt_tpl, state, tools=tools)

    #         # if ai_msg.content:
    #         #     await cl.Message("primary:" + ai_msg.content).send()
    #         return {"messages": ai_msg}
    #     else:
    #         # 下级的assistant 本身是直接回复用户，所以这里不需要再回复用户
    #         return {"messages": []}

    async def run_graph(
        self,
        # thread: RunnableConfig,
        messages: list[AnyMessage] = [],
        thread_id: str | None = None,
        # user: User | None = None,
        user_id: str | None = None,
    ):
        graph = await self.compile_graph()
        inputs = {
            "messages": messages,
        }

        if not thread_id:
            thread_id = str(uuid.uuid4())
        thread: RunnableConfig = {
            "configurable": {
                "thread_id": thread_id,
            }
        }

        async for event in graph.astream_events(
            inputs,
            version="v2",
            config=thread,
            subgraphs=True,
        ):
            kind = event["event"]
            node_name = event["name"]
            data = event["data"]

            yield aisdk.data(event)
            # if not is_internal_node(node_name):
            #     if not is_skip_kind(kind):
            #         logger.info("[event] %s@%s", kind, node_name)

            # if kind == "on_chat_model_stream":
            #     content = event["data"]["chunk"].content
            #     if content:
            #         yield aisdk.text(content)
