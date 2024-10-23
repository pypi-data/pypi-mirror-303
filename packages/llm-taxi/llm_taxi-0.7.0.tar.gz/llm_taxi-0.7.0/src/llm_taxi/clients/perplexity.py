from typing import ClassVar

from llm_taxi.clients.openai import OpenAI


class Perplexity(OpenAI):
    env_vars: ClassVar[dict[str, str]] = {
        "api_key": "PERPLEXITY_API_KEY",
        "base_url": "PERPLEXITY_BASE_URL",
    }
