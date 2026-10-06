import json
import os
import urllib.request
from datetime import date
from pathlib import Path

from . import config


class RosterError(RuntimeError):
    pass


def cache_path(d=None):
    d = d or date.today()
    return config.WORKSPACE / f"roster-{d.isoformat()}.json"


def filter_active(payload, test_slugs=None):
    test_slugs = set(test_slugs or config.TEST_SLUGS)
    out = []
    for c in payload.get("clients", []):
        slug = c.get("slug", "")
        if not slug or slug.startswith("prospect-"):
            continue
        if slug in test_slugs:
            continue
        if c.get("status") != "active":
            continue
        out.append(c)
    return out


def active_slugs(payload, test_slugs=None):
    return {c["slug"] for c in filter_active(payload, test_slugs)}


def fetch_raw(key=None, urlopen=urllib.request.urlopen, timeout=60):
    key = key or os.environ.get(config.ADMIN_KEY_ENV)
    if not key:
        raise RosterError(f"{config.ADMIN_KEY_ENV} is not set")
    url = config.ADMIN_BASE + config.CLIENTS_CLM_PATH
    req = urllib.request.Request(url, headers={"Authorization": f"Bearer {key}"})
    with urlopen(req, timeout=timeout) as resp:
        return json.loads(resp.read().decode("utf-8"))


def write_cache(payload, d=None):
    config.WORKSPACE.mkdir(parents=True, exist_ok=True)
    p = cache_path(d)
    p.write_text(json.dumps(payload), encoding="utf-8")
    return p


def load_roster(path=None):
    p = Path(path) if path else cache_path()
    if not p.exists():
        raise RosterError(f"roster cache missing: {p} (run 'fetch' first)")
    return json.loads(p.read_text(encoding="utf-8"))


def roster_is_fresh(path=None, d=None):
    p = Path(path) if path else cache_path(d)
    return p.exists()
