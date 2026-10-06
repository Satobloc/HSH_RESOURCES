#!/usr/bin/env python3
"""Local full-text ChatGPT export browser + multi-select exporter.

Uses only the Python standard library. It never uploads ChatGPT export contents.

Examples
--------
python chatgpt_export_picker.py ~/Downloads/chatgpt-export.zip --out ~/SAT_CHAT_INTAKE
python chatgpt_export_picker.py ~/Downloads/export-folder --out ~/SAT_CHAT_INTAKE --port 8787

Then open http://127.0.0.1:8787/ . Search title + full message text,
select multiple conversations, and export preserved raw JSON + readable Markdown.
"""
from __future__ import annotations

import argparse, csv, datetime as dt, html, io, json, os, re, sqlite3, sys, urllib.parse, zipfile
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path


def safe_name(s: str, limit=120) -> str:
    s = re.sub(r'[<>:"/\\|?*\x00-\x1f]+', '_', s or 'untitled')
    s = re.sub(r'\s+', ' ', s).strip(' ._') or 'untitled'
    return s[:limit]


def content_text(content) -> str:
    if not isinstance(content, dict):
        return ''
    parts = content.get('parts')
    if isinstance(parts, list):
        vals=[]
        for p in parts:
            if isinstance(p, str): vals.append(p)
            elif isinstance(p, dict):
                # Some exports store structured text/image metadata.
                t = p.get('text') or p.get('content')
                if isinstance(t, str): vals.append(t)
        return '\n'.join(vals)
    text = content.get('text')
    return text if isinstance(text, str) else ''


def flatten_messages(conv: dict) -> list[dict]:
    """Return message records in a stable approximate chronological order.

    ChatGPT exports can contain branches. We preserve every message node rather
    than silently selecting only one branch; node IDs and parent IDs are kept in
    the raw JSON, and Markdown labels each recovered node's timestamp/role.
    """
    mapping = conv.get('mapping') or {}
    out=[]
    if isinstance(mapping, dict):
        for node_id,node in mapping.items():
            if not isinstance(node, dict): continue
            msg=node.get('message')
            if not isinstance(msg, dict): continue
            author=msg.get('author') or {}
            role=author.get('role') if isinstance(author, dict) else str(author)
            txt=content_text(msg.get('content') or {})
            if not txt.strip(): continue
            out.append({
                'node_id': node_id,
                'parent': node.get('parent'),
                'role': role or 'unknown',
                'create_time': msg.get('create_time'),
                'text': txt,
            })
    else:
        # Fallback for future/simpler export shapes.
        msgs=conv.get('messages') or []
        for i,msg in enumerate(msgs):
            if not isinstance(msg, dict): continue
            role=msg.get('role') or ((msg.get('author') or {}).get('role') if isinstance(msg.get('author'),dict) else 'unknown')
            txt=content_text(msg.get('content') or {}) or (msg.get('text') if isinstance(msg.get('text'),str) else '')
            if txt.strip(): out.append({'node_id':str(i),'parent':None,'role':role,'create_time':msg.get('create_time'),'text':txt})
    def key(m):
        t=m.get('create_time')
        try: return (0,float(t),str(m.get('node_id')))
        except Exception: return (1,0,str(m.get('node_id')))
    return sorted(out,key=key)


def epoch_iso(x):
    try:
        return dt.datetime.fromtimestamp(float(x), tz=dt.timezone.utc).isoformat()
    except Exception:
        return ''


def discover_json_sources(path: Path):
    """Yield (label, bytes) for conversations JSON files from zip/dir/file."""
    if path.is_file() and path.suffix.lower()=='.zip':
        with zipfile.ZipFile(path) as z:
            names=[n for n in z.namelist() if re.search(r'(^|/)conversations(?:_\d+)?\.json$',n,re.I)]
            if not names:
                names=[n for n in z.namelist() if n.lower().endswith('.json') and 'conversation' in Path(n).name.lower()]
            for n in names:
                yield f'{path.name}:{n}', z.read(n)
    elif path.is_dir():
        files=sorted(path.rglob('conversations*.json'))
        if not files: files=sorted(p for p in path.rglob('*.json') if 'conversation' in p.name.lower())
        for p in files: yield str(p), p.read_bytes()
    elif path.is_file():
        yield str(path), path.read_bytes()
    else:
        raise FileNotFoundError(path)


def iter_conversations(path: Path):
    for label,data in discover_json_sources(path):
        obj=json.loads(data.decode('utf-8'))
        if isinstance(obj,list): rows=obj
        elif isinstance(obj,dict) and isinstance(obj.get('conversations'),list): rows=obj['conversations']
        else: rows=[obj]
        for conv in rows:
            if isinstance(conv,dict): yield label,conv


