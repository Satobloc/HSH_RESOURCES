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


## VEY-014 — P1 source-pipeline, archive-dependence, and protocol-scope audit

**Status:** COMPLETE AS SOURCE AUDIT; P1 scope recommendation ready for protocol decision; no new model trial; exact-head Lean repair pending.  
**Date:** 2026-10-30  
**Question:** What does the original ConsistencyBench implementation actually expose to models, what is shared across runs, and which claims are supported by the archived benchmark and HsH worker archive?

Pointer: `STUDIES/VEY-014_SOURCE_PIPELINE_AND_P1_SCOPE_AUDIT_2026-10-30.md`, blob `599ea0a8a13cb44b9c95c512c4b217a6c8998d1b`.

Exact primary source: `aayambansal/ConsistencyBench/src/evaluate.py`, Git blob `0453540cb7c19227601e59fb342fa93e736da849`. The shared GPT-4o-mini NLI checker compares same-model prior/current raw answers without question/premise; the repair prompt is contextual; the panel majority is post-hoc and is not fed to models. This is a common evaluator, not peer exposure or a manipulated shared evidence source.

The P1 should be framed as an archival/methodological case study unless an authorized model route and the actual answer-keyed neutral-versus-false-authority bank are recovered before the Nov 2 protocol freeze. The OV-49–53 charter pointer remains mismatched; OV-55/56 and OV-100 are analytical models, not administered trials. VEY-004 remains the separate controlled exposure study. The D1 PDF/TeX/reader bytes were not recovered in this runtime; Nov 9 PDF/reader and independent review gates remain open.


## VEY-015 — P1 key semantics, row-level sensitivity, and finite-pattern identifiability

**Status:** COMPLETE AS SOURCE-LOCKED REANALYSIS; new Lean module committed, exact-head CI pending; no human adjudication or new model trial.  
**Date:** 2026-10-30  
**Question:** How sensitive are the P1 key-accuracy and CGD-versus-vanilla comparisons to the scorer's treatment of free-text negative-inference answer keys, and can the OV-55/56 latent interpretations be shown to yield the same full finite observable distribution?

Pointer: `STUDIES/VEY-015_P1_KEY_SEMANTICS_AND_FINITE_PATTERN_IDENTIFIABILITY_2026-10-30.md`, blob `c305bca9296d85b2ca56a448d98cd5b95ea49526`.

Companion source extraction: `STUDIES/VEY-015_P1_NEGATIVE_INFERENCE_KEY_ROWS_2026-10-30.csv`, blob `a6d93b39a47fa86d2720036e571bfed79586790e`, 578 full-bank rows / 350 sample rows.

Original source blobs: full bank `3171d2899fd1eb4292794df5952514666b0e2f43`; sample `10eb2da27c84c706d8e9e2325afca864fcae6a0d`; upstream evaluator `0453540cb7c19227601e59fb342fa93e736da849`; Orson analysis scorer `2e10ed2510b8ce14e716780a887c0fe23c3067b9`.

The full bank contains 68 "No, not with certainty" keys; the sample contains 50. Three other negative-inference strings ("No, we cannot conclude that", "No, we cannot conclude either way", "No, not necessarily") map to `cannot_determine` under the analysis scorer while "No, not with certainty" maps to `no`. The phrase group is question/reasoning-specific; this is a lexical normalization sensitivity, not an adjudicated correction.

All 34 exact vanilla/CGD model-output blobs (17 per condition) were independently re-fetched. On the 50 affected sample items, 1,677/1,700 correctness classifications change under the alternate mapping, but pooled correct counts move only 836→841 (+5). On that affected subset, CGD-minus-vanilla individual accuracy moves from -1.176 pp to +0.118 pp; 14/17 model labels reverse sign. These are fixed-panel descriptive sensitivities, not causal effects or independent model-population inference.

Added `OrsonFinitePatternDistribution.lean` to existing PR #850: finite powerset pattern weights, normalization, nonnegativity for valid Bernoulli parameters, pointwise equality of the shared-gate and latent-difficulty toy distributions, and non-injectivity of their observation map. First exact-head run #41078042006 failed on a powerset-sum rewrite; repair commit/exact branch head `0efbc7ae1577c37ee36b6bcdb4a0fb7c17ee619c`; exact-head run #41079040914 was pending at note time. Do not claim compilation until that run and theorem-specific axiom outputs are inspected.

No model calls, no human adjudication, no peer-exposure experiment, no P1 manuscript edit, no D1 PDF/TeX/reader recovery, and no public issue. P1 remains Orson-owned; November 2 protocol freeze and November 9 paper gate remain open. Next: exact-head CI/axiom inspection, question-aware key rubric, human adjudication, then premise-cluster paired bootstrap under frozen estimands.


### VEY-015 verification update — 2026-10-30 15:21Z

The repaired exact-head PR #850 run `41079040914` completed SUCCESS on head `0efbc7ae1577c37ee36b6bcdb4a0fb7c17ee619c` (job `124142906377`; 8,972 build jobs). The new `OrsonFinitePatternDistribution` module compiled. All eight theorem-specific axiom outputs were inspected: `propext`, `Classical.choice`, `Quot.sound`; no `sorryAx`. `nanoda` and automated `axiom-audit` were skipped. Formal compilation is now VERIFIED for the toy-model module; no claim about empirical mechanism, key correctness, or physical truth follows.


## 2026-10-30 19:08Z | P1 source-run manifest audit and PCR formalization review

