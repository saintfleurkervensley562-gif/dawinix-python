"""
Models API resource.
"""

from typing import List, Dict, Any


class ModelsResource:
    """Resource for models API."""

    def __init__(self, client):
        self.client = client

    def list(self) -> List[Dict[str, Any]]:
        """List available models."""
        return self.client._request("GET", "/models")

    def retrieve(self, model_id: str) -> Dict[str, Any]:
        """Retrieve model information."""
        return self.client._request("GET", f"/models/{model_id}")
