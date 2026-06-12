"""
Test cases for agent.
"""

import pytest
from dawinix_sdk.build import Agent, Skill


def test_agent_initialization():
    """Test agent initialization."""
    agent = Agent(
        api_key="daw-sk-test123",
        model="dawinix-4",
        skills=[Skill.WEB_SEARCH],
    )
    assert agent.api_key == "daw-sk-test123"
    assert agent.model == "dawinix-4"


def test_agent_missing_api_key():
    """Test agent without API key."""
    with pytest.raises(ValueError):
        Agent()
