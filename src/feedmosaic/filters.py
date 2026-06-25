"""Composable post-processing filters for entry streams."""
from __future__ import annotations

from datetime import datetime
from typing import Iterable, List

from .models import FeedEntry


def dedupe(entries: Iterable[FeedEntry]) -> List[FeedEntry]:
    """Drop entries that repeat a canonical link, preserving order."""
    seen = set()
    out: List[FeedEntry] = []
    for e in entries:
        key = e.link or e.title
        if key in seen:
            continue
        seen.add(key)
        out.append(e)
    return out


def by_keyword(entries: Iterable[FeedEntry], *terms: str) -> List[FeedEntry]:
    """Keep entries whose title or summary contains any of *terms*."""
    needles = [t.lower() for t in terms if t]
    if not needles:
        return list(entries)
    out = []
    for e in entries:
        hay = (e.title + " " + e.summary).lower()
        if any(n in hay for n in needles):
            out.append(e)
    return out


def since(entries: Iterable[FeedEntry], cutoff: datetime) -> List[FeedEntry]:
    """Keep entries published on or after *cutoff* (undated entries dropped)."""
    return [e for e in entries if e.published and e.published >= cutoff]


def newest_first(entries: Iterable[FeedEntry]) -> List[FeedEntry]:
    """Sort entries by publication date descending; undated sink to the end."""
    return sorted(
        entries,
        key=lambda e: e.published or datetime.min.replace(tzinfo=None),
        reverse=True,
    )
