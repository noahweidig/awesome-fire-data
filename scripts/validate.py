#!/usr/bin/env python3
"""Validate data/*.yml against data/schema.json and cross-file rules."""
import json
import sys
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parent.parent


def load(path):
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def read_entries(validator, slugs, errors):
    """Return [(filename, entry)] and a map of id -> filename."""
    entries, ids = [], {}
    for f in sorted((ROOT / "data" / "datasets").glob("*.yml")):
        if f.stem not in slugs:
            errors.append(f"{f.name}: no theme with slug {f.stem!r} in data/themes.yml")
        data = load(f) or []
        for err in validator.iter_errors(data):
            path = "/".join(str(p) for p in err.absolute_path)
            errors.append(f"{f.name}: {path}: {err.message}")
        if not isinstance(data, list):
            continue
        for e in (e for e in data if isinstance(e, dict)):
            if e.get("id") in ids:
                errors.append(f"{f.name}: duplicate id {e['id']!r} (also in {ids[e['id']]})")
            ids[e.get("id")] = f.name
            entries.append((f.name, e))
    return entries, ids


def check_entry(name, e, tags, ids, errors):
    for t in e.get("tags", []):
        if t not in tags:
            errors.append(f"{name}: {e['id']}: tag {t!r} not in data/tag-vocab.yml")
    for r in e.get("related", []):
        if r not in ids:
            errors.append(f"{name}: {e['id']}: related id {r!r} does not exist")
        elif r == e["id"]:
            errors.append(f"{name}: {e['id']}: related lists itself")


def main():
    schema = json.loads((ROOT / "data" / "schema.json").read_text(encoding="utf-8"))
    validator = Draft202012Validator(schema)
    slugs = {t["slug"] for t in load(ROOT / "data" / "themes.yml")}
    vocab = load(ROOT / "data" / "tag-vocab.yml")
    tags = {t for v in vocab.values() for t in v["tags"]}
    errors = []
    entries, ids = read_entries(validator, slugs, errors)
    for name, e in entries:
        check_entry(name, e, tags, ids, errors)
    if errors:
        sys.exit("\n".join(errors))
    print(f"ok: {len(entries)} entries in {len(slugs)} themes")


if __name__ == "__main__":
    main()
