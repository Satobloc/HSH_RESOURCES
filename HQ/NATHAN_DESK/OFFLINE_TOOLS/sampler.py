#!/usr/bin/env python3
"""Build a deterministic, non-semantic source inventory and stratified sample manifest.

Purpose
-------
Inventory allowed repository trees without interpreting theory content. Record
file identity/size/hash/basic text statistics and produce reproducible stratified
samples for later extraction/availability QA.

HARD QUARANTINE
---------------
Any directory whose path component is exactly ``PRIOR_ART`` is pruned before
traversal. No file beneath it is opened, hashed, sampled, indexed, or listed.
Only an aggregate count of pruned quarantine roots is reported.

This tool assigns no theory authority, relevance, authorship, or quality status.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
import random
from collections import Counter, defaultdict
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable

TOOL_VERSION = "sable-source-inventory/0.1.0"
QUARANTINED_COMPONENTS = {"PRIOR_ART"}
TEXT_SUFFIXES = {
    ".txt", ".md", ".json", ".jsonl", ".csv", ".tsv", ".tex", ".py",
    ".yml", ".yaml", ".toml", ".ini", ".lean", ".wl", ".m", ".rst",
}


@dataclass(frozen=True)
class FileRecord:
    repository: str
    path: str
    topdir: str
    suffix: str
    kind: str
    size_bytes: int
    sha256: str
    line_count: int | None


def sha256_file(path: Path, chunk_size: int = 1024 * 1024) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        while True:
            chunk = handle.read(chunk_size)
            if not chunk:
                break
            digest.update(chunk)
    return digest.hexdigest()


def classify(path: Path) -> str:
    suffix = path.suffix.lower()
    if suffix in TEXT_SUFFIXES:
        return "text"
    if suffix == ".pdf":
        return "pdf"
    if suffix in {".png", ".jpg", ".jpeg", ".webp", ".gif", ".tif", ".tiff"}:
        return "image"
    return "other"


def line_count(path: Path) -> int | None:
    if path.suffix.lower() not in TEXT_SUFFIXES:
        return None
    try:
        with path.open("r", encoding="utf-8", errors="replace") as handle:
            return sum(1 for _ in handle)
    except OSError:
        return None


def contains_quarantined_component(relative: Path) -> bool:
    return any(part in QUARANTINED_COMPONENTS for part in relative.parts)


def iter_allowed_files(root: Path) -> tuple[Iterable[Path], int]:
    """Return allowed files plus count of quarantine roots pruned.

    ``os.walk`` pruning is intentional: files below PRIOR_ART are never touched.
    """
    allowed: list[Path] = []
    pruned_roots = 0
    for current, dirs, files in os.walk(root):
        current_path = Path(current)
        relative_current = current_path.relative_to(root)

        if contains_quarantined_component(relative_current):
            dirs[:] = []
            continue

        kept_dirs: list[str] = []
        for name in dirs:
            if name in QUARANTINED_COMPONENTS:
                pruned_roots += 1
            else:
                kept_dirs.append(name)
        dirs[:] = kept_dirs

        for name in files:
            path = current_path / name
            rel = path.relative_to(root)
            if not contains_quarantined_component(rel):
                allowed.append(path)
    return allowed, pruned_roots


def inventory_repo(label: str, root: Path) -> tuple[list[FileRecord], int]:
    files, pruned = iter_allowed_files(root)
    records: list[FileRecord] = []
    for path in sorted(files):
        rel = path.relative_to(root)
        stat = path.stat()
        topdir = rel.parts[0] if len(rel.parts) > 1 else "__ROOT__"
        records.append(
            FileRecord(
                repository=label,
                path=rel.as_posix(),
                topdir=topdir,
                suffix=path.suffix.lower(),
                kind=classify(path),
                size_bytes=stat.st_size,
                sha256=sha256_file(path),
                line_count=line_count(path),
            )
        )
    return records, pruned


def stratified_sample(
    records: list[FileRecord],
    per_stratum: int,
    seed: int,
) -> list[FileRecord]:
    groups: dict[tuple[str, str, str], list[FileRecord]] = defaultdict(list)
    for record in records:
        groups[(record.repository, record.topdir, record.kind)].append(record)

    rng = random.Random(seed)
    chosen: list[FileRecord] = []
    for key in sorted(groups):
        group = sorted(groups[key], key=lambda r: r.path)
        if len(group) <= per_stratum:
            chosen.extend(group)
        else:
            chosen.extend(rng.sample(group, per_stratum))
    return sorted(chosen, key=lambda r: (r.repository, r.topdir, r.kind, r.path))


def write_csv(path: Path, records: list[FileRecord]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fields = list(FileRecord.__dataclass_fields__)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for record in records:
            writer.writerow(asdict(record))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--repo",
        action="append",
        required=True,
        metavar="LABEL=PATH",
        help="Repository label and local checkout root. Repeat for multiple repos.",
    )
    parser.add_argument("--out-dir", type=Path, required=True)
    parser.add_argument("--sample-per-stratum", type=int, default=3)
    parser.add_argument("--seed", type=int, default=20260914)
    args = parser.parse_args()

    if args.sample_per_stratum < 1:
        parser.error("--sample-per-stratum must be >= 1")

    roots: list[tuple[str, Path]] = []
    for spec in args.repo:
        if "=" not in spec:
            parser.error(f"invalid --repo {spec!r}; expected LABEL=PATH")
        label, raw_path = spec.split("=", 1)
        root = Path(raw_path).expanduser().resolve()
        if not label.strip() or not root.is_dir():
            parser.error(f"invalid repository mapping: {spec!r}")
        roots.append((label.strip(), root))

    all_records: list[FileRecord] = []
    pruned_total = 0
    per_repo_pruned: dict[str, int] = {}
    for label, root in roots:
        records, pruned = inventory_repo(label, root)
        all_records.extend(records)
        pruned_total += pruned
        per_repo_pruned[label] = pruned

    all_records = sorted(all_records, key=lambda r: (r.repository, r.path))
    sample = stratified_sample(all_records, args.sample_per_stratum, args.seed)

    args.out_dir.mkdir(parents=True, exist_ok=True)
    write_csv(args.out_dir / "inventory.csv", all_records)
    write_csv(args.out_dir / "sample.csv", sample)

    inventory_sha = hashlib.sha256(
        "".join(
            f"{r.repository}\t{r.path}\t{r.size_bytes}\t{r.sha256}\n"
            for r in all_records
        ).encode("utf-8")
    ).hexdigest()

    summary = {
        "tool": TOOL_VERSION,
        "seed": args.seed,
        "sample_per_stratum": args.sample_per_stratum,
        "file_count": len(all_records),
        "sample_count": len(sample),
        "inventory_sha256": inventory_sha,
        "kinds": dict(sorted(Counter(r.kind for r in all_records).items())),
        "repositories": dict(sorted(Counter(r.repository for r in all_records).items())),
        "prior_art_quarantine_roots_pruned": pruned_total,
        "prior_art_pruned_by_repository": per_repo_pruned,
        "quarantine_policy": "PRIOR_ART path components are pruned before descent; contents are not opened, hashed, sampled, indexed, or listed.",
    }
    (args.out_dir / "summary.json").write_text(
        json.dumps(summary, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    print(json.dumps(summary, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
