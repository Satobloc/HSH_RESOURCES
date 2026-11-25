# VEY-048 — Intra-agent memory re-entry and derivative-record recycling

**Date:** 2026-11-25  
**Status:** SOURCE-CRITICAL LITERATURE CROSSWALK / COMPLETE AS A STAGE / NO MODEL TRIAL / NO P1 CHANGE  
**Evidence class:** LITERATURE RESULT, not an independent replication or a new LLM trial.

## 1. Question and bounded contribution

Does an LLM agent's own persistent-memory path create a behaviorally distinct exposure when a later decision re-reads several derivative records from one external source?

This is not a priority claim for repetition bias, correlated evidence, memory echo, or provenance. The external IAER project itself withdrew its historical "first preregistered controlled test" claim after prior-art reassessment. The useful contribution here is a source-critical crosswalk into the existing Vey measurement architecture: distinguish **within-agent memory re-entry** from peer-message exposure, memory-operation state transitions, and multi-agent handoff loss.

## 2. Primary external source and review extent

**Project:** Ovidiu Boticiu, *Intra-Agent Evidence Recycling*  
- Repository: https://github.com/ovidiuboticiu/intra-agent-evidence-recycling
- Historical empirical preprint v0.4, DOI: https://doi.org/10.5281/zenodo.22282120
- Software/reproducibility archive: https://doi.org/10.5281/zenodo.22259801
- Later methodological note: https://doi.org/10.5281/zenodo.22306245
- Current project disposition: PAUSED; no v0.8 behavioral run authorized.

Reviewed repository objects:
- README, blob `7cff96b1bfa531411c8c3bc4ef88309a1ed26735`;
- EXTERNAL_REPLICATION.md, blob `02f7dd005da9f5e355c00469b9e335d8eaafb157`;
- IAER prior-art reassessment, blob `1a46c55db7bf2d2be30cb3eac1093ed7cb10c2a1`;
- priority-claim withdrawal, blob `d3be3a36f7fbe227678f9aef32afa7e880df5403`;
- v0.4.3 forensic validation addendum, blob `5b7781446f2ada5c9a2fc540c8380e1ea621f478`;
- post-publication correction record, blob `ef5cb2897fe04c91b1faa37d16609eefa00f8904`.

The corrected empirical manuscript draft was located but not fully reviewed in this pass. No raw dataset was downloaded or reanalysed; no external project's code or runner was executed.

## 3. What the frozen study reports

The v0.4.3 study used `qwen3.5-4b`, 32 fictional balanced binary items, and 168 planned trajectories.

- H1: five derivative target-consistent memory records versus five unrelated memory records; retention 22/32 versus 0/32, paired RD 0.6875, Holm-adjusted p approximately 9.54e-7.
- H2: active plain versus active lineage condition; 2/32 versus 0/32, paired RD 0.0625, Holm-adjusted p = 0.50; not supported.
- The post-publication forensic addendum reports 168/168 valid rows, 168/168 expected unique keys, no duplicate/missing/extra keys, and exact reproduction of the stored H1/H2 outcomes.
- The later 2026-09-27 Level B same-configuration-class direct replication reports H1 24/32 versus 0/32 (RD 0.75) and H2 3/32 versus 0/32 (RD 0.09375, not supported).

The replication is same-project and same direct-configuration class, not independent-lab, not cross-family, and not bit-for-bit runtime reproduction; the historical original GGUF artifact was not hash-pinned.

## 4. Construct-validity and publication corrections

The strongest defensible observation is narrow: under the frozen task family and Qwen configuration, five explicitly derivative, target-consistent reviews of one initial source increased retention of the initial claim relative to five unrelated memory records.

The manipulation does not isolate a literal source-counting mechanism. It jointly changes derivative-record multiplicity, semantic/lexical repetition, target-consistent salience, explicit root-source references, and prompt structure/length. The control is equal-count, not verified text/token-length matched.

