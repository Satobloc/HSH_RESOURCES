import copy
import json
import tempfile
import unittest
from pathlib import Path

from intake_preflight_review import evaluate, PreflightError

COMMIT = "a" * 40
BLOB = "b" * 40
PATH = "30SEP_PAPER_DUMP/external-safe-demo.pdf"


def sample():
    inv = {"repository": "Satobloc/HSH_RESOURCES", "commit": COMMIT,
           "files": [{"path": PATH, "blob_sha": BLOB, "bytes": 10}]}
    approvals = {"repository": "Satobloc/HSH_RESOURCES", "inventory_commit": COMMIT,
                 "schema_version": 1, "approvals": [{
        "path": PATH, "blob_sha": BLOB, "bytes": 10, "reviewed_commit": COMMIT,
        "approved": True, "author_checked": True, "restriction_checked": True,
        "reviewer": "Human reviewer", "original_citation": "Demo citation; synthetic only",
        "canonical_work_id": "doi:10.0000/synthetic", "bibliographic_source": "Human-verified metadata fixture",
        "review_record": "TEST-ONLY"}]}
    return inv, [], approvals


class ReviewGateTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        p = self.root / PATH
        p.parent.mkdir(parents=True)
        p.write_bytes(b"0123456789")
        self.i, self.m, self.a = sample()

    def run_gate(self, root=True):
        return evaluate(self.i, self.m, self.a, self.root if root else None)

    def status(self, root=True):
        return self.run_gate(root)["results"][0]["status"]

    def test_explicit_review_provisionally_passes(self):
        self.assertEqual(self.status(), "provisional_review_pass_not_extraction_permission")

    def test_no_root_holds_even_approved(self):
        self.assertEqual(self.status(False), "hold_physical_containment_unverified")

    def test_absent_approval_holds(self):
        self.a["approvals"] = []
        self.assertEqual(self.status(), "hold_missing_approval")

    def test_rejected_review_holds(self):
        self.a["approvals"][0]["approved"] = False
        self.assertEqual(self.status(), "hold_incomplete_review")

    def test_integer_attestation_not_boolean(self):
        self.a["approvals"][0]["author_checked"] = 1
        self.assertEqual(self.status(), "hold_incomplete_review")

    def test_missing_citation_holds(self):
        self.a["approvals"][0]["original_citation"] = " "
        self.assertEqual(self.status(), "hold_incomplete_review")

    def test_changed_git_blob_holds(self):
        self.i["files"][0]["blob_sha"] = "c" * 40
        self.assertEqual(self.status(), "hold_content_version_mismatch")

    def test_size_mismatch_holds(self):
        self.a["approvals"][0]["bytes"] = 9
        self.assertEqual(self.status(), "hold_content_version_mismatch")

    def test_manifest_existing_not_grandfathered(self):
        self.m = [{"source_path": PATH, "status": "extracted"}]
        self.assertEqual(self.status(), "already_in_manifest_not_recleared")

    def test_traversal_fails_globally(self):
        self.i["files"][0]["path"] = "30SEP_PAPER_DUMP/../outside.pdf"
        with self.assertRaises(PreflightError): self.run_gate()

    def test_absolute_path_fails_globally(self):
        self.i["files"][0]["path"] = "/tmp/outside.pdf"
        with self.assertRaises(PreflightError): self.run_gate()

    def test_backslash_path_fails_globally(self):
        self.i["files"][0]["path"] = "30SEP_PAPER_DUMP\\foo.pdf"
        with self.assertRaises(PreflightError): self.run_gate()

    def test_prior_art_alias_fails_globally(self):
        self.i["files"][0]["path"] = "30SEP_PAPER_DUMP/PRIOR_ART/x.pdf"
        with self.assertRaises(PreflightError): self.run_gate()

    def test_restricted_name_blocks_even_with_approval(self):
        name = "30SEP_PAPER_DUMP/hypothesis_h.pdf"
        (self.root / name).write_bytes(b"test")
        self.i["files"][0]["path"] = name
        self.a["approvals"][0]["path"] = name
        self.assertEqual(self.status(), "hold_restricted_name_signal")

    def test_restricted_metadata_blocks_even_with_approval(self):
        self.a["approvals"][0]["original_citation"] = "A. Schreiber (synthetic forbidden signal)"
        self.assertEqual(self.status(), "hold_restricted_metadata_signal")

    def test_symlink_file_blocks(self):
        p = self.root / PATH
        p.unlink()
        external = self.root / "outside.txt"
        external.write_text("anything")
        p.symlink_to(external)
        self.assertEqual(self.status(), "hold_physical_containment_unverified")

    def test_symlink_directory_blocks(self):
        p = self.root / PATH
        p.unlink()
        (self.root / "30SEP_PAPER_DUMP").rmdir()
        (self.root / "actual").mkdir()
        (self.root / "actual" / "external-safe-demo.pdf").write_bytes(b"data")
        (self.root / "30SEP_PAPER_DUMP").symlink_to(self.root / "actual", target_is_directory=True)
        self.assertEqual(self.status(), "hold_physical_containment_unverified")

    def test_missing_physical_file_blocks(self):
        (self.root / PATH).unlink()
        self.assertEqual(self.status(), "hold_physical_containment_unverified")

    def test_physical_size_mismatch_blocks(self):
        (self.root / PATH).write_bytes(b"short")
        self.assertEqual(self.status(), "hold_physical_containment_unverified")

    def test_stale_commit_fails_globally(self):
        self.a["inventory_commit"] = "d" * 40
        with self.assertRaises(PreflightError): self.run_gate()

    def test_stale_reviewed_commit_fails_globally(self):
        self.a["approvals"][0]["reviewed_commit"] = "d" * 40
        with self.assertRaises(PreflightError): self.run_gate()

    def test_duplicate_approval_fails_globally(self):
        self.a["approvals"].append(copy.deepcopy(self.a["approvals"][0]))
        with self.assertRaises(PreflightError): self.run_gate()

    def test_duplicate_inventory_fails_globally(self):
        self.i["files"].append(copy.deepcopy(self.i["files"][0]))
        with self.assertRaises(PreflightError): self.run_gate()

    def test_duplicate_manifest_fails_globally(self):
        self.m = [{"source_path": PATH}, {"source_path": PATH}]
        with self.assertRaises(PreflightError): self.run_gate()

    def test_unknown_approval_path_fails_globally(self):
        self.a["approvals"][0]["path"] = "30SEP_PAPER_DUMP/other.pdf"
        with self.assertRaises(PreflightError): self.run_gate()

    def test_duplicate_blob_approved_both_blocks(self):
        extra = "30SEP_PAPER_DUMP/second.pdf"
        (self.root / extra).write_bytes(b"0123456789")
        self.i["files"].append({"path": extra, "blob_sha": BLOB, "bytes": 10})
        b = copy.deepcopy(self.a["approvals"][0])
        b["path"] = extra
        self.a["approvals"].append(b)
        states = [r["status"] for r in self.run_gate()["results"]]
        self.assertEqual(states, ["hold_multiple_approved_aliases"] * 2)

    def test_duplicate_blob_one_approved_is_one_provisional(self):
        extra = "30SEP_PAPER_DUMP/second.pdf"
        self.i["files"].append({"path": extra, "blob_sha": BLOB, "bytes": 10})
        self.assertEqual(self.run_gate()["counts"], {"hold_missing_approval": 1,
            "provisional_review_pass_not_extraction_permission": 1})

    def test_untrusted_inventory_repository_fails(self):
        self.i["repository"] = "Other/repo"
        with self.assertRaises(PreflightError): self.run_gate()

    def test_missing_approval_envelope_fails(self):
        self.a.pop("approvals")
        with self.assertRaises(PreflightError): self.run_gate()

    def test_missing_required_approval_record_fails(self):
        self.a["approvals"][0].pop("reviewed_commit")
        with self.assertRaises(PreflightError): self.run_gate()


if __name__ == "__main__":
    unittest.main()
