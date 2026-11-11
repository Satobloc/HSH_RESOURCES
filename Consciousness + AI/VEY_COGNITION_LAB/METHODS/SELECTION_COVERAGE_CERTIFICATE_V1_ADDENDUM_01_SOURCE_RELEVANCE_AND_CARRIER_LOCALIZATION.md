# VEY-042 Addendum 01: Source Relevance and Carrier Localization

**Date:** 2026-11-11  
**Owner lane:** Orson Vay, LLM cognition / continuity research  
**Status:** LITERATURE AND SOURCE AUDIT; PROPOSED METHOD EXTENSION; NOT VALIDATED IN A CONTROLLED LLM STUDY  
**Related study:** VEY-042 — Selection completeness and partial-state reporting in AI work-state continuation

## 1. Why this addendum exists

VEY-042 separated candidate-source selection from representation, review, qualification, successor disposition, action, and outcome. Two further distinctions are needed:

1. A search hit is not necessarily a source relevant to the target question, and multiple archive paths are not necessarily independent witnesses.
2. A condition described as no-memory may still retain task-local repository state, tests, task instructions, and other external causal carriers.

The certificate must therefore record source relevance and identity separately from coverage, and record the carrier of task-relevant state separately from the label assigned to a memory condition.

This addendum is a method proposal. It does not change the frozen P1 protocol, create a new experiment, or establish a general causal effect.

## 2. Mersearch receipt audit and a verified relevance false positive

The existing request was reused rather than overwritten or rerun:

- Request: orson-cognition-origin-bank-20261103-1745
- Tool: Mercer_Searcher_1.0, stable ref mersearch-stable-1.0
- Stable tool commit: 89933c358b67ccbfbbaa680aadeb1f35d22d91b2
- Source repositories and pinned commits:
  - Satobloc/SAT_THEORY_ARCHIVE_2023-25: 1d9b39babb82915b05dda47ebe5fd034108ab813
  - Satobloc/HsH: 9c22ddc466f1b1cb7c37a644f29242b0f5adf00c
  - Satobloc/HSH_RESOURCES: beaa05b279524a881c5f80e69f1f1f8b0f4b95f5
- Compact receipt: 16,942 files, 21,037,890 records, 135 hits, 74 distinct source paths.
- Raw SEARCH_RESULTS files remain withheld. The receipt explicitly describes its ranking as a lexical navigation heuristic, not semantic relevance or source authority. All four shared request lanes remain occupied. No new request or overwrite was made.

The first five displayed source paths include repeated appearances of one user message in the Meridian conversation:

- Conversation ID: 6a9aa91b-11f4-83ea-80a1-4d502522e441
- Title: Meridian [HsH] Michelstein-on-Meinorly
- Message ID: 3e7d7870-9cc6-42fd-83ce-92d8c6326789
- Role: user
- Created: 2026-09-08T10:01:25.258Z
- Message text asks whether to search the archive, HsH conversation logs, and exported chat history; it also notes Whirligig/NotebookLM use and requests access to recent geometric-solver and LLM-cognition literature.

Identity comparison:

- LIVE CONVOS copy and SAT_CONVOS_12 copy share exact blob SHA d21e251df093013903cc19789ded562f83b6e6ea.
- SAT_CONVOS_13 copy has blob SHA 1f841895a2585843373fe33d55a0180c91cc8423, but the target message has the same conversation ID, message ID, role, timestamp, and text.
- The compact receipt lists additional paths with the same message locator; those additional copies were not independently compared in this pass.

This is one Meridian user-message witness represented in multiple archive copies, not multiple independent source witnesses. Its scope is ADJACENT to the general literature/resource question and IRRELEVANT to the specific question of Nathan's original Orson role-reset instruction. It is not an Orson specialist charter.

The October 9 raw Orson role-reset message remains unrecovered. The current Orson role card remains an assistant-maintained reconstruction. The Mersearch compact receipt does not establish that the original message is absent because raw result rows are withheld and the search has coverage/exclusion limits.

A separate assistant-authored OV-54 cross-reading file, blob 31787835f92bf9036fd8d4380ebd6792db937710, identifies OV-49 through OV-53 as finite-core/geometric studies. It says the Orson cognition test bank was prepared but not executed. That file is not Nathan Direct and does not supply the missing matched-prompt bank.

## 3. External full-manuscript comparator: Paper 6

