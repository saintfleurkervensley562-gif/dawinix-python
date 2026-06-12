"""
Example: Vision (image analysis).
"""

import os
from dawinix_sdk.build import Agent, Skill


def main():
    """Analyze images with vision."""
    agent = Agent(
        api_key=os.getenv("DAWINIX_API_KEY"),
        model="dawinix-4",
        skills=[Skill.VISION],
    )

    result = agent.run(
        task="Describe what you see in this image",
        files=["./image.jpg"],
        mode="balanced",
    )

    print(f"Description: {result.output}")


if __name__ == "__main__":
    main()
