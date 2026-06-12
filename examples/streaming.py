"""
Example: Stream responses.
"""

import os
from dawinix_sdk.build import Agent, Skill


def main():
    """Stream agent responses."""
    agent = Agent(
        api_key=os.getenv("DAWINIX_API_KEY"),
        model="dawinix-4",
        skills=[Skill.WEB_SEARCH],
    )

    # Stream results
    for chunk in agent.stream("Explain AI in 5 steps"):
        print(chunk, end="", flush=True)


if __name__ == "__main__":
    main()
