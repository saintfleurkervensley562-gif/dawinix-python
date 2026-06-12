"""
Example: Code execution.
"""

import os
from dawinix_sdk.build import Agent, Skill


def main():
    """Execute code with agent."""
    agent = Agent(
        api_key=os.getenv("DAWINIX_API_KEY"),
        model="dawinix-4",
        skills=[Skill.CODE_EXECUTION],
    )

    result = agent.run(
        task="Write and execute Python code to calculate Fibonacci",
        mode="precise",
    )

    print(f"Execution result: {result.output}")


if __name__ == "__main__":
    main()
