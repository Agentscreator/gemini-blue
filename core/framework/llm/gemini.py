"""Google Gemini LLM provider - wrapper around LiteLLM for Gemini models."""

import os
from typing import Any

from framework.llm.litellm import LiteLLMProvider
from framework.llm.provider import LLMProvider, LLMResponse, Tool


def _get_api_key_from_credential_store() -> str | None:
    """Get API key from CredentialStoreAdapter or environment.

    Priority:
    1. CredentialStoreAdapter (supports encrypted storage + env vars)
    2. os.environ fallback
    """
    try:
        from aden_tools.credentials import CredentialStoreAdapter

        creds = CredentialStoreAdapter.default()
        if creds.is_available("google"):
            return creds.get("google")
    except ImportError:
        pass
    return os.environ.get("GOOGLE_API_KEY") or os.environ.get("GEMINI_API_KEY")


class GeminiProvider(LLMProvider):
    """
    Google Gemini LLM provider.

    This is a convenience wrapper that internally uses LiteLLMProvider.
    Provides a clean interface for Gemini models while benefiting from
    LiteLLM's unified interface and features.

    Supports:
    - gemini-2.0-flash-exp (fast, cost-effective, extended context)
    - gemini-1.5-pro (advanced reasoning, multimodal)
    - gemini-1.5-flash (balanced speed and capability)
    """

    def __init__(
        self,
        api_key: str | None = None,
        model: str = "gemini-2.0-flash-exp",
    ):
        """
        Initialize the Gemini provider.

        Args:
            api_key: Google API key. If not provided, uses CredentialStoreAdapter
                     or GOOGLE_API_KEY / GEMINI_API_KEY env var.
            model: Model to use (default: gemini-2.0-flash-exp)
                   Options: gemini-2.0-flash-exp, gemini-1.5-pro, gemini-1.5-flash
        """
        # Delegate to LiteLLMProvider internally.
        self.api_key = api_key or _get_api_key_from_credential_store()
        if not self.api_key:
            raise ValueError(
                "Google API key required. Set GOOGLE_API_KEY or GEMINI_API_KEY env var "
                "or pass api_key."
            )

        # Ensure model has gemini/ prefix for LiteLLM routing
        if not model.startswith("gemini/") and not model.startswith("gemini-"):
            model = f"gemini/{model}"
        elif model.startswith("gemini-") and not model.startswith("gemini/"):
            model = f"gemini/{model}"

        self.model = model

        self._provider = LiteLLMProvider(
            model=model,
            api_key=self.api_key,
        )

    def complete(
        self,
        messages: list[dict[str, Any]],
        system: str = "",
        tools: list[Tool] | None = None,
        max_tokens: int = 1024,
        response_format: dict[str, Any] | None = None,
        json_mode: bool = False,
        max_retries: int | None = None,
    ) -> LLMResponse:
        """Generate a completion from Gemini (via LiteLLM)."""
        return self._provider.complete(
            messages=messages,
            system=system,
            tools=tools,
            max_tokens=max_tokens,
            response_format=response_format,
            json_mode=json_mode,
            max_retries=max_retries,
        )

    async def acomplete(
        self,
        messages: list[dict[str, Any]],
        system: str = "",
        tools: list[Tool] | None = None,
        max_tokens: int = 1024,
        response_format: dict[str, Any] | None = None,
        json_mode: bool = False,
        max_retries: int | None = None,
    ) -> LLMResponse:
        """Async completion via LiteLLM."""
        return await self._provider.acomplete(
            messages=messages,
            system=system,
            tools=tools,
            max_tokens=max_tokens,
            response_format=response_format,
            json_mode=json_mode,
            max_retries=max_retries,
        )
