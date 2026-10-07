import re

_WS_RE = re.compile(r"\s+")
_DATE_RE = re.compile(r"(\d{4}-\d{2}-\d{2})")
_DASHES = {"\u2013": "-", "\u2014": "-", "\u2212": "-", "\u2010": "-", "\u2011": "-"}


def clean(text):
    if not text:
        return ""
    t = str(text)
    for bad, good in _DASHES.items():
        t = t.replace(bad, good)
    t = t.replace("|", "/")
    return _WS_RE.sub(" ", t).strip()


def parse_offers(payload):
    items = payload.get("itemListElement", []) if isinstance(payload, dict) else []
    out = []
    for entry in items:
        item = entry.get("item", entry) if isinstance(entry, dict) else {}
        if not isinstance(item, dict):
            continue
        name = clean(item.get("name"))
        if not name:
            continue
        out.append(
            {
                "name": name,
                "description": clean(item.get("description")),
                "valid_through": clean(item.get("validThrough")),
                "url": item.get("url") or item.get("@id") or "",
            }
        )
    return out


def _date(iso):
    if not iso:
        return "see source"
    return iso[:10]


def is_valid(offer, as_of):
    match = _DATE_RE.search(offer.get("valid_through") or "")
    if not match:
        return True
    return match.group(1) >= as_of


def valid_offers(offers, as_of):
    return [offer for offer in offers if is_valid(offer, as_of)]


def render_offers(bundle_dir, name, slug, offers, as_of, source_url=None):
    title = f"{name} - Current Offers"
    resource = source_url or f"https://api.promptgraph.ai/api/v1/{slug}/offers"
    lines = [
        "---",
        "type: Offer Catalog",
        f'title: "{title}"',
        f'description: "Current purchase, lease, and finance offers for {name}, as of {as_of}."',
        f"resource: {resource}",
        "tags:",
        "  - offers",
        "  - incentives",
        "  - promptgraph",
        f"timestamp: {as_of}",
        "---",
        "",
        f"# {title}",
        "",
        f"Current offers sourced from PromptGraph, as of {as_of}.",
        "",
        "| Offer | Details | Valid through | Source |",
        "|---|---|---|---|",
    ]
    for offer in offers:
        link = offer.get("url") or ""
        source = f"[link]({link})" if link else "see source"
        details = offer.get("description") or "-"
        lines.append(
            f"| {offer['name']} | {details} | {_date(offer.get('valid_through'))} | {source} |"
        )
    lines.append("")
    return "\n".join(lines)
