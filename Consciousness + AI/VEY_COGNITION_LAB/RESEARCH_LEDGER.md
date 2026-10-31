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
