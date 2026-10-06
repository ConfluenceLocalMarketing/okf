import os
import sys
from pathlib import Path

import yaml

RESERVED = {"index.md", "log.md"}


def check_bundle(bundle):
    bundle = Path(bundle)
    errors = []
    count = 0
    for root, _dirs, files in os.walk(bundle):
        for f in files:
            if not f.endswith(".md") or f == "viz.html":
                continue
            fp = Path(root) / f
            count += 1
            if f in RESERVED:
                continue
            content = fp.read_text(encoding="utf-8")
            rel = os.path.relpath(fp)
            if not content.startswith("---"):
                errors.append(f"{rel}: missing frontmatter")
                continue
            parts = content.split("---")
            if len(parts) < 3:
                errors.append(f"{rel}: malformed frontmatter")
                continue
            try:
                fm = yaml.safe_load(parts[1])
            except Exception as e:
                errors.append(f"{rel}: bad yaml - {e}")
                continue
            if not fm or not fm.get("type"):
                errors.append(f"{rel}: missing or empty type field")
    return errors, count


def discover_bundles(root="."):
    return sorted(
        p for p in Path(root).iterdir() if p.is_dir() and p.name.endswith("-okf")
    )


def main(bundles=None):
    bundles = bundles or discover_bundles()
    all_errors = []
    for b in bundles:
        errors, count = check_bundle(b)
        print(f"{b}: {count} md files, viz.html={(Path(b) / 'viz.html').exists()}")
        all_errors.extend(errors)
    if all_errors:
        print(f"\nERRORS ({len(all_errors)}):")
        for e in all_errors:
            print(f"  {e}")
        return 1
    print(f"\nAll {len(bundles)} bundles conformant.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
