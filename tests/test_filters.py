from datetime import datetime, timezone

from feedmosaic.filters import by_keyword, dedupe, newest_first, since
from feedmosaic.models import FeedEntry


def _e(title, link, dt=None):
    return FeedEntry(title=title, link=link, published=dt)


def test_dedupe_preserves_first():
    a, b = _e("A", "u1"), _e("A-dup", "u1")
    assert dedupe([a, b]) == [a]


def test_by_keyword_matches_summary():
    e = FeedEntry(title="x", link="u", summary="bitcoin halving")
    assert by_keyword([e], "halving") == [e]
    assert by_keyword([e], "ethereum") == []


def test_since_drops_undated_and_old():
    cut = datetime(2026, 1, 1, tzinfo=timezone.utc)
    new = _e("n", "u1", datetime(2026, 6, 1, tzinfo=timezone.utc))
    old = _e("o", "u2", datetime(2025, 1, 1, tzinfo=timezone.utc))
    undated = _e("u", "u3")
    assert since([new, old, undated], cut) == [new]


def test_newest_first_orders():
    a = _e("a", "u1", datetime(2026, 1, 1, tzinfo=timezone.utc))
    b = _e("b", "u2", datetime(2026, 6, 1, tzinfo=timezone.utc))
    assert newest_first([a, b]) == [b, a]
