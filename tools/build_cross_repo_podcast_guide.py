#!/usr/bin/env python3
"""Build a provenance-preserving cross-repository podcast guide.

Mechanical discovery/extraction only. Raw files remain canonical. PRIOR_ART is
pruned before traversal. No theory claims are promoted by this tool.
"""
from __future__ import annotations
import argparse, csv, hashlib, json, re, subprocess
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

VERSION="cross-podcast-guide/0.2.2"
REPOS={"resources":"Satobloc/HSH_RESOURCES","hsh":"Satobloc/HsH","archive":"Satobloc/SAT_THEORY_ARCHIVE_2023-25"}
PATH_TERMS=("podcast","podcast_ep","podcast eps","podcast stats","episode","debatinga.i","debating a.i","debating ai","the new physics","field notes")
TRANSCRIPT_TERMS=("transcript","field notes","first public mention","subtitle","caption")
ANALYTICS_TERMS=("analytics","listener","listenership","ranking","geolocation","audience","streams","starts","spotify","podlod","podlode","stats")
TEXT={".txt",".md",".srt",".vtt"}; DATA={".csv",".json",".tsv",".xlsx",".pdf"}; IMAGES={".png",".jpg",".jpeg",".webp"}
RIGOR=re.compile(r"\b(rigor|rigorous|rigorously|validation|falsification|verification|proof|audit|criteria|canonical|accepted|tentative|speculative|independent|blind|provenance)\b",re.I)
INSIGHT=re.compile(r"\b(you asked(?: us)? (?:to|for)|our job is to|secondary mission|read between the lines|identify additional (?:insights|convergences)|find additional (?:insights|convergences)|determine additional)\b",re.I)
FIELD=re.compile(r"\b(?:field theory|twist field|scalar field|field)\b",re.I)
DATES=[re.compile(r"(?im)^Published:\s*([A-Z][a-z]+\s+\d{1,2},\s+\d{4})"),re.compile(r"(?im)^Published Date:\s*([A-Z][a-z]+\s+\d{1,2},\s+\d{4})"),re.compile(r"(?im)^Release Date:\s*([A-Z][a-z]+\s+\d{1,2},\s+\d{4})")]

def sha(p):
 h=hashlib.sha256()
 with p.open("rb") as f:
  for b in iter(lambda:f.read(1048576),b""):h.update(b)
 return h.hexdigest()
def commit(root):
 try:return subprocess.check_output(["git","-C",str(root),"rev-parse","HEAD"],text=True).strip()
 except:return ""
def blob(root,rel):
 try:
  x=subprocess.check_output(["git","-C",str(root),"ls-files","-s","--",rel],text=True).strip();return x.split()[1] if x else ""
 except:return ""
def norm(s):return re.sub(r"\s+"," ",re.sub(r"[^a-z0-9]+"," ",s.casefold())).strip()
def slug(s,n=90):return (re.sub(r"[^A-Za-z0-9]+","-",s).strip("-").lower()[:n].rstrip("-") or "untitled")
def candidate(rel):
 h=rel.as_posix().casefold().replace("_"," ");return any(t in h for t in PATH_TERMS)
def kind(rel):
 n=rel.name.casefold().replace("_"," ");e=rel.suffix.casefold()
 if e in {".srt",".vtt"}:return "transcript_subtitle"
 if e in TEXT and any(t in n for t in TRANSCRIPT_TERMS):return "transcript_text"
 if e in DATA|TEXT|IMAGES and any(t in n for t in ANALYTICS_TERMS):return "analytics"
 if e in IMAGES:return "analytics_capture"
 if e in DATA:return "metadata_or_analytics"
 if e in TEXT:return "podcast_text_unspecified"
 return "podcast_other"
def title(path):
 s=re.sub(r"^(FULL_|TRANSCRIPT_|PODCAST[_ -]*)+","",path.stem,flags=re.I);s=re.sub(r"^(The New Physics|DebatingA\.I\.)\s*[-_:]*\s*","",s,flags=re.I)
 return re.sub(r"\s+"," ",s.replace("_"," ")).strip()
def date_in(text):
 for pat in DATES:
  m=pat.search(text[:8000])
  if m:
   try:return datetime.strptime(m.group(1),"%B %d, %Y").date().isoformat()
   except ValueError:pass
 return ""
def cues(text):
 out=[]
 for block in re.split(r"\n{2,}",text.replace("\r\n","\n").replace("\r","\n").strip()):
  ls=[x for x in block.splitlines() if x.strip()]
  if ls and ls[0].strip().upper()=="WEBVTT":ls=ls[1:]
  if ls and re.fullmatch(r"\d+",ls[0].strip()):ls=ls[1:]
  i=next((i for i,x in enumerate(ls) if "-->" in x),None)
  if i is None:continue
  a,b=[x.strip() for x in ls[i].split("-->",1)];body="\n".join(ls[i+1:]).strip()
  if body:out.append({"cue_index":len(out)+1,"start":a,"end":b,"speaker":None,"text":body,"raw_text":body})
 return out
