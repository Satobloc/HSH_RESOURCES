#!/usr/bin/env python3
"""Build neutral source and image-text inventories for Cross diffusion work.

No interpretation is performed. Raw repository files remain canonical.
The scopes below intentionally exclude PRIOR_ART.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import sqlite3
from pathlib import Path
from typing import Any

SCOPES = [
    Path("EXPOSURE_STATS"),
    Path("LIVE_RESEARCH_UPDATES"),
    Path("OUTSIDE RESEARCH LIBRARY/SCIENCE NEWS"),
    Path("OUTSIDE RESEARCH LIBRARY/CONTEMPORARY RESEARCH"),
]
IMAGE_EXTS = {".png", ".jpg", ".jpeg", ".webp", ".tif", ".tiff", ".bmp"}
TEXT_EXTS = {".txt", ".md", ".csv", ".json", ".jsonl", ".html", ".htm", ".xml", ".yml", ".yaml"}
SKIP_PARTS = {".git", "derived", "__pycache__", ".pytest_cache"}


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def load_jsonl(path: Path) -> dict[str, dict[str, Any]]:
    if not path.exists():
        return {}
    out: dict[str, dict[str, Any]] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        row = json.loads(line)
        source = row.get("source_path")
        if isinstance(source, str):
            out[source] = row
    return out


def collect(root: Path) -> list[Path]:
    files: list[Path] = []
    for scope in SCOPES:
        base = root / scope
        if not base.exists():
            continue
        candidates = [base] if base.is_file() else base.rglob("*")
        for path in candidates:
            if not path.is_file():
                continue
            rel = path.relative_to(root)
            if any(part in SKIP_PARTS for part in rel.parts):
                continue
            files.append(path)
    return sorted(set(files), key=lambda p: p.relative_to(root).as_posix().casefold())


def media_kind(path: Path) -> str:
    ext = path.suffix.lower()
    if ext in IMAGE_EXTS:
        return "image"
    if ext == ".pdf":
        return "pdf"
    if ext == ".csv":
        return "csv"
    if ext in TEXT_EXTS:
        return "text"
    return "other"


def text_record(rel: str, path: Path, pdf_manifest: dict[str, dict[str, Any]], image_manifest: dict[str, dict[str, Any]]) -> tuple[str, str, str, str]:
    kind = media_kind(path)
    if kind == "image":
        row = image_manifest.get(rel, {})
        return str(row.get("status") or "not_extracted"), str(row.get("text_path") or ""), str(row.get("text_characters_nonspace") or ""), "tesseract" if row else ""
    if kind == "pdf":
        row = pdf_manifest.get(rel, {})
        return str(row.get("status") or "not_extracted"), str(row.get("text_path") or ""), str(row.get("text_characters_nonspace") or ""), str(row.get("extractor") or "")
    if kind in {"text", "csv"}:
        try:
            chars = len(re.sub(r"\s+", "", path.read_text(encoding="utf-8-sig", errors="replace")))
        except OSError:
            chars = 0
        return "native_text", rel, str(chars), "native"
    return "not_text", "", "", ""


def write_source_manifest(root: Path, rows: list[dict[str, str]]) -> None:
    out = root / "EXPOSURE_STATS/CROSS_DIFFUSION_SOURCE_MANIFEST.csv"
    fields = ["source_path", "scope", "media_kind", "extension", "bytes", "sha256", "text_status", "text_path", "text_characters_nonspace", "text_method"]
    with out.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)


def md_link(from_dir: Path, target: str) -> str:
    if not target:
        return ""
    # All current targets are repository-relative. Keep links simple and stable.
    prefix = "../" if from_dir.as_posix() == "EXPOSURE_STATS" else ""
    return prefix + target


def write_image_index(root: Path, rows: list[dict[str, str]]) -> None:
    images = [r for r in rows if r["media_kind"] == "image"]
    out = root / "EXPOSURE_STATS/CROSS_IMAGE_TEXT_INDEX.md"
    lines = [
        "# Cross diffusion image-text index",
        "",
        "Neutral inventory only. No explanatory or similarity judgments are made here.",
        "",
        f"Images in current scopes: **{len(images)}**",
        "",
        "| Source image | SHA-256 | Text status | Extracted text | Non-space characters |",
        "|---|---|---|---|---:|",
    ]
    for r in images:
        src = r["source_path"].replace("|", "\\|")
        txt = r["text_path"]
        src_link = md_link(Path("EXPOSURE_STATS"), r["source_path"])
        text_link = md_link(Path("EXPOSURE_STATS"), txt) if txt else ""
        src_cell = f"[{src}]({src_link})"
        text_cell = f"[text]({text_link})" if text_link else ""
        lines.append(f"| {src_cell} | `{r['sha256']}` | {r['text_status']} | {text_cell} | {r['text_characters_nonspace']} |")
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")


def export_analytics(root: Path) -> None:
    db = root / "derived/analytics/cross_diffusion.sqlite"
    if not db.exists():
        return
    conn = sqlite3.connect(db)
    sources_out = root / "derived/analytics/cross_diffusion_sources.csv"
    observations_out = root / "derived/analytics/cross_diffusion_observations.csv"
    sources_out.parent.mkdir(parents=True, exist_ok=True)

    query_sources = "SELECT source_path,sha256,bytes,extension,source_family,media_kind,COALESCE(adapter,''),adapter_status FROM source_artifact ORDER BY source_path"
    with sources_out.open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["source_path","sha256","bytes","extension","source_family","media_kind","adapter","adapter_status"])
        w.writerows(conn.execute(query_sources))

    query_obs = """
      SELECT s.source_path, o.locator, COALESCE(e.kind,''), COALESCE(e.external_id,''), COALESCE(e.label,''),
             COALESCE(e.published_date,''), o.metric, COALESCE(o.dimension,''), COALESCE(o.dimension_value,''),
             COALESCE(CAST(o.value_numeric AS TEXT),''), COALESCE(o.value_text,''), COALESCE(o.unit,'')
      FROM observation o
      JOIN source_artifact s ON s.id=o.artifact_id
      LEFT JOIN entity e ON e.id=o.entity_id
      ORDER BY s.source_path, o.id
    """
    with observations_out.open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["source_path","locator","entity_kind","entity_id","entity_label","published_date","metric","dimension","dimension_value","value_numeric","value_text","unit"])
        w.writerows(conn.execute(query_obs))
    conn.close()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path("."))
    args = parser.parse_args()
    root = args.root.resolve()
    pdf_manifest = load_jsonl(root / "derived/manifests/extraction.jsonl")
    image_manifest = load_jsonl(root / "derived/manifests/image_text_extraction.jsonl")
    rows: list[dict[str, str]] = []
    for path in collect(root):
        rel = path.relative_to(root).as_posix()
        status, text_path, chars, method = text_record(rel, path, pdf_manifest, image_manifest)
        scope = next((s.as_posix() for s in SCOPES if rel == s.as_posix() or rel.startswith(s.as_posix() + "/")), "")
        rows.append({
            "source_path": rel,
            "scope": scope,
            "media_kind": media_kind(path),
            "extension": path.suffix.lower(),
            "bytes": str(path.stat().st_size),
            "sha256": sha256_file(path),
            "text_status": status,
            "text_path": text_path,
            "text_characters_nonspace": chars,
            "text_method": method,
        })
    write_source_manifest(root, rows)
    write_image_index(root, rows)
    export_analytics(root)
    counts: dict[str, int] = {}
    for row in rows:
        counts[row["media_kind"]] = counts.get(row["media_kind"], 0) + 1
    print(f"sources={len(rows)} kinds={json.dumps(counts, sort_keys=True)}")
    print("source_manifest=EXPOSURE_STATS/CROSS_DIFFUSION_SOURCE_MANIFEST.csv")
    print("image_index=EXPOSURE_STATS/CROSS_IMAGE_TEXT_INDEX.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
