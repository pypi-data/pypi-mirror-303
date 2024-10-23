from collections.abc import AsyncGenerator
from typing import Any, ClassVar, cast

from openai.types.chat import (
    ChatCompletion,
    ChatCompletionAssistantMessageParam,
    ChatCompletionMessageParam,
    ChatCompletionSystemMessageParam,
    ChatCompletionUserMessageParam,
)
from typing_extensions import override

from llm_taxi.clients.openai import OpenAI as OpenAIClient
from llm_taxi.conversation import Message, Role
from llm_taxi.llms.base import LLM
from llm_taxi.types import NOT_SUPPORTED, NotSupportedOr, SupportedParams


async def streaming_response(response: Any) -> AsyncGenerator[str]:
    async for chunk in response:
        if content := chunk.choices[0].delta.content:
            yield content


_PARAM_TYPES: dict[Role, type] = {
    Role.User: ChatCompletionUserMessageParam,
    Role.Assistant: ChatCompletionAssistantMessageParam,
    Role.System: ChatCompletionSystemMessageParam,
}


class OpenAI(OpenAIClient, LLM[list[ChatCompletionMessageParam]]):
    param_mapping: ClassVar[dict[SupportedParams, NotSupportedOr[str]]] = {
        "temperature": "temperature",
        "max_tokens": "max_tokens",
        "top_k": NOT_SUPPORTED,
        "top_p": "top_p",
        "stop": "stop",
        "seed": "seed",
        "frequency_penalty": "frequency_penalty",
        "presence_penalty": "presence_penalty",
        "response_format": "response_format",
        "tools": "tools",
        "tool_choice": "tool_choice",
    }

    @override
    def _convert_messages(
        self,
        messages: list[Message],
    ) -> list[ChatCompletionMessageParam]:
        return [
            _PARAM_TYPES[message.role](role=message.role.value, content=message.content)
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
        response = cast(
            ChatCompletion,
            await self.client.chat.completions.create(
                messages=self._convert_messages(messages),
                **self._get_call_options(llm_options),
            ),
        )

        if content := response.choices[0].message.content:
            return content

        return ""
