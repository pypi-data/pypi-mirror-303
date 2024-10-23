import logging
from collections.abc import Awaitable, Callable, Iterable
from typing import cast

from llm_taxi.utils import chunk, gather_with_concurrency

logger = logging.getLogger(__name__)


async def batch_create_embeddings(
    texts: Iterable[str],
    embedding_fn: Callable[[list[str]], Awaitable[list[list[float]]]],
    *,
    batch_size: int = 16,
    concurrency: int = 10,
    retry: bool = True,
) -> list[tuple[int, list[float]]]:
    """Asynchronously create embeddings for a list of texts in batches with optional retry logic.

    Args:
        texts (Iterable[str]): An iterable of strings for which embeddings need to be created.
        embedding_fn (Callable[[list[str]], Awaitable[list[list[float]]]]):
            A callable function that takes a list of strings and returns an awaitable list of embeddings.
        batch_size (int, optional): The size of each batch. Defaults to 16.
        concurrency (int, optional): The level of concurrency for processing batches. Defaults to 10.
        retry (bool, optional): Whether to retry failed batches by splitting them into smaller batches. Defaults to True.

    Returns:
        list[tuple[int, list[float]]]: A list of tuples containing the index of the text and its corresponding embedding.
            The returned list contains only the indices and embeddings of successfully created embeddings.
    """

    async def _create_embeddings(
        ordered_batch: Iterable[tuple[int, str]],
    ) -> (
        tuple[bool, list[tuple[int, str]]] | tuple[bool, list[tuple[int, list[float]]]]
    ):
        indices, batch = zip(*ordered_batch, strict=True)
        indices = cast(tuple[int], indices)
        batch = cast(tuple[str], batch)

        try:
            embeddings = await embedding_fn(list(batch))

        except BaseException:
            logger.exception("failed to create embeddings, texts: %s", batch)

            return False, list(zip(indices, batch, strict=True))

        return True, list(zip(indices, embeddings, strict=True))

    min_split_batch_size = 2
    ordered_embeddings = []

    futures = [
        _create_embeddings(ordered_batch)
        for ordered_batch in chunk(enumerate(texts), size=batch_size)
    ]

    while True:
        if not futures:
            break

        responses = await gather_with_concurrency(concurrency, *futures)
        futures = []
        for response in responses:
            if isinstance(response, BaseException):
                continue

            success, payload_or_result = response
            if success:
                ordered_embeddings += payload_or_result
                continue

            indices, batch = zip(*payload_or_result, strict=True)
            size = len(indices)
            if retry and size >= min_split_batch_size:
                size //= 2
                futures += [
                    _create_embeddings(zip(indices[:size], batch[:size], strict=True)),
                ]
                futures += [
                    _create_embeddings(zip(indices[size:], batch[size:], strict=True)),
                ]
                continue

    ordered_embeddings.sort(key=lambda x: x[0])

    return ordered_embeddings
