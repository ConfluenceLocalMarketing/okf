UNKNOWN = "unknown"


def _first(*vals):
    for v in vals:
        if v not in (None, "", [], {}):
            return v
    return None


def _business(payloads):
    return payloads.get("business") or {}


def _gbp(payloads):
    return payloads.get("gbp-context") or {}


def _place_id(business, gbp):
    meta = gbp.get("gbp_meta") or {}
    if meta.get("place_id"):
        return meta["place_id"]
    for u in business.get("sameAs", []):
        if "place_id:" in u:
            return u.split("place_id:")[-1]
    return UNKNOWN


def _format_hours_spec(spec):
    if isinstance(spec, str):
        return spec.strip() or None
    if isinstance(spec, dict):
        return (spec.get("description") or "").strip() or None
    if isinstance(spec, list):
        parts = []
        for item in spec:
            if isinstance(item, dict):
                desc = (item.get("description") or "").strip()
                if desc:
                    parts.append(desc)
                    continue
                days = item.get("dayOfWeek")
                if isinstance(days, list):
                    days = ", ".join(days)
                opens, closes = item.get("opens"), item.get("closes")
                if days or opens or closes:
                    parts.append(" ".join(p for p in (days, opens, closes) if p))
            elif isinstance(item, str) and item.strip():
                parts.append(item.strip())
        return "; ".join(parts) if parts else None
    return None


def _address(business, gbp):
    addr = business.get("address") or (gbp.get("business_info") or {}).get("address")
    if isinstance(addr, dict):
        head = ", ".join(
            p for p in (addr.get("streetAddress"), addr.get("addressLocality")) if p
        )
        tail = " ".join(
            p for p in (addr.get("addressRegion"), addr.get("postalCode")) if p
        )
        joined = f"{head}, {tail}" if head and tail else (head or tail)
        return joined or UNKNOWN
    return addr or UNKNOWN


def extract_snapshot(payloads):
    business = _business(payloads)
    gbp = _gbp(payloads)
    info = gbp.get("business_info") or {}
    meta = gbp.get("gbp_meta") or {}
    vehicles = payloads.get("vehicles") or []

    new = sum(1 for v in vehicles if (v.get("condition") or "").strip().lower() == "new")
    total = len(vehicles)
    used = total - new

    rating = _first(
        meta.get("average_rating"),
        (business.get("aggregateRating") or {}).get("ratingValue"),
        UNKNOWN,
    )
    reviews = _first(
        meta.get("total_reviews"),
        (business.get("aggregateRating") or {}).get("reviewCount"),
        UNKNOWN,
    )
    hours = _first(
        _format_hours_spec(business.get("openingHoursSpecification")),
        info.get("hours"),
        UNKNOWN,
    )
    phone = _first(business.get("telephone"), info.get("phone"), UNKNOWN)

    return {
        "new": new,
        "used": used,
        "total": total,
        "rating": rating,
        "reviews": reviews,
        "place_id": _place_id(business, gbp),
        "hours": hours,
        "phone": phone,
        "address": _address(business, gbp),
    }
