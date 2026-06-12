"""
Agents API resource.
"""

from typing import List, Dict, Any, Optional


class AgentsResource:
    """Resource for agents API."""

    def __init__(self, client):
        self.client = client

    def run(
        self,
        task: str,
        model: str = "dawinix-4",
        mode: str = "balanced",
        **kwargs,
    ) -> Dict[str, Any]:
        """Run an agent task."""
        data = {
            "task": task,
            "model": model,
            "mode": mode,
            **kwargs,
        }
        return self.client._request("POST", "/agents/run", json=data)

    def batch(
        self,
        tasks: List[str],
        model: str = "dawinix-4",
        **kwargs,
    ) -> List[Dict[str, Any]]:
        """Run multiple tasks in batch."""
        data = {
            "tasks": tasks,
            "model": model,
            **kwargs,
        }
        return self.client._request("POST", "/agents/batch", json=data)

    def stream(
        self,
        task: str,
        model: str = "dawinix-4",
        **kwargs,
    ):
        """Stream agent execution."""
        # Implementation for streaming
        pass
