#!/usr/bin/env python3
"""Insert/update a neutral podcast-title chronology in CROSS_MASTER_CHRONOLOGY.md.

Source of publish dates/titles: Spotify episode-ranking export in PODCAST_EPs.
No interpretation is performed.
"""
from __future__ import annotations

import csv
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CSV_PATH = ROOT / "EXPOSURE_STATS/PODCAST_EPs/DebatingA.I.OnScience_EpisodeRankings_all-time.csv"
MASTER = ROOT / "EXPOSURE_STATS/CROSS_MASTER_CHRONOLOGY.md"
START = "<!-- PODCAST_TITLES_START -->"
END = "<!-- PODCAST_TITLES_END -->"


def parse_date(s: str):
    s = (s or "").strip()
    if not s:
        return None
    try:
        return datetime.strptime(s, "%m/%d/%Y").date()
    except ValueError:
        return None


def esc(s: str) -> str:
    return (s or "").replace("|", "\\|").replace("\n", " ").strip()


def main() -> int:
    rows = []
    undated = []
    with CSV_PATH.open("r", encoding="utf-8-sig", newline="") as f:
        for row in csv.DictReader(f):
            title = (row.get("Episode title") or "").strip()
            if not title:
                continue
            date = parse_date(row.get("Publish date") or "")
            record = {
                "title": title,
                "date_raw": (row.get("Publish date") or "").strip(),
                "date": date,
                "streams": (row.get("Streams & downloads") or "").strip(),
                "rank": (row.get("Rank") or "").strip(),
                "uri": (row.get("Episode URI") or "").strip(),
            }
            (rows if date else undated).append(record)

    rows.sort(key=lambda r: (r["date"], r["title"].casefold()))
    undated.sort(key=lambda r: r["title"].casefold())

    lines = [
        START,
        "## Podcast episode/transcript title chronology",
        "",
        "Neutral title/date index drawn directly from `EXPOSURE_STATS/PODCAST_EPs/DebatingA.I.OnScience_EpisodeRankings_all-time.csv`. Titles, publish dates, ranks, stream/download counts, and Spotify episode URIs are preserved as supplied by the source export. No dates are corrected here.",
        "",
        "| Publish date | Episode / transcript title | Streams & downloads | Rank | Episode URI |",
        "|---|---|---:|---:|---|",
    ]
    for r in rows:
        lines.append(
            f"| {r['date'].isoformat()} | {esc(r['title'])} | {esc(r['streams'])} | {esc(r['rank'])} | `{esc(r['uri'])}` |"
        )

    if undated:
        lines += ["", "### Titles without a parseable publish date", "", "| Source date | Episode / transcript title | Streams & downloads | Rank | Episode URI |", "|---|---|---:|---:|---|"]
        for r in undated:
            lines.append(
                f"| {esc(r['date_raw'])} | {esc(r['title'])} | {esc(r['streams'])} | {esc(r['rank'])} | `{esc(r['uri'])}` |"
            )

    lines += ["", f"Catalog rows: **{len(rows) + len(undated)}**; dated: **{len(rows)}**; undated/unparseable: **{len(undated)}**.", END]
    block = "\n".join(lines)

    text = MASTER.read_text(encoding="utf-8")
    if START in text and END in text:
        before, rest = text.split(START, 1)
        _, after = rest.split(END, 1)
        text = before.rstrip() + "\n\n" + block + after
    else:
        insert_at = text.find("\n## Google Trends/search snapshots")
        if insert_at == -1:
            text = text.rstrip() + "\n\n" + block + "\n"
        else:
            text = text[:insert_at].rstrip() + "\n\n" + block + "\n" + text[insert_at:]
    MASTER.write_text(text, encoding="utf-8")
    print(f"podcast_catalog_rows={len(rows)+len(undated)} dated={len(rows)} undated={len(undated)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