def build_db(source: Path, db_path: Path, rebuild=False):
    if rebuild and db_path.exists(): db_path.unlink()
    con=sqlite3.connect(db_path)
    con.execute('PRAGMA journal_mode=WAL')
    con.execute('CREATE TABLE IF NOT EXISTS conversations (id TEXT PRIMARY KEY, title TEXT, create_time REAL, update_time REAL, source_file TEXT, body TEXT, raw_json TEXT)')
    try:
        con.execute("CREATE VIRTUAL TABLE IF NOT EXISTS conv_fts USING fts5(id UNINDEXED, title, body, tokenize='unicode61')")
    except sqlite3.OperationalError as e:
        raise RuntimeError('This Python SQLite build lacks FTS5 support.') from e
    existing=con.execute('SELECT COUNT(*) FROM conversations').fetchone()[0]
    if existing and not rebuild:
        return con,existing
    con.execute('DELETE FROM conversations'); con.execute('DELETE FROM conv_fts')
    n=0
    for source_file,conv in iter_conversations(source):
        cid=str(conv.get('id') or conv.get('conversation_id') or f'anon-{n:08d}')
        title=str(conv.get('title') or 'Untitled')
        msgs=flatten_messages(conv)
        body='\n\n'.join(f"[{m['role']}] {m['text']}" for m in msgs)
        raw=json.dumps(conv,ensure_ascii=False)
        con.execute('INSERT OR REPLACE INTO conversations VALUES (?,?,?,?,?,?,?)',(cid,title,conv.get('create_time'),conv.get('update_time'),source_file,body,raw))
        con.execute('INSERT INTO conv_fts(id,title,body) VALUES (?,?,?)',(cid,title,body))
        n+=1
        if n%500==0: con.commit(); print(f'indexed {n}',file=sys.stderr)
    con.commit(); return con,n


def markdown(conv: dict) -> str:
    title=str(conv.get('title') or 'Untitled')
    cid=str(conv.get('id') or conv.get('conversation_id') or '')
    lines=[f'# {title}','',f'- Conversation ID: `{cid}`',f'- Created UTC: `{epoch_iso(conv.get("create_time"))}`',f'- Updated UTC: `{epoch_iso(conv.get("update_time"))}`','', '---','']
    for m in flatten_messages(conv):
        stamp=epoch_iso(m.get('create_time'))
        lines += [f"## {str(m.get('role') or 'unknown').upper()} — {stamp}",'',m['text'],'']
    return '\n'.join(lines).rstrip()+'\n'


