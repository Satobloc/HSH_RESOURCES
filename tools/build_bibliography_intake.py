#!/usr/bin/env python3
"""Build a bibliographic intake queue from extracted PDF text.

This is a candidate-harvesting tool, not a bibliography writer. It extracts
high-value identity hints (title, DOI/arXiv, PDF metadata author/title, dates,
keywords) into a readable queue for human/LLM verification before promotion to
indexes/HUMAN_BIBLIOGRAPHY.md.

Byte-identical PDF copies are treated as one bibliographic lineage. If any path
in a duplicate lineage is already represented in the human bibliography, the
whole lineage is omitted from intake. Otherwise one canonical path is shown and
all duplicate paths are preserved beneath it.
"""
from __future__ import annotations

import argparse
import json
import re
from collections import defaultdict
from pathlib import Path
from typing import Any

DOI_RE = re.compile(r"\b10\.\d{4,9}/[-._;()/:A-Z0-9]+", re.I)
ARXIV_RE = re.compile(r"\b(?:arXiv\s*:\s*)?(\d{4}\.\d{4,5})(v\d+)?\b", re.I)
DATE_RE = re.compile(r"\b(?:19|20)\d{2}[-/.](?:0?[1-9]|1[0-2])[-/.](?:0?[1-9]|[12]\d|3[01])\b")
KEYWORD_RE = re.compile(r"^\s*(?:keywords?|key\s*words?|index\s+terms?)\s*[:—-]\s*(.+)$", re.I)
PAGE_MARKER_RE = re.compile(r"^===== PAGE \d+ =====$")
NOISE_RE = re.compile(
    r"^(?:arxiv|doi|http|www\.|received|accepted|published|copyright|abstract\b|"
    r"eur\.\s*phys\.|mon\.\s*not\.|will be inserted by the editor|preprint|manuscript no\b)",
    re.I,
)


