#!/usr/bin/env python3
"""Build a compact human-facing router plus bounded HSH_RESOURCES catalog shards.

This is a presentation/indexing layer over the reviewed bibliography, reviewed
batch files, provisional bibliography batches, and explicit exclusions. It does
not promote provisional records to reviewed status and does not infer citation
need, relevance, priority, novelty, or scientific validity.
"""
from __future__ import annotations

import argparse
import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(".")
OUTPUT = Path("!_HSH_RESOURCES_INDEX.md")
SHARD_DIR = Path("indexes/human_source_index")
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
        paths: list[str] = []
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


def slug(text: str) -> str:
    value = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return value or "root"


def cell(value: str, limit: int = 360) -> str:
    value = value.replace("|", "\\|").replace("\n", " ").strip()
    if len(value) > limit:
        value = value[: limit - 1].rstrip() + "…"
    return value


def path_cell(paths: list[str]) -> str:
    return "<br>".join(f"[`{cell(p, 170)}`](<../../{p}>)" for p in paths)


def coverage_summary() -> list[str]:
    if not COVERAGE.exists():
        return []
    wanted = (
        "PDF paths in structural index", "Unique PDF content groups", "Reviewed unique-content groups",
        "Provisionally machine-indexed unique-content groups", "Total bibliographically indexed unique-content groups",
        "Explicitly excluded non-bibliographic unique-content groups", "Total accounted unique-content groups",
        "Remaining unresolved unique-content groups",
    )
    return [
        line for line in COVERAGE.read_text(encoding="utf-8", errors="ignore").splitlines()
        if line.startswith("- ") and any(label in line for label in wanted)
    ]


def write_if_changed(path: Path, content: str) -> bool:
    if path.exists() and path.read_text(encoding="utf-8", errors="ignore") == content:
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8", newline="\n")
    return True


def render_shard(folder: str, part_no: int, total_parts: int, entries: list[dict], start_no: int, total_folder: int) -> str:
    end_no = start_no + len(entries) - 1
    out = [
        f"# HSH_RESOURCES — {folder} — Part {part_no} of {total_parts}",
        "",
        f"> Catalog rows **{start_no}–{end_no} of {total_folder}** for `{folder}`. [Return to the human-readable index](../../!_HSH_RESOURCES_INDEX.md).",
        "",
        "`reviewed` = bibliographic identity received human/LLM review. `provisional` = metadata/navigation only and still needs individual review. `excluded` = preserved non-source artifact.",
        "",
        "| Title | Author(s) | ID / date | Source type | Status / read level | Repository path(s) | Description / identity note |",
        "|---|---|---|---|---|---|---|",
    ]
    for e in entries:
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
    out += ["", "[← Return to human-readable index](../../!_HSH_RESOURCES_INDEX.md)", ""]
    return "\n".join(out)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--shard-size", type=int, default=100)
    args = parser.parse_args()
    shard_size = max(10, args.shard_size)

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

    SHARD_DIR.mkdir(parents=True, exist_ok=True)
    for old in SHARD_DIR.glob("*.md"):
        old.unlink()

    router_rows: list[tuple[str, int, list[tuple[str, int, int]]]] = []
    shard_count = 0
    for folder in sorted(grouped, key=str.casefold):
        values = grouped[folder]
        parts: list[tuple[str, int, int]] = []
        total_parts = (len(values) + shard_size - 1) // shard_size
        for part_no, start in enumerate(range(0, len(values), shard_size), 1):
            chunk = values[start:start + shard_size]
            filename = f"{slug(folder)}__{part_no:03d}.md"
            content = render_shard(folder, part_no, total_parts, chunk, start + 1, len(values))
            write_if_changed(SHARD_DIR / filename, content)
            parts.append((filename, start + 1, start + len(chunk)))
            shard_count += 1
        router_rows.append((folder, len(values), parts))

    readme = [
        "# Human-readable source-index shards",
        "",
        f"Generated catalog shards. Each shard contains at most **{shard_size} catalog rows**.",
        "",
        "Start from [`../../!_HSH_RESOURCES_INDEX.md`](../../!_HSH_RESOURCES_INDEX.md), which is the compact router. Do not treat these presentation files as source artifacts or as citation judgments.",
        "",
    ]
    write_if_changed(SHARD_DIR / "README.md", "\n".join(readme))

    out = [
        "# HSH_RESOURCES — Human-Readable Source Index",
        "",
        "> **Start here for people.** This is a compact router into bounded human-readable catalog shards. Source files, machine inventories, extraction manifests, bibliography ledgers, and audit logs remain separate layers.",
        "",
        "No catalog shard contains more than **{} rows**. Large repository areas are automatically divided into multiple parts rather than producing giant Markdown files.".format(shard_size),
        "",
        "This index does **not** imply that a source is correct, relevant to H(s)H, prior art for a specific claim, or an influence on SAT/H(s)H.",
        "",
        "## Coverage at this build",
        "",
    ]
    out += coverage_summary()
    out += [
        "",
        f"Human-facing catalog records: **{len(entries)}** ({reviewed_n} reviewed, {provisional_n} provisional, {excluded_n} explicit non-source exclusions).",
        f"Catalog shards: **{shard_count}**, maximum **{shard_size} rows per shard**.",
        "",
        "## Catalog router",
        "",
        "| Repository area | Records | Catalog shard(s) |",
        "|---|---:|---|",
    ]
    for folder, count, parts in router_rows:
        links = []
        for filename, first, last in parts:
            label = f"{first}–{last}" if first != last else str(first)
            links.append(f"[{label}](indexes/human_source_index/{filename})")
        out.append(f"| {folder.replace('|', '\\|')} | {count} | {' · '.join(links)} |")
    out += [
        "",
        "## Status key",
        "",
        "`reviewed` means bibliographic identity received human/LLM review. `provisional` means identity/navigation was generated from extraction metadata and first-page heuristics and still needs individual review. `excluded` means a preserved archive artifact is not itself a literature/source item.",
        "",
        "For citation decisions use `indexes/HUMAN_BIBLIOGRAPHY.md` and the HsH point-of-use citation ledger. For exact machine coverage use `indexes/BIBLIOGRAPHY_COVERAGE.md` and `indexes/RESOURCE_INDEX.md`.",
        "",
    ]
    changed = write_if_changed(OUTPUT, "\n".join(out))
    print(
        f"human_index_rows={len(entries)} reviewed={reviewed_n} provisional={provisional_n} "
        f"excluded={excluded_n} shards={shard_count} shard_size={shard_size} router_changed={changed}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
