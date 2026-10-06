import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from okfrefresh import apply


class TestApply(unittest.TestCase):
    def test_write_snapshot_dry_run(self):
        with TemporaryDirectory() as d:
            bundle = Path(d) / "acme-okf"
            (bundle / "tables").mkdir(parents=True)
            diff = apply.write_snapshot(bundle, "SNAP", write=False)
            self.assertTrue(diff)
            self.assertFalse((bundle / "tables" / "data-snapshot.md").exists())

    def test_write_snapshot_persists(self):
        with TemporaryDirectory() as d:
            bundle = Path(d) / "acme-okf"
            bundle.mkdir(parents=True)
            apply.write_snapshot(bundle, "SNAP", write=True)
            self.assertEqual(
                (bundle / "tables" / "data-snapshot.md").read_text(encoding="utf-8"),
                "SNAP",
            )

    def test_prune_refuses_outside_root(self):
        with TemporaryDirectory() as d:
            with self.assertRaises(ValueError):
                apply.prune_bundles([Path("C:/Windows")], repo_root=Path(d))

    def test_prune_dry_run_keeps_dir(self):
        with TemporaryDirectory() as d:
            root = Path(d)
            victim = root / "old-okf"
            victim.mkdir()
            removed = apply.prune_bundles([victim], repo_root=root)
            self.assertEqual(removed, [])
            self.assertTrue(victim.exists())

    def test_prune_confirm_removes_inside_root(self):
        with TemporaryDirectory() as d:
            root = Path(d)
            victim = root / "old-okf"
            victim.mkdir()
            removed = apply.prune_bundles([victim], repo_root=root, confirm=True)
            self.assertEqual(removed, [victim])
            self.assertFalse(victim.exists())

    def test_append_log_dedup(self):
        with TemporaryDirectory() as d:
            bundle = Path(d)
            (bundle / "log.md").write_text("# Directory Update Log\n", encoding="utf-8")
            apply.append_log_entry(bundle, "Refreshed snapshot.", "2026-10-07")
            apply.append_log_entry(bundle, "Refreshed snapshot.", "2026-10-07")
            text = (bundle / "log.md").read_text(encoding="utf-8")
            self.assertEqual(text.count("Refreshed snapshot."), 1)


if __name__ == "__main__":
    unittest.main()
