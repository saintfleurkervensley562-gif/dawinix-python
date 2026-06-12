"""
Main Dawinix client for API interactions.
"""

import os
from typing import Optional, List, Dict, Any
import httpx

from .build import Agent, AsyncAgent
from .resources import (
    ModelsResource,
    ChatsResource,
    AgentsResource,
)


class Dawinix:
    """Synchronous Dawinix API client."""

    def __init__(
        self,
        api_key: Optional[str] = None,
        base_url: str = "https://api.dawinix.com/v1",
        timeout: float = 30.0,
    ):
        self.api_key = api_key or os.getenv("DAWINIX_API_KEY")
        if not self.api_key:
            raise ValueError("DAWINIX_API_KEY not provided or set in environment")

        self.base_url = base_url
        self.timeout = timeout
        self.client = httpx.Client(
            base_url=base_url,
            headers={"Authorization": f"Bearer {self.api_key}"},
            timeout=timeout,
        )

        # Initialize resources
        self.models = ModelsResource(self)
        self.chats = ChatsResource(self)
        self.agents = AgentsResource(self)

    def _request(
        self,
        method: str,
        path: str,
        **kwargs,
    ) -> Dict[str, Any]:
        """Make an API request."""
        response = self.client.request(method, path, **kwargs)
        response.raise_for_status()
        return response.json()

    def close(self):
        """Close the client."""
        self.client.close()

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.close()


class AsyncDawinix:
    """Asynchronous Dawinix API client."""

    def __init__(
        self,
        api_key: Optional[str] = None,
        base_url: str = "https://api.dawinix.com/v1",
        timeout: float = 30.0,
    ):
        self.api_key = api_key or os.getenv("DAWINIX_API_KEY")
        if not self.api_key:
            raise ValueError("DAWINIX_API_KEY not provided or set in environment")

        self.base_url = base_url
        self.timeout = timeout
        self.client = None

    async def _init_client(self):
        """Initialize async client."""
        if self.client is None:
            self.client = httpx.AsyncClient(
                base_url=self.base_url,
                headers={"Authorization": f"Bearer {self.api_key}"},
                timeout=self.timeout,
            )

    async def _request(
        self,
        method: str,
        path: str,
        **kwargs,
    ) -> Dict[str, Any]:
        """Make an async API request."""
        await self._init_client()
        response = await self.client.request(method, path, **kwargs)
        response.raise_for_status()
        return response.json()

    async def close(self):
        """Close the client."""
        if self.client:
            await self.client.aclose()

    async def __aenter__(self):
        return self

    async def __aexit__(self, *args):
        await self.close()
