"""
Chats API resource.
"""

from typing import List, Dict, Any, Optional


class ChatsResource:
    """Resource for chats API."""

    def __init__(self, client):
        self.client = client

    def create_completion(
        self,
        model: str,
        messages: List[Dict[str, str]],
        temperature: float = 0.7,
        **kwargs,
    ) -> Dict[str, Any]:
        """Create a chat completion."""
        data = {
            "model": model,
            "messages": messages,
            "temperature": temperature,
            **kwargs,
        }
        return self.client._request("POST", "/chat/completions", json=data)

    def stream(
        self,
        model: str,
        messages: List[Dict[str, str]],
        **kwargs,
    ):
        """Stream chat completions."""
        # Implementation for streaming
        pass
