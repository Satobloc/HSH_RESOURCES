#!/usr/bin/env python3
"""Build the human-facing HSH_RESOURCES catalog.

This is a presentation/indexing layer over the reviewed bibliography, reviewed
batch files, provisional bibliography batches, and explicit exclusions. It does
not promote provisional records to reviewed status and does not infer citation
need, relevance, priority, novelty, or scientific validity.
"""
from __future__ import annotations

import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(".")
OUTPUT = Path("!_HSH_RESOURCES_INDEX.md")
MASTER = Path("indexes/HUMAN_BIBLIOGRAPHY.md")
REVIEWED_DIR = Path("indexes/bibliography_batches")
PROVISIONAL_DIR = Path("indexes/bibliography_provisional")
EXCLUSIONS = Path("indexes/BIBLIOGRAPHY_EXCLUSIONS.md")
COVERAGE = Path("indexes/BIBLIOGRAPHY_COVERAGE.md")
PATH_RE = re.compile(r"`([^`]+\.pdf)`", re.I)
FIELD_RE = re.compile(r"^\*\*(.+?):\*\*\s*(.*?)(?:\s{2})?$")
MASTER_ENTRY_RE = re.compile(r"^###\s+\d+\.\s+(.+)$")
BATCH_ENTRY_RE = re.compile(r"^##\s+(?:B\d{4}-\d{3}\s+—\s+|\d+\.\s+)(.+)$")
PROV_ENTRY_RE = re.compile(r"^##\s+\d+\.\s+(.+)$")


def clean_md(value: str) -> str:
    value = value.strip()
    value = re.sub(r"^\*([^*].*?)\*$", r"\1", value)
    value = value.replace("  ", " ")
    return value.strip()


def field_map(block: list[str]) -> dict[str, str]:
    fields: dict[str, str] = {}
    for line in block:
        m = FIELD_RE.match(line.strip())
        if m:
            fields[m.group(1).strip().lower()] = m.group(2).strip()
    return fields


def parse_entries(path: Path, kind: str) -> list[dict]:
    text = path.read_text(encoding="utf-8", errors="ignore")
    lines = text.splitlines()
    entry_re = MASTER_ENTRY_RE if kind == "master" else PROV_ENTRY_RE if kind == "provisional" else BATCH_ENTRY_RE
    starts: list[tuple[int, str]] = []
    for i, line in enumerate(lines):
        m = entry_re.match(line)
        if m:
            starts.append((i, clean_md(m.group(1))))
    out: list[dict] = []
    for pos, (start, title) in enumerate(starts):
        end = starts[pos + 1][0] if pos + 1 < len(starts) else len(lines)
        block = lines[start:end]
        fields = field_map(block)
        paths = []
        for p in PATH_RE.findall("\n".join(block)):
            p = p.replace("\\", "/")
            if p not in paths:
                paths.append(p)
        if not paths:
            continue
        author = (
            fields.get("author(s)") or fields.get("authors") or fields.get("author")
            or fields.get("author metadata") or fields.get("author / source") or "unresolved"
        )
        ident = fields.get("bibliographic id") or fields.get("identifier") or "unresolved"
        date = fields.get("date / publication") or fields.get("date") or fields.get("date hints") or "unresolved"
        source_type = fields.get("source type") or "PDF resource"
        read = fields.get("read / coverage") or fields.get("read level") or "not individually reviewed"
        desc = fields.get("neutral description") or fields.get("summary") or ""
        notes = fields.get("notes") or ""
        status = "provisional" if kind == "provisional" else "reviewed"
        if kind == "master":
            status = "reviewed"
        if not desc or desc.lower().startswith("pending"):
            if status == "provisional":
                keywords = fields.get("keywords from source") or fields.get("keywords") or ""
                if keywords and keywords.lower() != "none detected":
                    desc = f"Metadata-only record; source keywords: {keywords}"
                else:
                    desc = "Metadata-only record; concise description pending individual review."
            elif notes:
                desc = notes
            else:
                desc = "Bibliographic identity recorded; concise description pending review."
        out.append({
            "title": title,
            "author": clean_md(author),
            "ident": clean_md(ident),
            "date": clean_md(date),
            "type": infer_type(paths[0], title, ident, source_type),
            "status": status,
            "read": clean_md(read),
            "description": clean_md(desc),
            "paths": paths,
            "record": path.as_posix(),
        })
    return out


