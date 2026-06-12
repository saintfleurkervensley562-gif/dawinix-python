"""
Resource base class for API resources.
"""

from typing import Any, Dict


class BaseResource:
    """Base class for API resources."""

    def __init__(self, client: Any):
        self.client = client

    def _make_request(
        self,
        method: str,
        path: str,
        **kwargs: Any,
    ) -> Dict[str, Any]:
        """Make an API request."""
        return self.client._request(method, path, **kwargs)
