def build_report(entries, date):
    lines = [
        f"# Refresh Report - {date}",
        "",
        "| Bundle | Slug | Status | New | Used | Total | Rating | Unknown |",
        "|---|---|---|---|---|---|---|---|",
    ]
    for e in sorted(entries, key=lambda x: x["bundle"]):
        unknown = ", ".join(e.get("unknown") or []) or "-"
        lines.append(
            f"| {e['bundle']} | {e['slug']} | {e['status']} | {e['new']} | {e['used']} "
            f"| {e['total']} | {e['rating']} | {unknown} |"
        )
    lines.append("")
    return "\n".join(lines)


def write_report(text, path):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    return path