def infer_type(path: str, title: str, ident: str, existing: str) -> str:
    low = (path + " " + title + " " + ident).lower()
    if existing and existing.lower() != "pdf resource":
        return clean_md(existing)
    if "spotify for creators" in low or "analytics" in low:
        return "Analytics / exposure record"
    if "desi spectral viewer" in low:
        return "Observational-data capture"
    if "notebook" in low or ".ipynb" in low or "sparcl" in low:
        return "Scientific notebook / technical resource"
    if path.startswith("DATA/"):
        return "Dataset / data-analysis resource"
    if path.startswith("EXPOSURE_STATS/"):
        return "Exposure / provenance resource"
    if path.startswith("Consciousness + AI/"):
        return "Archive-native transcript / document"
    if "arxiv" in low or "ssrn" in low or path.startswith("PRIOR_ART/"):
        return "Research paper / preprint"
    return "Research/document PDF"


def parse_exclusions(path: Path) -> list[dict]:
    if not path.exists():
        return []
    text = path.read_text(encoding="utf-8", errors="ignore")
    items = []
    for p in PATH_RE.findall(text):
        p = p.replace("\\", "/")
        items.append({
            "title": Path(p).stem,
            "author": "—",
            "ident": "—",
            "date": "—",
            "type": "Non-bibliographic archive artifact",
            "status": "excluded",
            "read": "archive-role classification",
            "description": "Preserved in repository but explicitly excluded from the literature/source bibliography.",
            "paths": [p],
            "record": path.as_posix(),
        })
    return items


def top_folder(path: str) -> str:
    return path.split("/", 1)[0] if "/" in path else "Repository root"


def anchor(text: str) -> str:
    a = re.sub(r"[^a-z0-9 -]", "", text.lower())
    return re.sub(r"\s+", "-", a.strip())


def cell(value: str, limit: int = 360) -> str:
    value = value.replace("|", "\\|").replace("\n", " ").strip()
    if len(value) > limit:
        value = value[: limit - 1].rstrip() + "…"
    return value


def path_cell(paths: list[str]) -> str:
    bits = []
    for p in paths:
        # Angle-bracket destination keeps spaces readable in GitHub Markdown.
        bits.append(f"[`{cell(p, 170)}`](<{p}>)")
    return "<br>".join(bits)


def coverage_summary() -> list[str]:
    if not COVERAGE.exists():
        return []
    wanted = (
        "PDF paths in structural index", "Unique PDF content groups", "Reviewed unique-content groups",
        "Provisionally machine-indexed unique-content groups", "Total bibliographically indexed unique-content groups",
        "Explicitly excluded non-bibliographic unique-content groups", "Total accounted unique-content groups",
        "Remaining unresolved unique-content groups",
    )
    found = []
    for line in COVERAGE.read_text(encoding="utf-8", errors="ignore").splitlines():
        if line.startswith("- ") and any(label in line for label in wanted):
            found.append(line)
    return found


