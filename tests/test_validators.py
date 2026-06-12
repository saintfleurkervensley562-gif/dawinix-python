"""
Test cases for validators.
"""

import pytest
from dawinix_sdk.utils.validators import (
    validate_api_key,
    validate_task,
    validate_model,
)
from dawinix_sdk.errors import ValidationError


def test_validate_api_key_valid():
    """Test valid API key."""
    assert validate_api_key("daw-sk-test123")


def test_validate_api_key_invalid():
    """Test invalid API key."""
    with pytest.raises(ValidationError):
        validate_api_key("invalid-key")


def test_validate_task_valid():
    """Test valid task."""
    assert validate_task("This is a valid task")


def test_validate_task_empty():
    """Test empty task."""
    with pytest.raises(ValidationError):
        validate_task("")


def test_validate_model_valid():
    """Test valid model."""
    assert validate_model("dawinix-4")


def test_validate_model_invalid():
    """Test invalid model."""
    with pytest.raises(ValidationError):
        validate_model("invalid-model")
