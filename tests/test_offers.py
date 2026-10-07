import unittest

from okfrefresh import offers

PAYLOAD = {
    "@type": "ItemList",
    "itemListElement": [
        {
            "item": {
                "@type": "Offer",
                "name": "2026 MDX",
                "description": "3.49% APR \u2013 60 months",
                "validThrough": "2026-11-02T00:00:00.000Z",
                "url": "https://api.promptgraph.ai/api/v1/acme/offers/MDX",
            }
        },
        {"item": {"@type": "Offer", "name": ""}},
    ],
}


class TestOffers(unittest.TestCase):
    def test_clean_replaces_dashes_and_collapses_space(self):
        self.assertEqual(offers.clean("A \u2014 B\u2013C\n  D"), "A - B-C D")

    def test_clean_escapes_pipe(self):
        self.assertEqual(offers.clean("a | b"), "a / b")

    def test_parse_offers_skips_empty_names(self):
        got = offers.parse_offers(PAYLOAD)
        self.assertEqual(len(got), 1)
        self.assertEqual(got[0]["name"], "2026 MDX")
        self.assertEqual(got[0]["valid_through"], "2026-11-02T00:00:00.000Z")

    def test_render_has_frontmatter_and_row(self):
        md = offers.render_offers(
            "acme-okf", "Acme", "acme", offers.parse_offers(PAYLOAD), "2026-10-07"
        )
        self.assertTrue(md.startswith("---\n"))
        self.assertIn("type: Offer Catalog", md)
        self.assertIn("| 2026 MDX |", md)
        self.assertIn("2026-11-02", md)
        self.assertNotIn("\u2013", md)

    def test_render_empty_offers_still_has_header(self):
        md = offers.render_offers("acme-okf", "Acme", "acme", [], "2026-10-07")
        self.assertIn("| Offer | Details |", md)


if __name__ == "__main__":
    unittest.main()
