#!/usr/bin/env python3
"""Harvest discoverable primary/secondary sources for the history of spatial 4D thought.

Read scope:
  - this tool's JSON configuration;
  - explicitly supplied local files (only with --import-file).
  - public archive/API endpoints named in this script/configuration.

Write scope (only with --apply):
  HISTORICAL/FOURTH_DIMENSION_HISTORY/harvested/

The default is a dry run. Source documents are never modified. Downloads are
opt-in, sequential, size-bounded, and restricted to sources with an explicit
open-access/open-license signal. Paywalls, login walls, bot challenges, and
access controls are not bypassed.

Python 3.10+, standard library only.
"""
from __future__ import annotations

import argparse
import hashlib
import html
import json
import os
import random
import re
import shutil
import subprocess
import sys
import tempfile
import time
import urllib.error
import urllib.parse
import urllib.request
import uuid
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path
from typing import Any, Iterable

VERSION = "0.2.0"
PROJECT_ROOT = Path("HISTORICAL/FOURTH_DIMENSION_HISTORY")
OUTPUT_ROOT = PROJECT_ROOT / "harvested"
DEFAULT_CONFIG = Path(__file__).with_name("queries.json")
USER_AGENT = "FourthDimensionHistoryHarvester/0.2 (scholarly discovery; respectful low-rate access)"
EXCLUDED_COMPONENTS = {
    ".git", ".github", "__pycache__", ".pytest_cache", "PRIOR_ART",
    "PRIVATE_WORKSPACE", "QUARANTINE", "QUARANTINED", "SANDBOX",
}
OPEN_LICENSE_MARKERS = (
    "creativecommons.org/licenses/",
    "creativecommons.org/publicdomain/zero/",
    "creativecommons.org/publicdomain/mark/",
    "rightsstatements.org/vocab/noc/",
    "rightsstatements.org/vocab/noc-us/",
    "rightsstatements.org/vocab/noc-oklr/",
    "public domain",
    "cc-by", "cc-by-sa", "cc-by-nc", "cc-by-nc-sa", "cc-by-nd", "cc-by-nc-nd",
)


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def make_run_id() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ") + "_" + uuid.uuid4().hex[:8]


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def normalize_space(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, (list, tuple)):
        return "; ".join(normalize_space(item) for item in value if item is not None)
    if isinstance(value, dict):
        return json.dumps(value, ensure_ascii=False, sort_keys=True)
    return re.sub(r"\s+", " ", html.unescape(str(value))).strip()


def first_nonempty(*values: Any) -> str:
    for value in values:
        text = normalize_space(value)
        if text:
            return text
    return ""


def parse_year(value: Any) -> int | None:
    match = re.search(r"\b(18|19|20)\d{2}\b", normalize_space(value))
    return int(match.group(0)) if match else None


def allowed_open_license(*values: Any) -> bool:
    text = " ".join(normalize_space(value).lower() for value in values if value)
    return any(marker in text for marker in OPEN_LICENSE_MARKERS)


def record_key(record: dict[str, Any]) -> str:
    doi = normalize_space(record.get("doi")).lower()
    if doi:
        return "doi:" + doi.removeprefix("https://doi.org/").removeprefix("http://doi.org/")
    identifier = normalize_space(record.get("identifier"))
    source = normalize_space(record.get("source"))
    if identifier:
        return f"{source}:{identifier}"
    url = normalize_space(record.get("url") or record.get("landing_page_url"))
    if url:
        return "url:" + url.split("#", 1)[0]
    return "sha256:" + sha256_bytes(json.dumps(record, ensure_ascii=False, sort_keys=True).encode("utf-8"))


def normalized_record(source: str, query: str, **fields: Any) -> dict[str, Any]:
    date_value = fields.get("date", "")
    year_value = fields.get("year") or date_value
    record = {
        "schema_version": 1,
        "source": source,
        "query": query,
        "harvested_at": utc_now(),
        "title": first_nonempty(fields.pop("title", "")),
        "authors": fields.pop("authors", []),
        "date": first_nonempty(fields.pop("date", "")),
        "year": parse_year(year_value),
        "publication": first_nonempty(fields.pop("publication", "")),
        "description": first_nonempty(fields.pop("description", "")),
        "snippet": first_nonempty(fields.pop("snippet", "")),
        "language": first_nonempty(fields.pop("language", "")),
        "identifier": first_nonempty(fields.pop("identifier", "")),
        "doi": first_nonempty(fields.pop("doi", "")),
        "url": first_nonempty(fields.pop("url", "")),
        "landing_page_url": first_nonempty(fields.pop("landing_page_url", "")),
        "pdf_url": first_nonempty(fields.pop("pdf_url", "")),
        "license": first_nonempty(fields.pop("license", "")),
        "rights": first_nonempty(fields.pop("rights", "")),
        "download_status": "not_requested",
        "download_path": "",
        "raw": fields,
    }
    record["dedup_key"] = record_key(record)
    record["record_id"] = sha256_bytes((source + "\0" + record["dedup_key"] + "\0" + query).encode("utf-8"))[:24]
    return record


class RateLimiter:
    def __init__(self, delay: float):
        self.delay = max(0.0, delay)
        self.last_by_host: dict[str, float] = {}

    def wait(self, url: str) -> None:
        host = urllib.parse.urlparse(url).netloc.lower()
        now = time.monotonic()
        remaining = self.delay - (now - self.last_by_host.get(host, 0.0))
        if remaining > 0:
            time.sleep(remaining)
        self.last_by_host[host] = time.monotonic()


