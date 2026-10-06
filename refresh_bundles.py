#!/usr/bin/env python
"""OKF monthly refresh CLI. See docs/superpowers/specs/2026-10-07-okf-refresh-pipeline-design.md"""
import argparse
import subprocess
import sys
from datetime import date

from okfrefresh import api
from okfrefresh import apply as apply_mod
from okfrefresh import config, fields, report, roster, slugs
from okfrefresh import snapshot as snapshot_mod


def build_map_report(bundle_dirs, active, aliases):
    mapping, unmatched = slugs.build_slug_map(bundle_dirs, active, aliases)
    lines = [f"mapped: {len(mapping)}", f"unmatched: {len(unmatched)}"]
    if unmatched:
        lines.append("unmatched bundles (add an alias or prune):")
        for b in sorted(unmatched):
            lines.append(f"  - {b}")
    return "\n".join(lines)


def selected_bundles(subset, slug_map):
    if subset:
        names = [s for s in subset.split(",") if s]
        bad = [n for n in names if n not in slug_map]
        if bad:
            sys.exit(f"not in slug_map: {', '.join(bad)} (run 'map' first)")
        return names
    return sorted(slug_map)


def _load_active(args):
    return roster.active_slugs(roster.load_roster(args.roster))


def cmd_map(args):
    active = _load_active(args)
    bundles = args.bundles.split(",") if args.bundles else slugs.discover_bundles()
    mapping, _ = slugs.build_slug_map(bundles, active, config.ALIASES)
    print(build_map_report(bundles, active, config.ALIASES))
    if args.write:
        p = slugs.save_slug_map(mapping)
        print(f"wrote {p} ({len(mapping)} entries)")


def cmd_fetch(args):
    slug_map = slugs.load_slug_map()
    entries = []
    for bundle in selected_bundles(args.bundles, slug_map):
        slug = slug_map[bundle]
        payloads = api.fetch_payloads(slug)
        api.write_cache(bundle, payloads)
        snap = fields.extract_snapshot(payloads)
        unknown = [k for k, v in snap.items() if v == "unknown"]
        entries.append(
            {"bundle": bundle, "slug": slug, "status": "ok", **snap, "unknown": unknown}
        )
        print(f"fetched {bundle} ({slug})")
    config.WORKSPACE.mkdir(parents=True, exist_ok=True)
    report.write_report(
        report.build_report(entries, date.today().isoformat()),
        config.WORKSPACE / "report.md",
    )
    print(f"report -> {config.WORKSPACE / 'report.md'}")


def cmd_apply(args):
    slug_map = slugs.load_slug_map()
    written = 0
    for bundle in selected_bundles(args.bundles, slug_map):
        cp = api.cache_path(bundle)
        if not api.cache_is_fresh(cp):
            print(f"skip {bundle}: stale/missing cache (run 'fetch')")
            continue
        snap = fields.extract_snapshot(api.load_cache(bundle))
        md = snapshot_mod.render_snapshot(bundle, snap, date.today().isoformat())
        if apply_mod.write_snapshot(
            config.REPO_ROOT / (bundle + config.BUNDLE_SUFFIX), md, args.write
        ):
            written += 1
            print(("wrote " if args.write else "diff ") + bundle)
    print(f"{'written' if args.write else 'changed'}: {written}")


def cmd_prune(args):
    active = _load_active(args)
    slug_map = slugs.load_slug_map()
    retired = []
    for bundle in slugs.discover_bundles():
        slug = slugs.resolve_slug(bundle, slug_map)
        if bundle in config.MANUAL_EXCLUDE or slug not in active:
            retired.append(config.REPO_ROOT / (bundle + config.BUNDLE_SUFFIX))
    for p in retired:
        print(f"retire {p.name}")
    removed = apply_mod.prune_bundles(retired, config.REPO_ROOT, confirm=args.confirm)
    print(f"removed: {len(removed)} (confirm={args.confirm})")


def cmd_verify(args):
    r = subprocess.run([sys.executable, "verify_conformance.py"], cwd=config.REPO_ROOT)
    sys.exit(r.returncode)


def build_parser():
    p = argparse.ArgumentParser(prog="refresh_bundles")
    sub = p.add_subparsers(dest="command", required=True)

    m = sub.add_parser("map", help="resolve bundle dirs to admin slugs")
    m.add_argument("--roster", default=None)
    m.add_argument("--bundles", default=None, help="comma-separated subset")
    m.add_argument("--write", action="store_true", help="persist slug_map.json")
    m.set_defaults(func=cmd_map)

    f = sub.add_parser("fetch", help="fetch public API payloads into cache")
    f.add_argument("--bundles", default=None)
    f.set_defaults(func=cmd_fetch)

    a = sub.add_parser("apply", help="write data-snapshot.md from cache")
    a.add_argument("--bundles", default=None)
    a.add_argument("--write", action="store_true")
    a.set_defaults(func=cmd_apply)

    pr = sub.add_parser("prune", help="remove retired bundles")
    pr.add_argument("--roster", default=None)
    pr.add_argument("--confirm", action="store_true")
    pr.set_defaults(func=cmd_prune)

    v = sub.add_parser("verify", help="run conformance check")
    v.set_defaults(func=cmd_verify)
    return p


def main(argv=None):
    args = build_parser().parse_args(argv)
    args.func(args)


if __name__ == "__main__":
    sys.exit(main())
