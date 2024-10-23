from typing import Any, ClassVar

from together import AsyncTogether  # pyright: ignore[reportMissingTypeStubs]
from typing_extensions import override

from llm_taxi.clients.base import Client


class Together(Client[AsyncTogether]):
    env_vars: ClassVar[dict[str, str]] = {
        "api_key": "TOGETHER_API_KEY",
    }

    @override
    def _init_client(self, client_options: dict[str, Any]) -> AsyncTogether:
        return AsyncTogether(**client_options)
