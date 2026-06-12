"""
Configuration: Makefile for development.
"""

.PHONY: install test lint format clean

install:
	pip install -r requirements.txt

test:
	pytest tests/

test-cov:
	pytest tests/ --cov=dawinix_sdk

lint:
	pylint dawinix_sdk/
	mypy dawinix_sdk/

format:
	black dawinix_sdk/ tests/ examples/
	isort dawinix_sdk/ tests/ examples/

clean:
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	rm -rf build/ dist/ *.egg-info htmlcov/ .pytest_cache/ .coverage

build:
	python -m build

publish:
	python -m twine upload dist/*
