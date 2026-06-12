"""
Example: Async agent usage.
"""

import os
import asyncio
from dawinix_sdk.build import AsyncAgent, Skill


async def main():
    """Run async agent tasks."""
    agent = AsyncAgent(
        api_key=os.getenv("DAWINIX_API_KEY"),
        model="dawinix-4",
        skills=[Skill.WEB_SEARCH],
    )

    tasks = [
        "Find latest AI research papers",
        "Summarize quantum computing advances",
        "List top tech trends for 2024",
    ]

    results = await agent.batch(tasks)

    for i, result in enumerate(results):
        print(f"\nTask {i + 1}:")
        print(f"Output: {result.output}")


if __name__ == "__main__":
    asyncio.run(main())
