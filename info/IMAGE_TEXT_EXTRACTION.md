# Image and Scanned-PDF Text Extraction

`tools/extract_image_text.py` is the OCR companion to `tools/extract_papers.py`.

The ordinary PDF extractor should run first. It uses embedded PDF text when available and marks text-sparse/image-only files as `needs_ocr`. OCR is a slower, less reliable second stage and is therefore explicit rather than automatic.

## Requirements

The OCR tool uses external executables rather than adding large Python dependencies:

- **Tesseract OCR** — required for images and PDFs;
- **Poppler `pdftoppm`** — additionally required when OCRing PDFs.

Check the local installation without changing anything:

```text
py tools/extract_image_text.py --check-tools
```

## Safe defaults

The tool is dry-run by default. With no paths supplied it discovers ordinary image files in the repository; PDFs are not OCRed unless explicitly requested.

```text
py tools/extract_image_text.py
```

To write derived OCR text for images:

```text
py tools/extract_image_text.py --apply
```

To OCR only PDFs that `extract_papers.py` previously marked `needs_ocr`:

```text
py tools/extract_image_text.py --include-pdfs --apply
```

To process a bounded batch:

```text
py tools/extract_image_text.py --include-pdfs --max-files 20 --apply
```

To OCR selected files directly:

```text
py tools/extract_image_text.py "path/to/image.png" "path/to/scanned.pdf" --apply
```

`--all-pdfs` exists, but should be used sparingly: it rasterizes and OCRs every PDF even when good embedded text already exists.

## Outputs

Derived text is content-addressed:

```text
derived/image_text/<source-sha256>.txt
```

Each output preserves page boundaries as:

```text
===== PAGE 1 =====
...
```

The source-to-output map and extraction metadata are recorded in:

```text
derived/manifests/image_text_extraction.jsonl
```

Records include source path and size, SHA-256, source kind, tool version, processing time, OCR language, page-segmentation mode, DPI, Tesseract version, Poppler version where relevant, page count, extracted-character count, and output path.

The source image/PDF is never modified.

## Why OCR is separate

OCR errors are qualitatively different from ordinary text extraction errors. Equations, unusual symbols, subscripts, superscripts, diagrams, handwritten annotations, and low-resolution scans are particularly vulnerable. Keeping OCR in its own manifest lets later tooling distinguish:

- source-native text;
- deterministic PDF text extraction;
- machine OCR;
- reviewed/corrected transcription.

An OCR result makes an image searchable; it does **not** make the OCR transcription authoritative. Any quotation, equation, date, or priority-relevant wording should be checked against the source image/page.

## Recommended repository sequence

1. Run/update structural indexing.
2. Run `tools/extract_papers.py --apply` for PDFs.
3. Inspect the PDF manifest for `needs_ocr`.
4. Run this tool on native images and the `needs_ocr` PDF subset.
5. Run the accessibility audit to identify remaining gaps.
6. Review OCR manually when exact wording matters.

## Future extensions

Only add them in response to demonstrated archive gaps. Possible later adapters include handwriting-oriented transcription, table extraction, DOCX/PPTX/XLSX text extraction, and diagram metadata. Those should retain the same source-path/hash/manifest discipline rather than being folded invisibly into OCR output.
