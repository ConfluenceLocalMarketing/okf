import json
import time
import urllib.error
import urllib.request
from datetime import date
from pathlib import Path

from . import config


class ApiError(RuntimeError):
    pass


def build_url(slug, endpoint):
    return f"{config.PUBLIC_BASE}/{slug}/{endpoint}"


def http_get_json(url, attempts=4, timeout=60, urlopen=urllib.request.urlopen):
    last = None
    for i in range(attempts):
        try:
            req = urllib.request.Request(
                url,
                headers={"Accept": "application/json", "User-Agent": "okf-refresh/1.0"},
            )
            with urlopen(req, timeout=timeout) as resp:
                return json.loads(resp.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            last = e
            if e.code == 429 or e.code >= 500:
                time.sleep(min(60, 2 ** i))
                continue
            raise
        except Exception as e:
            last = e
            time.sleep(min(60, 2 ** i))
    raise ApiError(f"GET failed after {attempts} attempts: {url}: {last}")


def fetch_vehicles(slug, limit=None, get_json=None):
    limit = limit or config.VEHICLES_LIMIT
    get_json = get_json or http_get_json
    items = []
    page = 1
    while True:
        data = get_json(build_url(slug, f"vehicles?limit={limit}&page={page}"))
        batch = [e.get("item", e) for e in data.get("itemListElement", [])]
        items.extend(batch)
        if not data.get("hasNextPage") or not batch:
            break
        page += 1
    return items


def cache_path(bundle_dir):
    return config.CACHE_DIR / bundle_dir / "payloads.json"


def cache_is_fresh(path, d=None):
    p = Path(path)
    if not p.exists():
        return False
    return date.fromtimestamp(p.stat().st_mtime) == (d or date.today())


def fetch_payloads(slug, get_json=None):
    get_json = get_json or http_get_json
    payloads = {}
    for ep in config.ENDPOINTS:
        try:
            payloads[ep] = get_json(build_url(slug, ep))
        except Exception as e:
            payloads[ep] = {"_error": str(e)}
    payloads["vehicles"] = fetch_vehicles(slug, get_json=get_json)
    return payloads


def write_cache(bundle_dir, payloads):
    p = cache_path(bundle_dir)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(payloads), encoding="utf-8")
    return p


def load_cache(bundle_dir):
    return json.loads(cache_path(bundle_dir).read_text(encoding="utf-8"))
