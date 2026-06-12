# GitHub Release Template

## Release Information

**Tag Version:** `v1.0.0`
**Release Title:** Dawinix Python SDK v1.0.0 - Initial Release

**Target Branch:** main
**Release Date:** June 12, 2026

---

## Release Description

```markdown
# 🎉 Dawinix Python SDK v1.0.0 - Initial Release

The official Python SDK for the Dawinix API is now available!

## ✨ Major Features

🤖 **Agent Building & Execution**
- Autonomous agent framework with configurable models
- Full async/await support with `AsyncAgent`
- 11+ available skills (Web Search, Code Execution, Vision, etc.)

📦 **Type-Safe API**
- Full type hints for better IDE support
- Pydantic-based schema validation
- Comprehensive error types

⚡ **Performance**
- Batch processing for parallel task execution
- Streaming support for real-time responses
- Efficient connection pooling

🛠️ **Developer Friendly**
- 13 production-ready examples
- Comprehensive documentation
- Full test coverage with pytest

## 🚀 Quick Start

\`\`\`bash
pip install dawinix-sdk
\`\`\`

\`\`\`python
from dawinix_sdk.build import Agent, Skill
import os

agent = Agent(
    api_key=os.getenv("DAWINIX_API_KEY"),
    model="dawinix-4",
    skills=[Skill.WEB_SEARCH],
)

result = agent.run("Find recent AI news and summarize")
print(result.output)
\`\`\`

## 📚 Documentation

- **[README](./README.md)** - Overview and quick start
- **[API Reference](./docs/API.md)** - Complete API documentation
- **[Installation Guide](./docs/INSTALLATION.md)** - Setup instructions
- **[Examples](./examples/)** - 13 production examples
- **[Contributing](./CONTRIBUTING.md)** - Contribution guidelines

## 📋 What's Included

- ✅ 60+ files organized into logical modules
- ✅ Synchronous and asynchronous clients
- ✅ Agent framework with 11+ skills
- ✅ Structured output validation
- ✅ Error handling with retry logic
- ✅ Webhook support
- ✅ Complete test suite
- ✅ Comprehensive documentation

## 🔧 Supported Python Versions

- Python 3.8+
- Python 3.9
- Python 3.10
- Python 3.11

## 📦 Models Supported

- **dawinix-4** - Full-featured model
- **dawinix-4-mini** - Speed-optimized
- **dawinix-3** - Previous generation

## 🔒 Security

- Environment variable support for API keys
- Webhook signature verification (HMAC-SHA256)
- Support for secrets managers (AWS, GCP, Vault)
- No sensitive data in error messages

## 🐛 Known Issues

- None at this time

## 🔮 Roadmap

Upcoming features:
- Plugin system for custom skills
- Caching layer
- OpenTelemetry integration
- Additional language SDKs
- Web dashboard

## 🙏 Acknowledgments

Built with inspiration from industry-leading SDKs like OpenAI's Python client.

---

**Happy building! 🚀**
```

---

## Release Metadata

**Release Type:** Production Release
**Pre-release:** No
**Draft:** No

**Attached Files:** None (binaries/packages available on PyPI)

**Labels:** 
- `release`
- `v1.0.0`
- `initial-release`
- `python-sdk`

---

## Publishing Instructions

### Option 1: GitHub Web Interface

1. Go to https://github.com/dawinix/dawinix-python/releases/new
2. **Choose a tag**: Create new tag `v1.0.0`
3. **Target**: Select `main` branch
4. **Release title**: `Dawinix Python SDK v1.0.0 - Initial Release`
5. **Release notes**: Copy content from this template
6. **Attach binaries**: Skip (PyPI packages)
7. **Pre-release**: Uncheck (this is production)
8. Click **Publish release**

### Option 2: GitHub CLI

```bash
# Create and push tag
git tag -a v1.0.0 -m "Dawinix Python SDK v1.0.0 - Initial Release"
git push origin v1.0.0

# Create release (requires gh CLI)
gh release create v1.0.0 \
  --title "Dawinix Python SDK v1.0.0 - Initial Release" \
  --notes-file RELEASE_NOTES.md \
  --target main
```

### Option 3: Git + Manual Upload

```bash
# Create tag locally
git tag -a v1.0.0 -m "Initial release"

# Push to remote
git push origin v1.0.0

# Then create release on GitHub web interface
```

---

## Post-Release Checklist

- [ ] Tag v1.0.0 created and pushed
- [ ] Release published on GitHub
- [ ] Package published to PyPI: `pip install dawinix-sdk`
- [ ] Documentation updated at https://dawinix.readthedocs.io
- [ ] Announcement posted to forums/social media
- [ ] Release notes documented in CHANGELOG.md
- [ ] Contributors acknowledged

---

## Version Bumping Strategy (for future releases)

- **v1.0.x** - Patch releases (bug fixes)
- **v1.x.0** - Minor releases (new features)
- **vX.0.0** - Major releases (breaking changes)

Example progression:
- v1.0.0 (current)
- v1.0.1 (bug fix)
- v1.1.0 (new features)
- v2.0.0 (breaking changes)

---

## Assets to Include (Optional)

- [ ] dawinix-sdk-1.0.0.tar.gz (source)
- [ ] dawinix-sdk-1.0.0.whl (wheel)
- [ ] dawinix-sdk-1.0.0-py3-none-any.whl

Note: These are automatically generated when building for PyPI.

Build command:
```bash
python -m build
```

Files located in `dist/` directory.

---

**Release prepared by:** Dawinix Team  
**Preparation date:** June 12, 2026  
**Review status:** Ready for publishing
