#!/usr/bin/env python3
"""
cern_raw.py — thin, conservative wrapper around CERN's official
cernopendata-client for inspecting and acquiring CERN Open Data files.

Why a wrapper?
- Keeps us from accidentally downloading an entire multi-GB/TB record.
- Makes manifests before downloads.
- Supports HTTP/HTTPS and XRootD locations.
- Uses CERN's client for file-index expansion, checksum metadata, and downloads.

Dependency:
    python -m pip install -U cernopendata-client

Examples:
    # Inspect a DELPHI record by DOI:
    python cern_raw.py files --doi 10.7483/OPENDATA.DELPHI.JUHY.E2AF

    # Or try a record identifier:
    python cern_raw.py files --recid delphi-87218

    # Write an XRootD manifest without downloading:
    python cern_raw.py manifest --doi 10.7483/OPENDATA.DELPHI.JUHY.E2AF \
        --protocol xrootd -o delphi_87218_manifest.json

    # Dry-run the first file only:
    python cern_raw.py download --doi 10.7483/OPENDATA.DELPHI.JUHY.E2AF \
        --range 1-1

    # Actually download + verify first file:
    python cern_raw.py download --doi 10.7483/OPENDATA.DELPHI.JUHY.E2AF \
        --range 1-1 --yes --verify

    # Print XRootD endpoints for remote streaming:
    python cern_raw.py stream --doi 10.7483/OPENDATA.DELPHI.JUHY.E2AF
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Optional

CLIENT = "cernopendata-client"
SERVER = "https://opendata.cern.ch"


@dataclass
class FileEntry:
    index: int
    url: str
    size_bytes: Optional[int] = None
    checksum: Optional[str] = None

    @property
    def name(self) -> str:
        return self.url.rstrip("/").rsplit("/", 1)[-1]


def die(msg: str, code: int = 2) -> None:
    print(f"ERROR: {msg}", file=sys.stderr)
    raise SystemExit(code)


def require_client() -> None:
    if shutil.which(CLIENT) is None:
        die(
            "cernopendata-client was not found.\n"
            "Install it with:\n"
            "  python -m pip install -U cernopendata-client"
        )


def selector_args(args: argparse.Namespace) -> list[str]:
    supplied = [
        ("--recid", getattr(args, "recid", None)),
        ("--doi", getattr(args, "doi", None)),
        ("--title", getattr(args, "title", None)),
    ]
    selected = [(flag, val) for flag, val in supplied if val]
    if len(selected) != 1:
        die("Supply exactly one of --recid, --doi, or --title.")
    flag, val = selected[0]
    return [flag, str(val)]


def run_client(cmd: list[str], capture: bool = False) -> subprocess.CompletedProcess:
    require_client()
    full = [CLIENT, *cmd]
    return subprocess.run(
        full,
        text=True,
        capture_output=capture,
        check=False,
    )


def parse_verbose_file_list(text: str) -> list[FileEntry]:
    """
    Expected CERN client verbose lines are roughly:
      URL    SIZE    adler32:CHECKSUM

    We intentionally parse leniently so plain URL-only lines still work.
    """
    entries: list[FileEntry] = []
    for raw in text.splitlines():
        line = raw.strip()
        if not line or line.startswith(("==>", "NOTE", "WARNING", "ERROR")):
            continue

        # Find URL first; tolerate informational prefixes.
        m = re.search(r'((?:https?|root)://\S+)', line)
        if not m:
            continue
        url = m.group(1)
        rest = line[m.end():].strip()

        size = None
        checksum = None

        # First integer after URL is normally bytes.
        sm = re.search(r'\b(\d+)\b', rest)
        if sm:
            try:
                size = int(sm.group(1))
            except ValueError:
                pass

        cm = re.search(r'\b(?:adler32|md5|sha1|sha256):[0-9A-Fa-f]+\b', rest)
        if cm:
            checksum = cm.group(0)

        entries.append(FileEntry(len(entries) + 1, url, size, checksum))
    return entries


def get_files(args: argparse.Namespace, protocol: Optional[str] = None) -> list[FileEntry]:
    protocol = protocol or args.protocol
    cmd = [
        "get-file-locations",
        *selector_args(args),
        "--server", SERVER,
        "--protocol", protocol,
        "--verbose",
    ]
    if getattr(args, "no_expand", False):
        cmd.append("--no-expand")
    else:
        cmd.append("--expand")

    proc = run_client(cmd, capture=True)
    if proc.returncode != 0:
        sys.stderr.write(proc.stderr)
        die("CERN client could not retrieve file locations.", proc.returncode)

    files = parse_verbose_file_list(proc.stdout)
    if not files:
        # Some versions may put useful output on stderr or format differently.
        print(proc.stdout)
        if proc.stderr:
            print(proc.stderr, file=sys.stderr)
        die("No file URLs could be parsed from the client output.")
    return files


def human_bytes(n: Optional[int]) -> str:
    if n is None:
        return "?"
    x = float(n)
    units = ["B", "KiB", "MiB", "GiB", "TiB"]
    for u in units:
        if x < 1024 or u == units[-1]:
            return f"{x:.2f} {u}" if u != "B" else f"{int(x)} B"
        x /= 1024
    return f"{n} B"


def print_file_table(files: list[FileEntry]) -> None:
    print(f"{'#':>4}  {'size':>12}  {'checksum':<22}  file")
    print("-" * 100)
    for f in files:
        print(
            f"{f.index:>4}  {human_bytes(f.size_bytes):>12}  "
            f"{(f.checksum or '-'):22}  {f.name}"
        )
    known = [f.size_bytes for f in files if f.size_bytes is not None]
    if known:
        print("-" * 100)
        print(f"{len(files)} files; known total = {human_bytes(sum(known))}")
    else:
        print(f"{len(files)} files")


def cmd_metadata(args: argparse.Namespace) -> None:
    proc = run_client([
        "get-metadata",
        *selector_args(args),
        "--server", SERVER,
    ])
    raise SystemExit(proc.returncode)


def cmd_files(args: argparse.Namespace) -> None:
    print_file_table(get_files(args))


def cmd_manifest(args: argparse.Namespace) -> None:
    files = get_files(args)
    manifest = {
        "server": SERVER,
        "selector": {
            "recid": args.recid,
            "doi": args.doi,
            "title": args.title,
        },
        "protocol": args.protocol,
        "expanded_indexes": not args.no_expand,
        "files": [asdict(f) | {"name": f.name} for f in files],
    }
    out = Path(args.output)
    out.write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    print(f"Wrote {out} with {len(files)} file entries.")


def cmd_stream(args: argparse.Namespace) -> None:
    # XRootD endpoints only; no download.
    args.protocol = "xrootd"
    files = get_files(args, protocol="xrootd")
    chosen = files
    if args.range:
        chosen = select_range(files, args.range)
    for f in chosen:
        print(f.url)


def select_range(files: list[FileEntry], spec: str) -> list[FileEntry]:
    """
    Parse CERN-style ranges: 1-3,7,10-12
    """
    wanted: set[int] = set()
    for token in spec.split(","):
        token = token.strip()
        if not token:
            continue
        if "-" in token:
            a, b = token.split("-", 1)
            lo, hi = int(a), int(b)
            if lo > hi:
                lo, hi = hi, lo
            wanted.update(range(lo, hi + 1))
        else:
            wanted.add(int(token))
    return [f for f in files if f.index in wanted]


def cmd_download(args: argparse.Namespace) -> None:
    # Show what the record contains before doing anything.
    files = get_files(args)
    print_file_table(files)

    cmd = [
        "download-files",
        *selector_args(args),
        "--server", SERVER,
        "--protocol", args.protocol,
    ]

    if args.regexp:
        cmd += ["--filter-regexp", args.regexp]
    if args.name:
        cmd += ["--filter-name", args.name]
    if args.range:
        cmd += ["--filter-range", args.range]
    if args.verify:
        cmd.append("--verify")

    if args.protocol == "xrootd":
        cmd += ["--download-engine", "xrootd"]
    elif args.engine:
        cmd += ["--download-engine", args.engine]

    # Safety default: dry run.
    if not args.yes:
        cmd.append("--dry-run")
        print("\nDRY RUN ONLY. Re-run with --yes to download.\n")
    else:
        print("\nStarting download...\n")

    proc = run_client(cmd)
    raise SystemExit(proc.returncode)


def add_selector(p: argparse.ArgumentParser) -> None:
    g = p.add_mutually_exclusive_group(required=True)
    g.add_argument("--recid", help="CERN Open Data record ID")
    g.add_argument("--doi", help="Record DOI")
    g.add_argument("--title", help="Exact record title")


def add_file_options(p: argparse.ArgumentParser) -> None:
    p.add_argument(
        "--protocol",
        choices=["http", "xrootd"],
        default="http",
        help="Location/download protocol (default: http)",
    )
    p.add_argument(
        "--no-expand",
        action="store_true",
        help="Do not expand file-index records.",
    )


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        description="Safe CERN Open Data record/file access wrapper."
    )
    sub = p.add_subparsers(dest="command", required=True)

    q = sub.add_parser("metadata", help="Show record metadata.")
    add_selector(q)
    q.set_defaults(func=cmd_metadata)

    q = sub.add_parser("files", help="List files, sizes, and checksums.")
    add_selector(q)
    add_file_options(q)
    q.set_defaults(func=cmd_files)

    q = sub.add_parser("manifest", help="Write a JSON manifest; no download.")
    add_selector(q)
    add_file_options(q)
    q.add_argument("-o", "--output", default="cern_manifest.json")
    q.set_defaults(func=cmd_manifest)

    q = sub.add_parser("stream", help="Print XRootD URLs; no download.")
    add_selector(q)
    q.add_argument("--range", help="Optional file range, e.g. 1-2,5")
    q.add_argument("--no-expand", action="store_true")
    q.set_defaults(protocol="xrootd", func=cmd_stream)

    q = sub.add_parser("download", help="Dry-run or download selected files.")
    add_selector(q)
    add_file_options(q)
    q.add_argument("--range", help="CERN-style file range, e.g. 1-2,5-7")
    q.add_argument("--name", help="Exact file name filter.")
    q.add_argument("--regexp", help="Regular-expression file-name filter.")
    q.add_argument(
        "--engine",
        choices=["requests", "pycurl"],
        default="pycurl",
        help="HTTP download engine; pycurl supports resume in CERN's Python client.",
    )
    q.add_argument("--verify", action="store_true", help="Verify after download.")
    q.add_argument(
        "--yes",
        action="store_true",
        help="Actually download. Without this flag, download is a dry run.",
    )
    q.set_defaults(func=cmd_download)

    return p


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