class HttpClient:
    def __init__(self, delay: float = 1.25, timeout: int = 30, retries: int = 3, user_agent: str = USER_AGENT):
        self.limiter = RateLimiter(delay)
        self.timeout = timeout
        self.retries = max(0, retries)
        self.user_agent = user_agent

    def get(self, url: str, params: dict[str, Any] | list[tuple[str, str]] | None = None, accept: str = "*/*", max_bytes: int | None = None, extra_headers: dict[str, str] | None = None) -> tuple[bytes, dict[str, str], str]:
        if params:
            joiner = "&" if "?" in url else "?"
            url = url + joiner + urllib.parse.urlencode(params, doseq=True)
        last_error: Exception | None = None
        for attempt in range(self.retries + 1):
            self.limiter.wait(url)
            request = urllib.request.Request(
                url,
                headers={"User-Agent": self.user_agent, "Accept": accept, **(extra_headers or {})},
                method="GET",
            )
            try:
                with urllib.request.urlopen(request, timeout=self.timeout) as response:
                    body = response.read(max_bytes + 1) if max_bytes is not None else response.read()
                    if max_bytes is not None and len(body) > max_bytes:
                        raise RuntimeError(f"response exceeds configured size limit ({max_bytes} bytes): {url}")
                    return body, {k.lower(): v for k, v in response.headers.items()}, response.geturl()
            except urllib.error.HTTPError as exc:
                if exc.code in {401, 403, 404, 410, 451}:
                    raise RuntimeError(f"HTTP {exc.code} for {url}; access not retried or bypassed") from exc
                if exc.code not in {408, 425, 429, 500, 502, 503, 504} or attempt >= self.retries:
                    raise RuntimeError(f"HTTP {exc.code} for {url}") from exc
                retry_after = exc.headers.get("Retry-After") if exc.headers else None
                wait = float(retry_after) if retry_after and retry_after.isdigit() else min(30.0, 2.0 ** attempt + random.random())
                time.sleep(wait)
                last_error = exc
            except (urllib.error.URLError, TimeoutError, OSError) as exc:
                last_error = exc
                if attempt >= self.retries:
                    break
                time.sleep(min(30.0, 2.0 ** attempt + random.random()))
        raise RuntimeError(f"network failure for {url}: {last_error}")

    def get_json(self, url: str, params: dict[str, Any] | list[tuple[str, str]] | None = None, extra_headers: dict[str, str] | None = None) -> tuple[dict[str, Any], str]:
        body, headers, final_url = self.get(url, params, "application/json", extra_headers=extra_headers)
        if "json" not in headers.get("content-type", "").lower() and body.lstrip().startswith((b"<html", b"<!doctype html")):
            raise RuntimeError(f"expected JSON but received an HTML page from {final_url}; endpoint may have drifted or returned an access challenge")
        try:
            return json.loads(body.decode("utf-8", errors="replace")), final_url
        except json.JSONDecodeError as exc:
            raise RuntimeError(f"invalid JSON response from {final_url}: {body[:250]!r}") from exc


def safe_output_path(repo_root: Path, rel_path: Path) -> Path:
    if rel_path.is_absolute() or any(part in EXCLUDED_COMPONENTS for part in rel_path.parts):
        raise ValueError(f"refusing excluded or absolute output path: {rel_path}")
    if not rel_path.as_posix().startswith(OUTPUT_ROOT.as_posix() + "/"):
        raise ValueError(f"write path is outside declared output root: {rel_path}")
    repo_real = repo_root.resolve()
    target_expected = repo_real / rel_path
    root_expected = repo_real / OUTPUT_ROOT
    target = target_expected.resolve()
    root = root_expected.resolve()
    if target != target_expected or root != root_expected:
        raise ValueError(f"write path or declared output root traverses a symlink: {rel_path}")
    try:
        target.relative_to(root)
    except ValueError as exc:
        raise ValueError(f"write path escapes declared output root: {rel_path}") from exc
    return target


def atomic_create(path: Path, data: bytes) -> None:
    """Atomically create a file without replacing a concurrent writer's file."""
    path.parent.mkdir(parents=True, exist_ok=True)
    temp: Path | None = None
    try:
        with tempfile.NamedTemporaryFile("wb", dir=path.parent, prefix="." + path.name + ".", delete=False) as handle:
            handle.write(data)
            handle.flush()
            os.fsync(handle.fileno())
            temp = Path(handle.name)
        # Hard-link publication is atomic and fails rather than clobbering an
        # existing target. The temp file is on the same filesystem.
        os.link(temp, path)
    finally:
        if temp is not None:
            try:
                temp.unlink()
            except FileNotFoundError:
                pass


def atomic_write(path: Path, data: bytes) -> None:
    """Atomic replace, used only for unique content-addressed objects after verification."""
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile("wb", dir=path.parent, prefix="." + path.name + ".", delete=False) as handle:
        handle.write(data)
        handle.flush()
        os.fsync(handle.fileno())
        temp = Path(handle.name)
    temp.replace(path)


def write_run_file(repo_root: Path, rel_path: Path, data: bytes) -> Path:
    target = safe_output_path(repo_root, rel_path)
    if target.exists():
        if target.read_bytes() == data:
            return target
        raise FileExistsError(f"refusing to replace existing run artifact: {rel_path}")
    atomic_write(target, data)
    return target


def write_object(repo_root: Path, data: bytes, suffix: str) -> tuple[str, str]:
    digest = sha256_bytes(data)
    safe_suffix = suffix if re.fullmatch(r"\.[a-zA-Z0-9]{1,8}", suffix or "") else ".bin"
    rel = OUTPUT_ROOT / "objects" / digest[:2] / f"{digest}{safe_suffix.lower()}"
    target = safe_output_path(repo_root, rel)
    if target.exists():
        if sha256_file(target) != digest:
            raise RuntimeError(f"content-address collision or modified object: {rel}")
    else:
        try:
            atomic_create(target, data)
        except FileExistsError:
            if sha256_file(target) != digest:
                raise RuntimeError(f"concurrent content-address collision or modified object: {rel}")
    return rel.as_posix(), digest


def _first_value(value: Any) -> str:
    if isinstance(value, list):
        return normalize_space(value[0]) if value else ""
    return normalize_space(value)


def _ddb_clean_snippet(value: str) -> str:
    # DDB highlights are returned as plain text with {match} markers.
    return " ".join(normalize_space(value).split())


