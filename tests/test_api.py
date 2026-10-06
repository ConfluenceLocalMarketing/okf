import unittest
from pathlib import Path

from okfrefresh import api, config

FIXTURE_VEHICLES_P1 = {
    "numberOfItems": 3,
    "itemListElement": [{"item": {"condition": "New"}}, {"item": {"condition": "Used"}}],
    "hasNextPage": True,
}
FIXTURE_VEHICLES_P2 = {
    "numberOfItems": 3,
    "itemListElement": [{"item": {"condition": "Used"}}],
    "hasNextPage": False,
}


class TestApi(unittest.TestCase):
    def test_build_url(self):
        self.assertEqual(
            api.build_url("acme", "business"),
            f"{config.PUBLIC_BASE}/acme/business",
        )

    def test_vehicles_pagination_stops(self):
        pages = {1: FIXTURE_VEHICLES_P1, 2: FIXTURE_VEHICLES_P2}
        calls = []

        def fake(url, **kw):
            calls.append(url)
            page = int(url.split("page=")[1].split("&")[0])
            return pages[page]

        items = api.fetch_vehicles("acme", get_json=fake)
        self.assertEqual(len(items), 3)
        self.assertEqual(len(calls), 2)

    def test_cache_is_fresh_false_when_missing(self):
        self.assertFalse(api.cache_is_fresh(Path("no-such.json")))

    def test_cache_is_fresh_true_for_today(self):
        p = config.WORKSPACE / "cache_test.json"
        config.WORKSPACE.mkdir(parents=True, exist_ok=True)
        p.write_text("{}", encoding="utf-8")
        try:
            self.assertTrue(api.cache_is_fresh(p))
        finally:
            p.unlink()


if __name__ == "__main__":
    unittest.main()
