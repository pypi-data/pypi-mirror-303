import asyncio
from typing import Union

from literalai import ChatGeneration, CompletionGeneration
from literalai.helper import timestamp_utc

from mtmai.chainlit.context import get_context
from mtmai.chainlit.step import Step
from mtmai.chainlit.utils import check_module_version


def instrument_mistralai():
    from literalai.instrumentation.mistralai import instrument_mistralai

    def on_new_generation(
        generation: Union["ChatGeneration", "CompletionGeneration"], timing
    ):
        context = get_context()

        parent_id = None
        if context.current_step:
            parent_id = context.current_step.id

        step = Step(
            name=generation.model if generation.model else generation.provider,
            type="llm",
            parent_id=parent_id,
        )
        step.generation = generation
        # Convert start/end time from seconds to milliseconds
        step.start = (
            timestamp_utc(timing.get("start"))
            if timing.get("start", None) is not None
            else None
        )
        step.end = (
            timestamp_utc(timing.get("end"))
            if timing.get("end", None) is not None
            else None
        )

        if isinstance(generation, ChatGeneration):
            step.input = generation.messages
            step.output = generation.message_completion  # type: ignore
        else:
            step.input = generation.prompt
            step.output = generation.completion

        asyncio.create_task(step.send())

    instrument_mistralai(None, on_new_generation)
