import unittest

import refresh_bundles


class TestFetchSelection(unittest.TestCase):
    def test_selected_bundles(self):
        self.assertEqual(
            refresh_bundles.selected_bundles(None, {"a": "a", "b": "b"}), ["a", "b"]
        )

    def test_selected_bundles_subset(self):
        self.assertEqual(
            refresh_bundles.selected_bundles("b", {"a": "a", "b": "b"}), ["b"]
        )

    def test_selected_bundles_rejects_unmapped(self):
        with self.assertRaises(SystemExit):
            refresh_bundles.selected_bundles("a,zzz", {"a": "a"})


if __name__ == "__main__":
    unittest.main()
