"""
Test constants module.
"""

import pytest
from dawinix_sdk.constants import (
    AVAILABLE_MODELS,
    AVAILABLE_MODES,
    API_BASE_URL,
    MAX_TASK_LENGTH,
)


def test_models_list():
    """Test available models."""
    assert len(AVAILABLE_MODELS) > 0
    assert "dawinix-4" in AVAILABLE_MODELS


def test_modes_list():
    """Test available modes."""
    assert len(AVAILABLE_MODES) > 0
    assert "balanced" in AVAILABLE_MODES


def test_api_base_url():
    """Test API base URL."""
    assert API_BASE_URL.startswith("https://")


def test_max_task_length():
    """Test max task length."""
    assert MAX_TASK_LENGTH > 0
