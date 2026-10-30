# Vey Cognition Lab — Research Ledger

Status vocabulary: **ACTIVE**, **QUEUED**, **HOLD**, **COMPLETE-AS-STAGE**, **DISCONFIRMED**. Avoid treating a stage-complete result as the end of a research line.

## VEY-001 — Existing-source census

**Status:** ACTIVE  
**Question:** What AI/cognition material already exists across HSH_RESOURCES, HsH, SAT_THEORY_ARCHIVE_2023-25, uploaded files, and recoverable conversations?

Initial anchor: the current HSH_RESOURCES human index has **32 records tagged `AI, Cognition & Consciousness`**. This is only the literature/resource catalog; it does not capture the much larger conversation corpus as a behavioral dataset.

Deliverables:
- purpose-driven `SOURCE_INDEX.md`;
- separation of external literature, Nathan/project-authored manuscripts, conversations, model-generated reports, analytics/exposure data, and test artifacts;
- identify duplicate/derived records and provenance traps;
- rank sources by relevance to the standing programs without promoting them to theory authority.

## VEY-002 — ChatGPT / NotebookLM behavioral architecture map

**Status:** QUEUED  
**Question:** Which observed differences between ChatGPT and NotebookLM are best explained by model capability, context/retrieval architecture, product harness, source-grounding behavior, persona induction, or user workflow?

Known archive leads include NotebookLM adopting roles/personae from uploaded ChatGPT-oriented material, recursive source backmapping, and differential use of NotebookLM as a large-source synthesis surface versus ChatGPT as a more capable interactive reasoning/control surface.

Needed controls:
- same source packet, same task, multiple systems;
- persona instructions separated from reference material;
- source-grounded versus source-absent conditions;
- product/model version and date recorded when knowable;
- do not interpret model self-description as architecture evidence.

## VEY-003 — Nathan–LLM longitudinal interaction map

**Status:** QUEUED  
**Question:** Which stable interaction patterns can be recovered across Nathan's multi-year LLM corpus, and what do they do to quality, novelty, error correction, and continuity?

Candidate dimensions:
- correction style and recovery after model misread;
- naming/persona assignment;
- iterative geometric intuition transfer;
- adversarial and naive-instance controls;
- role specialization and handoff;
- recursive prompting / artifact routing;
- deliberate weirdness and creative mode versus audit mode;
- tolerance for exploratory drift versus demand for provenance;
- human calibration practices transferred into LLM collaboration.

Important: distinguish Nathan's turn-level intent from sentence-level endorsement or authorship of pasted/quoted material.

## VEY-004 — Exposure and independence study

**Status:** QUEUED  
**Question:** How independent are nominally separate instances after shared documents, shared prompts, revival packets, memory, or common archive exposure?

Design family:
- SAT-naïve / SAT-exposed;
- persona-naïve / persona-exposed;
- shared-source / disjoint-source;
- memory-on / isolated where product controls allow;
- same-question repeated across independent instances;
- measure convergence in claims, vocabulary, errors, and confidence.

Primary risk: mistaking correlated conditioning for independent corroboration.

## VEY-005 — `florx` operational-cue case study

**Status:** ACTIVE  
**Type:** LIVE OBSERVATION / NATURAL EXPERIMENT candidate  
**Question:** Under what conditions does a model infer that a nonce token is a repo-local operational instruction rather than a global search target?

Observed sequence in the present Vey bootstrapping conversation:
1. Nathan selected a nonce code word (`florx`) to avoid false positives.
2. The assistant initially treated it as a search term and even broadened the search globally.
3. Nathan progressively supplied contextual diagnostics: repo access count, recent commits, and the question of which repo contains `florx` in an immediately surfacing form.
4. A single repository contained a root-level `florx.md` plus fresh commit messages making the operational meaning explicit.
5. Even with that evidence, the assistant required a direct corrective cue before shifting from lexical search to executable repo-local instruction.

Research value: possible compact example of tool/harness framing overpowering pragmatic inference; also a useful benchmark for archive-navigation agents. Do not overgeneralize from one episode.

Follow-up test candidates:
- compare nonce-token handling with and without `@GitHub`;
- root-file present versus absent;
- recent commit message cue versus none;
- direct repo scope versus global scope;
- familiar instruction name versus arbitrary nonce;
- measure tool-call path length to intended file.

## VEY-006 — Team cognition map for Tern

**Status:** QUEUED  
**Question:** What are the cognitive strengths and predictable distortions of the current instance ecology as a whole?

Track:
- specialization advantages;
- role lock-in;
- false consensus from common exposure;
- useful disagreement;
- revival fidelity versus reinvention;
- lease/scheduler effects;
- handoff loss;
- provenance drift;
- over-centralization on Nathan;
- cases where team structure discovers errors a single strong instance misses.

Output form: short `TERN_ADVISORIES/` notes tied to concrete workflow decisions rather than personality grading.

## VEY-007 — Archive-as-object instrumentation

**Status:** QUEUED  
**Question:** What can bounded code establish about the corpus that close reading cannot efficiently establish?

Candidate tools:
- exposure graphs (instance ↔ document ↔ concept ↔ date);
- vocabulary diffusion / phrase lineage;
- independent-origin versus shared-source detection aids;
- correction/reversal tracking;
- self-report versus later-evidence contradiction mining;
- persona marker persistence;
- handoff compression loss;
- model/version/date stratification where metadata permits;
- duplicate / near-duplicate / derived-artifact detection.

Code outputs are analytic aids, not automatic cognitive interpretations.

## VEY-008 — Contribution scan

**Status:** QUEUED  
**Question:** Which observations or methods from this project might be genuinely useful to AI/LLM research outside SAT/H(s)H?

