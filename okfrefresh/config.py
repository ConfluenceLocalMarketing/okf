from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

ADMIN_BASE = "https://api.promptgraph.ai/api/admin"
CLIENTS_CLM_PATH = "/clients/clm"
ADMIN_KEY_ENV = "PG_ADMIN_API_KEY"

PUBLIC_BASE = "https://api.promptgraph.ai/api/v1"
ENDPOINTS = ["business", "gbp-context", "testimonials", "prompts"]
VEHICLES_LIMIT = 100

WORKSPACE = REPO_ROOT / "refresh"
CACHE_DIR = WORKSPACE / "cache"
SLUG_MAP_PATH = Path(__file__).resolve().parent / "slug_map.json"

MANUAL_EXCLUDE = [
    "avondale-auto-repair",
    "logan-square-auto-repair",
]

TEST_SLUGS = [
    "test-client",
    "static-tester",
    "performance-monitoring",
    "local-business",
    "maintenance",
    "new-age-marketing-placeholder",
]

BUNDLE_SUFFIX = "-okf"

ALIASES = {
    "basil-resale": "basil-resale-sheridan",
    "nick-mayer-dickson-bg": "dickson-bg",
    "nick-mayer-dickson-chevy": "dickson-chevy",
    "nick-mayer-lewisburg-chevy": "lewisburg-chevy",
    "nick-mayer-lewisburg-gmc": "lewisburg-gmc",
    "leif-johnson-ford-austin": "leif-johnson-austin",
    "leif-johnson-ford-buda": "leif-johnson-buda",
    "leif-johnson-ford-manor": "leif-johnson-manor",
    "texantitle": "texan-title",
    "memorial-hospital-converse-county": "memorial-hospital-of-converse-county",
    "car-x-arnold-mo": "arnold-mo",
    "car-x-ballwin-mo": "ballwin-mo",
    "car-x-bridgeton-mo": "bridgeton-mo",
    "car-x-concord-village-mo": "concord-village-mo",
    "car-x-crestwood-mo": "crestwood-mo",
    "car-x-florissant-mo": "florissant-mo",
    "car-x-hazelwood-mo": "hazelwood-mo",
    "car-x-jennings-mo": "jennings-mo",
    "car-x-kirkwood-mo": "kirkwood-mo",
    "car-x-maryland-heights-mo": "maryland-heights-mo",
    "car-x-mehlville-mo": "mehlville-mo",
    "car-x-mid-rivers-st-peters-mo": "mid-rivers-st-peters-mo",
    "car-x-ofallon-mo": "ofallon-mo",
    "car-x-overland-mo": "overland-mo",
    "car-x-shrewsbury-mo": "shrewsbury-mo",
    "car-x-st-louis-mo": "st-louis-mo",
    "car-x-university-city-mo": "university-city-mo",
    "car-x-chicago": "car-x-tire-&-auto-chicago",
    "car-x-fairview-heights-il": "fairview-heights-il",
    "car-x-granite-il": "granite-il",
    "bare-bones-furniture-mattress": "bare-bones-furniture-&-mattress",
    "weathercraft-garden": "weathercraft-roofing",
}
