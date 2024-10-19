from typing import List

from pydantic import BaseModel
from pydantic.dataclasses import Field, dataclass

from mtmai.chainlit.context import context
from mtmai.chainlit.input_widget import InputWidget
from mtmai.mtlibs.inputs.input_widget import InputWidgetBase


@dataclass
class ChatSettings:
    """Useful to create chat settings that the user can change."""

    inputs: List[InputWidget] = Field(default_factory=list, exclude=True)

    def __init__(
        self,
        inputs: List[InputWidget],
    ) -> None:
        self.inputs = inputs

    def settings(self):
        return dict(
            [(input_widget.id, input_widget.initial) for input_widget in self.inputs]
        )

    async def send(self):
        settings = self.settings()
        context.emitter.set_chat_settings(settings)

        inputs_content = [input_widget.to_dict() for input_widget in self.inputs]
        await context.emitter.emit("chat_settings", inputs_content)

        return settings




    # def settings(self) -> dict[str, Any]:
    #     return {input_widget.id: input_widget.initial for input_widget in self.inputs}

    # async def send(self) -> dict[str, Any]:
    #     settings = self.settings()
    #     # context.emitter.set_chat_settings(settings)

    #     # inputs_content = [input_widget.to_dict() for input_widget in self.inputs]
    #     await context.emitter.emit("chat_forms", inputs_content)

    #     return settings
