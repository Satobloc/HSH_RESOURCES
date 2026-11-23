# VEY-046 - Claim denominators and group-projection scope in Human-AI Teaming

**Date:** 2026-11-23  
**Status:** FULL-TEXT SOURCE REVIEW / FUTURE-METHODS CROSSWALK / NO MODEL TRIAL / NO P1 PROTOCOL CHANGE  
**Source type:** arXiv preprint; peer-review status not established  
**Local source copy:** none. The paper is indexed by its public arXiv record only.

## 1. New primary source

Hanjing Shi, Kimberly Wang, Sabrina Doherty, and Dominic DiFranzo, "Same Team Label, Different Evidence: A Full-Text Audit of Claim Denominators in Human-AI Teaming Research," arXiv:2609.27849v1, 2026-08-25.  
Primary record: https://arxiv.org/abs/2609.27849  
Full text: https://arxiv.org/html/2609.27849

Bibliographic identity was checked against the arXiv record and independently verified with Scholar Sidekick (high-confidence match). A separate retraction lookup found no retraction record. This is not a guarantee of peer review or scientific correctness.

## 2. What the audit actually did

The paper separates title/abstract relevance from full-text evidence admissibility.

- A 435-record title/abstract map was reduced by duplicate/version reconciliation to 419 primary records.
- The full-text audit purposively selected 86 records: 57 from a prior seed corpus and 29 added to fill underrepresented arrangement buckets.
- The remaining 333 records stayed at the map layer and did not receive full-text evidence-role coding.
- The 86-paper full-text set began with 74 core/near-core candidates and 12 boundary/dyadic-mechanism candidates.
- After full-text coding, the final evidence roles were 42 core empirical, 23 boundary-mechanism, 13 background/theory, and 8 context records.
- Thirty-six of the 74 apparent core candidates left the core denominator; four of the 12 boundary candidates moved into core. The paper summarizes this as 40 records changing core membership.

The final arrangement coding identified 27 human-AI dyads, 23 multi-human peer teams, 8 workplace/organizational workflows, 5 expert-client/clinical workflows, 2 governance settings, and 2 instructional groups. Ten records were background reviews/taxonomies, eight remained unclear, and one had no recoverable focal arrangement.

Team vocabulary was not a reliable proxy for the social unit: 14 of 27 dyadic studies and 20 of 23 multi-human peer-team studies used team or collaboration language. Only 20 of 86 papers specified who could see AI output.

The audit's outcome-level analysis retained 78 of 86 records. It used four nonexclusive levels: individual, team, workflow, and institutional. The authors explicitly caution that the keyword-based outcome coding does not establish that every matched construct was independently operationalized or measured.

## 3. The mechanism chain

The paper organizes claim scope as:

1. Human arrangement and the roles people occupy.
2. AI role within that arrangement.
3. Relational coupling through visibility, autonomy, control, and responsibility.
4. Team process that the arrangement permits or constrains.
5. Level of the reported outcome.

The paper's claim-pooling checkpoint is methodological. It asks whether two studies support the same kind of claim, not whether they share a surface label or AI-role name.

The audit is purposive, not a representative prevalence estimate of all Human-AI Teaming research. Its 86 full texts were selected to expose comparison failures across varied arrangements. The 333 map-only records do not enter the full-text denominator.

## 4. LLM diagnostic limits

Four blinded language-model runs unanimously assigned 53 screening labels and 59 arrangement labels. Yet 32% of the screening consensus decisions and 34% of the arrangement consensus decisions differed from the adjudicated full-text labels.

Each model-condition was run once. The models did not receive full texts, coding sheets, or the adjudication trail. The authors explicitly describe these as diagnostics of the published surface representation, not evaluations of general model capability.

This is useful evidence against treating model agreement as proof of correct source classification. It is not a general capability benchmark and not an independent replication.

## 5. Crosswalk with existing cognition sources

These sources remain distinct evidence classes and are reused rather than re-audited here:

- **Alsobay et al. (2026), "Bringing Everyone to the Table: An Experimental Study of LLM-Facilitated Group Decision-Making," PACM HCI 10(5), DOI 10.1145/3816907; arXiv:2508.08242.** Existing VEY-016 review. Its hidden-profile experiment separates facts surfaced in discussion from the group's actual choice: the LLM facilitator increased fact coverage, but the study did not find a significant improvement in the actual optimal-choice rate. The fact-mention annotation and normative score are distinct measurement stages.
- **Chen et al. (2026), "AI Agents Reshape Consensus Formation in Human Groups," arXiv:2609.02122.** Existing VEY-016/019/041 coverage, including a code/data reproducibility audit. Its consensus-strength and contribution measures are not decision accuracy. The study's single model-family design and LLM-judge dependencies remain relevant limits.
- **VEY-030/040/042/044/045** already distinguish state fidelity, action-relative projection, selection completeness, evaluator dependence, communication revision, and lifecycle state trajectories. This paper adds claim-denominator and human-arrangement admissibility; it does not replace those dimensions.

## 6. Implication for the CRTC group-projection kernel

The current assistant-reconstructed CRTC kernel in HsH PR #2375 is a narrow event-history model. It has a static roster and event-level author, availability, uptake, decision-incorporation, payload, and timestamp fields. It defines group-to-subgroup and group/subgroup-to-member projections and conditional composition.

That is a useful mathematical layer, but it is not yet an empirical adapter for the studies above. In particular, it does not yet type:

- human arrangement and membership intervals;
- AI role, authority, autonomy, control, and responsibility;
- initial information-item distribution separately from later message/disclosure events;
- fact exposure separately from message visibility;
- uptake records linked to a particular information item and source event;
- decision-use records linked to a decision and rationale;
- outcome unit and criterion;
- source/evaluator provenance for each measurement field.

A future extension should keep at least these objects distinct: Participant/Role, InformationItem, DisclosureEvent, UptakeRecord, DecisionUse, DecisionRecord, and OutcomeRecord. It should define explicit projections and composition conditions between group, subgroup, member, information, and outcome views. This is a design proposal, not implemented code or an empirical validation.

## 7. Boundary

No raw paper dataset or code was acquired or reanalyzed. No new LLM trial, human session, API spend, P1 protocol change, manuscript edit, paper-gate advancement, or theory promotion occurred. The frozen ConsistencyBench CGD protocol and P1 issue #564 remain unchanged.

**Evidence class:** LITERATURE RESULT / FULL-TEXT REVIEW / FUTURE-METHODS CROSSWALK. Not an H(s)H premise, not a causal result for the CRTC model, not a model-capability evaluation, and not an independent replication.