def clean(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip(" \t\r\n.-")


def first_page_lines(text: str) -> list[str]:
    lines = text.splitlines()
    out: list[str] = []
    started = False
    for raw in lines:
        line = raw.strip()
        if PAGE_MARKER_RE.match(line):
            if started:
                break
            started = True
            continue
        if not started:
            continue
        if line:
            out.append(clean(line))
    return out


def title_candidate(lines: list[str], metadata_title: str | None) -> tuple[str | None, str]:
    if metadata_title and len(clean(metadata_title)) >= 8:
        title = clean(metadata_title)
        if title.lower() not in {"untitled", "microsoft word", "document"} and not NOISE_RE.match(title):
            return title, "pdf-metadata"
    for line in lines[:24]:
        if not (18 <= len(line) <= 260):
            continue
        if NOISE_RE.match(line) or DOI_RE.search(line):
            continue
        if len(line.split()) < 3:
            continue
        if line.endswith(":"):
            continue
        return line, "first-page-heuristic"
    return None, "unresolved"


def find_keywords(text: str) -> str | None:
    for raw in text.splitlines()[:250]:
        m = KEYWORD_RE.match(raw)
        if m:
            value = clean(m.group(1))
            return value[:600] if value else None
    return None


def source_identifier(source_path: str, text: str) -> dict[str, str]:
    for m in DOI_RE.finditer(text[:20000]):
        value = m.group(0).rstrip(".,;)]}")
        if value:
            return {"scheme": "doi", "value": value}
    m = ARXIV_RE.search(Path(source_path).name)
    if not m:
        m = ARXIV_RE.search(text[:12000])
    if m:
        return {"scheme": "arxiv", "value": m.group(1) + (m.group(2) or "")}
    return {}


def load_manifest(path: Path) -> list[dict[str, Any]]:
    rows = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            rows.append(json.loads(line))
    return rows


def human_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore") if path.exists() else ""


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--root", type=Path, default=Path("."))
    p.add_argument("--manifest", type=Path, default=Path("derived/manifests/extraction.jsonl"))
    p.add_argument("--human-bib", type=Path, default=Path("indexes/HUMAN_BIBLIOGRAPHY.md"))
    p.add_argument("--output", type=Path, default=Path("indexes/BIBLIOGRAPHY_INTAKE.md"))
    p.add_argument("--max-items", type=int, default=250)
    args = p.parse_args()

    root = args.root.resolve()
    human = human_text(root / args.human_bib)
    rows = [r for r in load_manifest(root / args.manifest) if r.get("status") in {"extracted", "needs_ocr"}]

    by_hash: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        digest = str(row.get("sha256") or row.get("source_path") or "")
        by_hash[digest].append(row)

    records = []
    duplicate_lineages_skipped = 0
    for digest in sorted(by_hash, key=lambda d: min(str(r.get("source_path", "")).casefold() for r in by_hash[d])):
        lineage = sorted(by_hash[digest], key=lambda r: str(r.get("source_path", "")).casefold())
        paths = [str(r.get("source_path")) for r in lineage if r.get("source_path")]
        if any(f"`{path}`" in human for path in paths):
            duplicate_lineages_skipped += 1 if len(paths) > 1 else 0
            continue

        row = lineage[0]
        source = row.get("source_path")
        text_path = row.get("text_path")
        if not source or not text_path:
            continue
        pth = root / text_path
        if not pth.exists():
            continue
        text = pth.read_text(encoding="utf-8", errors="replace")
        lines = first_page_lines(text)
        title, title_basis = title_candidate(lines, row.get("title"))
        ident = source_identifier(source, text)
        dates = []
        for m in DATE_RE.finditer("\n".join(lines[:80])):
            if m.group(0) not in dates:
                dates.append(m.group(0))
        records.append({
            "source_path": source,
            "duplicate_paths": paths[1:],
            "status": row.get("status"),
            "title": title,
            "title_basis": title_basis,
            "author_metadata": clean(str(row.get("author") or "")) or None,
            "identifier": ident,
            "date_hints": dates[:5],
            "keywords": find_keywords(text),
            "pages": row.get("pages"),
            "text_chars": row.get("text_characters_nonspace"),
        })
        if len(records) >= max(args.max_items, 1):
            break

    lines = [
        "# Bibliography Intake Queue",
        "",
        "> Generated candidate metadata for human/LLM verification. Not the bibliography and not evidence of relevance.",
        "",
        f"Candidate unique-content entries shown: **{len(records)}**",
        f"Duplicate lineages already represented in the human bibliography and suppressed here: **{duplicate_lineages_skipped}**",
        "",
    ]
    for i, r in enumerate(records, 1):
        ident = r["identifier"]
        ident_text = f"{ident.get('scheme','').upper()}: `{ident.get('value','')}`" if ident else "unresolved"
        lines += [
            f"## {i}. {r['title'] or '[TITLE UNRESOLVED]'}",
            "",
            f"**Identifier candidate:** {ident_text}  ",
            f"**Author metadata:** {r['author_metadata'] or 'unresolved'}  ",
            f"**Date hints:** {', '.join(r['date_hints']) if r['date_hints'] else 'unresolved'}  ",
            f"**Repository path:** `{r['source_path']}`  ",
        ]
        if r["duplicate_paths"]:
            lines.append("**Duplicate repository paths:** " + "; ".join(f"`{p}`" for p in r["duplicate_paths"]) + "  ")
        lines += [
            f"**Keywords from source:** {r['keywords'] or 'none detected'}  ",
            f"**Extraction:** {r['status']}; {r['pages'] or '?'} pages; {r['text_chars'] or 0} non-space characters  ",
            f"**Title basis:** {r['title_basis']}  ",
            "",
        ]
    (root / args.output).write_text("\n".join(lines), encoding="utf-8", newline="\n")
    print(f"intake_candidates={len(records)} duplicate_lineages_suppressed={duplicate_lineages_skipped} output={args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
