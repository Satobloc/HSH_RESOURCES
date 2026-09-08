#!/usr/bin/env python3
"""arXiv structural scanner for SAT / H(s)H.

Pulls recent arXiv metadata from selected categories, then scores title/abstract
locally for structural co-occurrence. A high score means "worth reading", not
"supports SAT/H(s)H".

Standard-library only.
"""
from __future__ import annotations

import argparse, csv, html, json, re, sys, time
import urllib.error, urllib.parse, urllib.request
import xml.etree.ElementTree as ET
from dataclasses import asdict, dataclass, field
from datetime import datetime, timedelta, timezone
from pathlib import Path

API = "https://export.arxiv.org/api/query"
DELAY = 3.1  # arXiv legacy API: <= 1 request / 3 seconds, single connection
PAGE_SIZE = 500
MAX_FETCH = 5000

CATEGORIES = [
    "gr-qc","hep-th","hep-ph","hep-lat","quant-ph","math-ph","nucl-th","nucl-ex",
    "astro-ph.CO","astro-ph.HE","cond-mat.stat-mech","cond-mat.str-el","cond-mat.mes-hall",
    "nlin.PS","nlin.CD","math.DG","math.GT","math.SG","math.QA","math.AT",
]

# feature: (sector, weight, alternatives). Each feature scores at most once.
F = {
 "worldline": ("kinematics",2.6,["worldline","worldtube","world line","world tube","spacetime trajectory"]),
 "filament": ("kinematics",1.5,["filament","line defect","stringlike defect","one-dimensional defect"]),
 "framed_curve": ("geometry",2.0,["framed curve","frenet-serret","frenet serret","curve framing"]),
 "curvature": ("geometry",1.8,["extrinsic curvature","worldline curvature","curve curvature","bending energy","rigid particle"]),
 "torsion": ("geometry",2.2,["curve torsion","frenet torsion","geometric torsion","curvature and torsion","torsion action"]),
 "elastic": ("geometry",1.8,["elastic rod","kirchhoff rod","string rigidity","rigid string","bending stiffness"]),
 "strain": ("continuum",1.7,["strain tensor","shear tensor","vorticity tensor","expansion shear vorticity","elastic spacetime"]),
 "foliation": ("projection",2.1,["foliation","cauchy hypersurface","cauchy surface","spacelike hypersurface","adm slicing"]),
 "timeflow": ("projection",1.8,["timelike congruence","unit timelike vector","timelike vector field","preferred foliation","khronon"]),
 "projection": ("projection",1.5,["dimensional reduction","geometric projection","hypersurface intersection","projected observable"]),
 "intersection": ("projection",2.3,["brane intersection","intersecting branes","defect intersection","intersection of defects"]),
 "holonomy": ("topology",2.8,["holonomy","wilson loop","parallel transport","monodromy"]),
 "phase": ("topology",2.0,["geometric phase","berry phase","hannay angle","aharonov-bohm","phase holonomy"]),
 "braid": ("topology",2.7,["linking number","winding number","braid group","braiding","braided","braid statistics"]),
 "knot": ("topology",2.8,["knot theory","hopf link","hopfion","borromean","brunnian","torus knot","knotted soliton"]),
 "defect": ("topology",2.0,["topological defect","topological soliton","domain wall","vortex defect"]),
 "bundle": ("gauge",1.8,["fiber bundle","fibre bundle","principal bundle","gauge connection","spin connection"]),
 "metric": ("emergence",3.1,["emergent metric","induced metric","effective metric","metric emergence","emergent lorentzian"]),
 "emergence": ("emergence",2.6,["emergent gravity","induced gravity","emergent spacetime","pregeometric","pre-geometric"]),
 "chirality": ("particle",1.8,["geometric chirality","chirality","handedness","parity asymmetry","parity violation"]),
 "mass": ("particle",1.2,["geometric mass","effective mass","mass generation","mass from geometry","inertial mass"]),
 "confinement": ("particle",2.3,["color confinement","colour confinement","flux tube","center vortex","centre vortex","topological confinement"]),
 "symmetry": ("symmetry",1.8,["z3 symmetry","z_3 symmetry","triality","center symmetry","discrete gauge symmetry"]),
 "gensym": ("symmetry",2.0,["higher-form symmetry","higher form symmetry","non-invertible symmetry","categorical symmetry"]),
 "anomaly": ("symmetry",2.0,["anomaly inflow","anomaly matching","'t hooft anomaly","defect anomaly"]),
 "quantization": ("quantization",2.3,["geometric quantization","topological quantization","holonomy quantization","bohr-sommerfeld","topological selection rule"]),
 "helix": ("geometry",2.4,["helical worldline","helical trajectory","helical curve","superhelix","superhelical","nested helix","screw symmetry"]),
 "torus": ("geometry",1.8,["hopf fibration","contact geometry","toroidal flow","torus flow","toroidal phase space"]),
 "s3": ("cosmology",1.5,["3-sphere","three-sphere","s^3","hyperspherical cosmology","hypersphere","closed frw"]),
 "spinor": ("particle",1.8,["clifford algebra","dirac spinor","spinor geometry","geometric algebra","gamma matrices"]),
 "wormhole": ("geometry",2.3,["einstein-rosen","einstein rosen","er bridge","wormhole throat","wormhole geometry"]),
 "causal": ("causality",1.4,["causal diamond","light cone","causal structure","null propagation","null congruence"]),
 "entanglement": ("emergence",1.5,["entanglement geometry","entanglement wedge","geometry from entanglement","spacetime from entanglement","bulk reconstruction"]),
 "rg": ("scale",1.0,["renormalization group","renormalisation group","coarse-graining","coarse graining","rg flow","effective field theory"]),
}

