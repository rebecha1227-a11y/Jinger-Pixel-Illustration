#!/usr/bin/env python3
"""Author-only: register bundled Jinger as the confirmed local character.

Open-source users must create their own character (route A or B). Do not run this
to impersonate Jinger.
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

SKILL_ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    parser = argparse.ArgumentParser(description="Bootstrap author character Jinger (author only)")
    parser.add_argument(
        "--root",
        default=str(Path.cwd() / ".jinger-pixel-assets"),
        help="Runtime asset root, default: ./.jinger-pixel-assets",
    )
    parser.add_argument(
        "--i-am-the-author",
        action="store_true",
        help="Required flag. Confirms you are 静儿, not an open-source user borrowing Jinger's face.",
    )
    args = parser.parse_args()
    if not args.i_am_the_author:
        print(
            "error: 开源用户请用照片或自己的 IP 创建角色。作者静儿请加上 --i-am-the-author",
            file=sys.stderr,
        )
        return 2

    registry = SKILL_ROOT / "scripts" / "character_registry.py"
    sheet = SKILL_ROOT / "assets" / "character" / "jinger-turnaround.png"
    clean = SKILL_ROOT / "assets" / "character" / "jinger-pixel-fullbody.png"
    bust = SKILL_ROOT / "assets" / "character" / "jinger-pixel-bust.png"
    spec = SKILL_ROOT / "references" / "character-spec.md"
    for path in (registry, sheet, clean, bust, spec):
        if not path.is_file():
            print(f"error: missing {path}", file=sys.stderr)
            return 1

    root = Path(args.root).expanduser().resolve()
    root.mkdir(parents=True, exist_ok=True)

    register = subprocess.run(
        [
            sys.executable,
            str(registry),
            "register",
            "--root",
            str(root),
            "--slug",
            "jinger",
            "--name",
            "Jinger",
            "--sheet",
            str(sheet),
            "--clean-reference",
            str(clean),
            "--bust",
            str(bust),
            "--spec",
            str(spec),
        ],
        check=False,
    )
    if register.returncode != 0:
        return register.returncode

    confirm = subprocess.run(
        [
            sys.executable,
            str(registry),
            "confirm",
            "--root",
            str(root),
            "--slug",
            "jinger",
        ],
        check=False,
    )
    return confirm.returncode


if __name__ == "__main__":
    raise SystemExit(main())
