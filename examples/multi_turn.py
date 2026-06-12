"""
Example: Multi-turn conversation.
"""

import os
from dawinix_sdk import Dawinix


def main():
    """Multi-turn conversation example."""
    client = Dawinix(api_key=os.getenv("DAWINIX_API_KEY"))

    messages = [
        {"role": "user", "content": "What is machine learning?"},
    ]

    # First turn
    response1 = client.chats.create_completion(
        model="dawinix-4",
        messages=messages,
    )

    assistant_message = response1["choices"][0]["message"]
    messages.append(assistant_message)

    # Second turn
    messages.append({"role": "user", "content": "Can you give an example?"})

    response2 = client.chats.create_completion(
        model="dawinix-4",
        messages=messages,
    )

    print(f"Final response: {response2}")


if __name__ == "__main__":
    main()
