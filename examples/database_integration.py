"""
Example: Database integration.
"""

import os
from dawinix_sdk.build import Agent, Skill


def main():
    """Use database skill with agent."""
    agent = Agent(
        api_key=os.getenv("DAWINIX_API_KEY"),
        model="dawinix-4",
        skills=[Skill.DATABASE],
    )

    result = agent.run(
        task="Query the database and generate a report",
        mode="precise",
    )

    print(f"Database Report: {result.output}")


if __name__ == "__main__":
    main()
