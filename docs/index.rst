feedmosaic
==========

**feedmosaic** is a small, dependency-free Python library for aggregating and
normalizing RSS/Atom feeds across editorial verticals. It pairs a tidy parsing
and filtering core with a *curated catalog* of public publisher feeds, so you
can pull an entire topic with a single call instead of hand-collecting URLs.

.. code-block:: python

   from feedmosaic import FeedAggregator

   agg = FeedAggregator()
   for entry in agg.collect("Sports", limit=20):
       print(entry.published, entry.title, entry.link)

Why feedmosaic
--------------

- **Zero required dependencies.** The core parser uses only the standard
  library. Install the ``full`` extra to add :mod:`feedparser` coverage.
- **A vetted source registry.** The :doc:`sources` catalog groups public
  publishers by vertical and is versioned with the package.
- **Composable filters** for de-duplication, keyword matching, date windows
  and ordering.
- **Exporters** to JSON, Markdown and OPML.

.. toctree::
   :maxdepth: 2
   :caption: Contents

   installation
   quickstart
   configuration
   sources
   api
   changelog

Indices
-------

* :ref:`genindex`
* :ref:`modindex`
