"""
Validation utilities.
"""

from ..errors import ValidationError


def validate_api_key(api_key: str) -> bool:
    """Validate API key format."""
    if not api_key:
        raise ValidationError("API key cannot be empty", field="api_key")
    if not api_key.startswith("daw-sk-"):
        raise ValidationError("Invalid API key format", field="api_key")
    return True


def validate_task(task: str) -> bool:
    """Validate task string."""
    if not task:
        raise ValidationError("Task cannot be empty", field="task")
    if len(task) > 100000:
        raise ValidationError("Task exceeds maximum length", field="task")
    return True


def validate_model(model: str) -> bool:
    """Validate model name."""
    valid_models = ["dawinix-4", "dawinix-4-mini", "dawinix-3"]
    if model not in valid_models:
        raise ValidationError(f"Invalid model: {model}", field="model")
    return True
