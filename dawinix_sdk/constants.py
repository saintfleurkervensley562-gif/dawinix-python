"""
Constants used across the SDK.
"""

# API Endpoints
API_BASE_URL = "https://api.dawinix.com/v1"
API_TIMEOUT = 30.0

# Model names
MODEL_DAWINIX_4 = "dawinix-4"
MODEL_DAWINIX_4_MINI = "dawinix-4-mini"
MODEL_DAWINIX_3 = "dawinix-3"

AVAILABLE_MODELS = [
    MODEL_DAWINIX_4,
    MODEL_DAWINIX_4_MINI,
    MODEL_DAWINIX_3,
]

# Agent modes
MODE_BALANCED = "balanced"
MODE_PRECISE = "precise"
MODE_SPEED = "speed"
MODE_STRICT = "strict"

AVAILABLE_MODES = [MODE_BALANCED, MODE_PRECISE, MODE_SPEED, MODE_STRICT]

# Skills
SKILL_HTTP_REQUEST = "http_request"
SKILL_WEB_SEARCH = "web_search"
SKILL_FILE_PROCESSING = "file_processing"
SKILL_CODE_EXECUTION = "code_execution"
SKILL_SUMMARIZE = "summarize"

# Rate limits
DEFAULT_MAX_RETRIES = 3
DEFAULT_RETRY_DELAY = 1
MAX_RETRY_DELAY = 60

# Context limits
MAX_TASK_LENGTH = 100000
MAX_CONTEXT_WINDOW = 128000