def search_ddb(
    client: HttpClient,
    query: str,
    limit: int,
    start_year: int | None,
    end_year: int | None,
    api_key: str,
    max_pages: int = 5,
) -> list[dict[str, Any]]:
    """Search DDB's newspaper Solr index for page-level OCR matches.

    The DDB API is officially documented and requires a user API key. The
    newspaper Solr collection/field layout is not fully specified in the
    public API docs; this adapter uses the currently observed collection
    endpoint and treats schema drift or non-JSON responses as hard errors.
    """
    if not api_key:
        raise RuntimeError("DDB requires an API key. Register at deutsche-digitale-bibliothek.de, create a key in My DDB, then set DDB_API_KEY in the environment.")
    endpoint = "https://api.deutsche-digitale-bibliothek.de/search/index/newspaper-issues/select"
    solr_query = f"type:page AND plainpagefulltext:({query.strip()})"
    rows: list[dict[str, Any]] = []
    total: int | None = None
    pages_fetched = 0
    page_size = 100
    headers = {"Authorization": f'OAuth oauth_consumer_key="{api_key}"'}
    for page in range(1, max(1, max_pages) + 1):
        if len(rows) >= limit or (total is not None and len(rows) >= total):
            break
        params: list[tuple[str, str]] = [
            ("q", solr_query),
            ("rows", str(min(page_size, max(1, limit - len(rows))))),
            ("start", str((page - 1) * page_size)),
            ("fl", "id,pagename,pagenumber,paper_title,publication_date,place_of_distribution,provider,zdb_id,language,preview_reference,score"),
            ("wt", "json"),
            ("hl", "true"),
            ("hl.fl", "plainpagefulltext"),
            ("hl.method", "original"),
            ("hl.snippets", "3"),
            ("hl.fragsize", "240"),
            ("hl.simple.pre", "{"),
            ("hl.simple.post", "}"),
        ]
        if start_year is not None or end_year is not None:
            low = f"{start_year:04d}-01-01T00:00:00Z" if start_year is not None else "*"
            high = f"{end_year:04d}-12-31T23:59:59Z" if end_year is not None else "*"
            params.append(("fq", f"publication_date:[{low} TO {high}]"))
        payload, final_url = client.get_json(endpoint, params, extra_headers=headers)
        block = payload.get("response") or {}
        if "numFound" not in block or not isinstance(block.get("docs"), list):
            raise RuntimeError(f"DDB Solr response schema changed or was incomplete: {sorted(payload.keys())}")
        total = int(block.get("numFound", 0))
        exact = block.get("numFoundExact")
        highlights = payload.get("highlighting") or {}
        docs = block.get("docs", [])
        if not docs:
            break
        pages_fetched += 1
        for rank_offset, item in enumerate(docs, start=1):
            rank = (page - 1) * page_size + rank_offset
            identifier = first_nonempty(item.get("id"))
            if not identifier:
                raise RuntimeError(f"DDB result at rank {rank} has no page id; refusing to silently drop it")
            pagename = first_nonempty(item.get("pagename"))
            item_id = identifier[:-len(pagename)-1] if pagename and identifier.endswith("-" + pagename) else identifier.split("-", 1)[0]
            date = _first_value(item.get("publication_date"))
            page_number = _first_value(item.get("pagenumber"))
            excerpt_list = (highlights.get(identifier) or {}).get("plainpagefulltext") or []
            snippets = [_ddb_clean_snippet(str(x)) for x in excerpt_list]
            viewer_url = f"https://www.deutsche-digitale-bibliothek.de/newspaper/item/{urllib.parse.quote(item_id)}?issuepage={urllib.parse.quote(page_number or '1')}"
            record = normalized_record(
                "ddb_newspaper_portal", query,
                title=_first_value(item.get("paper_title")), date=date,
                publication=_first_value(item.get("paper_title")),
                description="; ".join(snippets), snippet=" | ".join(snippets),
                language=item.get("language"), identifier=identifier,
                url=viewer_url, landing_page_url=viewer_url,
                places=item.get("place_of_distribution"), provider=item.get("provider"),
                zdb_id=item.get("zdb_id"), page_number=page_number,
                page_name=pagename, issue_item_id=item_id, total_results=total,
                relevance_score=item.get("score"), api_endpoint=final_url,
                preview_reference=item.get("preview_reference"),
                highlight_count=len(snippets), result_rank=rank,
                ddb_result_count_exact=exact,
                ddb_page=page, ddb_page_size=page_size,
                ddb_pages_requested=max(1, max_pages),
                raw_fields={k: item.get(k) for k in ("id", "publication_date", "paper_title", "place_of_distribution", "provider", "zdb_id", "language", "pagenumber", "pagename", "score")},
            )
            rows.append(record)
            if len(rows) >= limit:
                break
        if len(rows) >= limit or len(rows) >= total or len(docs) < page_size:
            break
    # Put coverage accounting on every record so later merged exports retain it.
    complete = total is not None and len(rows) >= total
    for record in rows:
        record.setdefault("raw", {}).update({
            "ddb_total_results": total,
            "ddb_num_found_exact": exact,
            "ddb_pages_fetched": pages_fetched,
            "ddb_page_sweep_complete": complete,
            "ddb_page_limit_reached": pages_fetched >= max(1, max_pages) and not complete and len(rows) < limit,
        })
    return rows


def _anno_document_record(record: dict[str, Any], query: str, total: int, rank: int) -> dict[str, Any]:
    document_id = record.get("docId")
    uid = record.get("uid")
    if not document_id or not isinstance(uid, dict):
        raise RuntimeError(f"ANNO result has an unexpected shape; refusing to discard it: {record!r}")
    owner = uid.get("owner")
    if owner == "ANNO":
        date_info = uid.get("annoDate") or {}
        date = normalize_space(date_info.get("date"))
        if not date:
            raise RuntimeError(f"ANNO newspaper record {document_id} lacks its date: {record!r}")
        year = parse_year(date)
    elif owner == "ANNOP":
        year = parse_year(uid.get("year"))
        date = str(year) if year else ""
        if not year:
            raise RuntimeError(f"ANNO periodical record {document_id} lacks its year: {record!r}")
    else:
        raise RuntimeError(f"ANNO record {document_id} has unknown owner {owner!r}; refusing to guess its schema")
    return normalized_record(
        "anno_unofficial_search", query,
        title=record.get("displayTitle") or "Untitled", date=date, year=year,
        identifier=document_id, url=record.get("openUrl"), landing_page_url=record.get("openUrl"),
        language=record.get("languages") or [], places=record.get("places") or [],
        publication=record.get("displayTitle"), owner=owner, issue_type=record.get("type"),
        is_periodical=owner == "ANNOP", page_count=record.get("pageCount"),
        hits_in_issue=record.get("totalHitsInDoc"), total_results=total,
        result_rank=rank, uid=uid,
    )


