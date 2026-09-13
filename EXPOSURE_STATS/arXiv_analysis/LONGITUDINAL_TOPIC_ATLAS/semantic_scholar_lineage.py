#!/usr/bin/env python3
"""Harvest explicit citation lineage from Semantic Scholar Academic Graph.

Input IDs may be Semantic Scholar paper IDs, DOI:<doi>, or ARXIV:<id>.
Writes normalized node and edge files. Explicit citations only; no similarity-
based influence inference.
"""
from __future__ import annotations
import argparse, csv, json, os, time, urllib.error, urllib.parse, urllib.request
from pathlib import Path

BASE = "https://api.semanticscholar.org/graph/v1"
FIELDS = "paperId,corpusId,title,year,authors,venue,publicationDate,externalIds,url,abstract,citationCount,referenceCount"
EDGE_FIELDS = "contexts,intents,isInfluential,title,year,authors,externalIds,url"


def get_json(url: str, api_key: str | None, retries: int = 5):
    headers = {"User-Agent": "HsH-CitationLineage/1.0"}
    if api_key:
        headers["x-api-key"] = api_key
    last = None
    for i in range(retries):
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=90) as r:
                return json.loads(r.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            last = e
            if e.code not in (429, 500, 502, 503, 504):
                raise
        except Exception as e:
            last = e
        time.sleep(min(30, 2 ** (i + 1)))
    raise RuntimeError(f"request failed: {last}")


def paper(pid: str, key: str | None):
    q = urllib.parse.urlencode({"fields": FIELDS})
    return get_json(f"{BASE}/paper/{urllib.parse.quote(pid, safe=':/.')}?{q}", key)


def paged_edges(pid: str, direction: str, key: str | None):
    out = []
    offset = 0
    while True:
        q = urllib.parse.urlencode({"fields": EDGE_FIELDS, "limit": 1000, "offset": offset})
        obj = get_json(f"{BASE}/paper/{urllib.parse.quote(pid, safe=':/.')}/{direction}?{q}", key)
        out.extend(obj.get("data", []))
        nxt = obj.get("next")
        if nxt is None:
            break
        offset = nxt
        time.sleep(1.1 if key else 2.0)
    return out


def norm_authors(xs):
    return "; ".join(a.get("name", "") for a in (xs or []) if a.get("name"))


def node_row(p):
    ex = p.get("externalIds") or {}
    return {
        "paperId": p.get("paperId"), "corpusId": p.get("corpusId"),
        "title": p.get("title"), "year": p.get("year"),
        "publicationDate": p.get("publicationDate"), "venue": p.get("venue"),
        "authors": norm_authors(p.get("authors")), "arxiv": ex.get("ArXiv"),
        "doi": ex.get("DOI"), "url": p.get("url"),
        "citationCount": p.get("citationCount"), "referenceCount": p.get("referenceCount"),
        "abstract": p.get("abstract") or "",
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("ids", nargs="+")
    ap.add_argument("--out", type=Path, required=True)
    args = ap.parse_args()
    key = os.environ.get("SEMANTIC_SCHOLAR_API_KEY")
    args.out.mkdir(parents=True, exist_ok=True)
    nodes = {}
    edges = []
    raw = {}

    for supplied in args.ids:
        root = paper(supplied, key)
        rid = root["paperId"]
        nodes[rid] = node_row(root)
        refs = paged_edges(rid, "references", key)
        cites = paged_edges(rid, "citations", key)
        raw[rid] = {"root": root, "references": refs, "citations": cites}

        for direction, items, inner, src_is_root in [
            ("reference", refs, "citedPaper", True),
            ("citation", cites, "citingPaper", False),
        ]:
            for item in items:
                p = item.get(inner) or {}
                if not p.get("paperId"):
                    continue
                nodes.setdefault(p["paperId"], node_row(p))
                if src_is_root:
                    src, dst = rid, p["paperId"]
                else:
                    src, dst = p["paperId"], rid
                edges.append({
                    "source_paperId": src, "target_paperId": dst,
                    "edge_type": "EXPLICIT-CITATION",
                    "relation_to_seed": direction,
                    "contexts": " || ".join(item.get("contexts") or []),
                    "intents": "; ".join(item.get("intents") or []),
                    "isInfluential": item.get("isInfluential"),
                })
        time.sleep(1.1 if key else 2.0)

    node_fields = ["paperId","corpusId","title","year","publicationDate","venue","authors","arxiv","doi","url","citationCount","referenceCount","abstract"]
    with (args.out / "nodes.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=node_fields); w.writeheader(); w.writerows(nodes.values())
    edge_fields = ["source_paperId","target_paperId","edge_type","relation_to_seed","contexts","intents","isInfluential"]
    with (args.out / "edges.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=edge_fields); w.writeheader(); w.writerows(edges)
    (args.out / "lineage.json").write_text(json.dumps({"seeds": args.ids, "nodes": list(nodes.values()), "edges": edges, "raw": raw}, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    (args.out / "README.md").write_text(
        "# Citation lineage output\n\nEdges are explicit Semantic Scholar citation/reference records. Citation context, intent, and influential flags are retained when available. Missing edges are not evidence of no influence.\n",
        encoding="utf-8")
    print(f"wrote {len(nodes)} nodes and {len(edges)} explicit citation edges")

if __name__ == "__main__":
    main()
