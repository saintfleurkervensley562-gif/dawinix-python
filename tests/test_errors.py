"""
Test cases for errors module.
"""

import pytest
from dawinix_sdk.errors import (
    DawinixError,
    APIError,
    RateLimitError,
    ValidationError,
)


def test_dawinix_error():
    """Test base error."""
    error = DawinixError("Test error", "test_code")
    assert error.message == "Test error"
    assert error.code == "test_code"


def test_api_error():
    """Test API error."""
    error = APIError("API failed", "api_error", 500)
    assert error.status_code == 500


def test_rate_limit_error():
    """Test rate limit error."""
    error = RateLimitError("Too many requests", retry_after=60)
    assert error.retry_after == 60


def test_validation_error():
    """Test validation error."""
    error = ValidationError("Invalid input", "field_name")
    assert error.field == "field_name"