def search_anno(
    client: HttpClient,
    query: str,
    limit: int,
    start_year: int | None,
    end_year: int | None,
    allow_undocumented: bool,
    medium: str = "all",
    snippets: int = 0,
    max_pages: int = 10,
) -> list[dict[str, Any]]:
    """Search ANNO's currently observed, undocumented AnnoSearch backend.

    This provider is intentionally opt-in. It is not an official published API;
    the adapter validates the expected JSON envelope and fails loudly on drift.
    """
    if not allow_undocumented:
        raise RuntimeError("ANNO search uses an undocumented backend and is disabled by default; pass --allow-undocumented-anno-api to opt in")
    base = "https://anno.onb.ac.at/anno-suche/rest"
    rows: list[dict[str, Any]] = []
    page = 1
    pages_fetched = 0
    total = None
    while len(rows) < limit and page <= max(1, max_pages):
        params: list[tuple[str, str]] = [("text", query.strip()), ("from", str((page - 1) * 10)), ("facets", "true")]
        if start_year is not None:
            params.append(("dateFrom", str(start_year)))
        if end_year is not None:
            params.append(("dateTo", str(end_year)))
        if medium == "newspaper":
            params.append(("selectedFilters", "type:journal"))
        elif medium == "periodical":
            params.append(("selectedFilters", "type:periodical"))
        elif medium != "all":
            raise ValueError("ANNO medium must be all, newspaper, or periodical")
        payload, _url = client.get_json(base + "/search/complex", params)
        if "totalHits" not in payload or not isinstance(payload.get("documents"), list):
            raise RuntimeError(f"ANNO search schema changed or returned an incomplete response: {sorted(payload.keys())}")
        total = int(payload.get("totalHits", 0))
        pages_fetched += 1
        documents = payload.get("documents") or []
        if not documents:
            break
        for index, document in enumerate(documents, start=1):
            rank = (page - 1) * 10 + index
            item = _anno_document_record(document, query, total, rank)
            rows.append(item)
            if snippets > 0 and len(rows) <= snippets:
                doc_id = item.get("identifier", "")
                try:
                    snippet_payload, _ = client.get_json(base + "/search/snippet", [("documentId", doc_id), ("query", query.strip())])
                    snippet_rows = []
                    for page_entry in snippet_payload.get("snippetPages") or []:
                        for snip in page_entry.get("snippets") or []:
                            raw_text = str(snip.get("text") or "")
                            raw_text = re.sub(r"<span[^>]*class=['\"]?snp_txt_hl['\"]?[^>]*>(.*?)</span>", r"{\1}", raw_text, flags=re.I | re.S)
                            raw_text = re.sub(r"(?i)<\s*br\s*/?>", " ", raw_text)
                            raw_text = re.sub(r"<[^>]+>", "", raw_text)
                            snippet_rows.append({
                                "page": snip.get("page", page_entry.get("page")),
                                "page_label": snip.get("pageLabel", page_entry.get("pageLabel")),
                                "text": " ".join(html.unescape(raw_text).replace("­", "").split()),
                                "url": snip.get("openURL") or page_entry.get("openURL"),
                                "image_url": snip.get("imageURL"),
                            })
                    item["snippet"] = " | ".join(x["text"] for x in snippet_rows)
                    item["raw"]["page_snippets"] = snippet_rows
                except Exception as exc:
                    item["raw"]["snippet_error"] = f"{type(exc).__name__}: {exc}"
            if len(rows) >= limit:
                break
        if len(rows) >= limit or len(rows) >= total:
            break
        page += 1
    for row in rows:
        row.setdefault("raw", {})["total_results_for_query"] = total
        row["raw"]["pagination_complete_to_requested_limit"] = len(rows) >= min(limit, total or limit)
        row["raw"]["anno_pages_fetched"] = pages_fetched
        row["raw"]["anno_page_limit_reached"] = pages_fetched >= max(1, max_pages) and len(rows) < min(limit, total or limit)
    return rows


def search_loc(client: HttpClient, query: str, limit: int, start_year: int | None, end_year: int | None) -> list[dict[str, Any]]:
    endpoint = "https://www.loc.gov/collections/chronicling-america/"
    params: dict[str, Any] = {"qs": query, "ops": "OR", "fo": "json", "dl": "page", "c": min(max(limit, 1), 100)}
    if start_year:
        params["start_date"] = f"{start_year}-01-01"
    if end_year:
        params["end_date"] = f"{end_year}-12-31"
    payload, _url = client.get_json(endpoint, params)
    results = payload.get("results", []) or []
    rows = []
    for item in results[:limit]:
        full_text = item.get("full_text") or item.get("ocr_text") or ""
        rows.append(normalized_record(
            "loc_chronicling_america", query,
            title=item.get("title"), date=item.get("date"), publication=item.get("partof"),
            description=item.get("description"), snippet=full_text[:1800], language=item.get("language"),
            identifier=item.get("id") or item.get("url"), url=item.get("url"),
            landing_page_url=item.get("url"), pdf_url="", rights=item.get("rights"),
            api_record=item, full_text_available=bool(full_text),
        ))
        if full_text:
            rows[-1]["_full_text"] = full_text
    return rows


def search_internet_archive(client: HttpClient, query: str, limit: int) -> list[dict[str, Any]]:
    endpoint = "https://archive.org/advancedsearch.php"
    params = {
        "q": query,
        "fl[]": ["identifier", "title", "creator", "date", "year", "description", "language", "licenseurl", "rights", "mediatype"],
        "rows": min(max(limit, 1), 100),
        "page": 1,
        "output": "json",
    }
    payload, _url = client.get_json(endpoint, params)
    docs = payload.get("response", {}).get("docs", []) or []
    rows = []
    for item in docs[:limit]:
        identifier = normalize_space(item.get("identifier"))
        license_value = item.get("licenseurl") or item.get("rights") or ""
        rows.append(normalized_record(
            "internet_archive", query, title=item.get("title"), authors=item.get("creator", []),
            date=item.get("date") or item.get("year"), year=item.get("year"),
            description=item.get("description"), language=item.get("language"), identifier=identifier,
            url=f"https://archive.org/details/{identifier}" if identifier else "",
            landing_page_url=f"https://archive.org/details/{identifier}" if identifier else "",
            license=license_value, rights=item.get("rights"), mediatype=item.get("mediatype"),
        ))
    return rows


