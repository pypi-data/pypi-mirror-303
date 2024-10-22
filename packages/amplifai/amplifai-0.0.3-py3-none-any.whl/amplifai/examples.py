"""`amplifai.examples` module."""

from typing import Generic, TypeVar

from pydantic import BaseModel

Schema = TypeVar("Schema", bound=BaseModel)


class Example(BaseModel, Generic[Schema]):
    """
    A representation of an example consisting of text input and expected tool calls.
    For extraction, the tool calls are represented as instances of pydantic model.
    """

    input: str  # This is the example text
    outputs: list[Schema]  # Instances of pydantic model that should be extracted


class Examples(BaseModel, Generic[Schema]):
    """
    A collection of examples.
    """

    examples: list[Example[Schema]]
