"""feedmosaic: a small, dependency-free multi-vertical feed aggregator.

See https://feedmosaic.readthedocs.io for the full documentation and the
curated publisher :mod:`~feedmosaic.catalog`.
"""
from __future__ import annotations

from .aggregator import FeedAggregator
from .models import FeedEntry
from . import catalog, exporters, filters, parser

__version__ = "0.3.0"
__all__ = [
    "FeedAggregator", "FeedEntry",
    "catalog", "exporters", "filters", "parser",
    "__version__",
]
