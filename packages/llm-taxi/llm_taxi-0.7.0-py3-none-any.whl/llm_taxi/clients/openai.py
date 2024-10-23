from typing import Any, ClassVar

from openai import AsyncClient
from typing_extensions import override

from llm_taxi.clients.base import Client


class OpenAI(Client[AsyncClient]):
    env_vars: ClassVar[dict[str, str]] = {
        "api_key": "OPENAI_API_KEY",
    }

    @override
    def _init_client(self, client_options: dict[str, Any]) -> AsyncClient:
        return AsyncClient(**client_options)
