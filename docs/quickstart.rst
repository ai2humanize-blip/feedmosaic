Quickstart
==========

Aggregate a vertical
--------------------

The :class:`~feedmosaic.aggregator.FeedAggregator` fetches every feed in a
catalog vertical, normalizes the items, removes duplicates and returns them
newest-first.

.. code-block:: python

   from feedmosaic import FeedAggregator

   agg = FeedAggregator(timeout=15)
   items = agg.collect("World & General News", limit=25)
   for e in items:
       print(f"{e.published:%Y-%m-%d}  {e.title}")
       print(f"    {e.link}  [{e.source}]")

Work with the catalog directly
------------------------------

.. code-block:: python

   from feedmosaic import catalog

   print(catalog.verticals())
   for pub in catalog.by_vertical("Technology & Digital Safety"):
       print(pub["name"], "->", pub["url"])

   feeds = catalog.feed_urls("Markets & Personal Finance")

Filter and export
-----------------

.. code-block:: python

   from feedmosaic import FeedAggregator, exporters
   from feedmosaic.filters import by_keyword

   agg = FeedAggregator()
   crypto = agg.collect("Cryptocurrency & Blockchain", limit=100)
   stablecoins = by_keyword(crypto, "stablecoin", "usdc", "treasuries")

   print(exporters.to_markdown(stablecoins))
   open("crypto.opml", "w").write(exporters.to_opml("Cryptocurrency & Blockchain"))
