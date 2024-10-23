from typing import Literal, TypeVar

from typing_extensions import override


class NotSupported:
    def __bool__(self) -> Literal[False]:
        return False

    @override
    def __repr__(self) -> str:
        return "NOT_SUPPORTED"


NOT_SUPPORTED = NotSupported()

ParamT = TypeVar("ParamT")
NotSupportedOr = ParamT | NotSupported

SupportedParams = Literal[
    "temperature",
    "max_tokens",
    "top_k",
    "top_p",
    "stop",
    "seed",
    "frequency_penalty",
    "presence_penalty",
    "response_format",
    "tools",
    "tool_choice",
]
