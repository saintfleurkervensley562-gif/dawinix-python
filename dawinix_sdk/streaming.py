"""
Streaming utilities for API responses.
"""

from typing import Generator, Dict, Any, Optional


class StreamIterator:
    """Iterator for streaming API responses."""

    def __init__(self, response_generator: Generator[str, None, None]):
        self.generator = response_generator

    def __iter__(self):
        return self

    def __next__(self) -> str:
        return next(self.generator)
