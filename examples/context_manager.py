"""
Example: Using context manager.
"""

import os
from dawinix_sdk.context import dawinix_client


def main():
    """Use client with context manager."""
    with dawinix_client(os.getenv("DAWINIX_API_KEY")) as client:
        models = client.models.list()
        print(f"Available models: {len(models)}")


if __name__ == "__main__":
    main()
