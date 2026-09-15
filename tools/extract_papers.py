#!/usr/bin/env python3
"""Extract page-marked text from PDFs without modifying source files.

Dry-run is the default. Pass --apply to create derived text and a deterministic
current-state manifest. OCR is deliberately not automatic.

Safety properties
-----------------
- source PDFs are never modified;
- PRIOR_ART and other excluded roots are pruned before file discovery;
- explicit supplied paths inside excluded/quarantined roots are rejected;
- derived text is named by source SHA-256 and finalized atomically;
- the manifest is finalized atomically.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import tempfile
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

VERSION = "1.2.0"
SKIP_PARTS = {".git", "derived", "__pycache__", ".pytest_cache", "PRIOR_ART"}
QUARANTINED_COMPONENTS = {"PRIOR_ART"}


def iso_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def page_document(pages: list[str]) -> str:
    blocks = []
    for number, text in enumerate(pages, 1):
        normalized = text.replace("\r\n", "\n").replace("\r", "\n").strip()
        blocks.append(f"===== PAGE {number} =====\n{normalized}\n")
    return "\n".join(blocks)


def extract_with_pypdf(path: Path) -> tuple[list[str], dict[str, Any]]:
    from pypdf import PdfReader  # type: ignore

    reader = PdfReader(str(path))
    if reader.is_encrypted:
        try:
            reader.decrypt("")
        except Exception as exc:  # pragma: no cover - depends on source encryption
            raise RuntimeError(f"encrypted PDF: {exc}") from exc
    pages = [(page.extract_text() or "") for page in reader.pages]
    metadata = reader.metadata or {}
    return pages, {
        "extractor": "pypdf",
        "title": str(metadata.get("/Title") or "").strip() or None,
        "author": str(metadata.get("/Author") or "").strip() or None,
    }


def extract_with_pdftotext(path: Path) -> tuple[list[str], dict[str, Any]]:
    executable = shutil.which("pdftotext")
    if not executable:
        raise RuntimeError("neither pypdf nor pdftotext is available")
    completed = subprocess.run(
        [executable, "-layout", str(path), "-"],
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    text = completed.stdout.decode("utf-8", errors="replace")
    pages = text.split("\f")
    if pages and not pages[-1].strip():
        pages.pop()
    return pages, {"extractor": "pdftotext-layout", "title": None, "author": None}


def extract(path: Path) -> tuple[list[str], dict[str, Any]]:
    try:
        return extract_with_pypdf(path)
    except ImportError:
        return extract_with_pdftotext(path)


def load_manifest(path: Path) -> dict[str, dict[str, Any]]:
    if not path.exists():
        return {}
    result = {}
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        row = json.loads(line)
        result[row["source_path"]] = row
    return result


def atomic_write_text(path: Path, content: str) -> None:
    """Write a text file by temporary sibling + atomic replace."""
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(
        "w",
        encoding="utf-8",
        dir=path.parent,
        delete=False,
        newline="\n",
    ) as handle:
        handle.write(content)
        temp = Path(handle.name)
    temp.replace(path)


def write_manifest(path: Path, rows: dict[str, dict[str, Any]]) -> None:
    content = "".join(json.dumps(rows[key], ensure_ascii=False, sort_keys=True) + "\n" for key in sorted(rows))
    atomic_write_text(path, content)


def is_excluded_relative(relative: Path) -> bool:
    return any(part in SKIP_PARTS for part in relative.parts)


def discovered_pdfs(root: Path) -> list[Path]:
    """Discover PDFs while pruning excluded/quarantined directory roots before descent."""
    found: list[Path] = []
    for current, dirs, files in os.walk(root):
        current_path = Path(current)
        relative_current = current_path.relative_to(root)
        if is_excluded_relative(relative_current):
            dirs[:] = []
            continue

        dirs[:] = sorted(
            [name for name in dirs if name not in SKIP_PARTS],
            key=str.casefold,
        )
        for name in sorted(files, key=str.casefold):
            if name.lower().endswith(".pdf"):
                found.append(current_path / name)
    return found


def pdfs(root: Path, supplied: list[Path]) -> list[Path]:
    if supplied:
        candidates: list[Path] = []
        for raw in supplied:
            path = (root / raw).resolve() if not raw.is_absolute() else raw.resolve()
            try:
                relative = path.relative_to(root)
            except ValueError as exc:
                raise ValueError(f"supplied path is outside repository root: {raw}") from exc
            if any(part in QUARANTINED_COMPONENTS for part in relative.parts):
                raise ValueError(f"refusing quarantined path: {relative.as_posix()}")
            if is_excluded_relative(relative):
                continue
            candidates.append(path)
    else:
        candidates = discovered_pdfs(root)

    return sorted(
        [path for path in candidates if path.is_file() and path.suffix.lower() == ".pdf"],
        key=lambda p: p.relative_to(root).as_posix().casefold(),
    )


def pending_pdfs(
    root: Path,
    candidates: list[Path],
    prior: dict[str, dict[str, Any]],
    force: bool,
    max_files: int | None,
) -> tuple[list[tuple[Path, str]], int]:
    """Return a bounded list of PDFs requiring work and the current-file count.

    The bound is applied after already-extracted files are removed. This makes
    repeated bounded runs advance through the corpus instead of selecting the
    same completed prefix forever.
    """
    limit = None if max_files is None else max(max_files, 0)
    planned: list[tuple[Path, str]] = []
    current = 0
    for path in candidates:
        if limit is not None and len(planned) >= limit:
            break
        rel = path.relative_to(root).as_posix()
        digest = file_sha256(path)
        existing = prior.get(rel)
        if (
            not force
            and existing
            and existing.get("sha256") == digest
            and existing.get("status") in {"extracted", "needs_ocr"}
        ):
            current += 1
            continue
        planned.append((path, digest))
    return planned, current


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="*", type=Path)
    parser.add_argument("--root", type=Path, default=Path("."))
    parser.add_argument("--output-root", type=Path, default=Path("derived/text"))
    parser.add_argument("--manifest", type=Path, default=Path("derived/manifests/extraction.jsonl"))
    parser.add_argument("--max-files", type=int)
    parser.add_argument("--min-chars-per-page", type=int, default=40)
    parser.add_argument("--force", action="store_true")
    parser.add_argument("--apply", action="store_true", help="Write derived outputs; default is dry-run")
    parser.add_argument(
        "--allow-errors",
        action="store_true",
        help="Record per-file errors without failing the batch",
    )
    args = parser.parse_args()

    root = args.root.resolve()
    manifest_path = root / args.manifest
    prior = load_manifest(manifest_path)
    try:
        candidates = pdfs(root, args.paths)
    except ValueError as exc:
        parser.error(str(exc))
    selected, current = pending_pdfs(
        root, candidates, prior, args.force, args.max_files
    )
    print(
        f"eligible_pdfs={len(candidates)} pending={len(selected)} already_current={current} "
        f"mode={'apply' if args.apply else 'dry-run'} quarantine_pruned=PRIOR_ART"
    )
    if not args.apply:
        for path, _digest in selected:
            print(f"would-process\t{path.relative_to(root).as_posix()}")
        return 0

    rows = dict(prior)
    # Remove any legacy manifest rows that point into quarantine so ordinary generated
    # state cannot continue to expose quarantined path metadata.
    rows = {
        key: value
        for key, value in rows.items()
        if not any(part in QUARANTINED_COMPONENTS for part in Path(key).parts)
    }

    summary = {"extracted": 0, "already_current": current, "needs_ocr": 0, "error": 0}
    for path, digest in selected:
        rel = path.relative_to(root).as_posix()
        record: dict[str, Any] = {
            "schema_version": 1,
            "tool_version": VERSION,
            "source_path": rel,
            "source_bytes": path.stat().st_size,
            "sha256": digest,
            "processed_at": iso_now(),
        }
        try:
            pages, metadata = extract(path)
            document = page_document(pages)
            text_chars = sum(len(re.sub(r"\s+", "", page)) for page in pages)
            threshold = args.min_chars_per_page * max(len(pages), 1)
            status = "needs_ocr" if text_chars < threshold else "extracted"
            output_rel = args.output_root / f"{digest}.txt"
            output = root / output_rel
            if not output.exists() or output.read_text(encoding="utf-8") != document:
                atomic_write_text(output, document)
            record.update(
                {
                    "status": status,
                    "pages": len(pages),
                    "text_characters_nonspace": text_chars,
                    "text_path": output_rel.as_posix(),
                    **metadata,
                }
            )
            summary[status] += 1
        except Exception as exc:
            record.update({"status": "error", "error": f"{type(exc).__name__}: {exc}"})
            summary["error"] += 1
        rows[rel] = record
    write_manifest(manifest_path, rows)
    print(" ".join(f"{key}={value}" for key, value in summary.items()))
    return 0 if args.allow_errors or not summary["error"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
