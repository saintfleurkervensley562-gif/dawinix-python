"""
Example: Batch processing multiple tasks.
"""

import os
from dawinix_sdk.build import Agent, Skill


def main():
    """Process multiple tasks in batch."""
    agent = Agent(
        api_key=os.getenv("DAWINIX_API_KEY"),
        model="dawinix-4",
        skills=[Skill.SUMMARIZE],
    )

    tasks = [
        "Summarize the benefits of machine learning",
        "Explain neural networks in simple terms",
        "What are transformers in AI?",
    ]

    results = agent.batch(tasks, mode="balanced")

    for i, result in enumerate(results):
        print(f"\nTask {i + 1}:")
        print(f"Output: {result.output}")
        print(f"Tokens: {result.usage.total_tokens}")


if __name__ == "__main__":
    main()
