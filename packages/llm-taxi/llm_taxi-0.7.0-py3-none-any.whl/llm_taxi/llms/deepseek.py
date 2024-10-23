from typing import ClassVar

from llm_taxi.clients.deepseek import DeepSeek as DeepSeekClient
from llm_taxi.llms.openai import OpenAI
from llm_taxi.types import NOT_SUPPORTED, NotSupportedOr, SupportedParams


class DeepSeek(DeepSeekClient, OpenAI):
    param_mapping: ClassVar[dict[SupportedParams, NotSupportedOr[str]]] = {
        "temperature": "temperature",
        "max_tokens": "max_tokens",
        "top_k": NOT_SUPPORTED,
        "top_p": "top_p",
        "stop": "stop",
        "seed": NOT_SUPPORTED,
        "frequency_penalty": "frequency_penalty",
        "presence_penalty": "presence_penalty",
        "response_format": NOT_SUPPORTED,
        "tools": NOT_SUPPORTED,
        "tool_choice": NOT_SUPPORTED,
    }
