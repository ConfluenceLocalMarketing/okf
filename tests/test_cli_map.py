import json
import unittest
from pathlib import Path

import refresh_bundles
from okfrefresh import config, roster

FIXTURE = Path(__file__).parent / "fixtures" / "roster_sample.json"


class TestMapCommand(unittest.TestCase):
    def test_build_and_report(self):
        payload = json.loads(FIXTURE.read_text(encoding="utf-8"))
        active = roster.active_slugs(payload)
        bundles = ["acura-of-springfield", "a-abel-roofing", "retired-store"]
        text = refresh_bundles.build_map_report(bundles, active, config.ALIASES)
        self.assertIn("mapped: 2", text)
        self.assertIn("retired-store", text)


if __name__ == "__main__":
    unittest.main()
