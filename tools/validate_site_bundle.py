#!/usr/bin/env python3
"""Validate a document-reconstruction Sites bundle.

This is deliberately small. It does not decide editorial structure; the reviewing
LLM/editor does that. It checks that the handoff is coherent enough that Sites
can consume it without silently falling back to a PDF shelf.

Usage:
    python tools/validate_site_bundle.py path/to/site-bundle.json

Optional:
    python tools/validate_site_bundle.py path/to/latest.json --latest
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


class BundleError(Exception):
    pass


def load_json(path: Path) -> dict[str, Any]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise BundleError(f"missing file: {path}") from exc
    except json.JSONDecodeError as exc:
        raise BundleError(f"invalid JSON in {path}: {exc}") from exc
    if not isinstance(data, dict):
        raise BundleError(f"top level must be an object: {path}")
    return data


def require(obj: dict[str, Any], key: str, where: str) -> Any:
    if key not in obj:
        raise BundleError(f"missing required key {where}.{key}")
    return obj[key]


def validate_bundle(path: Path) -> list[str]:
    bundle = load_json(path)
    warnings: list[str] = []

    require(bundle, "schema_version", "bundle")
    require(bundle, "project_id", "bundle")
    require(bundle, "bundle_status", "bundle")
    default_experience = require(bundle, "default_experience", "bundle")
    site = require(bundle, "site", "bundle")
    routes = require(bundle, "routes", "bundle")
    views = require(bundle, "views", "bundle")

    if not isinstance(site, dict):
        raise BundleError("bundle.site must be an object")
    for key in ("title", "headline"):
        require(site, key, "bundle.site")

    if not isinstance(routes, list) or not routes:
        raise BundleError("bundle.routes must be a non-empty array")
    route_paths: set[str] = set()
    for i, route in enumerate(routes):
        if not isinstance(route, dict):
            raise BundleError(f"routes[{i}] must be an object")
        route_path = require(route, "path", f"routes[{i}]")
        require(route, "entity_id", f"routes[{i}]")
        require(route, "template", f"routes[{i}]")
        require(route, "readiness", f"routes[{i}]")
        if route_path in route_paths:
            raise BundleError(f"duplicate route path: {route_path}")
        route_paths.add(route_path)

    if "/" not in route_paths:
        warnings.append("no '/' route declared")

    if not isinstance(views, list) or not views:
        raise BundleError("bundle.views must be a non-empty array")
    view_ids: set[str] = set()
    defaults = 0
    for i, view in enumerate(views):
        if not isinstance(view, dict):
            raise BundleError(f"views[{i}] must be an object")
        view_id = require(view, "id", f"views[{i}]")
        require(view, "label", f"views[{i}]")
        require(view, "status", f"views[{i}]")
        if view_id in view_ids:
            raise BundleError(f"duplicate view id: {view_id}")
        view_ids.add(view_id)
        if view.get("default") is True:
            defaults += 1

    if defaults != 1:
        raise BundleError(f"exactly one view must have default=true; found {defaults}")
    if default_experience not in view_ids:
        raise BundleError(
            f"default_experience '{default_experience}' is not present in views[]"
        )

    # Local dependencies should exist when expressed as relative paths.
    for key in ("source_feed", "editorial_overlay"):
        value = bundle.get(key)
        if isinstance(value, str) and "://" not in value:
            dependency = (path.parent / value).resolve()
            if not dependency.exists():
                warnings.append(f"referenced {key} does not exist locally: {value}")

    render_now = bundle.get("render_now", [])
    if not render_now:
        warnings.append("no render_now instructions; Sites may have to infer too much")

    forbidden = bundle.get("do_not_render_as_primary", [])
    if not forbidden:
        warnings.append(
            "no do_not_render_as_primary guidance; generic PDF-viewer fallback may dominate"
        )

    if default_experience in {"facsimile", "pdf", "raw-pdf-order"}:
        warnings.append(
            "default experience is source/facsimile oriented; confirm this is intentional"
        )

    feedback = bundle.get("feedback")
    if not isinstance(feedback, dict):
        warnings.append("no feedback object / comm-line pointer")

    return warnings


def resolve_latest(path: Path) -> Path:
    latest = load_json(path)
    current = latest.get("current_bundle")
    if not isinstance(current, str) or not current:
        raise BundleError("latest.json missing non-empty current_bundle")
    return (path.parent / current).resolve()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("path", type=Path)
    parser.add_argument(
        "--latest",
        action="store_true",
        help="treat path as latest.json and validate its current_bundle",
    )
    args = parser.parse_args()

    path = args.path.resolve()
    try:
        if args.latest:
            path = resolve_latest(path)
        warnings = validate_bundle(path)
    except BundleError as exc:
        print(f"FAIL: {exc}")
        return 1

    print(f"PASS: {path}")
    for warning in warnings:
        print(f"WARN: {warning}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
