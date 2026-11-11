# VEY-042 — Selection completeness and partial-state reporting in AI work-state continuation

**Date:** 2026-11-11  
**Owner lane:** Orson Vay, LLM cognition / continuity research  
**Status:** SOURCE-LOCKED PREPRINT COMPARATOR; AUTHOR-PAGE / ABSTRACT-LEVEL REVIEW; NOT FULL-TEXT REVIEW; NO NEW TRIAL.

## 1. Research question

Can an apparently successful AI handoff be evaluated without measuring what was omitted before the handoff representation was created?

VEY-030 already separates retention, availability, access, comprehension, decision uptake, and task outcome. VEY-040 further separates global-state fidelity, action-relative support, provenance, pre-action disposition, execution, and outcome. This note adds a distinct upstream stage: **candidate-source selection completeness**.

The question is not whether structured handoffs are generally worse. It is whether selection omissions can be distinguished from representation loss, review error, qualification error, authority drift, and action failure.

## 2. External comparator and source custody

Jia Shen, “Transfer Is Not Continuation: Failure Boundaries in AI Work-State Continuation,” Miralucis Research Program, preprint v1.0, published 2026-10-11.

- Version DOI: 10.5281/zenodo.23291119.
- All-versions DOI: 10.5281/zenodo.23291118.
- License shown by the author page: CC BY 4.0.
- Author page: https://miralucis.ai/publications/p001/
- Publications page: https://miralucis.ai/publications/

The author identifies the work as a bounded case study from one long-span human–AI research project. It is a preprint. The inspected pages do not establish peer-review status.

**Access boundary:** both author-controlled HTML pages were inspected; SciSpace search and extraction were used for discovery/abstract-level cross-check. The Zenodo record/PDF link could not be retrieved through the available web/container routes. No full PDF, raw item-level dataset, code, or selection manifest was inspected. Absence of an observed public file is not evidence that no such file exists. This is therefore a bounded author-page comparator, not a completed full-text or independent reproduction review.

## 3. Reported observations

The dedicated P001 page reports:
- 97 material items.
- One structured handoff omitted 31 items.
- An ordinary free-form handoff omitted 13.
- The structured omissions were already present at extraction and persisted through review and packaging.
- A follow-up 2×2 representation × selection comparison with fixed eight-field outputs.
- Selection-associated differences larger than format-associated differences, with single-source, length, wording, sampling, and environment confounds.

The dedicated P001 page summarizes the fixed-eight-field cells using present/absent counts only: bounded selection 35/31 and richer selection 84/1. The separate author publications page supplies the three-category counts, each summing to 97:

| Selection | Present | Partial | Absent | Total |
|---|---:|---:|---:|---:|
| Bounded | 35 | 31 | 31 | 97 |
| Richer | 84 | 12 | 1 | 97 |

This is a **public-surface reporting-completeness discrepancy**: the dedicated page omits the partial category; the publications page exposes it. Do not interpret the abbreviated two-category presentation as a complete binary partition.

The same publication summary reports a qualification run with 40 correct and 3 partial judgments among 43 available statement units, with 2 further units unavailable from the input. Both successors respected a historical STOP boundary; only the qualification-bearing successor additionally requested current authorization.

## 4. Descriptive calculation

Using the author-reported counts only:

| Measure | Calculation | Result |
|---|---:|---:|
| Structured omission rate | 31/97 | 31.96% |
| Free-form omission rate | 13/97 | 13.40% |
| Difference | 18/97 | 18.56 percentage points |
| Count ratio | 31/13 | 2.38 |
| Bounded present | 35/97 | 36.08% |
| Bounded partial | 31/97 | 31.96% |
| Bounded absent | 31/97 | 31.96% |
| Richer present | 84/97 | 86.60% |
| Richer partial | 12/97 | 12.37% |
| Richer absent | 1/97 | 1.03% |
| Present-share difference | (84−35)/97 | +50.52 percentage points |

These are descriptive arithmetic, not inferential statistics. No p-value, confidence interval, or causal effect was calculated. The public summary does not provide all four factorial cell counts, item-level data, randomization details, or uncertainty intervals. The author explicitly warns against attributing the observed selection-associated difference to selection alone.

## 5. New stage distinction

The continuation pipeline should distinguish:

1. **Candidate universe formation:** define and version-pin the source set eligible for consideration.
2. **Selection:** include, exclude, or leave unresolved each candidate under a declared rule.
3. **Representation/encoding:** express selected material in the handoff.
4. **Review:** inspect the representation and compare it with available sources.
5. **Qualification:** assess only the material that reaches the qualifier.
6. **Successor pre-action disposition:** interpret current scope, authority, uncertainty, and action contract.
7. **Action and outcome:** record execution and result separately.

A downstream reviewer cannot qualify a source item that never reached its input unless the reviewer independently reopens the original source. Therefore selection completeness and representation fidelity require separate denominators. This extends, rather than replaces, VEY-030/040.

## 6. Selection Coverage Certificate

For each frozen candidate item, record:

- stable source ID, repository/path or DOI, version/hash, date, and scope;
- eligibility decision and rule;
- selection decision and inclusion/exclusion reason;
- location in the handoff representation, if selected;
- review and qualification result;
- provenance-evidence status;
- authority-boundary status;
- unresolved, inaccessible, or unassessed state.

