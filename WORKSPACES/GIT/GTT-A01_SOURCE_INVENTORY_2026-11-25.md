# GIT_TRAFFIC — GTT-A01.A Source Inventory, initial tranche

**Status:** ACTIVE / initial repository-tree inventory captured; source families located, not yet fully read or classified.
**Purpose:** Establish the candidate universe for the original Haul 9 request to inspect automation machinery, welcome/AI-facing surfaces, workflow recommendations, worker-facing documentation, and work logs across the three repositories.
**Scope:** Default branch `main` of HsH, SAT_THEORY_ARCHIVE_2023-25, and HSH_RESOURCES. This is a bounded tree inventory, not a claim of exhaustive full-text review.

## Repository snapshots

| Repository | Main tree SHA | Paths in recursive tree | Files in `.github/workflows/` | Keyword-selected candidate paths* |
|---|---|---:|---:|---:|
| `Satobloc/HsH` | `dfe9b970336fdaca2be9ad8c1d0f96ffde7c8b5d` | 17,604 | 40 | 123 |
| `Satobloc/SAT_THEORY_ARCHIVE_2023-25` | `028862e6f1b0ffad2f56f4989a2cd0a769d266fd` | 5,430 | 13 | 27 |
| `Satobloc/HSH_RESOURCES` | `ebe999cf948f40c4f4fe0300a52c133b6c74ea1b` | 5,331 | 10 | 28 |
| **Total** | | **28,365** | **63** | **178** |

*Keyword-selected candidate paths match names such as workflow, automation, worker, welcome, start-here, AI-start, agent, and work-log. They are triage candidates, not a complete semantic census. Recursive trees were not truncated.

## Automation surface

### HsH — 40 workflow files

```
.github/workflows/append-provenance-reasoning-batch.yml
.github/workflows/archive-math-hopper-smoke.yml
.github/workflows/archive-math-hopper-three-repo-pilot.yml
.github/workflows/arxiv-random-sample.yml
.github/workflows/audit-old-archive-access.yml
.github/workflows/build-conversation-viewer.yml
.github/workflows/build-keyword-bucket.yml
.github/workflows/build-public-library.yml
.github/workflows/build-visual-catalog.yml
.github/workflows/conversation-json-content-ci.yml
.github/workflows/date-tag-all-conversations.yml
.github/workflows/deploy-conversation-viewer-pages.yml
.github/workflows/extract-ravel-window.yml
.github/workflows/extract-raw-window.yml
.github/workflows/harvest-priority-vocabulary.yml
.github/workflows/issue-publisher.yml
.github/workflows/layered-nathan-autotag.yml
.github/workflows/maintain-navigation.yml
.github/workflows/mercer-cross-source-integrity.yml
.github/workflows/mercer-searcher-1-0.yml
.github/workflows/mercer-unfiled-corpus-audit.yml
.github/workflows/mercer-validator-repair-once.yml
.github/workflows/merge-verified-batches.yml
.github/workflows/mersearch-1-1-index.yml
.github/workflows/mersearch-receipt-backfill.yml
.github/workflows/mersearch-request-bridge-lane-2.yml
.github/workflows/mersearch-request-bridge-lane-3.yml
.github/workflows/mersearch-request-bridge-lane-4.yml
.github/workflows/mersearch-request-bridge.yml
.github/workflows/mysearch-nathan-direct.yml
.github/workflows/provenance-reasoning-scan.yml
.github/workflows/provenance-window-ravel.yml
.github/workflows/publish-paper-series.yml
.github/workflows/refresh-site-discovery.yml
.github/workflows/rotate-featured.yml
.github/workflows/sat-candidate-analysis-sample.yml
.github/workflows/sat-candidate-analysis.yml
.github/workflows/superset-conversation-duplicate-scan.yml
.github/workflows/sync-old-archive-state.yml
.github/workflows/visual-archaeology-cycle.yml
```

Priority orientation / worker / recommendation / log surfaces located:
- `README.md` — routes theory work to BEDROCK, archive discovery to Mersearch Worker Start Here, operations to WORKSPACES/COMMON.
- `AGENTS.md` — mandatory research-entry and execution/evidence rules.
- `WORKSPACES/COMMON/ACTIVE_AUTOMATION_ROSTER.md` — automation roster; contains multiple dated scheduler snapshots, so live-state claims require fresh scheduler readback.
- `WORKSPACES/COMMON/AUTOMATION_WORKFLOW_CONTROL.md` — current automation/workflow control surface.
- `WORKSPACES/COMMON/MERSEARCH_WORKER_START_HERE.md` and `WORKSPACES/COMMON/MERSEARCH_WORKER_REQUEST_TEMPLATE.md`.
- `WORKSPACES/COMMON/WORKER_AUTONOMY_HANDOFF_PROTOCOL.md`, `WORKER_UPKEEP_AND_PRIORITY_REVIEW_PROTOCOL_2026-11-05.md`, `WORKER_FRESHNESS_BREAK_CADENCE.md`, `WORKER_DISCRETION_INTERVENTION_SUBTEAMS_2026-09-24.md`.
- `WORKSPACES/COMMON/BIG_PUSH/WORKER_RECOMMENDATIONS.md`.
- `WORKSPACES/COMMON/REPOSITORY_AUTOMATION_SELF_CLONE_AND_SITE_AUDIT_2026-10-30.md` — prior initial audit, explicitly not a complete workflow census.
- `PUBLIC_SITE/SITE_DEVELOPMENT_WORK_LOG.md`; `CONSULTANTS/MERIDIAN/WORKLOG.md`.

### SAT_THEORY_ARCHIVE_2023-25 — 13 files in workflow directory

