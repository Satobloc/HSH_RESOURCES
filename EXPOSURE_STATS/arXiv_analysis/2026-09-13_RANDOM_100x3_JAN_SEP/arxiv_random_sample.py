#!/usr/bin/env python3
"""Reproducible random pull of 100 arXiv physics abstracts/year, Jan-Sep.

Uses arXiv's official OAI-PMH metadata API. Modern arXiv IDs encode submission
month as YYMM.NNNNN. For each year we uniformly shuffle the rectangular slot
space months 01..09 x sequence 00001..40000, query candidate IDs with
GetRecord(metadataPrefix=arXiv), and reject nonexistent/non-physics records.
Conditional on acceptance, every eligible extant ID in the frame has the same
draw probability. A fixed seed makes the pull reproducible.
"""
from __future__ import annotations
import argparse, csv, json, random, re, time, urllib.error, urllib.parse, urllib.request
import xml.etree.ElementTree as ET
from dataclasses import asdict, dataclass
from pathlib import Path

API="https://oaipmh.arxiv.org/oai"
OAI_NS="http://www.openarchives.org/OAI/2.0/"
ARXIV_NS="http://arxiv.org/OAI/arXiv/"
PHYS_PREFIXES=("astro-ph","cond-mat","gr-qc","hep-","nucl-","physics.","quant-ph","math-ph","nlin.")
MAX_SEQUENCE=40000
REQUEST_DELAY=0.40
BATCH=50
MAX_ATTEMPTS_PER_YEAR=2200

@dataclass
class Paper:
    year:int; arxiv_id:str; title:str; abstract:str; created:str; updated:str
    authors:str; categories:str; link:str

def ws(s): return re.sub(r"\s+"," ",s or "").strip()
def is_physics(cats): return any(c.startswith(PHYS_PREFIXES) for c in cats)

def fetch_id(arxiv_id,timeout=45):
    params={"verb":"GetRecord","identifier":f"oai:arXiv.org:{arxiv_id}","metadataPrefix":"arXiv"}
    url=API+"?"+urllib.parse.urlencode(params)
    req=urllib.request.Request(url,headers={"User-Agent":"HsH-ArxivRandomSampler/2.1 contact:nathanmcknight@users.noreply.github.com","Accept":"application/xml,text/xml;q=0.9,*/*;q=0.1"})
    for attempt in range(5):
        try:
            with urllib.request.urlopen(req,timeout=timeout) as r: root=ET.fromstring(r.read())
            err=root.find(f"{{{OAI_NS}}}error")
            if err is not None:
                if err.attrib.get("code") in {"idDoesNotExist","noRecordsMatch"}: return None
                raise RuntimeError(f"OAI error {err.attrib.get('code')}: {ws(err.text or '')}")
            md=root.find(f".//{{{OAI_NS}}}metadata")
            if md is None: return None
            rec=md.find(f"{{{ARXIV_NS}}}arXiv")
            if rec is None: return None
            rid=ws(rec.findtext(f"{{{ARXIV_NS}}}id",default=""))
            if not rid: return None
            cats=ws(rec.findtext(f"{{{ARXIV_NS}}}categories",default="")).split()
            if not is_physics(cats): return None
            names=[]
            for a in rec.findall(f".//{{{ARXIV_NS}}}author"):
                key=ws(a.findtext(f"{{{ARXIV_NS}}}keyname",default="")); fore=ws(a.findtext(f"{{{ARXIV_NS}}}forenames",default="")); name=ws(f"{fore} {key}") if fore else key
                if name: names.append(name)
            return Paper(2000+int(rid[:2]),rid,ws(rec.findtext(f"{{{ARXIV_NS}}}title",default="")),ws(rec.findtext(f"{{{ARXIV_NS}}}abstract",default="")),ws(rec.findtext(f"{{{ARXIV_NS}}}created",default="")),ws(rec.findtext(f"{{{ARXIV_NS}}}updated",default="")),"; ".join(names),"; ".join(cats),f"https://arxiv.org/abs/{rid}")
        except urllib.error.HTTPError as e:
            if e.code in (406,429,500,502,503,504) and attempt<4:
                wait=min(30,3*(2**attempt)); print(f"{arxiv_id}: HTTP {e.code}; retry in {wait}s",flush=True); time.sleep(wait); continue
            raise
        except (urllib.error.URLError,TimeoutError) as e:
            if attempt<4:
                wait=min(30,3*(2**attempt)); print(f"{arxiv_id}: {e}; retry in {wait}s",flush=True); time.sleep(wait); continue
            raise
    return None

