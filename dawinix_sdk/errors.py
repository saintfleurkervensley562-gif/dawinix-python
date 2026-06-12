"""
Error definitions for Dawinix SDK.
"""

from typing import Optional


class DawinixError(Exception):
    """Base exception for all Dawinix SDK errors."""

    def __init__(self, message: str, code: Optional[str] = None):
        self.message = message
        self.code = code
        super().__init__(self.message)


class APIError(DawinixError):
    """Raised when API returns an error."""

    def __init__(
        self,
        message: str,
        code: str,
        status_code: int,
        headers: Optional[dict] = None,
    ):
        super().__init__(message, code)
        self.status_code = status_code
        self.headers = headers or {}


class RateLimitError(APIError):
    """Raised when rate limit is exceeded."""

    def __init__(
        self,
        message: str,
        retry_after: Optional[int] = None,
        reset_at: Optional[str] = None,
    ):
        super().__init__(message, "rate_limit_error", 429)
        self.retry_after = retry_after
        self.reset_at = reset_at


class TimeoutError(DawinixError):
    """Raised when a request times out."""

    pass


class ContextLengthError(DawinixError):
    """Raised when task exceeds context length."""

    def __init__(self, message: str, max_length: int, current_length: int):
        super().__init__(message, "context_length_error")
        self.max_length = max_length
        self.current_length = current_length


class AgentLoopError(DawinixError):
    """Raised when agent exceeds max steps."""

    def __init__(self, message: str, partial_output: Optional[str] = None):
        super().__init__(message, "agent_loop_error")
        self.partial_output = partial_output


class ValidationError(DawinixError):
    """Raised when validation fails."""

    def __init__(self, message: str, field: Optional[str] = None):
        super().__init__(message, "validation_error")
        self.field = field


class AuthenticationError(APIError):
    """Raised when authentication fails."""

    pass


class PermissionError(APIError):
    """Raised when user lacks permissions."""

    pass


class NotFoundError(APIError):
    """Raised when resource not found."""

    pass
