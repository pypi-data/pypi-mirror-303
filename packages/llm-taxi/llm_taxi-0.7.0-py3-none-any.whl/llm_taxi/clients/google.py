from typing import Any, ClassVar

from google import generativeai as genai
from google.generativeai.generative_models import (  # pyright: ignore[reportMissingTypeStubs]
    GenerativeModel,
)
from typing_extensions import override

from llm_taxi.clients.base import Client


class Google(Client[GenerativeModel]):
    env_vars: ClassVar[dict[str, str]] = {
        "api_key": "GOOGLE_API_KEY",
    }

    def __init__(
        self,
        *,
        model: str,
        api_key: str,
        base_url: str | None = None,
        call_options: dict[str, Any] | None = None,
        client_options: dict[str, Any] | None = None,
    ) -> None:
        super().__init__(
            model=model,
            api_key=api_key,
            base_url=base_url,
            call_options=call_options,
            client_options=client_options,
        )
        if not client_options:
            client_options = {}

        genai.configure(api_key=api_key, **client_options)  # pyright: ignore[reportPrivateImportUsage,reportUnknownMemberType]

        self._call_options.pop("model", None)

    @override
    def _init_client(self, client_options: dict[str, Any]) -> GenerativeModel:
        client_options = {
            k: v for k, v in client_options.items() if k not in {"api_key", "base_url"}
        }

        return GenerativeModel(self.model, **client_options)
