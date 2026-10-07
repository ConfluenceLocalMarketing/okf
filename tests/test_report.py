import unittest

from okfrefresh import report


class TestReport(unittest.TestCase):
    def test_build_report(self):
        entries = [
            {
                "bundle": "acme",
                "slug": "acme",
                "status": "ok",
                "new": 1,
                "used": 2,
                "total": 3,
                "rating": 4.5,
                "unknown": [],
            },
            {
                "bundle": "globex",
                "slug": "globex",
                "status": "ok",
                "new": 0,
                "used": 0,
                "total": 0,
                "rating": "unknown",
                "unknown": ["rating"],
            },
        ]
        md = report.build_report(entries, "2026-10-07")
        self.assertIn("# Refresh Report - 2026-10-07", md)
        self.assertIn("| acme |", md)
        self.assertIn("globex", md)
        self.assertIn("rating", md)


if __name__ == "__main__":
    unittest.main()
