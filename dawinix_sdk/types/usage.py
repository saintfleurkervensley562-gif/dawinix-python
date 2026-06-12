"""
Usage information type definitions.
"""

from dataclasses import dataclass


@dataclass
class UsageInfo:
    """Information about API usage."""

    total_tokens: int
    prompt_tokens: int
    completion_tokens: int
    cached_tokens: int = 0

    @property
    def total_tokens_with_cache(self) -> int:
        """Get total tokens including cached tokens."""
        return self.total_tokens + self.cached_tokens
