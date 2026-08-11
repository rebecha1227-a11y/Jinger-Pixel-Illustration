#!/usr/bin/env python3
"""Check the runtime Skill for broken references and stale route files."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

OLD_REFERENCES = {
    "ip-builder.md", "character-package.md", "concept-visual-language.md",
    "explainer-workflow.md", "card-content-analysis.md", "card-gold-standard.md",
    "card-layout-system.md", "card-style-system.md", "card-character-system.md",
    "card-templates.md", "style-dna.md", "prompt-templates.md", "qa-checklist.md",
}


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate Jinger runtime references")
    parser.add_argument("root", nargs="?", default=".")
    args = parser.parse_args()
    root = Path(args.root).resolve()
    issues: list[str] = []
    skill = root / "SKILL.md"
    if not skill.is_file():
        issues.append("missing SKILL.md")
    else:
        content = skill.read_text(encoding="utf-8")
        if not content.startswith("---\n") or "\nname:" not in content or "\ndescription:" not in content:
            issues.append("SKILL.md has incomplete frontmatter")

    active_files = [root / "SKILL.md", *sorted((root / "references").glob("*.md"))]
    for path in active_files:
        if not path.is_file():
            continue
        content = path.read_text(encoding="utf-8")
        for old in sorted(OLD_REFERENCES):
            if old in content:
                issues.append(f"stale reference {old} in {path.relative_to(root)}")

        for ref in re.findall(r"`([^`]+\.md)`", content):
            if "/" in ref or ref.startswith("."):
                candidate = root / ref
            else:
                candidate = root / "references" / ref
            if not candidate.is_file():
                issues.append(f"missing reference {ref} in {path.relative_to(root)}")

    for required in ("agents/openai.yaml", "scripts/character_registry.py", "scripts/install.mjs"):
        if not (root / required).is_file():
            issues.append(f"missing required file {required}")

    result = {"ok": not issues, "issues": issues}
    print(result)
    if issues:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
