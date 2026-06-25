from feedmosaic.parser import parse_string

RSS = """<?xml version='1.0'?>
<rss version='2.0'><channel><title>Demo</title>
<item><title>First</title><link>https://example.com/1</link>
<pubDate>Mon, 01 Jun 2026 09:00:00 +0000</pubDate>
<description>hello</description></item>
</channel></rss>"""


def test_parse_rss_item():
    entries = parse_string(RSS, source="demo")
    assert len(entries) == 1
    e = entries[0]
    assert e.title == "First"
    assert e.link == "https://example.com/1"
    assert e.source == "demo"
    assert e.published is not None
