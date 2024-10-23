from google import generativeai as genai

from llm_taxi.clients.google import Google
from llm_taxi.embeddings import Embedding


class GoogleEmbedding(Embedding, Google):
    async def embed_text(self, text: str) -> list[float]:
        response = genai.embed_content(self.model, content=text)

        return response["embedding"]

    async def embed_texts(self, texts: list[str]) -> list[list[float]]:
        response = genai.embed_content(self.model, content=texts)

        return response["embedding"]
