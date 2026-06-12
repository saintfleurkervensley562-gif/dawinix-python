"""
Pagination utilities for API results.
"""

from typing import Generic, TypeVar, List, Dict, Any

T = TypeVar("T")


class Paginator(Generic[T]):
    """Paginator for API results."""

    def __init__(
        self,
        items: List[T],
        page: int = 1,
        page_size: int = 10,
        total: int = 0,
    ):
        self.items = items
        self.page = page
        self.page_size = page_size
        self.total = total

    @property
    def total_pages(self) -> int:
        """Get total number of pages."""
        return (self.total + self.page_size - 1) // self.page_size

    @property
    def has_next(self) -> bool:
        """Check if there's a next page."""
        return self.page < self.total_pages

    @property
    def has_previous(self) -> bool:
        """Check if there's a previous page."""
        return self.page > 1