def enrich_internet_archive(client: HttpClient, record: dict[str, Any]) -> dict[str, Any]:
    identifier = record.get("identifier")
    if not identifier:
        return record
    metadata, _url = client.get_json(f"https://archive.org/metadata/{urllib.parse.quote(identifier, safe='')}")
    meta = metadata.get("metadata", {})
    record["license"] = first_nonempty(record.get("license"), meta.get("licenseurl"), meta.get("rights"))
    record["rights"] = first_nonempty(record.get("rights"), meta.get("rights"))
    record["raw"]["ia_metadata"] = {
        "metadata": meta,
        "files": [
            {k: f.get(k) for k in ("name", "format", "size", "source", "private", "summation") if k in f}
            for f in metadata.get("files", [])
            if str(f.get("name", "")).lower().endswith(".pdf")
        ],
    }
    candidates = []
    for file_info in metadata.get("files", []) or []:
        name = str(file_info.get("name", ""))
        fmt = str(file_info.get("format", "")).lower()
        if name.lower().endswith(".pdf") and ("pdf" in fmt or fmt == "text pdf"):
            size = int(file_info.get("size", 0) or 0)
            candidates.append((0 if fmt == "text pdf" else 1, size, name))
    if candidates:
        candidates.sort()
        record["pdf_url"] = f"https://archive.org/download/{urllib.parse.quote(identifier, safe='')}/{urllib.parse.quote(candidates[0][2], safe='')}"
        record["raw"]["candidate_pdf_name"] = candidates[0][2]
        record["raw"]["candidate_pdf_bytes"] = candidates[0][1]
    return record


def search_crossref(client: HttpClient, query: str, limit: int, start_year: int | None, end_year: int | None) -> list[dict[str, Any]]:
    params: dict[str, Any] = {"query.bibliographic": query, "rows": min(max(limit, 1), 100), "select": "DOI,title,author,published,created,publisher,container-title,volume,issue,page,URL,link,license,abstract,subject,type"}
    if start_year:
        params["filter"] = f"from-pub-date:{start_year}-01-01"
    if end_year:
        extra = f"until-pub-date:{end_year}-12-31"
        params["filter"] = (params.get("filter", "") + "," + extra).strip(",")
    payload, _url = client.get_json("https://api.crossref.org/works", params)
    rows = []
    for item in payload.get("message", {}).get("items", [])[:limit]:
        title = (item.get("title") or [""])[0]
        published = item.get("published-print") or item.get("published-online") or item.get("created") or {}
        date_parts = published.get("date-parts", [[]])
        date = "-".join(str(x) for x in date_parts[0]) if date_parts and date_parts[0] else ""
        authors = [first_nonempty(a.get("given"), "") + (" " if a.get("given") else "") + first_nonempty(a.get("family")) for a in item.get("author", [])]
        links = item.get("link", []) or []
        pdf_url = next((l.get("URL", "") for l in links if "pdf" in str(l.get("content-type", "")).lower()), "")
        license_value = "; ".join(x.get("URL", "") for x in item.get("license", []) if x.get("URL"))
        rows.append(normalized_record(
            "crossref", query, title=title, authors=authors, date=date,
            publication=(item.get("container-title") or [""])[0], description=item.get("abstract"),
            identifier=item.get("DOI"), doi=item.get("DOI"), url=item.get("URL"),
            landing_page_url=item.get("URL"), pdf_url=pdf_url, license=license_value,
            publisher=item.get("publisher"), volume=item.get("volume"), issue=item.get("issue"),
            page=item.get("page"), subjects=item.get("subject", []), work_type=item.get("type"),
        ))
    return rows


def reconstruct_openalex_abstract(index: Any) -> str:
    if not isinstance(index, dict):
        return normalize_space(index)
    positioned: list[tuple[int, str]] = []
    for word, offsets in index.items():
        if isinstance(offsets, list):
            for offset in offsets:
                try:
                    positioned.append((int(offset), str(word)))
                except (TypeError, ValueError):
                    continue
    positioned.sort()
    return " ".join(word for _position, word in positioned)


def search_openalex(client: HttpClient, query: str, limit: int, start_year: int | None, end_year: int | None, mailto: str = "") -> list[dict[str, Any]]:
    params: dict[str, Any] = {"search": query, "per-page": min(max(limit, 1), 100)}
    if start_year:
        params["from_publication_date"] = f"{start_year}-01-01"
    if end_year:
        params["to_publication_date"] = f"{end_year}-12-31"
    if mailto:
        params["mailto"] = mailto
    payload, _url = client.get_json("https://api.openalex.org/works", params)
    rows = []
    for item in payload.get("results", [])[:limit]:
        authors = []
        for authorship in item.get("authorships", []) or []:
            author = (authorship.get("author") or {}).get("display_name")
            if author:
                authors.append(author)
        best = item.get("best_oa_location") or {}
        primary = item.get("primary_location") or {}
        source = (primary.get("source") or {}).get("display_name")
        oa = item.get("open_access") or {}
        rows.append(normalized_record(
            "openalex", query, title=item.get("title"), authors=authors,
            date=str(item.get("publication_date") or item.get("publication_year") or ""),
            publication=source, description=reconstruct_openalex_abstract(item.get("abstract_inverted_index")),
            identifier=item.get("id"), doi=item.get("doi"),
            url=item.get("doi") or item.get("id"), landing_page_url=item.get("id"),
            pdf_url=(best.get("pdf_url") or (best.get("landing_page_url") if str(best.get("landing_page_url", "")).lower().endswith(".pdf") else "")),
            license=best.get("license") or "", rights="open" if oa.get("is_oa") else "",
            is_oa=oa.get("is_oa"), oa_status=oa.get("oa_status"),
            cited_by_count=item.get("cited_by_count"), publication_year=item.get("publication_year"),
            type=item.get("type"), best_oa_location=best,
        ))
    return rows


def oai_local_name(tag: str) -> str:
    return tag.rsplit("}", 1)[-1]


