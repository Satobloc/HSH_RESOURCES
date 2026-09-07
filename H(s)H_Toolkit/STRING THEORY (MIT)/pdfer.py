#!/usr/bin/env python3
"""
Combine every PDF in one folder into numbered PDFs that stay below configurable
size and extracted-word limits.

Default output names:
    HsHtoolkit_1.pdf
    HsHtoolkit_2.pdf
    ...

The defaults are designed for NotebookLM's per-source limits:
    hard size limit:  200 MB (decimal MB: 200,000,000 bytes)
    planning target: 190 MB
    hard word limit: 500,000 extracted words
    planning target: 480,000 extracted words

Important:
- Word counts are estimates based on text extractable from the PDFs.
- Scanned/image-only PDFs may report zero words unless they have an OCR text layer.
- The script writes candidate files and checks their actual byte size. If a
  candidate is too large, it automatically divides it further, down to page
  ranges when necessary.

Dependency:
    python -m pip install pypdf

Typical use in PowerShell:
    python combine_pdfs_for_notebooklm.py "D:\\__SAT26\\PDF_SOURCES"

Choose a different prefix or output folder:
    python combine_pdfs_for_notebooklm.py . --prefix HsHtoolkit --output-dir .\\combined

Skip the relatively slow word-count pass:
    python combine_pdfs_for_notebooklm.py . --no-word-count
"""

from __future__ import annotations

import argparse
import csv
import math
import re
import shutil
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Sequence

try:
    from pypdf import PdfReader, PdfWriter
except ImportError as exc:  # pragma: no cover - dependency guard
    raise SystemExit(
        "This script requires pypdf. Install it with:\n"
        "    python -m pip install pypdf"
    ) from exc


WORD_PATTERN = re.compile(r"\b[\w\u00C0-\u024F]+(?:[’'-][\w\u00C0-\u024F]+)*\b", re.UNICODE)


@dataclass(frozen=True)
class PdfSource:
    path: Path
    page_words: tuple[int, ...]
    size_bytes: int
    scanned_warning: bool = False

    @property
    def page_count(self) -> int:
        return len(self.page_words)

    @property
    def word_count(self) -> int:
        return sum(self.page_words)


@dataclass(frozen=True)
class PdfUnit:
    """A contiguous, zero-based, end-exclusive page range from one source PDF."""

    source: PdfSource
    start_page: int
    end_page: int

    @property
    def page_count(self) -> int:
        return self.end_page - self.start_page

    @property
    def word_count(self) -> int:
        return sum(self.source.page_words[self.start_page : self.end_page])

    @property
    def estimated_bytes(self) -> int:
        # PDF page sizes vary, but this is adequate for initial planning.
        # Every final output is checked against its actual on-disk byte size.
        if self.source.page_count <= 0:
            return self.source.size_bytes
        fraction = self.page_count / self.source.page_count
        return max(1, math.ceil(self.source.size_bytes * fraction))

    @property
    def label(self) -> str:
        if self.start_page == 0 and self.end_page == self.source.page_count:
            return self.source.path.name
        return (
            f"{self.source.path.name} "
            f"[pages {self.start_page + 1}-{self.end_page}]"
        )


@dataclass
class BuiltPart:
    temp_path: Path
    units: list[PdfUnit]
    size_bytes: int
    word_count: int


def natural_sort_key(path: Path) -> list[object]:
    """Sort names so file2.pdf comes before file10.pdf."""
    return [int(piece) if piece.isdigit() else piece.casefold() for piece in re.split(r"(\d+)", path.name)]


def count_words(text: str | None) -> int:
    if not text:
        return 0
    return len(WORD_PATTERN.findall(text))


def open_reader(path: Path) -> PdfReader:
    reader = PdfReader(str(path), strict=False)
    if reader.is_encrypted:
        # Some PDFs are flagged encrypted but allow opening with an empty password.
        result = reader.decrypt("")
        if result == 0:
            raise RuntimeError("PDF is encrypted and could not be opened without a password")
    return reader


