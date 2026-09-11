#!/usr/bin/env python3
"""Build bounded human-facing HSH_RESOURCES indexes.

The root index is only a router. Records are exposed through four parallel views:
physical folder/subfolder, broad subject tags, first-listed author, and date.
Every record-bearing shard is bounded by --shard-size (default 100).

This is a presentation layer over reviewed/provisional bibliography records. It
does not promote provisional records to reviewed status and does not infer
citation need, priority, novelty, influence, or scientific validity.
"""
from __future__ import annotations

import argparse
import hashlib
import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(".")
OUTPUT = Path("!_HSH_RESOURCES_INDEX.md")
INDEX_DIR = Path("indexes/human_source_index")
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
YEAR_RE = re.compile(r"\b(19\d{2}|20\d{2})\b")

SUBJECT_RULES: list[tuple[str, tuple[str, ...]]] = [
    ("General Relativity & Gravitation", ("general relativity", "gravitation", "gravitational", "gravity", "equivalence principle", "black hole", "kerr", "de sitter", "carroll gravity")),
    ("Quantum Foundations", ("quantum foundation", "bell", "epr", "hidden variable", "measurement problem", "quantum mechanics", "emergent quantum", "wave function", "schrodinger")),
    ("Quantum Field Theory & Particle Physics", ("quantum field", "qft", "yang-mills", "gauge field", "standard model", "particle physics", "fermion", "boson", "dirac", "qed", "electroweak", "higgs", "neutrino")),
    ("Geometry, Topology & Holonomy", ("topology", "topological", "holonomy", "monodromy", "braid", "braiding", "finsler", "minkowski norm", "indicatrix", "manifold", "geometric phase", "differential geometry")),
    ("Strings, Branes & Higher Dimensions", ("string theory", "relativistic string", "nambu-goto", "brane", "kaluza-klein", "supergravity", "calabi-yau", "compactification", "higher-dimensional", "higher dimensional", "supertwistor")),
    ("Cosmology & Astrophysics", ("cosmology", "cosmic", "astrophys", "galaxy", "galactic", "stellar", "solar", "pulsar", "grb", "gamma-ray", "lunar laser", "desi", "dark energy", "early universe")),
    ("Dark Matter & Dark Sectors", ("dark matter", "dark photon", "wimp", "xenon", "lux-zeplin", "lz collaboration", "dark sector")),
    ("Condensed Matter & Topological Phases", ("condensed matter", "anyon", "laughlin", "moore-read", "topological phase", "photonic topological", "superconduct", "quantum hall")),
    ("Mathematics & Mathematical Methods", ("calculus of variations", "functional analysis", "banach", "mahler", "algebra", "clifford", "group theory", "category theory", "tensor", "differential equation", "variational", "theorem", "symplectic")),
    ("Numerical & Computational Methods", ("numerical", "simulation", "computational", "algorithm", "finite element", "monte carlo", "optimization", "notebook", ".ipynb", "python")),
    ("Observational Data & Surveys", ("data release", "survey", "spectral viewer", "spectroscopic", "observational", "dataset", "sparcl", "astro data lab", "catalog")),
    ("Nuclear Physics", ("nuclear", "shell model", "isotope", "hadron", "quark", "proton", "neutron")),
    ("Chemistry & Materials", ("chemistry", "chemical", "periodic table", "material", "lanthan", "calcium", "crystal")),
    ("Biology, Medicine & Applied Statistics", ("mortality", "medical", "health", "biology", "epidemic", "hospital", "clinical", "statistical", "statistics")),
    ("AI, Cognition & Consciousness", ("consciousness", "cognition", "artificial intelligence", "ai", "llm", "language model", "mind", "solonoid")),
    ("Information & Computation", ("information theory", "information-theoretic", "quantum computation", "computation", "entropy", "complexity", "coding")),
    ("Archive, Provenance & Exposure", ("exposure_stats", "spotify for creators", "analytics", "provenance", "plagiarismcheck", "archive-native", "conversation")),
]


