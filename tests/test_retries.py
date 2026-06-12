"""
Test utilities module.
"""

import pytest
from dawinix_sdk.utils.retries import retry_with_exponential_backoff


def test_retry_decorator():
    """Test retry decorator."""

    call_count = 0

    @retry_with_exponential_backoff(max_attempts=3)
    def failing_function():
        nonlocal call_count
        call_count += 1
        if call_count < 3:
            raise Exception("Failure")
        return "Success"

    result = failing_function()
    assert result == "Success"
    assert call_count == 3
