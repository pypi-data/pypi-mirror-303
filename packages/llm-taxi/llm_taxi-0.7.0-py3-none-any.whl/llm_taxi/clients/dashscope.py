from typing import ClassVar

from llm_taxi.clients.openai import OpenAI


class DashScope(OpenAI):
    env_vars: ClassVar[dict[str, str]] = {
        "api_key": "DASHSCOPE_API_KEY",
        "base_url": "DASHSCOPE_BASE_URL",
    }