def clean_md(value: str) -> str:
    value = value.strip()
    value = re.sub(r"^\*([^*].*?)\*$", r"\1", value)
    return value.replace("  ", " ").strip()


def field_map(block: list[str]) -> dict[str, str]:
    fields: dict[str, str] = {}
    for line in block:
        m = FIELD_RE.match(line.strip())
        if m:
            fields[m.group(1).strip().lower()] = m.group(2).strip()
    return fields


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


def directory_of(path: str) -> str:
    parent = Path(path).parent.as_posix()
    return "Repository root" if parent in (".", "") else parent


def top_folder(path: str) -> str:
    return path.split("/", 1)[0] if "/" in path else "Repository root"


def slug(text: str) -> str:
    value = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return value or "root"


def stable_key(text: str) -> str:
    return f"{slug(text)}-{hashlib.sha1(text.encode('utf-8')).hexdigest()[:6]}"


def cell(value: str, limit: int = 360) -> str:
    value = value.replace("|", "\\|").replace("\n", " ").strip()
    return value if len(value) <= limit else value[: limit - 1].rstrip() + "…"


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


def term_hit(haystack: str, term: str) -> bool:
    term = term.lower()
    if len(term) <= 4 and term.replace("-", "").isalnum():
        return re.search(rf"(?<![a-z0-9]){re.escape(term)}(?![a-z0-9])", haystack) is not None
    return term in haystack


def subject_tags(entry: dict) -> list[str]:
    haystack = " " + " ".join([
        entry["title"], entry["type"], entry["description"], entry["ident"], entry["paths"][0]
    ]).lower() + " "
    tags = [label for label, terms in SUBJECT_RULES if any(term_hit(haystack, term) for term in terms)]
    if not tags:
        tags = ["Other / Unclassified"]
    return tags[:5]


def primary_year(entry: dict) -> str:
    # Prefer an explicitly indexed date. Do not mine arbitrary 4-digit DOI
    # components (for example ApJL's 2041 journal code) as publication years.
    m = YEAR_RE.search(entry.get("date", ""))
    if m:
        return m.group(1)
    arx = re.search(r"arXiv\s*:?\s*`?(\d{2})(\d{2})\.\d+", entry.get("ident", ""), re.I)
    if arx:
        yy = int(arx.group(1))
        return str(2000 + yy if yy < 90 else 1900 + yy)
    return "Unknown"


def first_author_surname(entry: dict) -> str:
    author = entry.get("author", "").strip()
    if not author or author.lower() in {"unresolved", "—", "n"}:
        return "Unknown"
    first = re.split(r";|\band\b", author, maxsplit=1, flags=re.I)[0].strip()
    first = re.sub(r"\bet\s+al\.?$", "", first, flags=re.I).strip()
    if "," in first:
        surname = first.split(",", 1)[0].strip()
    else:
        tokens = re.findall(r"[A-Za-zÀ-ÖØ-öø-ÿ'’-]+", first)
        surname = tokens[-1] if tokens else "Unknown"
    return surname or "Unknown"


def author_bucket(entry: dict) -> str:
    surname = first_author_surname(entry)
    if surname == "Unknown":
        return "# / Unknown"
    c = surname[0].upper()
    return c if "A" <= c <= "Z" else "# / Unknown"


def author_sort_key(entry: dict) -> tuple[str, str, str]:
    return (first_author_surname(entry).casefold(), entry.get("author", "").casefold(), entry["title"].casefold())


