import itertools
from collections.abc import AsyncGenerator
from typing import Any, ClassVar

from google.generativeai.types import (  # pyright: ignore[reportMissingTypeStubs]
    AsyncGenerateContentResponse,
)
from typing_extensions import override

from llm_taxi.clients.google import Google as GoogleClient
from llm_taxi.conversation import Message, Role
from llm_taxi.llms.base import LLM
from llm_taxi.types import NOT_SUPPORTED, NotSupportedOr, SupportedParams


class Google(GoogleClient, LLM[list[dict[str, Any]]]):
    param_mapping: ClassVar[dict[SupportedParams, NotSupportedOr[str]]] = {
        "temperature": "temperature",
        "max_tokens": "max_output_tokens",
        "top_k": "top_k",
        "top_p": "top_p",
        "stop": "stop_sequences",
        "seed": NOT_SUPPORTED,
        "frequency_penalty": NOT_SUPPORTED,
        "presence_penalty": NOT_SUPPORTED,
        "response_format": NOT_SUPPORTED,
        "tools": NOT_SUPPORTED,
        "tool_choice": NOT_SUPPORTED,
    }

    @override
    def _convert_messages(self, messages: list[Message]) -> list[dict[str, Any]]:
        role_mappping = {
            Role.System: "user",
            Role.User: "user",
            Role.Assistant: "model",
        }
        groups = itertools.groupby(
            messages,
            key=lambda x: role_mappping[Role(x.role)],
        )

        return [
            {
                "role": role,
                "parts": [x.content for x in parts],
            }
            for role, parts in groups
        ]

    async def _streaming_response(
        self, response: AsyncGenerateContentResponse
    ) -> AsyncGenerator[str]:
        async for chunk in response:
            yield chunk.text

    @override
    async def streaming_response(
        self,
        messages: list[Message],
        llm_options: dict[str, Any] | None = None,
    ) -> AsyncGenerator[str]:
        from google import generativeai as genai

        response = await self.client.generate_content_async(  # pyright: ignore[reportUnknownMemberType]
            self._convert_messages(messages),
            stream=True,
            generation_config=genai.types.GenerationConfig(  # pyright: ignore[reportPrivateImportUsage]
                **self._get_call_options(llm_options),
            ),
        )

        return self._streaming_response(response)

    @override
    async def response(
        self,
        messages: list[Message],
        llm_options: dict[str, Any] | None = None,
    ) -> str:
        from google import generativeai as genai

        response = await self.client.generate_content_async(  # pyright: ignore[reportUnknownMemberType]
            self._convert_messages(messages),
            generation_config=genai.types.GenerationConfig(  # pyright: ignore[reportPrivateImportUsage]
                **self._get_call_options(llm_options),
            ),
        )

        return response.text
