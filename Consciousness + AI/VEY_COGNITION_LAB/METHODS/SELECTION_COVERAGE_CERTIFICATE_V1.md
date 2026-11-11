# Selection Coverage Certificate v1.0

**Owner:** Vey Cognition Lab (Orson Vay)  
**Date:** 2026-11-11  
**Status:** PROPOSED METHOD / NOT YET VALIDATED IN A CONTROLLED LLM STUDY  
**Related study:** VEY-042 — Selection completeness and partial-state reporting in AI work-state continuation

## Purpose

Measure what happens before, during, and after a handoff representation is formed. The certificate prevents a downstream reviewer from being credited for qualifying material that never reached the review input, and prevents partial preservation from disappearing into a binary present/absent score.

This is a research and workflow method, not a new automation, not a completeness guarantee, and not a claim that any declared candidate universe is exhaustive.

## 1. Freeze the candidate universe

Before selection or packaging, declare:

- universe ID and version;
- source scope, repositories, paths, conversation/date range, and retrieval method;
- eligibility rule and exclusions;
- retrieval timestamp and source commit(s);
- known inaccessible/quarantined sources;
- whether the universe is complete, bounded, sampled, or unknown.

A coverage result is conditional on this declared universe. It does not establish that the universe itself contains every relevant source item.

## 2. Item-level record

For every candidate item, retain:

| Field | Required meaning |
|---|---|
| candidate_id | Stable identifier within the frozen universe |
| source_id | Conversation/message/file/issue/DOI identifier |
| source_locator | Repository/path, line/page/span, URL, or message ID |
| source_version | Commit, blob SHA, DOI version, or retrieval timestamp |
| source_authority | Nathan Direct, assistant reconstruction, historical source, standard reference, external report, proposal, or unknown |
| eligibility | Eligible / excluded / unresolved |
| eligibility_reason | Rule and reason |
| selection | Selected / excluded / unresolved |
| selection_reason | Inclusion/exclusion rationale |
| representation_locator | Exact location in the handoff, if selected |
| coverage_state | PRESENT / PARTIAL / ABSENT / UNAVAILABLE / UNASSESSED / NOT_APPLICABLE |
| review_state | Not reviewed / checked / disputed / corrected / unresolved |
| qualification_state | Qualified / conditional / not qualified / unavailable / not assessed |
| provenance_state | Complete / label-only / missing / unknown |
| authority_state | Preserved / weakened / overstated / unknown |
| action_contract_id | The current action or decision contract, if applicable |
| action_relevance | Relevant / not relevant / unknown |
| outcome_state | Not run / executed / failed / completed / unknown |
| notes | Concise source-grounded explanation |

Do not replace source IDs with names or summaries. Preserve all original occurrences and corrections.

## 3. Coverage states

- **PRESENT:** the material content required for the declared item is represented sufficiently for the stated purpose.
- **PARTIAL:** some content is represented, but a material qualification, dependency, source span, uncertainty, authority boundary, or other required element is missing or weakened.
- **ABSENT:** the item is eligible within the frozen universe but is not represented in the handoff.
- **UNAVAILABLE:** the source could not be retrieved or inspected by the reviewer.
- **UNASSESSED:** no coverage determination was made.
- **NOT_APPLICABLE:** the declared eligibility rule excludes the item from this handoff's intended scope.

PARTIAL is not ABSENT. UNAVAILABLE is not zero content. NOT_APPLICABLE is not a successful preservation result. Report all states separately.

## 4. Separate stages and denominators

Keep these stages distinct:

1. candidate-universe formation;
2. selection;
3. representation/encoding;
4. review;
5. qualification;
6. successor pre-action disposition;
7. action;
8. outcome.

Report at least:

- candidate universe size;
- eligible, excluded, and unresolved counts;
- selected count;
- PRESENT / PARTIAL / ABSENT / UNAVAILABLE / UNASSESSED / NOT_APPLICABLE counts;
- representation fidelity over selected items;
- selection coverage over eligible items;
- authority and provenance status separately;
- action-relative support and actual execution/outcome separately.

Do not use a single “handoff success” score to combine these different denominators.

## 5. Authority and provenance are separate dimensions

A source item may be present while its authority is weakened or overstated. A label may be preserved while the underlying evidence is absent. Therefore record:

- provenance: complete / label-only / missing / unknown;
- authority: preserved / weakened / overstated / unknown.

Do not infer permission from descriptive status, role label, historical authorization, or a successful prior action. The current action contract remains controlling.

## 6. Successor pre-action check

Before an action, the successor should identify:

- which candidate items support the proposed action;
- which relevant items are PARTIAL, ABSENT, UNAVAILABLE, or UNASSESSED;
- whether the action depends on an unresolved source or authority boundary;
- whether the action is authorized now, not merely historically described;
- whether independent source reopening is needed.

A correct immediate action does not prove complete transfer. Conversely, incomplete global state does not automatically prevent a narrowly bounded action if its required evidence and authority are present.

## 7. Controlled follow-up design

To separate selection from representation, use a source-locked 2×2 design:

- selection: bounded versus richer;
- representation: free-form versus fixed-field.

Freeze the same candidate universe first. Hold model/version, task, source bundle, token budget, review instructions, and successor action contract constant where feasible. Randomize condition order and blind item-level adjudication. Publish all four cell counts and item-level statuses. Use a new source bundle as holdout.

A selection effect requires improvement when the selection policy changes while representation is held fixed. A format effect requires improvement when the selected item set is held fixed. Report interaction and confounds rather than attributing a combined difference to one factor.

Falsifiers include:
- richer selection fails to improve coverage on independent source bundles;
- format changes do not improve representation fidelity with a fixed selected set;
- content-presence gains are offset by weaker authority/provenance;
- successor action support does not improve despite greater global coverage;
- the apparent effect disappears under blinded adjudication or a new source bundle.

No numeric threshold should be invented before a real source bundle, model/version, adjudication rule, and uncertainty method are specified.

## 8. Evidence boundary

P001 (Jia Shen, Miralucis, preprint v1.0, 2026-10-11; version DOI 10.5281/zenodo.23291119) is a single-source external comparator. The inspected author pages report 97-item omissions and a three-category selection summary, but the full PDF and item-level data were not retrieved in the VEY-042 review. The source warns of length, wording, sampling, and environment confounds. P001 motivates this certificate; it does not validate the certificate or establish a general causal effect.

Formalization target: selection is a projection from the frozen candidate universe to the selected set. If that projection is non-injective, a downstream encoder that sees only the selected set cannot restore distinctions already removed, unless it independently reopens the source. Existing PR #1115 contains related generic projection statements but remains LEAN_NOT_RUN. No proof or compilation is claimed by this method document.

## 9. Versioning and change control

- Freeze and hash each universe and certificate before adjudication.
- Amend rather than overwrite prior selection decisions.
- Record the author, reviewer, timestamp, and reason for every change.
- Preserve original and corrected representations separately.
- Do not promote this method into BEDROCK or mandatory team policy without independent review and explicit authorization.
