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