# (label, bonus, AND-groups of OR-alternatives)
BUNDLES = [
 ("worldline_geometry",4.0,[("worldline","filament"),("curvature","torsion","elastic"),("foliation","projection","timeflow")]),
 ("holonomy_quantization",4.0,[("holonomy",),("phase","quantization")]),
 ("braided_particle_geometry",5.0,[("braid","knot"),("chirality","confinement","mass")]),
 ("emergent_metric_from_structure",5.0,[("metric",),("strain","timeflow","bundle")]),
 ("defect_gauge_symmetry",4.5,[("defect",),("bundle","holonomy"),("symmetry","gensym","anomaly")]),
 ("hyperhelix_projection",5.5,[("helix",),("worldline","framed_curve"),("torsion","curvature"),("foliation","projection")]),
 ("particle_as_intersection",4.5,[("intersection",),("foliation","projection"),("worldline","filament")]),
 ("wormhole_filament_geometry",4.0,[("wormhole",),("worldline","filament","causal")]),
 ("topology_plus_emergence",4.0,[("holonomy","braid","knot"),("metric","emergence","entanglement")]),
]

ATOM="{http://www.w3.org/2005/Atom}"; ARXIV="{http://arxiv.org/schemas/atom}"; OS="{http://a9.com/-/spec/opensearch/1.1/}"

@dataclass
class Paper:
    arxiv_id:str; title:str; authors:list[str]; abstract:str; published:str; updated:str
    primary_category:str; categories:list[str]; abs_url:str; pdf_url:str
    doi:str=""; journal_ref:str=""; score:float=0; tier:str="low"
    sectors:list[str]=field(default_factory=list); features:list[str]=field(default_factory=list)
    terms:list[str]=field(default_factory=list); bundles:list[str]=field(default_factory=list)
    new_or_updated:bool=True

def norm(s:str)->str:
    return re.sub(r"\s+"," ",html.unescape(s or "").lower().replace("–","-").replace("—","-")).strip()

def has(term:str,text:str)->bool:
    t=norm(term)
    return (t in text) if (" " in t or "-" in t or "_" in t or "^" in t) else bool(re.search(rf"(?<![a-z0-9]){re.escape(t)}(?![a-z0-9])",text))

def score(p:Paper)->Paper:
    ti,ab=norm(p.title),norm(p.abstract); found={}; sectors=set(); total=0.0
    for name,(sector,w,terms) in F.items():
        hit=next((x for x in terms if has(x,ti)),None); where="title"
        if hit is None: hit=next((x for x in terms if has(x,ab)),None); where="abstract"
        if hit is None: continue
        total += w*(1.65 if where=="title" else 1.0) + (0.35 if len(norm(hit).split())>1 else 0)
        found[name]=(hit,where); sectors.add(sector)
    for label,bonus,groups in BUNDLES:
        if all(any(x in found for x in group) for group in groups): total+=bonus; p.bundles.append(label)
    d=len(sectors); total += 6 if d>=5 else 4 if d==4 else 2.5 if d==3 else 1 if d==2 else 0
    if set(found)<= {"rg","mass"}: total*=0.35
    p.score=round(total,2); p.sectors=sorted(sectors); p.features=sorted(found)
    p.terms=[f"{k}:{v[0]} ({v[1]})" for k,v in sorted(found.items())]
    p.tier="very-high" if total>=24 else "high" if total>=16 else "medium" if total>=10 else "watch" if total>=7 else "low"
    return p

