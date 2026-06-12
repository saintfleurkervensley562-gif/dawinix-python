"""
Dawinix Python SDK

Official Python library for the Dawinix API.
"""

__version__ = "1.0.0"
__author__ = "Dawinix Inc."
__email__ = "support@dawinix.com"

from .client import Dawinix, AsyncDawinix
from .build import Agent, AsyncAgent, Skill
from .types import AgentResult, AgentConfig, SkillType
from .errors import (
    DawinixError,
    APIError,
    RateLimitError,
    TimeoutError,
    ContextLengthError,
    AgentLoopError,
    ValidationError,
)

__all__ = [
    "Dawinix",
    "AsyncDawinix",
    "Agent",
    "AsyncAgent",
    "Skill",
    "AgentResult",
    "AgentConfig",
    "SkillType",
    "DawinixError",
    "APIError",
    "RateLimitError",
    "TimeoutError",
    "ContextLengthError",
    "AgentLoopError",
    "ValidationError",
]
