#!/usr/bin/env python3
"""Build the canonical cross-repository podcast source/episode index.

This tool is deliberately mechanical. It discovers likely podcast/transcript/
analytics source material across the three SAT/H(s)H repositories, preserves
source provenance, extracts searchable text from transcript-like sources, and
builds a conservative logical episode registry.

It does NOT decide theory truth, canonical SAT status, influence, or semantic
corrections. PRIOR_ART is pruned before traversal.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import subprocess
from collections import defaultdict
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable

VERSION = "cross-podcast-guide/0.1.0"

REPO_LABELS = {
    "resources": "Satobloc/HSH_RESOURCES",
    "hsh": "Satobloc/HsH",
    "archive": "Satobloc/SAT_THEORY_ARCHIVE_2023-25",
}

# Discovery terms are intentionally path/name oriented. Content is not scanned
# merely to decide whether a file belongs in the podcast corpus.
PATH_TERMS = (
    "podcast", "podcast_ep", "podcast eps", "podcast stats", "episode",
    "exposure_stats", "exposure stats", "debatinga.i", "debating a.i",
    "the new physics", "field notes",
)
TRANSCRIPT_TERMS = (
    "transcript", "field notes", "first public mention", "subtitle",
    "captions", "closed caption", "dai_transcripts",
)
ANALYTICS_TERMS = (
    "analytics", "listener", "listenership", "ranking", "rankings",
    "geolocation", "audience", "streams", "starts", "spotify", "podlod",
    "podlode", "stats",
)
AGGREGATE_NAMES = {
    "dai_transcripts_text.txt",
    "comp_fieldnotes_full_test.txt",
}
TEXT_EXTS = {".txt", ".md", ".srt", ".vtt"}
DATA_EXTS = {".csv", ".json", ".tsv", ".xlsx"}
IMAGE_EXTS = {".png", ".jpg", ".jpeg", ".webp"}
QUARANTINE_PARTS = {"prior_art"}

DATE_PATTERNS = [
    re.compile(r"(?im)^Published:\s*([A-Z][a-z]+\s+\d{1,2},\s+\d{4})(?:\s+at\s+[^\n]+)?$"),
    re.compile(r"(?im)^Published Date:\s*([A-Z][a-z]+\s+\d{1,2},\s+\d{4})$"),
    re.compile(r"(?im)^Release Date:\s*([A-Z][a-z]+\s+\d{1,2},\s+\d{4})$"),
]

RIGOR_PAT = re.compile(
    r"\b(rigor|rigorous|rigorously|validation|falsification|verification|proof|"
    r"audit|criteria|canonical|accepted|tentative|speculative|independent|blind|"
    r"provenance)\b",
    re.I,
)
INSIGHT_PAT = re.compile(
    r"\b(you asked(?: us)? (?:to|for)|our job is to|secondary mission|"
    r"read between the lines|identify additional (?:insights|convergences)|"
    r"find additional (?:insights|convergences)|determine additional)\b",
    re.I,
)
FIELD_PAT = re.compile(r"\b(?:field theory|twist field|scalar field|field)\b", re.I)


@dataclass
class Source:
    source_id: str
    repository: str
    repo_key: str
    path: str
    kind: str
    extension: str
    bytes: int
    sha256: str
    git_blob: str
    duplicate_group: str
    title_candidate: str
    published_date_candidate: str
    public_exposure_evidence: bool
    rigor_signal: bool
    insight_generation_requested: bool
    terminology_hazard_field: bool
    derived_text_path: str
    cue_jsonl_path: str


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def git_commit(root: Path) -> str:
    try:
        return subprocess.check_output(
            ["git", "-C", str(root), "rev-parse", "HEAD"], text=True
        ).strip()
    except Exception:
        return ""


def git_blob(root: Path, rel: str) -> str:
    try:
        out = subprocess.check_output(
            ["git", "-C", str(root), "ls-files", "-s", "--", rel], text=True
        ).strip()
        if out:
            return out.split()[1]
    except Exception:
        pass
    return ""


def norm(s: str) -> str:
    s = s.casefold().replace("…", "...").replace("’", "'")
    s = re.sub(r"[^a-z0-9]+", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def safe_slug(s: str, limit: int = 90) -> str:
    x = re.sub(r"[^A-Za-z0-9]+", "-", s).strip("-").lower()
    return (x[:limit].rstrip("-") or "untitled")


def is_quarantined(rel: Path) -> bool:
    return any(part.casefold() in QUARANTINE_PARTS for part in rel.parts)


def discovery_candidate(rel: Path) -> bool:
    hay = rel.as_posix().casefold().replace("_", " ")
    return any(t in hay for t in PATH_TERMS)


def classify(rel: Path) -> str:
    name = rel.name.casefold().replace("_", " ")
    ext = rel.suffix.casefold()
    if ext in {".srt", ".vtt"}:
        return "transcript_subtitle"
    if any(t in name for t in TRANSCRIPT_TERMS) and ext in TEXT_EXTS:
        return "transcript_text"
    if any(t in name for t in ANALYTICS_TERMS) and ext in (DATA_EXTS | TEXT_EXTS | IMAGE_EXTS):
        return "analytics"
    if ext in IMAGE_EXTS:
        return "analytics_capture"
    if ext in DATA_EXTS:
        return "metadata_or_analytics"
    if ext in TEXT_EXTS:
        return "podcast_text_unspecified"
    return "podcast_other"


def title_from_filename(path: Path) -> str:
    stem = path.stem
    stem = re.sub(r"^(FULL_|TRANSCRIPT_|PODCAST[_ -]*)+", "", stem, flags=re.I)
    stem = re.sub(r"^(The New Physics|DebatingA\.I\.)\s*[-_:]*\s*", "", stem, flags=re.I)
    stem = stem.replace("_", " ")
    return re.sub(r"\s+", " ", stem).strip()


def source_date(text: str) -> str:
    for pat in DATE_PATTERNS:
        m = pat.search(text[:8000])
        if m:
            try:
                return datetime.strptime(m.group(1), "%B %d, %Y").date().isoformat()
            except ValueError:
                pass
    return ""


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def parse_srt_vtt(text: str) -> list[dict]:
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    blocks = re.split(r"\n{2,}", text.strip())
    cues = []
    for block in blocks:
        lines = [x for x in block.splitlines() if x.strip()]
        if not lines:
            continue
        if lines[0].strip().upper() == "WEBVTT":
            lines = lines[1:]
        if not lines:
            continue
        if re.fullmatch(r"\d+", lines[0].strip()):
            lines = lines[1:]
        if not lines:
            continue
        ti = next((i for i, x in enumerate(lines) if "-->" in x), None)
        if ti is None:
            continue
        a, b = [x.strip() for x in lines[ti].split("-->", 1)]
        body = "\n".join(lines[ti + 1:]).strip()
        if not body:
            continue
        cues.append({
            "cue_index": len(cues) + 1,
            "start": a,
            "end": b,
            "speaker": None,
            "text": body,
            "raw_text": body,
        })
    return cues


def subtitle_to_text(cues: list[dict]) -> str:
    out = []
    prev = None
    for cue in cues:
        s = re.sub(r"\s+", " ", cue["text"]).strip()
        if s and s != prev:
            out.append(s)
            prev = s
    return "\n".join(out).strip() + ("\n" if out else "")


def emit_derived(source: Source, raw: Path, out_root: Path) -> tuple[str, str]:
    if source.kind not in {"transcript_subtitle", "transcript_text"}:
        return "", ""
    base = f"{source.repo_key}--{safe_slug(Path(source.path).stem)}--{source.sha256[:12]}"
    text_dir = out_root / "text"
    cue_dir = out_root / "cues"
    text_dir.mkdir(parents=True, exist_ok=True)
    cue_dir.mkdir(parents=True, exist_ok=True)
    text_path = text_dir / f"{base}.txt"
    cue_path = cue_dir / f"{base}.jsonl"
    raw_text = read_text(raw)
    if source.kind == "transcript_subtitle":
        cues = parse_srt_vtt(raw_text)
        body = subtitle_to_text(cues)
        with cue_path.open("w", encoding="utf-8") as f:
            for cue in cues:
                f.write(json.dumps(cue, ensure_ascii=False) + "\n")
    else:
        body = raw_text
        cue_path = Path()
    header = (
        "# DERIVED TRANSCRIPT TEXT — MECHANICAL EXTRACTION ONLY\n"
        f"# source_repository: {source.repository}\n"
        f"# source_path: {source.path}\n"
        f"# source_sha256: {source.sha256}\n"
        f"# builder: {VERSION}\n"
        "# Raw source remains canonical. No theory terminology normalization applied.\n\n"
    )
    text_path.write_text(header + body, encoding="utf-8")
    return text_path.relative_to(out_root.parent.parent).as_posix(), (
        cue_path.relative_to(out_root.parent.parent).as_posix() if cue_path else ""
    )


def load_rankings(resources_root: Path) -> dict[str, dict]:
    p = resources_root / "EXPOSURE_STATS/PODCAST_EPs/DebatingA.I.OnScience_EpisodeRankings_all-time.csv"
    rows = {}
    if not p.exists():
        return rows
    with p.open("r", encoding="utf-8-sig", newline="") as f:
        for row in csv.DictReader(f):
            title = (row.get("Episode title") or "").strip()
            if title:
                rows[norm(title)] = row
    return rows


def ranking_match(candidate: str, rankings: dict[str, dict]) -> dict | None:
    n = norm(candidate)
    if n in rankings:
        return rankings[n]
    matches = [r for k, r in rankings.items() if len(n) >= 12 and (n in k or k in n)]
    return matches[0] if len(matches) == 1 else None


def classify_text_signals(text: str) -> tuple[bool, bool, bool]:
    sample = text[:2_000_000]
    return bool(RIGOR_PAT.search(sample)), bool(INSIGHT_PAT.search(sample)), bool(FIELD_PAT.search(sample))


def discover(repo_key: str, root: Path, out_root: Path) -> list[Source]:
    found = []
    if not root.exists():
        return found
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        rel = path.relative_to(root)
        if ".git" in rel.parts or is_quarantined(rel):
            continue
        if not discovery_candidate(rel):
            continue
        kind = classify(rel)
        # Generated central-guide outputs are not source inputs.
        if repo_key == "resources" and rel.as_posix().startswith("EXPOSURE_STATS/PODCAST_GUIDE/"):
            continue
        digest = sha256_file(path)
        text = ""
        published = ""
        rigor = insight = field = False
        if kind in {"transcript_subtitle", "transcript_text", "podcast_text_unspecified"} and path.suffix.casefold() in TEXT_EXTS:
            text = read_text(path)
            published = source_date(text)
            rigor, insight, field = classify_text_signals(text)
        src = Source(
            source_id=f"{repo_key}:{digest[:16]}",
            repository=REPO_LABELS[repo_key],
            repo_key=repo_key,
            path=rel.as_posix(),
            kind=kind,
            extension=path.suffix.casefold(),
            bytes=path.stat().st_size,
            sha256=digest,
            git_blob=git_blob(root, rel.as_posix()),
            duplicate_group=digest,
            title_candidate=title_from_filename(path),
            published_date_candidate=published,
            public_exposure_evidence=True,
            rigor_signal=rigor,
            insight_generation_requested=insight,
            terminology_hazard_field=field,
            derived_text_path="",
            cue_jsonl_path="",
        )
        if kind in {"transcript_subtitle", "transcript_text"}:
            txt, cues = emit_derived(src, path, out_root)
            src.derived_text_path = txt
            src.cue_jsonl_path = cues
        found.append(src)
    return found


def episode_key(title: str, date: str) -> str:
    base = norm(title)
    return f"{date or 'undated'}::{base}"


def build_episodes(sources: list[Source], rankings: dict[str, dict]) -> list[dict]:
    groups: dict[str, list[Source]] = defaultdict(list)
    for s in sources:
        if s.kind not in {"transcript_subtitle", "transcript_text", "podcast_text_unspecified"}:
            continue
        rank = ranking_match(s.title_candidate, rankings)
        title = (rank.get("Episode title") if rank else "") or s.title_candidate
        date = s.published_date_candidate
        if not date and rank:
            pd = (rank.get("Publish date") or "").strip()
            try:
                date = datetime.strptime(pd, "%m/%d/%Y").date().isoformat()
            except ValueError:
                pass
        groups[episode_key(title, date)].append(s)

    episodes = []
    for key, items in groups.items():
        exemplar = items[0]
        rank = ranking_match(exemplar.title_candidate, rankings)
        title = (rank.get("Episode title") if rank else "") or exemplar.title_candidate
        date = next((x.published_date_candidate for x in items if x.published_date_candidate), "")
        date_basis = "transcript_header" if date else ""
        if not date and rank:
            pd = (rank.get("Publish date") or "").strip()
            try:
                date = datetime.strptime(pd, "%m/%d/%Y").date().isoformat()
                date_basis = "episode_rankings_export"
            except ValueError:
                pass
        eid = f"ep-{date or 'undated'}-{safe_slug(title, 70)}"
        transcript_items = [x for x in items if x.kind in {"transcript_subtitle", "transcript_text"}]
        episodes.append({
            "episode_id": eid,
            "series": "Debating A.I. On the Future of Physics / The New Physics",
            "series_aliases": ["Debating A.I.", "DAI", "The New Physics"],
            "title": title,
            "published_date": date,
            "published_date_basis": date_basis,
            "published_date_confidence": "source-derived" if date else "unknown",
            "episode_number_if_known": "",
            "duration": (rank.get("Duration") if rank else "") or "",
            "spotify_uri_or_url": (rank.get("Episode URI") if rank else "") or "",
            "source_instances": [x.source_id for x in items],
            "transcript_status": "located" if transcript_items else "candidate_only",
            "derived_text_paths": [x.derived_text_path for x in transcript_items if x.derived_text_path],
            "analytics_sources": [],
            "public_exposure_evidence": True,
            "interpretive_task_class": "insight_generation_requested" if any(x.insight_generation_requested for x in items) else "ordinary_public_exposition",
            "rigor_signal": any(x.rigor_signal for x in items),
            "terminology_hazards": (["field"] if any(x.terminology_hazard_field for x in items) else []),
            "review_status": "unreviewed",
            "notes": "Podcast/public-exposure record; not automatic SAT core authority.",
        })
    episodes.sort(key=lambda x: (x["published_date"] or "9999-99-99", x["title"].casefold()))
    return episodes


def write_csv(path: Path, rows: list[dict], fields: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--resources-root", type=Path, required=True)
    ap.add_argument("--hsh-root", type=Path, required=True)
    ap.add_argument("--archive-root", type=Path, required=True)
    args = ap.parse_args()

    roots = {
        "resources": args.resources_root.resolve(),
        "hsh": args.hsh_root.resolve(),
        "archive": args.archive_root.resolve(),
    }
    out_root = roots["resources"] / "EXPOSURE_STATS/PODCAST_GUIDE"
    out_root.mkdir(parents=True, exist_ok=True)

    sources = []
    for key, root in roots.items():
        sources.extend(discover(key, root, out_root))
    sources.sort(key=lambda x: (x.repository, x.path.casefold()))

    duplicate_sizes = defaultdict(int)
    for s in sources:
        duplicate_sizes[s.sha256] += 1
    for s in sources:
        s.duplicate_group = f"sha256:{s.sha256}" if duplicate_sizes[s.sha256] > 1 else ""

    rankings = load_rankings(roots["resources"])
    episodes = build_episodes(sources, rankings)

    source_rows = [asdict(s) for s in sources]
    source_fields = list(asdict(sources[0]).keys()) if sources else [f.name for f in Source.__dataclass_fields__.values()]
    write_csv(out_root / "SOURCE_INVENTORY.csv", source_rows, source_fields)

    analytics = [asdict(s) for s in sources if s.kind in {"analytics", "analytics_capture", "metadata_or_analytics"}]
    write_csv(out_root / "ANALYTICS_INVENTORY.csv", analytics, source_fields)

    (out_root / "EPISODES.json").write_text(json.dumps(episodes, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    episode_flat = []
    for e in episodes:
        episode_flat.append({
            "episode_id": e["episode_id"],
            "published_date": e["published_date"],
            "title": e["title"],
            "transcript_status": e["transcript_status"],
            "source_instance_count": len(e["source_instances"]),
            "derived_text_count": len(e["derived_text_paths"]),
            "interpretive_task_class": e["interpretive_task_class"],
            "rigor_signal": e["rigor_signal"],
            "terminology_hazards": ";".join(e["terminology_hazards"]),
            "spotify_uri_or_url": e["spotify_uri_or_url"],
            "review_status": e["review_status"],
        })
    write_csv(out_root / "EPISODES.csv", episode_flat, [
        "episode_id", "published_date", "title", "transcript_status",
        "source_instance_count", "derived_text_count", "interpretive_task_class",
        "rigor_signal", "terminology_hazards", "spotify_uri_or_url", "review_status",
    ])

    md = [
        "# Episode Guide", "",
        "Generated mechanically from cross-repository podcast source discovery.",
        "Podcast transcripts are public-exposure evidence; they are not automatic SAT/H(s)H core authority.", "",
        f"Episodes represented: **{len(episodes)}**  ",
        f"Source instances: **{len(sources)}**  ",
        f"Analytics/metadata instances: **{len(analytics)}**", "",
        "| Date | Episode | Transcript | Sources | Review signals |", "|---|---|---|---:|---|",
    ]
    for e in episodes:
        signals = []
        if e["interpretive_task_class"] == "insight_generation_requested":
            signals.append("insight-generation requested")
        if e["rigor_signal"]:
            signals.append("rigor signal")
        if "field" in e["terminology_hazards"]:
            signals.append("field-language hazard")
        md.append(
            f"| {e['published_date'] or 'undated'} | {e['title'].replace('|','\\|')} | "
            f"{e['transcript_status']} | {len(e['source_instances'])} | {', '.join(signals)} |"
        )
    (out_root / "EPISODE_GUIDE.md").write_text("\n".join(md) + "\n", encoding="utf-8")

    generated = ["SOURCE_INVENTORY.csv", "ANALYTICS_INVENTORY.csv", "EPISODES.json", "EPISODES.csv", "EPISODE_GUIDE.md"]
    manifest = {
        "builder": VERSION,
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "input_commits": {k: git_commit(v) for k, v in roots.items()},
        "repositories": {k: REPO_LABELS[k] for k in roots},
        "counts": {
            "source_instances": len(sources),
            "episodes": len(episodes),
            "analytics_or_metadata_sources": len(analytics),
            "exact_duplicate_source_instances": sum(n for n in duplicate_sizes.values() if n > 1),
        },
        "generated_files": {},
        "quarantine_rule": "PRIOR_ART pruned before traversal",
        "theory_status_rule": "podcast transcripts are public-exposure evidence, not automatic core authority",
    }
    for name in generated:
        p = out_root / name
        manifest["generated_files"][name] = sha256_file(p)
    (out_root / "MANIFEST.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(manifest["counts"], indent=2))


if __name__ == "__main__":
    main()
