#!/usr/bin/env python3
"""Stage arbitrary local files/directories into an HsH INGEST batch.

This is intentionally a local-filesystem tool. It preserves source names/relative
paths, hashes content, detects exact duplicates in prior intake manifests, and
can optionally git commit/push from an existing local HsH checkout.

Examples:
  python batch_file_stage.py --repo C:\\repos\\HsH --source-system OFFLINE_DISK D:\\SAT_OFFLINE
  python batch_file_stage.py --repo ~/repos/HsH --source-system NOTEBOOKLM_EXPORT ~/Downloads/notebook-export --commit --push
"""
from __future__ import annotations
import argparse, csv, datetime as dt, hashlib, json, os, shutil, subprocess, sys
from pathlib import Path

GITHUB_SOFT_LIMIT = 95 * 1024 * 1024  # warn before GitHub's hard 100 MB blob limit


def sha256(path: Path, block=1024*1024):
    h=hashlib.sha256()
    with path.open('rb') as f:
        while True:
            b=f.read(block)
            if not b: break
            h.update(b)
    return h.hexdigest()


def prior_hashes(repo: Path):
    out={}
    root=repo/'INGEST'
    if not root.exists(): return out
    for p in root.rglob('manifest.csv'):
        try:
            with p.open(encoding='utf-8',newline='') as f:
                for r in csv.DictReader(f):
                    h=(r.get('sha256') or '').strip()
                    if h and h not in out: out[h]=f"{p.relative_to(repo)}::{r.get('staged_path','')}"
        except Exception: pass
    return out


def expand_inputs(paths):
    """Yield (input_root, file, relative_path)."""
    for raw in paths:
        p=Path(raw).expanduser().resolve()
        if p.is_file():
            yield p.parent,p,Path(p.name)
        elif p.is_dir():
            for f in sorted(x for x in p.rglob('*') if x.is_file()):
                yield p,f,Path(p.name)/f.relative_to(p)
        else:
            print(f'WARNING missing: {p}',file=sys.stderr)


def unique_dest(base: Path, rel: Path):
    d=base/rel
    if not d.exists(): return d
    stem,suffix=d.stem,d.suffix; i=2
    while True:
        cand=d.with_name(f'{stem}__collision_{i}{suffix}')
        if not cand.exists(): return cand
        i+=1


def git(repo:Path,*args):
    return subprocess.run(['git','-C',str(repo),*args],check=True,text=True)


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--repo',type=Path,required=True,help='existing local checkout of Satobloc/HsH')
    ap.add_argument('--source-system',required=True,help='e.g. OFFLINE_DISK, CHATGPT_EXPORT, NOTEBOOKLM_EXPORT')
    ap.add_argument('--batch-id',default=None)
    ap.add_argument('--dest-root',default='INGEST/INBOX')
    ap.add_argument('--no-copy-duplicates',action='store_true',default=True)
    ap.add_argument('--copy-duplicates',dest='no_copy_duplicates',action='store_false')
    ap.add_argument('--commit',action='store_true')
    ap.add_argument('--push',action='store_true')
    ap.add_argument('inputs',nargs='+')
    a=ap.parse_args(); repo=a.repo.expanduser().resolve()
    if not (repo/'.git').exists(): raise SystemExit(f'Not a git checkout: {repo}')
    now=dt.datetime.now(dt.timezone.utc); batch=a.batch_id or f"{now.strftime('%Y-%m-%d_%H%M%S')}_{a.source_system.lower()}"
    root=repo/a.dest_root/batch; rawdir=root/'RAW'; rawdir.mkdir(parents=True,exist_ok=False)
    known=prior_hashes(repo); rows=[]
    for input_root,f,rel in expand_inputs(a.inputs):
        st=f.stat(); h=sha256(f); dup=known.get(h,''); too_large=st.st_size>GITHUB_SOFT_LIMIT
        status='DUPLICATE_NOT_COPIED' if dup and a.no_copy_duplicates else ('OVERSIZE_STAGED_LOCAL' if too_large else 'STAGED')
        staged=''
        if status!='DUPLICATE_NOT_COPIED':
            dest=unique_dest(rawdir,rel); dest.parent.mkdir(parents=True,exist_ok=True); shutil.copy2(f,dest); staged=str(dest.relative_to(repo))
            known.setdefault(h,staged)
        rows.append({
            'batch_id':batch,'source_system':a.source_system,'original_path':str(f),'relative_input_path':str(rel),
            'original_filename':f.name,'bytes':st.st_size,'sha256':h,'filesystem_mtime_utc':dt.datetime.fromtimestamp(st.st_mtime,tz=dt.timezone.utc).isoformat(),
            'acquired_utc':now.isoformat(),'staged_path':staged,'duplicate_of':dup,'github_oversize_warning':str(too_large).lower(),
            'processing_status':status,'canonical_destination_status':'UNREVIEWED','provenance_notes':''
        })
    fields=list(rows[0]) if rows else []
    with (root/'manifest.csv').open('w',newline='',encoding='utf-8') as fh:
        w=csv.DictWriter(fh,fieldnames=fields); w.writeheader(); w.writerows(rows)
    (root/'manifest.json').write_text(json.dumps(rows,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    counts={}
    for r in rows: counts[r['processing_status']]=counts.get(r['processing_status'],0)+1
    (root/'README.md').write_text(
        f"# Intake batch `{batch}`\n\nSource system: `{a.source_system}`\n\nAcquired UTC: `{now.isoformat()}`\n\nFiles considered: **{len(rows)}**\n\nStatus counts: `{json.dumps(counts,sort_keys=True)}`\n\nFilesystem timestamps are preserved as evidence only and are not treated as authoritative creation dates. Exact duplicate detection is SHA-256 based. Oversize warnings require separate large-file handling before push.\n",
        encoding='utf-8')
    print(f'Staged batch: {root}')
    print(json.dumps(counts,indent=2))
    if a.commit or a.push:
        git(repo,'add',str(root.relative_to(repo)))
        git(repo,'commit','-m',f'Ingest offline batch {batch}')
    if a.push: git(repo,'push')

if __name__=='__main__': main()
