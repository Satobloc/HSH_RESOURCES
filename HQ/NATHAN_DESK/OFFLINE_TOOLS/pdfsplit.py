#!/usr/bin/env python3
"""
split_pdf_24mb.py

Split one PDF, or every PDF in a folder, into page-contiguous PDF parts
that stay below a byte-size limit.

Default target: 23.5 MB = 23,500,000 bytes, deliberately below a 24 MB
upload limit to leave a little safety margin.

Requires:
    python -m pip install -U pypdf

Examples:
    python split_pdf_24mb.py "big.pdf"
    python split_pdf_24mb.py "C:\path\to\pdfs"
    python split_pdf_24mb.py "big.pdf" --max-mb 20
    python split_pdf_24mb.py "C:\path\to\pdfs" --recursive

If a single PDF page by itself is larger than the target, the script
reports that page instead of silently degrading or recompressing it.
"""

from __future__ import annotations

import argparse
import io
import sys
from pathlib import Path

try:
    from pypdf import PdfReader, PdfWriter
except ImportError:
    print(
        "pypdf is not installed.\n"
        "Run:\n"
        "  python -m pip install -U pypdf",
        file=sys.stderr,
    )
    raise SystemExit(2)


def mb_decimal(n: int) -> str:
    return f"{n / 1_000_000:.2f} MB"


def make_chunk_bytes(reader: PdfReader, start: int, end: int) -> bytes:
    """Serialize pages start..end inclusive and return the PDF bytes."""
    writer = PdfWriter()

    for page_index in range(start, end + 1):
        writer.add_page(reader.pages[page_index])

    # Preserve ordinary document metadata when possible.
    try:
        if reader.metadata:
            clean_meta = {}
            for key, value in reader.metadata.items():
                if isinstance(key, str) and value is not None:
                    clean_meta[key] = str(value)
            if clean_meta:
                writer.add_metadata(clean_meta)
    except Exception:
        pass

    buf = io.BytesIO()
    writer.write(buf)
    return buf.getvalue()


def largest_fitting_end(
    reader: PdfReader,
    start: int,
    max_bytes: int,
) -> tuple[int, bytes]:
    """
    Find the largest contiguous page range beginning at start that fits.
    Actual serialized PDF size is measured rather than estimated.
    """
    total_pages = len(reader.pages)

    # First make sure one page can fit at all.
    one_page = make_chunk_bytes(reader, start, start)
    if len(one_page) >= max_bytes:
        raise ValueError(
            f"Page {start + 1} alone is {mb_decimal(len(one_page))}, "
            f"which is not below the {mb_decimal(max_bytes)} target."
        )

    best_end = start
    best_bytes = one_page

    lo = start + 1
    hi = total_pages - 1

    # Binary search works well here because adding pages normally increases
    # serialized size. We still verify the selected result afterward.
    while lo <= hi:
        mid = (lo + hi) // 2
        data = make_chunk_bytes(reader, start, mid)

        if len(data) < max_bytes:
            best_end = mid
            best_bytes = data
            lo = mid + 1
        else:
            hi = mid - 1

    # Defensive forward check in case compression/resource sharing caused
    # an unusual non-monotonic result around the boundary.
    probe = best_end + 1
    while probe < total_pages:
        data = make_chunk_bytes(reader, start, probe)
        if len(data) < max_bytes:
            best_end = probe
            best_bytes = data
            probe += 1
        else:
            break

    return best_end, best_bytes


