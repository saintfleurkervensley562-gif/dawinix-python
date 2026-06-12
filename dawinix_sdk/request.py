"""
Request handling utilities.
"""

from typing import Dict, Any, Optional
from dataclasses import dataclass


@dataclass
class Request:
    """Wrapper for API requests."""

    method: str
    path: str
    headers: Optional[Dict[str, str]] = None
    body: Optional[Dict[str, Any]] = None

    def to_dict(self) -> Dict[str, Any]:
        """Convert request to dictionary."""
        return {
            "method": self.method,
            "path": self.path,
            "headers": self.headers or {},
            "body": self.body or {},
        }
