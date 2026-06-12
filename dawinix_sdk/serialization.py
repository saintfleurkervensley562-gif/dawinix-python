"""
Serialization utilities.
"""

import json
from typing import Any, Dict


class JSONSerializer:
    """JSON serialization utilities."""

    @staticmethod
    def serialize(obj: Any) -> str:
        """Serialize object to JSON."""
        return json.dumps(obj, default=str)

    @staticmethod
    def deserialize(data: str) -> Dict[str, Any]:
        """Deserialize JSON string."""
        return json.loads(data)
