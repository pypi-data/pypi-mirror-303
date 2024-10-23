from collections.abc import AsyncGenerator, Iterable
from typing import Any, ClassVar, Literal, cast

from anthropic import AsyncStream
from anthropic._types import NOT_GIVEN, NotGiven
from anthropic.types import Message as ChatMessage
from anthropic.types import MessageParam, RawMessageStreamEvent, TextBlock, TextDelta
from typing_extensions import override

from llm_taxi.clients.anthropic import Anthropic as AnthropicClient
from llm_taxi.conversation import Message, Role
from llm_taxi.llms.base import LLM
from llm_taxi.types import NOT_SUPPORTED, NotSupportedOr, SupportedParams


class Anthropic(AnthropicClient, LLM[Iterable[MessageParam]]):
    param_mapping: ClassVar[dict[SupportedParams, NotSupportedOr[str]]] = {
        "temperature": "temperature",
        "max_tokens": "max_tokens",
        "top_k": "top_k",
        "top_p": "top_p",
        "stop": "stop_sequences",
        "seed": NOT_SUPPORTED,
        "frequency_penalty": NOT_SUPPORTED,
        "presence_penalty": NOT_SUPPORTED,
        "response_format": NOT_SUPPORTED,
        "tools": "tools",
        "tool_choice": "tool_choice",
    }

    @override
    def _convert_messages(self, messages: list[Message]) -> Iterable[MessageParam]:
        return [
            MessageParam(
                role=cast(Literal["user", "assistant"], message.role.value),
                content=message.content,
            )
            for message in messages
            if message.role in {Role.User, Role.Assistant}
        ]

    def _get_system_message_content(
        self,
        messages: list[Message],
    ) -> str | NotGiven:
        if message := next(
            (x for x in reversed(messages) if x.role == Role.System),
            NOT_GIVEN,
        ):
            return message.content

        return NOT_GIVEN

    async def _streaming_response(
        self, response: AsyncStream[RawMessageStreamEvent]
    ) -> AsyncGenerator[str]:
        async for chunk in response:
            if chunk.type == "content_block_delta":
                yield cast(TextDelta, chunk.delta).text

    @override
    async def streaming_response(
        self,
        messages: list[Message],
        llm_options: dict[str, Any] | None = None,
    ) -> AsyncGenerator[str]:
        system_message = self._get_system_message_content(messages)

        response = await self.client.messages.create(
            system=system_message,
            messages=self._convert_messages(messages),
            stream=True,
            **self._get_call_options(llm_options),
        )

        return self._streaming_response(response)

    @override
    async def response(
        self,
        messages: list[Message],
        llm_options: dict[str, Any] | None = None,
    ) -> str:
        system_message = self._get_system_message_content(messages)

        response = cast(
            ChatMessage,
            await self.client.messages.create(
                system=system_message,
                messages=self._convert_messages(messages),
                **self._get_call_options(llm_options),
            ),
        )

        return cast(TextBlock, response.content[0]).text
