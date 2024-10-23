from llm_taxi.clients.mistral import Mistral
from llm_taxi.embeddings.base import Embedding


class MistralEmbedding(Mistral, Embedding):
    async def embed_text(self, text: str) -> list[float]:
        response = await self.client.embeddings(model=self.model, input=text)

        return response.data[0].embedding

    async def embed_texts(self, texts: list[str]) -> list[list[float]]:
        response = await self.client.embeddings(model=self.model, input=texts)

        return [x.embedding for x in response.data]