def render_records(title: str, note: str, entries: list[dict], start_no: int, total: int) -> str:
    end_no = start_no + len(entries) - 1
    out = [
        f"# {title}",
        "",
        f"> Records **{start_no}–{end_no} of {total}**. {note}",
        "",
        "[← Human-readable index](../../!_HSH_RESOURCES_INDEX.md)",
        "",
        "| Title | Author(s) | ID / date | Subject tag(s) | Source type | Status / read level | Repository path(s) | Description / identity note |",
        "|---|---|---|---|---|---|---|---|",
    ]
    for e in entries:
        iddate = e["ident"]
        if e["date"] and e["date"] not in {"unresolved", "—"}:
            iddate += f"<br>{e['date']}"
        tags = "; ".join(e["subjects"])
        status_read = f"**{e['status']}**<br>{e['read']}<br>record: `{e['record']}`"
        out.append("| " + " | ".join([
            cell(e["title"], 220), cell(e["author"], 180), cell(iddate, 220), cell(tags, 180),
            cell(e["type"], 150), cell(status_read, 260), path_cell(e["paths"]), cell(e["description"], 360),
        ]) + " |")
    out += ["", "[← Human-readable index](../../!_HSH_RESOURCES_INDEX.md)", ""]
    return "\n".join(out)


