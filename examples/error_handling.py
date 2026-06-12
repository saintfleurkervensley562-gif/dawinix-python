"""
Example: Error handling and retries.
"""

import os
from dawinix_sdk.build import Agent, Skill
from dawinix_sdk.errors import RateLimitError, TimeoutError
from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type


def main():
    """Demonstrate error handling."""
    agent = Agent(api_key=os.getenv("DAWINIX_API_KEY"), model="dawinix-4")

    @retry(
        retry=retry_if_exception_type(RateLimitError),
        wait=wait_exponential(multiplier=1, min=4, max=60),
        stop=stop_after_attempt(5),
    )
    def run_with_retry(task: str):
        return agent.run(task=task, mode="precise")

    try:
        result = run_with_retry("Analyze this dataset")
        print(result.output)
    except RateLimitError:
        print("Rate limit exceeded after retries")
    except TimeoutError:
        print("Request timed out")


if __name__ == "__main__":
    main()
