#!/usr/bin/env python3
"""Build a neutral date/title/keyword index over podcast transcript text files.

No semantic scoring or interpretation is performed. Keyword matching is literal,
case-insensitive, and phrase-aware. Source text remains canonical.
"""
from __future__ import annotations

import csv
import re
from collections import Counter
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
POD = ROOT / "EXPOSURE_STATS/PODCAST_EPs"
KEYWORDS = POD / "CROSS_PODCAST_KEYWORDS.txt"
RANKINGS = POD / "DebatingA.I.OnScience_EpisodeRankings_all-time.csv"
OUT_CATALOG = POD / "CROSS_TRANSCRIPT_CATALOG.csv"
OUT_HITS = POD / "CROSS_TRANSCRIPT_KEYWORD_HITS.csv"
OUT_MATRIX = POD / "CROSS_TRANSCRIPT_KEYWORD_MATRIX.csv"
OUT_MD = POD / "CROSS_TRANSCRIPT_KEYWORD_INDEX.md"

AGGREGATES = {
    "DAI_Transcripts_TEXT.txt",
    "COMP_FieldNotes_FULL_test.txt",
    "CROSS_PODCAST_KEYWORDS.txt",
}

DATE_PATTERNS = [
    re.compile(r"(?im)^Published:\s*([A-Z][a-z]+\s+\d{1,2},\s+\d{4})(?:\s+at\s+[^\n]+)?$"),
    re.compile(r"(?im)^Published Date:\s*([A-Z][a-z]+\s+\d{1,2},\s+\d{4})$"),
    re.compile(r"(?im)^Release Date:\s*([A-Z][a-z]+\s+\d{1,2},\s+\d{4})$"),
]


def load_keywords() -> list[str]:
    out=[]
    for line in KEYWORDS.read_text(encoding="utf-8").splitlines():
        s=line.strip()
        if s and not s.startswith("#"):
            out.append(s)
    return out


def load_rankings() -> dict[str, dict[str,str]]:
    exact={}
    with RANKINGS.open("r",encoding="utf-8-sig",newline="") as f:
        for row in csv.DictReader(f):
            title=(row.get("Episode title") or "").strip()
            if title:
                exact[normalize(title)]=row
    return exact


def normalize(s: str) -> str:
    s=s.casefold().replace("…","...").replace("’","'").replace("“",'"').replace("”",'"')
    s=re.sub(r"[^a-z0-9]+"," ",s)
    return re.sub(r"\s+"," ",s).strip()


def title_from_filename(path: Path) -> str:
    stem=path.stem
    stem=re.sub(r"^(FULL_|TRANSCRIPT_|PODCAST[_ -]*)+","",stem,flags=re.I)
    stem=stem.replace("_"," ")
    return re.sub(r"\s+"," ",stem).strip()


def source_date(text: str):
    for pat in DATE_PATTERNS:
        m=pat.search(text[:5000])
        if m:
            try:
                return datetime.strptime(m.group(1),"%B %d, %Y").date(), "transcript_header"
            except ValueError:
                pass
    return None, ""


def ranking_match(candidate: str, rankings: dict[str,dict[str,str]]):
    n=normalize(candidate)
    if n in rankings:
        return rankings[n]
    # conservative containment fallback; only accept unique long-title match
    matches=[]
    for k,row in rankings.items():
        if len(n) >= 12 and (n in k or k in n):
            matches.append(row)
    return matches[0] if len(matches)==1 else None


def parse_rank_date(row):
    if not row: return None
    s=(row.get("Publish date") or "").strip()
    try: return datetime.strptime(s,"%m/%d/%Y").date()
    except ValueError: return None


def count_keyword(text: str, kw: str) -> int:
    # literal phrase matching with alphanumeric boundaries where possible
    escaped=re.escape(kw)
    left=r"(?<!\w)" if kw and kw[0].isalnum() else ""
    right=r"(?!\w)" if kw and kw[-1].isalnum() else ""
    return len(re.findall(left+escaped+right,text,flags=re.I))


def excerpt(text: str, kw: str, width=180) -> str:
    m=re.search(re.escape(kw),text,flags=re.I)
    if not m: return ""
    a=max(0,m.start()-width); b=min(len(text),m.end()+width)
    s=re.sub(r"\s+"," ",text[a:b]).strip()
    return s[:500]


