"""
Documentation and API reference.
"""

# Dawinix SDK Documentation

## Installation

```bash
pip install dawinix-sdk
```

## Getting Started

### Basic Usage

```python
from dawinix_sdk.build import Agent, Skill
import os

agent = Agent(
    api_key=os.getenv("DAWINIX_API_KEY"),
    model="dawinix-4",
    skills=[Skill.WEB_SEARCH, Skill.SUMMARIZE],
)

result = agent.run(
    task="Find recent news about AI",
    mode="balanced",
)

print(result.output)
```

## API Reference

### Agent

- `run(task, mode, output_schema, files)` - Execute a task
- `batch(tasks, mode)` - Execute multiple tasks
- `stream(task, mode)` - Stream execution

### Client

- `models.list()` - List available models
- `models.retrieve(model_id)` - Get model info
- `chats.create_completion()` - Create chat completion
- `agents.run()` - Run agent task

## Examples

See `examples/` directory for more examples.
