#!/usr/bin/env python3
"""Check delivered PNG dimensions and naming for article/card folders."""

from __future__ import annotations

import argparse
import json
import struct
import sys
from pathlib import Path


def png_size(path: Path) -> tuple[int, int]:
    header = path.read_bytes()[:24]
    if header[:8] != b"\x89PNG\r\n\x1a\n" or header[12:16] != b"IHDR":
        raise ValueError(f"not a PNG: {path}")
    return struct.unpack(">II", header[16:24])


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate Jinger PNG delivery dimensions")
    parser.add_argument("directory")
    parser.add_argument("--kind", choices=("article", "card"), required=True)
    args = parser.parse_args()
    directory = Path(args.directory)
    images = sorted(directory.glob("*.png"))
    issues: list[str] = []
    if not images:
        issues.append("no PNG images found")
    for image in images:
        if not image.name[:2].isdigit() or " " in image.name:
            issues.append(f"invalid filename: {image.name}")
        try:
            width, height = png_size(image)
        except (OSError, ValueError) as error:
            issues.append(str(error))
            continue
        expected = 16 / 9 if args.kind == "article" else 3 / 4
        actual = width / height
        if abs(actual - expected) > 0.03:
            issues.append(f"wrong aspect ratio for {image.name}: {width}x{height}")
    result = {"ok": not issues, "kind": args.kind, "images": len(images), "issues": issues}
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if not issues else 1


if __name__ == "__main__":
    raise SystemExit(main())
