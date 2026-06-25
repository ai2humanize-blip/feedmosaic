from feedmosaic import catalog


def test_catalog_is_populated():
    assert len(catalog.sources()) >= 30


def test_every_entry_has_required_fields():
    for p in catalog.sources():
        assert p["url"].startswith("https://")
        assert p["feed"].startswith("https://")
        assert p["vertical"]
        assert p["slug"]


def test_by_vertical_roundtrip():
    for v in catalog.verticals():
        members = catalog.by_vertical(v)
        assert members
        assert all(str(p["vertical"]) == v for p in members)


def test_find_known_slug():
    first = catalog.sources()[0]
    assert catalog.find(first["slug"]) == first
    assert catalog.find("no_such_slug") is None
