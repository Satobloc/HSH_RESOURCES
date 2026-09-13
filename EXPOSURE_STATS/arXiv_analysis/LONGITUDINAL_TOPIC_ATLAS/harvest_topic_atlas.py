#!/usr/bin/env python3
"""Neutral arXiv longitudinal-topic atlas harvester.

This script intentionally contains no SAT/H(s)H vocabulary or classifier.
It builds external comparison infrastructure from the official arXiv OAI-PMH
metadata service.

Sampling design
---------------
For each requested year:
  * choose K calendar days uniformly at random from the eligible part of year;
  * harvest ALL records in arXiv's broad `physics` set on each selected day;
  * retain native arXiv categories and metadata;
  * deduplicate cross-listed/revised records by arXiv id;
  * if the pooled cluster sample exceeds --max-per-year, make a deterministic
    simple random subsample for the compact comparison file while preserving
    the complete harvested-day pool separately.

Uniform random-day cluster sampling is not IID paper sampling. It is useful for
longitudinal topic prevalence because every eligible calendar day has equal
inclusion probability and all papers on an included day are harvested. The
metadata records sampled days and counts so later analyses can use cluster-aware
uncertainty estimates.

The script also snapshots OAI ListSets so current arXiv taxonomy/set names are
stored verbatim rather than reconstructed from memory.
"""
from __future__ import annotations

import argparse
import csv
import datetime as dt
import json
import random
import re
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from dataclasses import asdict, dataclass
from pathlib import Path

API = "https://oaipmh.arxiv.org/oai"
OAI = "http://www.openarchives.org/OAI/2.0/"
ARXIV = "http://arxiv.org/OAI/arXiv/"
USER_AGENT = "HsH-ArxivTopicAtlas/1.0 contact:nathanmcknight@users.noreply.github.com"
REQUEST_DELAY = 3.2
MAX_RETRIES = 5

@dataclass
class Paper:
    sampled_year: int
    sampled_day: str
    arxiv_id: str
    created: str
    updated: str
    title: str
    abstract: str
    authors: str
    categories: str
    primary_category: str
    doi: str
    journal_ref: str
    comments: str
    link: str


def ws(s: str) -> str:
    return re.sub(r"\s+", " ", s or "").strip()


