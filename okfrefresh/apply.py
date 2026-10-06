import shutil
from pathlib import Path


def write_snapshot(bundle_dir, snapshot_md, write=False):
    bundle = Path(bundle_dir)
    target = bundle / "tables" / "data-snapshot.md"
    old = target.read_text(encoding="utf-8") if target.exists() else None
    if old == snapshot_md:
        return False
    if write:
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(snapshot_md, encoding="utf-8")
    return True


def append_log_entry(bundle_dir, entry, date):
    bundle = Path(bundle_dir)
    log = bundle / "log.md"
    text = log.read_text(encoding="utf-8") if log.exists() else "# Directory Update Log\n"
    if entry in text:
        return False
    if f"## {date}" in text:
        text = text.replace(f"## {date}\n", f"## {date}\n- **Refresh**: {entry}\n", 1)
    else:
        text = text.rstrip("\n") + f"\n\n## {date}\n- **Refresh**: {entry}\n"
    log.write_text(text, encoding="utf-8")
    return True


def prune_bundles(dirs, repo_root, confirm=False):
    root = Path(repo_root).resolve()
    victims = []
    for d in dirs:
        p = Path(d)
        if root not in p.resolve().parents:
            raise ValueError(f"refusing to prune outside repo root: {p}")
        if p.exists():
            victims.append(p)
    if not confirm:
        return []
    for p in victims:
        shutil.rmtree(p)
    return victims
