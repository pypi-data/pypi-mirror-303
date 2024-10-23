import abc
import warnings
from typing import Any, ClassVar, Generic, TypeVar

from llm_taxi.types import NOT_SUPPORTED, NotSupportedOr, SupportedParams

ClientT = TypeVar("ClientT")


class Client(Generic[ClientT]):
    env_vars: ClassVar[dict[str, str]] = {}
    param_mapping: ClassVar[dict[SupportedParams, NotSupportedOr[str]]] = {}

    def __init__(
        self,
        *,
        model: str,
        api_key: str,
        base_url: str | None = None,
        call_options: dict[str, Any] | None = None,
        client_options: dict[str, Any] | None = None,
    ) -> None:
        """Initialize the Client instance.

        Args:
            model (str): The model to be used.
            api_key (str): The API key for authentication.
            base_url (str, optional): The base URL for the API. Defaults to None.
            call_options (dict[str, Any] | None, optional): Additional keyword arguments for the API call. Defaults to None.
            client_options (dict[str, Any] | None, optional): Additional keyword arguments for the client initialization.

        Returns:
            None
        """
        if not call_options:
            call_options = {}

        if not client_options:
            client_options = {}

        client_options = client_options | {"base_url": base_url, "api_key": api_key}

        self._model = model
        self._api_key = api_key
        self._base_url = base_url
        self._call_options = call_options | {"model": self.model}
        self._client = self._init_client(client_options=client_options)

    @property
    def model(self) -> str:
        return self._model

    @property
    def client(self) -> ClientT:
        return self._client

    @abc.abstractmethod
    def _init_client(self, client_options: dict[str, Any]) -> ClientT:
        raise NotImplementedError

    def _get_call_options(
        self, llm_options: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        if not llm_options:
            llm_options = {}

        llm_options = self._call_options | llm_options

        kept_kwargs: dict[str, Any] = {}
        for key, value in llm_options.items():
            rename = self.param_mapping.get(key)  # pyright: ignore[reportArgumentType]
            if rename == NOT_SUPPORTED:
                warnings.warn(
                    f"Parameter '{key}' is not supported by the API, and will be ignored.",
                    stacklevel=2,
                )
                continue

            kept_kwargs[rename or key] = value

        return kept_kwargs
