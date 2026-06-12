"""
Example: Cron job for daily digest.
"""

import os
import sys
import logging
from datetime import datetime, timedelta
from dawinix_sdk.build import Agent, Skill

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
)
log = logging.getLogger(__name__)


def main():
    """Generate daily digest."""
    api_key = os.getenv("DAWINIX_API_KEY")
    if not api_key:
        log.error("DAWINIX_API_KEY not set")
        sys.exit(1)

    agent = Agent(
        api_key=api_key,
        model="dawinix-4",
        skills=[Skill.HTTP_REQUEST, Skill.SUMMARIZE],
        max_steps=15,
        timeout=120,
    )

    yesterday = (datetime.utcnow() - timedelta(days=1)).strftime("%Y-%m-%d")

    try:
        result = agent.run(
            task=f"Generate daily digest for {yesterday}",
            mode="precise",
        )
        log.info(f"Digest generated: {result.elapsed_ms}ms")
        print(result.output)
        return 0
    except Exception as e:
        log.error(f"Failed: {e}", exc_info=True)
        return 1


if __name__ == "__main__":
    sys.exit(main())
