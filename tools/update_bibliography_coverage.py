#!/usr/bin/env python3
"""Build deterministic bibliography coverage accounting for HSH_RESOURCES.

Reports reviewed coverage, provisional machine-index coverage, explicit
non-bibliographic exclusions, and any remaining unresolved groups separately.
It does not decide relevance, citation need, scientific quality, prior-art
status, novelty, or theory authority.
"""
from __future__ import annotations

import argparse
import json
import re
from collections import defaultdict
from pathlib import Path
from typing import Any

DEFAULT_STATE = Path("indexes/index-state.json")
DEFAULT_BIBLIOGRAPHY = Path("indexes/HUMAN_BIBLIOGRAPHY.md")
DEFAULT_BATCH_DIR = Path("indexes/bibliography_batches")
DEFAULT_PROVISIONAL_DIR = Path("indexes/bibliography_provisional")
DEFAULT_EXCLUSIONS = Path("indexes/BIBLIOGRAPHY_EXCLUSIONS.md")
DEFAULT_OUTPUT = Path("indexes/BIBLIOGRAPHY_COVERAGE.md")
HANDOFF_HEADING = "## Citation handoff register"
PATH_RE = re.compile(r"`([^`]+\.pdf)`", re.IGNORECASE)


def load_state(path: Path) -> dict[str, Any]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict) or not isinstance(data.get("items"), list):
        raise ValueError("index state does not contain an items list")
    return data


def source_section(text: str) -> str:
    return text.split(HANDOFF_HEADING, 1)[0] if HANDOFF_HEADING in text else text


def corpus(root: Path, master: Path | None, directory: Path | None, glob: str) -> str:
    docs: list[str] = []
    if master is not None and (root / master).exists():
        docs.append(source_section((root / master).read_text(encoding="utf-8", errors="ignore")))
    if directory is not None and (root / directory).exists():
        for path in sorted((root / directory).glob(glob), key=lambda p: p.name.casefold()):
            docs.append(source_section(path.read_text(encoding="utf-8", errors="ignore")))
    return "\n".join(docs)


def mentioned_paths(text: str) -> set[str]:
    return {m.replace("\\", "/") for m in PATH_RE.findall(text)}


def pdf_rows(state: dict[str, Any]) -> list[dict[str, Any]]:
    return [row for row in state["items"] if row.get("kind") == "paper-pdf"]


