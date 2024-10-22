"""`amplifier.amplifier` module.

Defines the `Amplifier` class, which is the main class of the package.
"""

import uuid
from typing import Any, Generic, Self, TypeVar

from langchain_core.language_models.chat_models import BaseChatModel
from langchain_core.messages import AIMessage, BaseMessage, HumanMessage, ToolMessage
from langchain_core.prompts.chat import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables import Runnable
from pydantic import BaseModel, ConfigDict

from amplifai.examples import Example
from amplifai.prompt import DEFAULT_HUMAN_PROMPT, DEFAULT_SYSTEM_PROMPT

PydanticModel = TypeVar("PydanticModel", bound=BaseModel)
ChatModel = TypeVar("ChatModel", bound=BaseChatModel)


class Amplifier(BaseModel, Generic[ChatModel, PydanticModel]):
    """Structurize a text into a dictionary.

    Arguments
    -----------------------------------------------
    llm: ChatModel
        The language model to use.
    system_prompt::str|None
        The instructions to the system.
    human_prompt::str|None
        The human provided context.

    """


    llm: ChatModel
    system_prompt: str | None = DEFAULT_SYSTEM_PROMPT
    #instructions: str | None = None # cf https://github.com/langchain-ai/langchain-extract/blob/main/backend/server/extraction_runnable.py
    human_prompt: str | None = DEFAULT_HUMAN_PROMPT
    examples: list[BaseMessage] = []  # Converted example

    @property
    def with_examples(self) -> bool:
        """Check if the amplifier has examples."""

        return len(self.examples) > 0

    # ------------------------------------------------------------
    # Pydantic Config
    # ------------------------------------------------------------
    model_config = ConfigDict(validate_default=True)

    
    # ------------------------------------------------------------
    # Sync Interface
    # ------------------------------------------------------------
    def denoise(self, include_raw: bool = False, **kwargs: Any) -> PydanticModel:
        """Creates a pydantic object from textual unstructured data.

        Arguments:
        -----------------------------------------------
        **kwargs: Any,
            The arguments to fill in the prompt to complete it.
            For example, if the base prompt is "What is the capital of {country}?",
            then the kwargs will be {"country": "France"}

        """

        if self.with_examples:
            kwargs["examples"] = self.examples

        chain = self._create_chain(include_raw=include_raw)
        output = chain.invoke(kwargs)

        return output

    # ------------------------------------------------------------
    # Async Interface
    # ------------------------------------------------------------
    async def async_denoise(self, include_raw: bool = False, **kwargs: Any) -> PydanticModel:
        """Creates a pydantic object from textual unstructured data.
        Asynchronous version of the `amplifier.extract` method.

        See Also:
        -----------------------------------------------
        - `amplifier.extract` for more details

        """

        if self.with_examples:
            kwargs["examples"] = self.examples

        chain = self._create_chain(include_raw)
        output = await chain.ainvoke(kwargs)

        return output

    # ------------------------------------------------------------
    # Common Internal Methods
    # ------------------------------------------------------------
    def add_examples(
        self,
        examples: list[Example[PydanticModel]],
    ) -> Self:
        """
        Converts a list of examples to a list of base messages.

        Args:
            examples (List[Any]): The list of examples to use.

        Returns:
            List[BaseMessage]: The examples as tool messages.
        """

        messages = []
        for example in examples:
            messages.extend(self._build_tool_messages(example=example))

        self.examples = messages

        return self
    

    def _get_chat_model(self) -> type[BaseChatModel]:
        """Returns the chat model type parameter of the amplifier instance."""

        return self.__class__.__pydantic_generic_metadata__["args"][0]


    def _get_pydantic_model(self) -> type[PydanticModel]:
        """Returns the pydantic model type parameter of the amplifier instance."""

        # NOTE : Useful link to understand the below <VM, 28/02/2024>
        # https://discuss.python.org/t/runtime-access-to-type-parameters/37517

        return self.__class__.__pydantic_generic_metadata__["args"][1]

    def _create_chain(self, include_raw: bool = False) -> Runnable:
        """Creates the extraction chain.

        Arguments:
        -----------------------------------------------
        include_raw: bool,
            Whether to include the raw output of the language model in the final output.

        """

        llm = self.llm.with_structured_output(
            self._get_pydantic_model(),
            method="function_calling",
            include_raw=include_raw,
        )
        prompt = self._build_prompt_template()
        chain = prompt | llm

        return chain

    def _build_prompt_template(self) -> ChatPromptTemplate:
        """Builds the prompt template from the system and human prompts or from the base_prompt."""

        if self.with_examples:
            prompt_template = ChatPromptTemplate.from_messages(
                [
                    ("system", self.system_prompt),
                    MessagesPlaceholder("examples"),
                    ("human", self.human_prompt),
                ]
            )
        else:
            prompt_template = ChatPromptTemplate.from_messages(
                [
                    ("system", self.system_prompt),
                    ("human", self.human_prompt),
                ]
            )

        return prompt_template

    def _build_tool_messages(
        self,
        example: Example[PydanticModel],
    ) -> list[BaseMessage]:
        """
        Converts an example into a list of messages that can be fed ito an LLM.

        Arguments:
        -----------------------------------------------
        example : Example[PydanticModel]:
            A representation of an example consisting of text input and expected tool calls.
            For extraction, the tool calls are represented as instances of pydantic model.

        """

        messages: list[BaseMessage] = [HumanMessage(content=example.input)]
        tool_calls = []

        for output in example.outputs:
            tool_calls.append(
                {
                    "id": str(uuid.uuid4()),
                    "type": "function",
                    "function": {
                        "name": output.__class__.__name__,
                        "arguments": output.model_dump_json(),
                    },
                }
            )

        messages.append(AIMessage(content="", additional_kwargs={"tool_calls": tool_calls}))
        tool_messages = ["You have correctly called this tool."] * len(tool_calls)

        for tool_message, tool_output in zip(tool_messages, tool_calls):
            messages.append(ToolMessage(content=tool_message, tool_call_id=tool_output["id"]))

        return messages
