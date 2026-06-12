"""
Test cases for client.
"""

import pytest
from dawinix_sdk.client import Dawinix


def test_client_initialization():
    """Test client initialization."""
    client = Dawinix(api_key="daw-sk-test123")
    assert client.api_key == "daw-sk-test123"


def test_client_missing_api_key():
    """Test client without API key."""
    with pytest.raises(ValueError):
        Dawinix()
