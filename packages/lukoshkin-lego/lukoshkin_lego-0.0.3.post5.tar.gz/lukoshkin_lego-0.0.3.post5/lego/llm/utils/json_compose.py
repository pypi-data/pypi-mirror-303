"""
An example of how tool calling can be used with a router:

```python
    router(
        prompt,  # type: list[dict[str, str]]
        tools=[model_to_tool(SomePydanticModel)],
        tool_choice=[convert_to_tool_choice(SomePydanticModel)],
    )
```
"""

from typing import Type, TypedDict

from pydantic import BaseModel
from pydantic_core import from_json

from lego.lego_types import JSONDict


class ResponseFormat(TypedDict):
    """Response format parameter for structured output OpenAI API calls."""

    type: str
    json_schema: dict[str, str]


def response_format(pymodel: BaseModel) -> ResponseFormat:
    return {
        "type": "json_schema",
        "json_schema": {
            "name": pymodel.__class__.__name__,
            "schema": pymodel.model_json_schema(),
        },
    }


def read_model(
    model: Type[BaseModel], model_json: str, allow_partial: bool = False
) -> BaseModel:
    """Create a pydantic model from a JSON string."""
    return model.model_validate(
        from_json(model_json, allow_partial=allow_partial)
    )


def model_to_tool(model: BaseModel) -> JSONDict:
    """Convert a Pydantic model to a tool."""
    json_schema = model.model_json_schema()
    desc = json_schema.pop("description", None)
    if desc is None:
        raise ValueError("Please add a docstring for the provided model.")

    return {
        "type": "function",
        "function": {
            "name": model.__class__.__name__,
            "description": desc,
            "parameters": json_schema,
        },
    }


def convert_to_tool_choice(tool: JSONDict | BaseModel) -> JSONDict:
    """Convert a tool or Pydantic model to a tool choice."""
    if isinstance(tool, BaseModel):
        return {
            "type": "function",
            "function": {"name": tool.__class__.__name__},
        }
    return {
        "type": "function",
        "function": {"name": tool["function"]["name"]},
    }
