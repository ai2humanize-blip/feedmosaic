"""High-level aggregation across many catalogued feeds."""
from __future__ import annotations

from typing import List, Optional

from . import catalog, filters, parser
from .models import FeedEntry


class FeedAggregator:
    """Fetch, normalize, dedupe and order entries across publisher feeds.

    Example:
        >>> agg = FeedAggregator()
        >>> items = agg.collect("Sports")          # doctest: +SKIP
        >>> headlines = [e.title for e in items]    # doctest: +SKIP
    """

    def __init__(self, timeout: int = 20) -> None:
        self.timeout = timeout

    def collect(self, vertical: Optional[str] = None, limit: int = 50) -> List[FeedEntry]:
        """Aggregate the newest, de-duplicated entries for a vertical.

        Args:
            vertical: A catalog vertical name, or ``None`` for every source.
            limit: Maximum number of entries to return.
        """
        pool = catalog.by_vertical(vertical) if vertical else catalog.sources()
        collected: List[FeedEntry] = []
        for pub in pool:
            try:
                collected.extend(parser.fetch(str(pub["feed"]), source=str(pub["slug"]),
                                               timeout=self.timeout))
            except Exception:  # noqa: BLE001 - a dead feed must not abort the batch
                continue
        return filters.newest_first(filters.dedupe(collected))[:limit]
