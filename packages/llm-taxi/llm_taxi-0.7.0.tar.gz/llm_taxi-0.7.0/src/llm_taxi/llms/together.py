from collections.abc import AsyncGenerator
from typing import Any, ClassVar, cast

from together.types import (  # pyright: ignore[reportMissingTypeStubs]
    ChatCompletionResponse,
)
from typing_extensions import override

from llm_taxi.clients.together import Together as TogetherClient
from llm_taxi.conversation import Message
from llm_taxi.llms.base import LLM
from llm_taxi.llms.openai import streaming_response
from llm_taxi.types import NOT_SUPPORTED, NotSupportedOr, SupportedParams


class Together(TogetherClient, LLM[list[dict[str, Any]]]):
    param_mapping: ClassVar[dict[SupportedParams, NotSupportedOr[str]]] = {
        "temperature": "temperature",
        "max_tokens": "max_tokens",
        "top_k": "top_k",
        "top_p": "top_p",
        "stop": "stop",
        "seed": NOT_SUPPORTED,
        "frequency_penalty": "frequency_penalty",
        "presence_penalty": "presence_penalty",
        "response_format": "response_format",
        "tools": "tools",
        "tool_choice": "tool_choice",
    }

    @override
    def _convert_messages(self, messages: list[Message]) -> list[dict[str, Any]]:
        return [
            {
                "role": message.role.value,
                "content": message.content,
            }
            for message in messages
        ]

    @override
    async def streaming_response(
        self,
        messages: list[Message],
        llm_options: dict[str, Any] | None = None,
    ) -> AsyncGenerator[str]:
        response = await self.client.chat.completions.create(
            messages=self._convert_messages(messages),
            stream=True,
            **self._get_call_options(llm_options),
        )

        return streaming_response(response)

    @override
    async def response(
        self,
        messages: list[Message],
        llm_options: dict[str, Any] | None = None,
    ) -> str:
        response = await self.client.chat.completions.create(
            messages=self._convert_messages(messages),
            **self._get_call_options(llm_options),
        )
        response = cast(ChatCompletionResponse, response)

        if (
            (choices := response.choices)
            and (data := choices[0])
            and (message := data.message)
            and (content := message.content)
        ):
            return content

        return ""
