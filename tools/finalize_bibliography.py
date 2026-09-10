#!/usr/bin/env python3
"""Finalize clean bibliography indexing into deterministic provisional batches.

Reviewed bibliography batches remain the high-confidence human/LLM-reviewed layer.
This tool indexes every other successfully extracted PDF lineage into bounded
PROVISIONAL_*.md files using extraction metadata and first-page heuristics only.
It also writes a straggler report for lineages that cannot yet be indexed from
available extraction state. Explicit non-bibliographic exclusions are respected.
Provisional indexing is not review and is not a citation/relevance/prior-art judgment.
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
NOISE_RE = re.compile(r"^(?:arxiv|doi|http|www\.|received|accepted|published|copyright|abstract\b|eur\.\s*phys\.|mon\.\s*not\.|will be inserted by the editor|prepared for submission|preprint|manuscript no\b)", re.I)
PATH_RE = re.compile(r"`([^`]+\.pdf)`", re.I)
HANDOFF_HEADING = "## Citation handoff register"
EXCLUSIONS_FILE = Path("indexes/BIBLIOGRAPHY_EXCLUSIONS.md")


def clean(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip(" \t\r\n.-")


def first_page_lines(text: str) -> list[str]:
    out: list[str] = []
    started = False
    for raw in text.splitlines():
        line = raw.strip()
        if PAGE_MARKER_RE.match(line):
            if started:
                break
            started = True
            continue
        if started and line:
            out.append(clean(line))
    return out


def title_candidate(lines: list[str], metadata_title: str | None, source_path: str) -> tuple[str, str]:
    if metadata_title:
        title = clean(metadata_title)
        if len(title) >= 8 and title.lower() not in {"untitled", "microsoft word", "document"} and not NOISE_RE.match(title):
            return title, "pdf-metadata"
    for line in lines[:30]:
        if 12 <= len(line) <= 260 and len(line.split()) >= 2 and not NOISE_RE.match(line) and not DOI_RE.search(line) and not line.endswith(":"):
            return line, "first-page-heuristic"
    return Path(source_path).stem, "repository-filename"


def find_keywords(text: str) -> str | None:
    for raw in text.splitlines()[:300]:
        m = KEYWORD_RE.match(raw)
        if m:
            value = clean(m.group(1))
            return value[:600] if value else None
    return None


def source_identifier(source_path: str, text: str) -> tuple[str, str] | None:
    m = ARXIV_RE.search(Path(source_path).name)
    if m:
        return "arXiv", m.group(1) + (m.group(2) or "")
    for m in DOI_RE.finditer(text[:25000]):
        value = m.group(0).rstrip(".,;)]}")
        if value:
            return "DOI", value
    m = ARXIV_RE.search(text[:15000])
    if m:
        return "arXiv", m.group(1) + (m.group(2) or "")
    return None


def bibliography_source_section(text: str) -> str:
    return text.split(HANDOFF_HEADING, 1)[0] if HANDOFF_HEADING in text else text


def reviewed_corpus(root: Path) -> str:
    docs: list[str] = []
    master = root / "indexes/HUMAN_BIBLIOGRAPHY.md"
    if master.exists():
        docs.append(bibliography_source_section(master.read_text(encoding="utf-8", errors="ignore")))
    batch_dir = root / "indexes/bibliography_batches"
    if batch_dir.exists():
        for path in sorted(batch_dir.glob("BATCH_*.md"), key=lambda p: p.name.casefold()):
            docs.append(path.read_text(encoding="utf-8", errors="ignore"))
    return "\n".join(docs)


def excluded_paths(root: Path) -> set[str]:
    path = root / EXCLUSIONS_FILE
    if not path.exists():
        return set()
    return {p.replace("\\", "/") for p in PATH_RE.findall(path.read_text(encoding="utf-8", errors="ignore"))}


def load_manifest(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            rows.append(json.loads(line))
    return rows


def load_state(path: Path) -> dict[str, Any]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict) or not isinstance(data.get("items"), list):
        raise ValueError("index state does not contain an items list")
    return data


def md_safe(value: str) -> str:
    return value.replace("\n", " ").strip()


def build_entry(index: int, representative: dict[str, Any], paths: list[str], text: str) -> str:
    source = str(representative.get("source_path") or paths[0])
    lines = first_page_lines(text)
    title, title_basis = title_candidate(lines, representative.get("title"), source)
    ident = source_identifier(source, text)
    dates: list[str] = []
    for m in DATE_RE.finditer("\n".join(lines[:100])):
        if m.group(0) not in dates:
            dates.append(m.group(0))
    author = clean(str(representative.get("author") or "")) or "unresolved"
    keywords = find_keywords(text) or "none detected"
    out = [
        f"## {index}. {md_safe(title)}",
        "",
        "**Status:** provisional machine index; not individually reviewed  ",
        "**Source type:** PDF resource  ",
        f"**Identifier:** {(ident[0] + ': `' + ident[1] + '`') if ident else 'unresolved'}  ",
        f"**Author metadata:** {md_safe(author)}  ",
        f"**Date hints:** {', '.join(dates[:5]) if dates else 'unresolved'}  ",
        f"**Repository path:** `{source}`  ",
    ]
    duplicates = [p for p in paths if p != source]
    if duplicates:
        out.append("**Duplicate repository paths:** " + "; ".join(f"`{p}`" for p in duplicates) + "  ")
    out += [
        f"**Keywords from source:** {md_safe(keywords)}  ",
        f"**Extraction:** extracted; {representative.get('pages') or '?'} pages; {representative.get('text_characters_nonspace') or 0} non-space characters  ",
        f"**Title basis:** {title_basis}  ",
        "**Read level:** machine extraction metadata + first-page heuristic only; no claim-level reading implied  ",
        "",
    ]
    return "\n".join(out)


def write_if_changed(path: Path, text: str) -> bool:
    if path.exists() and path.read_text(encoding="utf-8") == text:
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")
    return True


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--root", type=Path, default=Path("."))
    p.add_argument("--batch-size", type=int, default=50)
    args = p.parse_args()
    root = args.root.resolve()
    batch_size = max(1, args.batch_size)

    manifest = load_manifest(root / "derived/manifests/extraction.jsonl")
    state = load_state(root / "indexes/index-state.json")
    reviewed = reviewed_corpus(root)
    reviewed_paths = {p.replace("\\", "/") for p in PATH_RE.findall(reviewed)}
    exclusions = excluded_paths(root)
    accounted_paths = reviewed_paths | exclusions

    by_hash: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in manifest:
        key = str(row.get("sha256") or row.get("source_path") or "")
        by_hash[key].append(row)

    provisional: list[tuple[dict[str, Any], list[str], str]] = []
    stragglers: list[tuple[str, list[str], str]] = []
    manifest_paths: set[str] = set()

    for key in sorted(by_hash, key=lambda k: min(str(r.get("source_path", "")).casefold() for r in by_hash[k])):
        lineage = sorted(by_hash[key], key=lambda r: str(r.get("source_path", "")).casefold())
        paths = [str(r.get("source_path")) for r in lineage if r.get("source_path")]
        manifest_paths.update(paths)
        if set(paths) & accounted_paths:
            continue
        extracted = [r for r in lineage if r.get("status") == "extracted" and r.get("text_path")]
        if extracted:
            rep = extracted[0]
            text_path = root / str(rep["text_path"])
            if text_path.exists():
                provisional.append((rep, paths, text_path.read_text(encoding="utf-8", errors="replace")))
                continue
            stragglers.append(("missing derived text", paths, str(rep.get("text_path"))))
            continue
        statuses = sorted({str(r.get("status") or "unknown") for r in lineage})
        stragglers.append(("extraction not clean", paths, ", ".join(statuses)))

    structural_pdf_paths = {str(row.get("path")) for row in state["items"] if row.get("kind") == "paper-pdf" and row.get("path")}
    for path in sorted(structural_pdf_paths - manifest_paths, key=str.casefold):
        if path not in accounted_paths:
            stragglers.append(("no extraction-manifest record", [path], "structurally indexed PDF"))

    out_dir = root / "indexes/bibliography_provisional"
    out_dir.mkdir(parents=True, exist_ok=True)
    for old in out_dir.glob("PROVISIONAL_*.md"):
        old.unlink()

    readme = """# Provisional bibliography batches

