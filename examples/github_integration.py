"""
Example: GitHub API integration.
"""

import os
from dawinix_sdk.build import Agent, Skill


def main():
    """Use GitHub API with agent."""
    agent = Agent(
        api_key=os.getenv("DAWINIX_API_KEY"),
        model="dawinix-4",
        skills=[Skill.HTTP_REQUEST, Skill.SUMMARIZE],
    )

    result = agent.run(
        task="Fetch top repositories from GitHub and summarize trends",
        mode="balanced",
    )

    print(f"GitHub Analysis: {result.output}")


if __name__ == "__main__":
    main()
