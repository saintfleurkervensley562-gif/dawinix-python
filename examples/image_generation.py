"""
Example: Image generation.
"""

import os
from dawinix_sdk.build import Agent, Skill


def main():
    """Generate images with agent."""
    agent = Agent(
        api_key=os.getenv("DAWINIX_API_KEY"),
        model="dawinix-4",
        skills=[Skill.IMAGE_GENERATION],
    )

    result = agent.run(
        task="Generate a beautiful landscape painting of mountains and lakes",
        mode="balanced",
    )

    print(f"Generated image: {result.output}")


if __name__ == "__main__":
    main()
