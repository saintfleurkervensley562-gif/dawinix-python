"""
Decorators for SDK functionality.
"""

from functools import wraps
from typing import Callable, Any
import logging

logger = logging.getLogger(__name__)


def log_api_call(func: Callable) -> Callable:
    """Decorator to log API calls."""

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        logger.debug(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        logger.debug(f"{func.__name__} returned {type(result)}")
        return result

    return wrapper


def handle_errors(func: Callable) -> Callable:
    """Decorator to handle common errors."""

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logger.error(f"Error in {func.__name__}: {e}")
            raise

    return wrapper


def require_api_key(func: Callable) -> Callable:
    """Decorator to require API key."""

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        # Check if api_key is provided
        if "api_key" not in kwargs or not kwargs["api_key"]:
            raise ValueError("API key is required")
        return func(*args, **kwargs)

    return wrapper