def search_oai_pmh(client: HttpClient, endpoint: str, query: str, limit: int, metadata_prefix: str = "oai_dc", set_spec: str = "", from_date: str = "", until_date: str = "", max_batches: int = 5) -> list[dict[str, Any]]:
    params: dict[str, str] = {"verb": "ListRecords", "metadataPrefix": metadata_prefix}
    if set_spec:
        params["set"] = set_spec
    if from_date:
        params["from"] = from_date
    if until_date:
        params["until"] = until_date
    rows: list[dict[str, Any]] = []
    next_params = params
    batches = 0
    while len(rows) < limit and batches < max(1, max_batches):
        body, _headers, _final_url = client.get(endpoint, next_params, "application/xml,text/xml")
        batches += 1
        root = ET.fromstring(body)
        error = next((node for node in root.iter() if oai_local_name(node.tag) == "error"), None)
        if error is not None:
            raise RuntimeError("OAI-PMH error: " + normalize_space(error.text))
        for node in root.iter():
            if oai_local_name(node.tag) != "record":
                continue
            metadata = next((child for child in node if oai_local_name(child.tag) == "metadata"), None)
            if metadata is None:
                continue
            fields: dict[str, list[str]] = {}
            for child in metadata.iter():
                key = oai_local_name(child.tag)
                value = normalize_space(child.text)
                if value:
                    fields.setdefault(key, []).append(value)
            joined = " ".join(v for values in fields.values() for v in values).lower()
            terms = [t.lower() for t in re.findall(r"[\wÀ-ž-]+", query) if len(t) > 2]
            if terms and not any(t in joined for t in terms):
                continue
            header = next((child for child in node if oai_local_name(child.tag) == "header"), None)
            oai_id = ""
            if header is not None:
                id_node = next((child for child in header if oai_local_name(child.tag) == "identifier"), None)
                oai_id = normalize_space(id_node.text if id_node is not None else "")
            rows.append(normalized_record(
                "oai_pmh", query, title=fields.get("title", [""]), authors=fields.get("creator", []),
                date=fields.get("date", [""]), publication=fields.get("source", [""]),
                description=fields.get("description", []), language=fields.get("language", [""]),
                identifier=oai_id, url=fields.get("identifier", [""])[0] if fields.get("identifier") else oai_id,
                landing_page_url=fields.get("identifier", [""])[0] if fields.get("identifier") else "",
                subject=fields.get("subject", []), metadata_fields=fields,
            ))
            if len(rows) >= limit:
                break
        token_node = next((node for node in root.iter() if oai_local_name(node.tag) == "resumptionToken"), None)
        token = normalize_space(token_node.text if token_node is not None else "")
        if not token:
            break
        next_params = {"verb": "ListRecords", "resumptionToken": token}
    if len(rows) < limit and batches >= max(1, max_batches) and token:
        # Mark the ceiling so downstream users do not mistake the bounded sweep
        # for an exhaustive harvest.
        for row in rows:
            row.setdefault("raw", {})["oai_batch_limit_reached"] = True
    return rows


class SavedHtmlParser(HTMLParser):
    """Small dependency-free parser for locally saved, already-rendered result pages."""
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.title_parts: list[str] = []
        self.in_title = False
        self.anchor: dict[str, Any] | None = None
        self.links: list[dict[str, str]] = []
        self.base_url = ""

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attrs_map = dict(attrs)
        if tag.lower() == "title":
            self.in_title = True
        if tag.lower() == "base" and attrs_map.get("href"):
            self.base_url = attrs_map["href"] or ""
        if tag.lower() == "link" and attrs_map.get("rel", "").lower() == "canonical" and attrs_map.get("href"):
            self.base_url = attrs_map["href"] or ""
        if tag.lower() == "meta" and attrs_map.get("property", "").lower() == "og:url" and attrs_map.get("content"):
            self.base_url = attrs_map["content"] or ""
        if tag.lower() == "a" and attrs_map.get("href"):
            self.anchor = {"href": attrs_map["href"] or "", "text": ""}

    def handle_data(self, data: str) -> None:
        text = normalize_space(data)
        if not text:
            return
        if self.in_title:
            self.title_parts.append(text)
        if self.anchor is not None:
            self.anchor["text"] = normalize_space(self.anchor["text"] + " " + text)

    def handle_endtag(self, tag: str) -> None:
        if tag.lower() == "title":
            self.in_title = False
        if tag.lower() == "a" and self.anchor is not None:
            self.links.append(self.anchor)
            self.anchor = None


def import_saved_html(path: Path, query: str = "manual portal import") -> list[dict[str, Any]]:
    parser = SavedHtmlParser()
    parser.feed(path.read_text(encoding="utf-8", errors="replace"))
    rows = []
    base = urllib.parse.urljoin(path.resolve().as_uri(), parser.base_url) if parser.base_url else ""
    for link in parser.links:
        raw_href = link["href"]
        if not link["text"]:
            continue
        if urllib.parse.urlparse(raw_href).scheme in {"http", "https"}:
            href = raw_href
        elif base:
            href = urllib.parse.urljoin(base, raw_href)
        else:
            continue
        rows.append(normalized_record(
            "saved_html_portal", query, title=link["text"], url=href,
            landing_page_url=href, local_import_path=str(path),
            page_title=" ".join(parser.title_parts),
        ))
    if not rows:
        rows.append(normalized_record(
            "saved_html_portal", query, title="Saved portal page (no result links parsed)",
            url="", local_import_path=str(path), page_title=" ".join(parser.title_parts),
            warning="The saved page may be JavaScript-rendered; retain it as a source capture and inspect manually.",
        ))
    return rows


def import_local_file(path: Path, source_url: str = "") -> dict[str, Any]:
    path = path.resolve()
    if not path.is_file():
        raise FileNotFoundError(path)
    suffix = path.suffix.lower()
    mime = {
        ".pdf": "application/pdf", ".txt": "text/plain", ".html": "text/html",
        ".htm": "text/html", ".xml": "application/xml", ".json": "application/json",
    }.get(suffix, "application/octet-stream")
    extra: dict[str, Any] = {"local_path": str(path), "local_bytes": path.stat().st_size, "sha256": sha256_file(path), "mime_type": mime}
    if suffix == ".pdf":
        try:
            from pypdf import PdfReader  # type: ignore
            reader = PdfReader(str(path))
            extra["page_count"] = len(reader.pages)
            metadata = reader.metadata or {}
            extra["pdf_title"] = normalize_space(metadata.get("/Title"))
            extra["pdf_author"] = normalize_space(metadata.get("/Author"))
        except Exception as exc:
            extra["pdf_metadata_status"] = f"unavailable: {type(exc).__name__}: {exc}"
    return normalized_record(
        "local_user_supplied_file", "manual import",
        title=extra.get("pdf_title") or path.stem, authors=[extra.get("pdf_author", "")] if extra.get("pdf_author") else [],
        date="", identifier=extra["sha256"], url=source_url or path.as_uri(), landing_page_url=source_url or path.as_uri(),
        rights="User-supplied local file; copyright status not assessed", local_file=extra, source_url=source_url,
    )


