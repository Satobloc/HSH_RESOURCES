#!/usr/bin/env python3
"""Build a source-traceable SQLite analytics store for HSH_RESOURCES.

The database is derived and rebuildable. Raw repository files remain canonical.
Version 0.1 inventories selected research/exposure areas, records CSV schemas,
normalizes common Spotify-style matrix/episode CSVs, and ingests the JSON output
of tools/arxiv_sat_scanner.py as research-item/match records.

Dry-run is the default. Pass --apply to atomically replace the derived database.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import sqlite3
import tempfile
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

VERSION = "0.1.0"
DEFAULT_SCOPES = [
    Path("EXPOSURE_STATS"),
    Path("LIVE_RESEARCH_UPDATES"),
    Path("OUTSIDE RESEARCH LIBRARY"),
    Path("PRIOR_ART"),
]
SKIP_PARTS = {".git", "derived", "__pycache__", ".pytest_cache"}
TEXT_EXTENSIONS = {".txt", ".md", ".csv", ".json", ".jsonl", ".html", ".htm", ".xml"}

SCHEMA = """
PRAGMA foreign_keys = ON;
CREATE TABLE meta (key TEXT PRIMARY KEY, value TEXT NOT NULL);
CREATE TABLE source_artifact (
  id INTEGER PRIMARY KEY,
  source_path TEXT NOT NULL UNIQUE,
  sha256 TEXT NOT NULL,
  bytes INTEGER NOT NULL,
  extension TEXT NOT NULL,
  source_family TEXT NOT NULL,
  media_kind TEXT NOT NULL,
  adapter TEXT,
  adapter_status TEXT NOT NULL DEFAULT 'unhandled'
);
CREATE TABLE csv_schema (
  artifact_id INTEGER PRIMARY KEY REFERENCES source_artifact(id) ON DELETE CASCADE,
  headers_json TEXT NOT NULL,
  row_count INTEGER NOT NULL,
  dialect TEXT NOT NULL
);
CREATE TABLE entity (
  id INTEGER PRIMARY KEY,
  kind TEXT NOT NULL,
  external_id TEXT,
  label TEXT NOT NULL,
  published_date TEXT,
  UNIQUE(kind, external_id)
);
CREATE TABLE observation (
  id INTEGER PRIMARY KEY,
  artifact_id INTEGER NOT NULL REFERENCES source_artifact(id) ON DELETE CASCADE,
  entity_id INTEGER REFERENCES entity(id) ON DELETE SET NULL,
  metric TEXT NOT NULL,
  dimension TEXT,
  dimension_value TEXT,
  value_numeric REAL,
  value_text TEXT,
  unit TEXT,
  locator TEXT
);
CREATE TABLE research_item (
  id INTEGER PRIMARY KEY,
  canonical_key TEXT NOT NULL UNIQUE,
  arxiv_id TEXT,
  doi TEXT,
  title TEXT NOT NULL,
  authors_json TEXT NOT NULL,
  published TEXT,
  updated TEXT,
  primary_category TEXT,
  categories_json TEXT NOT NULL,
  abs_url TEXT,
  pdf_url TEXT,
  journal_ref TEXT
);
CREATE TABLE research_match (
  id INTEGER PRIMARY KEY,
  research_item_id INTEGER NOT NULL REFERENCES research_item(id) ON DELETE CASCADE,
  artifact_id INTEGER NOT NULL REFERENCES source_artifact(id) ON DELETE CASCADE,
  scan_utc TEXT,
  score REAL,
  tier TEXT,
  sectors_json TEXT NOT NULL,
  features_json TEXT NOT NULL,
  terms_json TEXT NOT NULL,
  bundles_json TEXT NOT NULL,
  control_score REAL,
  control_families_json TEXT NOT NULL,
  control_features_json TEXT NOT NULL,
  contrast REAL,
  new_or_updated INTEGER,
  UNIQUE(research_item_id, artifact_id)
);
CREATE TABLE import_note (
  id INTEGER PRIMARY KEY,
  artifact_id INTEGER REFERENCES source_artifact(id) ON DELETE CASCADE,
  level TEXT NOT NULL,
  code TEXT NOT NULL,
  note TEXT NOT NULL
);
CREATE INDEX observation_metric_idx ON observation(metric);
CREATE INDEX observation_dimension_idx ON observation(dimension, dimension_value);
CREATE INDEX research_item_arxiv_idx ON research_item(arxiv_id);
CREATE INDEX research_item_doi_idx ON research_item(doi);
CREATE INDEX research_match_score_idx ON research_match(score DESC);
"""


def iso_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def source_family(rel: str) -> str:
    return rel.split("/", 1)[0]


def media_kind(path: Path) -> str:
    suffix = path.suffix.lower()
    if suffix == ".csv": return "csv"
    if suffix == ".json": return "json"
    if suffix == ".pdf": return "pdf"
    if suffix in TEXT_EXTENSIONS: return "text"
    if suffix in {".png", ".jpg", ".jpeg", ".webp", ".tif", ".tiff"}: return "image"
    return "binary_or_other"


def files_for_scopes(root: Path, scopes: list[Path], max_files: int | None) -> list[Path]:
    found: list[Path] = []
    for scope in scopes:
        base = (root / scope).resolve()
        if not base.exists():
            continue
        candidates = [base] if base.is_file() else base.rglob("*")
        for path in candidates:
            if not path.is_file():
                continue
            rel_parts = path.resolve().relative_to(root).parts
            if any(part in SKIP_PARTS for part in rel_parts):
                continue
            found.append(path.resolve())
    unique = sorted(set(found), key=lambda item: item.relative_to(root).as_posix().casefold())
    return unique if max_files is None else unique[: max(max_files, 0)]


def float_or_none(value: str) -> float | None:
    text = value.strip().replace(",", "")
    if not text:
        return None
    try:
        return float(text)
    except ValueError:
        return None


def normalize_date(value: str) -> str | None:
    text = value.strip()
    if not text:
        return None
    for pattern in ("%m/%d/%Y", "%Y-%m-%d"):
        try:
            return datetime.strptime(text, pattern).date().isoformat()
        except ValueError:
            pass
    return text


def infer_unit(header: str) -> str | None:
    lower = header.casefold()
    if "%" in header or "percentage" in lower or "percent" in lower: return "percent"
    if "hour" in lower: return "hours"
    if "minute" in lower: return "minutes"
    if "second" in lower: return "seconds"
    return None


def insert_artifact(conn: sqlite3.Connection, rel: str, path: Path) -> int:
    conn.execute(
        "INSERT INTO source_artifact(source_path,sha256,bytes,extension,source_family,media_kind) VALUES (?,?,?,?,?,?)",
        (rel, sha256_file(path), path.stat().st_size, path.suffix.lower() or "[none]", source_family(rel), media_kind(path)),
    )
    return int(conn.execute("SELECT last_insert_rowid()").fetchone()[0])


def get_or_create_entity(conn: sqlite3.Connection, kind: str, external_id: str | None, label: str, published_date: str | None) -> int:
    if external_id:
        row = conn.execute("SELECT id FROM entity WHERE kind=? AND external_id=?", (kind, external_id)).fetchone()
        if row:
            conn.execute(
                "UPDATE entity SET label=COALESCE(NULLIF(?,''),label), published_date=COALESCE(?,published_date) WHERE id=?",
                (label, published_date, row[0]),
            )
            return int(row[0])
    conn.execute("INSERT INTO entity(kind,external_id,label,published_date) VALUES (?,?,?,?)", (kind, external_id, label, published_date))
    return int(conn.execute("SELECT last_insert_rowid()").fetchone()[0])


def open_csv(path: Path) -> tuple[list[str], list[list[str]], str]:
    text = path.read_text(encoding="utf-8-sig", errors="replace")
    try:
        dialect = csv.Sniffer().sniff(text[:65536], delimiters=",\t;|")
        delimiter = dialect.delimiter
    except csv.Error:
        dialect = csv.excel
        delimiter = ","
    rows = list(csv.reader(text.splitlines(), dialect))
    if not rows:
        return [], [], delimiter
    return [cell.strip() for cell in rows[0]], rows[1:], delimiter


def is_episode_table(headers: list[str]) -> bool:
    folded = {header.casefold() for header in headers}
    return {"episode title", "publish date", "episode uri"}.issubset(folded)


def ingest_episode_csv(conn: sqlite3.Connection, artifact_id: int, headers: list[str], rows: list[list[str]]) -> int:
    by_name = {header.casefold(): index for index, header in enumerate(headers)}
    title_i, date_i, uri_i = by_name["episode title"], by_name["publish date"], by_name["episode uri"]
    metric_indices = [i for i in range(len(headers)) if i not in {title_i, date_i, uri_i}]
    inserted = 0
    for row_number, row in enumerate(rows, 2):
        padded = row + [""] * (len(headers) - len(row))
        title, uri = padded[title_i].strip(), padded[uri_i].strip() or None
        if not title and not uri:
            continue
        entity_id = get_or_create_entity(conn, "podcast_episode", uri, title or uri or "untitled episode", normalize_date(padded[date_i]))
        for i in metric_indices:
            raw, numeric = padded[i].strip(), float_or_none(padded[i])
            if numeric is None:
                continue
            conn.execute(
                "INSERT INTO observation(artifact_id,entity_id,metric,value_numeric,value_text,unit,locator) VALUES (?,?,?,?,?,?,?)",
                (artifact_id, entity_id, headers[i], numeric, raw, infer_unit(headers[i]), f"row {row_number}"),
            )
            inserted += 1
    return inserted


def ingest_matrix_csv(conn: sqlite3.Connection, artifact_id: int, headers: list[str], rows: list[list[str]]) -> int:
    if len(headers) < 2:
        return 0
    numeric_columns: set[int] = set()
    for i in range(1, len(headers)):
        samples = [row[i] for row in rows[:25] if i < len(row) and row[i].strip()]
        if samples and sum(float_or_none(value) is not None for value in samples) >= max(1, len(samples) // 2):
            numeric_columns.add(i)
    if not numeric_columns:
        return 0
    inserted = 0
    for row_number, row in enumerate(rows, 2):
        padded = row + [""] * (len(headers) - len(row))
        dimension_value = padded[0].strip()
        if not dimension_value:
            continue
        for i in sorted(numeric_columns):
            raw, numeric = padded[i].strip(), float_or_none(padded[i])
            if numeric is None:
                continue
            conn.execute(
                "INSERT INTO observation(artifact_id,metric,dimension,dimension_value,value_numeric,value_text,unit,locator) VALUES (?,?,?,?,?,?,?,?)",
                (artifact_id, headers[i], headers[0], dimension_value, numeric, raw, infer_unit(headers[i]), f"row {row_number}"),
            )
            inserted += 1
    return inserted


def ingest_csv(conn: sqlite3.Connection, artifact_id: int, path: Path) -> tuple[str, str, int]:
    headers, rows, delimiter = open_csv(path)
    conn.execute(
        "INSERT INTO csv_schema(artifact_id,headers_json,row_count,dialect) VALUES (?,?,?,?)",
        (artifact_id, json.dumps(headers, ensure_ascii=False), len(rows), delimiter),
    )
    if not headers:
        return "empty_csv", "handled", 0
    if is_episode_table(headers):
        return "episode_metrics_csv", "handled", ingest_episode_csv(conn, artifact_id, headers, rows)
    count = ingest_matrix_csv(conn, artifact_id, headers, rows)
    return ("numeric_matrix_csv", "handled", count) if count else ("schema_only_csv", "needs_adapter", 0)


def canonical_research_key(item: dict[str, Any]) -> str:
    arxiv_id = str(item.get("arxiv_id") or "").strip()
    if arxiv_id:
        return "arxiv:" + re.sub(r"v\d+$", "", arxiv_id)
    doi = str(item.get("doi") or "").strip().casefold()
    if doi:
        return "doi:" + doi
    title = re.sub(r"\s+", " ", str(item.get("title") or "").strip().casefold())
    return "title:" + hashlib.sha256(title.encode("utf-8")).hexdigest()


def upsert_research_item(conn: sqlite3.Connection, item: dict[str, Any]) -> int:
    key = canonical_research_key(item)
    row = conn.execute("SELECT id FROM research_item WHERE canonical_key=?", (key,)).fetchone()
    payload = (
        str(item.get("arxiv_id") or "") or None,
        str(item.get("doi") or "") or None,
        str(item.get("title") or "").strip() or "[untitled]",
        json.dumps(item.get("authors") or [], ensure_ascii=False),
        str(item.get("published") or "") or None,
        str(item.get("updated") or "") or None,
        str(item.get("primary_category") or "") or None,
        json.dumps(item.get("categories") or [], ensure_ascii=False),
        str(item.get("abs_url") or "") or None,
        str(item.get("pdf_url") or "") or None,
        str(item.get("journal_ref") or "") or None,
    )
    if row:
        conn.execute(
            "UPDATE research_item SET arxiv_id=?,doi=?,title=?,authors_json=?,published=?,updated=?,primary_category=?,categories_json=?,abs_url=?,pdf_url=?,journal_ref=? WHERE id=?",
            (*payload, row[0]),
        )
        return int(row[0])
    conn.execute(
        "INSERT INTO research_item(canonical_key,arxiv_id,doi,title,authors_json,published,updated,primary_category,categories_json,abs_url,pdf_url,journal_ref) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)",
        (key, *payload),
    )
    return int(conn.execute("SELECT last_insert_rowid()").fetchone()[0])


def ingest_arxiv_scan_json(conn: sqlite3.Connection, artifact_id: int, payload: dict[str, Any]) -> int:
    scan = payload.get("scan") if isinstance(payload.get("scan"), dict) else {}
    results = payload.get("results")
    if not isinstance(results, list):
        return 0
    inserted = 0
    for item in results:
        if not isinstance(item, dict):
            continue
        research_id = upsert_research_item(conn, item)
        conn.execute(
            """INSERT OR REPLACE INTO research_match
               (research_item_id,artifact_id,scan_utc,score,tier,sectors_json,features_json,terms_json,bundles_json,control_score,control_families_json,control_features_json,contrast,new_or_updated)
               VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
            (
                research_id, artifact_id, str(scan.get("scan_utc") or "") or None,
                item.get("score"), str(item.get("tier") or "") or None,
                json.dumps(item.get("sectors") or [], ensure_ascii=False),
                json.dumps(item.get("features") or [], ensure_ascii=False),
                json.dumps(item.get("terms") or [], ensure_ascii=False),
                json.dumps(item.get("bundles") or [], ensure_ascii=False),
                item.get("control_score"),
                json.dumps(item.get("control_families") or [], ensure_ascii=False),
                json.dumps(item.get("control_features") or [], ensure_ascii=False),
                item.get("contrast"), 1 if item.get("new_or_updated") else 0,
            ),
        )
        inserted += 1
    return inserted


