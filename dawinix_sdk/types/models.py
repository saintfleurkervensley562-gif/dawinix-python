"""
Model-related type definitions.
"""

from dataclasses import dataclass
from typing import Optional, List
from enum import Enum


class ModelFamily(str, Enum):
    """Model families."""

    DAWINIX_4 = "dawinix-4"
    DAWINIX_4_MINI = "dawinix-4-mini"
    DAWINIX_3 = "dawinix-3"


@dataclass
class ModelInfo:
    """Information about a model."""

    name: str
    family: ModelFamily
    context_window: int
    max_tokens: int
    cost_per_1k_input: float
    cost_per_1k_output: float


@dataclass
class Model:
    """Represents an AI model."""

    id: str
    object: str = "model"
    owned_by: str = "dawinix"
    info: Optional[ModelInfo] = None
