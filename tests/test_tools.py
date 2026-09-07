from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def load(name: str, relative: str):
    spec = importlib.util.spec_from_file_location(name, ROOT / relative)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


index_papers = load("index_papers", "tools/index_papers.py")
extract_papers = load("extract_papers", "tools/extract_papers.py")


class IndexTests(unittest.TestCase):
    def test_identifier_hints_do_not_overclaim(self):
        self.assertEqual(index_papers.identifier("x/ssrn-7055399.pdf")["scheme"], "ssrn")
        self.assertEqual(index_papers.identifier("x/2307.05548v2.pdf")["scheme"], "arxiv")
        self.assertEqual(
            index_papers.identifier("x/0010047v2.pdf")["scheme"],
            "unresolved-seven-digit-id",
        )

    def test_duplicate_group_is_structural(self):
        entries = index_papers.enrich(
            [
                {"path": "A/a.pdf", "bytes": 1, "content_id": "same", "hash_kind": "test"},
                {"path": "B/b.pdf", "bytes": 1, "content_id": "same", "hash_kind": "test"},
            ]
        )
        state = index_papers.make_state(entries, "tree", False, "time")
        self.assertEqual(state["counts"]["duplicate_content_groups"], 1)


class ExtractionTests(unittest.TestCase):
    def test_page_markers_are_explicit(self):
        text = extract_papers.page_document(["one", "two"])
        self.assertIn("===== PAGE 1 =====", text)
        self.assertIn("===== PAGE 2 =====", text)


if __name__ == "__main__":
    unittest.main()