def write_record_shards(prefix: str, label: str, entries: list[dict], shard_size: int, sort_key) -> list[tuple[str, int, int]]:
    values = sorted(entries, key=sort_key)
    links: list[tuple[str, int, int]] = []
    total_parts = max(1, (len(values) + shard_size - 1) // shard_size)
    for part_no, start in enumerate(range(0, len(values), shard_size), 1):
        chunk = values[start:start + shard_size]
        filename = f"{prefix}__{part_no:03d}.md"
        title = f"HSH_RESOURCES — {label} — Part {part_no} of {total_parts}"
        note = "Subject tags are machine-assigned navigation aids until individually reviewed."
        write_if_changed(INDEX_DIR / filename, render_records(title, note, chunk, start + 1, len(values)))
        links.append((filename, start + 1, start + len(chunk)))
    return links


def links_md(links: list[tuple[str, int, int]]) -> str:
    bits = []
    for filename, first, last in links:
        label = f"{first}–{last}" if first != last else str(first)
        bits.append(f"[{label}]({filename})")
    return " · ".join(bits)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--shard-size", type=int, default=100)
    parser.add_argument("--router-size", type=int, default=100)
    args = parser.parse_args()
    shard_size = max(10, args.shard_size)
    router_size = max(20, args.router_size)

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
    for e in entries:
        e["subjects"] = subject_tags(e)
        e["year"] = primary_year(e)
        e["directory"] = directory_of(e["paths"][0])
        e["top_folder"] = top_folder(e["paths"][0])

    reviewed_n = sum(e["status"] == "reviewed" for e in entries)
    provisional_n = sum(e["status"] == "provisional" for e in entries)
    excluded_n = sum(e["status"] == "excluded" for e in entries)

    INDEX_DIR.mkdir(parents=True, exist_ok=True)
    for old in INDEX_DIR.glob("*.md"):
        old.unlink()

    # 1) Physical folder/subfolder view.
    directory_groups: dict[str, list[dict]] = defaultdict(list)
    for e in entries:
        directory_groups[e["directory"]].append(e)
    directory_links: dict[str, list[tuple[str, int, int]]] = {}
    for directory, values in sorted(directory_groups.items(), key=lambda kv: kv[0].casefold()):
        directory_links[directory] = write_record_shards(
            f"folder-records__{stable_key(directory)}", f"Folder: {directory}", values, shard_size,
            lambda e: (e["title"].casefold(), e["paths"][0].casefold()),
        )

    top_to_dirs: dict[str, list[str]] = defaultdict(list)
    for directory in directory_groups:
        top = "Repository root" if directory == "Repository root" else directory.split("/", 1)[0]
        top_to_dirs[top].append(directory)

    folder_router_rows: list[tuple[str, int, int, list[tuple[str, int, int]]]] = []
    for top in sorted(top_to_dirs, key=str.casefold):
        dirs = sorted(top_to_dirs[top], key=str.casefold)
        map_links = []
        total_parts = max(1, (len(dirs) + router_size - 1) // router_size)
        for part_no, start in enumerate(range(0, len(dirs), router_size), 1):
            chunk = dirs[start:start + router_size]
            filename = f"folder-map__{stable_key(top)}__{part_no:03d}.md"
            lines = [
                f"# Folder map — {top} — Part {part_no} of {total_parts}", "",
                "> Physical repository hierarchy. Each linked record shard is capped at {} records.".format(shard_size), "",
                "[← Human-readable index](../../!_HSH_RESOURCES_INDEX.md)", "",
                "| Directory / subfolder | Records | Catalog shard(s) |", "|---|---:|---|",
            ]
            for d in chunk:
                lines.append(f"| `{d}` | {len(directory_groups[d])} | {links_md(directory_links[d])} |")
            lines += ["", "[← Human-readable index](../../!_HSH_RESOURCES_INDEX.md)", ""]
            write_if_changed(INDEX_DIR / filename, "\n".join(lines))
            map_links.append((filename, start + 1, start + len(chunk)))
        record_count = sum(len(directory_groups[d]) for d in dirs)
        folder_router_rows.append((top, len(dirs), record_count, map_links))

    folder_router = [
        "# Browse by Folder / Subfolder", "",
        "> This is the physical archive view. It preserves the actual containing directory rather than flattening everything to the top-level folder.", "",
        "[← Human-readable index](../../!_HSH_RESOURCES_INDEX.md)", "",
        "| Top-level area | Directories / subfolders | Records | Folder map(s) |", "|---|---:|---:|---|",
    ]
    for top, dir_count, record_count, map_links in folder_router_rows:
        folder_router.append(f"| {top.replace('|', '\\|')} | {dir_count} | {record_count} | {links_md(map_links)} |")
    write_if_changed(INDEX_DIR / "BY_FOLDER.md", "\n".join(folder_router) + "\n")

    # 2) Subject-tag view. Records may appear under multiple subjects.
    subject_groups: dict[str, list[dict]] = defaultdict(list)
    for e in entries:
        for tag in e["subjects"]:
            subject_groups[tag].append(e)
    subject_router = [
        "# Browse by Subject", "",
        "> Broad subject tags are machine-assigned navigation aids. A source may appear under multiple subjects. Tags are not claims of relevance to H(s)H and can be corrected during review.", "",
        "[← Human-readable index](../../!_HSH_RESOURCES_INDEX.md)", "",
        "| Subject | Tagged records | Catalog shard(s) |", "|---|---:|---|",
    ]
    for subject in sorted(subject_groups, key=str.casefold):
        links = write_record_shards(
            f"subject__{stable_key(subject)}", f"Subject: {subject}", subject_groups[subject], shard_size,
            lambda e: (e["title"].casefold(), e["paths"][0].casefold()),
        )
        subject_router.append(f"| {subject.replace('|', '\\|')} | {len(subject_groups[subject])} | {links_md(links)} |")
    write_if_changed(INDEX_DIR / "BY_SUBJECT.md", "\n".join(subject_router) + "\n")

    # 3) Author view, sorted by first-listed author's surname and bucketed A-Z.
    author_groups: dict[str, list[dict]] = defaultdict(list)
    for e in entries:
        author_groups[author_bucket(e)].append(e)
    author_router = [
        "# Browse by Author", "",
        "> Sorted by the surname of the first listed author when recoverable. Group/collaboration or unresolved authors remain under their literal/unknown bucket.", "",
        "[← Human-readable index](../../!_HSH_RESOURCES_INDEX.md)", "",
        "| First-author bucket | Records | Catalog shard(s) |", "|---|---:|---|",
    ]
    buckets = sorted((b for b in author_groups if b != "# / Unknown")) + (["# / Unknown"] if "# / Unknown" in author_groups else [])
    for bucket in buckets:
        links = write_record_shards(
            f"author__{slug(bucket)}", f"Author sort: {bucket}", author_groups[bucket], shard_size, author_sort_key,
        )
        author_router.append(f"| {bucket.replace('|', '\\|')} | {len(author_groups[bucket])} | {links_md(links)} |")
    write_if_changed(INDEX_DIR / "BY_AUTHOR.md", "\n".join(author_router) + "\n")

    # 4) Date view, grouped by primary bibliographic year and newest first.
    year_groups: dict[str, list[dict]] = defaultdict(list)
    for e in entries:
        year_groups[e["year"]].append(e)
    date_router = [
        "# Browse by Date", "",
        "> Grouped by the first recoverable bibliographic year from the indexed date fields or an arXiv identifier. `Unknown` is kept explicit rather than guessed from unrelated numeric identifiers.", "",
        "[← Human-readable index](../../!_HSH_RESOURCES_INDEX.md)", "",
        "| Year | Records | Catalog shard(s) |", "|---|---:|---|",
    ]
    years = sorted((y for y in year_groups if y != "Unknown"), key=int, reverse=True) + (["Unknown"] if "Unknown" in year_groups else [])
    for year in years:
        links = write_record_shards(
            f"date__{slug(year)}", f"Date: {year}", year_groups[year], shard_size,
            lambda e: (e["date"].casefold(), e["title"].casefold()),
        )
        date_router.append(f"| {year} | {len(year_groups[year])} | {links_md(links)} |")
    write_if_changed(INDEX_DIR / "BY_DATE.md", "\n".join(date_router) + "\n")

    readme = [
        "# Human-readable source-index views", "",
        f"Generated navigation layer. Every record-bearing shard contains at most **{shard_size} records**.", "",
        "Start at [`../../!_HSH_RESOURCES_INDEX.md`](../../!_HSH_RESOURCES_INDEX.md). Parallel views are by physical folder/subfolder, broad subject tag, first-listed author, and bibliographic year.", "",
    ]
    write_if_changed(INDEX_DIR / "README.md", "\n".join(readme))

    root = [
        "# HSH_RESOURCES — Human-Readable Source Index", "",
        "> **Start here for people.** This is a compact router; the catalog itself is split into bounded documents rather than one giant file.", "",
        f"No record-bearing catalog document contains more than **{shard_size} records**.", "",
        "## Browse the archive", "",
        "| View | Use it for |", "|---|---|",
        "| [Folder / subfolder](indexes/human_source_index/BY_FOLDER.md) | Follow the actual repository hierarchy down to the containing directory. |",
        "| [Subject](indexes/human_source_index/BY_SUBJECT.md) | Browse broad machine-assigned subject tags; records may appear in more than one subject. |",
        "| [Author](indexes/human_source_index/BY_AUTHOR.md) | Alphabetical first-author browsing. |",
        "| [Date](indexes/human_source_index/BY_DATE.md) | Browse by recoverable bibliographic year, newest first. |", "",
        "## Coverage at this build", "",
    ]
    root += coverage_summary()
    root += [
        "", f"Human-facing catalog records: **{len(entries)}** ({reviewed_n} reviewed, {provisional_n} provisional, {excluded_n} explicit non-source exclusions).", "",
        "### Status and tag discipline", "",
        "`reviewed` means bibliographic identity received human/LLM review. `provisional` means identity/navigation came from extraction metadata and first-page heuristics and still needs individual review. `excluded` means the preserved artifact is not itself a literature/source item.", "",
        "Subject tags are navigation aids, not theory claims. They are machine-assigned until individually reviewed and may be corrected without changing source provenance.", "",
        "For citation decisions use `indexes/HUMAN_BIBLIOGRAPHY.md` and the HsH point-of-use citation ledger. For exact machine coverage use `indexes/BIBLIOGRAPHY_COVERAGE.md` and `indexes/RESOURCE_INDEX.md`.", "",
    ]
    write_if_changed(OUTPUT, "\n".join(root))

    print(
        f"human_index_rows={len(entries)} reviewed={reviewed_n} provisional={provisional_n} excluded={excluded_n} "
        f"directories={len(directory_groups)} subjects={len(subject_groups)} author_buckets={len(author_groups)} years={len(year_groups)} "
        f"shard_size={shard_size}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
