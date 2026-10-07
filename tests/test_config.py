import unittest

from okfrefresh import config


class TestConfig(unittest.TestCase):
    def test_paths_are_absolute(self):
        self.assertTrue(str(config.REPO_ROOT).endswith("okf"))
        self.assertEqual(config.SLUG_MAP_PATH.name, "slug_map.json")
        self.assertEqual(config.WORKSPACE.name, "refresh")

    def test_admin_key_env_name(self):
        self.assertEqual(config.ADMIN_KEY_ENV, "PG_ADMIN_API_KEY")

    def test_manual_exclude_contains_user_removals(self):
        self.assertIn("avondale-auto-repair", config.MANUAL_EXCLUDE)
        self.assertIn("logan-square-auto-repair", config.MANUAL_EXCLUDE)

    def test_endpoints(self):
        self.assertEqual(
            config.ENDPOINTS, ["business", "gbp-context", "testimonials", "prompts"]
        )


if __name__ == "__main__":
    unittest.main()
