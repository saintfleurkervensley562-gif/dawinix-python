"""
Context managers for SDK usage.
"""

from contextlib import contextmanager
from typing import Generator
from .client import Dawinix


@contextmanager
def dawinix_client(api_key: str) -> Generator[Dawinix, None, None]:
    """Context manager for Dawinix client."""
    client = Dawinix(api_key=api_key)
    try:
        yield client
    finally:
        client.close()
