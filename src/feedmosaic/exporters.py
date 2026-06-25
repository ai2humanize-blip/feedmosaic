"""Serialize aggregated entries to JSON, Markdown, or OPML."""
from __future__ import annotations

import json
from typing import Iterable

from .catalog import PUBLISHERS
from .models import FeedEntry


def to_json(entries: Iterable[FeedEntry], indent: int = 2) -> str:
    """Render entries as a JSON array."""
    return json.dumps([e.as_dict() for e in entries], indent=indent, ensure_ascii=False)


def to_markdown(entries: Iterable[FeedEntry]) -> str:
    """Render entries as a Markdown bullet list of linked headlines."""
    lines = []
    for e in entries:
        when = f" — {e.published:%Y-%m-%d}" if e.published else ""
        lines.append(f"- [{e.title}]({e.link}){when}")
    return "\n".join(lines)


def to_opml(vertical: str | None = None) -> str:
    """Render the publisher catalog (optionally one vertical) as an OPML file."""
    pool = [p for p in PUBLISHERS if not vertical or str(p["vertical"]).lower() == vertical.lower()]
    body = "\n".join(
        f'    <outline text="{p["name"]}" type="rss" xmlUrl="{p["feed"]}" htmlUrl="{p["url"]}"/>'
        for p in pool
    )
    return (
        '<?xml version="1.0" encoding="UTF-8"?>\n<opml version="2.0">\n'
        "  <head><title>feedmosaic catalog</title></head>\n  <body>\n"
        f"{body}\n  </body>\n</opml>\n"
    )
