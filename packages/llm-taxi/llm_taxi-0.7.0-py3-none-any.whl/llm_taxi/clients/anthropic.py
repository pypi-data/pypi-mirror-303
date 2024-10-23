from typing import Any, ClassVar

from anthropic import AsyncAnthropic
from typing_extensions import override

from llm_taxi.clients.base import Client


class Anthropic(Client[AsyncAnthropic]):
    env_vars: ClassVar[dict[str, str]] = {
        "api_key": "ANTHROPIC_API_KEY",
    }

    @override
    def _init_client(self, client_options: dict[str, Any]) -> AsyncAnthropic:
        return AsyncAnthropic(**client_options)
