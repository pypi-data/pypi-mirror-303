from typing import ClassVar

from llm_taxi.clients.deepinfra import DeepInfra as DeepInfraClient
from llm_taxi.llms.openai import OpenAI
from llm_taxi.types import NotSupportedOr, SupportedParams


class DeepInfra(DeepInfraClient, OpenAI):
    param_mapping: ClassVar[dict[SupportedParams, NotSupportedOr[str]]] = {}
