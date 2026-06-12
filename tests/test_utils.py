"""
Testing utilities.
"""

from typing import Any, Dict
from unittest.mock import Mock, MagicMock


class MockClient:
    """Mock Dawinix client for testing."""

    def __init__(self, api_key: str = "daw-sk-test"):
        self.api_key = api_key
        self.models = Mock()
        self.chats = Mock()
        self.agents = Mock()

    def _request(self, method: str, path: str, **kwargs) -> Dict[str, Any]:
        """Mock request method."""
        return {"status": "success", "data": {}}


def create_mock_agent_result():
    """Create a mock agent result."""
    from dawinix_sdk.types import UsageInfo
    from dawinix_sdk.types.agent import AgentResult

    return AgentResult(
        output="Test output",
        status="success",
        elapsed_ms=1000,
        usage=UsageInfo(
            total_tokens=100,
            prompt_tokens=50,
            completion_tokens=50,
        ),
    )
