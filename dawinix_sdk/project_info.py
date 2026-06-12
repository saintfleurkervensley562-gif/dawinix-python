"""
Project structure documentation.
"""

import os
import json


class ProjectInfo:
    """Project information."""

    @staticmethod
    def get_structure() -> dict:
        """Get project structure."""
        return {
            "name": "dawinix-python-sdk",
            "version": "1.0.0",
            "description": "Official Python SDK for Dawinix API",
            "author": "Dawinix Inc.",
            "license": "MIT",
            "repository": "https://github.com/dawinix/dawinix-python",
        }

    @staticmethod
    def get_modules() -> dict:
        """Get available modules."""
        return {
            "client": "Main API client",
            "build": "Agent building and execution",
            "types": "Type definitions",
            "errors": "Error classes",
            "resources": "API resources",
            "utils": "Utility functions",
            "webhooks": "Webhook handling",
        }


def print_project_info():
    """Print project information."""
    info = ProjectInfo.get_structure()
    modules = ProjectInfo.get_modules()

    print(json.dumps({"project": info, "modules": modules}, indent=2))


if __name__ == "__main__":
    print_project_info()
