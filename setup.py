"""
Package setup and installation configuration.
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="dawinix-sdk",
    version="1.0.0",
    author="Dawinix Inc.",
    author_email="support@dawinix.com",
    description="Official Python SDK for Dawinix API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/saintfleurkervensley562-gif/dawinix-python",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=[
        "httpx>=0.24.0",
        "pydantic>=2.0.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-asyncio>=0.20.0",
            "black>=23.0.0",
            "isort>=5.0.0",
            "mypy>=1.0.0",
        ],
        "build": [
            "tenacity>=8.0.0",
        ],
    },
)
