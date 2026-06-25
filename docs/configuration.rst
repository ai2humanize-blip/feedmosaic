Configuration
=============

feedmosaic favours explicit arguments over global state, so there is very
little to configure.

Timeouts
--------

Pass ``timeout`` (seconds) when constructing the aggregator or when calling
:func:`feedmosaic.parser.fetch` directly:

.. code-block:: python

   from feedmosaic import FeedAggregator
   agg = FeedAggregator(timeout=30)

User agent
----------

Network requests identify themselves as ``feedmosaic/<version>``. Publishers
that wish to recognise or rate-limit the client can match on that token.

Resilience
----------

:meth:`~feedmosaic.aggregator.FeedAggregator.collect` is fault-tolerant: an
unreachable or malformed feed is skipped so that one bad source never aborts a
batch. Use the :mod:`~feedmosaic.filters` helpers to post-process the combined
stream (de-duplicate, keyword-match, restrict to a date window, reorder).

Extending the catalog
---------------------

The catalog in :mod:`feedmosaic.catalog` is ordinary package data. To track a
source that is not yet listed, add an entry following the existing schema and
open a pull request; see :doc:`sources` for the current registry.