def groups(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        key = str(row.get("content_id") or f"path:{row['path']}")
        grouped[key].append(row)
    out = []
    for cid, members in sorted(grouped.items()):
        out.append({"content_id": cid, "members": sorted(members, key=lambda r: r["path"].casefold())})
    return out


def identifier_hint(row: dict[str, Any]) -> str:
    ident = row.get("identifier") or {}
    return f"{ident.get('scheme')}:{ident.get('value')}" if ident.get("scheme") and ident.get("value") else ""


def escape(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", " ")


def build_report(state: dict[str, Any], reviewed_text: str, provisional_text: str, exclusions_text: str) -> str:
    rows = pdf_rows(state)
    known_paths = {row["path"] for row in rows}
    reviewed_exact = mentioned_paths(reviewed_text) & known_paths
    provisional_exact = mentioned_paths(provisional_text) & known_paths
    excluded_exact = mentioned_paths(exclusions_text) & known_paths
    bibliographic_exact = reviewed_exact | provisional_exact
    accounted_exact = bibliographic_exact | excluded_exact

    stale_reviewed = sorted(mentioned_paths(reviewed_text) - known_paths)
    stale_provisional = sorted(mentioned_paths(provisional_text) - known_paths)
    stale_exclusions = sorted(mentioned_paths(exclusions_text) - known_paths)

    all_groups = groups(rows)
    reviewed_groups = []
    provisional_only_groups = []
    excluded_groups = []
    missing_groups = []
    for group in all_groups:
        paths = {row["path"] for row in group["members"]}
        if paths & reviewed_exact:
            reviewed_groups.append(group)
        elif paths & provisional_exact:
            provisional_only_groups.append(group)
        elif paths & excluded_exact:
            excluded_groups.append(group)
        else:
            missing_groups.append(group)

    indexed_total = len(reviewed_groups) + len(provisional_only_groups)
    accounted_total = indexed_total + len(excluded_groups)

    lines = [
        "# HSH Resources — Bibliography Coverage",
        "",
        "> Generated coverage artifact. Reviewed, provisional, excluded, and unresolved layers are reported separately. This does **not** decide relevance, citation need, prior art, novelty, or theory authority.",
        "",
        f"- Structural index scan: `{state.get('scanned_at', 'unknown')}`",
        f"- PDF paths in structural index: **{len(rows)}**",
        f"- Unique PDF content groups: **{len(all_groups)}**",
        f"- Reviewed unique-content groups: **{len(reviewed_groups)}**",
        f"- Provisionally machine-indexed unique-content groups: **{len(provisional_only_groups)}**",
        f"- Total bibliographically indexed unique-content groups: **{indexed_total}**",
        f"- Explicitly excluded non-bibliographic unique-content groups: **{len(excluded_groups)}**",
        f"- Total accounted unique-content groups: **{accounted_total}**",
        f"- Remaining unresolved unique-content groups: **{len(missing_groups)}**",
        f"- Exact PDF paths represented in reviewed + provisional bibliography: **{len(bibliographic_exact)}**",
        f"- Exact PDF paths explicitly excluded as non-bibliographic artifacts: **{len(excluded_exact)}**",
        "",
        "Reviewed corpus: `indexes/HUMAN_BIBLIOGRAPHY.md` plus `indexes/bibliography_batches/BATCH_*.md`.",
        "",
        "Provisional corpus: deterministic `indexes/bibliography_provisional/PROVISIONAL_*.md` files produced only from successfully extracted PDF lineages. Provisional means indexed, not individually reviewed.",
        "",
        "Explicit exclusions: `indexes/BIBLIOGRAPHY_EXCLUSIONS.md`. These remain preserved in the repository but are not literature/source bibliography items.",
        "",
        "Byte-identical copies count as one content lineage when any path in the lineage is represented.",
        "",
        "## Remaining unresolved unique PDF content groups",
        "",
        "| Representative source path | Duplicate paths | Identifier hint |",
        "|---|---:|---|",
    ]
    for group in missing_groups:
        members = group["members"]
        rep = members[0]
        lines.append(f"| `{escape(rep['path'])}` | {len(members)-1} | {escape(identifier_hint(rep))} |")
    if not missing_groups:
        lines.append("| — | 0 | Every currently indexed PDF content group is accounted for as reviewed bibliography, provisional bibliography, or an explicit non-bibliographic exclusion. |")

    lines += ["", "## Bibliography path discrepancies", ""]
    if stale_reviewed or stale_provisional or stale_exclusions:
        if stale_reviewed:
            lines.append("Reviewed corpus paths absent from current structural index:")
            lines.extend(f"- `{p}`" for p in stale_reviewed)
        if stale_provisional:
            lines.append("Provisional corpus paths absent from current structural index:")
            lines.extend(f"- `{p}`" for p in stale_provisional)
        if stale_exclusions:
            lines.append("Exclusion paths absent from current structural index:")
            lines.extend(f"- `{p}`" for p in stale_exclusions)
    else:
        lines.append("No bibliography or exclusion PDF paths fall outside the current structural index.")

    lines += [
        "",
        "## Machine/human boundary",
        "",
        "Provisional coverage closes the machine-indexing backlog without pretending that every source received individual review. Exception batches may preserve unresolved identity fields rather than guess. Metadata correction, neutral description refinement, source reading, H(s)H relationship, and citation-handoff decisions remain review work. Any future extraction/indexing failures are tracked separately in `indexes/BIBLIOGRAPHY_STRAGGLERS.md`.",
        "",
    ]
    return "\n".join(lines)


def write_if_changed(path: Path, content: str) -> bool:
    if path.exists() and path.read_text(encoding="utf-8") == content:
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8", newline="\n")
    return True


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--root", type=Path, default=Path("."))
    p.add_argument("--state", type=Path, default=DEFAULT_STATE)
    p.add_argument("--bibliography", type=Path, default=DEFAULT_BIBLIOGRAPHY)
    p.add_argument("--batch-dir", type=Path, default=DEFAULT_BATCH_DIR)
    p.add_argument("--provisional-dir", type=Path, default=DEFAULT_PROVISIONAL_DIR)
    p.add_argument("--exclusions", type=Path, default=DEFAULT_EXCLUSIONS)
    p.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    p.add_argument("--apply", action="store_true")
    args = p.parse_args()
    root = args.root.resolve()
    state = load_state(root / args.state)
    reviewed = corpus(root, args.bibliography, args.batch_dir, "BATCH_*.md")
    provisional = corpus(root, None, args.provisional_dir, "PROVISIONAL_*.md")
    exclusions_path = root / args.exclusions
    exclusions = exclusions_path.read_text(encoding="utf-8", errors="ignore") if exclusions_path.exists() else ""
    report = build_report(state, reviewed, provisional, exclusions)
    known = {row["path"] for row in pdf_rows(state)}
    print(
        f"pdf_paths={len(known)} reviewed_exact={len(mentioned_paths(reviewed)&known)} "
        f"provisional_exact={len(mentioned_paths(provisional)&known)} excluded_exact={len(mentioned_paths(exclusions)&known)}"
    )
    if not args.apply:
        print("dry-run: no files written")
        return 0
    changed = write_if_changed(root / args.output, report)
    print(f"written={args.output.as_posix()}" if changed else "written=none (already current)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
