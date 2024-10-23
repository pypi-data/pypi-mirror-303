from collections.abc import AsyncGenerator
from typing import Any, ClassVar, cast

from groq.types.chat import ChatCompletion
from groq.types.chat.chat_completion_assistant_message_param import (
    ChatCompletionAssistantMessageParam,
)
from groq.types.chat.chat_completion_system_message_param import (
    ChatCompletionSystemMessageParam,
)
from groq.types.chat.chat_completion_user_message_param import (
    ChatCompletionUserMessageParam,
)
from typing_extensions import override

from llm_taxi.clients.groq import Groq as GroqClient
from llm_taxi.conversation import Message, Role
from llm_taxi.llms.base import LLM
from llm_taxi.llms.openai import streaming_response
from llm_taxi.types import NOT_SUPPORTED, NotSupportedOr, SupportedParams

_PARAM_TYPES: dict[Role, type] = {
    Role.User: ChatCompletionUserMessageParam,
    Role.Assistant: ChatCompletionAssistantMessageParam,
    Role.System: ChatCompletionSystemMessageParam,
}


class Groq(GroqClient, LLM[list[Any]]):
    param_mapping: ClassVar[dict[SupportedParams, NotSupportedOr[str]]] = {
        "temperature": "temperature",
        "max_tokens": "max_tokens",
        "top_k": NOT_SUPPORTED,
        "top_p": "top_p",
        "stop": "stop",
        "seed": "seed",
        "frequency_penalty": NOT_SUPPORTED,
        "presence_penalty": NOT_SUPPORTED,
        "response_format": "response_format",
        "tools": "tools",
        "tool_choice": "tool_choice",
    }

    @override
    def _convert_messages(self, messages: list[Message]) -> list[Any]:
        return [
            _PARAM_TYPES[message.role](
                role=message.role.value,
                content=message.content,
            )
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
