"""
Retry utilities with exponential backoff.
"""

import time
from typing import TypeVar, Callable, Any
from functools import wraps

T = TypeVar("T")


def retry_with_exponential_backoff(
    max_attempts: int = 5,
    base_wait: float = 1,
    max_wait: float = 60,
    exponential_base: float = 2,
):
    """Decorator for retry with exponential backoff."""

    def decorator(func: Callable[..., T]) -> Callable[..., T]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> T:
            attempt = 0
            while attempt < max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    attempt += 1
                    if attempt >= max_attempts:
                        raise

                    wait_time = min(base_wait * (exponential_base ** (attempt - 1)), max_wait)
                    time.sleep(wait_time)

        return wrapper

    return decorator
