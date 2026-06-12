"""
Example: File processing.
"""

import os
from dawinix_sdk.build import Agent, Skill


def main():
    """Process files with agent."""
    agent = Agent(
        api_key=os.getenv("DAWINIX_API_KEY"),
        model="dawinix-4",
        skills=[Skill.FILE_PROCESSING, Skill.SUMMARIZE],
    )

    result = agent.run(
        task="Analyze and summarize the attached PDF document",
        files=["./document.pdf"],
        mode="precise",
    )

    print(f"Analysis: {result.output}")


if __name__ == "__main__":
    main()