def inspect_pdf(path: Path, do_word_count: bool) -> PdfSource:
    reader = open_reader(path)
    page_count = len(reader.pages)
    if page_count == 0:
        raise RuntimeError("PDF contains no pages")

    if do_word_count:
        page_words: list[int] = []
        failed_pages = 0
        for page_number, page in enumerate(reader.pages, start=1):
            try:
                page_words.append(count_words(page.extract_text()))
            except Exception as exc:  # keep the document usable, but report uncertainty
                failed_pages += 1
                page_words.append(0)
                print(
                    f"  WARNING: could not extract text from {path.name}, "
                    f"page {page_number}: {exc}",
                    file=sys.stderr,
                )
        total_words = sum(page_words)
        scanned_warning = total_words == 0 or failed_pages == page_count
    else:
        page_words = [0] * page_count
        scanned_warning = False

    return PdfSource(
        path=path,
        page_words=tuple(page_words),
        size_bytes=path.stat().st_size,
        scanned_warning=scanned_warning,
    )


def discover_pdfs(
    input_dir: Path,
    output_dir: Path,
    prefix: str,
    recursive: bool,
) -> list[Path]:
    iterator: Iterable[Path] = input_dir.rglob("*.pdf") if recursive else input_dir.glob("*.pdf")
    generated_name = re.compile(rf"^{re.escape(prefix)}_\d+\.pdf$", re.IGNORECASE)

    paths: list[Path] = []
    for path in iterator:
        if not path.is_file():
            continue
        # Do not ingest outputs from an earlier run when output and input overlap.
        if path.parent.resolve() == output_dir.resolve() and generated_name.match(path.name):
            continue
        paths.append(path)

    return sorted(paths, key=natural_sort_key)


def choose_page_split(unit: PdfUnit) -> int:
    """Choose an internal page boundary that roughly balances size and words."""
    if unit.page_count < 2:
        raise ValueError("Cannot split a one-page unit")

    if unit.word_count > 0:
        target = unit.word_count / 2
        running = 0
        best_boundary = unit.start_page + 1
        best_error = float("inf")
        for boundary in range(unit.start_page + 1, unit.end_page):
            running += unit.source.page_words[boundary - 1]
            error = abs(running - target)
            if error < best_error:
                best_error = error
                best_boundary = boundary
        return best_boundary

    return unit.start_page + unit.page_count // 2


def presplit_unit(
    unit: PdfUnit,
    target_bytes: int,
    target_words: int | None,
) -> list[PdfUnit]:
    """Avoid initially writing extremely oversized candidates."""
    bytes_ok = unit.estimated_bytes <= target_bytes
    words_ok = target_words is None or unit.word_count <= target_words
    if bytes_ok and words_ok:
        return [unit]
    if unit.page_count == 1:
        return [unit]

    boundary = choose_page_split(unit)
    left = PdfUnit(unit.source, unit.start_page, boundary)
    right = PdfUnit(unit.source, boundary, unit.end_page)
    return presplit_unit(left, target_bytes, target_words) + presplit_unit(
        right, target_bytes, target_words
    )


def create_planned_batches(
    units: Sequence[PdfUnit],
    target_bytes: int,
    target_words: int | None,
) -> list[list[PdfUnit]]:
    batches: list[list[PdfUnit]] = []
    current: list[PdfUnit] = []
    current_bytes = 0
    current_words = 0

    for unit in units:
        would_exceed_bytes = current and current_bytes + unit.estimated_bytes > target_bytes
        would_exceed_words = (
            current
            and target_words is not None
            and current_words + unit.word_count > target_words
        )

        if would_exceed_bytes or would_exceed_words:
            batches.append(current)
            current = []
            current_bytes = 0
            current_words = 0

        current.append(unit)
        current_bytes += unit.estimated_bytes
        current_words += unit.word_count

    if current:
        batches.append(current)

    return batches


