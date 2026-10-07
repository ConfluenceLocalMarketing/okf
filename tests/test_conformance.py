import unittest
from pathlib import Path

from verify_conformance import check_bundle

FIXTURE = Path(__file__).parent / "fixtures" / "conformance"


class TestConformance(unittest.TestCase):
    def test_valid_bundle_passes(self):
        errors, count = check_bundle(FIXTURE / "good-okf")
        self.assertEqual(errors, [])
        self.assertGreater(count, 0)

    def test_missing_type_fails(self):
        errors, _ = check_bundle(FIXTURE / "bad-okf")
        self.assertEqual(len(errors), 1)


if __name__ == "__main__":
    unittest.main()