def candidate_slots(year,rng):
    yy=year%100; slots=[(m,s) for m in range(1,10) for s in range(1,MAX_SEQUENCE+1)]; rng.shuffle(slots)
    for m,s in slots: yield f"{yy:02d}{m:02d}.{s:05d}"

def sample_year(year,n,rng):
    accepted={}; attempted=0; slots=candidate_slots(year,rng)
    while len(accepted)<n and attempted<MAX_ATTEMPTS_PER_YEAR:
        todo=min(BATCH,MAX_ATTEMPTS_PER_YEAR-attempted)
        for _ in range(todo):
            aid=next(slots); attempted+=1
            try: p=fetch_id(aid)
            except Exception as e:
                print(f"WARN {aid}: {type(e).__name__}: {e}",flush=True); p=None
            if p is not None and p.year==year: accepted[p.arxiv_id]=p
            time.sleep(REQUEST_DELAY)
            if len(accepted)>=n: break
        print(f"{year}: attempted={attempted} eligible_physics={len(accepted)}",flush=True)
    if len(accepted)<n: raise RuntimeError(f"{year}: only {len(accepted)} eligible records after {attempted} probes")
    ids=rng.sample(sorted(accepted),n); papers=[accepted[x] for x in ids]; rng.shuffle(papers)
    meta={"year":year,"period":f"{year}-01 through {year}-09 (arXiv ID month)","sample_size":n,"attempted_id_slots":attempted,"eligible_records_found":len(accepted),"acceptance_rate":len(accepted)/attempted,"max_sequence_slot":MAX_SEQUENCE,"months":list(range(1,10)),"physics_category_prefixes":list(PHYS_PREFIXES),"api":API,"metadata_prefix":"arXiv","request_delay_seconds":REQUEST_DELAY,"method":"Uniform random YYMM.NNNNN slot probing through official arXiv OAI-PMH GetRecord; reject nonexistent/non-physics records; fixed seed.","caveat":"Uniform over eligible extant modern arXiv IDs in the Jan-Sep rectangular slot frame, assuming 40000 exceeds each month's highest sequence. Cross-listed records qualify if any category is physics-family."}
    return papers,meta

def write_csv(path,papers):
    path.parent.mkdir(parents=True,exist_ok=True); fields=list(Paper.__dataclass_fields__)
    with path.open("w",newline="",encoding="utf-8") as f:
        w=csv.DictWriter(f,fieldnames=fields); w.writeheader()
        for p in papers: w.writerow(asdict(p))

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--years",nargs="+",type=int,default=[2024,2025,2026]); ap.add_argument("--n",type=int,default=100); ap.add_argument("--seed",type=int,default=20260912); ap.add_argument("--out",type=Path,default=Path("results")); args=ap.parse_args()
    args.out.mkdir(parents=True,exist_ok=True); allp=[]; per={}
    for year in args.years:
        papers,meta=sample_year(year,args.n,random.Random(args.seed+year)); allp+=papers; per[str(year)]=meta
        write_csv(args.out/f"arxiv_random_{args.n}_{year}_jan_sep.csv",papers)
        (args.out/f"arxiv_random_{args.n}_{year}_jan_sep.json").write_text(json.dumps({"metadata":meta,"papers":[asdict(p) for p in papers]},indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    combined={"seed":args.seed,"years":args.years,"n_per_year":args.n,"total_records":len(allp),"source":"official arXiv OAI-PMH API","source_url":API,"per_year":per}
    write_csv(args.out/"arxiv_random_100_2024_2025_2026_combined.csv",allp)
    (args.out/"arxiv_random_100_2024_2025_2026_combined.json").write_text(json.dumps({"metadata":combined,"papers":[asdict(p) for p in allp]},indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    (args.out/"README.md").write_text(f"# arXiv random physics abstract pull\n\n- 100 abstracts/year; {len(allp)} total\n- Jan-Sep 2024, 2025, 2026\n- fixed seed `{args.seed}`\n- official arXiv OAI-PMH API\n- uniform shuffled modern arXiv ID-slot sampling; nonexistent/non-physics IDs rejected\n- category-based physics membership includes cross-lists\n\nThis is an auditable random corpus for structural/philosophical comparison. Full method and acceptance statistics are preserved in JSON metadata.\n",encoding="utf-8")
    print(f"DONE: wrote {len(allp)} records",flush=True)
if __name__=="__main__": main()