These files are deterministic machine-generated bibliographic indexing, not the reviewed human bibliography.

A provisional entry means the PDF lineage was successfully extracted and received source identity hints from PDF metadata, repository naming, and/or the first extracted page. It does **not** mean the source was individually read or verified, and it carries no judgment about relevance, citation need, prior art, novelty, authority, or scientific validity.

Reviewed bibliography remains in `indexes/HUMAN_BIBLIOGRAPHY.md` and `indexes/bibliography_batches/BATCH_*.md`. Explicit non-source exclusions are recorded in `indexes/BIBLIOGRAPHY_EXCLUSIONS.md`.

Provisional batches are bounded at 50 unique-content lineages by default. Byte-identical repository copies are collapsed into one entry while retaining all known paths.
"""
    write_if_changed(out_dir / "README.md", readme)

    for batch_no, start in enumerate(range(0, len(provisional), batch_size), 1):
        chunk = provisional[start:start + batch_size]
        header = [
            f"# Provisional bibliography batch {batch_no:04d}",
            "",
            f"Unique-content lineages: **{len(chunk)}**",
            "",
            "> Machine-indexed from successful extraction state. Not individually reviewed.",
            "",
        ]
        body = [build_entry(i, rep, paths, text) for i, (rep, paths, text) in enumerate(chunk, 1)]
        write_if_changed(out_dir / f"PROVISIONAL_{batch_no:04d}.md", "\n".join(header + body).rstrip() + "\n")

    s_lines = [
        "# Bibliography Stragglers",
        "",
        "> Generated cleanup queue. These lineages are neither bibliographically represented nor explicitly classified as non-source exclusions.",
        "",
        f"Straggler lineages/items: **{len(stragglers)}**",
        "",
        "| Reason | Repository path(s) | Detail |",
        "|---|---|---|",
    ]
    for reason, paths, detail in stragglers:
        path_text = "; ".join(f"`{p}`" for p in paths)
        s_lines.append(f"| {reason} | {path_text} | {str(detail).replace('|', '\\|')} |")
    if not stragglers:
        s_lines.append("| — | — | No bibliography stragglers remain. |")
    s_lines += [
        "",
        f"Explicit non-bibliographic exclusions tracked separately: **{len(exclusions)} path(s)** in `indexes/BIBLIOGRAPHY_EXCLUSIONS.md`.",
        "",
    ]
    write_if_changed(root / "indexes/BIBLIOGRAPHY_STRAGGLERS.md", "\n".join(s_lines))

    print(f"reviewed_paths={len(reviewed_paths)} excluded_paths={len(exclusions)} provisional_lineages={len(provisional)} batches={(len(provisional)+batch_size-1)//batch_size} stragglers={len(stragglers)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
