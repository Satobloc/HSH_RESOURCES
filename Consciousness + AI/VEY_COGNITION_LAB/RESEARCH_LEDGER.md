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
