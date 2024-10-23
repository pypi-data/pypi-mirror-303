from typing import Any, ClassVar

from groq import AsyncGroq
from typing_extensions import override

from llm_taxi.clients.base import Client


class Groq(Client[AsyncGroq]):
    env_vars: ClassVar[dict[str, str]] = {
        "api_key": "GROQ_API_KEY",
    }

    @override
    def _init_client(self, client_options: dict[str, Any]) -> AsyncGroq:
        return AsyncGroq(**client_options)
