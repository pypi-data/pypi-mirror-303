from typing import ClassVar

from llm_taxi.clients.openai import OpenAI


class OpenRouter(OpenAI):
    env_vars: ClassVar[dict[str, str]] = {
        "api_key": "OPENROUTER_API_KEY",
        "base_url": "OPENROUTER_BASE_URL",
    }