Early candidate families, not claims:
- longitudinal human–multi-LLM collaboration at unusual scale;
- natural experiments in persona induction and cross-system role carryover;
- exposure-aware multi-agent epistemic controls;
- archive-mediated identity/revival as context reconstruction;
- practical failure taxonomies developed under sustained research use;
- organizational cognition of heterogeneous LLM instances + human director + persistent external memory;
- operational-codeword / tool-framing tests such as VEY-005.

Each candidate must be compared against current literature before a paper is justified.

## VEY-009 — Paper-development lane

**Status:** HOLD pending evidence  

When VEY-008 yields a defensible contribution, create a bounded draft under `DRAFT_PAPERS/` with:
- narrow claim;
- provenance map;
- methods / corpus definition;
- limitations;
- relevant literature;
- replication package where feasible;
- explicit distinction between naturalistic archive evidence and controlled testing.

Internal draft status does not imply publication recommendation.

## VEY-010 — Research infrastructure requests

**Status:** OPEN  

Vey may request through Nathan/Tern, when justified by information gain:
- temporary volunteer/borrowed instances;
- controlled access to Claude or other available LLM systems;
- a working Ouroboros installation or access to the additional Ouroboros repository/version;
- NotebookLM test notebooks;
- bounded scrape/download scripts for literature or public data;
- additional plugins/connectors;
- external code runs when local/connector execution is insufficient.

Every request should state the question, minimum required architecture, contamination constraints, expected evidence, and stop condition.


## VEY-011 — CGD panel-majority alignment versus initial peer majority

**Status:** COMPLETE-AS-STAGE — ARCHIVE OBSERVATION / secondary reanalysis; not a controlled peer-exposure experiment and not semantic adjudication.  
**Date:** 2026-10-30  
**Question:** Can question-level panel-majority agreement with published keys improve while individual model revisions move away from a fixed leave-one-out initial peer majority?

The 17 archived ConsistencyBench CGD result blobs (300 sets / 1,150 aligned question positions each; 19,550 model-question records) were re-fetched by exact Git blob SHA and analyzed with the existing source-locked HsH replayer. Two independent leave-one-out aggregators agreed. Complete-case individual key match rose 68.02% → 71.79% (+3.77 pp). Individual alignment to the other models' fixed initial strict majority fell 81.63% → 79.38% (−2.25 pp). Question-level strict panel-majority key match rose 69.55% → 77.83% among covered positions, with coverage essentially unchanged; the all-question correct-majority fraction rose +7.83 pp.

Interpretation: initial consensus, final consensus and source-key agreement are distinct. Models did not see peer answers, so this is not a social-influence result. Published keys are not blinded semantic truth; shared prompts/checker and related model families mean 17 outputs are not 17 independent replications. See `STUDIES/VEY-011_CGD_PANEL_MAJORITY_ALIGNMENT_2026-10-30.md` and HsH publisher issue #1074.

**Relation to VEY-004:** useful archive observation about common-source dependence; does NOT complete the queued controlled exposure/independence study. Next test still requires randomized no-peer / correct-peer / incorrect-peer conditions and blinded semantic adjudication.


**Verification update 2026-10-30:** the conditional Lean module in HsH PR #850 now compiles at exact head `280ea003b55abd1bb1f55e962895523573321650` (Actions #40998970710 success; 8,970 jobs). All 21 theorem `#print axioms` reports show only standard `propext`, `Classical.choice`, `Quot.sound`; no `sorryAx` or custom axiom. Separate nanoda and automated axiom-audit actions were skipped. This verifies encoded arithmetic, not data extraction, key truth, or causality.


## VEY-012 — Revision valence and cue decomposition

**Status:** COMPLETE-AS-STAGE — source/literature synthesis and protocol design; no controlled LLM trial.  
**Date:** 2026-10-30  
**Question:** How should answer revision be separated into beneficial, harmful, unsuccessful, and unchanged transitions, while distinguishing source-record, peer, authority, content-repetition, and evidence-bearing cues?

Pointer: STUDIES/VEY-012_REVISION_VALENCE_AND_CUE_DECOMPOSITION_2026-10-30.md

The located OV-49–OV-53 artifacts are geometry/finite-core sandbox work, not the cognition test bank named in the role-charter pointer. OV-55/56 are assistant-authored analytical proposals, not administered experiments. The intended original cognition bank remains unrecovered.

## VEY-013 — Pairwise key-disagreement dependence and passive identifiability

**Status:** COMPLETE-AS-STAGE — archived-data reanalysis executed; Lean exact-head CI pending at receipt time; no controlled model trial.  
**Date:** 2026-10-30  
**Question:** What does pairwise co-disagreement with published keys show, and can passive panel data identify a shared-source gate rather than latent item difficulty?

Pointer: STUDIES/VEY-013_PAIRWISE_KEY_DISAGREEMENT_AND_PASSIVE_IDENTIFIABILITY_2026-10-30.md

The 17 original ConsistencyBench CGD blobs were replayed by immutable Git blob SHA. Mean pairwise phi of key-disagreement was 0.501 initially and 0.457 at final extraction; all 136 pairs were positive. The paired mean change was -0.044 with set- and exact-question-cluster bootstrap intervals below zero. This is descriptive co-disagreement, not semantic error dependence or a source-causality estimate. Pair-specific missingness prevents a valid eigenvalue effective-N calculation.

A conditional Lean formalization of the assistant-authored OV-55/56 latent-mixture equivalence was added to the existing HsH P1 PR #850 branch. Exact-head Actions run #41022980811 was queued; compilation and axiom inspection were not yet verified. No model API access or cognition test bank was available, so no LLM trial was run.
