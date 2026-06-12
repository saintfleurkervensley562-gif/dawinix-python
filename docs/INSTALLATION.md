"""
Installation guide.
"""

# Installation Guide

## Using pip

```bash
pip install dawinix-sdk
```

## From source

```bash
git clone https://github.com/dawinix/dawinix-python.git
cd dawinix-python
pip install -e .
```

## Development installation

```bash
pip install -e ".[dev]"
```

This installs development dependencies including pytest, black, and mypy.

## Verification

```python
import dawinix_sdk
print(dawinix_sdk.__version__)
```