def write_units(units: Sequence[PdfUnit], output_path: Path) -> None:
    writer = PdfWriter()

    for unit in units:
        reader = open_reader(unit.source.path)
        for page_index in range(unit.start_page, unit.end_page):
            writer.add_page(reader.pages[page_index])

    # A small, neutral metadata block. Source-level metadata is intentionally not
    # combined because conflicting document metadata is common in merged corpora.
    writer.add_metadata(
        {
            "/Title": "HsH / SAT source toolkit",
            "/Producer": "combine_pdfs_for_notebooklm.py using pypdf",
        }
    )

    with output_path.open("wb") as file_obj:
        writer.write(file_obj)

    # Reopen the result immediately to catch truncated or structurally invalid output.
    verification_reader = open_reader(output_path)
    expected_pages = sum(unit.page_count for unit in units)
    actual_pages = len(verification_reader.pages)
    if actual_pages != expected_pages:
        raise RuntimeError(
            f"Verification failed for {output_path.name}: "
            f"expected {expected_pages} pages, found {actual_pages}"
        )


def choose_unit_split(units: Sequence[PdfUnit]) -> int:
    """Choose a unit boundary that approximately balances estimated workload."""
    if len(units) < 2:
        raise ValueError("Need at least two units to choose a unit split")

    weights = [
        max(unit.estimated_bytes, unit.word_count * 8, 1)
        for unit in units
    ]
    target = sum(weights) / 2
    running = 0
    best_index = 1
    best_error = float("inf")

    for index in range(1, len(units)):
        running += weights[index - 1]
        error = abs(running - target)
        if error < best_error:
            best_error = error
            best_index = index

    return best_index


def build_fitting_parts(
    units: Sequence[PdfUnit],
    temp_dir: Path,
    hard_max_bytes: int,
    hard_max_words: int | None,
    sequence: list[int],
) -> list[BuiltPart]:
    """
    Write a candidate, check its exact size, and recursively divide it if needed.
    """
    if not units:
        return []

    sequence[0] += 1
    candidate = temp_dir / f"candidate_{sequence[0]:06d}.pdf"
    write_units(units, candidate)

    actual_bytes = candidate.stat().st_size
    words = sum(unit.word_count for unit in units)
    size_ok = actual_bytes <= hard_max_bytes
    words_ok = hard_max_words is None or words <= hard_max_words

    if size_ok and words_ok:
        return [
            BuiltPart(
                temp_path=candidate,
                units=list(units),
                size_bytes=actual_bytes,
                word_count=words,
            )
        ]

    candidate.unlink(missing_ok=True)

    reason_parts: list[str] = []
    if not size_ok:
        reason_parts.append(
            f"{actual_bytes / 1_000_000:.2f} MB > {hard_max_bytes / 1_000_000:.2f} MB"
        )
    if not words_ok and hard_max_words is not None:
        reason_parts.append(f"{words:,} words > {hard_max_words:,} words")
    print(f"  Dividing candidate ({'; '.join(reason_parts)})")

    if len(units) > 1:
        split_index = choose_unit_split(units)
        left_units = units[:split_index]
        right_units = units[split_index:]
    else:
        unit = units[0]
        if unit.page_count == 1:
            raise RuntimeError(
                "A single PDF page cannot fit within the configured limit:\n"
                f"  {unit.label}\n"
                f"  Generated size: {actual_bytes / 1_000_000:.2f} MB\n"
                "Reduce the page's image resolution/compression, or increase the limit."
            )
        boundary = choose_page_split(unit)
        left_units = [PdfUnit(unit.source, unit.start_page, boundary)]
        right_units = [PdfUnit(unit.source, boundary, unit.end_page)]

    return build_fitting_parts(
        left_units,
        temp_dir,
        hard_max_bytes,
        hard_max_words,
        sequence,
    ) + build_fitting_parts(
        right_units,
        temp_dir,
        hard_max_bytes,
        hard_max_words,
        sequence,
    )