```
.github/workflows/archive-admin.yml
.github/workflows/build-archive-structure.yml
.github/workflows/build_archive_structure.py
.github/workflows/combine-text-folder.yml
.github/workflows/extract-nathan-corpus.yml
.github/workflows/extract-pdf-text.yml
.github/workflows/flc-auto-digitize-test.yml
.github/workflows/flc-story-feed.yml
.github/workflows/full-archive-index.yml
.github/workflows/index_folder.py
.github/workflows/index_folder.yml
.github/workflows/tag-sat-mentions.yml
.github/workflows/⚒️_FOLDER_INDEXER.txt
```

Priority orientation / AI / automation surfaces located:
- `README.md` — current human welcome; says AI visitors should start with welcome documents in the `AI/` folder and use `..findex.txt` if they cannot find them.
- `README_SAT_KMAP_PIPELINE.txt`, `README—CORE_RULESET_1.txt` — additional root guidance; the latter identifies itself as a NotebookLM-specific ruleset and must not be mistaken for current GitHub worker control.
- `.[⚙️_AI_FILES]/WORKFLOWS/🪧_WAYFINDING.txt` — explicitly marked STUB / NEEDS REVIEW; gives workflow conventions and requests that workflow edits update the sign.
- `.[⚙️_AI_FILES]/LOGS/workflows/archive_admin_last_run.txt` — latest located run pointer at tree snapshot; links to a dated detailed log.
- `AI_AUTOMATION_ADMIN/` and `.[⚙️_AI_FILES]/` contain further request, tool, workflow, and log surfaces; these need bounded inspection and current-vs-migration-hold separation.

### HSH_RESOURCES — 10 workflow files

```
.github/workflows/arxiv-longitudinal-topic-atlas-pilot.yml
.github/workflows/bibliography-coverage.yml
.github/workflows/consolidate-audience-metrics.yml
.github/workflows/cross-archive-audience-catalog.yml
.github/workflows/cross-diffusion-data.yml
.github/workflows/cross-podcast-transcript-index.yml
.github/workflows/extract-papers.yml
.github/workflows/prepare-arxiv-blind-xray.yml
.github/workflows/source-inventory.yml
.github/workflows/sync-arxiv-random-sample.yml
```

Priority orientation / AI / workflow surfaces located:
- `README.md` — states this is private reference/prior-art storage, not a public synthesis or theory-authority repository; routes AI/LLM users to `indexes/AI_START_HERE.md`.
- `indexes/AI_START_HERE.md` — explicit Mysearch/Mersearch route; generic GitHub search is fallback only when bespoke archive search cannot be operated.
- `info/WORKFLOW_SWITCHBOARD_PROTOTYPE_READ_ME_FIRST.md`, `info/WORKFLOW_SWITCHBOARD_POC.md`, `info/WORKFLOW_THREADING_OPERATORS.md`, `info/WORKFLOW_THREADING_PROTOTYPE.md` — prototype/sandbox workflow systems, not production authority.
- `info/NATHAN_PREFERENCES/AUTOMATION_COORDINATION.md` — user-facing coordination preferences; not a replacement for project control surfaces.
- `WORKSPACES/GIT/GIT_THREAD_START_HERE.md`, BIO and PHYS start-here documents are lane anchors, not worker control documents.

## Prior work and duplication control

HsH already contains `WORKSPACES/COMMON/REPOSITORY_AUTOMATION_SELF_CLONE_AND_SITE_AUDIT_2026-10-30.md`. It is an initial source-inspected checkpoint, explicitly not a complete workflow census. It identified the conversation-viewer build/deploy, Mersearch bridge, and SAT Archive Admin as important automation families and listed the remaining audit work. GTT-A01 must extend and reconcile that report, not repeat it as new discovery.

The previous audit specifically called for:
- all workflow YAMLs in all three repositories and trigger/permission/checkout/write/commit/guard/concurrency/schedule/external-repo classification;
- recent Actions runs/job logs and correlations with bot commits/issues/PRs;
- request lanes and actual receipts/runs;
- issue/PR/branch causality;
- site/editor boundaries.

## Inventory limitations / next work

1. The 63 workflow-directory files are inventoried by path; their current triggers, permissions, checkouts, writes, guards and actual executions have **not** yet been re-audited.
2. HsH has the densest worker/control-plane surface. Do not assume every file named WORKER is a currently active directive; read its authority/status and supersession notes.
3. SAT README points to an `AI/` welcome folder. Inspect the folder and its welcome files next; do not infer that the top-level README is the only AI entry.
4. The HsH README, AGENTS, and selected current automation/worker documents were directly read. The SAT README, workflow wayfinding stub and archive-admin last-run pointer were directly read. HSH_RESOURCES README, AI_START_HERE and workflow prototype orientation files were directly read.
5. Work-log filename sweep found explicit HsH worklogs at `PUBLIC_SITE/SITE_DEVELOPMENT_WORK_LOG.md` and `CONSULTANTS/MERIDIAN/WORKLOG.md`; SAT has `.[⚙️_AI_FILES]/LOGS/workflows/archive_admin_last_run.txt` plus linked run logs; no HSH_RESOURCES file was identified by the literal worklog-name sweep. This is a filename finding, not proof that no logs exist.
6. No workflow, issue, branch, PR, worker instruction, scheduler setting, or production site state was changed by this inventory.

**Next substantive bite:** inspect the SAT `AI/` welcome entry and the live HsH automation controls/prior audit, then classify the 63 workflow files and map only the relevant execution evidence. Keep documentation/configuration distinct from actual runs and actual Traffic attribution.
