"""Types common to all lego submodules."""

from typing import Any, DefaultDict, NewType, TypeAlias, TypeVar

T = TypeVar("T")
# -- mypy contradicts with pyright here?
OneOrMany = T | list[T]  # type: ignore[misc]
MilvusParamConfig: TypeAlias = dict[str, str | dict[str, int]]

JSONDict: TypeAlias = dict[str, Any]  # type: ignore[misc]
FlatParamConfig: TypeAlias = dict[str, str | int | float | bool]

UseProfiler = NewType("UseProfiler", bool)
ProfilerSessions = NewType(
    "ProfilerSessions", DefaultDict[str, dict[str, float]]
)

Messages: TypeAlias = list[dict[str, str]]
LegoLLMRouter = NewType("LegoLLMRouter", object)
