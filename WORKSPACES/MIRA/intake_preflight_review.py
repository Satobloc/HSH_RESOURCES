#!/usr/bin/env python3
"""Mira review-only, deny-by-default PDF identity/clearance preflight.

NEVER opens PDFs, extracts content, changes production state, or dispatches work.
A provisional approval is a human attestation, not independently verified safety.
"""
from __future__ import annotations

import argparse
import json
import re
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

REPO = "Satobloc/HSH_RESOURCES"
SCOPE = "30SEP_PAPER_DUMP"
HEX40 = re.compile(r"^[0-9a-f]{40}$", re.I)
DENY_NAME = re.compile(r"schreiber|hypothesis[ _-]*h(?:\b|[_-])", re.I)
DENY_COMPONENTS = {"prior_art", "quarantine", ".git", "derived"}
REQUIRED_APPROVAL_STRINGS = (
    "reviewer", "original_citation", "canonical_work_id",
    "bibliographic_source", "review_record",
)


class PreflightError(ValueError):
    """Invalid/untrusted metadata: fail closed globally."""


def safe_path(value: Any) -> str:
    if not isinstance(value, str) or not value or "\\" in value or "\x00" in value:
        raise PreflightError("invalid path syntax")
    parts = value.split("/")
    if (value.startswith("/") or any(p in ("", ".", "..") for p in parts)
            or len(parts) < 2 or parts[0] != SCOPE
            or any(p.casefold() in DENY_COMPONENTS for p in parts)):
        raise PreflightError("outside approved intake scope or unsafe path")
    if not value.lower().endswith(".pdf"):
        raise PreflightError("not a PDF path")
    return value


def valid_sha(value: Any) -> bool:
    return isinstance(value, str) and bool(HEX40.fullmatch(value))


def parse_inventory(obj: Any) -> tuple[str, dict[str, dict[str, Any]]]:
    if not isinstance(obj, dict) or obj.get("repository") != REPO or not valid_sha(obj.get("commit")):
        raise PreflightError("inventory has no trusted repository / pinned commit identity")
    files = obj.get("files")
    if not isinstance(files, list):
        raise PreflightError("inventory files must be list")
    entries: dict[str, dict[str, Any]] = {}
    for row in files:
        if not isinstance(row, dict):
            raise PreflightError("malformed inventory row")
        path = safe_path(row.get("path"))
        if path in entries:
            raise PreflightError("duplicate inventory path")
        if not valid_sha(row.get("blob_sha")) or type(row.get("bytes")) is not int or row["bytes"] < 0:
            raise PreflightError("invalid blob identity or size")
        entries[path] = row
    return obj["commit"].lower(), entries


def parse_manifest(rows: Any) -> set[str]:
    if not isinstance(rows, list):
        raise PreflightError("manifest rows must be list")
    out: set[str] = set()
    for row in rows:
        if not isinstance(row, dict) or not isinstance(row.get("source_path"), str):
            raise PreflightError("malformed manifest row")
        path = row["source_path"]
        if path in out:
            raise PreflightError("duplicate manifest source path")
        out.add(path)
    return out


def parse_approvals(obj: Any, commit: str) -> dict[str, dict[str, Any]]:
    if (not isinstance(obj, dict) or obj.get("repository") != REPO
            or str(obj.get("inventory_commit", "")).lower() != commit
            or obj.get("schema_version") != 1 or not isinstance(obj.get("approvals"), list)):
        raise PreflightError("approval envelope missing/version mismatched")
    result: dict[str, dict[str, Any]] = {}
    for row in obj["approvals"]:
        if not isinstance(row, dict):
            raise PreflightError("malformed approval row")
        path = safe_path(row.get("path"))
        if path in result:
            raise PreflightError("duplicate or contradictory approvals")
        if not valid_sha(row.get("blob_sha")) or type(row.get("bytes")) is not int:
            raise PreflightError("malformed approval identity")
        if str(row.get("reviewed_commit", "")).lower() != commit:
            raise PreflightError("approval not bound to pinned inventory commit")
        result[path] = row
    return result


