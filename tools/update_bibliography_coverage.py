#!/usr/bin/env python3
"""Build deterministic bibliography-coverage accounting for HSH_RESOURCES.

This tool answers one narrow machine question: which structurally indexed PDF
content groups are already represented in the human bibliography corpus, and
which are not? It does NOT decide relevance, citation need, scientific quality,
prior-art status, or theory authority.

The human bibliography corpus consists of indexes/HUMAN_BIBLIOGRAPHY.md plus
reviewed BATCH_*.md files in indexes/bibliography_batches/. Dry-run is the
default. Pass --apply to write indexes/BIBLIOGRAPHY_COVERAGE.md.
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
DEFAULT_OUTPUT = Path("indexes/BIBLIOGRAPHY_COVERAGE.md")
HANDOFF_HEADING = "## Citation handoff register"
PATH_RE = re.compile(r"`([^`]+\.pdf)`", re.IGNORECASE)


def load_state(path: Path) -> dict[str, Any]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict) or not isinstance(data.get("items"), list):
        raise ValueError("index state does not contain an items list")
    return data


def bibliography_source_section(text: str) -> str:
    """Exclude handoff registers so a citation request alone does not count."""
    if HANDOFF_HEADING in text:
        return text.split(HANDOFF_HEADING, 1)[0]
    return text


def bibliography_corpus(root: Path, bibliography: Path, batch_dir: Path) -> str:
    documents: list[str] = []
    master = root / bibliography
    if master.exists():
        documents.append(bibliography_source_section(master.read_text(encoding="utf-8", errors="ignore")))
    directory = root / batch_dir
    if directory.exists():
        for path in sorted(directory.glob("BATCH_*.md"), key=lambda p: p.name.casefold()):
            documents.append(bibliography_source_section(path.read_text(encoding="utf-8", errors="ignore")))
    return "\n".join(documents)


def mentioned_pdf_paths(text: str) -> set[str]:
    return {match.replace("\\", "/") for match in PATH_RE.findall(text)}


def pdf_rows(state: dict[str, Any]) -> list[dict[str, Any]]:
    return [row for row in state["items"] if row.get("kind") == "paper-pdf"]


def content_groups(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        key = str(row.get("content_id") or f"path:{row['path']}")
        grouped[key].append(row)
    groups = []
    for content_id, members in sorted(grouped.items()):
        members = sorted(members, key=lambda row: row["path"].casefold())
        groups.append({"content_id": content_id, "members": members})
    return groups


def identifier_hint(row: dict[str, Any]) -> str:
    ident = row.get("identifier") or {}
    scheme = ident.get("scheme")
    value = ident.get("value")
    return f"{scheme}:{value}" if scheme and value else ""


def escape_cell(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", " ")


def build_report(state: dict[str, Any], bibliography_text: str) -> str:
    rows = pdf_rows(state)
    known_paths = {row["path"] for row in rows}
    mentioned = mentioned_pdf_paths(bibliography_text)
    represented_exact = mentioned & known_paths
    stale_mentions = sorted(mentioned - known_paths)

    groups = content_groups(rows)
    represented_groups = []
    missing_groups = []
    for group in groups:
        paths = {row["path"] for row in group["members"]}
        if paths & represented_exact:
            represented_groups.append(group)
        else:
            missing_groups.append(group)

    lines = [
        "# HSH Resources — Bibliography Coverage",
        "",
        "> Generated structural/coverage artifact. It does **not** decide relevance, citation need, prior art, novelty, or theory authority.",
        "",
        f"- Structural index scan: `{state.get('scanned_at', 'unknown')}`",
        f"- PDF paths in structural index: **{len(rows)}**",
        f"- Unique PDF content groups: **{len(groups)}**",
        f"- Exact indexed PDF paths mentioned in the human bibliography corpus: **{len(represented_exact)}**",
        f"- Unique PDF content groups represented in the human bibliography corpus: **{len(represented_groups)}**",
        f"- Unique PDF content groups not yet represented: **{len(missing_groups)}**",
        "",
        "The human bibliography corpus is `indexes/HUMAN_BIBLIOGRAPHY.md` plus reviewed `indexes/bibliography_batches/BATCH_*.md` files.",
        "",
        "A duplicate file is counted as bibliographically represented when at least one byte-identical path in its content group is represented. This avoids inflating the human backlog with mirrored copies.",
        "",
        "A source can be structurally present yet unprocessed; an unprocessed source is not thereby irrelevant.",
        "",
        "## Unrepresented unique PDF content groups",
        "",
        "| Representative source path | Duplicate paths | Identifier hint |",
        "|---|---:|---|",
    ]

    for group in missing_groups:
        members = group["members"]
        representative = members[0]
        lines.append(
            f"| `{escape_cell(representative['path'])}` | {len(members) - 1} | {escape_cell(identifier_hint(representative))} |"
        )

    if not missing_groups:
        lines.append("| — | 0 | Human bibliography covers every currently indexed PDF content group. |")

    lines += ["", "## Bibliography path discrepancies", ""]
    if stale_mentions:
        lines.append(
            "The following PDF-like paths appear in the human bibliography corpus but are not present in the current structural index. They may be stale paths, cross-repo references, or indexing discrepancies and require human review."
        )
        lines.append("")
        lines.extend(f"- `{path}`" for path in stale_mentions)
    else:
        lines.append("No bibliographic PDF paths fall outside the current structural index.")

    lines += [
        "",
        "## Machine/human boundary",
        "",
        "This report may be regenerated automatically after resource ingest or a reviewed bibliography batch. Metadata recovery, neutral description, reading status, H(s)H relationship, and citation-handoff decisions remain human/LLM-reviewed fields.",
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
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path("."))
    parser.add_argument("--state", type=Path, default=DEFAULT_STATE)
    parser.add_argument("--bibliography", type=Path, default=DEFAULT_BIBLIOGRAPHY)
    parser.add_argument("--batch-dir", type=Path, default=DEFAULT_BATCH_DIR)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--apply", action="store_true", help="write output; default is dry-run")
    args = parser.parse_args()

    root = args.root.resolve()
    state = load_state(root / args.state)
    bibliography_text = bibliography_corpus(root, args.bibliography, args.batch_dir)
    report = build_report(state, bibliography_text)

    represented = len(mentioned_pdf_paths(bibliography_text) & {row["path"] for row in pdf_rows(state)})
    print(f"pdf_paths={len(pdf_rows(state))}; exact_bibliography_paths={represented}")
    if not args.apply:
        print("dry-run: no files written")
        return 0

    changed = write_if_changed(root / args.output, report)
    print(f"written={args.output.as_posix()}" if changed else "written=none (already current)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
