#!/usr/bin/env python3
"""Consolidate original podcast audience CSVs from a checked-out repository.

Only *.csv inputs are considered, so generated files cannot recursively ingest themselves.
Preserves every original field, raw CSV, source path and SHA-256. Requires only stdlib.
"""
import csv
import hashlib
import io
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "EXPOSURE_STATS" / "AUDIENCE_METRICS"
DEST = SOURCE / "audience_metrics_complete.json"

def build():
    inputs = sorted(SOURCE.rglob("*.csv"), key=lambda p: p.relative_to(ROOT).as_posix().casefold())
    if not inputs:
        raise RuntimeError("No source CSV files found")
    data = []
    for file in inputs:
        raw = file.read_bytes()
        content = raw.decode("utf-8-sig")
        reader = csv.reader(io.StringIO(content, newline=""))
        table = list(reader)
        headers = table[0] if table else []
        rows = table[1:] if table else []
        if any(len(row) != len(headers) for row in rows):
            raise ValueError(f"CSV column mismatch: {file}")
        data.append({
            "source_path": file.relative_to(ROOT).as_posix(),
            "sha256": hashlib.sha256(raw).hexdigest(),
            "bytes": len(raw),
            "columns": headers,
            "row_count": len(rows),
            "rows": rows,
            "raw_csv": content,
        })
    result = {
        "schema_version": 1,
        "source_repository": "Satobloc/HSH_RESOURCES",
        "source_directory": SOURCE.relative_to(ROOT).as_posix(),
        "file_count": len(data),
        "total_data_rows": sum(x["row_count"] for x in data),
        "files": data,
    }
    serialized = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
    DEST.write_text(serialized, encoding="utf-8")
    found = json.loads(DEST.read_text(encoding="utf-8"))
    assert found["file_count"] == len(inputs)
    assert all(hashlib.sha256((b"\xef\xbb\xbf" if file.read_bytes().startswith(b"\xef\xbb\xbf") else b"") + x["raw_csv"].encode("utf-8")).hexdigest() == x["sha256"] for file, x in zip(inputs, found["files"]))
    print(json.dumps({"status": "VERIFIED_LOCAL", "csv_files": len(inputs), "rows": result["total_data_rows"], "output": DEST.relative_to(ROOT).as_posix()}))
    return result

if __name__ == "__main__":
    try: build()
    except Exception as exc:
        print(f"ERROR: {type(exc).__name__}: {exc}", file=sys.stderr)
        sys.exit(1)
