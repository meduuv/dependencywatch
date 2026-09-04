# DependencyWatch

> Compare dependency snapshots and make package changes easy to detect.

[![Python](https://img.shields.io/badge/python-3.10%2B-3776AB?style=flat-square)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-111111?style=flat-square)](LICENSE)

DependencyWatch is a lightweight Python utility for comparing two dependency snapshots and identifying what was **added, removed or changed**.

## Features

- Compare requirement snapshots
- Detect added dependencies
- Detect removed dependencies
- Detect changed dependency versions
- Small, deterministic API
- Zero runtime dependencies

## Installation

```bash
pip install dependencywatch
```

## Example

```python
from dependencywatch import diff

changes = diff(
    ["requests==2.31"],
    ["requests==2.32", "httpx==0.27"],
)

print(changes)
```

## Use cases

- Dependency checks in CI
- Release preparation
- Project auditing
- Automated update reports
- Supply-chain visibility

## Design

```text
snapshot A ─┐
            ├── compare ──→ added / removed / changed
snapshot B ─┘
```

DependencyWatch only analyzes supplied snapshots. It does not install packages or modify the environment.

## Development

```bash
python -m pytest
```

## License

MIT. See `LICENSE`.

## Author

Built by **Meduuv**.

[More projects](https://github.com/meduuv?tab=repositories) · [guns.lol/meduu](https://guns.lol/meduu)