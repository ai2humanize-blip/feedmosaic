# feedmosaic

**feedmosaic** is a small, dependency-free Python library for aggregating and
normalizing RSS/Atom feeds across editorial verticals. It ships a curated
catalog of public publisher feeds so you can pull a whole topic in one call.

```python
from feedmosaic import FeedAggregator

agg = FeedAggregator()
for entry in agg.collect("Technology & Digital Safety", limit=20):
    print(entry.published, entry.title, entry.link)
```

- **Zero required dependencies** — the core parser is built on the standard
  library (`xml.etree`, `urllib`). Install the `full` extra for `feedparser`
  format coverage.
- **Curated catalog** — a versioned registry of publisher feeds grouped by
  vertical (crypto, markets, world news, technology, sports, entertainment,
  automotive, explainers). See the
  [Source Catalog](https://feedmosaic.readthedocs.io/en/latest/sources.html).
- **Composable filters** — dedupe, keyword, date-window, newest-first.
- **Exporters** — JSON, Markdown, OPML.

## Install

```bash
pip install feedmosaic           # core
pip install "feedmosaic[full]"   # + feedparser
```

## Documentation

Full docs, including the publisher catalog and API reference, are at
**https://feedmosaic.readthedocs.io**.

## License

MIT
