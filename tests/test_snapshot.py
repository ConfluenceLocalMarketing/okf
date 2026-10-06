import unittest

from okfrefresh import snapshot


class TestSnapshot(unittest.TestCase):
    def setUp(self):
        self.data = {
            "new": 10,
            "used": 5,
            "total": 15,
            "rating": 4.7,
            "reviews": 100,
            "place_id": "ChIJ15",
            "hours": "Mon-Fri 9-8",
            "phone": "(352) 309-0695",
            "address": "1 Main St, Clermont, FL 34711",
        }

    def test_render_has_frontmatter_and_date(self):
        md = snapshot.render_snapshot("hyundai-of-central-florida", self.data, "2026-10-07")
        self.assertTrue(md.startswith("---\n"))
        self.assertIn("type: Data Snapshot", md)
        self.assertIn("2026-10-07", md)
        self.assertIn("| New | 10 |", md)
        self.assertIn("| Used | 5 |", md)

    def test_roundtrip(self):
        md = snapshot.render_snapshot("acme", self.data, "2026-10-07")
        parsed = snapshot.parse_snapshot(md)
        self.assertEqual(parsed["new"], "10")
        self.assertEqual(parsed["rating"], "4.7")

    def test_diff_existing_none(self):
        md = snapshot.render_snapshot("acme", self.data, "2026-10-07")
        self.assertFalse(snapshot.diff_existing(md, md))

    def test_diff_existing_changed(self):
        old = snapshot.render_snapshot("acme", self.data, "2026-10-06")
        new = snapshot.render_snapshot("acme", self.data, "2026-10-07")
        self.assertTrue(snapshot.diff_existing(old, new))


if __name__ == "__main__":
    unittest.main()
