import unittest

from okfrefresh import slugs


class TestSlugs(unittest.TestCase):
    def test_bundle_dir_from_name(self):
        self.assertEqual(
            slugs.bundle_dir_from_name("acura-of-springfield-okf"),
            "acura-of-springfield",
        )

    def test_resolve_exact(self):
        m = {"acura-of-springfield": "acura-of-springfield"}
        self.assertEqual(
            slugs.resolve_slug("acura-of-springfield", m), "acura-of-springfield"
        )

    def test_resolve_alias(self):
        m = {"basil-resale": "basil-resale-sheridan"}
        self.assertEqual(
            slugs.resolve_slug("basil-resale", m), "basil-resale-sheridan"
        )

    def test_resolve_missing_is_none(self):
        self.assertIsNone(slugs.resolve_slug("nope", {}))

    def test_build_map_exact_and_alias(self):
        active = {"acura-of-springfield", "basil-resale-sheridan"}
        aliases = {"basil-resale": "basil-resale-sheridan"}
        m, unmatched = slugs.build_slug_map(
            ["acura-of-springfield", "basil-resale", "retired-store"], active, aliases
        )
        self.assertEqual(m["acura-of-springfield"], "acura-of-springfield")
        self.assertEqual(m["basil-resale"], "basil-resale-sheridan")
        self.assertEqual(unmatched, ["retired-store"])

    def test_build_map_ignores_alias_to_missing(self):
        m, unmatched = slugs.build_slug_map(["x"], {"other"}, {"x": "gone"})
        self.assertEqual(m, {})
        self.assertEqual(unmatched, ["x"])


if __name__ == "__main__":
    unittest.main()