def split_pdf(pdf_path: Path, output_root: Path | None, max_bytes: int) -> None:
    print(f"\nReading: {pdf_path}")

    try:
        reader = PdfReader(str(pdf_path))
    except Exception as exc:
        print(f"  ERROR: could not open PDF: {exc}", file=sys.stderr)
        return

    if reader.is_encrypted:
        try:
            result = reader.decrypt("")
            if not result:
                print(
                    "  ERROR: PDF is encrypted and needs a password.",
                    file=sys.stderr,
                )
                return
        except Exception:
            print(
                "  ERROR: PDF is encrypted and needs a password.",
                file=sys.stderr,
            )
            return

    total_pages = len(reader.pages)
    if total_pages == 0:
        print("  Skipped: PDF has no pages.")
        return

    if output_root is None:
        out_dir = pdf_path.parent / f"{pdf_path.stem}_parts"
    else:
        out_dir = output_root / f"{pdf_path.stem}_parts"

    out_dir.mkdir(parents=True, exist_ok=True)

    start = 0
    part = 1
    outputs: list[Path] = []

    while start < total_pages:
        try:
            end, data = largest_fitting_end(reader, start, max_bytes)
        except ValueError as exc:
            print(f"  ERROR: {exc}", file=sys.stderr)
            print(
                "  This PDF cannot be split below the target by page boundaries "
                "without recompressing that oversized page.",
                file=sys.stderr,
            )
            return

        name = (
            f"{pdf_path.stem}_part{part:03d}"
            f"_p{start + 1:04d}-{end + 1:04d}.pdf"
        )
        out_path = out_dir / name
        out_path.write_bytes(data)

        actual = out_path.stat().st_size
        if actual >= max_bytes:
            print(
                f"  ERROR: verification failed for {out_path.name}: "
                f"{mb_decimal(actual)}",
                file=sys.stderr,
            )
            return

        outputs.append(out_path)
        print(
            f"  Part {part:03d}: pages {start + 1}-{end + 1} "
            f"-> {mb_decimal(actual)}"
        )

        start = end + 1
        part += 1

    print(
        f"  Done: {len(outputs)} part(s), {total_pages} page(s), "
        f"all below {mb_decimal(max_bytes)}"
    )
    print(f"  Output: {out_dir}")


def collect_pdfs(path: Path, recursive: bool) -> list[Path]:
    if path.is_file():
        if path.suffix.lower() != ".pdf":
            raise ValueError(f"Input file is not a PDF: {path}")
        return [path]

    if path.is_dir():
        pattern = "**/*.pdf" if recursive else "*.pdf"
        # Ignore our own previously generated *_parts directories.
        pdfs = [
            p for p in path.glob(pattern)
            if p.is_file() and not any(
                parent.name.endswith("_parts") for parent in p.parents
            )
        ]
        return sorted(pdfs)

    raise ValueError(f"Path does not exist: {path}")


def main() -> None:
    parser = argparse.ArgumentParser(
        description=(
            "Split PDFs into page-contiguous parts below a size limit. "
            "Default is 23.5 MB (23,500,000 bytes)."
        )
    )
    parser.add_argument(
        "input",
        help="PDF file or folder containing PDFs.",
    )
    parser.add_argument(
        "--max-mb",
        type=float,
        default=23.5,
        help=(
            "Maximum decimal MB target per output file. "
            "Default: 23.5. Each output must be strictly below this size."
        ),
    )
    parser.add_argument(
        "--output",
        help=(
            "Optional parent output folder. By default, each PDF gets a "
            "<filename>_parts folder next to the original."
        ),
    )
    parser.add_argument(
        "--recursive",
        action="store_true",
        help="When input is a folder, include PDFs in subfolders.",
    )
    args = parser.parse_args()

    if args.max_mb <= 0:
        parser.error("--max-mb must be greater than zero.")

    input_path = Path(args.input).expanduser().resolve()
    output_root = (
        Path(args.output).expanduser().resolve()
        if args.output
        else None
    )
    max_bytes = int(args.max_mb * 1_000_000)

    try:
        pdfs = collect_pdfs(input_path, args.recursive)
    except ValueError as exc:
        parser.error(str(exc))

    if not pdfs:
        print("No PDFs found.")
        return

    print(
        f"Found {len(pdfs)} PDF(s). "
        f"Target per part: strictly below {mb_decimal(max_bytes)}."
    )

    for pdf in pdfs:
        split_pdf(pdf, output_root, max_bytes)


if __name__ == "__main__":
    main()
