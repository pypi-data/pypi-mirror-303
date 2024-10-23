from typing import ClassVar

from llm_taxi.clients.openrouter import OpenRouter as OpenRouterClient
from llm_taxi.llms.openai import OpenAI
from llm_taxi.types import NotSupportedOr, SupportedParams


class OpenRouter(OpenRouterClient, OpenAI):
    param_mapping: ClassVar[dict[SupportedParams, NotSupportedOr[str]]] = {}
