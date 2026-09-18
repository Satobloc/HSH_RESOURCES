# CROSS — START HERE

**Workspace:** PRIOR_ART/WORKSPACES/CROSS/  
**Status:** ACTIVE / QUARANTINE-BOUND  
**Current lane:** factual-record construction, source attribution, provenance, chronology, and analysis-readiness administration.  
**Controlling rule:** collection and chronology only unless Nathan explicitly authorizes interpretation in this factual-record instance.

This page is the human-readable front door to the Cross workspace. It exists so a new instance does not need chat memory, filename intuition, or inherited summaries to understand what is current.

## 60-second entry path

Read these in order:

1. **Operating control:** [CONTINUITY.md](CONTINUITY.md)  
   Current role, quarantine boundary, strict evidence-vs-analysis interlock, speaker discipline, and bounded-bite rule.

2. **Current processing state:** [CURRENT_PROCESSING_CHECKPOINT_2026-09-17.md](CURRENT_PROCESSING_CHECKPOINT_2026-09-17.md)  
   What has been processed, what raw sources are accessible, and which provenance gaps are open.

3. **Analysis boundary / Organizatino ledger:** [ANALYSIS_READINESS_LEDGER_2026-09-17.md](ANALYSIS_READINESS_LEDGER_2026-09-17.md)  
   What the separate Analysis instance may analyze now, what requires caveats, and what remains on hold.

4. **Nathan-only argument record:** [NATHAN_ARGUMENT_LEDGER.md](NATHAN_ARGUMENT_LEDGER.md)  
   Nathan's propositions, questions, qualifications, and corrections kept separate from generated LLM narrative.

5. **Source-attribution routing:** [EXPOSURE_SOURCE_ATTRIBUTION_MAP.md](EXPOSURE_SOURCE_ATTRIBUTION_MAP.md)  
   Classification of mixed podcast/exposure files, duplicate controls, and speaker/source cautions.

6. **Open/closed provenance gaps:** [CROSS_SOURCE_GAPS.tsv](CROSS_SOURCE_GAPS.tsv)  
   Exact missing-source questions, search history, present status, and next route.

7. **External chronology:** [CROSS_EXTERNAL_CHRONOLOGY.tsv](CROSS_EXTERNAL_CHRONOLOGY.tsv)  
   Dated external scientific records with source metadata and neutral notes.

8. **Current separate-Analysis report:** [ANALYSIS_PRE_CROSS_ARGUMENT_AUDIT_2026-09-18.md](ANALYSIS_PRE_CROSS_ARGUMENT_AUDIT_2026-09-18.md)  
   Reconstructs and audits the pre-Cross ~91% percolation argument before prior-art review proper. This is an Analysis-lane product and is **not** a factual-record conclusion or collection control.

For a machine-readable inventory of every artifact in this directory, use [ARTIFACT_REGISTRY.tsv](ARTIFACT_REGISTRY.tsv).

## External controlling / primary interface files

These are outside this workspace but are part of the current Cross interface:

- EXPOSURE_STATS/CROSS_DIFFUSION_JOB_DESCRIPTION.md — present collection-only job definition.
- EXPOSURE_STATS/CROSS_MASTER_CHRONOLOGY.md — master dated timeline combining SAT/public, podcast, GitHub, and external records.
- EXPOSURE_STATS/CROSS_DIFFUSION_SOURCE_MANIFEST.csv — source manifest for the exposure corpus.
- EXPOSURE_STATS/CROSS_IMAGE_TEXT_INDEX.md — image-text routing/index artifact.
- EXPOSURE_STATS/PODCAST_EPs/CROSS_TRANSCRIPT_CATALOG.csv — transcript catalog.
- EXPOSURE_STATS/PODCAST_EPs/CROSS_TRANSCRIPT_KEYWORD_HITS.csv
- EXPOSURE_STATS/PODCAST_EPs/CROSS_TRANSCRIPT_KEYWORD_MATRIX.csv
- EXPOSURE_STATS/PODCAST_EPs/CROSS_TRANSCRIPT_KEYWORD_INDEX.md

