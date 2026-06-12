"""
Chat-related type definitions.
"""

from dataclasses import dataclass
from typing import Optional, List
from enum import Enum


class MessageRole(str, Enum):
    """Chat message roles."""

    USER = "user"
    ASSISTANT = "assistant"
    SYSTEM = "system"


@dataclass
class ChatMessage:
    """Represents a chat message."""

    role: MessageRole
    content: str
    name: Optional[str] = None


@dataclass
class ChatCompletionResponse:
    """Response from chat completion."""

    message: ChatMessage
    finish_reason: str
    tokens: int
    model: str
