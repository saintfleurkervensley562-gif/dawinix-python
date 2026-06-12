"""
Async HTTP client implementation.
"""

import httpx
from typing import Optional, Dict, Any


class AsyncHTTPClient:
    """Async HTTP client for API requests."""

    def __init__(
        self,
        base_url: str,
        api_key: str,
        timeout: float = 30.0,
    ):
        self.base_url = base_url
        self.api_key = api_key
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

    async def get(self, path: str, **kwargs) -> Dict[str, Any]:
        """Make async GET request."""
        await self._init_client()
        response = await self.client.get(path, **kwargs)
        response.raise_for_status()
        return response.json()

    async def post(self, path: str, **kwargs) -> Dict[str, Any]:
        """Make async POST request."""
        await self._init_client()
        response = await self.client.post(path, **kwargs)
        response.raise_for_status()
        return response.json()

    async def close(self):
        """Close the client."""
        if self.client:
            await self.client.aclose()