def txt(e,tag):
    n=e.find(tag); return re.sub(r"\s+"," ",n.text).strip() if n is not None and n.text else ""

def parse_feed(data:bytes):
    root=ET.fromstring(data); total=int(txt(root,OS+"totalResults") or 0); out=[]
    for e in root.findall(ATOM+"entry"):
        eid=txt(e,ATOM+"id"); aid=eid.rstrip("/").split("/")[-1]
        authors=[txt(a,ATOM+"name") for a in e.findall(ATOM+"author")]
        cats=[c.attrib.get("term","") for c in e.findall(ATOM+"category") if c.attrib.get("term")]
        pn=e.find(ARXIV+"primary_category"); primary=pn.attrib.get("term","") if pn is not None else ""
        abs_url=eid; pdf=""
        for link in e.findall(ATOM+"link"):
            href=link.attrib.get("href","")
            if link.attrib.get("rel")=="alternate" and href: abs_url=href
            if link.attrib.get("title")=="pdf" or link.attrib.get("type")=="application/pdf": pdf=href
        out.append(Paper(aid,txt(e,ATOM+"title"),authors,txt(e,ATOM+"summary"),txt(e,ATOM+"published"),txt(e,ATOM+"updated"),primary,cats,abs_url,pdf,txt(e,ARXIV+"doi"),txt(e,ARXIV+"journal_ref")))
    return total,out

def build_query(cats:list[str],since:datetime,until:datetime)->str:
    c=" OR ".join(f"cat:{x}" for x in cats)
    f=lambda d:d.astimezone(timezone.utc).strftime("%Y%m%d%H%M")
    return f"({c}) AND submittedDate:[{f(since)} TO {f(until)}]"

def request(url:str,last:[float])->bytes:
    elapsed=time.monotonic()-last[0]
    if last[0] and elapsed<DELAY: time.sleep(DELAY-elapsed)
    last[0]=time.monotonic()
    req=urllib.request.Request(url,headers={"User-Agent":"HSH-arXiv-Structural-Scanner/0.2","Accept":"application/atom+xml"})
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req,timeout=60) as r:return r.read()
        except (urllib.error.HTTPError,urllib.error.URLError,TimeoutError) as ex:
            if isinstance(ex,urllib.error.HTTPError) and ex.code not in {429,500,502,503,504}:raise
            if attempt==3:raise
            time.sleep(max(DELAY,2**attempt))
    raise RuntimeError("unreachable")

def fetch(query:str,page_size:int,max_fetch:int):
    papers=[]; start=0; total=0; last=[0.0]
    while start<max_fetch:
        n=min(page_size,max_fetch-start)
        q=urllib.parse.urlencode({"search_query":query,"start":start,"max_results":n,"sortBy":"submittedDate","sortOrder":"descending"})
        total,page=parse_feed(request(API+"?"+q,last))
        if not page:break
        papers.extend(page); start+=len(page); print(f"Fetched {len(papers)}/{min(total,max_fetch)}",file=sys.stderr)
        if start>=total:break
    return total,papers

def load_state(path:Path)->dict[str,str]:
    if not path.exists():return {}
    try:d=json.loads(path.read_text(encoding="utf-8")); return {str(k):str(v) for k,v in d.get("papers",{}).items()}
    except Exception:return {}

def save_state(path:Path,state:dict[str,str],papers:list[Paper]):
    for p in papers:state[p.arxiv_id]=p.updated
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps({"last_run_utc":datetime.now(timezone.utc).isoformat(),"papers":state},indent=2,sort_keys=True),encoding="utf-8")

