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


## Additional entry-point verification — SAT archive

The SAT archive README's instruction to start with an `AI/` folder does not match the live tree. The recursive tree contains no root `AI/` directory. The actual AI/tooling welcome surface is `.[⚙️_AI_FILES]/`, and the direct entry sequence is:

1. `README.md`
2. `.[⚙️_AI_FILES]/🪧_WAYFINDING.txt`
3. `.[⚙️_AI_FILES]/ORIENTATION.txt`
4. `.[⚙️_AI_FILES]/INSTITUTIONAL_MAP.txt`
5. `.[⚙️_AI_FILES]/RESOURCES.txt`

Directly read these five surfaces, along with `GUESTBOOK.txt`, and the WORKFLOWS, TOOLS and LOGS wayfinding files. The institutional map distinguishes SAT artifacts, artifact catalogs and archive machinery; it explicitly says `_MIGRATION_HOLD/` contains older/relocated automation and must not be treated as current without confirmation. The Archive Admin request-file workflow is documented as the default for routine archive operations; manual `workflow_dispatch` is fallback/debug. This is documentation evidence only; actual current workflow triggers and execution are for the mechanism-mapping stage.

**Documentation defect:** the root README's AI welcome pointer is stale or misnamed relative to the current tree. Preserve this as a finding for later recommendation, not an authorization to edit the README during inventory.

**Source identities:**
- Root `..findex.txt`: blob `0355c349587a5e3ffffe46117b2157b29a6e384a`, generated 2026-11-23T21:32:19.564781Z.
- `.[⚙️_AI_FILES]/..findex.txt`: blob `1c456c66f159feca61eb4b374bd45860745c4c1e`, indexed 2026-06-08, depth 2 / max 500 entries; historical structural guide, not a current complete inventory.
- `.[⚙️_AI_FILES]/ORIENTATION.txt`: blob `6a8dd474aa7c88e77fe8ea36caafda1803f5e6de`.
- `.[⚙️_AI_FILES]/🪧_WAYFINDING.txt`: blob `be4256c244e9eb470272d0e8d1e4a0444ee63ebc`.
- `.[⚙️_AI_FILES]/INSTITUTIONAL_MAP.txt`: blob `01f9ecef145d9845f1ffbec41f1c94b62be867ad`.
- `.[⚙️_AI_FILES]/RESOURCES.txt`: blob `dedb4ce25f2ca2ff85caf2f0975bae6a751e5a4c`.
- `.[⚙️_AI_FILES]/GUESTBOOK.txt`: blob `599ef7b370c7cdde47ee2f74fbc119c44660d115`.

## A-stage disposition

**GTT-A01.A COMPLETE for the bounded main-branch tree inventory.** The three full recursive trees were read without truncation, the 63 workflow-directory files and priority orientation/control/log surfaces were inventoried, and the prior October 30 HsH audit was recovered to prevent duplication. The inventory is not a full-text review and does not claim that every candidate is active or authoritative.

**Next:** GTT-A01.B maps workflow configuration and worker recommendations to the actual repository targets and operation types. Inspect the 63 workflow files in bounded batches, prioritizing cross-repository reads, checkout/materialization, write permissions, bot commits, issue/PR creation, request-file triggers, schedules, recursion guards and concurrency. Existing Oct 30 findings should be treated as provisional leads until current YAML and execution evidence are read.


## GTT-A01.B — Initial mechanism-to-target mapping (sampled families)

**State:** ACTIVE / first high-priority families mapped. This is not yet the complete 63-file workflow classification. Configuration and run evidence are distinguished below; none of these observations establishes GitHub Traffic attribution.

