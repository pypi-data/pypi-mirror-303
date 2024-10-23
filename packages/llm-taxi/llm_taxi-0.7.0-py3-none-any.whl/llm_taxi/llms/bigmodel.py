from typing import ClassVar

from llm_taxi.clients.bigmodel import BigModel as BigModelClient
from llm_taxi.llms.openai import OpenAI
from llm_taxi.types import NOT_SUPPORTED, NotSupportedOr, SupportedParams


class BigModel(BigModelClient, OpenAI):
    param_mapping: ClassVar[dict[SupportedParams, NotSupportedOr[str]]] = {
        "temperature": "temperature",
        "max_tokens": "max_tokens",
        "top_k": NOT_SUPPORTED,
        "top_p": "top_p",
        "stop": "stop",
        "seed": NOT_SUPPORTED,
        "frequency_penalty": NOT_SUPPORTED,
        "presence_penalty": NOT_SUPPORTED,
        "response_format": NOT_SUPPORTED,
        "tools": "tools",
        "tool_choice": "tool_choice",
    }
