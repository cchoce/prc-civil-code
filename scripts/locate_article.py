#!/usr/bin/env python3
"""Locate an article in the Civil Code hierarchy; does not reproduce article text."""

from __future__ import annotations

import json
import sys
from pathlib import Path


def main() -> int:
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: locate_article.py <1-1260>", file=sys.stderr)
        return 2
    number = int(sys.argv[1])
    path = Path(__file__).resolve().parents[1] / "references" / "article-map.json"
    items = json.loads(path.read_text(encoding="utf-8"))
    item = next((row for row in items if row["article"] == number), None)
    if item is None:
        print(f"Article out of range: {number}", file=sys.stderr)
        return 1
    fields = [item.get("book"), item.get("subpart"), item.get("chapter"), item.get("section")]
    print(f"第{number}条：" + " → ".join(value for value in fields if value))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
