#!/usr/bin/env python3
"""Audit text accessibility across a SAT/H(s)H repository checkout.

The audit is repository-agnostic. It distinguishes structural visibility from
text accessibility and recognizes the manifests produced by HSH_RESOURCES'
PDF extractor and OCR extractor when those manifests are present.

Dry-run/check mode is the default. Pass --apply to write a JSON state file and
a compact Markdown report. Source files are never modified.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

VERSION = "1.0.0"
SKIP_PARTS = {".git", "__pycache__", ".pytest_cache"}
GENERATED_PATHS = {
    "indexes/ACCESSIBILITY_AUDIT.md",
    "indexes/accessibility-state.json",
}

NATIVE_TEXT_EXTENSIONS = {
    ".txt", ".md", ".markdown", ".rst", ".csv", ".tsv", ".json", ".jsonl",
    ".yaml", ".yml", ".toml", ".ini", ".cfg", ".conf", ".xml", ".html",
    ".htm", ".css", ".js", ".mjs", ".cjs", ".py", ".sh", ".bat", ".cmd",
    ".ps1", ".lean", ".tex", ".bib", ".svg", ".rtf", ".log", ".sql",
    ".ipynb", ".c", ".h", ".cpp", ".hpp", ".java", ".rs", ".go",
}
IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".tif", ".tiff", ".bmp", ".webp", ".gif"}
OFFICE_BINARY_EXTENSIONS = {".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".odt", ".ods", ".odp"}
MEDIA_EXTENSIONS = {".mp3", ".m4a", ".wav", ".flac", ".ogg", ".mp4", ".mov", ".avi", ".mkv", ".webm"}
ARCHIVE_EXTENSIONS = {".zip", ".7z", ".rar", ".tar", ".gz", ".bz2", ".xz"}
OTHER_BINARY_EXTENSIONS = {".lnk", ".exe", ".dll", ".bin", ".dat", ".db", ".sqlite", ".sqlite3"}


@dataclass(frozen=True)
class Record:
    path: str
    extension: str
    bytes: int
    state: str
    retrieval: str
    derived_path: str | None = None
    note: str | None = None


def iso_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def load_jsonl(path: Path) -> dict[str, dict[str, Any]]:
    if not path.exists():
        return {}
    rows: dict[str, dict[str, Any]] = {}
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            row = json.loads(line)
        except json.JSONDecodeError as exc:
            raise ValueError(f"{path}:{line_number}: invalid JSONL: {exc}") from exc
        if isinstance(row, dict) and isinstance(row.get("source_path"), str):
            rows[row["source_path"]] = row
    return rows


def is_skipped(rel: str) -> bool:
    return rel in GENERATED_PATHS or any(part in SKIP_PARTS for part in Path(rel).parts)


def files_under(root: Path) -> list[Path]:
    return [
        path
        for path in sorted(root.rglob("*"), key=lambda item: item.as_posix().casefold())
        if path.is_file() and not is_skipped(path.relative_to(root).as_posix())
    ]


def classify(
    root: Path,
    path: Path,
    pdf_manifest: dict[str, dict[str, Any]],
    ocr_manifest: dict[str, dict[str, Any]],
) -> Record:
    rel = path.relative_to(root).as_posix()
    suffix = path.suffix.lower()
    extension = suffix or "[none]"
    size = path.stat().st_size

    ocr = ocr_manifest.get(rel)
    pdf = pdf_manifest.get(rel)

    if suffix in NATIVE_TEXT_EXTENSIONS:
        return Record(rel, extension, size, "native_text", "source file")

    if suffix == ".pdf":
        if ocr and ocr.get("status") == "extracted":
            return Record(rel, extension, size, "ocr_extracted", "derived OCR text", str(ocr.get("text_path") or "") or None)
        if pdf and pdf.get("status") == "extracted":
            return Record(rel, extension, size, "pdf_extracted", "derived PDF text", str(pdf.get("text_path") or "") or None)
        if pdf and pdf.get("status") == "needs_ocr":
            return Record(rel, extension, size, "needs_ocr", "run OCR extractor", note="PDF text extractor found too little embedded text")
        if ocr and ocr.get("status") == "error":
            return Record(rel, extension, size, "ocr_error", "review OCR error", note=str(ocr.get("error") or "OCR error"))
        if pdf and pdf.get("status") == "error":
            return Record(rel, extension, size, "pdf_error", "review PDF extraction error", note=str(pdf.get("error") or "PDF extraction error"))
        return Record(rel, extension, size, "pdf_untracked", "run PDF extractor")

    if suffix in IMAGE_EXTENSIONS:
        if ocr and ocr.get("status") == "extracted":
            return Record(rel, extension, size, "ocr_extracted", "derived OCR text", str(ocr.get("text_path") or "") or None)
        if ocr and ocr.get("status") == "error":
            return Record(rel, extension, size, "ocr_error", "review OCR error", note=str(ocr.get("error") or "OCR error"))
        return Record(rel, extension, size, "image_untracked", "run OCR extractor")

    if suffix in OFFICE_BINARY_EXTENSIONS:
        return Record(rel, extension, size, "needs_handler", "format-specific text extractor", note="office/document binary")
    if suffix in MEDIA_EXTENSIONS:
        return Record(rel, extension, size, "needs_handler", "transcription/media handler", note="audio/video")
    if suffix in ARCHIVE_EXTENSIONS:
        return Record(rel, extension, size, "needs_handler", "archive/container inspection", note="compressed archive")
    if suffix in OTHER_BINARY_EXTENSIONS:
        return Record(rel, extension, size, "unsupported_binary", "manual or format-specific inspection")

    try:
        sample = path.read_bytes()[:8192]
    except OSError as exc:
        return Record(rel, extension, size, "read_error", "review filesystem error", note=str(exc))
    if b"\x00" not in sample:
        try:
            sample.decode("utf-8")
            return Record(rel, extension, size, "native_text", "source file", note="UTF-8 probe")
        except UnicodeDecodeError:
            pass
    return Record(rel, extension, size, "unknown_binary", "classify format / add handler")


def build_state(root: Path, label: str, generated_at: str) -> dict[str, Any]:
    pdf_manifest_path = root / "derived/manifests/extraction.jsonl"
    ocr_manifest_path = root / "derived/manifests/image_text_extraction.jsonl"
    pdf_manifest = load_jsonl(pdf_manifest_path)
    ocr_manifest = load_jsonl(ocr_manifest_path)
    records = [classify(root, path, pdf_manifest, ocr_manifest) for path in files_under(root)]
    counts = Counter(record.state for record in records)
    unresolved_states = {
        "needs_ocr", "pdf_untracked", "pdf_error", "image_untracked", "ocr_error",
        "needs_handler", "unsupported_binary", "unknown_binary", "read_error",
    }
    unresolved = [record for record in records if record.state in unresolved_states]
    digest = hashlib.sha256()
    for record in records:
        digest.update(json.dumps(asdict(record), ensure_ascii=False, sort_keys=True).encode("utf-8"))
        digest.update(b"\n")
    return {
        "schema_version": 1,
        "tool_version": VERSION,
        "repository_label": label,
        "generated_at_utc": generated_at,
        "root": str(root),
        "inventory_digest": digest.hexdigest(),
        "files": len(records),
        "counts_by_state": dict(sorted(counts.items())),
        "unresolved_count": len(unresolved),
        "manifests": {
            "pdf_extraction": pdf_manifest_path.relative_to(root).as_posix() if pdf_manifest_path.exists() else None,
            "image_ocr": ocr_manifest_path.relative_to(root).as_posix() if ocr_manifest_path.exists() else None,
        },
        "records": [asdict(record) for record in records],
        "limitations": [
            "This audit reports retrieval/accessibility state, not semantic indexing quality.",
            "Native-readable means text can be consumed directly; it does not mean the file has been semantically summarized or reviewed.",
            "OCR text is a search aid and must be checked against the source for exact wording, equations, dates, or priority evidence.",
            "Binary-handler status means an explicit extraction/transcription route is still required.",
        ],
    }


def render_markdown(state: dict[str, Any]) -> str:
    lines = [
        f"# Accessibility Audit — {state['repository_label']}",
        "",
        "> Generated retrieval audit; not primary theory material.",
        "",
        f"- Generated: `{state['generated_at_utc']}`",
        f"- Files inventoried: **{state['files']}**",
        f"- Unresolved accessibility items: **{state['unresolved_count']}**",
        f"- Inventory digest: `{state['inventory_digest']}`",
        "",
        "## Accessibility states",
        "",
        "| State | Files |",
        "|---|---:|",
    ]
    for state_name, count in state["counts_by_state"].items():
        lines.append(f"| `{state_name}` | {count} |")

    unresolved_states = {
        "needs_ocr", "pdf_untracked", "pdf_error", "image_untracked", "ocr_error",
        "needs_handler", "unsupported_binary", "unknown_binary", "read_error",
    }
    unresolved = [record for record in state["records"] if record["state"] in unresolved_states]
    lines.extend(["", "## Remaining accessibility work", ""])
    if not unresolved:
        lines.append("No unresolved file-accessibility items detected by this audit.")
    else:
        for record in unresolved:
            detail = f" — {record['note']}" if record.get("note") else ""
            lines.append(
                f"- `{record['path']}` — `{record['state']}` — {record['retrieval']}{detail}"
            )

    lines.extend(["", "## Manifests recognized", ""])
    for name, path in state["manifests"].items():
        lines.append(f"- `{name}`: `{path or 'not present'}`")
    lines.extend(["", "## Limitations", ""])
    lines.extend(f"- {item}" for item in state["limitations"])
    lines.append("")
    return "\n".join(lines)


def write_if_changed(path: Path, text: str) -> bool:
    if path.exists() and path.read_text(encoding="utf-8") == text:
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")
    return True


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path("."))
    parser.add_argument("--label", default=None, help="display label; defaults to root directory name")
    parser.add_argument("--output-dir", type=Path, default=Path("indexes"))
    parser.add_argument("--generated-at", default=None)
    parser.add_argument("--apply", action="store_true", help="write audit outputs; default is report-only")
    parser.add_argument("--list-unresolved", action="store_true")
    args = parser.parse_args()

    root = args.root.resolve()
    if not root.is_dir():
        print(f"error: root directory not found: {root}")
        return 2
    label = args.label or root.name
    try:
        state = build_state(root, label, args.generated_at or iso_now())
    except (OSError, UnicodeError, ValueError, json.JSONDecodeError) as exc:
        print(f"error: {exc}")
        return 2

    counts = " ".join(f"{key}={value}" for key, value in state["counts_by_state"].items())
    print(f"files={state['files']} unresolved={state['unresolved_count']} {counts}")
    if args.list_unresolved:
        resolved = {"native_text", "pdf_extracted", "ocr_extracted"}
        for record in state["records"]:
            if record["state"] not in resolved:
                print(f"{record['state']}\t{record['path']}\t{record['retrieval']}")

    if not args.apply:
        return 0

    output_dir = root / args.output_dir
    state_text = json.dumps(state, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    report_text = render_markdown(state)
    changed: list[str] = []
    if write_if_changed(output_dir / "accessibility-state.json", state_text):
        changed.append("accessibility-state.json")
    if write_if_changed(output_dir / "ACCESSIBILITY_AUDIT.md", report_text):
        changed.append("ACCESSIBILITY_AUDIT.md")
    print("updated=" + (",".join(changed) if changed else "none"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