These mechanical indices are retrieval aids, not conclusions.

## Authority order

When two artifacts appear to disagree, first identify what kind of disagreement it is.

### Operating instructions

Use this order:

1. Nathan's latest explicit instruction in the active task.
2. CONTINUITY.md and CROSS_DIFFUSION_JOB_DESCRIPTION.md.
3. this START_HERE.md interface and the current processing checkpoint.
4. older README/work-record/savepoint language.

Older plans that call for immediate causal/diffusion synthesis are historical planning only while the current collection-only interlock is active.

### Factual/source content

Use this order:

1. directly inspected raw source / raw analytics / authoritative external record;
2. explicit source metadata and direct Nathan correction;
3. source-specific SOURCE_TRIAGE_*.md note;
4. current structured ledgers;
5. routing maps / matrices;
6. derivative summaries, old compilation passes, memory/savepoints.

Never promote an older summary above a directly available raw source.

### Analysis products

Separate Analysis-lane reports may interpret READY / READY WITH CAVEATS material inside their documented limits. They do **not** override the factual/source authority order above and must not be silently folded back into raw-data ledgers as factual conclusions.

## Artifact classes

### A. Current control and interface

- START_HERE.md — human front door.
- ARTIFACT_REGISTRY.tsv — machine-readable artifact inventory.
- CONTINUITY.md — controlling role/interlock.
- README.md — concise workspace landing page; should point here.
- RECORD.md — chronological work log, not a current-state substitute.

### B. Current state / handoff

- CURRENT_PROCESSING_CHECKPOINT_2026-09-17.md — current factual-processing checkpoint.
- ANALYSIS_READINESS_LEDGER_2026-09-17.md — READY / READY WITH CAVEATS / HOLD interface for Analysis.
- CROSS_SOURCE_GAPS.tsv — active provenance-gap ledger.

### C. Core factual ledgers

- NATHAN_ARGUMENT_LEDGER.md — Nathan-only propositions/corrections.
- CROSS_EXTERNAL_CHRONOLOGY.tsv — external dated records.
- CROSS_ARGUMENT_EVIDENCE_LEDGER.tsv.gz.b64 — compressed snapshot of the argument/evidence TSV. Treat as a snapshot, not an automatically live table.

### D. Routing / attribution aids

- EXPOSURE_SOURCE_ATTRIBUTION_MAP.md — source classes, duplicate relationships, attribution cautions.
- EXPOSURE_ARGUMENT_EVIDENCE_MATRIX.md — mixed argument/evidence routing matrix.

**Caution:** these files contain some inherited interpretive language from earlier Cross phases. The present collection-only control supersedes any causal/significance language in them. Use their source-attribution and routing content; do not treat older analytical passages as current factual-record conclusions.

### E. Current Analysis products

- ANALYSIS_PRE_CROSS_ARGUMENT_AUDIT_2026-09-18.md — separate Analysis-lane reconstruction of the pre-Cross diffuse-percolation case, its failed/weakened/surviving premises, and the freeze immediately before prior-art review proper. **Interpretive; not a factual-record control.**

### F. Source-specific triage notes

Each SOURCE_TRIAGE_*.md note records a bounded source classification, provenance, speaker structure, duplicate relationship, correction/conflict, and routing rule. Current set includes:

- SOURCE_TRIAGE_DEBATING_AI_1_2026-09-17.md
- SOURCE_TRIAGE_DEBATING_AI_2_2026-09-17.md
- SOURCE_TRIAGE_DEBATING_AI_3_2026-09-17.md
- SOURCE_TRIAGE_DEBATING_AI_PODCAST_2026-09-17.md
- SOURCE_TRIAGE_GG1_2026-09-17.md
- SOURCE_TRIAGE_GG2_2026-09-17.md
- SOURCE_TRIAGE_GG3_GOOG_2026-09-17.md
- SOURCE_TRIAGE_GG4_2026-09-17.md
- SOURCE_TRIAGE_GOOGLE4_2026-09-17.md
- SOURCE_TRIAGE_GOOGLE_PY_2026-09-17.md
- SOURCE_TRIAGE_TRENDS_IMAGES_2026-09-17.md

