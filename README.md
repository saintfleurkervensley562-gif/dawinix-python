[![PyPI version](https://img.shields.io/pypi/v/dawinix-python.svg?label=PyPI)](https://pypi.org/project/dawinix-python/)
[![Python Version](https://img.shields.io/pypi/pyversions/dawinix-python.svg)](https://pypi.org/project/dawinix-python/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Build Status](https://github.com/saintfleurkervensley562-gif/dawinix-python/workflows/tests/badge.svg)](https://github.com/saintfleurkervensley562-gif/dawinix-python)
[![Code Coverage](https://img.shields.io/badge/coverage-95%25-brightgreen.svg)](https://github.com/saintfleurkervensley562-gif/dawinix-python)

# 🤖 Dawinix Python SDK

> The official Python SDK for the **Dawinix API** - Build, deploy, and scale autonomous AI agents with ease.

Welcome to the Dawinix Python SDK! This comprehensive library provides everything you need to integrate Dawinix's powerful AI agents into your Python applications. Whether you're building chatbots, data processors, or complex automation workflows, the Dawinix SDK makes it simple and intuitive.

**Version:** 1.0.0 | **Status:** Production Ready | **License:** MIT

---

## 📋 Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Configuration](#configuration)
- [Core Concepts](#core-concepts)
- [Usage Examples](#usage-examples)
- [API Reference](#api-reference)
- [Agent Skills](#agent-skills)
- [Error Handling](#error-handling)
- [Advanced Usage](#advanced-usage)
- [Best Practices](#best-practices)
- [Troubleshooting](#troubleshooting)
- [FAQ](#faq)
- [Contributing](#contributing)
- [Support](#support)
- [License](#license)

---

## ✨ Features

### 🤖 Agent Building & Execution
- **Autonomous Agents**: Build intelligent agents that can reason and take actions
- **Sync & Async APIs**: Both synchronous and asynchronous implementations available
- **Skill System**: 11+ pre-built skills (Web Search, Code Execution, Vision, etc.)
- **Configurable Models**: Support for dawinix-4, dawinix-4-mini, and dawinix-3

### 📦 Type-Safe & Validated
- **Full Type Hints**: Complete type annotations for IDE autocomplete and type checking
- **Pydantic Validation**: Schema-based output validation for structured results
- **Error Types**: Specific exception types for different error scenarios
- **Response Objects**: Strongly-typed response objects with computed properties

### ⚡ Performance & Scale
- **Batch Processing**: Execute multiple tasks in parallel efficiently
- **Streaming Support**: Real-time response streaming for long-running operations
- **Connection Pooling**: Automatic HTTP connection reuse
- **Async/Await**: Non-blocking I/O operations with asyncio support

### 🛡️ Production Ready
- **Retry Logic**: Built-in exponential backoff for transient failures
- **Rate Limit Handling**: Intelligent rate limit detection and retry
- **Timeout Management**: Configurable timeout with sensible defaults
- **Logging**: Comprehensive logging for debugging and monitoring

### 🔒 Security
- **Environment Variables**: API key management via environment variables
- **Webhook Verification**: HMAC-SHA256 signature verification
- **Secrets Management**: Integration with AWS Secrets Manager, Vault, GCP
- **No Sensitive Data in Logs**: Error messages sanitized automatically

### 📚 Developer Experience
- **Comprehensive Docs**: Detailed documentation with examples
- **13 Examples**: Production-ready example scripts
- **Full Test Suite**: 7 test modules with 15+ test cases
- **Type Stubs**: Complete type information for mypy/pyright

---

## 🚀 Installation

### Via PyPI (Recommended)

```bash
pip install dawinix-sdk
```

### Verify Installation

```python
import dawinix_sdk
print(dawinix_sdk.__version__)  # Output: 1.0.0
```

### Optional Dependencies

For additional features, install extras:

```bash
# For retry logic with tenacity
pip install dawinix-sdk[build]

# For development
pip install dawinix-sdk[dev]

# Everything
pip install dawinix-sdk[build,dev]
```

### From Source

```bash
git clone https://github.com/dawinix/dawinix-python.git
cd dawinix-python
pip install -e .

# With development dependencies
pip install -e ".[dev]"
```

### Python Version Support

- Python 3.8+
- Python 3.9
- Python 3.10
- Python 3.11

---

## ⚡ Quick Start

### Basic Agent Task

```python
from dawinix_sdk.build import Agent, Skill
import os

# Initialize an agent
agent = Agent(
    api_key=os.getenv("DAWINIX_API_KEY"),
    model="dawinix-4",
    skills=[Skill.WEB_SEARCH, Skill.SUMMARIZE],
)

# Run a task
result = agent.run(
    task="Find and summarize the latest AI breakthroughs",
    mode="balanced",
)

print(f"Output: {result.output}")
print(f"Tokens Used: {result.usage.total_tokens}")
print(f"Time Taken: {result.elapsed_ms}ms")
```

### Asynchronous Execution

```python
import asyncio
from dawinix_sdk.build import AsyncAgent, Skill

async def main():
    agent = AsyncAgent(
        api_key=os.getenv("DAWINIX_API_KEY"),
        model="dawinix-4",
        skills=[Skill.WEB_SEARCH],
    )
    
    result = await agent.run("What are the latest AI trends?")
    print(result.output)

asyncio.run(main())
```

### Batch Processing

```python
agent = Agent(
    api_key=os.getenv("DAWINIX_API_KEY"),
    skills=[Skill.SUMMARIZE],
)

tasks = [
    "Summarize machine learning",
    "Explain deep learning",
    "What are neural networks?",
]

# Process multiple tasks in parallel
results = agent.batch(tasks, mode="balanced")

for task, result in zip(tasks, results):
    print(f"Task: {task}")
    print(f"Result: {result.output}\n")
```

---

## 🔧 Configuration

### Environment Variables

```bash
# Required: Your Dawinix API key
export DAWINIX_API_KEY=daw-sk-your-key-here

# Optional: Custom API endpoint
export DAWINIX_API_BASE_URL=https://api.dawinix.com/v1

# Optional: Request timeout in seconds
export DAWINIX_API_TIMEOUT=30

# Optional: Enable debug logging
export DAWINIX_SDK_DEBUG=true
```

### Programmatic Configuration

```python
from dawinix_sdk import Dawinix
from dawinix_sdk.build import Agent

# Direct initialization
client = Dawinix(
    api_key="daw-sk-your-key",
    base_url="https://api.dawinix.com/v1",
    timeout=30.0,
)

# Agent with custom configuration
agent = Agent(
    api_key="daw-sk-your-key",
    model="dawinix-4",
    skills=[Skill.WEB_SEARCH],
    max_steps=15,
    timeout=120,
    temperature=0.7,
    top_p=0.9,
)
```

### Using Context Manager

```python
from dawinix_sdk.context import dawinix_client

with dawinix_client("daw-sk-your-key") as client:
    models = client.models.list()
    print(f"Available models: {len(models)}")
    
    response = client.chats.create_completion(
        model="dawinix-4",
        messages=[{"role": "user", "content": "Hello!"}],
    )
```

---

## 📖 Core Concepts

### Agents

An **Agent** is an autonomous system that can perceive its environment, make decisions, and take actions using available skills. Agents in Dawinix can:

- Accept natural language tasks
- Reason about the problem
- Use available skills to gather information
- Iterate and refine approaches
- Return structured results

```python
agent = Agent(
    api_key=api_key,
    model="dawinix-4",        # Model choice
    skills=[Skill.WEB_SEARCH], # Available skills
    max_steps=15,              # Max reasoning steps
    timeout=120,               # Timeout in seconds
    temperature=0.7,           # Creativity (0-1)
    top_p=0.9,                 # Diversity (0-1)
)
```

### Skills

**Skills** enable agents to interact with external systems and data sources. Available skills:

- **HTTP_REQUEST** - Make HTTP calls to APIs
- **WEB_SEARCH** - Search the internet
- **FILE_PROCESSING** - Parse documents (PDF, DOCX, etc.)
- **CODE_EXECUTION** - Run Python code safely
- **SUMMARIZE** - Summarize long texts
- **EMAIL** - Send and receive emails
- **SLACK** - Slack integration
- **GITHUB** - GitHub API access
- **DATABASE** - Query databases
- **IMAGE_GENERATION** - Generate images
- **VISION** - Analyze images

### Modes

**Execution modes** control how the agent operates:

- **balanced** (default) - Good balance of speed and quality
- **precise** - Prioritizes accuracy over speed
- **speed** - Optimized for fast responses
- **strict** - Validates output against schema

---

## 💡 Usage Examples

### Web Search and Summarization

```python
from dawinix_sdk.build import Agent, Skill

agent = Agent(
    api_key=os.getenv("DAWINIX_API_KEY"),
    model="dawinix-4",
    skills=[Skill.WEB_SEARCH, Skill.SUMMARIZE],
)

result = agent.run(
    task="Find information about renewable energy trends and summarize in 3 points",
    mode="precise",
)

print(result.output)
```

### Data Extraction with Structured Output

```python
from pydantic import BaseModel
from dawinix_sdk.build import Agent

class Article(BaseModel):
    title: str
    author: str
    date: str
    summary: str

agent = Agent(api_key=os.getenv("DAWINIX_API_KEY"))

result = agent.run(
    task="Extract article metadata from the webpage",
    output_schema=Article,
    mode="strict",
)

# Access structured data
article = result.parsed
print(f"Title: {article.title}")
print(f"Author: {article.author}")
```

### File Processing

```python
from dawinix_sdk.build import Agent, Skill

agent = Agent(
    api_key=os.getenv("DAWINIX_API_KEY"),
    skills=[Skill.FILE_PROCESSING, Skill.SUMMARIZE],
)

result = agent.run(
    task="Analyze the attached PDF and extract key insights",
    files=["report.pdf"],
    mode="precise",
)

print(result.output)
```

### Code Execution

```python
from dawinix_sdk.build import Agent, Skill

agent = Agent(
    api_key=os.getenv("DAWINIX_API_KEY"),
    skills=[Skill.CODE_EXECUTION],
)

result = agent.run(
    task="Write and execute Python code to calculate Fibonacci numbers up to 1000",
    mode="balanced",
)

print(result.output)
```

### Image Analysis (Vision)

```python
from dawinix_sdk.build import Agent, Skill

agent = Agent(
    api_key=os.getenv("DAWINIX_API_KEY"),
    skills=[Skill.VISION],
)

result = agent.run(
    task="Analyze this image and describe what you see",
    files=["image.jpg"],
    mode="balanced",
)

print(result.output)
```

### Image Generation

```python
from dawinix_sdk.build import Agent, Skill

agent = Agent(
    api_key=os.getenv("DAWINIX_API_KEY"),
    skills=[Skill.IMAGE_GENERATION],
)

result = agent.run(
    task="Generate a beautiful landscape with mountains and a lake at sunset",
    mode="balanced",
)

print(f"Generated image: {result.output}")
```

### Cron Job for Scheduled Tasks

```python
#!/usr/bin/env python3
import os
import sys
import logging
from datetime import datetime, timedelta
from dawinix_sdk.build import Agent, Skill

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

def daily_digest():
    agent = Agent(
        api_key=os.getenv("DAWINIX_API_KEY"),
        model="dawinix-4",
        skills=[Skill.HTTP_REQUEST, Skill.SUMMARIZE],
        timeout=120,
    )
    
    yesterday = (datetime.utcnow() - timedelta(days=1)).strftime("%Y-%m-%d")
    
    result = agent.run(
        task=f"Generate daily digest for {yesterday}",
        mode="precise",
    )
    
    log.info(f"Generated in {result.elapsed_ms}ms")
    print(result.output)

if __name__ == "__main__":
    daily_digest()
```

---

## 🔌 API Reference

### Agent Class

```python
class Agent:
    def __init__(
        self,
        api_key: Optional[str] = None,
        model: str = "dawinix-4",
        skills: Optional[List[SkillType]] = None,
        max_steps: int = 15,
        timeout: int = 120,
        temperature: float = 0.7,
        top_p: float = 0.9,
    ) -> None: ...

    def run(
        self,
        task: str,
        mode: AgentMode = AgentMode.BALANCED,
        output_schema: Optional[BaseModel] = None,
        files: Optional[List[str]] = None,
    ) -> AgentResult: ...

    def batch(
        self,
        tasks: List[str],
        mode: AgentMode = AgentMode.BALANCED,
    ) -> List[AgentResult]: ...

    def stream(
        self,
        task: str,
        mode: AgentMode = AgentMode.BALANCED,
    ) -> Generator[str, None, None]: ...
```

### Dawinix Client

```python
class Dawinix:
    def __init__(
        self,
        api_key: Optional[str] = None,
        base_url: str = "https://api.dawinix.com/v1",
        timeout: float = 30.0,
    ) -> None: ...

    # Properties
    models: ModelsResource
    chats: ChatsResource
    agents: AgentsResource

    def close(self) -> None: ...
    def __enter__(self) -> "Dawinix": ...
    def __exit__(self, *args) -> None: ...
```

### Response Object

```python
@dataclass
class AgentResult:
    output: str                          # Task output
    status: str                          # Completion status
    elapsed_ms: int                      # Execution time
    usage: UsageInfo                     # Token usage
    raw_json: Optional[str] = None       # Raw JSON response
    parsed: Optional[Any] = None         # Parsed schema
    partial_output: Optional[str] = None # Partial output on error

@dataclass
class UsageInfo:
    total_tokens: int       # Total tokens used
    prompt_tokens: int      # Tokens in prompt
    completion_tokens: int  # Tokens in output
    cached_tokens: int = 0  # Cached tokens
```

---

## 🎯 Agent Skills

### Web Search

```python
agent = Agent(
    skills=[Skill.WEB_SEARCH],
)

result = agent.run(
    task="Search for Python 3.12 features",
)
```

### HTTP Requests

```python
agent = Agent(
    skills=[Skill.HTTP_REQUEST],
)

result = agent.run(
    task="Fetch data from https://api.example.com/data",
)
```

### File Processing

```python
agent = Agent(
    skills=[Skill.FILE_PROCESSING],
)

result = agent.run(
    task="Extract tables from this PDF",
    files=["data.pdf"],
)
```

### Code Execution

```python
agent = Agent(
    skills=[Skill.CODE_EXECUTION],
)

result = agent.run(
    task="Write Python code to analyze a dataset",
)
```

---

## ⚠️ Error Handling

### Exception Types

```python
from dawinix_sdk.errors import (
    DawinixError,           # Base exception
    APIError,               # API errors
    RateLimitError,         # Rate limit exceeded
    TimeoutError,           # Request timeout
    ContextLengthError,     # Input too long
    AgentLoopError,         # Max steps exceeded
    ValidationError,        # Input validation
    AuthenticationError,    # Auth failed
    PermissionError,        # No permission
    NotFoundError,          # Resource not found
)
```

### Error Handling Pattern

```python
from dawinix_sdk.build import Agent
from dawinix_sdk.errors import (
    RateLimitError,
    TimeoutError,
    ContextLengthError,
)

agent = Agent(api_key=os.getenv("DAWINIX_API_KEY"))

try:
    result = agent.run("Process large dataset")
    print(result.output)

except ContextLengthError as e:
    print(f"Input too long: {e.current_length}/{e.max_length}")
    # Split the task and retry
    
except RateLimitError as e:
    print(f"Rate limited. Retry after {e.retry_after}s")
    # Implement exponential backoff
    
except TimeoutError:
    print("Request timed out")
    # Increase timeout or reduce complexity

except Exception as e:
    print(f"Unexpected error: {e}")
```

### Retry with Exponential Backoff

```python
from tenacity import (
    retry,
    stop_after_attempt,
    wait_exponential,
    retry_if_exception_type,
)
from dawinix_sdk.errors import RateLimitError

@retry(
    retry=retry_if_exception_type(RateLimitError),
    wait=wait_exponential(multiplier=1, min=4, max=60),
    stop=stop_after_attempt(5),
)
def run_with_retry(agent, task):
    return agent.run(task)

result = run_with_retry(agent, "Your task here")
```

---

## 🚀 Advanced Usage

### Streaming Responses

```python
agent = Agent(api_key=os.getenv("DAWINIX_API_KEY"))

for chunk in agent.stream("Explain quantum computing"):
    print(chunk, end="", flush=True)
```

### Custom Configuration

```python
from dawinix_sdk.config import Config
from dawinix_sdk import Dawinix

config = Config(
    api_key=os.getenv("DAWINIX_API_KEY"),
    base_url="https://api.dawinix.com/v1",
    timeout=60.0,
    max_retries=3,
    enable_logging=True,
)

config.validate()  # Validate configuration

client = Dawinix(
    api_key=config.api_key,
    base_url=config.base_url,
    timeout=config.timeout,
)
```

### Pagination

```python
from dawinix_sdk.pagination import Paginator

# Example with API resources
models = client.models.list()

paginator = Paginator(
    items=models,
    page=1,
    page_size=10,
    total=len(models),
)

if paginator.has_next:
    print(f"Page {paginator.page} of {paginator.total_pages}")
```

---

## 📋 Best Practices

### 1. Security

- Never hardcode API keys
- Use environment variables or secrets managers
- Rotate API keys regularly
- Use HTTPS for all connections

```python
import os
from dawinix_sdk import Dawinix

# ✅ Good
api_key = os.getenv("DAWINIX_API_KEY")
client = Dawinix(api_key=api_key)

# ❌ Bad
client = Dawinix(api_key="daw-sk-1234567890")
```

### 2. Error Handling

- Always catch specific exceptions
- Implement retry logic for transient failures
- Log errors for debugging
- Provide meaningful error messages

```python
try:
    result = agent.run(task)
except RateLimitError:
    # Handle rate limiting
    pass
except TimeoutError:
    # Handle timeout
    pass
except Exception as e:
    # Log unexpected errors
    logger.error(f"Unexpected error: {e}")
```

### 3. Performance

- Use async for I/O-bound operations
- Batch multiple tasks for efficiency
- Configure appropriate timeouts
- Monitor token usage

```python
# ✅ Efficient batching
results = agent.batch(tasks, mode="balanced")

# Use async for non-blocking I/O
async_agent = AsyncAgent(api_key=api_key)
await async_agent.run(task)
```

### 4. Resource Management

- Close clients when done
- Use context managers
- Clean up file handles
- Monitor memory usage

```python
# ✅ Good
with dawinix_client(api_key) as client:
    result = client.agents.run(task)

# ✅ Also good
client = Dawinix(api_key=api_key)
try:
    result = client.agents.run(task)
finally:
    client.close()
```

---

## 🔧 Troubleshooting

### Authentication Error

```
AuthenticationError: Invalid API key
```

**Solution:**
- Verify API key is set: `echo $DAWINIX_API_KEY`
- Check key format: `daw-sk-...`
- Regenerate key if needed

### Rate Limit Error

```
RateLimitError: Too many requests
```

**Solution:**
- Implement exponential backoff
- Reduce request frequency
- Use batch processing for efficiency

### Timeout Error

```
TimeoutError: Request exceeded timeout
```

**Solution:**
- Increase timeout value
- Break task into smaller subtasks
- Use streaming for long operations

### Context Length Error

```
ContextLengthError: Input exceeds context window
```

**Solution:**
- Reduce input size
- Split task into multiple parts
- Use summarization to compress input

---

## ❓ FAQ

**Q: Can I use this SDK in production?**
A: Yes! Version 1.0.0 is production-ready with full testing and documentation.

**Q: Which Python versions are supported?**
A: Python 3.8 and later (3.8, 3.9, 3.10, 3.11).

**Q: How do I handle rate limiting?**
A: Use the retry decorator with exponential backoff or implement custom retry logic.

**Q: Can I use multiple agents simultaneously?**
A: Yes, use AsyncAgent for concurrent execution or AgentPool for managing multiple agents.

**Q: How do I stream large responses?**
A: Use `agent.stream()` instead of `agent.run()` for real-time streaming.

**Q: What are the costs?**
A: Pricing depends on usage. Check dawinix.com for current pricing.

**Q: Is there a CLI tool?**
A: Yes, the `dawinix` CLI is available for command-line usage.

**Q: How do I contribute?**
A: See CONTRIBUTING.md for guidelines.

---

## 🤝 Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for details.

### Development Setup

```bash
git clone https://github.com/dawinix/dawinix-python.git
cd dawinix-python
pip install -e ".[dev]"
pytest
```

---

## 📞 Support

- 📖 **Documentation**: https://dawinix.readthedocs.io
- 💬 **Discussions**: https://github.com/dawinix/dawinix-python/discussions
- 🐛 **Issues**: https://github.com/dawinix/dawinix-python/issues
- 📧 **Email**: support@dawinix.com
- 🌐 **Website**: https://dawinix.com

---

## 📄 License

MIT License - See [LICENSE](LICENSE) for details.

---

**Built with ❤️ by the Dawinix Team**

*Ready to build amazing AI applications? Let's get started!*
