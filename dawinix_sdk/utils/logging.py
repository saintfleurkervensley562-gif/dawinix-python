"""
Logging utilities.
"""

import logging
from typing import Optional


def setup_logging(
    level: int = logging.INFO,
    name: str = "dawinix_sdk",
    handlers: Optional[list] = None,
) -> logging.Logger:
    """Setup logging for the SDK."""
    logger = logging.getLogger(name)
    logger.setLevel(level)

    if handlers is None:
        handler = logging.StreamHandler()
        handler.setLevel(level)
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    else:
        for handler in handlers:
            logger.addHandler(handler)

    return logger