def ingest_json(conn: sqlite3.Connection, artifact_id: int, path: Path) -> tuple[str, str, int]:
    try:
        payload = json.loads(path.read_text(encoding="utf-8-sig"))
    except (UnicodeError, json.JSONDecodeError) as exc:
        conn.execute("INSERT INTO import_note(artifact_id,level,code,note) VALUES (?,'warning','json_parse',?)", (artifact_id, str(exc)))
        return "json_parse_error", "error", 0
    if isinstance(payload, dict) and isinstance(payload.get("scan"), dict) and isinstance(payload.get("results"), list):
        return "arxiv_scan_json", "handled", ingest_arxiv_scan_json(conn, artifact_id, payload)
    return "generic_json", "needs_adapter", 0


def set_adapter(conn: sqlite3.Connection, artifact_id: int, adapter: str, status: str) -> None:
    conn.execute("UPDATE source_artifact SET adapter=?,adapter_status=? WHERE id=?", (adapter, status, artifact_id))


def build_database(root: Path, scopes: list[Path], target: Path, max_files: int | None) -> dict[str, Any]:
    files = files_for_scopes(root, scopes, max_files)
    target.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(prefix="analytics-", suffix=".sqlite", dir=target.parent, delete=False) as handle:
        temporary = Path(handle.name)
    try:
        conn = sqlite3.connect(temporary)
        conn.executescript(SCHEMA)
        generated_at = iso_now()
        conn.executemany("INSERT INTO meta(key,value) VALUES (?,?)", [
            ("schema_version", "1"), ("tool_version", VERSION), ("generated_at_utc", generated_at),
            ("repository_root", str(root)), ("scopes_json", json.dumps([scope.as_posix() for scope in scopes])),
        ])
        stats: dict[str, Any] = {"files":0,"csv":0,"json":0,"observations":0,"research_matches":0,"handled":0,"needs_adapter":0,"unhandled":0,"error":0}
        for path in files:
            rel = path.relative_to(root).as_posix()
            artifact_id = insert_artifact(conn, rel, path)
            stats["files"] += 1
            suffix = path.suffix.lower()
            if suffix == ".csv":
                stats["csv"] += 1
                try:
                    adapter, status, count = ingest_csv(conn, artifact_id, path)
                    set_adapter(conn, artifact_id, adapter, status)
                    stats["observations"] += count
                except Exception as exc:
                    status = "error"
                    set_adapter(conn, artifact_id, "csv_error", status)
                    conn.execute("INSERT INTO import_note(artifact_id,level,code,note) VALUES (?,'error','csv_ingest',?)", (artifact_id, f"{type(exc).__name__}: {exc}"))
                stats[status] = stats.get(status, 0) + 1
            elif suffix == ".json":
                stats["json"] += 1
                adapter, status, count = ingest_json(conn, artifact_id, path)
                set_adapter(conn, artifact_id, adapter, status)
                stats["research_matches"] += count
                stats[status] = stats.get(status, 0) + 1
            else:
                stats["unhandled"] += 1
        conn.commit()
        stats["research_items"] = int(conn.execute("SELECT COUNT(*) FROM research_item").fetchone()[0])
        stats["entities"] = int(conn.execute("SELECT COUNT(*) FROM entity").fetchone()[0])
        stats["generated_at_utc"] = generated_at
        conn.close()
        temporary.replace(target)
        return stats
    except Exception:
        temporary.unlink(missing_ok=True)
        raise


