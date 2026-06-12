"""
Response handling utilities.
"""

from typing import Dict, Any, TypeVar, Optional
from dataclasses import dataclass


T = TypeVar("T")


@dataclass
class Response:
    """Wrapper for API responses."""

    status_code: int
    data: Dict[str, Any]
    headers: Optional[Dict[str, str]] = None

    @property
    def is_success(self) -> bool:
        """Check if response is successful."""
        return 200 <= self.status_code < 300

    @property
    def is_error(self) -> bool:
        """Check if response is an error."""
        return self.status_code >= 400
