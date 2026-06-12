# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2026-06-12

### Added

#### Core Features
- Initial release of Dawinix Python SDK
- Synchronous and asynchronous API clients
- Agent building and execution framework
- 11+ configurable agent skills
- Batch processing and streaming support
- Structured output with Pydantic validation
- Comprehensive error handling

#### API Resources
- Models resource (list, retrieve)
- Chats resource (completions, streaming)
- Agents resource (run, batch)

#### Developer Features
- Full type hints for IDE support
- Logging utilities and decorators
- Retry mechanism with exponential backoff
- Webhook signature verification
- Context managers for resource management
- Pagination utilities

#### Documentation
- Comprehensive README with examples
- API reference documentation
- Installation guide
- Contribution guidelines
- 13 production-ready examples

#### Testing
- 7 test modules with pytest
- Integration test framework
- Mock utilities for testing

### Components

- **dawinix_sdk/**: Main package (19 core modules)
- **dawinix_sdk/types/**: Type definitions (4 modules)
- **dawinix_sdk/build/**: Agent framework
- **dawinix_sdk/api/**: HTTP clients (sync/async)
- **dawinix_sdk/resources/**: API resources
- **dawinix_sdk/utils/**: Utilities (validators, retries, logging)
- **dawinix_sdk/webhooks/**: Webhook handling
- **examples/**: 13 examples covering common use cases
- **tests/**: Comprehensive test suite
- **docs/**: Detailed documentation

### Dependencies

- httpx >= 0.24.0
- pydantic >= 2.0.0
- tenacity >= 8.0.0 (optional, for build extra)

### Python Support

- Python 3.8+
- Python 3.9
- Python 3.10
- Python 3.11

---

## Planned for Future Releases

### [1.1.0] - Upcoming
- [ ] Plugin system for custom skills
- [ ] Enhanced caching layer
- [ ] Performance optimizations
- [ ] Additional model support
- [ ] Extended webhook features

### [1.2.0] - Planned
- [ ] OpenTelemetry integration
- [ ] Advanced monitoring
- [ ] Custom model fine-tuning support
- [ ] Batch file processing

### [2.0.0] - Major Version
- [ ] Additional language SDKs
- [ ] Web dashboard
- [ ] CLI improvements
- [ ] Breaking changes (TBD)

---

## Migration Guide

This is the first release, so no migration needed. Start fresh!

```bash
pip install dawinix-sdk
```

## Installation

```bash
pip install dawinix-sdk
```

## Getting Started

See [README.md](./README.md) and [examples/](./examples/) for quick start guides.

## Support

- Documentation: [docs/](./docs/)
- Issues: GitHub Issues
- Contributing: [CONTRIBUTING.md](./CONTRIBUTING.md)
- License: [LICENSE](./LICENSE)
