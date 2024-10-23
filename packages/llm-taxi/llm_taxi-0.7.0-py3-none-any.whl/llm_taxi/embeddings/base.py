import abc


class Embedding(metaclass=abc.ABCMeta):
    """Abstract base class for embedding text using various embedding models.

    This class defines the interface for embedding single texts and multiple texts.
    Subclasses must implement the `embed_text` and `embed_texts` methods.

    Methods:
        embed_text(text: str) -> list[float]:
            Abstract method to embed a single text string into a list of floats.

        embed_texts(texts: list[str]) -> list[list[float]]:
            Abstract method to embed multiple text strings into a list of lists of floats.
    """

    @abc.abstractmethod
    async def embed_text(self, text: str) -> list[float]:
        raise NotImplementedError

    @abc.abstractmethod
    async def embed_texts(self, texts: list[str]) -> list[list[float]]:
        raise NotImplementedError
