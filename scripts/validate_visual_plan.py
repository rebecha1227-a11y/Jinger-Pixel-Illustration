#!/usr/bin/env python3
"""Validate a JSON visual plan without third-party dependencies."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

REQUIRED = ("asset_id", "source_anchor", "communication_job", "visual_grammar")
GRAMMARS = {"scene", "process", "comparison", "timeline", "evidence", "data", "checklist", "conclusion"}


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate a Jinger visual plan JSON file")
    parser.add_argument("path")
    args = parser.parse_args()
    path = Path(args.path)
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 1
    if not isinstance(value, dict):
        print("error: visual plan must be a JSON object", file=sys.stderr)
        return 1
    missing = [key for key in REQUIRED if not value.get(key)]
    grammar = value.get("visual_grammar")
    if grammar not in GRAMMARS:
        missing.append(f"visual_grammar ({', '.join(sorted(GRAMMARS))})")
    if not isinstance(value.get("exact_text", []), list):
        missing.append("exact_text must be an array")
    if not isinstance(value.get("essential_props", []), list):
        missing.append("essential_props must be an array")
    if missing:
        print(json.dumps({"ok": False, "issues": missing}, ensure_ascii=False, indent=2))
        return 1
    print(json.dumps({"ok": True, "asset_id": value["asset_id"]}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
