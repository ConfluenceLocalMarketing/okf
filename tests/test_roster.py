import json
import unittest
from datetime import date
from pathlib import Path

from okfrefresh import roster

FIXTURE = Path(__file__).parent / "fixtures" / "roster_sample.json"


class TestRoster(unittest.TestCase):
    def setUp(self):
        self.payload = json.loads(FIXTURE.read_text(encoding="utf-8"))

    def test_filter_active_drops_prospects_tests_inactive(self):
        got = [c["slug"] for c in roster.filter_active(self.payload)]
        self.assertEqual(got, ["acura-of-springfield", "a-abel-roofing"])

    def test_active_slugs_returns_set(self):
        self.assertEqual(
            roster.active_slugs(self.payload),
            {"acura-of-springfield", "a-abel-roofing"},
        )

    def test_cache_path_uses_date(self):
        p = roster.cache_path(date.today())
        self.assertTrue(str(p).endswith(f"roster-{date.today().isoformat()}.json"))

    def test_load_roster_missing_raises(self):
        with self.assertRaises(roster.RosterError):
            roster.load_roster(Path("does-not-exist.json"))


if __name__ == "__main__":
    unittest.main()