def physical_check(root: Path | None, path: str) -> bool:
    """Check physical location without reading PDF data. No root => no green paths."""
    if root is None:
        return False
    try:
        base = root.resolve(strict=True)
        if not base.is_dir():
            return False
        current = base
        for component in path.split("/"):
            current = current / component
            if current.is_symlink():
                return False
        resolved = current.resolve(strict=True)
        resolved.relative_to(base)
        return resolved.is_file()
    except (OSError, ValueError, RuntimeError):
        return False


def evaluate(inventory: Any, manifest: Any, approved: Any,
             root: Path | None = None) -> dict[str, Any]:
    commit, entries = parse_inventory(inventory)
    existing = parse_manifest(manifest)
    approvals = parse_approvals(approved, commit)
    if any(path not in entries for path in approvals):
        raise PreflightError("approval refers to absent inventory path")
    blob_to_paths: dict[str, list[str]] = defaultdict(list)
    for path, row in entries.items():
        blob_to_paths[row["blob_sha"].lower()].append(path)
    explicitly_approved_blobs = Counter(
        entries[p]["blob_sha"].lower() for p, a in approvals.items()
        if a.get("approved") is True and p not in existing
    )
    results = []
    for path, file in sorted(entries.items()):
        auth = approvals.get(path)
        label = "hold_missing_approval"
        if path in existing:
            label = "already_in_manifest_not_recleared"
        elif DENY_NAME.search(path):
            label = "hold_restricted_name_signal"
        elif auth is not None:
            values_match = (auth.get("blob_sha", "").lower() == file["blob_sha"].lower()
                            and auth.get("bytes") == file["bytes"])
            attestations = (auth.get("approved") is True
                            and auth.get("author_checked") is True
                            and auth.get("restriction_checked") is True)
            citation_fields = all(isinstance(auth.get(k), str) and auth[k].strip()
                                  for k in REQUIRED_APPROVAL_STRINGS)
            unsafe_meta = any(DENY_NAME.search(auth.get(k, ""))
                              for k in REQUIRED_APPROVAL_STRINGS
                              if isinstance(auth.get(k), str))
            if not values_match:
                label = "hold_content_version_mismatch"
            elif unsafe_meta:
                label = "hold_restricted_metadata_signal"
            elif not attestations or not citation_fields:
                label = "hold_incomplete_review"
            elif explicitly_approved_blobs[file["blob_sha"].lower()] > 1:
                label = "hold_multiple_approved_aliases"
            elif not physical_check(root, path):
                label = "hold_physical_containment_unverified"
            else:
                label = "provisional_review_pass_not_extraction_permission"
        results.append({"path": path, "git_blob_sha": file["blob_sha"],
                        "status": label, "alias_count": len(blob_to_paths[file["blob_sha"].lower()])})
    counts = dict(sorted(Counter(r["status"] for r in results).items()))
    return {"mode": "REVIEW_ONLY_NO_PDF_READ", "repository": REPO,
            "pinned_commit": commit, "pdf_paths": len(entries), "counts": counts,
            "results": results}


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def read_jsonl(path: Path) -> list[Any]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines()
            if line.strip()]


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--inventory", required=True, type=Path)
    p.add_argument("--manifest", required=True, type=Path)
    p.add_argument("--approvals", required=True, type=Path)
    p.add_argument("--root", type=Path, help="checked-out trusted repository root; absent means every pending path is held")
    p.add_argument("--output", type=Path, help="optional report JSON; does not write an extractor allowlist")
    args = p.parse_args()
    try:
        report = evaluate(read_json(args.inventory), read_jsonl(args.manifest),
                          read_json(args.approvals), args.root)
    except (OSError, ValueError, KeyError, TypeError) as exc:
        p.exit(2, f"PREFLIGHT_DENIED (no outputs written): {type(exc).__name__}: {exc}\n")
    rendered = json.dumps(report, indent=2, ensure_ascii=False) + "\n"
    if args.output:
        args.output.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