def request(params: dict[str, str]) -> ET.Element:
    url = API + "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT, "Accept": "application/xml,text/xml;q=0.9,*/*;q=0.1"})
    last = None
    for attempt in range(MAX_RETRIES):
        try:
            with urllib.request.urlopen(req, timeout=90) as r:
                root = ET.fromstring(r.read())
            time.sleep(REQUEST_DELAY)
            return root
        except urllib.error.HTTPError as e:
            last = e
            if e.code not in (429, 500, 502, 503, 504):
                raise
        except (urllib.error.URLError, TimeoutError) as e:
            last = e
        wait = min(60, 5 * (2 ** attempt))
        print(f"API retry {attempt+1}/{MAX_RETRIES} after {wait}s: {last}", flush=True)
        time.sleep(wait)
    raise RuntimeError(f"OAI request failed: {last}")


def list_sets() -> list[dict[str, str]]:
    out = []
    token = None
    while True:
        params = {"verb": "ListSets"} if not token else {"verb": "ListSets", "resumptionToken": token}
        root = request(params)
        err = root.find(f"{{{OAI}}}error")
        if err is not None:
            raise RuntimeError(f"ListSets: {err.attrib.get('code')} {ws(err.text or '')}")
        for s in root.findall(f".//{{{OAI}}}set"):
            out.append({
                "setSpec": ws(s.findtext(f"{{{OAI}}}setSpec", default="")),
                "setName": ws(s.findtext(f"{{{OAI}}}setName", default="")),
            })
        rt = root.find(f".//{{{OAI}}}resumptionToken")
        token = ws(rt.text or "") if rt is not None else ""
        if not token:
            break
    return out


def parse_record(record: ET.Element, sampled_year: int, sampled_day: str) -> Paper | None:
    header = record.find(f"{{{OAI}}}header")
    if header is not None and header.attrib.get("status") == "deleted":
        return None
    md = record.find(f"{{{OAI}}}metadata")
    if md is None:
        return None
    rec = md.find(f"{{{ARXIV}}}arXiv")
    if rec is None:
        return None
    aid = ws(rec.findtext(f"{{{ARXIV}}}id", default=""))
    if not aid:
        return None
    cats = ws(rec.findtext(f"{{{ARXIV}}}categories", default=""))
    primary = cats.split()[0] if cats else ""
    names = []
    for a in rec.findall(f".//{{{ARXIV}}}author"):
        key = ws(a.findtext(f"{{{ARXIV}}}keyname", default=""))
        fore = ws(a.findtext(f"{{{ARXIV}}}forenames", default=""))
        if key or fore:
            names.append(ws(f"{fore} {key}"))
    return Paper(
        sampled_year=sampled_year,
        sampled_day=sampled_day,
        arxiv_id=aid,
        created=ws(rec.findtext(f"{{{ARXIV}}}created", default="")),
        updated=ws(rec.findtext(f"{{{ARXIV}}}updated", default="")),
        title=ws(rec.findtext(f"{{{ARXIV}}}title", default="")),
        abstract=ws(rec.findtext(f"{{{ARXIV}}}abstract", default="")),
        authors="; ".join(names),
        categories=cats.replace(" ", "; "),
        primary_category=primary,
        doi=ws(rec.findtext(f"{{{ARXIV}}}doi", default="")),
        journal_ref=ws(rec.findtext(f"{{{ARXIV}}}journal-ref", default="")),
        comments=ws(rec.findtext(f"{{{ARXIV}}}comments", default="")),
        link=f"https://arxiv.org/abs/{aid}",
    )


def harvest_day(day: dt.date, set_spec: str = "physics") -> list[Paper]:
    day_s = day.isoformat()
    params = {
        "verb": "ListRecords",
        "metadataPrefix": "arXiv",
        "set": set_spec,
        "from": day_s,
        "until": day_s,
    }
    out: list[Paper] = []
    token = None
    while True:
        p = params if not token else {"verb": "ListRecords", "resumptionToken": token}
        root = request(p)
        err = root.find(f"{{{OAI}}}error")
        if err is not None:
            code = err.attrib.get("code", "")
            if code == "noRecordsMatch":
                return out
            raise RuntimeError(f"{day_s}: {code} {ws(err.text or '')}")
        for r in root.findall(f".//{{{OAI}}}record"):
            paper = parse_record(r, day.year, day_s)
            if paper:
                out.append(paper)
        rt = root.find(f".//{{{OAI}}}resumptionToken")
        token = ws(rt.text or "") if rt is not None else ""
        if not token:
            break
    return out


def eligible_days(year: int, current_date: dt.date) -> list[dt.date]:
    start = dt.date(year, 1, 1)
    # arXiv started in 1991; avoid pre-launch months in the first year.
    if year == 1991:
        start = dt.date(1991, 8, 14)
    end = dt.date(year, 12, 31)
    if year == current_date.year:
        end = min(end, current_date)
    if end < start:
        return []
    return [start + dt.timedelta(days=i) for i in range((end-start).days + 1)]


def write_csv(path: Path, papers: list[Paper]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fields = list(Paper.__dataclass_fields__)
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for p in papers:
            w.writerow(asdict(p))


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--years", nargs="+", type=int, required=True)
    ap.add_argument("--days-per-year", type=int, default=6)
    ap.add_argument("--max-per-year", type=int, default=600)
    ap.add_argument("--seed", type=int, default=20260913)
    ap.add_argument("--out", type=Path, default=Path("atlas_data"))
    ap.add_argument("--current-date", default="2026-09-13")
    ap.add_argument("--set-spec", default="physics")
    args = ap.parse_args()

    current_date = dt.date.fromisoformat(args.current_date)
    args.out.mkdir(parents=True, exist_ok=True)

    sets = list_sets()
    (args.out / "OAI_SET_SNAPSHOT.json").write_text(json.dumps({"retrieved_for_run": args.current_date, "sets": sets}, indent=2) + "\n", encoding="utf-8")
    with (args.out / "OAI_SET_SNAPSHOT.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["setSpec", "setName"]); w.writeheader(); w.writerows(sets)

    all_compact: list[Paper] = []
    metadata = {
        "api": API,
        "metadataPrefix": "arXiv",
        "set_spec": args.set_spec,
        "seed": args.seed,
        "days_per_year": args.days_per_year,
        "max_per_year": args.max_per_year,
        "current_date_cap": args.current_date,
        "years": {},
        "design": "uniform random-day cluster sample; all records harvested on selected days; compact file deterministically subsampled only if pooled day harvest exceeds max-per-year",
    }

    for year in args.years:
        rng = random.Random(args.seed + year)
        days = eligible_days(year, current_date)
        if not days:
            continue
        k = min(args.days_per_year, len(days))
        chosen = sorted(rng.sample(days, k))
        pool_by_id: dict[str, Paper] = {}
        day_counts = {}
        for d in chosen:
            print(f"{year}: harvesting {d}", flush=True)
            records = harvest_day(d, args.set_spec)
            day_counts[d.isoformat()] = len(records)
            for p in records:
                pool_by_id[p.arxiv_id] = p
        pool = list(pool_by_id.values())
        pool.sort(key=lambda p: (p.sampled_day, p.arxiv_id))
        write_csv(args.out / f"{year}_sampled_days_FULL.csv", pool)
        if len(pool) > args.max_per_year:
            compact = [pool[i] for i in sorted(rng.sample(range(len(pool)), args.max_per_year))]
        else:
            compact = pool
        write_csv(args.out / f"{year}_comparison_sample.csv", compact)
        all_compact.extend(compact)
        metadata["years"][str(year)] = {
            "eligible_day_count": len(days),
            "sampled_days": [d.isoformat() for d in chosen],
            "records_by_sampled_day": day_counts,
            "unique_records_full_pool": len(pool),
            "compact_records": len(compact),
        }

    write_csv(args.out / "ALL_YEARS_comparison_sample.csv", all_compact)
    (args.out / "RUN_METADATA.json").write_text(json.dumps(metadata, indent=2) + "\n", encoding="utf-8")
    print(f"DONE: {len(all_compact)} compact records across {len(metadata['years'])} years", flush=True)

if __name__ == "__main__":
    main()