def write_csv(path,rows,fields):
 path.parent.mkdir(parents=True,exist_ok=True)
 with path.open("w",encoding="utf-8",newline="") as f:
  w=csv.DictWriter(f,fieldnames=fields,extrasaction="ignore");w.writeheader();w.writerows(rows)
def rankings(root):
 p=root/"EXPOSURE_STATS/PODCAST_EPs/DebatingA.I.OnScience_EpisodeRankings_all-time.csv";out={}
 if p.exists():
  with p.open("r",encoding="utf-8-sig",newline="") as f:
   for r in csv.DictReader(f):
    t=(r.get("Episode title") or "").strip()
    if t:out[norm(t)]=r
 return out
def rank_match(t,rs):
 n=norm(t)
 if n in rs:return rs[n]
 ms=[r for k,r in rs.items() if len(n)>=12 and (n in k or k in n)]
 return ms[0] if len(ms)==1 else None

def main():
 ap=argparse.ArgumentParser();ap.add_argument("--resources-root",type=Path,required=True);ap.add_argument("--hsh-root",type=Path,required=True);ap.add_argument("--archive-root",type=Path,required=True);a=ap.parse_args()
 roots={"resources":a.resources_root.resolve(),"hsh":a.hsh_root.resolve(),"archive":a.archive_root.resolve()};out=roots["resources"]/"EXPOSURE_STATS/PODCAST_GUIDE";out.mkdir(parents=True,exist_ok=True)
 src=[]
 for rk,root in roots.items():
  if not root.exists():continue
  for p in root.rglob("*"):
   if not p.is_file():continue
   rel=p.relative_to(root)
   if ".git" in rel.parts or any(x.casefold()=="prior_art" for x in rel.parts):continue
   if rk=="resources" and rel.as_posix().startswith("EXPOSURE_STATS/PODCAST_GUIDE/"):continue
   if not candidate(rel):continue
   k=kind(rel);digest=sha(p);txt="";d="";rg=ins=fh=False;derived="";cuepath=""
   if p.suffix.casefold() in TEXT and k in {"transcript_subtitle","transcript_text","podcast_text_unspecified"}:
    txt=p.read_text(encoding="utf-8",errors="replace");d=date_in(txt);sample=txt[:2000000];rg=bool(RIGOR.search(sample));ins=bool(INSIGHT.search(sample));fh=bool(FIELD.search(sample))
   if k in {"transcript_subtitle","transcript_text"}:
    base=f"{rk}--{slug(p.stem)}--{digest[:12]}";td=out/"text";cd=out/"cues";td.mkdir(exist_ok=True);cd.mkdir(exist_ok=True);tp=td/f"{base}.txt";body=txt
    if k=="transcript_subtitle":
     cc=cues(txt);prev=None;lines=[]
     for c in cc:
      s=re.sub(r"\s+"," ",c["text"]).strip()
      if s and s!=prev:lines.append(s);prev=s
     body="\n".join(lines)+("\n" if lines else "");cp=cd/f"{base}.jsonl"
     with cp.open("w",encoding="utf-8") as f:
      for c in cc:f.write(json.dumps(c,ensure_ascii=False)+"\n")
     cuepath=cp.relative_to(roots["resources"]).as_posix()
    header=f"# DERIVED TRANSCRIPT TEXT — MECHANICAL EXTRACTION ONLY\n# source_repository: {REPOS[rk]}\n# source_path: {rel.as_posix()}\n# source_sha256: {digest}\n# builder: {VERSION}\n# Raw source remains canonical. No theory terminology normalization applied.\n\n";tp.write_text(header+body,encoding="utf-8");derived=tp.relative_to(roots["resources"]).as_posix()
   src.append({"source_id":f"{rk}:{digest[:16]}","repository":REPOS[rk],"repo_key":rk,"path":rel.as_posix(),"kind":k,"extension":p.suffix.casefold(),"bytes":p.stat().st_size,"sha256":digest,"git_blob":blob(root,rel.as_posix()),"duplicate_group":"","title_candidate":title(p),"published_date_candidate":d,"public_exposure_evidence":True,"rigor_signal":rg,"insight_generation_requested":ins,"terminology_hazard_field":fh,"derived_text_path":derived,"cue_jsonl_path":cuepath})
 counts=defaultdict(int)
 for s in src:counts[s["sha256"]]+=1
 for s in src:
  if counts[s["sha256"]]>1:s["duplicate_group"]="sha256:"+s["sha256"]
 src.sort(key=lambda x:(x["repository"],x["path"].casefold()));fields=list(src[0]) if src else []
 write_csv(out/"SOURCE_INVENTORY.csv",src,fields);analytics=[s for s in src if s["kind"] in {"analytics","analytics_capture","metadata_or_analytics"}];write_csv(out/"ANALYTICS_INVENTORY.csv",analytics,fields)
 rs=rankings(roots["resources"]);groups=defaultdict(list)
 for s in src:
  if s["kind"] not in {"transcript_subtitle","transcript_text"}:continue
  r=rank_match(s["title_candidate"],rs);t=(r.get("Episode title") if r else "") or s["title_candidate"];d=s["published_date_candidate"]
  if not d and r:
   try:d=datetime.strptime((r.get("Publish date") or "").strip(),"%m/%d/%Y").date().isoformat()
   except ValueError:pass
  groups[(d,norm(t))].append((s,r,t))
 eps=[]
 for (d,_),items in groups.items():
  s0,r,t=items[0];trans=[x[0] for x in items]
  eps.append({"episode_id":f"ep-{d or 'undated'}-{slug(t,70)}","series":"Debating A.I. On the Future of Physics / The New Physics","series_aliases":["Debating A.I.","DAI","The New Physics"],"title":t,"published_date":d,"published_date_basis":"transcript_header_or_episode_rankings","episode_number_if_known":"","duration":(r.get("Duration") if r else "") or "","spotify_uri_or_url":(r.get("Episode URI") if r else "") or "","source_instances":[x[0]["source_id"] for x in items],"transcript_status":"located","derived_text_paths":[x["derived_text_path"] for x in trans if x["derived_text_path"]],"analytics_sources":[],"public_exposure_evidence":True,"interpretive_task_class":"insight_generation_requested" if any(x[0]["insight_generation_requested"] for x in items) else "ordinary_public_exposition","rigor_signal":any(x[0]["rigor_signal"] for x in items),"terminology_hazards":["field"] if any(x[0]["terminology_hazard_field"] for x in items) else [],"review_status":"unreviewed","notes":"Public-exposure record; not automatic SAT/H(s)H core authority."})
 eps.sort(key=lambda x:(x["published_date"] or "9999",x["title"].casefold()));(out/"EPISODES.json").write_text(json.dumps(eps,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
 flat=[{"episode_id":e["episode_id"],"published_date":e["published_date"],"title":e["title"],"transcript_status":e["transcript_status"],"source_instance_count":len(e["source_instances"]),"derived_text_count":len(e["derived_text_paths"]),"interpretive_task_class":e["interpretive_task_class"],"rigor_signal":e["rigor_signal"],"terminology_hazards":";".join(e["terminology_hazards"]),"spotify_uri_or_url":e["spotify_uri_or_url"],"review_status":e["review_status"]} for e in eps];write_csv(out/"EPISODES.csv",flat,list(flat[0]) if flat else [])
 lines=["# Episode Guide","","Mechanical cross-repository guide. Podcast transcripts are public-exposure evidence, not automatic SAT/H(s)H core authority.","",f"Episodes represented: **{len(eps)}**  ",f"Source instances: **{len(src)}**  ",f"Analytics/metadata instances: **{len(analytics)}**","","| Date | Episode | Transcript | Sources | Review signals |","|---|---|---|---:|---|"]
 for e in eps:
  sig=[]
  if e["interpretive_task_class"]=="insight_generation_requested":sig.append("insight-generation requested")
  if e["rigor_signal"]:sig.append("rigor signal")
  if "field" in e["terminology_hazards"]:sig.append("field-language hazard")
  lines.append(f"| {e['published_date'] or 'undated'} | {e['title'].replace('|','/')} | {e['transcript_status']} | {len(e['source_instances'])} | {', '.join(sig)} |")
 (out/"EPISODE_GUIDE.md").write_text("\n".join(lines)+"\n",encoding="utf-8")
 manifest={"builder":VERSION,"generated_at_utc":datetime.now(timezone.utc).isoformat(),"input_commits":{k:commit(v) for k,v in roots.items()},"repositories":REPOS,"counts":{"source_instances":len(src),"episodes":len(eps),"analytics_or_metadata_sources":len(analytics),"duplicate_groups":sum(1 for n in counts.values() if n>1)},"quarantine_rule":"PRIOR_ART pruned before traversal","theory_status_rule":"podcast transcripts are public-exposure evidence, not automatic core authority"};(out/"MANIFEST.json").write_text(json.dumps(manifest,indent=2)+"\n",encoding="utf-8");print(json.dumps(manifest["counts"],indent=2))
if __name__=="__main__":main()
