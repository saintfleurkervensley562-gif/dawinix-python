"""
Example: Chat completion.
"""

import os
from dawinix_sdk import Dawinix


def main():
    """Create chat completion."""
    client = Dawinix(api_key=os.getenv("DAWINIX_API_KEY"))

    response = client.chats.create_completion(
        model="dawinix-4",
        messages=[
            {"role": "user", "content": "Explain quantum computing"},
        ],
        temperature=0.7,
    )

    print(f"Response: {response}")


if __name__ == "__main__":
    main()
