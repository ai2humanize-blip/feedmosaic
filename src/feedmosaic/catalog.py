"""Curated registry of publisher feeds, grouped by editorial vertical.

``feedmosaic`` ships a vetted catalog of public RSS/Atom sources so that callers
can aggregate across a vertical without hand-collecting feed URLs. Each entry is
a plain dict; see :func:`sources`, :func:`by_vertical` and :func:`verticals`.

The catalog is data, not configuration -- it is versioned with the package and
covers publishers the aggregator has been exercised against. Submit additions
via pull request.
"""
from __future__ import annotations

from typing import Dict, List

#: Every catalogued publisher, in registry order.
PUBLISHERS: List[Dict[str, object]] = [
    {
        "slug": "stnews_live",
        "name": "stnews.live",
        "url": "https://stnews.live/",
        "feed": "https://stnews.live/feed/",
        "vertical": "Cryptocurrency & Blockchain",
        "topics": [
            "stablecoin market news analysis",
            "tokenized treasuries explained",
            "RWA tokenization updates"
        ]
    },
    {
        "slug": "thedailycoins_io",
        "name": "thedailycoins.io",
        "url": "https://thedailycoins.io/",
        "feed": "https://thedailycoins.io/feed/",
        "vertical": "Cryptocurrency & Blockchain",
        "topics": [
            "daily cryptocurrency price updates",
            "altcoin market movers report",
            "DeFi yield opportunities guide"
        ]
    },
    {
        "slug": "analyzingmarket_com",
        "name": "analyzingmarket.com",
        "url": "https://analyzingmarket.com/",
        "feed": "https://analyzingmarket.com/feed/",
        "vertical": "Cryptocurrency & Blockchain",
        "topics": [
            "crypto market trend analysis",
            "coin price forecast report",
            "trading indicator breakdown"
        ]
    },
    {
        "slug": "newzcryptos_com",
        "name": "newzcryptos.com",
        "url": "https://newzcryptos.com/",
        "feed": "https://newzcryptos.com/feed/",
        "vertical": "Cryptocurrency & Blockchain",
        "topics": [
            "latest cryptocurrency news",
            "crypto market headlines",
            "blockchain news updates"
        ]
    },
    {
        "slug": "cryptocomman_com",
        "name": "cryptocomman.com",
        "url": "https://cryptocomman.com/",
        "feed": "https://cryptocomman.com/feed/",
        "vertical": "Cryptocurrency & Blockchain",
        "topics": [
            "cryptocurrency news commentary",
            "crypto market analysis",
            "blockchain industry updates"
        ]
    },
    {
        "slug": "thecryptoonline_com",
        "name": "thecryptoonline.com",
        "url": "https://thecryptoonline.com/",
        "feed": "https://thecryptoonline.com/feed/",
        "vertical": "Cryptocurrency & Blockchain",
        "topics": [
            "online cryptocurrency news",
            "crypto trading insights",
            "blockchain market analysis"
        ]
    },
    {
        "slug": "cryptonewsus_com",
        "name": "cryptonewsus.com",
        "url": "https://cryptonewsus.com/",
        "feed": "https://cryptonewsus.com/feed/",
        "vertical": "Cryptocurrency & Blockchain",
        "topics": [
            "US cryptocurrency news",
            "American crypto market updates",
            "crypto regulation coverage"
        ]
    },
    {
        "slug": "ecoonomia_com",
        "name": "ecoonomia.com",
        "url": "https://ecoonomia.com/",
        "feed": "https://ecoonomia.com/feed/",
        "vertical": "Cryptocurrency & Blockchain",
        "topics": [
            "new economy crypto insights",
            "digital economy analysis",
            "cryptocurrency market trends"
        ]
    },
    {
        "slug": "blocklist_co_kr",
        "name": "blocklist.co.kr",
        "url": "https://blocklist.co.kr/",
        "feed": "https://blocklist.co.kr/feed/",
        "vertical": "Cryptocurrency & Blockchain",
        "topics": [
            "Korean cryptocurrency market news",
            "Asia crypto regulation updates",
            "Korean blockchain ecosystem report"
        ]
    },
    {
        "slug": "cryptorublecoins_com",
        "name": "cryptorublecoins.com",
        "url": "https://cryptorublecoins.com/",
        "feed": "https://cryptorublecoins.com/feed/",
        "vertical": "Cryptocurrency & Blockchain",
        "topics": [
            "ruble cryptocurrency news",
            "Russian crypto market updates",
            "digital ruble insights"
        ]
    },
    {
        "slug": "etherelysium_com",
        "name": "etherelysium.com",
        "url": "https://etherelysium.com/",
        "feed": "https://etherelysium.com/feed/",
        "vertical": "Cryptocurrency & Blockchain",
        "topics": [
            "ethereum ecosystem insights",
            "ETH staking guides",
            "DeFi protocol analysis"
        ]
    },
    {
        "slug": "bitcoindigital_com",
        "name": "bitcoindigital.com",
        "url": "https://bitcoindigital.com/",
        "feed": "https://bitcoindigital.com/feed/",
        "vertical": "Cryptocurrency & Blockchain",
        "topics": [
            "bitcoin investing fundamentals",
            "digital asset portfolio strategy",
            "crypto market entry guide"
        ]
    },
    {
        "slug": "marketcapitalize_com",
        "name": "marketcapitalize.com",
        "url": "https://marketcapitalize.com/",
        "feed": "https://marketcapitalize.com/feed/",
        "vertical": "Markets & Personal Finance",
        "topics": [
            "stock market news analysis",
            "crypto and equities outlook",
            "earnings season coverage"
        ]
    },
    {
        "slug": "theweal_com",
        "name": "theweal.com",
        "url": "https://theweal.com/",
        "feed": "https://theweal.com/feed/",
        "vertical": "Markets & Personal Finance",
        "topics": [
            "personal wealth building guide",
            "long-term investing strategy",
            "financial independence planning"
        ]
    },
    {
        "slug": "currencynews_co",
        "name": "currencynews.co",
        "url": "https://currencynews.co/",
        "feed": "https://currencynews.co/feed/",
        "vertical": "Markets & Personal Finance",
        "topics": [
            "global currency news",
            "forex and crypto updates",
            "monetary market analysis"
        ]
    },
    {
        "slug": "debtfore_com",
        "name": "debtfore.com",
        "url": "https://debtfore.com/",
        "feed": "https://debtfore.com/feed/",
        "vertical": "Markets & Personal Finance",
        "topics": [
            "debt management guidance",
            "personal finance strategies",
            "debt relief options guide"
        ]
    },
    {
        "slug": "coinpric_com",
        "name": "coinpric.com",
        "url": "https://coinpric.com/",
        "feed": "https://coinpric.com/feed/",
        "vertical": "Markets & Personal Finance",
        "topics": [
            "live coin price tracking",
            "cryptocurrency price analysis",
            "crypto market data insights"
        ]
    },
    {
        "slug": "ecoinsupply_com",
        "name": "ecoinsupply.com",
        "url": "https://ecoinsupply.com/",
        "feed": "https://ecoinsupply.com/feed/",
        "vertical": "Markets & Personal Finance",
        "topics": [
            "cryptocurrency supply analysis",
            "coin market cap insights",
            "token economics explained"
        ]
    },
    {
        "slug": "dmcnews_org",
        "name": "dmcnews.org",
        "url": "https://dmcnews.org/",
        "feed": "https://dmcnews.org/feed/",
        "vertical": "World & General News",
        "topics": [
            "breaking world news coverage",
            "in-depth current affairs reporting",
            "politics and policy analysis"
        ]
    },
    {
        "slug": "cubednews_com",
        "name": "cubednews.com",
        "url": "https://cubednews.com/",
        "feed": "https://cubednews.com/feed/",
        "vertical": "World & General News",
        "topics": [
            "breaking news coverage",
            "current affairs analysis",
            "trending news stories"
        ]
    },
    {
        "slug": "tbnexpress_com",
        "name": "tbnexpress.com",
        "url": "https://tbnexpress.com/",
        "feed": "https://tbnexpress.com/feed/",
        "vertical": "World & General News",
        "topics": [
            "breaking news express coverage",
            "current affairs roundup",
            "trending news reports"
        ]
    },
    {
        "slug": "dailywatchreports_com",
        "name": "dailywatchreports.com",
        "url": "https://dailywatchreports.com/",
        "feed": "https://dailywatchreports.com/feed/",
        "vertical": "World & General News",
        "topics": [
            "daily news reports and analysis",
            "breaking news coverage roundup",
            "current affairs reporting"
        ]
    },
    {
        "slug": "tiliasnews_com",
        "name": "tiliasnews.com",
        "url": "https://tiliasnews.com/",
        "feed": "https://tiliasnews.com/feed/",
        "vertical": "World & General News",
        "topics": [
            "breaking news and headlines",
            "current affairs coverage",
            "daily news reports"
        ]
    },
    {
        "slug": "foxperiodical_com",
        "name": "foxperiodical.com",
        "url": "https://foxperiodical.com/",
        "feed": "https://foxperiodical.com/feed/",
        "vertical": "World & General News",
        "topics": [
            "independent news magazine features",
            "culture and society reporting",
            "business trend analysis"
        ]
    },
    {
        "slug": "optimistindia_co",
        "name": "optimistindia.co",
        "url": "https://optimistindia.co/",
        "feed": "https://optimistindia.co/feed/",
        "vertical": "World & General News",
        "topics": [
            "positive India news and stories",
            "Indian current affairs coverage",
            "inspiring India features"
        ]
    },
    {
        "slug": "hogatoga_com_co",
        "name": "hogatoga.com.co",
        "url": "https://hogatoga.com.co/",
        "feed": "https://hogatoga.com.co/feed/",
        "vertical": "Technology & Digital Safety",
        "topics": [
            "latest tech news and updates",
            "gadget reviews and comparisons",
            "mobile gaming guides and tips"
        ]
    },
    {
        "slug": "technofee_in_net",
        "name": "technofee.in.net",
        "url": "https://technofee.in.net/",
        "feed": "https://technofee.in.net/feed/",
        "vertical": "Technology & Digital Safety",
        "topics": [
            "latest technology news and reviews",
            "gadget and software guides",
            "tech how-to tutorials"
        ]
    },
    {
        "slug": "worldgeek_net",
        "name": "worldgeek.net",
        "url": "https://worldgeek.net/",
        "feed": "https://worldgeek.net/feed/",
        "vertical": "Technology & Digital Safety",
        "topics": [
            "tech and geek culture news",
            "gadget reviews and guides",
            "gaming and pop culture coverage"
        ]
    },
    {
        "slug": "cyberkannadigs_org",
        "name": "cyberkannadigs.org",
        "url": "https://cyberkannadigs.org/",
        "feed": "https://cyberkannadigs.org/feed/",
        "vertical": "Technology & Digital Safety",
        "topics": [
            "online scam awareness guides",
            "cybersecurity safety tips",
            "digital fraud prevention advice"
        ]
    },
    {
        "slug": "joho_no_todai_en",
        "name": "Joho no Todai (English)",
        "url": "https://joho-todai.com/en/",
        "feed": "https://joho-todai.com/en/rss/",
        "vertical": "Technology & Digital Safety",
        "topics": [
            "PC hardware and semiconductor industry reporting",
            "Windows Linux and open-source software",
            "AI and cybersecurity news analysis"
        ]
    },
    {
        "slug": "360sportnews_com",
        "name": "360sportnews.com",
        "url": "https://360sportnews.com/",
        "feed": "https://360sportnews.com/feed/",
        "vertical": "Sports",
        "topics": [
            "football match analysis report",
            "live sports news coverage",
            "cricket tournament updates"
        ]
    },
    {
        "slug": "thedigitalweekly_co",
        "name": "thedigitalweekly.co",
        "url": "https://thedigitalweekly.co/",
        "feed": "https://thedigitalweekly.co/feed/",
        "vertical": "Sports",
        "topics": [
            "sports news and match coverage",
            "live scores and game updates",
            "league standings and previews"
        ]
    },
    {
        "slug": "thedigitalwise_com",
        "name": "thedigitalwise.com",
        "url": "https://thedigitalwise.com/",
        "feed": "https://thedigitalwise.com/feed/",
        "vertical": "Entertainment & Culture",
        "topics": [
            "latest movie reviews and ratings",
            "web series streaming guide",
            "sports highlights and analysis"
        ]
    },
    {
        "slug": "thedigitalweekly_com",
        "name": "thedigitalweekly.com",
        "url": "https://thedigitalweekly.com/",
        "feed": "https://thedigitalweekly.com/feed/",
        "vertical": "Entertainment & Culture",
        "topics": [
            "latest movie news and reviews",
            "film release coverage",
            "cinema industry updates"
        ]
    },
    {
        "slug": "peopleonthenews_com",
        "name": "peopleonthenews.com",
        "url": "https://peopleonthenews.com/",
        "feed": "https://peopleonthenews.com/feed/",
        "vertical": "Entertainment & Culture",
        "topics": [
            "celebrity news and profiles",
            "entertainment industry updates",
            "influencer culture coverage"
        ]
    },
    {
        "slug": "illicitlabel_com",
        "name": "illicitlabel.com",
        "url": "https://illicitlabel.com/",
        "feed": "https://illicitlabel.com/feed/",
        "vertical": "Entertainment & Culture",
        "topics": [
            "music and culture features",
            "streetwear and lifestyle guides",
            "entertainment news coverage"
        ]
    },
    {
        "slug": "carmannews_co",
        "name": "carmannews.co",
        "url": "https://carmannews.co/",
        "feed": "https://carmannews.co/feed/",
        "vertical": "Automotive & Lifestyle",
        "topics": [
            "new car model reviews",
            "automotive industry news roundup",
            "electric vehicle buying guide"
        ]
    },
    {
        "slug": "areyoufashion_com",
        "name": "areyoufashion.com",
        "url": "https://areyoufashion.com/",
        "feed": "https://areyoufashion.com/feed/",
        "vertical": "Automotive & Lifestyle",
        "topics": [
            "latest fashion trends and style",
            "outfit ideas and style guides",
            "seasonal fashion inspiration"
        ]
    },
    {
        "slug": "abcyapi_net",
        "name": "abcyapi.net",
        "url": "https://abcyapi.net/",
        "feed": "https://abcyapi.net/feed/",
        "vertical": "Explainers & How-To",
        "topics": [
            "practical how-to guides and tips",
            "everyday knowledge explainers",
            "beginner-friendly information articles"
        ]
    },
    {
        "slug": "sidhewolf_com",
        "name": "sidhewolf.com",
        "url": "https://sidhewolf.com/",
        "feed": "https://sidhewolf.com/feed/",
        "vertical": "Explainers & How-To",
        "topics": [
            "curated articles and guides",
            "trending stories and features",
            "in-depth blog coverage"
        ]
    },
    {
        "slug": "reportspedia_com",
        "name": "reportspedia.com",
        "url": "https://reportspedia.com/",
        "feed": "https://reportspedia.com/feed/",
        "vertical": "Explainers & How-To",
        "topics": [
            "in-depth research reports",
            "market and industry analysis",
            "data-driven insights"
        ]
    },
    {
        "slug": "roo2ya_com",
        "name": "roo2ya.com",
        "url": "https://roo2ya.com/",
        "feed": "https://roo2ya.com/feed/",
        "vertical": "Explainers & How-To",
        "topics": [
            "curated digital resources",
            "online information guides",
            "helpful knowledge articles"
        ]
    }
]


def sources() -> List[Dict[str, object]]:
    """Return the full publisher catalog as a list of dicts."""
    return list(PUBLISHERS)


def verticals() -> List[str]:
    """Return the distinct editorial verticals, in registry order."""
    seen: List[str] = []
    for p in PUBLISHERS:
        v = str(p["vertical"])
        if v not in seen:
            seen.append(v)
    return seen


def by_vertical(vertical: str) -> List[Dict[str, object]]:
    """Return all publishers tagged with *vertical* (case-insensitive)."""
    v = vertical.strip().lower()
    return [p for p in PUBLISHERS if str(p["vertical"]).lower() == v]


def feed_urls(vertical: str | None = None) -> List[str]:
    """Return feed URLs for *vertical*, or for the whole catalog if ``None``."""
    pool = by_vertical(vertical) if vertical else PUBLISHERS
    return [str(p["feed"]) for p in pool]


def find(slug: str) -> Dict[str, object] | None:
    """Look up a single publisher by its catalog ``slug``."""
    for p in PUBLISHERS:
        if p["slug"] == slug:
            return p
    return None
