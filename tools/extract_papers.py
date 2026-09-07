#!/usr/bin/env python3
"""Extract page-marked text from PDFs without modifying source files.

Dry-run is the default. Pass --apply to create derived text and a deterministic
current-state manifest. OCR is deliberately not automatic.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import subprocess
import tempfile
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

VERSION = "1.1.0"
SKIP_PARTS = {".git", "derived", "__pycache__", ".pytest_cache"}


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


def write_manifest(path: Path, rows: dict[str, dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    content = "".join(json.dumps(rows[key], ensure_ascii=False, sort_keys=True) + "\n" for key in sorted(rows))
    with tempfile.NamedTemporaryFile("w", encoding="utf-8", dir=path.parent, delete=False, newline="\n") as handle:
        handle.write(content)
        temp = Path(handle.name)
    temp.replace(path)


def pdfs(root: Path, supplied: list[Path]) -> list[Path]:
    if supplied:
        candidates = [(root / path).resolve() if not path.is_absolute() else path.resolve() for path in supplied]
    else:
        candidates = sorted(root.rglob("*.pdf"), key=lambda p: p.as_posix().casefold())
    return [
        path for path in candidates
        if path.is_file() and path.suffix.lower() == ".pdf" and not any(part in SKIP_PARTS for part in path.relative_to(root).parts)
    ]


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
    args = parser.parse_args()

    root = args.root.resolve()
    manifest_path = root / args.manifest
    prior = load_manifest(manifest_path)
    selected, current = pending_pdfs(
        root, pdfs(root, args.paths), prior, args.force, args.max_files
    )
    print(
        f"pending={len(selected)} already_current={current} "
        f"mode={'apply' if args.apply else 'dry-run'}"
    )
    if not args.apply:
        for path, _digest in selected:
            print(f"would-process\t{path.relative_to(root).as_posix()}")
        return 0

    rows = dict(prior)
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
            output.parent.mkdir(parents=True, exist_ok=True)
            if not output.exists() or output.read_text(encoding="utf-8") != document:
                output.write_text(document, encoding="utf-8", newline="\n")
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
    return 1 if summary["error"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
