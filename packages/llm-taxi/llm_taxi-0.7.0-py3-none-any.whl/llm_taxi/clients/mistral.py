from typing import Any, ClassVar

from mistralai import Mistral as MistralClient
from typing_extensions import override

from llm_taxi.clients.base import Client


class Mistral(Client[MistralClient]):
    env_vars: ClassVar[dict[str, str]] = {
        "api_key": "MISTRAL_API_KEY",
    }

    @override
    def _init_client(self, client_options: dict[str, Any]) -> MistralClient:
        client_options.pop("base_url", None)

        return MistralClient(**client_options)
