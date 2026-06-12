"""
Webhooks for Dawinix events.
"""

from typing import Dict, Any, Callable
import hashlib
import hmac
import json


class WebhookManager:
    """Manages webhook verification and handling."""

    @staticmethod
    def verify_signature(
        payload: str,
        signature: str,
        secret: str,
    ) -> bool:
        """Verify webhook signature."""
        expected_signature = hmac.new(
            secret.encode(),
            payload.encode(),
            hashlib.sha256,
        ).hexdigest()
        return hmac.compare_digest(signature, expected_signature)

    @staticmethod
    def parse_webhook(payload: str) -> Dict[str, Any]:
        """Parse webhook payload."""
        return json.loads(payload)
