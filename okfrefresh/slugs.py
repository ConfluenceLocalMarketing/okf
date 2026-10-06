import json
from pathlib import Path

from . import config


def bundle_dir_from_name(name):
    if name.endswith(config.BUNDLE_SUFFIX):
        return name[: -len(config.BUNDLE_SUFFIX)]
    return name


def discover_bundles(repo_root=None):
    root = Path(repo_root) if repo_root else config.REPO_ROOT
    return sorted(
        b
        for b in (bundle_dir_from_name(d.name) for d in root.iterdir() if d.is_dir())
        if root.joinpath(b + config.BUNDLE_SUFFIX).is_dir()
    )


def load_slug_map(path=None):
    p = Path(path) if path else config.SLUG_MAP_PATH
    if not p.exists():
        return {}
    return json.loads(p.read_text(encoding="utf-8"))


def save_slug_map(mapping, path=None):
    p = Path(path) if path else config.SLUG_MAP_PATH
    p.write_text(json.dumps(dict(sorted(mapping.items())), indent=2), encoding="utf-8")
    return p


def resolve_slug(bundle_dir, slug_map):
    return slug_map.get(bundle_dir)


def build_slug_map(bundle_dirs, active_slugs, aliases=None):
    aliases = aliases or {}
    mapping = {}
    unmatched = []
    for b in bundle_dirs:
        target = aliases.get(b, b)
        if target in active_slugs:
            mapping[b] = target
        else:
            unmatched.append(b)
    return mapping, unmatched
