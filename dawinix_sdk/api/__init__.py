"""
Configuration and API module.
"""

from typing import Optional, Dict, Any


class APIConfig:
    """API configuration."""

    def __init__(
        self,
        base_url: str = "https://api.dawinix.com/v1",
        timeout: float = 30.0,
        max_retries: int = 3,
    ):
        self.base_url = base_url
        self.timeout = timeout
        self.max_retries = max_retries


class APIRequest:
    """Represents an API request."""

    def __init__(
        self,
        method: str,
        path: str,
        headers: Optional[Dict[str, str]] = None,
        json: Optional[Dict[str, Any]] = None,
    ):
        self.method = method
        self.path = path
        self.headers = headers or {}
        self.json = json


class APIResponse:
    """Represents an API response."""

    def __init__(
        self,
        status_code: int,
        data: Dict[str, Any],
        headers: Optional[Dict[str, str]] = None,
    ):
        self.status_code = status_code
        self.data = data
        self.headers = headers or {}