def outputs(outdir:Path,papers:list[Paper],meta:dict):
    outdir.mkdir(parents=True,exist_ok=True); stamp=datetime.now(timezone.utc).strftime("%Y-%m-%dT%H%M%SZ"); stem=outdir/f"{stamp}_SAT_HsH_arxiv_scan"
    jp=stem.with_suffix(".json"); cp=stem.with_suffix(".csv"); mp=stem.with_suffix(".md")
    jp.write_text(json.dumps({"scan":meta,"results":[asdict(p) for p in papers]},indent=2,ensure_ascii=False),encoding="utf-8")
    fields=["score","tier","new_or_updated","arxiv_id","title","authors","published","updated","primary_category","categories","sectors","features","bundles","terms","abstract","abs_url","pdf_url","doi","journal_ref"]
    with cp.open("w",newline="",encoding="utf-8") as f:
        w=csv.DictWriter(f,fieldnames=fields);w.writeheader()
        for p in papers:w.writerow({"score":p.score,"tier":p.tier,"new_or_updated":p.new_or_updated,"arxiv_id":p.arxiv_id,"title":p.title,"authors":"; ".join(p.authors),"published":p.published,"updated":p.updated,"primary_category":p.primary_category,"categories":"; ".join(p.categories),"sectors":"; ".join(p.sectors),"features":"; ".join(p.features),"bundles":"; ".join(p.bundles),"terms":"; ".join(p.terms),"abstract":p.abstract,"abs_url":p.abs_url,"pdf_url":p.pdf_url,"doi":p.doi,"journal_ref":p.journal_ref})
    md=["# SAT / H(s)H arXiv Structural Scan","","> Literature-navigation heuristic only; similarity is not confirmation.","",f"Fetched {meta['fetched']} of {meta['available']} records; reported {len(papers)} at score >= {meta['min_score']}.",""]
    for i,p in enumerate(papers,1):
        md += [f"## {i}. [{p.title}]({p.abs_url})","",f"**Score:** {p.score} ({p.tier}) · **Primary:** `{p.primary_category}` · **{'NEW/UPDATED' if p.new_or_updated else 'seen'}**","",f"**Sectors:** {', '.join(p.sectors)}","",f"**Bundles:** {', '.join(p.bundles) or '—'}","",f"**Features:** {', '.join(p.features)}","",p.abstract,""]
    mp.write_text("\n".join(md),encoding="utf-8");return cp,jp,mp

def main():
    ap=argparse.ArgumentParser(description="Scan recent arXiv metadata for SAT/H(s)H structural cousins.")
    ap.add_argument("--days",type=int,default=7);ap.add_argument("--since");ap.add_argument("--until")
    ap.add_argument("--categories",default=",".join(CATEGORIES));ap.add_argument("--min-score",type=float,default=7.0)
    ap.add_argument("--page-size",type=int,default=PAGE_SIZE);ap.add_argument("--max-fetch",type=int,default=MAX_FETCH)
    ap.add_argument("--output-dir",type=Path,default=Path("DATA/arxiv_scans"));ap.add_argument("--state-file",type=Path,default=Path("DATA/arxiv_scans/.arxiv_sat_state.json"))
    ap.add_argument("--include-seen",action="store_true");ap.add_argument("--no-state-write",action="store_true");ap.add_argument("--dry-run",action="store_true")
    a=ap.parse_args(); now=datetime.now(timezone.utc)
    until=min(datetime.strptime(a.until,"%Y-%m-%d").replace(tzinfo=timezone.utc)+timedelta(days=1)-timedelta(minutes=1),now) if a.until else now
    since=datetime.strptime(a.since,"%Y-%m-%d").replace(tzinfo=timezone.utc) if a.since else until-timedelta(days=a.days)
    cats=[x.strip() for x in a.categories.split(",") if x.strip()]; query=build_query(cats,since,until)
    if a.dry_run:print(query);return 0
    if not 1<=a.page_size<=2000:raise SystemExit("--page-size must be 1..2000")
    available,papers=fetch(query,a.page_size,a.max_fetch)
    if available>a.max_fetch:print(f"WARNING: {available} available; truncated at {a.max_fetch}",file=sys.stderr)
    state=load_state(a.state_file)
    for p in papers:p.new_or_updated=state.get(p.arxiv_id)!=p.updated;score(p)
    report=[p for p in papers if p.score>=a.min_score and (a.include_seen or p.new_or_updated)]
    report.sort(key=lambda p:(p.score,p.updated),reverse=True)
    meta={"scan_utc":datetime.now(timezone.utc).isoformat(),"since":since.isoformat(),"until":until.isoformat(),"categories":cats,"query":query,"available":available,"fetched":len(papers),"min_score":a.min_score}
    cp,jp,mp=outputs(a.output_dir,report,meta)
    if not a.no_state_write:save_state(a.state_file,state,papers)
    print(f"Fetched {len(papers)} of {available}; reported {len(report)}")
    print(f"CSV: {cp}\nJSON: {jp}\nMarkdown: {mp}")
    for p in report[:15]:print(f"{p.score:6.2f}  {p.tier:9s}  {p.arxiv_id:16s}  {p.title}")
    return 0

if __name__=="__main__":raise SystemExit(main())
