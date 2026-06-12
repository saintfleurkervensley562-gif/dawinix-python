"""
HTTP client implementation.
"""

import httpx
from typing import Optional, Dict, Any


class HTTPClient:
    """HTTP client for API requests."""

    def __init__(
        self,
        base_url: str,
        api_key: str,
        timeout: float = 30.0,
    ):
        self.base_url = base_url
        self.api_key = api_key
        self.timeout = timeout
        self.client = httpx.Client(
            base_url=base_url,
            headers={"Authorization": f"Bearer {api_key}"},
            timeout=timeout,
        )

    def get(self, path: str, **kwargs) -> Dict[str, Any]:
        """Make GET request."""
        response = self.client.get(path, **kwargs)
        response.raise_for_status()
        return response.json()

    def post(self, path: str, **kwargs) -> Dict[str, Any]:
        """Make POST request."""
        response = self.client.post(path, **kwargs)
        response.raise_for_status()
        return response.json()

    def put(self, path: str, **kwargs) -> Dict[str, Any]:
        """Make PUT request."""
        response = self.client.put(path, **kwargs)
        response.raise_for_status()
        return response.json()

    def delete(self, path: str, **kwargs) -> Dict[str, Any]:
        """Make DELETE request."""
        response = self.client.delete(path, **kwargs)
        response.raise_for_status()
        return response.json()

    def close(self):
        """Close the client."""
        self.client.close()
