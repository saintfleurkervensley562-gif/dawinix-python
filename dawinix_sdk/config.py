"""
Configuration module.
"""

import os
from typing import Optional


class Config:
    """SDK configuration."""

    def __init__(
        self,
        api_key: Optional[str] = None,
        base_url: str = "https://api.dawinix.com/v1",
        timeout: float = 30.0,
        max_retries: int = 3,
        enable_logging: bool = False,
    ):
        self.api_key = api_key or os.getenv("DAWINIX_API_KEY")
        self.base_url = base_url
        self.timeout = timeout
        self.max_retries = max_retries
        self.enable_logging = enable_logging

    def validate(self) -> bool:
        """Validate configuration."""
        if not self.api_key:
            raise ValueError("API key is required")
        return True
