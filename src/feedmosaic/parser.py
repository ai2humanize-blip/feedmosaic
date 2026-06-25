"""Minimal, dependency-free RSS 2.0 / Atom parser built on the stdlib.

If `feedparser` is installed (the ``full`` extra) it is used for broader format
coverage; otherwise the built-in :mod:`xml.etree` path handles the common cases.
"""
from __future__ import annotations

import urllib.request
from datetime import datetime
from email.utils import parsedate_to_datetime
from typing import List
from xml.etree import ElementTree as ET

from .models import FeedEntry

_ATOM = "{http://www.w3.org/2005/Atom}"
_UA = "feedmosaic/0.3 (+https://feedmosaic.readthedocs.io)"


def _parse_date(text: str):
    text = (text or "").strip()
    if not text:
        return None
    try:
        return parsedate_to_datetime(text)
    except (TypeError, ValueError):
        pass
    for fmt in ("%Y-%m-%dT%H:%M:%S%z", "%Y-%m-%dT%H:%M:%SZ", "%Y-%m-%d"):
        try:
            return datetime.strptime(text, fmt)
        except ValueError:
            continue
    return None


def parse_string(xml: str, source: str = "") -> List[FeedEntry]:
    """Parse a feed document already held in memory.

    Args:
        xml: Raw RSS or Atom markup.
        source: Catalog slug/domain to stamp onto each entry.

    Returns:
        A list of :class:`~feedmosaic.models.FeedEntry`.
    """
    root = ET.fromstring(xml)
    entries: List[FeedEntry] = []

    # RSS 2.0
    for item in root.iter("item"):
        title = (item.findtext("title") or "").strip()
        link = (item.findtext("link") or "").strip()
        entries.append(FeedEntry(
            title=title, link=link,
            published=_parse_date(item.findtext("pubDate") or ""),
            summary=(item.findtext("description") or "").strip(),
            source=source,
        ))
    if entries:
        return entries

    # Atom
    for item in root.iter(_ATOM + "entry"):
        title = (item.findtext(_ATOM + "title") or "").strip()
        link_el = item.find(_ATOM + "link")
        link = link_el.get("href", "") if link_el is not None else ""
        entries.append(FeedEntry(
            title=title, link=link,
            published=_parse_date(item.findtext(_ATOM + "updated") or ""),
            summary=(item.findtext(_ATOM + "summary") or "").strip(),
            source=source,
        ))
    return entries


def fetch(url: str, source: str = "", timeout: int = 20) -> List[FeedEntry]:
    """Fetch *url* over HTTP(S) and parse it into entries.

    Args:
        url: Feed endpoint.
        source: Catalog slug/domain to stamp onto each entry.
        timeout: Socket timeout in seconds.
    """
    req = urllib.request.Request(url, headers={"User-Agent": _UA})
    with urllib.request.urlopen(req, timeout=timeout) as resp:  # noqa: S310
        raw = resp.read().decode("utf-8", "replace")
    return parse_string(raw, source=source or url)
