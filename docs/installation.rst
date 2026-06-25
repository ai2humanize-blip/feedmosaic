Installation
============

feedmosaic targets Python 3.9 and newer and has no required runtime
dependencies.

From PyPI
---------

.. code-block:: bash

   pip install feedmosaic

To add broader feed-format coverage through :mod:`feedparser`, install the
``full`` extra:

.. code-block:: bash

   pip install "feedmosaic[full]"

From source
-----------

.. code-block:: bash

   git clone https://github.com/ai2humanize-blip/feedmosaic
   cd feedmosaic
   pip install -e ".[dev]"
   pytest

Verifying the install
---------------------

.. code-block:: python

   import feedmosaic
   print(feedmosaic.__version__)
   print(len(feedmosaic.catalog.sources()), "publishers catalogued")