def dry_run(root: Path, scopes: list[Path], max_files: int | None) -> dict[str, Any]:
    files = files_for_scopes(root, scopes, max_files)
    by_family: dict[str,int] = {}
    by_extension: dict[str,int] = {}
    for path in files:
        rel = path.relative_to(root).as_posix()
        family, extension = source_family(rel), path.suffix.lower() or "[none]"
        by_family[family] = by_family.get(family, 0) + 1
        by_extension[extension] = by_extension.get(extension, 0) + 1
    return {"files":len(files),"by_family":dict(sorted(by_family.items())),"by_extension":dict(sorted(by_extension.items()))}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path("."))
    parser.add_argument("--scope", action="append", type=Path, dest="scopes")
    parser.add_argument("--include-toolkit", action="store_true")
    parser.add_argument("--output", type=Path, default=Path("derived/analytics/research_analytics.sqlite"))
    parser.add_argument("--max-files", type=int)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()

    root = args.root.resolve()
    if not root.is_dir():
        print(f"error: repository root not found: {root}")
        return 2
    scopes = list(args.scopes or DEFAULT_SCOPES)
    if args.include_toolkit and Path("H(s)H_Toolkit") not in scopes:
        scopes.append(Path("H(s)H_Toolkit"))

    if not args.apply:
        report = dry_run(root, scopes, args.max_files)
        print(f"mode=dry-run files={report['files']}")
        print("families=" + json.dumps(report["by_family"], ensure_ascii=False, sort_keys=True))
        print("extensions=" + json.dumps(report["by_extension"], ensure_ascii=False, sort_keys=True))
        return 0

    try:
        stats = build_database(root, scopes, root / args.output, args.max_files)
    except (OSError, UnicodeError, ValueError, sqlite3.Error, json.JSONDecodeError) as exc:
        print(f"error: {type(exc).__name__}: {exc}")
        return 2
    print(" ".join(f"{key}={value}" for key,value in stats.items()))
    print(f"database={args.output.as_posix()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