| Repository / workflow family | Configured trigger and permissions | Repository access / output mechanism | Evidence state |
|---|---|---|---|
| HsH Conversation Viewer build | Manual, hourly at minute 23, and scoped pushes; `contents: write`; concurrency group; skip marker `[skip conversation-viewer]` | Checks out HsH full history and SAT archive shallowly; discovers external conversations; generates catalog/body-search/manifests; commits and pushes generated output to HsH main, with up to four fresh-main retries | YAML directly inspected. Cross-repository read and bot write are configured. Current run not established by the recent first-page run sample. |
| HsH Viewer Pages deployment | Manual and scoped pushes; `contents: read`, Pages write and OIDC | Checks out HsH; validates catalog; uploads Pages artifact and deploys. No repository-content write step in this workflow | YAML directly inspected. Deployment is an execution event, not itself evidence of a Git clone by an outside actor. |
| HsH Mersearch request bridge, lane 2 | Push to lane-2 request file; `contents: write`; independent concurrency group | Checks out HsH full history, stable Mersearch shallow, SAT archive shallow, HSH_RESOURCES shallow; runs Mersearch; builds request manifest/receipt; commits request-scoped results to HsH | Run **45554091984** is live/in progress. Job **139001876678** confirms all four checkout steps completed and Mersearch execution is in progress. No result/receipt claimed. This is another lane's PHY-01 request; GIT did not submit it. |
| HsH issue publisher | Issue events; only owner-authored `[HSH-PUBLISH-V1]` payloads; `contents: write`, `issues: write` | Checks out HsH, then uses GitHub REST Contents API GET/PUT to publish a validated submission and read it back; comments on the issue. It does not use a Git push for the published artifact | Run **45574724859** completed successfully. Job **139069704782** logs show the checkout and verified submission `aldus-h1088-s0-whirligig-source-lineage-decoder-20261125t0800z-001`. Direct execution evidence. |
| SAT Archive Admin | Broad push and manual dispatch; `contents: write`; concurrency; skips its own `[skip archive-admin]` commit | Checks out SAT full history; request-driven Archive Admin tasks, indexing, extraction, logs; commits dashboard/AI files and index to SAT main | Run **44684054130** succeeded. Job **136114046436** confirms Archive Admin, request/index steps and commit. Detailed log shows append-buffer absorption rejected unrecognized material but the workflow continued, recorded a warning, and successfully committed its log/output. |
| HSH three-repository source inventory | Manual, every six hours, and pushes except its generated-output folder; `contents: write`; concurrency group | Checks out HSH full history, HsH shallow, SAT/GLASS shallow; runs the HsH sampler over all three; writes a generated private inventory into HSH_RESOURCES and commits it | Run **45577972228** is in progress. Job **139081117818** confirms HSH and HsH checkouts completed and GLASS checkout was in progress at read time. Run **45578519813** is pending on the GIT anchor commit; it has no job yet. Three runs associated with the preceding GIT writes were cancelled; cancellation cause is not established. |
| HSH cross-archive audience catalogue | Daily schedule at 08:19 UTC, manual and scoped pushes; `contents: write` | One HSH checkout; script uses authenticated GitHub REST API to read recursive trees and blobs across HSH_RESOURCES, HsH and SAT; writes a generated catalogue and pushes to HSH | YAML and script directly inspected. API-based cross-repository reads are configured; no current run was established in this sample. |
| HSH cross-diffusion compiler | Manual and scoped pushes; `contents: write` | One HSH full-history checkout; focused PDF extraction/OCR, analytics database, source manifests and chronology; commits derived output to HSH | YAML directly inspected. No cross-repository checkout appears in this workflow. |

### Important execution observations

1. The GIT workspace writes themselves triggered HSH_RESOURCES' `source-inventory.yml` because its push filter excludes only `SOURCE_INVENTORY/SABLE/source_inventory_run/**`. This is a real automation feedback path: a normal GIT anchor/manifest commit schedules a three-repository inventory run.
2. Four GIT-related commits in this session produced three observed cancelled source-inventory runs and one pending run; an earlier run remains in progress. The workflow declares `cancel-in-progress: false`, so the reason for the cancellations is not inferred from the configuration. Do not treat a pending run as a completed checkout.
3. The source-inventory workflow itself checks out HsH and GLASS as well as HSH_RESOURCES. The current in-progress run directly confirms two checkouts completed and the third was underway. This is strong evidence of an internal cross-repository automation mechanism, but **not** a direct GitHub Traffic COUNTED attribution.
4. The Mersearch lane-2 run independently confirms four repository checkouts in an active search job. It belongs to PHYS and must not be overwritten, claimed as GIT work, or counted as a GIT-submitted search.
5. The HsH issue publisher demonstrates why a workflow run and a Git checkout must be separated from a repository clone event: it checks out the full HsH working tree, but publishes its artifact through REST Contents API calls and an issue comment, not a Git push.
6. The SAT Archive Admin run's successful conclusion masks a contained subtask warning: append-buffer absorption rejected unrecognized material, left the Dashboard/index untouched, and routine logging/publication continued. Workflow success is not equivalent to every internal subtask succeeding.

### Next B bite

Continue the remaining workflow families, prioritizing any that:
- check out more than one repository;
- use broad push or scheduled triggers;
- write commits or create issues/PRs;
- trigger another workflow or consume request files;
- access repositories through authenticated APIs without checkout.

After the configuration map is sufficiently bounded, use `⤳` to join selected actual runs/jobs/steps to canonical event-ledger rows. Preserve missing or ambiguous event identity and Traffic attribution as UNKNOWN. Avoid additional repository writes until this inspection batch is consolidated, because HSH_RESOURCES writes themselves activate the source-inventory workflow.
