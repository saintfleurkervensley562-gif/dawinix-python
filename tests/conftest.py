"""
Pytest configuration.
"""

import os
import pytest


def pytest_configure(config):
    """Configure pytest."""
    config.addinivalue_line(
        "markers", "integration: mark test as an integration test"
    )


@pytest.fixture
def api_key():
    """Get API key from environment."""
    return os.getenv("DAWINIX_API_KEY", "daw-sk-test123")


@pytest.fixture
def mock_response():
    """Mock API response."""
    return {
        "id": "test-123",
        "object": "agent_result",
        "output": "Test output",
        "usage": {
            "total_tokens": 100,
            "prompt_tokens": 50,
            "completion_tokens": 50,
        },
    }
