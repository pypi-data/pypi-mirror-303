"""
An example of how it can be used with a router from 'simple_router' module:

```python
    router(
        prompt,  # type: list[dict[str, str]]
        tools=[model_to_tool(SomePydanticModel)],
        tool_choice=[convert_to_tool_choice(SomePydanticModel)],
    )
```
"""

from pydantic import BaseModel

from lego.lego_types import JSONDict


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