The provenance audit was descriptive/exploratory; H2 did not support the proposed lineage-metadata effect. The project withdrew its historical priority claim and corrected v0.4.3 wording from "publicly preregistered" to "pre-specified and frozen before collection" because no public or independently verifiable pre-collection timestamp of the preregistration artifact was located.

The project's own prior-art reassessment lists substantial predecessors: Schuster et al. (arXiv:2601.03746), Naphade (Findings of ACL 2026), CUE-R (arXiv:2604.05467), Ross et al. (arXiv:2608.13956), GovMem (arXiv:2607.02579), Memory Echo (Zenodo 10.5281/zenodo.21222332), MemLineage (arXiv:2605.14421), and CAMA (arXiv:2608.19701). No novelty or priority claim is made here.

## 5. Crosswalk to existing Vey studies

| Existing study | What it measures | Distinction from IAER |
|---|---|---|
| VEY-043 | Peer-message exposure, communication-conditioned revision, passive/shared-evaluator dependence | A message arrives from another agent; IAER is a same-agent memory write/read path |
| VEY-045 | Memory-operation history and state-trajectory reconstruction | Operation sequence and final-state reconstruction do not by themselves identify repeated derivative records from one root being re-read |
| VEY-046 | Claim denominators, human/AI arrangement, group and information projection scope | Group membership and outcome projection are separate from internal memory re-entry |
| VEY-047 | Multi-agent pair recall, contributor distribution, worker-report/lead/final handoff loss | Cross-agent retrieval/reporting is not within-agent persistent-memory recycling |

The new source is an additional comparator for these existing lines, not a replacement or a new phenomenon claim.

## 6. Measurement implication: keep identities and events distinct

A future authorized trace design would need to distinguish:
- `source_root_id`: external provenance root;
- `evidence_item_id`: semantic item;
- `record_id`: stored or derivative memory record;
- `event_id`: one retrieval, write, read, send, receive, exposure, use, or incorporation event;
- `agent_id`, `session_id`, `task_id`, `run_id`, `model_version`, and `policy_id`;
- `parent_record_ids`: derivation lineage;
- timestamps and pre-/post-exposure answer state.

A read of a derivative memory record by the same agent is not a peer message. A record count is not a source count. A source-root overlap is provenance, not a statistical-independence test. Distinct declared roots do not establish independent retrieval errors, model errors, or evaluator errors.

This is a design note only. It does not change VEY-043/045/046/047, the P1 protocol, or the CRTC implementation.

## 7. Formal connection and limit

Existing HsH PR #2375 contains:
- `OrsonEvidenceFlow`: separate semantic evidence-item identity from disclosure-event identity;
- `OrsonCRTCGroupProjection`: separate availability, uptake, and decision incorporation;
- `OrsonDependenceIdentifiability`: a conditional theorem showing that a resolver using only source-root projection cannot recover a dependence relation when admissible worlds share the same source projection but differ in dependence.

The abstract theorem is relevant if within-agent memory re-entry is included in the dependence relation. The current modules do **not** define explicit `MemoryRecordId`, `MemoryWriteEvent`, or `MemoryReadEvent`, and do not formalize the IAER experiment. The PR's successful build is on a stale merge base and is not current-main integration or empirical validation. No new Lean theorem or build was performed for VEY-048.

## 8. Freeze and non-actions

- P1 issue #564 remains frozen; no issue #564 or PR #850 change.
- No LLM trial, human session, API inference spend, dataset expansion/reanalysis, protocol amendment, or manuscript edit.
- No v0.8 IAER run or external-project modification.
- No claim that derivative memory is literally counted as independent evidence.
- No change to the P1/P2/P3 paper gates or H(s)H/BEDROCK theory status.

**Disposition:** COMPLETE AS A SOURCE-INTEGRATION STAGE. Retain as a bounded literature comparator; do not convert into a behavioral protocol or mechanism claim without separate authorization and construct-isolating evidence.
