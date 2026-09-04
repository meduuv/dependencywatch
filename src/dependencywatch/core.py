import re

_NAME = re.compile(r"^([A-Za-z0-9][A-Za-z0-9_.-]*)")


def _map(items: list[str]) -> dict[str, str]:
    result = {}
    for item in items:
        text = item.strip()
        match = _NAME.match(text)
        if not match:
            raise ValueError(f"invalid requirement: {item!r}")
        result[match.group(1).lower()] = text
    return result


def diff(old: list[str], new: list[str]) -> dict[str, list[str]]:
    before, after = _map(old), _map(new)
    added = sorted(set(after) - set(before))
    removed = sorted(set(before) - set(after))
    changed = sorted(name for name in set(before) & set(after) if before[name] != after[name])
    return {"added": added, "removed": removed, "changed": changed}