Thomas Ryan, The Scaffold Continuity Trap: A Blinded Scaffold-Lesion Test in Persistent Coding Agents, preprint v1.0.0, 2026-07-13, Zenodo DOI 10.5281/zenodo.21342748.

Public source repository: https://github.com/Atomics-hub/consciousness-research

Read in this pass:

- paper6/manuscript.md, blob ee308d71cee52de5bd280173ec7753a6ade4d9cc, 25,439 characters, full Markdown manuscript including limitations and references.
- paper6/results_summary.md, blob d6f83842a65504b078ba42382580c9ce0404174a.
- paper6/reproducibility_note.md, blob b0f1e752a53e90ae1653b80b28ef8d35bf915824.
- paper6/zenodo_metadata.md, blob 82064f7344097752dac83430ffa1ffd10bec886f.
- paper6/README.md, blob e95b1acab752a293a008d710e5c0de442a78a75d.

The public repository says the PDF is the published Zenodo file and declares SHA-256 1ded94cf5c92ccbe51548f7d020c58b834b2e0cb26ea40ef1c59ba080b1af487. That PDF hash was not independently verified here. The full Markdown manuscript and public result summary were read. The repository explicitly excludes coordinator-private harness state, hidden keys, blind packet archives, runner return packets, and internal Codex workspace outputs; none of those materials were accessed. Peer-review status is not established.

The four eligible blinded straight-condition rows were:

| Condition | Core score | Hidden-probe accuracy | Self-report continuity |
|---|---:|---:|---|
| Full scaffold | 12/12 | 0.2 | Strong |
| Summary-only | 12/12 | 0.0 | Moderate |
| No-memory | 12/12 | 0.0 | Moderate |
| Sham lesion | 12/12 | 0.2 | Strong |

The preregistered full-scaffold versus no-memory gate required a difference of at least 3/12; observed difference was 0. The full-versus-summary comparison also failed; sham stability passed. The manuscript therefore narrows or rejects the original headline claim for this fixture. Self-report varied with scaffold richness while action-level score did not.

Critical limitations stated by the authors:

- One eligible row per condition; not a population estimate.
- Four separate blinded Codex threads, but all in the same broader Codex environment; not independent human replications or independent agent systems.
- The no-memory condition still had visible repository state, tests, and task files. It was not a no-state or blank-agent condition.
- Hidden-probe accuracy was low in all conditions.
- Corrupted and adversarial scaffold conditions remain pending.

The supported bounded conclusion is that task-local repository artifacts can carry enough causal structure for action-level recovery in small coding-continuation tasks, even when broader memory or narrative scaffolds are removed. This does not establish that persistent memory is generally irrelevant. It establishes that carrier identity and the actual visibility boundary must be measured. The paper expressly disclaims consciousness, personhood, moral status, survival, subjective continuity, and internal persistence of a base model.

## 4. P001 metadata and access-depth correction

Jia Shen's P001 author-controlled pages identify the work as a preprint v1.0 published 2026-10-11, with version DOI 10.5281/zenodo.23291119 and all-versions DOI 10.5281/zenodo.23291118. The publications page supplies the complete present/partial/absent counts; the dedicated P001 page abbreviates the follow-up as present/absent. These are two pages in the same author-controlled source family, not independent replications.

SciSpace's record uses the all-versions DOI and labels the item as a journal article. That indexer metadata must not override the author-controlled preprint record. SciSpace extraction is an indexer-assisted cross-check, not a full-text review. The Zenodo PDF and item-level data were not retrieved in this pass. P001 remains a bounded single-source preprint comparator with unresolved length, wording, sampling, and environment confounds.

## 5. New certificate dimensions

Keep the existing coverage states and authority/provenance dimensions. Add these orthogonal fields:

| Field | Values or meaning |
|---|---|
| scope_relation | EXACT / ADJACENT / IRRELEVANT / UNRESOLVED |
| identity_state | VERIFIED / CONFLICT / UNRESOLVED |
| access_depth | LOCATOR_ONLY / METADATA / ABSTRACT_OR_AUTHOR_PAGE / FULL_TEXT / ITEM_LEVEL_DATA / CODE_OR_EXECUTION |
| duplicate_family | INDEPENDENT / EXACT_COPY / SAME_SOURCE_VARIANT / UNKNOWN |
| carrier_class | TASK_LOCAL_REPOSITORY / TEST_SUITE / TASK_SPEC / HANDOFF / SUMMARY / PERSISTENT_MEMORY / TOOL_TRACE / CONTROL_STATE / HUMAN_CONTEXT / MODEL_INTERNAL_UNOBSERVABLE |
| actual_access | NOT_AVAILABLE / AVAILABLE_NOT_ACCESSED / ACCESSED / VERIFIED_READBACK / UNKNOWN |
| discovery_method | Mersearch, SciSpace, repository search, direct source, or other named route |
| discovery_record | Request ID, result locator, or stable source record |