def download_if_eligible(client: HttpClient, repo_root: Path, record: dict[str, Any], max_bytes: int) -> None:
    url = normalize_space(record.get("pdf_url"))
    if not url:
        record["download_status"] = "no_pdf_link"
        return
    source = record.get("source")
    if source == "openalex" and not record.get("raw", {}).get("is_oa"):
        record["download_status"] = "skipped_not_open_access"
        return
    if not allowed_open_license(record.get("license"), record.get("rights")):
        record["download_status"] = "skipped_no_explicit_open_license"
        return
    try:
        body, headers, final_url = client.get(url, accept="application/pdf,application/octet-stream,*/*", max_bytes=max_bytes)
        content_type = headers.get("content-type", "").lower()
        if "html" in content_type or body[:20].lstrip().lower().startswith((b"<!doctype html", b"<html")):
            record["download_status"] = "skipped_html_response"
            return
        suffix = Path(urllib.parse.urlparse(final_url).path).suffix.lower() or ".pdf"
        if suffix not in {".pdf", ".txt", ".xml", ".djvu", ".epub"}:
            suffix = ".pdf" if "pdf" in content_type else ".bin"
        rel, digest = write_object(repo_root, body, suffix)
        record["download_status"] = "downloaded_open_license"
        record["download_path"] = rel
        record["raw"]["download_sha256"] = digest
        record["raw"]["download_bytes"] = len(body)
        record["raw"]["download_final_url"] = final_url
        record["raw"]["download_content_type"] = content_type
    except Exception as exc:
        message = str(exc)
        record["download_status"] = "skipped_size_limit" if "exceeds configured size limit" in message else "error"
        record["raw"]["download_error"] = f"{type(exc).__name__}: {exc}"


