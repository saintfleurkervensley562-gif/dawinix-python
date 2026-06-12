"""
Example: Structured output with schemas.
"""

import os
from pydantic import BaseModel
from dawinix_sdk.build import Agent


class CompanyInfo(BaseModel):
    """Structured company information."""

    name: str
    industry: str
    employees: int
    founded_year: int


def main():
    """Extract structured data."""
    agent = Agent(api_key=os.getenv("DAWINIX_API_KEY"), model="dawinix-4")

    result = agent.run(
        task="Extract company info from Wikipedia article about Google",
        output_schema=CompanyInfo,
        mode="strict",
    )

    # Access parsed data
    if result.parsed:
        print(f"Company: {result.parsed.name}")
        print(f"Employees: {result.parsed.employees}")


if __name__ == "__main__":
    main()
