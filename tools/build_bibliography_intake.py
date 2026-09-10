#!/usr/bin/env python3
"""Build a bibliographic intake queue from extracted PDF text.

This is a candidate-harvesting tool, not a bibliography writer. It extracts
high-value identity hints (title, DOI/arXiv, PDF metadata author/title, dates,
keywords) into a readable queue for human/LLM verification before promotion to
indexes/HUMAN_BIBLIOGRAPHY.md.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any

DOI_RE = re.compile(r"\b10\.\d{4,9}/[-._;()/:A-Z0-9]+", re.I)
ARXIV_RE = re.compile(r"\b(?:arXiv\s*:\s*)?(\d{4}\.\d{4,5})(v\d+)?\b", re.I)
DATE_RE = re.compile(r"\b(?:19|20)\d{2}[-/.](?:0?[1-9]|1[0-2])[-/.](?:0?[1-9]|[12]\d|3[01])\b")
KEYWORD_RE = re.compile(r"^\s*(?:keywords?|key\s*words?|index\s+terms?)\s*[:—-]\s*(.+)$", re.I)
PAGE_MARKER_RE = re.compile(r"^===== PAGE \d+ =====$")
NOISE_RE = re.compile(r"^(?:arxiv|doi|http|www\.|received|accepted|published|copyright|abstract\b)", re.I)


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
        if title.lower() not in {"untitled", "microsoft word", "document"}:
            return title, "pdf-metadata"
    # First-page heuristic: favor an early substantial line that is not obvious metadata/noise.
    for line in lines[:18]:
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
    dois = []
    for m in DOI_RE.finditer(text[:20000]):
        value = m.group(0).rstrip(".,;)]}")
        if value not in dois:
            dois.append(value)
    if dois:
        return {"scheme": "doi", "value": dois[0]}
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


def already_in_human_bib(path: Path, source_path: str) -> bool:
    if not path.exists():
        return False
    return f"`{source_path}`" in path.read_text(encoding="utf-8", errors="ignore")


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--root", type=Path, default=Path("."))
    p.add_argument("--manifest", type=Path, default=Path("derived/manifests/extraction.jsonl"))
    p.add_argument("--human-bib", type=Path, default=Path("indexes/HUMAN_BIBLIOGRAPHY.md"))
    p.add_argument("--output", type=Path, default=Path("indexes/BIBLIOGRAPHY_INTAKE.md"))
    p.add_argument("--max-items", type=int, default=250)
    args = p.parse_args()

    root = args.root.resolve()
    human = root / args.human_bib
    records = []
    for row in load_manifest(root / args.manifest):
        if row.get("status") not in {"extracted", "needs_ocr"}:
            continue
        source = row.get("source_path")
        text_path = row.get("text_path")
        if not source or not text_path or already_in_human_bib(human, source):
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
        f"Candidate entries shown: **{len(records)}**",
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
            f"**Keywords from source:** {r['keywords'] or 'none detected'}  ",
            f"**Extraction:** {r['status']}; {r['pages'] or '?'} pages; {r['text_chars'] or 0} non-space characters  ",
            f"**Title basis:** {r['title_basis']}  ",
            "",
        ]
    (root / args.output).write_text("\n".join(lines), encoding="utf-8", newline="\n")
    print(f"intake_candidates={len(records)} output={args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
