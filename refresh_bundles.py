#!/usr/bin/env python
"""OKF monthly refresh CLI. See docs/superpowers/specs/2026-10-07-okf-refresh-pipeline-design.md"""
import argparse
import sys

from okfrefresh import config, roster, slugs


def build_map_report(bundle_dirs, active, aliases):
    mapping, unmatched = slugs.build_slug_map(bundle_dirs, active, aliases)
    lines = [f"mapped: {len(mapping)}", f"unmatched: {len(unmatched)}"]
    if unmatched:
        lines.append("unmatched bundles (add an alias or prune):")
        for b in sorted(unmatched):
            lines.append(f"  - {b}")
    return "\n".join(lines)


def _load_active(args):
    payload = roster.load_roster(args.roster)
    return roster.active_slugs(payload)


def cmd_map(args):
    active = _load_active(args)
    bundles = args.bundles.split(",") if args.bundles else slugs.discover_bundles()
    mapping, _ = slugs.build_slug_map(bundles, active, config.ALIASES)
    print(build_map_report(bundles, active, config.ALIASES))
    if args.write:
        p = slugs.save_slug_map(mapping)
        print(f"wrote {p} ({len(mapping)} entries)")


def build_parser():
    p = argparse.ArgumentParser(prog="refresh_bundles")
    sub = p.add_subparsers(dest="command", required=True)

    m = sub.add_parser("map", help="resolve bundle dirs to admin slugs")
    m.add_argument("--roster", default=None)
    m.add_argument("--bundles", default=None, help="comma-separated subset")
    m.add_argument("--write", action="store_true", help="persist slug_map.json")
    m.set_defaults(func=cmd_map)
    return p


def main(argv=None):
    args = build_parser().parse_args(argv)
    args.func(args)


if __name__ == "__main__":
    sys.exit(main())
