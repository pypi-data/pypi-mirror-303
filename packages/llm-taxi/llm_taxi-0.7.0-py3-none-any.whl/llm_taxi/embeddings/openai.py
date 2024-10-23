from llm_taxi.clients.openai import OpenAI
from llm_taxi.embeddings.base import Embedding


class OpenAIEmbedding(OpenAI, Embedding):
    async def embed_text(self, text: str, **kwargs) -> list[float]:
        response = await self.client.embeddings.create(
            model=self.model,
            input=text,
            **kwargs,
        )

        return response.data[0].embedding

    async def embed_texts(self, texts: list[str], **kwargs) -> list[list[float]]:
        response = await self.client.embeddings.create(
            model=self.model,
            input=texts,
            **kwargs,
        )

        return [x.embedding for x in response.data]
