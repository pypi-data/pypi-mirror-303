from typing import ClassVar

from llm_taxi.clients.perplexity import Perplexity as PerplexityClient
from llm_taxi.llms.openai import OpenAI
from llm_taxi.types import NotSupportedOr, SupportedParams


class Perplexity(PerplexityClient, OpenAI):
    param_mapping: ClassVar[dict[SupportedParams, NotSupportedOr[str]]] = {}