Do not collapse these into one status. In particular:

- Source authority is not source relevance.
- A user-role message is not automatically relevant to every user directive.
- Multiple paths to the same conversation/message are not independent evidence.
- A high lexical search score is not semantic adjudication.
- A source can be PRESENT but IRRELEVANT to the target question.
- A source can be relevant but UNAVAILABLE at the required access depth.

For team/agent comparisons, represent evidence independence as a vector with separate values for subject identity, execution identity, primary-source lineage, context exposure, model/version, and evaluator independence. Do not compress this into one independent/not-independent Boolean.

## 6. Carrier-localization experiment design

A staged design is preferable to one large factorial.

**Stage A: carrier localization, 2 x 2**

- Factor 1: task-local source-of-truth state available versus removed.
- Factor 2: additional continuity scaffold full versus absent or summary-only.

Hold task specification, model/version, toolchain, source content, action contract, token budget, scoring rubric, evaluator, and time budget constant where feasible. Use calibration tasks to avoid a ceiling effect, then new independent task bundles as holdouts.

Measure separately:

- action-level task score;
- source/provenance recovery;
- hidden-probe recovery;
- successor pre-action disposition;
- execution and outcome;
- self-report continuity.

**Stage B: selection versus representation, 2 x 2**

With the candidate universe frozen, vary bounded versus richer selection and free-form versus fixed-field representation. Hold the selected item set fixed when estimating the representation effect, and hold representation fixed when estimating the selection effect. Use independent source bundles as holdouts.

The Paper 6 3/12 threshold belongs to that paper's fixture and is not automatically transferable. A new study must preregister its own minimum practically important difference, sample/cluster structure, uncertainty method, missingness rules, and stopping criterion before administration. No numeric threshold is invented here. Corrupted/adversarial source conditions should follow only after a non-ceiling baseline is established.

## 7. Formalization status

The existing Orson PR #1115 branch was updated with the conditional theorem:

not Injective(select) implies not Injective(encode composed with select).

The theorem is named noninjective_selection_remains_noninjective_after_encoding. It states that a downstream encoder receiving only the selected value cannot restore distinctions already removed by a non-injective upstream selection map. Independent reopening of the original source is a different operation.

The existing branch's Lean workflow was given a narrowly scoped push filter for the review branch. The connector-mediated commits did not produce a Lean Actions run; fetch_commit_workflow_runs returned an empty list and the combined status exposed only an unrelated Vercel deployment failure. The container has no Lean, Lake, or Elan executable, and DNS/network access to GitHub failed. Therefore the new theorem is LEAN_SOURCE_PRESENT / LEAN_NOT_RUN, not compiled or proof-verified. PR #1115 remains OPEN / DRAFT / UNMERGED; no independent review is recorded.

This formal statement does not establish that any real handoff selection map is non-injective or that any cognitive mechanism has been identified.

## 8. P1 and publication boundary

P1 issue #564 and the 2026-11-02 protocol freeze remain unchanged. P1 remains a source-audited ConsistencyBench CGD methods/archival study, not a cross-model peer-deliberation experiment. The OV-49–OV-53 original matched-prompt bank remains unrecovered; no new LLM trial, human session, API spend, manuscript/PDF/reader, or independent review occurred.

Existing HsH issue #1611 remains REJECTED for a declared-versus-actual SHA-256 mismatch. Its expected canonical artifact path returned 404. The issue-publisher workflow listens to issues.opened only; no edit-trigger or dispatch action is available in this runtime. No retry, duplicate issue, direct artifact write, or publisher bypass was attempted. No canonical public artifact exists for that submission.

**Disposition:** source relevance and carrier localization are added as proposed dimensions to VEY-042. Paper 6 is a full-Markdown-manuscript literature review, not an independent replication. No P1 scope change, new experiment, paper-gate advancement, or theory promotion.