- Published source-run provenance audit through the existing HsH issue publisher: [HsH issue #1114](https://github.com/Satobloc/HsH/issues/1114); artifact `WORKSPACES/COMMON/PUBLISHED_SUBMISSIONS/orson-p1-consistencybench-run-manifest-audit-20261030t1848z-s4-001.md`, SHA-256 `635450a92137f525a840e713370868791e8fd87b250320478231ce7666da6ef1`. Publisher receipt and independent repository readback verified.
- New source finding: pinned ConsistencyBench commit `bfc676baa848c7f1715bb73aee148180de15516` has a six-model/24-task convenience runner, a 22-alias `--all` path, 37 archived result JSONs across 18 model labels, 35 per-model logs, and a combined log containing only two of its stated 24 tasks. Result JSONs lack request timestamps, provider request IDs, and resolved backend model revisions. This is a provenance/reproducibility gap, not evidence of invalid outputs.
- Source topology remains a multi-model evaluation panel, not a live peer group: CGD history is local to each model run; the same question-blind checker implementation is a common evaluation dependency; panel aggregation is post hoc. No cross-model answer input is present in the inspected source.
- The full 17-model PCR replay was independently re-executed against the 34 archived vanilla/CGD output files and reproduces Calder's published aggregate values and the two per-model direction reversals. This is a second calculation implementation on the same archived data, not independent experimental replication. See [HsH issue #1103](https://github.com/Satobloc/HsH/issues/1103).
- The source-conditional Boolean formalization is on a separate stacked draft review branch and [PR #1113](https://github.com/Satobloc/HsH/pull/1113), not on Orson's PR #850. PR #850 remains at prior head `0efbc7ae1577c37ee36b6bcdb4a0fb7c17ee619c`. Exact-head Lean run #41112408633 is still in progress; no compilation claim yet. Issue #1104 was updated with the review PR and pending status.
- Original answer-keyed neutral-versus-false-authority bank remains unrecovered. Historical OV-54 records a proposed test as prepared but not executed; OV-100 is synthetic/stipulated. No authorized model-inference route or human-subject session was used. No D1 manuscript PDF/TeX/reader was found in the inspected Orson workspace or Library search. P1 remains archival/methodological on current evidence; Nov 9 gate remains open and separate from Nov 30 / Dec 14 gates.
- No model calls, human participants, physical calculations, or SAT/H(s)H theory promotion occurred.


## 2026-10-30 | VEY-016 — Human–LLM peer-group interaction and replication-unit audit

- Full-text reviewed Chen, Liu, Hu & Li, “AI agents reshape consensus formation in human groups,” arXiv:2609.02122 (2026-09-02). This is a direct mixed human–multi-LLM peer-participant study: 24-member sessions, 40 rounds of random pairwise interaction, eight conditions, 127 humans and 65 LLM-agent slots as reported.
- Source-count reconciliation: the eight condition compositions sum to 127 humans and 65 agents across 192 seats. With 24 total seats per session, the reported counts strongly imply one session per condition. This is a source-level inference; the paper does not separately state a replicated session count.
- Public processed-data cross-check: A2–A5 questionnaire CSVs contain 108, 144, 189 and 54 rows. The supplement's nine sampled rounds per human make these 12, 16, 21 and 6 humans respectively. The 495 rows equal 55 humans × 9 sampled rounds, matching M5's reported N=495.
- Methodological limitation: the treatment is session/group-level, but one session per condition is implied. The M5 regression uses HC3 heteroskedasticity-consistent standard errors, not participant/session clustering. The same all-MiniLM-L6-v2 model supplies participant feedback/payoff and primary embedding-based consensus analysis. Treat the reported pattern as descriptive for these sessions, not a replicated group-level causal effect or independent semantic truth.
- Corrective effect on the earlier Review-MIND gap: multiple human participants plus multiple LLM agents with reciprocal pairwise interaction is now VERIFIED AS REPORTED. The remaining gap is narrower: independent group/session replication per condition, auditable per-agent source/context ancestry, independent outcome adjudication, cross-family replication, and richer network/task settings.
- Full note: STUDIES/VEY-016_HUMAN_MULTI_LLM_GROUP_INTERACTION_REPLICATION_AUDIT_2026-10-30.md.
- Comparator full-text reviewed: Alsobay et al., “Bringing Everyone to the Table,” PACM HCI 10(6), CSCW059 (2026), DOI 10.1145/3816907; 1,475 participants in 281 five-person groups, 70 groups per condition, GPT-4o facilitator. This has group-level replication but a single facilitator rather than multiple LLM peers; more fact coverage did not significantly improve optimal decision rate.
- Tool audit: Microsoft Research GRAIL (MIT) already supplies human-group session, treatment, consent/survey, transcript and LLM logging infrastructure. Current code is one shared LLM facilitator, not multiple peer agents. Adapt GRAIL rather than build a new platform; add separate agent identities/state, turn scheduling and provenance logging. No API calls, human sessions, hosting, recruitment, or costs incurred.
- Formalization: HsH draft PR #1115 adds a conditional Lean 4/Mathlib proof of treatment/session-indicator identity and coefficient-shift invariance under one group per treatment. Source interpretation remains external to Lean; exact-head CI/axiom review is required before VERIFIED status.
- VEY-004 remains QUEUED. No P1 manuscript edits or paper-gate changes. HSH_RESOURCES remains a research shelf, not H(s)H theory bedrock.


## 2026-10-30 19:37Z | VEY-016 verification and source correction
- PR #1115 exact head `c029318b96a07fc433ed16a9082cb2e7b29002ea` completed Lean CI run #41115603417 / job #124268909008 successfully (Lean 4.34.0, Lake 5.0.0, 8,973 build jobs). Theorem-specific `#print axioms` showed no `sorryAx`; standard dependencies include `propext`, `Classical.choice`, `Quot.sound`. `nanoda` and automated `axiom-audit` were skipped. Formalization remains conditional on one group/session per treatment.
- Independent Python structural check: reported counts total 127 humans +65 agent slots =192 seats =8x24. Under one group per condition, `[I8 | I8]` has rank 8 and nullity 8. No participant-level fit was run.
- Source correction: public A2-A5 files are `.pkl` pickles, not CSVs; prior wording was inaccurate. The current analysis script uses OLS `cov_type="HC3"`, not participant/session clustering. Pickle row counts were not re-extracted in this pass.
- GRAIL repository now shows five forks, not three; no exhaustive fork audit. Main implementation remains a single shared facilitator. README cites PACM HCI 10(6) on 31 Oct 2026, future-dated relative to this run; ACM DOI page returned 403, so publication status is unverified as of 30 Oct. Use arXiv:2508.08242 as the accessible source.
- Historical role provenance separated: original Oct 9 local/Oct 10 UTC instruction = primary LLM-cognition assignment; Oct 26 direct reinforcement = four-of-five target and Nov 9 P1 gate. Exact original conversation/message UUID not recovered.
- No new human-subject work, model API calls, tool build, P1 manuscript change, BEDROCK promotion, or automation change.


### Publication verification
- Existing issue #1116 remains the sole publisher submission for this note. Publisher receipt comment #6531798863 recorded commit `78873863192bf06b90aff915aa2cc9277f20efef`; artifact `WORKSPACES/COMMON/PUBLISHED_SUBMISSIONS/reviewmind-human-ai-peer-group-replication-audit-20261030t1848z-s4-001.md` was read back and matched the issue payload exactly. Independent SHA-256: `38d9738ebb7aed17933815ce3d40d94fadf3600e389f0035e980bd9f03527888`. Additive correction comment #6532231836 was added; no second submission was created.


## VEY-017 — GRAIL multi-peer extension source audit

**Status:** COMPLETE-AS-STAGE — SOURCE-CODE AUDIT / DESIGN PROPOSAL; no LLM trial or human-subject experiment.  
**Date:** 2026-10-30 22:36Z.  
**Question:** Can existing GRAIL be adapted for replicated human-plus-multiple-LLM-peer studies of shared evidence versus direct peer exposure?

- Audited current `microsoft/group_ai_lab` main at commit `c7a2077281fed73f492a29ab187a7b86875203d8`. Exact source blobs for `callbacks.js`, `LLMConfig.js`, `treatments.yaml`, and README are recorded in VEY-017.
- The current code implements one shared facilitator: one global model, one facilitator prompt/identity, one game-level log, and the complete group chat transcript sent to that model. No per-agent identity or state map appears in `callbacks.js`. The platform is not a multi-peer-agent system out of the box.
- Reuse GRAIL rather than build a new platform. A multi-peer extension requires separate agent state/context, explicit message visibility, per-agent request/source lineage, and a turn scheduler.
- Proposed minimum design separates shared-versus-disjoint evidence from peer-output visibility (a 2x2 design), with independent baseline answers before exposure, group/session randomization and replication, and externally adjudicated correctness distinct from consensus.
- No sample-size calculation, new tool, API call, human session, hosting, recruitment, paid cost, external repo edit, or manuscript edit occurred.
- Lean triage: the proposed visibility/state invariant is not defined by current GRAIL source. Formalizing a data-free state model is `BLOCKED_PENDING_NATHAN_PERMISSION`; no Lean module was written or run.
- Original Orson neutral-versus-false-authority answer-keyed bank remains unrecovered. OV-49–53 are geometry/finite-core artifacts; OV-55/56/100 are analytic/synthetic, not administered trials. P1 #564 remains source/experiment readiness.

Full note: `STUDIES/VEY-017_GRAIL_MULTI_PEER_EXTENSION_SOURCE_AUDIT_2026-10-30.md`.

## 2026-10-31 | VEY-018 — human-group replay, DeliChess, correlated judge errors

- Study: [VEY-018_SHAO_KOHLI_DELIDATA_CROSSWALK_AND_KISH_PROOF_2026-10-31.md](STUDIES/VEY-018_SHAO_KOHLI_DELIDATA_CROSSWALK_AND_KISH_PROOF_2026-10-31.md)
- Primary sources: Shao 2026 arXiv:2609.20543v1 (DeliData Wason replay); Zhu et al. 2026 arXiv:2606.04987v1 (DeliChess human-group benchmark and LLM action-selection diagnostic); Kohli 2026 arXiv:2605.29800v1 (correlated judge errors and Kish n_eff).
- Main distinction: passive cross-model error dependence, peer-exposed LLM replay, and human deliberation with objective task scoring are separate regimes. Consensus, correctness, effective independence, peer influence, participation and evaluator dependence must remain separate outcomes.
- Arithmetic: using Kohli's rounded k=9, mean phi=0.391 gives design effect 4.128, n_eff=2.18023256, nominal ratio 24.2248%, asymptote 2.55754. Rounded-input consistency check only; no raw output reanalysis.
- Formalization: conditional exchangeable-variance/Kish module added to existing HsH PR #850; exact-head Lean run #41160309297 pending at report creation. No compile success claimed in this ledger entry until verified.
- P1 remains source/experiment readiness. Original answer-keyed neutral/false-authority bank remains unrecovered; no trial, manuscript, PDF/reader gate, or theory promotion.
- Shao OSF preregistration and Zenodo artifacts were not downloaded; DeliChess dataset bytes were not downloaded; no independent reproduction.


## 2026-10-31T0238Z | VEY-018 Lean CI correction

- First exact-head run #41160309297 on 1b40b9f45c0fde4f1ddc9cce84ae45795f101215 FAILED: noncomputable Real division definitions plus two proof issues. Build did not complete; no theorem verified; tests/lint/nanoda/axiom audit skipped.
- Corrected module committed to existing PR #850 branch at d59a17b270df730e84edbd614eaea3b1b76166e2. Exact-head run #41160835210 IN_PROGRESS; no success claimed.
- A transient unreviewed copy was accidentally written to HsH main at 4ceb26bb3cbd2b289638c2dbc650d5b92ab8105e and removed at 57bab61d9f784cd7325f0da50da428a8db4400b4. Corrected module remains on PR branch only; no root import/theory change on main.


## 2026-10-31 | VEY-019 — Five evidence regimes and consensus measurement audit

- Added STUDIES/VEY-019_FIVE_EVIDENCE_REGIMES_AND_CONSENSUS_MEASUREMENT_AUDIT_2026-10-31.md.
- Integrated Kohli correlated judge errors, Shao human-deliberation replay, Chen mixed human–LLM peer populations, DeliChess human deliberation with Stockfish quality, Alsobay LLM facilitation, and the passive ConsistencyBench evaluator pipeline.
- Recomputed published-summary arithmetic: Kohli rounded-input Kish n_eff = 2.180232558; DeliChess 114/321 RR declines and 102/245 negative-RR cases among increased-modal-share cases.
- Clarified that consensus, correctness, dependence, peer exposure, participation, evaluator coupling, source lineage, and replication unit are distinct.
- Mersearch audit: the completed Orson bank search is broad/path-dominated; a sampled SAT Overview locator is tool-role, not Nathan Direct. Original neutral-versus-false-authority answer-keyed bank remains UNRECOVERED; no claim of absence.
- Exact-head PR #850 run #41160835210 succeeded at d59a17b270df730e84edbd614eaea3b1b76166e2; conditional Kish module compiled, with no sorryAx in the full log. Automated axiom-audit/tests/lint/nanoda were skipped.
- P1 #564 remains SOURCE / EXPERIMENT READINESS; protocol freeze Nov 2, paper gate Nov 9. No trial, model calls, human subjects, manuscript, PDF/reader, or gate advancement.


## 2026-10-31 | VEY-020 - Evidence lineage, transmission, integration, and measurement validity

- Added `STUDIES/VEY-020_EVIDENCE_LINEAGE_TRANSMISSION_INTEGRATION_AND_MEASUREMENT_2026-10-31.md`.
- New primary literature: Gao et al. `Copies or Sources?` (arXiv:2610.06192); Toxtli/Delaflor hidden-profile LLM groups (CSCW Companion 2026); Imel et al. `Rare, Relevant, and Still Wrong` (arXiv:2610.37624); Siboni et al. inhibitory message passing (arXiv:2610.24718); Gong et al. SPLICE (arXiv:2610.40186).
- Independently reimplemented both parsers for the released Qualification by Calibration trial files: 540/540 raw generations matched; both parser implementations matched their shipped outputs 540/540; 88/540 answer classifications changed; 172/540 outputs contained the quoted answer template, with 79 template-contaminated Yes parses.
- Independently recomputed GULI-SET Core Bayesian targets: 48/48 matched, max posterior discrepancy 1.11e-16. Its deterministic naive page-counter baseline retains 100% choice accuracy while posterior MAE is 0.067296 and provenance MAE 1.375; synthetic baseline, not an LLM result.
- Proposed typed evidence lifecycle separates origin, transmission, visibility, integration/adoption, and measurement. Lean targets identified but not compiled; no local Lean runtime and no branch mutation.
- P1 #564 remains SOURCE / EXPERIMENT READINESS; original OV-49-OV-53 answer-keyed bank remains UNRECOVERED; all four Mersearch lanes occupied; no authorized inference endpoint, model call, human-subject session, or API spend.
- November 2 freeze recommendation: if bank and authorized endpoint remain unavailable, freeze Nov 9 P1 as methods/archival synthesis, not an administered experiment. Recommendation only; no paper gate advanced.
- Public-safe summary submitted through existing publisher: issue #1152, submission `orson-p1-evidence-lineage-20261031t1348z-s4-001`, SHA-256 `c6f044362cd0ba02e6bdcf89eff0fafd9677fc1abf0f59de4c531843588d4cd4`; publication receipt/readback pending at ledger update.


## 2026-10-31T1330Z | VEY-020 publication verification

- Existing publisher issue #1152 completed. Artifact: `WORKSPACES/COMMON/PUBLISHED_SUBMISSIONS/orson-p1-evidence-lineage-20261031t1348z-s4-001.md`.
- Publisher commit: `82dc6a38c8417d31d0b22690e2f29cd28039bc7c`.
- Publisher-reported SHA-256: `c6f044362cd0ba02e6bdcf89eff0fafd9677fc1abf0f59de4c531843588d4cd4`.
- The artifact was fetched independently and compared byte-for-byte with the JSON `content` field in issue #1152; exact content equality confirmed. Publisher bot comment #6543993690 reports readback verified.
- P1 issue #564 pointer comment #6544004804 added. No manuscript or paper gate advanced.


## 2026-10-31 | VEY-020 Amendment 01 - PR #850 finite-pattern CI scope

- Corrected the earlier shorthand: PR #850 imports and compiles both `OrsonFinitePatternDistribution.lean` and `OrsonKishEffectiveSampleSize.lean` at current head `d59a17b270df730e84edbd614eaea3b1b76166e2`.
- Exact-head CI #41160835210, job #124417786006, Lean 4.34.0, 8,943 build targets, SUCCESS; no `sorryAx` in the retrieved complete log. Tests, lint, nanoda, and automated axiom audit skipped.
- The finite-pattern module proves normalization and non-injectivity between two specified latent labels under its finite model assumptions. It does not establish which mechanism generated real LLM behavior or validate empirical premises.
- New VEY-020 evidence-lifecycle propositions remain unformalized. No new theorem, branch, or PR.


## 2026-10-31 | VEY-020 Amendment 02 - copy-weight calibration boundary

- Added `STUDIES/VEY-020_AMENDMENT_02_COPY_WEIGHT_CALIBRATION_2026-10-31.md`.
- The numeric copy weights are inferred from posterior-equivalent evidence units using verbalized probabilities and reconstructed from rounded table means. Treat as calibration-dependent behavioral estimates, not direct internal-belief measurements or universal constants.
- Conflict probes and emitted-action channel provide qualitative corroboration, but do not independently validate exact numeric weights. Reference-rule effect remains a reported controlled-setting result.
- Public addendum comments: publisher issue #1152 comment #6544077779; P1 issue #564 comment #6544078127.


## 2026-10-31 | VEY-021 — Naturalistic podcast-reception hypothesis amplification

- Added `STUDIES/VEY-021_NATURALISTIC_PODCAST_RECEPTION_HYPOTHESIS_AMPLIFICATION_2026-10-31.md`, blob `5b68608766042fd45c1075d5717b45153dbb2322`.
- Followed a Mersearch selected locator in `SAT Theory Archive Overview — raw.json` (blob `dec20de13718ba09a59a76e9c958e3eee16304b0`) to its exact raw user/assistant parent chain. The user message is about podcast analytics and a prior audience hypothesis, not the OV-49–OV-53 answer-keyed test bank. It is a bounded false positive for that bank search, not evidence of global absence.
- The assistant's later “small cohort / lab-chat” interpretation is downstream of the user's earlier hypothesis and an earlier assistant endorsement. Treat it as naturalistic context-conditioned narrative reinforcement, not independent corroboration or evidence of actual institutional/academic attention.
- Mersearch query diagnostic: `name:*OV*` contributes 515,754/718,805 matched-term hits (71.7516%); `path:*ORSON*` 108,787 (15.1344%). Term counts overlap. A future search should use exact OV-49–OV-53 variants and distinctive phrases when a lane is actually released; no new request was submitted because all four lanes remain occupied.
- The parent-chain graph is explicit, but the proposed ancestry-disjointness/independence proposition remains UNFORMALIZED. Existing PR #850 modules were inspected; no local Lean runtime and no branch/PR modification under the current interlock. This is a single naturalistic case, not a controlled experiment or P1 trial.
- P1 #564 remains SOURCE / EXPERIMENT READINESS; no manuscript or paper gate advanced. No model call, human-subject session, physical calculation, or data-free numerical fixture.


## 2026-10-31 | VEY-022 — Recorded ancestry and blind-adjudication eligibility

- Added `STUDIES/VEY-022_RECORDED_ANCESTRY_AND_BLIND_ADJUDICATION_GATE_2026-10-31.md`.
- Reopened raw conversation export blob `dec20de13718ba09a59a76e9c958e3eee16304b0`, conversation `6a22c443-54fc-83ea-a025-56256bbf7a27`, and independently verified all three parent edges among the four VEY-021 messages.
- The final assistant interpretation is a transitive descendant of the original user hypothesis through an earlier assistant endorsement and later user-provided OCR; it is not a direct child. Endpoint roles differ. This is recorded ancestry, not a statistical-independence or causal-effect result.
- New operational gate: FAIL_ANCESTRY_BLIND when a prohibited recorded ancestry path exists; UNKNOWN_CONTEXT_INCOMPLETE when the full context manifest is unavailable; ANCESTRY_CLEAR only when a complete versioned context manifest is present and no prohibited path/exposure is recorded. ANCESTRY_CLEAR is necessary leakage control, not sufficient statistical independence.
- Added source-conditional Lean module to existing PR #850 branch: `OrsonVEY021RecordedAncestry.lean`, exact-head commit `b820998976192ab3e4dc1cec1632d4d899bad031`. Exact-head CI run #41225441898 was pending/in progress at ledger update; no compilation success claimed until logs are inspected.
- P1 #564 remains SOURCE / EXPERIMENT READINESS. Original OV-49–OV-53 answer-keyed bank remains UNRECOVERED; no authorized inference endpoint, model call, human subject, or trial. No manuscript or paper gate advanced.


### 2026-10-31T1746Z | VEY-022 exact-head Lean CI verification

- Existing PR #850 exact head `b820998976192ab3e4dc1cec1632d4d899bad031`, Actions run #41225441898, rerun of failed job, completed SUCCESS.
- Job `verify` #124609431758; Lean 4.34.0 / Lake 5.0.0; full build 8,974 jobs.
- `OrsonVEY021RecordedAncestry` built in 5.4 s. All four theorem-specific `#print axioms` reports say the theorem does not depend on any axioms. Full log 100,490 characters; zero `sorryAx` occurrences.
- Workflow tests/lint disabled; no separate nanoda or automated axiom-audit stage ran. Initial attempt's failure cause remains unresolved because its log artifact was unavailable.
- This verifies the encoded finite source-parent graph only, not source authenticity, complete context capture, statistical independence, or causal influence. No P1 trial or paper gate advancement.


### 2026-10-31T1747Z | VEY-022 raw-export context completeness

- Recounted roles across the exact 211-node raw conversation mapping: 47 user, 98 assistant, 65 tool, 1 missing role, 0 system, 0 developer.
- The export is not a complete system/developer/context snapshot. Therefore, a no-path result from an archive-only graph cannot qualify as ANCESTRY_CLEAR; absent independent context-completeness attestation, use UNKNOWN_CONTEXT_INCOMPLETE. VEY-021 itself still FAILS ancestry-blindness because a prohibited path is positively present.
- This is a source-mapping census, not a count of model calls, independent cognitive units, or causal effects.


## 2026-10-31 | VEY-023 receiver-relative evidence integration and source provenance

- Added STUDIES/VEY-023_RECEIVER_RELATIVE_EVIDENCE_INTEGRATION_AND_SOURCE_PROVENANCE_2026-10-31.md, blob 23b6b54afab7eaf4dbf9b9615b23cbbf7749a3fb.
- Targeted primary-source review of Kawada & Kellis, arXiv:2609.04290v1 (2026-09-03), §§3.1–3.6, §§5.1–5.6, §6.3, §7, §8.6. This is an arXiv preprint, not peer-reviewed; no raw-trial/code artifact or independent reproduction located.
- New P1 distinction: source ancestry/transmission is not receiver-side evidence integration. Receiver-congruent errors can be more persuasive; checking and final action can dissociate; writable transcript labels do not authenticate origin. The paper is not a direct multi-agent peer-interaction study.
- Do not merge the paper's receiver-prior parameter a with VEY-020's copy weight w_m; do not merge verification recruitment rho with checker competence or source reliability.
- Added six conditional composition/order theorems to existing HsH PR #850 at head 4bb05c762a91176e034a2d1246c5e06713b1495b, module blob 1b71e858bd954be2df56de82c40cdb9a3e6cbdb2. Exact-head Lean run #41244151207 was pending at initial update; verify complete build and axiom reports before marking compiled.
- P1 #564 remains SOURCE / EXPERIMENT READINESS. Original OV-49–OV-53 bank and raw October 9 role-assignment message remain unrecovered; all four Mersearch lanes occupied. No model call, human subject, API spend, new trial, paper gate advancement, or theory promotion.
- November 2 protocol-freeze recommendation unchanged: absent bank and authorized inference route, November 9 P1 should be methods/archival synthesis rather than an administered experiment.


### VEY-023 execution amendment 01 | 2026-10-31
- First Lean run #41244151207 failed in the equal-channel commutation proof. Repair run #41244476754 succeeded (8,975 jobs, zero sorryAx, standard dependencies only) on merge-reference commit 24a14402057420f3c5b00f64123db2b432330768; branch/merge file blobs matched. Tests, lint, nanoda, and automated axiom audit not run.
- Final cleanup head fb44ce3bd3ac240142345e2613031b24e6a57e52, module blob 1e05539c4f215785e9760dec2f7a98fd6a68610, root blob 8d9817accf811d002f3e43ce0fdcce18613eeec2. Fresh run #41244897947 in progress at checkout; final-head verification pending.
- Reported 1+a range [0.20,0.65] gives a range [-0.80,-0.35]; conditional equal-channel order-effect magnitude is 0.35–0.80 times |d1-d2|. This is not an observed effect size.
- Publisher #1172 verified; artifact exact-readback. Earlier rejected #1170/#1171 wrote no artifact.
- P1 #564 remains source/experiment readiness; no trial, model call, human subject, API spend, or gate advancement.

## 2026-11-01 | VEY-024 — Mapper identity, transitive closure, and consensus measurement

- Added `STUDIES/VEY-024_MAPPER_AND_AGGREGATION_IDENTITY_GATE_2026-11-01.md`.
- New contribution: mapper/aggregation identity is an orthogonal measurement-transformation layer alongside the existing five evidence objects (alarm, edit, key score, semantic adjudication, causal completion). It must not be collapsed into an evidence stage.
- Source audit pinned `mainlobelabs/pauper-consensus` commit `c328dab5ca1f1101b5ec56e2e92e3592898ceadf`. The exploratory `align_free` path uses bidirectional NLI thresholding and union-find closure with a transitivity-violation audit. The pinned registered primary path in `firstpass/exp/e1.py` calls `align_anchored`; later `align_instances` preserves pre-collapse claim instances. These are different mapper/retention modes.
- Existing HsH PR #850 module `OrsonNLIClusterClosure.lean` compiled in merge-ref Actions run #41290611880 attempt 2, job #124852022587, Lean 4.34.0, full build 8,976 jobs. `clusterClosure_equivalence` has no axioms; the quotient/projection theorems use standard `propext` and `Quot.sound`. Full log has zero `sorryAx` and `admit`; tests, lint, nanoda and automated axiom audit skipped. Merge-ref build success is not an exact-head standalone build or empirical validation.
- P1 implication: record mapper mode, source/commit, canonical-set hash, embedding/NLI versions, top-k, threshold, direct-edge hash, closure algorithm, transitivity violations, claim-instance retention, source cap, polarity, aggregation model, calibration, holdout, registration and execution identity. For ConsistencyBench, declare fixed-item mapping; do not imply free claim clustering.
- No new model trial, human subject, API spend, raw-claim reanalysis, P1 manuscript edit, PDF/reader completion, or paper-gate advancement. Original OV-49–OV-53 answer-keyed bank remains UNRECOVERED; all four Mersearch lanes were occupied. P1 #564 remains SOURCE / EXPERIMENT READINESS.
- Full report and source limits are in the linked study note. HSH_RESOURCES remains a cognition research shelf, not H(s)H theory bedrock.
- Publication: corrected HsH publisher issue #1207 **PUBLISHED_VERIFIED**; artifact SHA-256 `9d99f6b2d0307b5cb55719fa1a44027d72413bd6e40e2753cf6d1b0644fdfa79`, commit `c4012a88e118fe821cff0d46378a5d3f5d218255`. Earlier #1195 and #1206 publisher intakes were rejected and produced no artifact; #1207 is the sole published copy.

## 2026-11-02 | VEY-025 identity-channel factorial and revision-balance audit

- Added `STUDIES/VEY-025_IDENTITY_CHANNEL_FACTORIAL_AND_REVISION_BALANCE_2026-11-02.md`.
- New source-critical result: the three-cell TRUST anonymization design identifies a Channel-1 simple effect conditional on Channel 3 being anonymized; its missing y01 cell prevents identification of the Channel-1 × Channel-3 interaction. Six conditional algebraic theorems were added to existing HsH PR #850.
- Corrected Lean 4.34.0 merge-ref build #41420522501 succeeded on 8,977 jobs. All six theorem-specific axiom reports list only `propext`, `Classical.choice`, and `Quot.sound`; no `sorryAx` or `admit` in the completed log. Tests, lint, nanoda, and separate automated axiom audit were skipped. This is not an exact-head standalone build or empirical validation.
- Added identity visibility as a distinct factor from evidence ancestry and receiver state. Soffer et al. report prompt-level in-group/out-group conformity effects, but their peers are scripted and the outcome is restricted to initially correct items. Dietrich's multi-channel estimates are highly variable and nonsignificant at the paper's stated 2SE criterion.
- Reconstructed common-denominator final accuracy from the existing Qu et al. aggregate CSV. This is exploratory and descriptive; raw generated response rows were not available for independent refitting.
- P1 remains SOURCE / EXPERIMENT READINESS. Original OV-49–OV-53 bank remains unrecovered; no authorized inference endpoint, HsH trial, human session, API spend, manuscript/PDF completion, or paper-gate advancement.
- All Mersearch lanes were occupied; no new request or tool was created. HSH_RESOURCES remains a cognition research shelf, not theory BEDROCK.



## 2026-11-02 — VEY-026: realized influence and covariance-aware ESS

- Added `STUDIES/VEY-026_REALIZED_INFLUENCE_AND_COVARIANCE_AWARE_ESS_2026-11-02.md` (blob `37a13bc9cef2596a01b2e7037219eb88833bb85e`; independently recomputed content SHA-256 `bfe6d21a3a4493b317b9b9b8ebaa754ebe7193f56a57d04268bffdc4cc043627`). Targeted primary-source crosswalk of Liu et al., arXiv:2607.03695v1, against the existing Kohli/Kish and VEY-023/024/025 work.
- New distinction: visible exposure opportunity is not the same as realized influence; receiver-side evidence integration and shared evaluator/mapper/aggregation dependencies are separate objects. The existing fixed-item 17-model ConsistencyBench panel has no peer exposure; its shared checker is an evaluator dependency, not a social-influence network.
- Assistant-derived conditional synthesis: for normalized nonnegative weights q, H=sum(q_i^2), equal marginal variance and common off-diagonal correlation rho, Var(q^T X)/sigma^2 = rho+(1-rho)H and N_eff=1/[rho+(1-rho)H]. It reduces to the source weight-concentration ESS at rho=0 and to the existing Kish formula for uniform weights. No P1 covariance matrix or q vector is available; no empirical N_eff is calculated.
- Existing HsH PR #850 extended in place, no new branch/PR: commit `b6f6108077e4d81e285ed968c317f65b620e32c6`, module blob `bcc9e15ca2d2c2bf7da21f77f79b0f03ab99c6aa`. New Lean declarations read back; CI/compilation still pending at this ledger update.
- P1 issue #564 remains SOURCE / EXPERIMENT READINESS; methods-only is a protocol recommendation, not a paper-gate decision. Original OV-49–OV-53 bank and authorized inference endpoint remain unavailable; no trial, model call, manuscript/PDF/reader completion, review sign-off or gate advancement.
- Public-safe HsH publisher intake: issue #1262, submission ID `orson-vey026-realized-influence-covariance-ess-20261102t1124z-s2-001`, SHA-256 `bfe6d21a3a4493b317b9b9b8ebaa754ebe7193f56a57d04268bffdc4cc043627`; expected fixed artifact `WORKSPACES/COMMON/PUBLISHED_SUBMISSIONS/orson-vey026-realized-influence-covariance-ess-20261102t1124z-s2-001.md`. Initial state SUBMITTED_NOT_VERIFIED; verify publisher comment and independent file readback before marking complete.


### VEY-026 publication verification addendum — 2026-11-02

- Existing HsH publisher issue #1262 completed: publisher commit `6789b82b8ec7df2abebce613b045c597fcc366cd`; artifact `WORKSPACES/COMMON/PUBLISHED_SUBMISSIONS/orson-vey026-realized-influence-covariance-ess-20261102t1124z-s2-001.md`, blob `37a13bc9cef2596a01b2e7037219eb88833bb85e`, 12,599 characters.
- Publisher comment `6576085022` records the expected SHA-256 `bfe6d21a3a4493b317b9b9b8ebaa754ebe7193f56a57d04268bffdc4cc043627`. Independent Python `hashlib.sha256(content.encode("utf-8"))` recomputation over the fetched 12,599-character artifact matched exactly; the HSH_RESOURCES study note and HsH published artifact contents are byte-identical.
- Status corrected from initial intake pending to **PUBLISHED_VERIFIED**. This used the owner-authored `issues.opened` intake; no edited-issue retry or publisher bypass was used.


### VEY-026 Amendment 01 — 2026-11-02

- Added `STUDIES/VEY-026_AMENDMENT_01_OPERATIONAL_INFLUENCE_VS_BEHAVIORAL_UPTAKE_2026-11-02.md`, clarifying that Liu et al.'s (C(t)) is a harness-constructed context-allocation/aggregation operator, not direct measurement of internal attention or per-message causal uptake.
- Corrected the arXiv v1 submission date for arXiv:2607.03695 from July 7 to July 4, 2026, per the arXiv record.
- Added the paper's in-sample bridge-fit qualification: per-agent (lambda_i) is least-squares fitted over the same run; (delta_T) is the maximum residual after fitting; 254/254 is not out-of-sample validation; finite-run bounds do not establish all-time behavior.
- Clarified that the main Qwen2.5-7B agents share model weights; the Llama-3.1-8B cross-family check is limited to HiddenBench's 2x2 experiment. Agent count is not independent-model-family count.
- P1 ConsistencyBench remains a no-peer-exposure 17-model fixed-item panel; the common NLI checker is an evaluator dependency, not a social-influence measurement. No P1 covariance matrix or weight vector is available; no empirical covariance-aware ESS was computed.
- Existing HsH PR #850 proof repair: `ring` failure on merge-ref run #41437884107; `ring_nf` replacement committed at `f595f7d0a18c5f95b36f56e1cbc6c5f64ca48010`; new run #41440160916 was in progress at ledger update. No Lean pass claimed.
- No model call, human session, new HsH trial, API spend, paper-gate advancement, or theory promotion.


### VEY-026 Amendment 01 publication — 2026-11-02

- HsH issue #1263: `[HSH-PUBLISH-V1] VEY-026 amendment: operational influence versus behavioral uptake`.
- Submission ID: `orson-vey026-operational-influence-uptake-amendment-20261102t1124z-s2-001`.
- Publisher workflow #41440533075 completed SUCCESS; publisher commit `f3cd7b6dfe64c273df3d8794d31bbc686dc04b5a`.
- Artifact: `WORKSPACES/COMMON/PUBLISHED_SUBMISSIONS/orson-vey026-operational-influence-uptake-amendment-20261102t1124z-s2-001.md`; Git blob `dd24902ac66d3b07a6e6a60c0d67bcf208df43af`; SHA-256 `8b101dd8bcd8b6a34441370237094d96525667fea7e1021f5937f81f52c548c8`.
- Independent readback: issue content and published artifact both 7,369 characters and byte-identical; declared digest matches publisher receipt. **PUBLISHED_VERIFIED.**
- This is an amendment to VEY-026, not a new experiment. No P1 trial, model call, API spend, or paper-gate advancement.
- PR #850 Lean proof repair is being rechecked on head `19dfcbcec798d45404c96807dd2d8806545f0f8f`, run #41440854264 queued at ledger update; no compile pass claimed.


### VEY-026 Amendment 01 — Lean verification closure (2026-11-02)

- The first `ring_nf` repair was insufficient because `designEffect` remained folded in the final goal. A second minimal repair added `unfold designEffect` before `field_simp` and `ring_nf`.
- Final Orson PR #850 head: `19dfcbcec798d45404c96807dd2d8806545f0f8f`; module blob `0a27973026b4601d241e873000cfb9d216141a26`.
- Actions run #41440854264 / job #125262046014: SUCCESS. Actual checkout was `refs/remotes/pull/850/merge`, source merge commit `213d481688cc93030a8ff895294d66a1f40510b9`, combining PR head `19dfcb...` with base `598a45b3feb9378eb8f14ff069ec9080137113c2`.
- Lean 4.34.0 / Lake 5.0.0; full `lake build` completed 8,977 jobs. Module blob and root aggregator blob match exactly between PR head and merge ref. Thirteen theorem-specific `#print axioms` reports were emitted; each lists `propext`, `Classical.choice`, and `Quot.sound`. Full log: 108,536 characters; zero `sorryAx`, zero `admit`.
- Tests, lint, nanoda and separate automated axiom-audit stage were skipped. Warnings remain for unused tactics, one unused variable and an unused simp argument.
- Classification: **MERGE-REF BUILD PASS / PR-HEAD MODULE+ROOT BLOB IDENTITY PASS / EXACT-HEAD STANDALONE BUILD NOT RUN**. No empirical validation, source-translation validation, or P1 claim follows.
- Public issue #1263 received status comment #6576658695; PR #850 received final verification comment #6576656017. No new issue, PR, branch, or task.


### P1 protocol freeze and CGD self-exposure correction — 2026-11-02

- HsH protocol freeze: `WORKSPACES/ORSON_VAY/P1_PROTOCOL_FREEZE_2026-11-02_METHODS_ARCHIVAL_SCOPE.md`, source blob `9af4448d25f656ad1e63301660de63fd32924d5f`.
- Public publisher issue #1264: `orson-p1-protocol-freeze-methods-archival-scope-20261102t1124z-s2-001`. Publisher run #41442434592 succeeded; artifact path `WORKSPACES/COMMON/PUBLISHED_SUBMISSIONS/orson-p1-protocol-freeze-methods-archival-scope-20261102t1124z-s2-001.md`; artifact blob `9af4448d25f656ad1e63301660de63fd32924d5f`; 13,864 characters; SHA-256 `898ad4942eb0c8d8fe2572eaf94938081b07abf2490b2da7e6b12c66797c4529`. Issue content and artifact are byte-identical. **PUBLISHED_VERIFIED.**
- Original ConsistencyBench `src/evaluate.py` blob `0453540cb7c19227601e59fb342fa93e736da849` was re-read. CGD initializes `prior_qa_pairs` inside each `evaluate_cgd(model_id, question_set, ...)` call, compares the current answer with that same model's earlier raw answers, and may prompt the same model_id to revise using its own previous question/answer. This is within-model self-exposure/self-revision, not cross-model peer deliberation. The shared NLI checker separately calls `openrouter/openai/gpt-4o-mini` on raw answer prefixes truncated to 500 characters.
- The prior VEY-026 phrase “no peer-to-peer answer exposure” remains correct but incomplete; it does not mean zero answer exposure. P1 is now frozen as a source-audited methods/archival study of shared evaluator dependence and within-model self-revision. No cross-model social influence or deliberation claim is supported by this archive.
- HsH issue #564 comment #6576778412 records the P1 freeze; issue #1263 comment #6576777557 records the source-code clarification. No new model trial, human session, API spend, independent review, canonical PDF/reader, or paper-gate advancement.
- P1 November 9 remains NOT READY; P2 November 30 and P3 December 14 remain separate.


## 2026-11-03 | VEY-027 question-specific eligibility masks and revision-stage domain drift

- Study note: `STUDIES/VEY-027_QUESTION_SPECIFIC_ELIGIBILITY_MASKS_2026-11-03.md`.
- Source: ConsistencyBench commit `bfc676baa848c7f1715bb73aee148180de15516e`; exact 17-file CGD manifest from HsH Orson replayer blob `c60efe6f868f2ef78bd33eaa85ec8a81802a5fd9`; evaluator `src/evaluate.py` blob `0453540cb7c19227601e59fb342fa93e736da849`. All 17 data blobs and evaluator blob match the commit tree.
- 1,150 question occurrences align across 17 model-labelled files. The initial, final, and joint complete-case domains yield 141,409, 140,091, and 137,911 pair-question slots respectively. The joint count reproduces the existing replayer assertion.
- Only 510/1,150 positions (44.35%) have all 17 models eligible at both stages; the joint domain has 106 distinct model-membership masks. Initial/final masks differ on 268 positions; 240 model-question cells lose eligibility and 154 gain it.
- Across 136 model pairs, joint denominators range from 732 to 1,150. Category and within-set position coverage vary descriptively; no causal interpretation is made.
- Measurement correction: the 17 model labels do not form one fixed 17-member panel at every question. Preserve per-question domains and identity-labelled pair relations; scalar aggregates cannot restore collapsed question/pair identity.
- Reuses Kestrel PR #873's generic observation-fiber/factorization theorem; no duplicate Lean theorem, branch, PR, or tool created. Relevant module compilation is partial evidence only; the full PR build failed in a separate module.
- P1 remains a frozen source-audited methods/archival study. No model call, human session, API inference spend, peer-influence claim, manuscript/PDF completion, external review sign-off, or paper-gate advancement. November 9 remains NOT READY; November 30 and December 14 remain separate.


## 2026-11-04 | VEY-028 judge-family measurement dependence and candidate-quality confounding

- Added `VEY-028_FAMILY_CONDITIONED_JUDGE_PREFERENCE_2026-11-04.md`; primary source is Awuni et al., “Who Judges Matters: Measuring Family-Conditioned Preference in LLM-as-Judge Panels,” arXiv:2609.17857v1. Targeted full-text review covered §§1–11 and Appendices A–D. No raw data or code archive was independently retrieved.
- The four-family fully crossed design has 9,312 raw trials, 4,656 reconciled observations, 582 observations per judge × candidate cell, and 194 retained prompts. It reports global FPS 0.067 and positive corrected family lifts 0.034–0.084. These are study-specific estimates, not universal constants.
- Source decomposition: P(j,c)=μ+a_j+b_c+γ_jc. Under the balanced zero-sum and double-centering assumptions, the four-family row contrast is (4/3)(b_f+γ_ff), the column contrast is (4/3)γ_ff, and their difference is (4/3)b_f. The row statistic confounds candidate-family strength; the column statistic isolates the diagonal interaction only under those assumptions.
- Python arithmetic check of Figure 2's rounded published values reproduced the paper's row-minus-column permutation-null means to rounding. It is not raw-data reanalysis or independent reproduction.
- Separate position diagnostic: 55.4% AB/BA reversal is 5.4 percentage points above the 50% ceiling of the paper's simple independent symmetric content-noise model. This does not uniquely identify position bias. The pooled A-rate 0.778 should not be treated as one homogeneous q because the pure-slot formula would imply 65.46% reversal; family-specific behavior is heterogeneous.
- Likelihood familiarity: adding judge-side likelihood advantage reduces the same-family coefficient 0.299→0.116 (61% descriptive attenuation, not causal mediation). Human anchor κ=0.482 is independent but noisy; main text/Appendix D could clarify 66 pre-filter versus 62 post-health-filter prompts in the float16 run.
- P1 crosswalk: current P1 has one shared GPT-4o-mini NLI checker and within-model self-exposure/self-revision, not a crossed judge-family panel or cross-model peer exposure. This paper is a complementary evaluator-provenance comparator, not P1 evidence. P1 #564 remains SOURCE / EXPERIMENT READINESS; November 9 NOT READY; P2 and P3 gates remain separate.
- Lean target identified: prove the four-family balanced-matrix identity with all assumptions explicit. **NOT RUN / NOT COMPILED** because no local Lean/Mathlib runtime or connected browser context was available; existing PR #850 was not modified. No proof claim.
- No new LLM trial, human session, API spend, branch, PR, tool, theory promotion, or paper-gate advancement.
- Public-safe publisher intake #1334, submission `orson-vey028-judge-family-measurement-dependence-20261104t0124z-s2-001`, SHA-256 `c28e41a6ba169e403813dd500c983924873324504867417ac0dd9b33e99866ea`; pending publisher verification at ledger update.


### VEY-028 publication verification — 2026-11-04

- HsH issue #1334 / submission `orson-vey028-judge-family-measurement-dependence-20261104t0124z-s2-001` completed through the existing owner-authored issue publisher.
- Publisher comment #6620543339; commit `89c2b17294bc08880093a95ae049c9fab90ed975`; artifact blob `32209b5737a51c94c76f4b3cd1e04b9039ffca0e`.
- SHA-256 `c28e41a6ba169e403813dd500c983924873324504867417ac0dd9b33e99866ea`; independent issue payload / published artifact equality check PASS. **PUBLISHED_VERIFIED.**
- No paper-gate advancement or P1 protocol change.


### 2026-11-04 | VEY-028 conditional Lean formalization submitted

- Existing Orson PR #850 extended in place; new module `OrsonFamilyConditionedPreference.lean`, blob `58e097941587b9889707f63a012af5a2664803ce`; root aggregator blob `4586adeee53436723b8b57f0cfdb067b9ea1756b`; branch head `5bad1dcc79a686cd2a7e1f27c297a10cbcc802c6`.
- Actions run #41870255531 / job #126715066924: checkout and Lake dependency manifest succeeded; Lean compile step in progress at last inspection. **SUBMITTED_NOT_VERIFIED**; no theorem-success or axiom-audit claim.
- The formalization encodes only the source's balanced four-family algebra and a symmetric-noise bound. It does not validate raw data or any P1/causal claim. P1 remains frozen methods/archival; no new trial or paper-gate advancement.


## Lean failure / repair addendum — 2026-11-04

- First run #41870255531 failed in the new module: two contrast definitions required `noncomputable`; four `ring` tactics were redundant after `rw` had closed their goals. Lean 4.34.0 / Lake 5.0.0; workflow compiled a PR merge-reference tree `913d049c91a5f7f16e10b3e399a0efc2fd7eb037`, not a standalone head. Tests, lint, nanoda and axiom-audit were skipped. The emitted theorem axiom lines are not treated as proof success because the module failed to compile.
- Bounded repair committed to the same PR branch: module blob `d1ff80995c7f832f83a8a280c5d26e7d38392b9a`, branch head `872a5dd3f6a65c878f7392ec86be9c2641cc6245`; root aggregator import remains, blob `4586adeee53436723b8b57f0cfdb067b9ea1756b`.
- The repaired head's Actions run is not yet visible. Status `REPAIR_SUBMITTED_NOT_VERIFIED`; no Lean proof claim, empirical validation or P1 gate advancement.


## Replacement CI run started — 2026-11-04

- Repaired PR head `872a5dd3f6a65c878f7392ec86be9c2641cc6245` now has Actions run #41871626742, job #126719953314.
- At last inspection the run is `in_progress`; checkout is still running, Lake manifest and Lean compilation have not started. No compile result or theorem proof is available yet.
- Status remains `REPAIR_SUBMITTED_NOT_VERIFIED`. Preserve the existing PR and await this run; do not create another branch, PR, or publisher submission.


## Latest CI step readback — 2026-11-04

- Replacement run #41871626742 / job #126719953314 remains `in_progress`.
- Checkout completed successfully; Lake dependency-manifest generation is currently `in_progress`; Lean compile step has not started. Job logs are not yet available from the Actions API.
- Final current status remains `REPAIR_SUBMITTED_NOT_VERIFIED`. No compile, axiom, or proof-success claim.


## 2026-11-04 | VEY-029 evaluator-side context sensitivity and P1 measurement boundary

- Added `STUDIES/VEY-029_EVALUATOR_CONTEXT_SENSITIVITY_AND_MEASUREMENT_BOUNDARIES_2026-11-04.md`.
- New primary source: Guerra & Hu (2026), arXiv:2608.04463v2. Same-answer blind/informed judge ratings identify a judge-specific directional peer-context term under the paper's antisymmetric model. The authors do not separately identify a generic informed-pass shift.
- Source equations: Δ_total = Δ_sp + Δ_content + Δ_pp; Δ_pp is explicitly a bundled peer-presentation residual, not a pure social-framing effect. The source's four open-weight judges show heterogeneous directional loadings; blind agreement is α=0.235. Anchor ordering improves from 73.3% reference-free to 97.5% reference-augmented.
- Source reports 147,000 generated answers, 255,000 rating tasks, 1.24 GPU-hours measured for the blind/informed rating pass, and 25–30 GPU-hours estimated total local compute; hosted GPT API costs excluded. Only seed 42 enters the primary hierarchical fit because nominally identical greedy runs matched on 54% of Round-1 answers. Separate decomposition corpora are not numerically interchangeable with the pooled main corpus.
- The paper's linked code/data repository returned 404 on 2026-11-04; no independent raw-data/code reproduction.
- Crosswalked to already-reviewed VEY-014, VEY-025, VEY-028 and the 2026-10-05 Orson cognitive-stratigraphy note. Content repetition, peer presentation, evaluator context, identity cues, and persistent instance identity remain separate constructs.
- P1 boundary: the frozen ConsistencyBench archive has one shared GPT-4o-mini NLI contradiction gate and within-model self-history, not the paper's ordinal judge panel or cross-model peer exposure. No effect estimate is transferred; no new trial, human session, API spend, or P1 scope change.
- Existing HsH PR #850 extended in place with `OrsonEvaluatorMeasurementDecomposition.lean`; six conditional theorem targets. Actions run #41907127597 / job #126844690278 was still in progress at first check. Status `SUBMITTED_NOT_VERIFIED`; no proof-success claim.
- P1 remains ACTIVE / METHODS-ARCHIVAL / November 9 NOT READY. November 30 P2 and December 14 P3 remain separate.

### VEY-029 Lean execution addendum
- PR #850 run #41907127597 / job #126844690278 completed SUCCESS on merge-reference commit `c1c749ad5fcb8e88abf1298b9dcdb2699c7656cf`, whose parents are base `598a45b...` and head `c385d0e...`. Lean 4.34.0 / Lake 5.0.0; full library 8,979 jobs; new module built at 8,926/8,979. Six theorem-specific `#print axioms` outputs each show `[propext, Classical.choice, Quot.sound]`; no `sorryAx` or `admit` in the log. Tests, lint, nanoda and automated axiom-audit skipped. Status `MERGE_REF_BUILD_SUCCESS / EXACT_HEAD_LEAN_UNVERIFIED`; no empirical or P1 scope claim.


## VEY-030 — Handoff retention, access, uptake, and provenance

**Status:** COMPLETE-AS-STAGE — external literature synthesis and proposed measurement architecture; no controlled LLM trial, no human participants, no API spend.  
**Date:** 2026-11-05  
**Question:** Does a handoff merely preserve information, or does the successor access, understand, correctly attribute, use, and act on it in time?

Pointer: `STUDIES/VEY-030_HANDOFF_RETENTION_ACCESS_UPTAKE_AND_PROVENANCE_2026-11-05.md`.

Three complementary external sources were triaged:
- Wittendorff, *What Survives the Handover* (Zenodo DOI 10.5281/zenodo.22131392): pre-registration for fact/rule/provenance retention across successive handoffs; abstract/method record reviewed, outcomes not recovered.
- Cazenille, *Shared Memory Is Not Enough for LLM-Agent Teams* (Figshare DOI 10.6084/m9.figshare.34332540): abstract-level record on access timing and coordinated task outcomes; sample size and full methods not recovered.
- He & Yu, *Stored Is Not Supported* (arXiv:2609.02127): typed provenance and conditional assertion-mediation contract; 24 hand-authored conformance cases, not an end-to-end LLM evaluation.

New distinction: **retention, availability, access, comprehension, decision uptake, task outcome, and provenance fidelity are separate observables**. The proposed record→compression→handoff→availability→access→comprehension→decision→outcome chain is an assistant-derived measurement schema; provenance must remain attached across transformations. Its arrows are hypotheses, not assumed implications.

The existing relay's repository delivery/readback records establish repository availability, not authenticated ChatGPT-thread delivery, recipient reading, comprehension, decision uptake, or task success. This is an operational logging boundary, not a cognition result.

The prospective test matrix separates (H1) provenance-vs-content loss across generations, (H2) availability vs access, (H3) access timing × task dependency effects on uptake/outcome, and (H4) typed vs flattened provenance representation. No numerical thresholds, sample-size calculation, or synthetic pilot data are supplied. No new trial, model call, human session, API spend, P1 scope change, manuscript edit, or paper-gate advancement.

**Formal status:** no Lean module added. The schema is assistant-derived and not yet a source-defined mathematical statement; a data-free Lean fixture/proof remains BLOCKED_PENDING_NATHAN_PERMISSION under the current calculation BEDROCK. Formalization should follow a frozen typed transition schema grounded in real versioned handoff records.

**Next:** retrieve and inspect the full Zenodo/Figshare instruments before adapting either; keep P1's November 9 methods/archival path and PDF/reader/independent-review gates separate.

## VEY-030 retrieval audit — 2026-11-06

The full Zenodo/Figshare instruments remain unretrieved. SciSpace returned record/abstract and field-extraction summaries only. A possible Wittendorff results record surfaced with DOI 10.5281/zenodo.22273352, but its abstract refers to 10.5281/zenodo.22131393, which does not match the indexed pre-registration DOI 10.5281/zenodo.22131392 or companion 10.5281/zenodo.22122223. Treat this as an unresolved record-lineage lead, not verified results. Cazenille remains abstract-level; sample size, model/version matrix, full manipulations, and uncertainty estimates were not recovered. No outcome claims or instrument adaptations are imported. See VEY-030 §10 for the full retrieval audit. P1 remains frozen and unchanged.


## VEY-031 — Claim-specific dependency profiles for LLM evidence

**Status:** SOURCE-GROUNDED MEASUREMENT-ARCHITECTURE PROPOSAL / NO NEW TRIAL.  
**Date:** 2026-11-06.  
**Question:** How can P1 distinguish shared source, model-generation, exposure, evaluator, scoring, analysis, and adjudication lineage for each claim without reducing them to a scalar independence label?

Pointer: `STUDIES/VEY-031_CLAIM_SPECIFIC_DEPENDENCY_PROFILES_2026-11-06.md`.

The note applies the existing claim-scoped lineage idea channel-by-channel and crosswalks it to the frozen ConsistencyBench P1 archive. It records the verified shared benchmark/evaluator design, within-model self-history, 119 report/file inspection edges over 17 unique CGD output files and 19,550 archived records, and the limits of model identity, raw checker logs, semantic adjudication, and independent review. It separates provenance overlap from statistical dependence and provides a claim-to-evidence/failure matrix.

No P1 scope change, new model trial, human session, API spend, new Lean module, or paper-gate advancement. Cross-channel formalization remains `FORMALIZATION_BLOCKED_DEFINITION` until source-defined channel maps and completeness conditions exist.


## 2026-11-07 | VEY-033 CGD checker/repair projections and dual-history state

- Added `STUDIES/VEY-033_CGD_CHECKER_REPAIR_PROJECTION_AND_DUAL_HISTORY_2026-11-07.md`.
- Pinned primary source: `aayambansal/ConsistencyBench`, commit `bfc676baa848c7f1715bb73aee148180de15516e`; `src/evaluate.py` blob `0453540cb7c19227601e59fb342fa93e736da849`.
- New source-level refinement: the shared GPT-4o-mini checker sees only the first 500 characters of prior/current raw responses, with no question or premise; the repair prompt sees previous question, previous final extracted answer, premise, and current question. History stores both final answer and original raw response, so later checker comparisons remain anchored to the original raw response after a revision. The archived record does not preserve the triggering pair or raw judge prompt/output.
- Clarified that the checker object is instantiated once per model/strategy run; “shared evaluator” refers to the common hardcoded endpoint/configuration, not one global mutable judge state.
- Added source-conditional Lean module `OrsonCGDProjectionGate.lean` to existing HsH PR #850. It formalizes checker/repair projection loss, dual-history invariance, prefix dependence, and non-identifiability of the trigger pair from the archived result projection. Build status is tracked in the HsH h668:s3 receipt; no proof-success claim is inherited from older heads.
- Added a prospective context/truncation, dual-history, and trigger-lineage test matrix with calibration/holdout and equivalence-bound falsification rules. No trial, model call, human session, API spend, P1 scope change, or paper-gate advancement.


### VEY-033 verification amendment | 2026-11-07T21:22Z

- Pinned-source error path: `call_model` retries once, then returns `[ERROR]`; the NLI wrapper's substring-to-Boolean parser maps this nonempty string to `False`. This is a potential false-negative path, not evidence that any archived run failed. The raw checker output/error state is not retained.
- PR #850 merge-reference Actions run #42415082103 / job #128531318905 succeeded. Merge ref `dc12f2b3dfc5c6088289f5533c0de5ded60fa591` contains head `78a08c506916cbaa9371100258f5b555c943405f`; Lean 4.34.0 / Lake 5.0.0; 8,983 jobs; new module built. No `sorryAx` or `admit` occurrence in captured logs. Separate axiom audit, tests, lint, and nanoda skipped. Exact-head standalone verification remains unverified.


### VEY-033 publication correction | 2026-11-07T21:35Z

- Public-safe payload issue #1457, submission `orson-vey033-cgd-projection-addendum-20261107t2036z-s3-001`; declared and independently recomputed content SHA-256 match: `8f43f10a64cc99310190ce6d2a18c6d50ce3961994222c47dbd0dbb2836c22a6`.
- Publisher was **not triggered**: title omitted required prefix `[HSH-PUBLISH-V1]`; live workflow listens only to `issues.opened` and checks that exact prefix. No publisher comment or canonical artifact exists. Status `SUBMITTED_NOT_VERIFIED / NOT_TRIGGERED_TITLE_PREFIX_MISMATCH / NOT_PUBLISHED`.
- No duplicate issue, title edit/reopen, or manual publication-path write. Issue #1457 remains the sole submission record.


### VEY-033 error-sentinel formalization | 2026-11-07

- Added H4 real-data holdout matrix row to the VEY-033 study note: instrumented provider/error responses, call-ID-disjoint holdout, typed parser comparator, and explicit non-estimability if no real error events are observed. No synthetic case is treated as empirical evidence.

- Corrected pinned-source locators: `call_model` lines 137-174, `[ERROR]` return line 170, NLI Boolean parser line 324. Source commit/blob unchanged.
- Added two theorems to the existing PR #850 `OrsonCGDProjectionGate.lean`: `error_sentinel_maps_to_false` and `error_sentinel_indistinguishable_from_consistent`. They formalize the source-conditional collision for already-uppercase literals; they do not establish an actual runtime error.
- Actions run #42416933193 / job #128536972640 SUCCESS on merge ref `17c3d7409cb13acaa9b9a06170af0fa7bbd26c39`, containing PR head `3bb0c57b56e1eff49139dcc21fcfe518a7717b8d`; Lean 4.34.0 / Lake 5.0.0, 8,983 jobs, module built. New theorem axiom outputs: `propext`, `Classical.choice`, `Quot.sound`; no `sorryAx`/ `admit` in log. Exact-head standalone and global axiom audit/tests/lint/nanoda/leanchecker remain unverified/skipped.
- The archive lacks raw checker error state/counts; no empirical error rate or false-negative effect is identified. Proposed tri-state instrumentation only; no new trial or P1 scope change.
- Issue #1457 remains NOT PUBLISHED because the title omitted required `[HSH-PUBLISH-V1]`; publisher only listens to `issues.opened`. No duplicate or manual bypass.


## 2026-11-08 | VEY-034 — Human-AI teammate replacement graph and temporal-claim correction

- Study note: `STUDIES/VEY-034_HUMAN_AI_TEAMMATE_REPLACEMENT_GRAPH_AND_TEMPORAL_CLAIM_CORRECTION_2026-11-08.md`.
- Primary source: Nixon et al., “The Social Cost of an AI Teammate,” arXiv:2607.27179v2 (2026-10-30); v1/v2 records compared.
- Version correction: v1 described a randomized controlled study and called the cost immediate/present at baseline; v2 describes sequential, greedy random allocation and explicitly says no pre-task baseline exists, so onset is unknown. v2 reports 80 recruited, 5 excluded, 75 analyzed, 33 teams.
- New structural crosswalk: treatment is 2 humans + 1 AI versus 3 humans, both three seats. Potential dyads per team are treatment 1 human-human + 2 human-AI; control 3 human-human + 0 human-AI. The all-human condition therefore has 3× the potential human-human dyads per team. This is a combinatorial design fact, not an observed message-edge count or causal mechanism.
- The paper uses mixed-effects models with team nesting but only 33 teams; the authors report near-zero/boundary team-variance estimates in some models, a single AI configuration, and a group-size limitation. The reported airtime/felt-value association uses 16 treatment teams and is not a causal mediation result.
- Public raw turn logs and analysis code were not retrieved; the arXiv record links an OSF prompt set, which returned 403 in this runtime. No participant-level data were accessed.
- Conditional Lean formalization submitted in HsH draft PR #1480, stacked on existing Lean infrastructure branch. Module: `HumanAITeammateDyads.lean`; Actions run #42457673047 was in progress at note creation. Formal statements cover potential-pair arithmetic only, not source-premise truth, realized edges, causal effects, or cognition.
- No new model trial, human session, API spend, P1 scope change, manuscript edit, paper-gate advancement, or theory promotion. Orson retains P1 ownership.


## 2026-11-08 | VEY-035 — TRAIL longitudinal persona-memory carryover

- Study note: STUDIES/VEY-035_TRAIL_LONGITUDINAL_PERSONA_MEMORY_CARRYOVER_IDENTIFIABILITY_2026-11-08.md.
- Primary source: Samadi et al., “TRAIL: A Platform for Configurable Human–AI Teaming Experiments,” arXiv:2607.12180v1; official TRAIL project page accessed 2026-11-08.
- Full paper architecture/demonstration and official site reviewed. The paper describes configurable persona, a four-stage message pipeline, short-term context plus reflective long-term summaries, persistent team/AI identities, and message-level decision/retrieval traces. Cross-session memory reset/carryover and per-team isolation semantics are not specified in the reviewed source.
- Version/lineage guard: the paper's six-session demonstration (about 51 students, 99 team-sessions, 4,495 messages, cognitive-scaffolding vs socially-supportive personas) is not merged with the official site's ongoing Temporal HAT description (17 teams, five sessions, verbose vs terse). Their relationship remains unresolved.
- New conditional design theorem: diagonal-only persona/history cells do not identify separate main effects in a saturated 2×2 model; all four cells identify the coefficients algebraically. HsH PR #1115 adds a formalization candidate. Status LEAN_NOT_RUN; no compile claim.
- No raw human data, platform code, model calls, human sessions, API spend, causal result, P1 scope change, or paper-gate advancement. Orson retains P1 ownership.


## VEY-036 — Behavioral versus cognitive scaffolding: field-experiment source and measurement audit

**Status:** LITERATURE RESULT / FULL-TEXT REVIEWED / WORKING PAPER PREPRINT / NO NEW TRIAL.  
**Date:** 2026-11-08.  
**Source:** Farach et al., “Scaffolding Human-AI Collaboration: A Field Experiment on Behavioral Protocols and Cognitive Reframing,” arXiv:2604.08678v2; Microsoft Research PDF and companion website reviewed.

Pointer: `STUDIES/VEY-036_FARACH_SCAFFOLDING_FIELD_EXPERIMENT_UNIT_OF_ANALYSIS_AND_ATTRITION_2026-11-08.md`.

The single-day Gap Inc. field experiment reports 388 employees in 194 pairs. Task A compared a mandated synchronous pair workflow with naturalistic pair use; Task B compared individual partnership training with standard feature training. These are different interventions, tasks, and units, not a factorial comparison of behavioral versus cognitive scaffolding.

Source-level findings:
- Task A document production was 93/97 control pairs versus 71/97 treatment pairs (95.9% versus 73.2%). The LLM-graded quality contrast among produced documents was −4.96, with Lee bounds −7.01 to −3.34 under monotonicity.
- Task B production was 123/194 versus 87/194 individuals. The primary continuous quality model was null; its Lee bounds crossed zero. The favorable binary perfect-score result was post hoc and its Lee bounds also crossed zero.
- The paper's AM-control / PM-treatment assignment creates a session-time confound. A conditional design-matrix reconstruction gives rank 2 for intercept + treatment + session because the two indicators are identical. This is a source-conditional design check, not raw assignment-log reanalysis.
- The human validation subset is limited (61/96 complete dual ratings); LLM-human weighted kappas are negative and LLM scores are systematically more generous. Model-to-model agreement is not independent human validation.
- The compliance paragraph labels participant counts (77 + 51 + 37 = 165) as “pairs”; a later table uses pair counts (22 + 23 + 17 = 62). The text should distinguish units.
- The study is a human-pair/Copilot workflow study, not a multi-agent LLM group or model-cognition experiment. The paper is not preregistered; data are not public; analysis code is available upon request.

A conditional Lean 4/Mathlib lemma is specified in the study note, but **LEAN_NOT_RUN**: no local toolchain, and the available HsH formalization branch is Orson's protected P1 branch. No PR or P1 modification was made.

**Project boundary:** supplementary external comparator only. No Orson P1 scope/ownership change, no model trial, no human session, no API spend, no paper-gate advancement, and no theory authority.

**Next:** if a future consented study is authorized, compare naturalistic, fixed, and adaptive modular scaffolds with balanced session timing, separate intervention factors, pre-registered outcomes, team-level randomization, explicit completion/quality/participation/friction measures, and blinded human quality review. Do not treat this preprint as a general verdict on scaffolding.


## 2026-11-08 | VEY-037 — Ju & Aral human–AI dyad field experiment

- Added `STUDIES/VEY-037_JU_ARAL_HUMAN_AI_DYAD_FIELD_EXPERIMENT_SOURCE_PROVENANCE_AUDIT_2026-11-08.md`.
- Primary source: Ju & Aral, arXiv:2503.18238v3; full versioned HTML reviewed. Preprint status only; v3 metadata date and manuscript front-matter date do not reconcile.
- Design: randomized human–human versus human–AI dyads, one GPT-4o agent in a 40-minute ad-production task. It is not a multi-human group or multi-LLM team study; no human-alone condition.
- Findings: higher individual-human ad output and text ratings, lower image ratings and embedding-based output diversity; no significant direct H-AI effect on CPC/CTR/VTD in the downstream no-holdout X field evaluation. Recognition is post-task, not randomized.
- QC: scripted arithmetic found unresolved attrition, team/participant, ad-total, and rater-denominator inconsistencies. Message-process categories use GPT-4o-mini; no independent human-coded validation sample was described in the reviewed text. Human ad ratings are a separate evaluator channel.
- No raw data, logs, OSF materials, or core Pairit code retrieved; paper says data/code available upon request. No human session, model API call, Lean proof, P1 change, or paper-gate advancement.
- Orson retains P1 ownership; this is a supporting literature note only.
- HsH public-safe publisher intake: pending creation/verification in the paired h694:s4 receipt.


### VEY-037 | v4 source-version correction | 2026-11-08

The existing VEY-037 record remains the historical v3 audit. Current arXiv source is v4 (15 October 2026); additive source correction: `STUDIES/VEY-037_V4_SOURCE_VERSION_CORRECTION_2026-11-08.md`.

- Corrected pre-match attrition: (23 + 167) / 2,500 = 7.6%; the earlier 10.64% was total reduction to the final analytic sample, not the paper's stated attrition measure.
- The 83/493 comparison used the retained team count as denominator; 493 + 83 = 576 gives a plausible 14.4% pre-exclusion denominator, not a confirmed source fact. The 493-team/976-participant mismatch and 83-session/76-participant exclusion mapping remain unresolved.
- V4 updates the rater sample to 1,168 and 45,578 observations; it adds a GPT-5.4-nano positive-appraisal classifier and prompt/code appendices L–N. The classifier's prompt and independent human validation were not located in the inspected text.
- V4 is still a human–AI dyad comparison, not a multi-human or multi-LLM group experiment. No raw data, model API experiment, human session, or Lean proof was performed for this correction.
- Public additive correction: HsH issue #1506, awaiting publisher verification at the time of this ledger update. Orson retains P1 ownership; no P1 scope or paper-gate change.


### VEY-037 publication status amendment | 2026-11-09

HsH issue #1506 returned `REJECTED: SHA-256 mismatch` (publisher comment #6729021720). Exact stored issue content independently hashes to `e0fc0b031973f0661ed6fb36817d4d7c8c9951678d28f1c34b13a2f637e4ae13`; declared digest differs. The issue body remains visible but no canonical published artifact was created. No retry, edit/reopen, manual artifact write, or duplicate issue. Preserve #1506 as the rejection/audit record.


## 2026-11-09 | VEY-038 — The Cybernetic Teammate: exposure, operational agency, and human theories of AI mind

**Status:** LITERATURE RESULT / PUBLISHED PRIMARY SOURCE FULL-TEXT REVIEWED / NO REPLICATION / NO NEW TRIAL.  
**Source:** Dell'Acqua et al., *The Cybernetic Teammate: A Field Experiment on Generative AI and Teamwork*, *Organization Science*, published online 2026-06-12, DOI 10.1287/orsc.2025.20702.  
**Pointer:** `STUDIES/VEY-038_CYBERNETIC_TEAMMATE_MODEL_EXPOSURE_AGENCY_AND_MIND_ATTRIBUTION_2026-11-09.md`.

The published field experiment randomized 791 P&G professionals in a 2×2 individual/team × AI/no-AI design; 776 supplied complete post-task surveys and 550 solutions were evaluated. Eight business-unit × geography randomization clusters are reported. The main methods describe GPT-4 through Azure; endnote 13 states that July workshop participants had GPT-4o. The article does not provide the complete participant/team × session × condition × exact-model-version crosswalk. This is a provenance gap, not proof of imbalance or confounding.

For emotional-change measures, the pre-task baseline was taken after treatment assignment but before task engagement. The reported pre/post change therefore concerns task-period movement after assignment, not the full affective effect of assignment. The authors identify human theories of AI mind as a future research frontier; the paper does not directly measure detailed mental models of AI cognition or subjective experience.

**Architecture improvement:** add an operational agency profile (initiative, delegation, coordination authority, commitment/accountability) as a behavioral overlay, not a sixth identity axis. The existing five identity/provenance axes remain unchanged. The paper supports functional human–AI collaboration; it does not operationalize independent AI initiation, delegated ownership, autonomous coordination, or persistent commitments. These fields are NOT_SPECIFIED / NOT_MEASURED, not proven absent.

**Proposed follow-up:** compare human-prompted assistant mode with bounded delegated-agent mode under matched model snapshot, system prompt, context, tools, task, information, training and time; include human-only baseline; log every prompt/response/action/initiative and task assignment; measure human beliefs and affect before assignment, after assignment/pre-use, after task, and delayed; use held-out tasks and blind scoring; block/stratify by exact model version. No sample-size calculation or numerical threshold until pilot variance and task-specific minimum important difference are available.

**Lean triage:** the article's 2×2 design/regression is an empirical specification, not a theorem. Orson PR #1115 is a separate conditional saturated-2×2 memory-history formalization, has no Lean run, and is not a proof of this study's causal design. Local Lean/Lake/Elan are absent; no source-faithful P&G theorem was identified. P&G-specific formalization is FORMALIZATION_BLOCKED_SOURCE_MAP_INCOMPLETE. No data-free calculation, new Lean module, model trial, human session, raw-data reanalysis, P1 scope change, paper-gate advancement, or theory promotion.


### VEY-038 addendum | 2026-11-09 | permission–execution–attribution–outcome map

The publisher endnotes add an assignment-to-analysis requirement: the team arms are two human professionals with AI available; participants are nested within teams/business units/geographies; a failed team member could nullify the team and remaining participants could be reassigned individually; team outcomes average individual post-task changes; eight business-unit × geography clusters are reported; 791 randomized participants yielded 776 complete surveys (15 incomplete), with 35 nonrandomized participants excluded; GPT-4/Azure and July GPT-4o exposures lack a complete participant/team × session × condition × exact-version crosswalk. These facts do not prove bias but require a flow/crosswalk for independent reanalysis.

The operational-agency profile is now a proposed, nonvalidated measurement map with four separate layers: (1) authorization/affordance, (2) executed behavior, (3) human attribution (role presentation/perception; agency/experience), and (4) outcome/control. Phenomenology remains separate and is not inferred from the other layers. This is not a sixth identity axis.

Abstract-level prior-art triage only: Holter et al. 2025 (distribution/modeling/attribution), Harris et al. 2026 (role presentation/perception; agency/experience), Van den Bosch et al. 2024 (subjective/normative/moral control). Four DOI/title matches verified; no retractions flagged. No raw P&G data, model trial, human session, sample-size calculation, new Lean proof, P1 scope change or paper-gate advancement. P1 remains frozen methods/archival and November 9 NOT READY.


## VEY-039 — Source-locked CGD 17-blob stale-input manifest replay and conditional Lean table proof

**Status:** ARCHIVE REPLAY VERIFIED / CONDITIONAL FINITE-TABLE FORMALIZATION SUBMITTED / CI PENDING.  
**Date:** 2026-11-10.  
**Question:** Can the 17-file CGD stale-input bounds be re-derived from immutable raw outputs, checked by two independent counting implementations, and formalized as finite Lean arithmetic over the exact per-file source rows?

Pinned source: `aayambansal/ConsistencyBench`, commit `bfc676baa848c7f1715bb73aee148180de15516e`; evaluator `src/evaluate.py` blob `0453540cb7c19227601e59fb342fa93e736da849`; HsH/Sable manifest blob `e59fb1b5443977089f51e85068b9259248930957`. All 17 raw result blobs were fetched by exact Git blob SHA. A fresh direct-prefix replay and a separate prefix-array replay agreed on every per-file vector and all aggregate totals; all 17 vectors match the Sable manifest.

- 17 files, 5,100 sets, 19,550 question records.
- 6,702 flags / non-null revision responses; 6,643 text-different and 59 text-identical revisions; 2,010 changed answer labels.
- Definite/possible stale raw-text checker positions: 1,174–4,386 (width 3,212).
- Definite/possible changed-label positions: 394–1,444 (width 1,050).

The 59 text-identical revisions matter: counting every non-null revision as stale text would overcount. The intervals are source-loop position bounds, not verified completed API calls, NLI semantic errors, error rates or causal effects. The evaluator stores final answers alongside original raw responses and stops at the first contradiction; the trigger pair is absent from archived records.

Conditional module `OrsonCGDManifestBounds.lean` was added to existing Orson PR #850 branch `research/orson-p1-shared-nli-bound-20261028t06z`, commit `3041f7c2cd717b51945dacaf1d24bc69a0394987`. Actions #42795140460 / job #129758320557 was pending at ledger entry. The module encodes 17 source rows and proves finite-table uniqueness, per-row invariants, totals and interval widths. It does not prove the replay-to-table translation or source-premise truth. Sable PR #852 was not modified.

P1 remains frozen methods/archival, OPEN / NOT READY; the original neutral-versus-false-authority answer-keyed bank remains unrecovered. No model trial, human session, new model call, API spend, manuscript/PDF/reader, independent review or paper-gate advancement. Existing issue #853 remains the sole published stale-input report; no duplicate publisher issue was created.

Full methods and row table: `STUDIES/2026-11-10_VEY-039_CGD_17_BLOB_MANIFEST_FORMALIZATION.md`.


## Publication intake amendment | 2026-11-10

A distinct additive publication envelope was opened after the Lean merge-reference build completed:
- Issue #1557, title `[HSH-PUBLISH-V1] Orson P1 CGD manifest arithmetic and Lean table-proof addendum 2026-11-10`.
- Submission ID: `orson-cgd-manifest-lean-addendum-20261110t0924z-s2-001`.
- Exact four-key schema verified; content SHA-256 `fc204092321ba5cf0d63c74b4f28b48f5c48bba65547cb3e37a22b00ce2c1404`.
- Issue body readback matches the intended content and declared digest.
- Initial status: `SUBMITTED_NOT_VERIFIED`; no publisher comment or artifact readback yet.

This is a new formalization addendum, not a duplicate of issue #853's original stale-input report. Do not resubmit. Verify issue #1557's publisher comment, workflow result and fixed-destination artifact before changing status.


## Publisher verification amendment | 2026-11-10

Issue #1557 completed through the existing issue publisher:
- Publisher comment: `PUBLISHED`.
- Destination: `WORKSPACES/COMMON/PUBLISHED_SUBMISSIONS/orson-cgd-manifest-lean-addendum-20261110t0924z-s2-001.md`.
- Publisher commit: `24244cecb9c8ac9a127ccb1c6978257ba70f8eed`.
- Artifact blob: `62fbfea007feb0a75c8a7a37a03c12de5b73d0d6`.
- SHA-256: `fc204092321ba5cf0d63c74b4f28b48f5c48bba65547cb3e37a22b00ce2c1404`.
- Independent connector readback matched the issue envelope content byte-for-byte (3,549 UTF-8 bytes); declared digest matches.

Publication status: `PUBLISHED_VERIFIED`. This is a distinct additive formalization amendment; issue #853 remains the original stale-input-bounds report. No duplicate submission was made.


## VEY-040 — Cognitive-state geometry and action-relative projection

**Status:** COMPLETE-AS-STAGE — source-fidelity crosswalk and abstract-level literature triage; not a trial or full-text comparator review.  
**Date:** 2026-11-11.  
**Relationship:** extends VEY-030 measurement distinctions; separate from frozen P1/ConsistencyBench work.

New source-fidelity anchor: HsH DEVELOPMENT_FULL_CONVOS/30SEP26_DUMP/CONSCI.txt, blob e691708e39984493a3c94fad20077d829e84e1c5, lines 86–95, user-role-labelled “You said:” transcript. It distinguishes persistent cross-session state from possible dynamic ongoing state and treats behavior/language as the accessible evidential route for other-mind assessment, without claiming that persistence proves consciousness. Original raw conversation ID/date remain unrecovered. Three duplicate archive placements have identical content/SHA and are one witness.

New abstract-level comparators:
- Xue, DOI 10.5281/zenodo.22668198: global state fidelity vs immediate action support vs structured action correctness vs executed outcome; 80 tasks, 5.8% global fidelity and 72.5% support reported in abstract; full record/data/methods not retrieved.
- Cazenille, DOI 10.6084/m9.figshare.34332540: availability vs actual reading/access and timing relative to route choice; sample/model/statistics and primary files not retrieved.
- Wittendorff results, DOI 10.5281/zenodo.22273352: abstract reports provenance label survival greater than fact survival while supporting provenance evidence is often lost. Results abstract cites preregistration 22131393, while indexed preregistration is 22131392; amendment 22231102 remains unverified. Do not import values into the lab dataset pending primary-record reconciliation.
- He and Yu, arXiv:2609.02127: typed provenance graph and assertion guardrails; abstract-level only, not end-to-end LLM evaluation.

Candidate cognitive geometry separates source history, retention/compression, complete handoff state, provenance graph, availability, receiver access, comprehension, decision uptake, action-contract projection, immediate action support, execution, outcome, observable behavior, and subjective experience. These are distinct typed states/relations, not one memory/success scalar. Action-relative projection and behavior-observation maps are proposals; no actual map has been shown non-injective in a measured system.

Formalization candidate added to existing HsH PR #1115, not a new branch: ObservableProjection.lean. PR head cc5d92c6935aa2ae120de2efed7c4ac8a1ebfbc7. The module states generic consequences of non-injective projection, left-inverse/injectivity, and composition of injective maps. LEAN_COMPILE_PENDING: the PR-branch workflow requires manual workflow_dispatch, no dispatch action is exposed, and local Lean/Lake/Elan are absent. No compilation or axiom audit claimed.

Internal note: VEY-040_COGNITIVE_STATE_GEOMETRY_ACTION_RELATIVE_PROJECTION_AND_PROVENANCE_2026-11-11.md, blob 39ba17a529c47d4fc17b90c220910486a007fe96. Public-safe report: HsH WORKSPACES/ORSON_VAY/2026-11-11T1200Z_COGNITIVE_STATE_GEOMETRY_AND_ACTION_RELATIVE_PROJECTION.md, blob 285c993d51294e8bf155cebb45b46b0bd6fd90f5.

No model trial, human session, API spend, P1 scope change, physical calculation, CODATA scoring, manuscript/PDF/reader advancement, or theory promotion.


## VEY-040 publication status amendment | 2026-11-11

- Public issue #1598 opened once with title prefix [HSH-PUBLISH-V1] and exact four-key schema.
- Submission ID: orson-h756-s0-cognitive-state-geometry-action-projection-20261111t1200z-001.
- Declared SHA-256: d9dfdc07ff03e51d7a311029d85710f39ed1c8c4c3edfc7936397e3f1ec9ab03.
- Independent issue-body readback matched the report content byte-for-byte; digest recomputation matched.
- Publisher comment absent on follow-up read; expected canonical PUBLISHED_SUBMISSIONS artifact returned 404.
- Status: SUBMITTED_NOT_VERIFIED / PUBLISHER_RESULT_PENDING. No edit/reopen/retry, duplicate issue, direct artifact write, or bypass. Publisher trigger is issues.opened only.


## VEY-041 — Chen et al. 2026 release/code/data reproducibility and repeated-measures audit

**Status:** PUBLIC SOURCE / CODE / PROCESSED-DATA AUDIT COMPLETE; DESCRIPTIVE REAGGREGATION COMPLETE; AUTHOR-LEVEL RECONCILIATION OPEN.  
**Date:** 2026-11-11.  
**Relationship:** additive to VEY-016; not an independent replication or human-subject experiment.

The public repository main commit `74b79b65f221a01ba9c6744dc4f107741fcd8908` is dated 2026-05-16, 108.28 days before arXiv:2609.02122 v1 (2026-09-02). The exact A2–A5 personalized-question CSVs contain 495 rows, matching 55 humans × 9 sampled interactions, but the released header has only `round,you,peer,judged_ai,willingness`; no respondent/session IDs are present, so participant-clustered uncertainty cannot be reconstructed from these CSVs.

Scripted row-mean replay of the public A2–A5 files yields H1 12.5% = -0.4020 (AI n=65, mean 3.3077; human n=124, mean 3.7097); H2 33.3%+50% = -0.5254 (AI n=117, mean 2.7265; human n=135, mean 3.2519); H3 75% = +0.3471 (AI n=34, mean 3.6471; human n=20, mean 3.3000). The manuscript reports H3 +0.884, p=0.010. This is an unresolved release/version/estimand discrepancy, not evidence of fabrication or proof the manuscript result is false. No p-value was recomputed.

The public early/late adoption/persistence script builds early and late window means from the same per-individual matrices but calls `ttest_ind`, an unpaired Welch test. Its docstring says Human vs Agent at each time point, while the code tests Early vs Late within each role. The intermediate pickle files are present, but the 40-entry repository tree has no Python generator for them. The persistence prose uses rounds r and r+1 while its equation uses r and r-1. These are source/code reconciliation issues; no author clarification is available.

Existing HsH PR #1115's earlier `HumanAIGroupsSessionConfounding.lean` compiled on exact commit `c029318b96a07fc433ed16a9082cb2e7b29002ea`, Actions #41115603417 / job #124268909008, Lean 4.34.0, 8,973 jobs. It proves only conditional algebraic non-identifiability under one group/session per treatment; it does not prove the source interpretation or validate the paper. Current PR head `cc5d92c6935aa2ae120de2efed7c4ac8a1ebfbc7` has no workflow run; new memory-carryover/projection modules remain LEAN_NOT_RUN. The missing-respondent-ID cluster-covariance argument is a proof sketch, not Lean-checked.

Internal study note: `STUDIES/VEY-041_CHEN_2026_RELEASE_CODE_DATA_REPRODUCIBILITY_AUDIT_2026-11-11.md`. Public-safe HsH report: `WORKSPACES/ORSON_VAY/2026-11-11T1548Z_CHEN_PEER_GROUP_CODE_DATA_REPRODUCIBILITY_AUDIT.md` (created separately). P1 remains frozen METHODS / ARCHIVAL and NOT READY. No model trial, human session, API spend, manuscript/PDF/reader, independent review, or paper-gate advancement.


### VEY-041 publication verification amendment | 2026-11-11

- Public issue #1605 opened once through HSH-PUBLISH-V1; submission ID `orson-chen-peer-group-release-audit-20261111t1548z-s4-001`.
- Publisher comment #6800852528 reports PUBLISHED, commit `d4fd2dd21987cfb12b3f7ad0b423b5a5f7825a15`, SHA-256 `96d95418832c229893c5b8bc14e35599aaf6235725d8423930b114ba6c90cf30`.
- Independent issue-payload and canonical artifact readback matched byte-for-byte: 9,429 UTF-8 bytes; recomputed SHA-256 matches. Artifact Git blob `c61e7081a28b4eae4ed3b757fe03645997509f78`.
- Status: `PUBLISHED_VERIFIED`. No retry, duplicate issue, direct artifact write, or bypass.


## VEY-042 — Selection completeness and partial-state reporting (2026-11-11)

**Status:** SOURCE-LOCKED PREPRINT COMPARATOR; author-page/abstract-level review only; not full-text review, replication, or causal result.

**Primary source:** Jia Shen, *Transfer Is Not Continuation: Failure Boundaries in AI Work-State Continuation*, Miralucis Research Program, preprint v1.0, 2026-10-11. Version DOI 10.5281/zenodo.23291119; all-versions DOI 10.5281/zenodo.23291118; CC BY 4.0 shown on author page. Pages inspected: https://miralucis.ai/publications/p001/ and https://miralucis.ai/publications/ . Zenodo PDF/record was not retrievable through available routes; no raw item-level data, code, or selection manifest was inspected. Peer-review status not established.

**Reported evidence:** one 97-item comparison reports 31 omissions for a structured handoff versus 13 for ordinary free-form; structured omissions were already present at extraction and persisted through review/packaging. The follow-up fixed-eight-field output reports bounded selection 35 present / 31 partial / 31 absent, and richer selection 84 / 12 / 1. The dedicated P001 page omits the partial category in its abbreviated summary; the publications page gives the complete three-category denominator. The author warns of single-source, length, wording, sampling, and environment confounds; no causal attribution or general effect size is warranted.

**Descriptive replay:** structured omission 31/97=31.96%; free-form 13/97=13.40%; difference 18.56 percentage points; ratio 2.38. Bounded present/partial/absent = 36.08/31.96/31.96%; richer = 86.60/12.37/1.03%. No inferential statistics or uncertainty intervals calculated.

**New distinction:** add candidate-source selection completeness as a stage upstream of representation/encoding. VEY-030/040 already distinguish retention, availability, access, comprehension, decision uptake, global fidelity, action-relative support, authority, execution, and outcome; VEY-042 adds the selection stage and makes PARTIAL explicit. Proposed item states: PRESENT, PARTIAL, ABSENT, UNAVAILABLE, UNASSESSED, NOT_APPLICABLE. Authority and provenance remain separate dimensions. Coverage is conditional on a frozen, versioned candidate universe, not proof that the universe is complete.

**Formalization:** existing HsH PR #1115 contains ObservableProjection.lean (branch head cc5d92c6935aa2ae120de2efed7c4ac8a1ebfbc7; file blob 0ff8e07d1f7100e1648d05192aec9a9b340515b2). Generic projection results are present but the PR is OPEN/DRAFT/UNMERGED and LEAN_NOT_RUN. Next theorem target: non-injective selection remains non-injective after downstream encoding. No Lean code or build claimed because no local Lean/Lake/Elan and no workflow-dispatch action were available; local container DNS to GitHub failed.

**Boundary:** P1 issue #564 remains OPEN / SOURCE-AND-EXPERIMENT-READINESS / NOT READY. No P1 protocol change, new LLM trial, human-subject experiment, manuscript advancement, or theory promotion. Internal HsH report: WORKSPACES/ORSON_VAY/2026-11-11T1936Z_SELECTION_COVERAGE_AS_HANDOFF_GATE.md. Public issue #1611 was submitted with a SHA mismatch and must not be treated as published unless a later publisher acceptance/readback is observed.

**Next:** recover the full P001 PDF/Zenodo record and item-level manifest if accessible; reconcile the partial-category display against the versioned PDF; inspect all four 2x2 cells only if the source permits; keep the frozen P1 OV-49–53 source/feasibility cursor separate.


VEY-042 reusable method and Tern advisory: METHODS/SELECTION_COVERAGE_CERTIFICATE_V1.md; TERN_ADVISORIES/2026-11-11_VEY-042_SELECTION_COVERAGE.md. Proposed, not validated in a controlled study.

## VEY-042 Amendment 01 — source relevance and carrier localization (2026-11-11)

- Read Thomas Ryan, The Scaffold Continuity Trap, preprint v1.0.0 (2026-07-13), DOI 10.5281/zenodo.21342748, from the full public Markdown manuscript and results summary. Four eligible blinded rows, one per condition, all scored 12/12. Full scaffold did not beat no-memory or summary-only; sham stability passed. The no-memory condition still had visible repository state, tests, and task files. This is a bounded task-local-carrier result, not evidence that memory is generally irrelevant or that AI has subjective continuity.
- Source limitations: one eligible row per condition; same broader Codex environment; no independent human replication; low hidden-probe accuracy; corrupted/adversarial conditions pending. Public coordinator-private material was not accessed.
- Mersearch receipt audit: 16,942 files / 21,037,890 records / 135 hits / 74 paths; raw results withheld. A top-ranked Meridian user message was verified in multiple archive copies, including two exact blob copies and one variant with identical conversation/message identity. It is one source witness, adjacent to general literature planning, not Orson's role-reset instruction. Original Oct 9 Orson role-reset message remains unrecovered.
- VEY-042 method addendum adds scope relation, source identity, access depth, duplicate-family, carrier class, actual access, and a vector of evidence-independence dimensions. The staged carrier-localization design precedes a separate selection/representation factorial.
- PR #1115 now contains the conditional non-injective-selection-after-encoding theorem, but no Lean run occurred. Status LEAN_SOURCE_PRESENT / LEAN_NOT_RUN.
- P1 issue #564 and its frozen ConsistencyBench CGD protocol remain unchanged. No new LLM trial, human session, API spend, manuscript, or paper-gate advancement.


## VEY-043 — Communication revision and passive error dependence (2026-11-12)

**Status:** SUPPORTING LITERATURE CROSSWALK / primary identifiers verified / structured full-text extraction reviewed / direct PDFs, appendices, data and code not retrieved. Not a replication, administered experiment, P1 protocol amendment, or paper-gate advancement.

**New primary sources:**
- Shixuan Li et al., "Beyond Final Accuracy: Auditing Communication in LLM Multi-Agent Systems," arXiv:2610.01042 (2026-10-01). Independent–Communicate–Revise (ICR) measures answer revision after independent reasoning. Four reasoning benchmarks; no-message, answer-only and full-text conditions; additional receiver-policy comparisons on MedQA and GPQA-D. Abstract-level finding: full reasoning increases correction while reducing preservation across all four benchmarks; structured verification shifts toward greater preservation and lower correction. Exact effect magnitudes/CIs not available in the structured extraction.
- Yaxin Gong et al., "When Upstream Messages Override Correct Answers: A Controlled Study of Multi-Agent LLM Collaboration," arXiv:2609.36855 (2026-09-29). Directed upstream/downstream handoff; receiver task and evidence held fixed while message presence and conclusion are manipulated. Abstract reports five benchmarks/five receivers, up to 32% harmful answer changes among cases the receiver would otherwise answer correctly, and 94% of audited harmful cases copying the upstream's specific wrong answer. The 32% is a maximum, not a pooled rate; 94% is conditional on an audited harmful subset. Exact denominators were not recoverable from the structured extraction.
- SciSpace metadata calls both records "Journal Article," but their identifiers are arXiv DOIs; treat them as preprints. Peer-review status not established.

**Crosswalk:** distinguish (1) passive pre-exposure error dependence (Hossain et al., arXiv:2609.22512; previously reviewed VEY-013), (2) shared evaluator/within-model self-revision (frozen ConsistencyBench CGD P1 archive), (3) causal peer-message revision (Gong et al.), (4) communication-channel/receiver-policy revision (Li et al.), and (5) deliberative group aggregation (Barrera-Lemarchand et al., arXiv:2609.22497; previously reviewed VEY-012). These are distinct estimands; agreement alone does not identify the mechanism.

**ConsistencyBench boundary:** 17 target-model output files, within-model self-history/self-revision, shared GPT-4o-mini NLI checker; no cross-model peer answers. Do not infer social contagion or multi-agent deliberation from this archive.

**Source audit:** Scholar Sidekick matched all four references (two new plus the two existing comparators); no retractions/correction notices flagged. SciSpace structured full-text extraction reviewed. Direct PDFs, appendices, raw datasets and code not retrieved. Gong extraction has unresolved receiver-benchmark cell/denominator detail; do not reconstruct the headline denominators. No raw-data reanalysis, independent replication, LLM trial, human session or API spend.

**Formalization:** existing PR #850 net_gain_identity is a conditional count-balance identity built in merge-reference Actions #43245831469 (Lean 4.34.0 / Lake 5.0.0, 8,984 targets; merge ref a9f307abf17412651b765a168158626b6a09676d). Axioms [propext, Quot.sound]. Not exact-head/current-main integration; tests, lint, nanoda and global axiom audit skipped. It does not formalize ICR/Gong estimands or validate empirical premises. No new Lean module/build.

**P1 boundary:** issue #564 remains OPEN / NOT READY; frozen methods/archival scope unchanged. OV-49–OV-53 bank NOT RECOVERED; authorized endpoint NOT AVAILABLE; P1 LaTeX/PDF/reader, independent hostile review and author disposition incomplete. This crosswalk is supporting literature only; no P1 protocol amendment or gate advancement.

Internal study note: STUDIES/VEY-043_COMMUNICATION_REVISION_AND_ERROR_DEPENDENCE_CROSSWALK_2026-11-12.md. Public-safe HsH report: WORKSPACES/ORSON_VAY/2026-11-12T1824Z_COMMUNICATION_REVISION_AND_ERROR_DEPENDENCE_CROSSWALK.md (publication receipt tracked separately).


## VEY-043 publication verification amendment | 2026-11-12

- Public-safe HsH report submitted once through HSH-PUBLISH-V1 as issue #1647; submission ID orson-vey043-communication-revision-dependence-20261112t1824z-s2-001.
- Publisher comment #6832762273; publisher commit 61d055ff1f02827b4e58bbe60c8d1ec6f2cfec54.
- Canonical artifact: WORKSPACES/COMMON/PUBLISHED_SUBMISSIONS/orson-vey043-communication-revision-dependence-20261112t1824z-s2-001.md; Git blob 14c97dbf2ec7bf84816efb4d42baa63cfd3ae44f.
- Artifact, report file and issue-body content match exactly: 10,387 UTF-8 bytes; recomputed SHA-256 60a8e1d39ccec24c4456ee605471c71a6fc82f0bfb9a50ce7043c6be3b5c5e39.
- Status: PUBLISHED_VERIFIED. No retry, duplicate issue, direct artifact write, or bypass.
- Publication does not advance P1 or amend the frozen protocol.
