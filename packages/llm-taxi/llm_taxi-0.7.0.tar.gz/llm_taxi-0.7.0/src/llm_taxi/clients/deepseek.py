from typing import ClassVar

from llm_taxi.clients.openai import OpenAI


class DeepSeek(OpenAI):
    env_vars: ClassVar[dict[str, str]] = {
        "api_key": "DEEPSEEK_API_KEY",
        "base_url": "DEEPSEEK_BASE_URL",
    }
