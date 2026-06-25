"""Normalized data model shared across parsers and exporters."""
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional


@dataclass(frozen=True)
class FeedEntry:
    """A single normalized feed item.

    Attributes:
        title: Human-readable headline.
        link: Canonical URL of the item.
        published: Parsed publication timestamp, when available.
        summary: Short description or excerpt.
        source: Catalog slug or domain the entry was aggregated from.
        tags: Free-form topic labels carried from the source.
    """

    title: str
    link: str
    published: Optional[datetime] = None
    summary: str = ""
    source: str = ""
    tags: List[str] = field(default_factory=list)

    def as_dict(self) -> dict:
        """Return a JSON-serializable representation of the entry."""
        return {
            "title": self.title,
            "link": self.link,
            "published": self.published.isoformat() if self.published else None,
            "summary": self.summary,
            "source": self.source,
            "tags": list(self.tags),
        }
