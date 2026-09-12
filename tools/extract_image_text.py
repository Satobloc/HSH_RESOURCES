#!/usr/bin/env python3
"""OCR image files and image-only PDFs without modifying source material.

This is the second-stage companion to tools/extract_papers.py. The PDF text
extractor deliberately marks sparse/image-only PDFs as ``needs_ocr``; this tool
can consume that manifest and OCR only those files.

Dry-run is the default. Pass --apply to write derived text plus a deterministic
JSONL manifest. OCR requires the external ``tesseract`` executable. PDF OCR
additionally requires ``pdftoppm`` (Poppler).
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
from typing import Any, Iterable

VERSION = "1.0.0"
IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".tif", ".tiff", ".bmp", ".webp"}
SKIP_PARTS = {".git", "derived", "__pycache__", ".pytest_cache"}


def iso_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    rows: list[dict[str, Any]] = []
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            row = json.loads(line)
        except json.JSONDecodeError as exc:
            raise ValueError(f"{path}:{line_number}: invalid JSONL: {exc}") from exc
        if isinstance(row, dict):
            rows.append(row)
    return rows


def load_manifest_by_source(path: Path) -> dict[str, dict[str, Any]]:
    return {
        row["source_path"]: row
        for row in load_jsonl(path)
        if isinstance(row.get("source_path"), str)
    }


def write_manifest(path: Path, rows: dict[str, dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    content = "".join(
        json.dumps(rows[key], ensure_ascii=False, sort_keys=True) + "\n"
        for key in sorted(rows)
    )
    with tempfile.NamedTemporaryFile(
        "w", encoding="utf-8", dir=path.parent, delete=False, newline="\n"
    ) as handle:
        handle.write(content)
        temporary = Path(handle.name)
    temporary.replace(path)


def normalized_rel(root: Path, path: Path) -> str:
    return path.resolve().relative_to(root).as_posix()


def is_skipped(root: Path, path: Path) -> bool:
    try:
        parts = path.resolve().relative_to(root).parts
    except ValueError:
        return True
    return any(part in SKIP_PARTS for part in parts)


def discover_images(root: Path, supplied: list[Path]) -> list[Path]:
    if supplied:
        candidates = [
            (root / item).resolve() if not item.is_absolute() else item.resolve()
            for item in supplied
        ]
    else:
        candidates = sorted(root.rglob("*"), key=lambda path: path.as_posix().casefold())
    return [
        path
        for path in candidates
        if path.is_file()
        and path.suffix.lower() in IMAGE_EXTENSIONS
        and not is_skipped(root, path)
    ]


def discover_ocr_pdfs(
    root: Path,
    manifest: Path,
    supplied: list[Path],
    all_pdfs: bool,
) -> list[Path]:
    supplied_pdfs: list[Path] = []
    for item in supplied:
        path = (root / item).resolve() if not item.is_absolute() else item.resolve()
        if path.is_file() and path.suffix.lower() == ".pdf" and not is_skipped(root, path):
            supplied_pdfs.append(path)

    if supplied_pdfs:
        return sorted(set(supplied_pdfs), key=lambda path: path.as_posix().casefold())

    if all_pdfs:
        return [
            path
            for path in sorted(root.rglob("*.pdf"), key=lambda item: item.as_posix().casefold())
            if path.is_file() and not is_skipped(root, path)
        ]

    selected: list[Path] = []
    for row in load_jsonl(root / manifest):
        if row.get("status") != "needs_ocr" or not isinstance(row.get("source_path"), str):
            continue
        path = (root / row["source_path"]).resolve()
        if path.is_file() and path.suffix.lower() == ".pdf" and not is_skipped(root, path):
            selected.append(path)
    return sorted(set(selected), key=lambda path: path.as_posix().casefold())


def executable_version(executable: str, arguments: list[str]) -> str | None:
    try:
        completed = subprocess.run(
            [executable, *arguments],
            check=False,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            encoding="utf-8",
            errors="replace",
        )
    except OSError:
        return None
    lines = (completed.stdout or "").splitlines()
    return lines[0].strip() if lines else None


def ocr_image(tesseract: str, image: Path, languages: str, psm: int, dpi: int) -> str:
    completed = subprocess.run(
        [
            tesseract,
            str(image),
            "stdout",
            "-l",
            languages,
            "--psm",
            str(psm),
            "--dpi",
            str(dpi),
            "quiet",
        ],
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    return (
        completed.stdout.decode("utf-8", errors="replace")
        .replace("\r\n", "\n")
        .replace("\r", "\n")
    )


def page_document(pages: Iterable[str]) -> str:
    return "\n".join(
        f"===== PAGE {number} =====\n{text.strip()}\n"
        for number, text in enumerate(pages, 1)
    )


def rasterize_pdf(pdftoppm: str, pdf: Path, output_dir: Path, dpi: int) -> list[Path]:
    prefix = output_dir / "page"
    subprocess.run(
        [pdftoppm, "-png", "-r", str(dpi), str(pdf), str(prefix)],
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )

    def page_number(path: Path) -> int:
        match = re.search(r"-(\d+)\.png$", path.name)
        return int(match.group(1)) if match else 10**9

    return sorted(output_dir.glob("page-*.png"), key=page_number)


def process_image(
    path: Path,
    *,
    tesseract: str,
    languages: str,
    psm: int,
    dpi: int,
) -> tuple[str, int]:
    return page_document([ocr_image(tesseract, path, languages, psm, dpi)]), 1


def process_pdf(
    path: Path,
    *,
    tesseract: str,
    pdftoppm: str,
    languages: str,
    psm: int,
    dpi: int,
) -> tuple[str, int]:
    with tempfile.TemporaryDirectory(prefix="hsh-ocr-") as temporary_name:
        images = rasterize_pdf(pdftoppm, path, Path(temporary_name), dpi)
        if not images:
            raise RuntimeError("pdftoppm produced no page images")
        pages = [ocr_image(tesseract, image, languages, psm, dpi) for image in images]
        return page_document(pages), len(pages)


def pending(
    root: Path,
    paths: list[Path],
    prior: dict[str, dict[str, Any]],
    force: bool,
    max_files: int | None,
) -> tuple[list[tuple[Path, str]], int]:
    limit = None if max_files is None else max(max_files, 0)
    planned: list[tuple[Path, str]] = []
    current = 0
    for path in paths:
        if limit is not None and len(planned) >= limit:
            break
        rel = normalized_rel(root, path)
        digest = file_sha256(path)
        existing = prior.get(rel)
        if (
            not force
            and existing
            and existing.get("sha256") == digest
            and existing.get("status") == "extracted"
        ):
            current += 1
            continue
        planned.append((path, digest))
    return planned, current


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="*", type=Path)
    parser.add_argument("--root", type=Path, default=Path("."))
    parser.add_argument("--output-root", type=Path, default=Path("derived/image_text"))
    parser.add_argument(
        "--manifest",
        type=Path,
        default=Path("derived/manifests/image_text_extraction.jsonl"),
    )
    parser.add_argument(
        "--pdf-extraction-manifest",
        type=Path,
        default=Path("derived/manifests/extraction.jsonl"),
        help="Manifest written by extract_papers.py; entries marked needs_ocr are selected.",
    )
    parser.add_argument("--include-pdfs", action="store_true")
    parser.add_argument(
        "--all-pdfs",
        action="store_true",
        help="OCR every PDF instead of only supplied/needs_ocr PDFs. Use sparingly.",
    )
    parser.add_argument("--languages", default="eng")
    parser.add_argument("--psm", type=int, default=3)
    parser.add_argument("--dpi", type=int, default=300)
    parser.add_argument("--max-files", type=int)
    parser.add_argument("--force", action="store_true")
    parser.add_argument("--apply", action="store_true", help="Write derived outputs; default is dry-run")
    parser.add_argument("--allow-errors", action="store_true")
    parser.add_argument("--check-tools", action="store_true")
    args = parser.parse_args()

    root = args.root.resolve()
    if not root.is_dir():
        print(f"error: root directory not found: {root}")
        return 2

    tesseract = shutil.which("tesseract")
    pdftoppm = shutil.which("pdftoppm")

    if args.check_tools:
        print(f"tesseract={tesseract or 'missing'}")
        print(
            "tesseract_version="
            + str(executable_version(tesseract, ["--version"]) if tesseract else "missing")
        )
        print(f"pdftoppm={pdftoppm or 'missing'}")
        print(
            "pdftoppm_version="
            + str(executable_version(pdftoppm, ["-v"]) if pdftoppm else "missing")
        )
        return 0 if tesseract else 1

    if not tesseract:
        print("error: tesseract executable not found on PATH")
        return 2

    images = discover_images(root, args.paths)
    pdfs: list[Path] = []
    if args.include_pdfs or args.all_pdfs or any(item.suffix.lower() == ".pdf" for item in args.paths):
        pdfs = discover_ocr_pdfs(root, args.pdf_extraction_manifest, args.paths, args.all_pdfs)
        if pdfs and not pdftoppm:
            print("error: pdftoppm is required for PDF OCR but was not found on PATH")
            return 2

    candidates = sorted(
        set(images + pdfs),
        key=lambda path: normalized_rel(root, path).casefold(),
    )
    manifest_path = root / args.manifest
    prior = load_manifest_by_source(manifest_path)
    selected, current = pending(root, candidates, prior, args.force, args.max_files)
    print(
        f"candidates={len(candidates)} pending={len(selected)} already_current={current} "
        f"mode={'apply' if args.apply else 'dry-run'}"
    )

    if not args.apply:
        for path, _digest in selected:
            print(f"would-process\t{normalized_rel(root, path)}")
        return 0

    rows = dict(prior)
    summary = {"extracted": 0, "already_current": current, "error": 0}
    tesseract_version = executable_version(tesseract, ["--version"])
    pdftoppm_version = executable_version(pdftoppm, ["-v"]) if pdftoppm else None

    for path, digest in selected:
        rel = normalized_rel(root, path)
        record: dict[str, Any] = {
            "schema_version": 1,
            "tool_version": VERSION,
            "source_path": rel,
            "source_bytes": path.stat().st_size,
            "source_kind": "pdf" if path.suffix.lower() == ".pdf" else "image",
            "sha256": digest,
            "processed_at": iso_now(),
            "languages": args.languages,
            "psm": args.psm,
            "dpi": args.dpi,
            "tesseract_version": tesseract_version,
        }
        try:
            if path.suffix.lower() == ".pdf":
                if not pdftoppm:
                    raise RuntimeError("pdftoppm unavailable")
                document, pages = process_pdf(
                    path,
                    tesseract=tesseract,
                    pdftoppm=pdftoppm,
                    languages=args.languages,
                    psm=args.psm,
                    dpi=args.dpi,
                )
                record["pdftoppm_version"] = pdftoppm_version
            else:
                document, pages = process_image(
                    path,
                    tesseract=tesseract,
                    languages=args.languages,
                    psm=args.psm,
                    dpi=args.dpi,
                )
            output_rel = args.output_root / f"{digest}.txt"
            output = root / output_rel
            output.parent.mkdir(parents=True, exist_ok=True)
            if not output.exists() or output.read_text(encoding="utf-8") != document:
                output.write_text(document, encoding="utf-8", newline="\n")
            record.update(
                {
                    "status": "extracted",
                    "pages": pages,
                    "text_characters_nonspace": len(re.sub(r"\s+", "", document)),
                    "text_path": output_rel.as_posix(),
                }
            )
            summary["extracted"] += 1
        except Exception as exc:
            record.update({"status": "error", "error": f"{type(exc).__name__}: {exc}"})
            summary["error"] += 1
        rows[rel] = record

    write_manifest(manifest_path, rows)
    print(" ".join(f"{key}={value}" for key, value in summary.items()))
    return 0 if args.allow_errors or not summary["error"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
