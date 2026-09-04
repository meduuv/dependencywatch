# DependencyWatch

Detect dependency changes between two requirement snapshots.

## API

```python
from dependencywatch import diff

diff(["requests==2.31"], ["requests==2.32", "httpx==0.27"])
```

Returns added, removed, and changed dependency names.

## Development

`python -m pytest`

MIT licensed. Built by meduuv. https://guns.lol/meduu
