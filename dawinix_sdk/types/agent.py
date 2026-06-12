"""
Agent-related type definitions.
"""

from dataclasses import dataclass
from typing import Optional, List, Dict, Any
from enum import Enum


class SkillType(str, Enum):
    """Available agent skills."""

    HTTP_REQUEST = "http_request"
    WEB_SEARCH = "web_search"
    FILE_PROCESSING = "file_processing"
    CODE_EXECUTION = "code_execution"
    SUMMARIZE = "summarize"
    EMAIL = "email"
    SLACK = "slack"
    GITHUB = "github"
    DATABASE = "database"
    IMAGE_GENERATION = "image_generation"
    VISION = "vision"


class AgentMode(str, Enum):
    """Agent execution modes."""

    BALANCED = "balanced"
    PRECISE = "precise"
    SPEED = "speed"
    STRICT = "strict"


@dataclass
class AgentConfig:
    """Configuration for an agent."""

    api_key: str
    model: str = "dawinix-4"
    skills: Optional[List[SkillType]] = None
    max_steps: int = 15
    timeout: int = 120
    temperature: float = 0.7
    top_p: float = 0.9


@dataclass
class AgentResult:
    """Result from agent execution."""

    output: str
    status: str
    elapsed_ms: int
    usage: "UsageInfo"
    raw_json: Optional[str] = None
    parsed: Optional[Any] = None
    partial_output: Optional[str] = None
