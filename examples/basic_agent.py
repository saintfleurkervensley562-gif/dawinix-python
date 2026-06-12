"""
Example: Basic agent usage.
"""

import os
from dawinix_sdk.build import Agent, Skill


def main():
    """Run a simple agent task."""
    agent = Agent(
        api_key=os.getenv("DAWINIX_API_KEY"),
        model="dawinix-4",
        skills=[Skill.WEB_SEARCH, Skill.SUMMARIZE],
    )

    result = agent.run(
        task="Find and summarize recent news about AI in healthcare",
        mode="balanced",
    )

    print(f"Output: {result.output}")
    print(f"Tokens used: {result.usage.total_tokens}")
    print(f"Time taken: {result.elapsed_ms}ms")


if __name__ == "__main__":
    main()
