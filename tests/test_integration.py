"""
Integration tests.
"""

import pytest
import os
from dawinix_sdk import Dawinix


@pytest.mark.integration
def test_client_connection():
    """Test client can connect."""
    api_key = os.getenv("DAWINIX_API_KEY")
    if not api_key:
        pytest.skip("DAWINIX_API_KEY not set")

    client = Dawinix(api_key=api_key)
    # Test connection
    assert client is not None


@pytest.mark.integration
def test_list_models():
    """Test listing models."""
    api_key = os.getenv("DAWINIX_API_KEY")
    if not api_key:
        pytest.skip("DAWINIX_API_KEY not set")

    client = Dawinix(api_key=api_key)
    models = client.models.list()
    assert isinstance(models, list)