def write_manifest(
    manifest_path: Path,
    finalized_parts: Sequence[tuple[Path, BuiltPart]],
) -> None:
    with manifest_path.open("w", newline="", encoding="utf-8-sig") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(
            [
                "output_file",
                "output_bytes",
                "output_MB_decimal",
                "estimated_extracted_words",
                "source_pdf",
                "source_start_page",
                "source_end_page",
                "source_pages_in_output",
            ]
        )

        for output_path, part in finalized_parts:
            for unit in part.units:
                writer.writerow(
                    [
                        output_path.name,
                        part.size_bytes,
                        f"{part.size_bytes / 1_000_000:.3f}",
                        part.word_count,
                        str(unit.source.path),
                        unit.start_page + 1,
                        unit.end_page,
                        unit.page_count,
                    ]
                )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Merge PDFs from one folder into numbered outputs while enforcing "
            "actual file-size and optional extracted-word limits."
        )
    )
    parser.add_argument(
        "input_dir",
        nargs="?",
        default=".",
        help="Folder containing input PDFs (default: current folder)",
    )
    parser.add_argument(
        "--output-dir",
        default=None,
        help="Output folder (default: input folder)",
    )
    parser.add_argument(
        "--prefix",
        default="HsHtoolkit",
        help="Output filename prefix (default: HsHtoolkit)",
    )
    parser.add_argument(
        "--max-mb",
        type=float,
        default=200.0,
        help="Hard maximum output size in decimal MB (default: 200)",
    )
    parser.add_argument(
        "--target-mb",
        type=float,
        default=190.0,
        help="Planning target in decimal MB; must not exceed --max-mb (default: 190)",
    )
    parser.add_argument(
        "--max-words",
        type=int,
        default=500_000,
        help="Hard maximum estimated extracted words per output (default: 500000)",
    )
    parser.add_argument(
        "--target-words",
        type=int,
        default=480_000,
        help="Planning target words; must not exceed --max-words (default: 480000)",
    )
    parser.add_argument(
        "--no-word-count",
        action="store_true",
        help="Do not extract/count text; enforce only file-size limits",
    )
    parser.add_argument(
        "--recursive",
        action="store_true",
        help="Include PDFs in subfolders",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Replace existing numbered outputs and manifest with the same prefix",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    input_dir = Path(args.input_dir).expanduser().resolve()
    output_dir = (
        Path(args.output_dir).expanduser().resolve()
        if args.output_dir
        else input_dir
    )

    if not input_dir.is_dir():
        print(f"ERROR: input folder does not exist: {input_dir}", file=sys.stderr)
        return 2
    output_dir.mkdir(parents=True, exist_ok=True)

    if args.max_mb <= 0 or args.target_mb <= 0:
        print("ERROR: size limits must be positive", file=sys.stderr)
        return 2
    if args.target_mb > args.max_mb:
        print("ERROR: --target-mb cannot exceed --max-mb", file=sys.stderr)
        return 2
    if not args.no_word_count:
        if args.max_words <= 0 or args.target_words <= 0:
            print("ERROR: word limits must be positive", file=sys.stderr)
            return 2
        if args.target_words > args.max_words:
            print("ERROR: --target-words cannot exceed --max-words", file=sys.stderr)
            return 2

    hard_max_bytes = int(args.max_mb * 1_000_000)
    target_bytes = int(args.target_mb * 1_000_000)
    hard_max_words = None if args.no_word_count else args.max_words
    target_words = None if args.no_word_count else args.target_words

    pdf_paths = discover_pdfs(
        input_dir=input_dir,
        output_dir=output_dir,
        prefix=args.prefix,
        recursive=args.recursive,
    )

    if not pdf_paths:
        print(f"No input PDFs found in: {input_dir}")
        return 1

    existing_outputs = sorted(output_dir.glob(f"{args.prefix}_[0-9]*.pdf"))
    manifest_path = output_dir / f"{args.prefix}_manifest.csv"
    if (existing_outputs or manifest_path.exists()) and not args.overwrite:
        print(
            "ERROR: output files already exist. Use --overwrite to replace them:\n"
            + "\n".join(f"  {path}" for path in [*existing_outputs, manifest_path] if path.exists()),
            file=sys.stderr,
        )
        return 2

    if args.overwrite:
        for path in existing_outputs:
            path.unlink()
        manifest_path.unlink(missing_ok=True)

    print(f"Input folder : {input_dir}")
    print(f"Output folder: {output_dir}")
    print(f"PDFs found  : {len(pdf_paths)}")
    print(f"Hard size   : {args.max_mb:.2f} MB decimal")
    print(f"Target size : {args.target_mb:.2f} MB decimal")
    if hard_max_words is None:
        print("Word count  : disabled")
    else:
        print(f"Hard words  : {hard_max_words:,}")
        print(f"Target words: {target_words:,}")

    print("\nInspecting PDFs...")
    sources: list[PdfSource] = []
    for index, path in enumerate(pdf_paths, start=1):
        print(f"[{index}/{len(pdf_paths)}] {path.name}")
        try:
            source = inspect_pdf(path, do_word_count=not args.no_word_count)
        except Exception as exc:
            print(f"ERROR reading {path}: {exc}", file=sys.stderr)
            return 3
        sources.append(source)
        details = (
            f"  {source.page_count:,} pages, "
            f"{source.size_bytes / 1_000_000:.2f} MB"
        )
        if not args.no_word_count:
            details += f", about {source.word_count:,} extracted words"
        print(details)
        if source.scanned_warning:
            print(
                "  WARNING: no extractable words were found. This may be an "
                "image-only/scanned PDF without OCR.",
                file=sys.stderr,
            )

    units: list[PdfUnit] = []
    for source in sources:
        whole = PdfUnit(source, 0, source.page_count)
        units.extend(presplit_unit(whole, target_bytes, target_words))

    planned_batches = create_planned_batches(units, target_bytes, target_words)
    print(
        f"\nInitial plan: {len(units)} source/page-range unit(s) in "
        f"{len(planned_batches)} candidate batch(es)."
    )

    built_parts: list[BuiltPart] = []
    sequence = [0]

    try:
        with tempfile.TemporaryDirectory(prefix="hsh_pdf_merge_", dir=str(output_dir)) as temp_name:
            temp_dir = Path(temp_name)
            for batch_number, batch in enumerate(planned_batches, start=1):
                print(f"Building candidate batch {batch_number}/{len(planned_batches)}...")
                built_parts.extend(
                    build_fitting_parts(
                        units=batch,
                        temp_dir=temp_dir,
                        hard_max_bytes=hard_max_bytes,
                        hard_max_words=hard_max_words,
                        sequence=sequence,
                    )
                )

            finalized_parts: list[tuple[Path, BuiltPart]] = []
            for index, part in enumerate(built_parts, start=1):
                final_path = output_dir / f"{args.prefix}_{index}.pdf"
                shutil.move(str(part.temp_path), final_path)
                finalized_parts.append((final_path, part))

            write_manifest(manifest_path, finalized_parts)

    except Exception as exc:
        print(f"\nERROR: {exc}", file=sys.stderr)
        return 4

    print("\nCompleted successfully:")
    for final_path, part in finalized_parts:
        words_text = (
            "word count disabled"
            if hard_max_words is None
            else f"about {part.word_count:,} extracted words"
        )
        print(
            f"  {final_path.name}: {part.size_bytes / 1_000_000:.2f} MB, "
            f"{words_text}, {sum(unit.page_count for unit in part.units):,} pages"
        )
    print(f"  Manifest: {manifest_path.name}")

    if any(source.scanned_warning for source in sources) and not args.no_word_count:
        print(
            "\nNOTE: At least one source had no extractable text. Its NotebookLM "
            "word count may differ after ingestion. OCR those PDFs first for a "
            "more meaningful preflight word estimate."
        )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
