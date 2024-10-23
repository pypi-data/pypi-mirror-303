from typing import ClassVar

from llm_taxi.clients.openai import OpenAI


class BigModel(OpenAI):
    env_vars: ClassVar[dict[str, str]] = {
        "api_key": "BIGMODEL_API_KEY",
        "base_url": "BIGMODEL_BASE_URL",
    }