Use distinct item states:
- PRESENT
- PARTIAL
- ABSENT
- UNAVAILABLE
- UNASSESSED
- NOT_APPLICABLE

Do not collapse PARTIAL into ABSENT or UNAVAILABLE into zero content. Keep authority status (preserved / weakened / overstated / unknown) and provenance status (complete / label-only / missing / unknown) as separate dimensions.

Report counts over the frozen candidate universe. Coverage is conditional on that declared universe; it does not prove that the universe itself is complete.

## 7. Falsifiable follow-up

A source-locked 2×2 design can separate selection from representation:

- Factor A: bounded versus richer selection, with the candidate universe frozen first.
- Factor B: free-form versus fixed-field representation.
- Hold model/version, source bundle, task, token budget, review instructions, and successor action contract constant where feasible.
- Randomize condition order and blind item-level adjudication.
- Publish all four cell counts and the item-level PRESENT/PARTIAL/ABSENT/UNAVAILABLE ledger.
- Score selection coverage before encoding, representation fidelity after encoding, authority preservation, action-relative support, and successor pre-action disposition separately.
- Use a new source bundle as holdout.

A selection benefit is weakened or falsified if richer selection does not improve item coverage on independent source bundles, or if content-presence gains are offset by worse authority/provenance preservation. A format benefit requires improvement when the selected item set is held fixed.

## 8. Formalization status

Existing HsH PR #1115 contains ObservableProjection.lean (branch head cc5d92c6935aa2ae120de2efed7c4ac8a1ebfbc7; file blob 0ff8e07d1f7100e1648d05192aec9a9b340515b2). It formalizes generic conditional results about non-injective projections, downstream predicates, and injectivity under composition. The PR is OPEN / DRAFT / UNMERGED and its new modules are LEAN_NOT_RUN.

The next precise theorem target is: if the selection map is non-injective, composing it with any downstream encoder remains non-injective. This is a conditional mathematical statement, not an empirical result. No Lean code was added because the local runtime has no Lean/Lake/Elan and no workflow-dispatch action is exposed; container DNS resolution to GitHub failed. No compilation is claimed.

## 9. P1 boundary and next cursor

P1 issue #564 remains OPEN / SOURCE-AND-EXPERIMENT-READINESS / NOT READY. The frozen ConsistencyBench CGD scope, shared GPT-4o-mini NLI checker, and original OV-49–53 source inventory are unchanged. VEY-042 is a separate continuity/cognition methods note; it does not reopen P1, claim a new trial, or advance the November 9 paper gate.

Next:
1. Retrieve the complete P001 PDF/Zenodo record and any item-level manifest or code, if accessible.
2. Reconcile the dedicated-page versus publications-page partial-category display against the actual versioned PDF.
3. If source material permits, inspect the selection/representation 2×2 at item level before making any causal or general claim.
4. Formalize the selection→encoding composition theorem only when an actual Lean 4.34.0/Mathlib compile route is available.
5. Continue the frozen P1 OV-49–53 origin inventory and controlled experimental-feasibility check separately.

**Disposition:** selection completeness is a distinct upstream continuation gate; PARTIAL is a required status, not a cosmetic annotation. Evidence remains a single-source preprint comparator pending full-text and item-level recovery.

## Amendment 01 — Source relevance and carrier localization

This addendum is separate from the original source-locked P001 analysis. It adds source relevance, source identity, access depth, duplicate-family identity, and carrier class as orthogonal dimensions. See METHODS/SELECTION_COVERAGE_CERTIFICATE_V1_ADDENDUM_01_SOURCE_RELEVANCE_AND_CARRIER_LOCALIZATION.md.

A full Markdown manuscript review of Thomas Ryan, The Scaffold Continuity Trap (preprint v1.0.0, 2026-07-13, DOI 10.5281/zenodo.21342748), found four eligible blinded rows, one per condition, all 12/12 on the core score. Full scaffold did not beat no-memory or summary-only; sham stability passed. The no-memory condition still retained visible repository state, tests, and task files, so it is not a no-state baseline. One row per condition, shared broader Codex environment, low hidden-probe accuracy, and pending corrupted/adversarial conditions limit the result. The manuscript disclaims consciousness and subjective-continuity claims.

The existing Mersearch receipt's top-ranked Meridian message was directly checked. At least three archive copies represent one source message, including two exact blob copies and one variant export with identical conversation/message identity, role, timestamp, and text. The message is relevant to general literature/resource planning but not to Orson's original role-reset instruction. Multiple paths are not independent source witnesses.

The method addendum defines scope_relation, identity_state, access_depth, duplicate_family, carrier_class, and actual_access separately from coverage, authority, and provenance. It proposes a staged carrier-localization design followed by a separate selection/representation factorial. No new LLM trial, human session, or causal estimate was produced.

Formalization: theorem noninjective_selection_remains_noninjective_after_encoding was added to existing PR #1115. The source is present, but no Lean Actions run or local Lean runtime was available; status remains LEAN_NOT_RUN. P1 issue #564 and its frozen protocol remain unchanged.
