"""
Models resource tests.
"""

import pytest
from dawinix_sdk.resources.models import ModelsResource
from unittest.mock import Mock


def test_models_list():
    """Test listing models."""
    mock_client = Mock()
    mock_client._request.return_value = [
        {"id": "dawinix-4", "name": "Dawinix 4"},
    ]

    resource = ModelsResource(mock_client)
    result = resource.list()

    assert len(result) > 0
    mock_client._request.assert_called_once()


def test_models_retrieve():
    """Test retrieving model info."""
    mock_client = Mock()
    mock_client._request.return_value = {"id": "dawinix-4", "name": "Dawinix 4"}

    resource = ModelsResource(mock_client)
    result = resource.retrieve("dawinix-4")

    assert result["id"] == "dawinix-4"
