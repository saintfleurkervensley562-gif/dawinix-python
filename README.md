"""
README for the Dawinix Python SDK.
"""


[![PyPI version](https://img.shields.io/pypi/v/dawinix-python.svg?label=pypi%20(stable))](https://pypi.org/project/dawinix-python/)

# Dawinix Python SDK

Official Python library for the Dawinix API.

## Installation

```bash
pip install dawinix-sdk
```

## Quick Start

```python
from dawinix_sdk.build import Agent, Skill
import os

agent = Agent(
    api_key=os.getenv("DAWINIX_API_KEY"),
    model="dawinix-4",
    skills=[Skill.WEB_SEARCH],
)

result = agent.run(
    task="Find and summarize recent news about AI",
    mode="balanced",
)

print(result.output)
```

## Features

- 🤖 **Agent Building** - Build and run autonomous agents
- 🔍 **Multiple Skills** - Web search, code execution, file processing
- ⚡ **Async Support** - Async/await for non-blocking operations
- 🛡️ **Error Handling** - Built-in retry logic and error handling
- 📦 **Type Hints** - Full type hints for better IDE support
- 🧪 **Well Tested** - Comprehensive test suite

## Documentation

See [docs](./docs/) for full documentation.

[![PyPI version](https://img.shields.io/pypi/v/dawinix-python.svg)](https://pypi.org/project/dawinix-python/)

## Examples

Check the [examples/](./examples/) directory for more examples.

## License

MIT License
