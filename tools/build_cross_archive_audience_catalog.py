#!/usr/bin/env python3
"""Discover audience/exposure metrics across the three SAT/H(s)H GitHub repositories.

Default is catalogue-only. Sources remain in their original repositories.
No personal files, secrets, PRIOR_ART, or unrelated CSVs are included in
consolidated records; ambiguous CSVs appear as review candidates only.
Uses GitHub git-tree API with a per-file size cap, caching by git blob SHA
and no mandatory third-party packages.
"""
from __future__ import annotations
import argparse, csv, hashlib, io, json, os, re, sys, urllib.request, urllib.error
from pathlib import Path

REPOS = ["Satobloc/HSH_RESOURCES", "Satobloc/HsH", "Satobloc/SAT_THEORY_ARCHIVE_2023-25"]
BASE = Path(__file__).resolve().parents[1]
OUT = BASE / "EXPOSURE_STATS" / "AUDIENCE_METRICS"
EXCLUDE = ("prior_art/", "secrets/", ".git/", "private/", "credentials/", "node_modules/", "derived/", "vendor/")
POSITIVE = ("audience", "podcast", "spotify", "listenership", "listener", "geolocation", "geo_location", "retention", "episodecompletion", "episode_completion", "consumption", "analytics", "exposure_stats", "agebygender", "age_by_gender")
HEADERS = ("listener", "listenership", "audience", "retention", "episode title", "consumption time", "gender", "geolocation", "geo", "streams", "plays", "completion rate")
MAX_BYTES = 2_000_000

def api(url):
    h = {"Accept": "application/vnd.github+json", "User-Agent": "hsh-audience-catalog-v1"}
    if os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN"):
        h["Authorization"] = "Bearer " + (os.environ.get("GH_TOKEN") or os.environ["GITHUB_TOKEN"])
    with urllib.request.urlopen(urllib.request.Request(url, headers=h), timeout=45) as response:
        return json.load(response)

def blob(repo, sha):
    doc = api(f"https://api.github.com/repos/{repo}/git/blobs/{sha}")
    import base64
    if doc.get("encoding") != "base64":
        raise ValueError("Unexpected GitHub blob encoding")
    return base64.b64decode(doc["content"])

def category(path):
    p = path.casefold()
    if p.startswith(EXCLUDE) or any("/"+e in p for e in EXCLUDE):
        return "excluded"
    if not p.endswith(".csv"):
        return "excluded"
    if any(term in p for term in POSITIVE):
        return "candidate"
    return "review"

def parse_csv(data):
    s = data.decode("utf-8-sig")
    table = list(csv.reader(io.StringIO(s, newline="")))
    if not table:
        return [], []
    width = len(table[0])
    if any(len(row) != width for row in table[1:]):
        raise ValueError("ragged CSV")
    return table[0], table[1:]

def scan():
    records, errors = [], []
    for repo in REPOS:
        try:
            tree = api(f"https://api.github.com/repos/{repo}/git/trees/main?recursive=1")
            if tree.get("truncated"):
                raise RuntimeError("GitHub tree truncated; abort rather than assert complete coverage")
            items = [x for x in tree.get("tree", []) if x.get("type") == "blob" and x["path"].casefold().endswith(".csv")]
            for x in items:
                path = x["path"]
                state = category(path)
                if state == "excluded": continue
                entry = {"repository": repo, "source_path": path, "git_sha": x["sha"], "bytes": x.get("size"), "classification": state}
                if state == "review":
                    records.append(entry)
                    continue
                if x.get("size", MAX_BYTES+1) > MAX_BYTES:
                    entry["classification"] = "oversize_review"
                    records.append(entry)
                    continue
                try:
                    raw = blob(repo, x["sha"])
                    columns, rows = parse_csv(raw)
                    entry["sha256"] = hashlib.sha256(raw).hexdigest()
                    entry["columns"] = columns
                    entry["row_count"] = len(rows)
                    relevant = any(any(key in cell.casefold() for key in HEADERS) for cell in columns)
                    entry["classification"] = "audience_metric" if relevant else "review"
                    if relevant:
                        entry["rows"] = rows
                        entry["raw_csv"] = raw.decode("utf-8-sig")
                except Exception as exc:
                    entry["classification"] = "error"
                    entry["error"] = str(exc)
                    errors.append({"repository": repo, "path": path, "error": str(exc)})
                records.append(entry)
        except Exception as exc:
            errors.append({"repository": repo, "error": str(exc)})
    return {"schema_version": 1, "repositories": REPOS, "complete": not errors, "record_count": len(records), "included_count": sum(x["classification"]=="audience_metric" for x in records), "records": records, "errors": errors}

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--output", default=str(OUT / "cross_archive_audience_catalog.json"))
    args = p.parse_args()
    result = scan()
    target = Path(args.output)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({"complete": result["complete"], "candidate_records": result["record_count"], "included": result["included_count"], "errors": len(result["errors"])}))
    if not result["complete"]: sys.exit(1)

if __name__ == "__main__": main()