If a source is already triaged, do not reopen it generically. Reopen only for a specific unresolved datum.

### G. Historical / superseded working snapshots

- CURRENT_COMPILATION_LEDGER_2026-09-16.md
- CURRENT_COMPILATION_LEDGER_2026-09-16_PASS2.md
- SAVEPOINT_2026-09-17_0316ET.md
- SOURCE_PROVENANCE_MANIFEST_2026-09-17_0316ET.tsv
- MEMORY.md

These are retained for auditability and continuity. They are not the current front door. If they conflict with the current checkpoint/readiness ledger or a later source-triage note, use the later/current artifact.

### H. Deferred / separate scope

- SCHREIBER_HH_LINEAGE_RESEARCH_PLAN.md — prior-art / Schreiber / nLab lineage plan. It is deliberately outside the current diffusion factual-record assignment unless Nathan reopens that lane.

## Current analysis interface

The separate Analysis instance should begin with ANALYSIS_READINESS_LEDGER_2026-09-17.md.

Current interface states are:

- **READY** — organized enough for analysis without basic source archaeology.
- **READY WITH CAVEATS** — analysis may proceed only inside the documented limits.
- **HOLD** — normalization/provenance is incomplete; do not force a conclusion.
- **OUT OF CURRENT CROSS SCOPE** — route elsewhere.

The readiness label describes organization, not evidentiary strength.

The current Analysis-lane synthesis is `ANALYSIS_PRE_CROSS_ARGUMENT_AUDIT_2026-09-18.md`. It is explicitly downstream of the factual record and freezes the diffuse-percolation case before prior-art review proper.

## Current major unresolved data work

The current readiness ledger identifies these main pre-Pass-2 jobs:

1. canonical podcast metric dictionary and reconciled raw time series;
2. canonical/deduplicated GitHub traffic series;
3. Google Trends settings/value recovery where possible;
4. earliest-public/preprint date backfill for analytically relevant external items;
5. any remaining mixed-source attribution cleanup that could alter the factual record.

Open provenance gaps are maintained separately in CROSS_SOURCE_GAPS.tsv; do not infer that an unresolved gap is either positive or negative evidence.

## Speaker/source labels

Use these labels explicitly in new records:

- **RAW DATUM** — directly observed value/text/metadata.
- **NATHAN** — Nathan's statement, question, qualification, or correction.
- **LLM / ASSISTANT** — generated claim, interpretation, hypothesis, or question premise.
- **DERIVATIVE SUMMARY** — NotebookLM/LLM/compiled synthesis of other material.
- **EXTERNAL SOURCE** — outside publication/news/record.
- **UNRESOLVED** — conflict, missing source, uncertain identity, or incomplete metadata.

A compiled NATHAN: document is not the same thing as a raw ChatGPT export. Preserve that distinction.

## Update protocol

After a bounded collection task:

1. create/update the source-specific triage note if classification/provenance changed;
2. update EXPOSURE_SOURCE_ATTRIBUTION_MAP.md if routing changed;
3. update NATHAN_ARGUMENT_LEDGER.md only for a genuinely new Nathan proposition/correction;
4. update CROSS_SOURCE_GAPS.tsv only if a gap opens, closes, or materially changes;
5. update CURRENT_PROCESSING_CHECKPOINT_2026-09-17.md;
6. update ANALYSIS_READINESS_LEDGER_2026-09-17.md only if organization/readiness status changes;
7. keep ARTIFACT_REGISTRY.tsv current when an artifact is added, superseded, or changes role.

Do not silently overwrite provenance history. RECORD.md is the append-oriented work log for interface or process changes.

## Quarantine

All Cross artifacts remain inside PRIOR_ART unless Nathan explicitly releases specific material. This is provenance/plagiarism hygiene. Do not leak substantive quarantined prior-art content into ordinary H(s)H theory development.