def main():
    keywords=load_keywords()
    rankings=load_rankings()
    files=[]
    for p in POD.glob("*.txt"):
        if p.name in AGGREGATES or p.name.startswith("CROSS_"):
            continue
        if p.stat().st_size < 1000:
            continue
        files.append(p)
    files.sort(key=lambda p:p.name.casefold())

    catalog=[]; hits=[]; matrices=[]
    for p in files:
        text=p.read_text(encoding="utf-8",errors="replace")
        candidate=title_from_filename(p)
        rank=ranking_match(candidate,rankings)
        title=(rank.get("Episode title") if rank else None) or candidate
        dt, date_source=source_date(text)
        if not dt:
            dt=parse_rank_date(rank)
            if dt: date_source="spotify_catalog"
        counts={kw:count_keyword(text,kw) for kw in keywords}
        hit_total=sum(counts.values())
        catalog.append({
            "date":dt.isoformat() if dt else "",
            "date_source":date_source,
            "title":title,
            "source_path":p.relative_to(ROOT).as_posix(),
            "characters":len(text),
            "keyword_hit_total":hit_total,
            "matched_spotify_uri":(rank.get("Episode URI") if rank else "") or "",
        })
        mrow={"date":dt.isoformat() if dt else "","title":title,"source_path":p.relative_to(ROOT).as_posix()}
        mrow.update(counts); matrices.append(mrow)
        for kw,n in counts.items():
            if n:
                hits.append({
                    "date":dt.isoformat() if dt else "",
                    "title":title,
                    "keyword":kw,
                    "count":n,
                    "first_excerpt":excerpt(text,kw),
                    "source_path":p.relative_to(ROOT).as_posix(),
                })

    catalog.sort(key=lambda r:(r["date"] or "9999",r["title"].casefold()))
    hits.sort(key=lambda r:(r["date"] or "9999",r["title"].casefold(),r["keyword"].casefold()))
    matrices.sort(key=lambda r:(r["date"] or "9999",r["title"].casefold()))

    def write_csv(path,rows,fields):
        with path.open("w",encoding="utf-8",newline="") as f:
            w=csv.DictWriter(f,fieldnames=fields); w.writeheader(); w.writerows(rows)

    write_csv(OUT_CATALOG,catalog,["date","date_source","title","source_path","characters","keyword_hit_total","matched_spotify_uri"])
    write_csv(OUT_HITS,hits,["date","title","keyword","count","first_excerpt","source_path"])
    write_csv(OUT_MATRIX,matrices,["date","title","source_path",*keywords])

    per_kw=Counter()
    for h in hits: per_kw[h["keyword"]]+=h["count"]
    lines=[
        "# Cross podcast transcript keyword index","",
        "Mechanical, literal keyword index only. Counts are case-insensitive literal matches; no semantic or causal interpretation is applied.","",
        f"Transcript-like text files indexed: **{len(catalog)}**  ",
        f"Keyword phrases: **{len(keywords)}**  ",
        f"Episode-keyword hit rows: **{len(hits)}**","",
        "## Keyword totals","",
        "| Keyword | Literal hits |","|---|---:|",
    ]
    for kw,n in sorted(per_kw.items(),key=lambda x:(-x[1],x[0].casefold())):
        lines.append(f"| {kw.replace('|','\\|')} | {n} |")
    lines += ["","## Files","",
              "- `CROSS_TRANSCRIPT_CATALOG.csv` — one row per indexed transcript file.",
              "- `CROSS_TRANSCRIPT_KEYWORD_HITS.csv` — one row per episode/keyword combination with at least one hit, plus first excerpt.",
              "- `CROSS_TRANSCRIPT_KEYWORD_MATRIX.csv` — one row per episode, one column per keyword.",
              "- `CROSS_PODCAST_KEYWORDS.txt` — editable literal keyword list."]
    OUT_MD.write_text("\n".join(lines)+"\n",encoding="utf-8")
    print(f"transcripts={len(catalog)} keywords={len(keywords)} hit_rows={len(hits)}")

if __name__=="__main__":
    main()