def load_config(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def select_queries(config: dict[str, Any], group: str) -> list[str]:
    groups = config.get("query_groups", {})
    if group == "all":
        output: list[str] = []
        for rows in groups.values():
            output.extend(str(item["query"] if isinstance(item, dict) else item) for item in rows)
        return list(dict.fromkeys(output))
    if group not in groups:
        raise ValueError(f"unknown query group {group!r}; choose one of: {', '.join(groups)}")
    return [str(item["query"] if isinstance(item, dict) else item) for item in groups[group]]


def execute_searches(client: HttpClient, providers: list[str], queries: list[str], limit: int, start_year: int | None, end_year: int | None, mailto: str, oai_endpoint: str = "", oai_max_batches: int = 5, ddb_api_key: str = "", allow_undocumented_anno: bool = False, anno_medium: str = "all", anno_snippets: int = 0, ddb_max_pages: int = 5, anno_max_pages: int = 10) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    records: list[dict[str, Any]] = []
    errors: list[dict[str, Any]] = []
    for provider in providers:
        for query in queries:
            try:
                if provider == "loc":
                    found = search_loc(client, query, limit, start_year, end_year)
                elif provider == "ia":
                    found = search_internet_archive(client, query, limit)
                    for record in found:
                        try:
                            enrich_internet_archive(client, record)
                        except Exception as exc:
                            record["raw"]["ia_metadata_error"] = f"{type(exc).__name__}: {exc}"
                elif provider == "crossref":
                    found = search_crossref(client, query, limit, start_year, end_year)
                elif provider == "openalex":
                    found = search_openalex(client, query, limit, start_year, end_year, mailto)
                elif provider == "ddb":
                    found = search_ddb(client, query, limit, start_year, end_year, ddb_api_key, ddb_max_pages)
                elif provider == "anno":
                    found = search_anno(client, query, limit, start_year, end_year, allow_undocumented_anno, anno_medium, anno_snippets, anno_max_pages)
                elif provider == "oai":
                    if not oai_endpoint:
                        raise ValueError("OAI-PMH provider requires --oai-endpoint")
                    found = search_oai_pmh(client, oai_endpoint, query, limit, max_batches=oai_max_batches)
                else:
                    raise ValueError(f"unsupported provider: {provider}")
                records.extend(found)
            except Exception as exc:
                errors.append({"provider": provider, "query": query, "error": f"{type(exc).__name__}: {exc}"})
    return records, errors


def current_git_state(repo_root: Path) -> dict[str, str]:
    state = {"commit": "unavailable", "branch": "unavailable"}
    try:
        commit = subprocess.run(["git", "-C", str(repo_root), "rev-parse", "HEAD"], check=True, capture_output=True, text=True)
        branch = subprocess.run(["git", "-C", str(repo_root), "branch", "--show-current"], check=True, capture_output=True, text=True)
        state["commit"] = commit.stdout.strip()
        state["branch"] = branch.stdout.strip()
    except (OSError, subprocess.CalledProcessError):
        pass
    return state


def save_run(repo_root: Path, run_id: str, records: list[dict[str, Any]], run_manifest: dict[str, Any], raw_responses: bool = False) -> tuple[Path, Path]:
    run_dir = OUTPUT_ROOT / "runs" / run_id
    serializable = []
    for record in records:
        row = {k: v for k, v in record.items() if not k.startswith("_")}
        serializable.append(row)
    jsonl = "".join(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n" for row in serializable).encode("utf-8")
    records_path = write_run_file(repo_root, run_dir / "records.jsonl", jsonl)
    manifest_path = write_run_file(repo_root, run_dir / "run.json", (json.dumps(run_manifest, indent=2, ensure_ascii=False, sort_keys=True) + "\n").encode("utf-8"))
    return records_path, manifest_path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--repo-root", type=Path, default=Path("."), help="local checkout of Satobloc/HSH_RESOURCES")
    parser.add_argument("--config", type=Path, default=DEFAULT_CONFIG)
    parser.add_argument("--providers", default="loc,ia,crossref,openalex", help="comma-separated: loc,ia,crossref,openalex,ddb,anno,oai")
    parser.add_argument("--query-group", default="core", help="core, people, stigma, all, or a group in queries.json")
    parser.add_argument("--query", action="append", default=[], help="additional search query; may be repeated")
    parser.add_argument("--limit", type=int, default=15, help="maximum results per provider/query")
    parser.add_argument("--start-year", type=int, default=1870)
    parser.add_argument("--end-year", type=int, default=1945)
    parser.add_argument("--delay", type=float, default=1.25, help="minimum seconds between requests to each host")
    parser.add_argument("--timeout", type=int, default=30)
    parser.add_argument("--max-download-mb", type=float, default=30.0)
    parser.add_argument("--download", action="store_true", help="download explicitly open-licensed PDFs only")
    parser.add_argument("--import-file", type=Path, action="append", default=[], help="record a local seed file; may be repeated")
    parser.add_argument("--import-file-url", action="append", default=[], help="canonical/public source URL for the corresponding --import-file; repeat in the same order")
    parser.add_argument("--import-html", type=Path, action="append", default=[], help="parse locally saved portal results HTML; may be repeated")
    parser.add_argument("--oai-endpoint", default="", help="optional OAI-PMH endpoint when using provider=oai")
    parser.add_argument("--oai-max-batches", type=int, default=5, help="maximum ListRecords batches per OAI query (bounded sweep)")
    parser.add_argument("--allow-undocumented-anno-api", action="store_true", help="opt in to ANNO AnnoSearch backend; undocumented and may drift")
    parser.add_argument("--anno-medium", choices=("all", "newspaper", "periodical"), default="all")
    parser.add_argument("--anno-snippets", type=int, default=0, help="fetch ANNO page snippets for first N issue hits per query (extra requests)")
    parser.add_argument("--ddb-api-key", default=os.environ.get("DDB_API_KEY", ""), help="DDB API key; prefer DDB_API_KEY environment variable")
    parser.add_argument("--ddb-max-pages", type=int, default=5, help="maximum 100-result Solr pages per DDB query; default 5")
    parser.add_argument("--anno-max-pages", type=int, default=10, help="maximum 10-result ANNO pages per query; default 10")
    parser.add_argument("--mailto", default=os.environ.get("OPENALEX_MAILTO", ""), help="polite-pool contact for OpenAlex; optional")
    parser.add_argument("--user-agent", default=os.environ.get("ARCHIVE_HARVESTER_UA", USER_AGENT))
    parser.add_argument("--apply", action="store_true", help="write run manifest/records; default is dry-run")
    args = parser.parse_args()

    repo_root = args.repo_root.resolve()
    if not repo_root.is_dir():
        parser.error(f"repo root does not exist: {repo_root}")
    config = load_config(args.config)
    queries = select_queries(config, args.query_group) + args.query
    queries = list(dict.fromkeys(q.strip() for q in queries if q.strip()))
    providers = [item.strip().lower() for item in args.providers.split(",") if item.strip()]
    client = HttpClient(delay=args.delay, timeout=args.timeout, user_agent=args.user_agent)
    run_id = make_run_id()
    started = utc_now()

    if args.import_file_url and len(args.import_file_url) != len(args.import_file):
        parser.error("--import-file-url must be supplied once for each --import-file, in the same order")
    records, errors = execute_searches(
        client, providers, queries, min(50000, max(1, args.limit)), args.start_year, args.end_year,
        args.mailto, args.oai_endpoint, max(1, args.oai_max_batches), args.ddb_api_key,
        args.allow_undocumented_anno_api, args.anno_medium, max(0, args.anno_snippets),
        max(1, args.ddb_max_pages), max(1, args.anno_max_pages),
    )
    urls = args.import_file_url or [""] * len(args.import_file)
    for path, source_url in zip(args.import_file, urls):
        records.append(import_local_file(path, source_url))
    for path in args.import_html:
        records.extend(import_saved_html(path))

    if args.download:
        max_bytes = int(max(0.1, args.max_download_mb) * 1024 * 1024)
        if args.apply:
            for record in records:
                if record.get("pdf_url"):
                    download_if_eligible(client, repo_root, record, max_bytes)
        else:
            for record in records:
                if record.get("pdf_url"):
                    record["download_status"] = "would_download_if_apply_and_license_allows"

    run_manifest = {
        "schema_version": 1,
        "tool_version": VERSION,
        "run_id": run_id,
        "started_at": started,
        "finished_at": utc_now(),
        "repository": "Satobloc/HSH_RESOURCES",
        "source_revision": current_git_state(repo_root),
        "read_scope": ["tool config", "public API endpoints", "explicit --import-file/--import-html paths"],
        "write_scope": [OUTPUT_ROOT.as_posix()] if args.apply else [],
        "write_mode": "append-only run directory plus content-addressed objects" if args.apply else "dry-run",
        "providers": providers,
        "queries": queries,
        "date_window": {"start_year": args.start_year, "end_year": args.end_year},
        "rate_limit_seconds_per_host": args.delay,
        "download_opt_in": bool(args.download),
        "ddb_max_pages_per_query": max(1, args.ddb_max_pages),
        "anno_max_pages_per_query": max(1, args.anno_max_pages),
        "anno_undocumented_backend_opt_in": bool(args.allow_undocumented_anno_api),
        "max_download_bytes": int(max(0.1, args.max_download_mb) * 1024 * 1024),
        "records_found": len(records),
        "errors": errors,
        "limitations": [
            "Discovery metadata is not evidence that a source supports a historical claim.",
            "Search results are not exhaustive; OCR, cataloguing, API coverage, and date filters vary by provider.",
            "DDB newspaper portal and ANNO browser-only searches are represented as manual discovery/import routes; no undocumented endpoint is scraped.",
            "Crossref/OpenAlex provide metadata and links; full text is not presumed available.",
            "DDB search uses the documented DDB API host and its currently observed newspaper Solr collection; an API key is required.",
            "ANNO search is an opt-in adapter for an undocumented AnnoSearch backend; endpoint shape is validated but stability is not guaranteed.",
            "OAI-PMH harvesting is capped by --oai-max-batches and must not be represented as exhaustive unless the token stream is exhausted.",
            "Only explicit open-license signals are eligible for automatic PDF download.",
        ],
    }

    print(f"run_id={run_id} records={len(records)} providers={','.join(providers)} queries={len(queries)} errors={len(errors)}")
    for error in errors:
        print(f"ERROR\t{error['provider']}\t{error['query']}\t{error['error']}")
    for record in records[:40]:
        print("RESULT\t" + normalize_space(record.get("source")) + "\t" + normalize_space(record.get("date")) + "\t" + normalize_space(record.get("title"))[:180])
    if len(records) > 40:
        print(f"... {len(records)-40} additional records omitted from console preview")
    if not args.apply:
        print("dry-run: no repository files written; pass --apply to save records")
        return 0 if not errors else 1

    records_path, manifest_path = save_run(repo_root, run_id, records, run_manifest)
    print(f"records={records_path.relative_to(repo_root)}")
    print(f"run_manifest={manifest_path.relative_to(repo_root)}")
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
