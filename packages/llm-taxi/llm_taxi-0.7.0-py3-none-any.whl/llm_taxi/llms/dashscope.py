from typing import ClassVar

from llm_taxi.clients.dashscope import DashScope as DashScopeClient
from llm_taxi.llms.openai import OpenAI
from llm_taxi.types import NOT_SUPPORTED, NotSupportedOr, SupportedParams


class DashScope(DashScopeClient, OpenAI):
    param_mapping: ClassVar[dict[SupportedParams, NotSupportedOr[str]]] = {
        "temperature": "temperature",
        "max_tokens": "max_tokens",
        "top_k": NOT_SUPPORTED,
        "top_p": "top_p",
        "stop": "stop",
        "seed": "seed",
        "frequency_penalty": NOT_SUPPORTED,
        "presence_penalty": "presence_penalty",
        "response_format": NOT_SUPPORTED,
        "tools": "tools",
        "tool_choice": "tool_choice",
    }