def export_ids(con: sqlite3.Connection, ids: list[str], out: Path):
    batch=dt.datetime.now(dt.timezone.utc).strftime('%Y%m%dT%H%M%SZ')
    root=out/f'chatgpt_selected_{batch}'; rawdir=root/'RAW_JSON'; mddir=root/'MARKDOWN'
    rawdir.mkdir(parents=True,exist_ok=True); mddir.mkdir(parents=True,exist_ok=True)
    manifest=[]
    for cid in ids:
        row=con.execute('SELECT id,title,create_time,update_time,source_file,raw_json FROM conversations WHERE id=?',(cid,)).fetchone()
        if not row: continue
        cid,title,ct,ut,src,raw=row; conv=json.loads(raw)
        stem=f"{safe_name(title)}__{safe_name(cid,50)}"
        rp=rawdir/f'{stem}.json'; mp=mddir/f'{stem}.md'
        rp.write_text(json.dumps(conv,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
        mp.write_text(markdown(conv),encoding='utf-8')
        manifest.append({'conversation_id':cid,'title':title,'created_utc':epoch_iso(ct),'updated_utc':epoch_iso(ut),'export_source':src,'raw_json':str(rp.relative_to(root)),'markdown':str(mp.relative_to(root))})
    with (root/'manifest.csv').open('w',newline='',encoding='utf-8') as f:
        fields=list(manifest[0]) if manifest else ['conversation_id','title','created_utc','updated_utc','export_source','raw_json','markdown']
        w=csv.DictWriter(f,fieldnames=fields); w.writeheader(); w.writerows(manifest)
    (root/'README.md').write_text(f'# Selected ChatGPT conversation intake\n\nGenerated UTC: {dt.datetime.now(dt.timezone.utc).isoformat()}\n\nConversations: {len(manifest)}\n\nRaw JSON is preserved alongside normalized Markdown. The account export remains the upstream source.\n',encoding='utf-8')
    return root,len(manifest)


def page(results, q, total):
    cards=[]
    for cid,title,ct,ut,snippet in results:
        cards.append(f'''<label class="card"><input type="checkbox" name="id" value="{html.escape(cid,quote=True)}"><span><b>{html.escape(title)}</b><br><small>{html.escape(epoch_iso(ct))} · {html.escape(cid)}</small><br><span>{html.escape((snippet or '')[:700])}</span></span></label>''')
    return f'''<!doctype html><meta charset="utf-8"><title>ChatGPT Export Picker</title>
<style>body{{font-family:system-ui;max-width:1200px;margin:2rem auto;padding:0 1rem}}form.search{{display:flex;gap:.5rem}}input[type=text]{{flex:1;padding:.7rem}}button{{padding:.7rem 1rem}}.card{{display:flex;gap:.8rem;padding:1rem;border-bottom:1px solid #ddd}}.card input{{margin-top:.25rem}}small{{opacity:.65}}.bar{{position:sticky;top:0;background:white;padding:.7rem 0;border-bottom:1px solid #ccc}}</style>
<h1>ChatGPT Export Picker</h1><p>Indexed conversations: {total}. Search is local to this computer.</p>
<form class="search" method="get"><input type="text" name="q" value="{html.escape(q,quote=True)}" placeholder="Full-text search"><button>Search</button></form>
<form method="post" action="/export"><div class="bar"><button type="button" onclick="document.querySelectorAll('input[name=id]').forEach(x=>x.checked=true)">Select all shown</button> <button type="button" onclick="document.querySelectorAll('input[name=id]').forEach(x=>x.checked=false)">Clear</button> <button type="submit">Export selected</button></div>{''.join(cards)}</form>'''


def serve(con, out, host, port):
    class H(BaseHTTPRequestHandler):
        def send_html(self,s,status=200):
            b=s.encode('utf-8'); self.send_response(status); self.send_header('Content-Type','text/html; charset=utf-8'); self.send_header('Content-Length',str(len(b))); self.end_headers(); self.wfile.write(b)
        def do_GET(self):
            u=urllib.parse.urlparse(self.path)
            if u.path!='/': return self.send_html('Not found',404)
            qs=urllib.parse.parse_qs(u.query); q=(qs.get('q') or [''])[0].strip(); limit=300
            if q:
                # Quote user tokens for a forgiving AND query; fall back to LIKE if FTS syntax fails.
                terms=[t for t in re.findall(r'[^\s"]+',q) if t]
                fts=' AND '.join('"'+t.replace('"','')+'"' for t in terms)
                try:
                    rows=con.execute('SELECT c.id,c.title,c.create_time,c.update_time,snippet(conv_fts,2,"","", " … ", 45) FROM conv_fts JOIN conversations c USING(id) WHERE conv_fts MATCH ? ORDER BY rank LIMIT ?',(fts,limit)).fetchall()
                except sqlite3.OperationalError:
                    like=f'%{q}%'; rows=con.execute('SELECT id,title,create_time,update_time,substr(body,1,700) FROM conversations WHERE title LIKE ? OR body LIKE ? ORDER BY update_time DESC LIMIT ?',(like,like,limit)).fetchall()
            else:
                rows=con.execute('SELECT id,title,create_time,update_time,substr(body,1,700) FROM conversations ORDER BY update_time DESC LIMIT ?',(limit,)).fetchall()
            total=con.execute('SELECT COUNT(*) FROM conversations').fetchone()[0]
            self.send_html(page(rows,q,total))
        def do_POST(self):
            if self.path!='/export': return self.send_html('Not found',404)
            n=int(self.headers.get('Content-Length','0')); data=self.rfile.read(n).decode('utf-8'); form=urllib.parse.parse_qs(data); ids=form.get('id') or []
            root,count=export_ids(con,ids,out)
            self.send_html(f'<h1>Exported {count}</h1><p>Saved to <code>{html.escape(str(root))}</code></p><p><a href="/">Back</a></p>')
        def log_message(self,fmt,*args): pass
    srv=ThreadingHTTPServer((host,port),H)
    print(f'Open http://{host}:{port}/',file=sys.stderr)
    print(f'Exports will be written under: {out}',file=sys.stderr)
    try: srv.serve_forever()
    except KeyboardInterrupt: pass


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('export',type=Path,help='ChatGPT export ZIP, export directory, or conversations*.json')
    ap.add_argument('--out',type=Path,default=Path('CHATGPT_SELECTED_EXPORTS'))
    ap.add_argument('--db',type=Path,default=None)
    ap.add_argument('--rebuild',action='store_true')
    ap.add_argument('--host',default='127.0.0.1')
    ap.add_argument('--port',type=int,default=8787)
    a=ap.parse_args(); a.out.mkdir(parents=True,exist_ok=True)
    db=a.db or (a.out/'chatgpt_export_index.sqlite')
    con,n=build_db(a.export,db,a.rebuild)
    print(f'Indexed {n} conversations',file=sys.stderr)
    serve(con,a.out,a.host,a.port)

if __name__=='__main__': main()
