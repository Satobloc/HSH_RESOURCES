from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TOOL_DIR = ROOT / "tools" / "fourth_dimension_history_harvester"
sys.path.insert(0, str(TOOL_DIR))

import harvest  # noqa: E402


class FakeClient:
    def __init__(self, responses):
        self.responses = list(responses)
        self.calls = []

    def get_json(self, url, params=None, extra_headers=None):
        self.calls.append((url, params, extra_headers))
        if not self.responses:
            raise AssertionError(f"unexpected extra request: {url}")
        return self.responses.pop(0), url

    def get(self, url, params=None, accept="*/*", max_bytes=None, extra_headers=None):
        raise AssertionError("unexpected binary request")


class HarvesterTests(unittest.TestCase):
    def test_normalized_record_extracts_year_from_date(self):
        row = harvest.normalized_record("test", "query", title="A title", date="1924-11-21")
        self.assertEqual(row["year"], 1924)
        self.assertEqual(row["title"], "A title")
        self.assertEqual(len(row["record_id"]), 24)

    def test_record_key_normalizes_doi_url(self):
        one = {"doi": "https://doi.org/10.1000/ABC"}
        two = {"doi": "10.1000/abc"}
        self.assertEqual(harvest.record_key(one), harvest.record_key(two))

    def test_license_requires_explicit_marker(self):
        self.assertTrue(harvest.allowed_open_license("https://creativecommons.org/licenses/by/4.0/"))
        self.assertTrue(harvest.allowed_open_license("Public Domain Mark 1.0"))
        self.assertFalse(harvest.allowed_open_license("Open access"))
        self.assertFalse(harvest.allowed_open_license("All rights reserved"))

    def test_openalex_abstract_reconstruction(self):
        inverted = {"fourth": [0], "dimension": [1], "physics": [2], "space": [3]}
        self.assertEqual(harvest.reconstruct_openalex_abstract(inverted), "fourth dimension physics space")

    def test_safe_output_path_allows_only_harvested_root(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            allowed = harvest.safe_output_path(root, harvest.OUTPUT_ROOT / "runs" / "r1" / "run.json")
            self.assertTrue(str(allowed).endswith("run.json"))
            with self.assertRaises(ValueError):
                harvest.safe_output_path(root, Path("HISTORICAL/OTHER/file.txt"))
            with self.assertRaises(ValueError):
                harvest.safe_output_path(root, Path("PRIOR_ART/file.txt"))
            with self.assertRaises(ValueError):
                harvest.safe_output_path(root, Path("/tmp/outside.txt"))

    def test_safe_output_path_rejects_symlink_escape(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td) / "repo"
            outside = Path(td) / "outside"
            root.mkdir()
            outside.mkdir()
            declared = root / harvest.OUTPUT_ROOT
            declared.parent.mkdir(parents=True, exist_ok=True)
            declared.symlink_to(outside, target_is_directory=True)
            with self.assertRaises(ValueError):
                harvest.safe_output_path(root, harvest.OUTPUT_ROOT / "escape.txt")

    def test_run_file_never_overwrites(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            rel = harvest.OUTPUT_ROOT / "runs" / "r1" / "run.json"
            target = harvest.write_run_file(root, rel, b'{"a":1}\n')
            self.assertEqual(target.read_bytes(), b'{"a":1}\n')
            self.assertEqual(harvest.write_run_file(root, rel, b'{"a":1}\n'), target)
            with self.assertRaises(FileExistsError):
                harvest.write_run_file(root, rel, b'{"a":2}\n')

    def test_content_addressed_object(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            rel, digest = harvest.write_object(root, b"abc", ".pdf")
            self.assertEqual(digest, harvest.sha256_bytes(b"abc"))
            self.assertEqual((root / rel).read_bytes(), b"abc")
            rel2, digest2 = harvest.write_object(root, b"abc", ".pdf")
            self.assertEqual((rel, digest), (rel2, digest2))

    def test_saved_html_uses_canonical_base_for_relative_links(self):
        with tempfile.TemporaryDirectory() as td:
            path = Path(td) / "capture.html"
            path.write_text(
                '<html><head><title>Results</title><link rel="canonical" href="https://archive.example/search?q=x"></head>'
                '<body><a href="/item/123">A newspaper page</a></body></html>',
                encoding="utf-8",
            )
            rows = harvest.import_saved_html(path)
            self.assertEqual(len(rows), 1)
            self.assertEqual(rows[0]["title"], "A newspaper page")
            self.assertEqual(rows[0]["url"], "https://archive.example/item/123")

    def test_import_local_file_keeps_hash_and_public_source_url(self):
        with tempfile.TemporaryDirectory() as td:
            path = Path(td) / "seed.txt"
            path.write_text("source text", encoding="utf-8")
            before = harvest.sha256_file(path)
            row = harvest.import_local_file(path, "https://archive.example/original")
            self.assertEqual(row["identifier"], before)
            self.assertEqual(row["url"], "https://archive.example/original")
            self.assertEqual(harvest.sha256_file(path), before)

    def test_ddb_search_captures_page_metadata_and_snippets(self):
        payload = {
            "response": {
                "numFound": 1,
                "numFoundExact": True,
                "docs": [{
                    "id": "ISSUE-001-PAGE-3", "pagename": "PAGE-3", "pagenumber": 3,
                    "paper_title": "Leipziger Zeitung", "publication_date": "1888-03-18T00:00:00Z",
                    "place_of_distribution": "Leipzig", "provider": "Example Library", "zdb_id": "123",
                    "language": "ger", "score": 4.2
                }]
            },
            "highlighting": {"ISSUE-001-PAGE-3": {"plainpagefulltext": ["… {vierte Dimension} …"]}}
        }
        client = FakeClient([payload])
        rows = harvest.search_ddb(client, '"vierte dimension"', 10, 1870, 1945, "secret", 5)
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]["source"], "ddb_newspaper_portal")
        self.assertIn("vierte Dimension", rows[0]["snippet"])
        self.assertEqual(rows[0]["year"], 1888)
        self.assertEqual(client.calls[0][2]["Authorization"], 'OAuth oauth_consumer_key="secret"')

    def test_ddb_sweeps_pages_but_respects_page_ceiling(self):
        first_docs = [
            {"id": f"id{i}-p1", "pagename": "p1", "pagenumber": 1,
             "paper_title": f"Paper {i}", "publication_date": "1890-01-01T00:00:00Z"}
            for i in range(100)
        ]
        first = {"response": {"numFound": 250, "numFoundExact": True, "docs": first_docs}, "highlighting": {}}
        second = {"response": {"numFound": 250, "numFoundExact": True,
                                "docs": [{"id": "id100-p1", "pagename": "p1", "pagenumber": 1,
                                          "paper_title": "Paper 100", "publication_date": "1890-01-01T00:00:00Z"}]},
                  "highlighting": {}}
        client = FakeClient([first, second])
        rows = harvest.search_ddb(client, "Zöllner", 500, 1870, 1945, "secret", 2)
        self.assertEqual(len(rows), 101)
        self.assertEqual(len(client.calls), 2)
        self.assertFalse(rows[0]["raw"]["ddb_page_sweep_complete"])
        self.assertEqual(rows[0]["raw"]["ddb_pages_fetched"], 2)

    def test_anno_requires_explicit_opt_in(self):
        with self.assertRaisesRegex(RuntimeError, "disabled by default"):
            harvest.search_anno(FakeClient([]), "vierte Dimension", 5, 1870, 1945, False)

    def test_anno_search_parses_issue_and_bounds_pagination(self):
        payload = {
            "totalHits": 1,
            "documents": [{
                "docId": "ANNO_nwg19241121",
                "uid": {"owner": "ANNO", "annoDate": {"date": "1924-11-21"}},
                "displayTitle": "Neues Wiener Tagblatt",
                "openUrl": "https://anno.onb.ac.at/example",
                "pageCount": 22,
                "totalHitsInDoc": 4,
                "places": ["Wien"], "languages": ["ger"]
            }]
        }
        client = FakeClient([payload])
        rows = harvest.search_anno(client, '"vierte Dimension"', 10, 1870, 1945, True, "all", 0, 5)
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]["year"], 1924)
        self.assertEqual(rows[0]["title"], "Neues Wiener Tagblatt")
        self.assertTrue(rows[0]["raw"]["pagination_complete_to_requested_limit"])

    def test_oai_pmh_resumption_tokens_are_bounded(self):
        xml1 = b'''<OAI-PMH><ListRecords><record><header><identifier>oai:1</identifier></header><metadata><dc><title>irrelevant record</title></dc></metadata></record><resumptionToken>next</resumptionToken></ListRecords></OAI-PMH>'''
        xml2 = b'''<OAI-PMH><ListRecords><record><header><identifier>oai:2</identifier></header><metadata><dc><title>still irrelevant</title></dc></metadata></record><resumptionToken>last</resumptionToken></ListRecords></OAI-PMH>'''
        class OaiClient:
            def __init__(self):
                self.calls = 0
            def get(self, *args, **kwargs):
                self.calls += 1
                return (xml1 if self.calls == 1 else xml2), {}, args[0]
        client = OaiClient()
        rows = harvest.search_oai_pmh(client, "https://example.org/oai", "Zöllner", 10, max_batches=2)
        self.assertEqual(rows, [])
        self.assertEqual(client.calls, 2)


if __name__ == "__main__":
    unittest.main(verbosity=2)