def main() -> int:
    entries: list[dict] = []
    if MASTER.exists():
        entries += parse_entries(MASTER, "master")
    if REVIEWED_DIR.exists():
        for path in sorted(REVIEWED_DIR.glob("BATCH_*.md"), key=lambda p: p.name.casefold()):
            entries += parse_entries(path, "reviewed")
    if PROVISIONAL_DIR.exists():
        for path in sorted(PROVISIONAL_DIR.glob("PROVISIONAL_*.md"), key=lambda p: p.name.casefold()):
            entries += parse_entries(path, "provisional")
    entries += parse_exclusions(EXCLUSIONS)

    # If a path appears in more than one presentation layer, keep the strongest record.
    rank = {"reviewed": 3, "provisional": 2, "excluded": 1}
    by_primary: dict[str, dict] = {}
    for entry in entries:
        primary = entry["paths"][0]
        old = by_primary.get(primary)
        if old is None or rank[entry["status"]] > rank[old["status"]]:
            by_primary[primary] = entry
    entries = list(by_primary.values())

    grouped: dict[str, list[dict]] = defaultdict(list)
    for entry in entries:
        grouped[top_folder(entry["paths"][0])].append(entry)
    for values in grouped.values():
        values.sort(key=lambda e: (e["title"].casefold(), e["paths"][0].casefold()))

    reviewed_n = sum(e["status"] == "reviewed" for e in entries)
    provisional_n = sum(e["status"] == "provisional" for e in entries)
    excluded_n = sum(e["status"] == "excluded" for e in entries)

    out = [
        "# HSH_RESOURCES — Human-Readable Source Index",
        "",
        "> **Start here for people.** This is the consolidated navigation catalog for source material in this repository. The machine inventory, extraction manifests, bibliography ledgers, and audit logs remain separate supporting layers.",
        "",
        "This index does **not** imply that a source is correct, relevant to H(s)H, prior art for a specific claim, or an influence on SAT/H(s)H. It preserves the reviewed/provisional distinction explicitly.",
        "",
        "## Coverage at this build",
        "",
    ]
    out += coverage_summary()
    out += [
        "",
        f"Catalog rows in this human-facing view: **{len(entries)}** ({reviewed_n} reviewed records, {provisional_n} provisional records, {excluded_n} explicit non-source exclusions). Multiple byte-identical or bibliographically duplicate repository paths can appear in one row.",
        "",
        "**Status key:** `reviewed` = bibliographic identity received human/LLM review; `provisional` = identity/navigation generated from extraction metadata and first-page heuristics and still needs individual review; `excluded` = preserved archive artifact that is not itself a literature/source item.",
        "",
        "For citation decisions, use `indexes/HUMAN_BIBLIOGRAPHY.md` and the HsH point-of-use citation ledger. For exact machine coverage, use `indexes/BIBLIOGRAPHY_COVERAGE.md` and `indexes/RESOURCE_INDEX.md`.",
        "",
        "## Quick navigation",
        "",
    ]
    for folder in sorted(grouped, key=str.casefold):
        out.append(f"- [{folder}](#{anchor(folder)}) — {len(grouped[folder])} catalog row(s)")

    for folder in sorted(grouped, key=str.casefold):
        out += [
            "",
            f"## {folder}",
            "",
            "| Title | Author(s) | ID / date | Source type | Status / read level | Repository path(s) | Description / identity note |",
            "|---|---|---|---|---|---|---|",
        ]
        for e in grouped[folder]:
            iddate = e["ident"]
            if e["date"] and e["date"] != "unresolved":
                iddate += f"<br>{e['date']}"
            status_read = f"**{e['status']}**<br>{e['read']}<br>record: `{e['record']}`"
            out.append(
                "| " + " | ".join([
                    cell(e["title"], 220), cell(e["author"], 180), cell(iddate, 220),
                    cell(e["type"], 150), cell(status_read, 260), path_cell(e["paths"]),
                    cell(e["description"], 360),
                ]) + " |"
            )

    out += [
        "",
        "## Reading this index",
        "",
        "The catalog is intentionally broad. A provisional row is useful for finding and identifying a source, but should not be cited or used for priority adjudication solely on the basis of this index. Upgrade a source through the reviewed bibliography layer when title/author/identifier/description or H(s)H relationship matters to an argument.",
        "",
        "The exact repository path is retained at point of use so a reader can move from this human-facing catalog directly to the preserved source file, while the originating bibliography-record file is also shown in the status column.",
        "",
    ]
    content = "\n".join(out)
    changed = not OUTPUT.exists() or OUTPUT.read_text(encoding="utf-8", errors="ignore") != content
    if changed:
        OUTPUT.write_text(content, encoding="utf-8", newline="\n")
    print(f"human_index_rows={len(entries)} reviewed={reviewed_n} provisional={provisional_n} excluded={excluded_n} changed={changed}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
