"""
Contribution guidelines.
"""

# Contributing to Dawinix Python SDK

## Development Setup

1. Clone the repository
2. Create a virtual environment: `python -m venv venv`
3. Activate it: `source venv/bin/activate` (on Windows: `venv\\Scripts\\activate`)
4. Install dev dependencies: `pip install -r requirements.txt`

## Running Tests

```bash
pytest tests/
```

## Code Style

We use Black for formatting and isort for import sorting:

```bash
make format
```

## Linting

```bash
make lint
```

## Submitting Changes

1. Create a new branch
2. Make your changes
3. Run tests and linting
4. Submit a pull request
