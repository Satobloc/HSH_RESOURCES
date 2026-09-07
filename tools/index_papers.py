#!/usr/bin/env python3
"""Build a deterministic structural catalog of HSH resource files.

The index records presence and byte identity. It does not assign scientific or
H(s)H relevance. Dry-run is the default; pass --apply to write outputs.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable

VERSION = "1.0.0"
GENERATED = {
    "indexes/RESOURCE_INDEX.md",
    "indexes/index-state.json",
}
SKIP_PARTS = {".git", "__pycache__", ".pytest_cache"}


def iso_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def identifier(path: str) -> dict[str, str]:
    name = Path(path).stem
    ssrn = re.search(r"(?:^|\b)ssrn[-_ ]?(\d{5,8})\b", name, re.I)
    if ssrn:
        return {"scheme": "ssrn", "value": ssrn.group(1)}
    arxiv = re.search(r"(?:^|\b)(\d{4}\.\d{4,5})(v\d+)?\b", name, re.I)
    if arxiv:
        value = arxiv.group(1) + (arxiv.group(2) or "")
        return {"scheme": "arxiv", "value": value}
    legacy = re.fullmatch(r"(\d{7})(v\d+)?", name, re.I)
    if legacy:
        # A bare seven-digit filename can be a legacy arXiv number, an SSRN
        # identifier, or a local accession. Do not silently choose among them.
        return {"scheme": "unresolved-seven-digit-id", "value": legacy.group(0)}
    return {}


def github_entries(payload: dict[str, Any]) -> tuple[list[dict[str, Any]], str, bool]:
    entries = []
    for item in payload.get("tree", []):
        if item.get("type") != "blob":
            continue
        path = item["path"]
        if path in GENERATED:
            continue
        entries.append(
            {
                "path": path,
                "bytes": item.get("size"),
                "content_id": item.get("sha"),
                "hash_kind": "git-blob-sha1",
            }
        )
    return entries, payload.get("sha", "unknown"), bool(payload.get("truncated"))


def local_entries(root: Path) -> tuple[list[dict[str, Any]], str, bool]:
    entries = []
    for path in sorted(root.rglob("*")):
        if not path.is_file() or any(part in SKIP_PARTS for part in path.parts):
            continue
        rel = path.relative_to(root).as_posix()
        if rel in GENERATED or rel.startswith("derived/text/"):
            continue
        entries.append(
            {
                "path": rel,
                "bytes": path.stat().st_size,
                "content_id": sha256(path),
                "hash_kind": "sha256",
            }
        )
    tree_hash = hashlib.sha256(
        "\n".join(f"{x['path']}\0{x['content_id']}" for x in entries).encode()
    ).hexdigest()
    return entries, tree_hash, False


def enrich(entries: Iterable[dict[str, Any]]) -> list[dict[str, Any]]:
    result = []
    for entry in entries:
        row = dict(entry)
        suffix = Path(row["path"]).suffix.lower() or "[none]"
        row["extension"] = suffix
        top = row["path"].split("/", 1)[0]
        is_source = top not in {"tools", "tests", "indexes", "derived"} and row["path"] not in {
            "README.md", ".gitignore", "requirements-tools.txt"
        }
        if is_source and suffix == ".pdf":
            row["kind"] = "paper-pdf"
        elif is_source:
            row["kind"] = "supporting-resource"
        else:
            row["kind"] = "repository-machinery"
        row["identifier"] = identifier(row["path"])
        result.append(row)
    return sorted(result, key=lambda x: x["path"].casefold())


def make_state(entries: list[dict[str, Any]], tree_id: str, truncated: bool, scanned_at: str) -> dict[str, Any]:
    groups: dict[str, list[str]] = defaultdict(list)
    for row in entries:
        if row.get("content_id"):
            groups[row["content_id"]].append(row["path"])
    duplicates = [
        {"content_id": key, "paths": sorted(paths)}
        for key, paths in sorted(groups.items())
        if len(paths) > 1
    ]
    pdfs = [row for row in entries if row["kind"] == "paper-pdf"]
    sources = [row for row in entries if row["kind"] in {"paper-pdf", "supporting-resource"}]
    return {
        "schema_version": 1,
        "tool_version": VERSION,
        "scanned_at": scanned_at,
        "tree_id": tree_id,
        "github_tree_truncated": truncated,
        "coverage": "complete structural traversal" if not truncated else "partial structural traversal",
        "counts": {
            "files": len(entries),
            "source_files": len(sources),
            "papers_pdf": len(pdfs),
            "repository_machinery_files": len(entries) - len(sources),
            "bytes_known": sum(row.get("bytes") or 0 for row in entries),
            "duplicate_content_groups": len(duplicates),
        },
        "counts_by_extension": dict(sorted(Counter(row["extension"] for row in entries).items())),
        "counts_by_kind": dict(sorted(Counter(row["kind"] for row in entries).items())),
        "counts_by_top_level": dict(sorted(Counter(row["path"].split("/")[0] for row in entries).items())),
        "duplicates": duplicates,
        "items": entries,
        "errors": [],
        "limitations": [
            "Structural identity is not bibliographic identity or scientific relevance.",
            "GitHub-tree mode records Git blob SHA-1; local mode records SHA-256.",
            "Titles, authors, DOI data, page counts, and extraction quality require a local PDF pass.",
        ],
    }


def markdown(state: dict[str, Any]) -> str:
    counts = state["counts"]
    lines = [
        "# HSH Resource Structural Index",
        "",
        "> Generated navigation artifact; not a bibliography or theory-evidence judgment.",
        "",
        f"- Scanned: `{state['scanned_at']}`",
        f"- Tree/content state: `{state['tree_id']}`",
        f"- Coverage: {state['coverage']}",
        f"- Files: {counts['files']}",
        f"- Uploaded source files: {counts['source_files']}",
        f"- PDF papers: {counts['papers_pdf']}",
        f"- Repository machinery files: {counts['repository_machinery_files']}",
        f"- Byte-identical duplicate groups: {counts['duplicate_content_groups']}",
        "",
        "## Top-level coverage",
        "",
        "| Path | Files |",
        "|---|---:|",
    ]
    lines.extend(f"| `{key}` | {value} |" for key, value in state["counts_by_top_level"].items())
    lines += ["", "## Duplicate-content groups", ""]
    if state["duplicates"]:
        for group in state["duplicates"]:
            lines.append(f"- `{group['content_id']}`")
            lines.extend(f"  - `{path}`" for path in group["paths"])
    else:
        lines.append("None detected.")
    lines += ["", "## PDF inventory", "", "| Path | Bytes | Identifier hint |", "|---|---:|---|"]
    for row in state["items"]:
        if row["kind"] != "paper-pdf":
            continue
        ident = row["identifier"]
        hint = f"{ident.get('scheme', '')}:{ident.get('value', '')}" if ident else ""
        lines.append(f"| `{row['path']}` | {row.get('bytes') or ''} | {hint} |")
    lines += ["", "## Limitations", ""]
    lines.extend(f"- {item}" for item in state["limitations"])
    return "\n".join(lines) + "\n"


def write_if_changed(path: Path, content: str) -> bool:
    if path.exists() and path.read_text(encoding="utf-8") == content:
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8", newline="\n")
    return True


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path("."))
    parser.add_argument("--github-tree-json", type=Path)
    parser.add_argument("--state", type=Path, default=Path("indexes/index-state.json"))
    parser.add_argument("--markdown", type=Path, default=Path("indexes/RESOURCE_INDEX.md"))
    parser.add_argument("--scanned-at", default=None)
    parser.add_argument("--apply", action="store_true", help="Write generated outputs; default is dry-run")
    args = parser.parse_args()

    if args.github_tree_json:
        payload = json.loads(args.github_tree_json.read_text(encoding="utf-8"))
        raw, tree_id, truncated = github_entries(payload)
    else:
        raw, tree_id, truncated = local_entries(args.root.resolve())
    state = make_state(enrich(raw), tree_id, truncated, args.scanned_at or iso_now())
    md = markdown(state)
    print(
        f"files={state['counts']['files']} pdfs={state['counts']['papers_pdf']} "
        f"duplicates={state['counts']['duplicate_content_groups']} tree={tree_id}"
    )
    if not args.apply:
        print("dry-run: no files written")
        return 0
    changed = []
    if write_if_changed(args.root / args.state, json.dumps(state, indent=2, ensure_ascii=False) + "\n"):
        changed.append(args.state.as_posix())
    if write_if_changed(args.root / args.markdown, md):
        changed.append(args.markdown.as_posix())
    print("written: " + (", ".join(changed) if changed else "none (already current)"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
