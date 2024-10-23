from collections.abc import AsyncGenerator
from typing import Any, ClassVar

from mistralai import CompletionEvent
from mistralai.models import MessagesTypedDict
from typing_extensions import override

from llm_taxi.clients.mistral import Mistral as MistralClient
from llm_taxi.conversation import Message
from llm_taxi.llms.base import LLM
from llm_taxi.types import NOT_SUPPORTED, NotSupportedOr, SupportedParams


class Mistral(MistralClient, LLM[list[MessagesTypedDict]]):
    param_mapping: ClassVar[dict[SupportedParams, NotSupportedOr[str]]] = {
        "temperature": "temperature",
        "max_tokens": "max_tokens",
        "top_k": NOT_SUPPORTED,
        "top_p": "top_p",
        "stop": NOT_SUPPORTED,
        "seed": "random_seed",
        "frequency_penalty": NOT_SUPPORTED,
        "presence_penalty": NOT_SUPPORTED,
        "response_format": "response_format",
        "tools": "tools",
        "tool_choice": "tool_choice",
    }

    @override
    def _convert_messages(self, messages: list[Message]) -> list[MessagesTypedDict]:
        return [
            {
                "role": x.role.value,
                "content": x.content,
            }
            for x in messages
        ]  # pyright: ignore[reportReturnType]

    async def _streaming_response(
        self,
        response: AsyncGenerator[CompletionEvent] | None,
    ) -> AsyncGenerator[str]:
        if response is not None:
            async for chunk in response:
                if content := chunk.data.choices[0].delta.content:
                    yield content

    @override
    async def streaming_response(
        self,
        messages: list[Message],
        llm_options: dict[str, Any] | None = None,
    ) -> AsyncGenerator[str]:
        response = await self.client.chat.stream_async(
            messages=self._convert_messages(messages),
            **self._get_call_options(llm_options),
        )

        return self._streaming_response(response)

    @override
    async def response(
        self,
        messages: list[Message],
        llm_options: dict[str, Any] | None = None,
    ) -> str:
        response = await self.client.chat.complete_async(
            messages=self._convert_messages(messages),
            **self._get_call_options(llm_options),
        )
        if response is None:
            return ""

        if (choices := response.choices) and (content := choices[0].message.content):
            return content

        return ""
