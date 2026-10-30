# VEY-012 | Revision valence, common-cue shifts, and evidence-bearing deliberation

**Date:** 2026-10-30  
**Status:** COMPLETE-AS-STAGE — PRIMARY-LITERATURE REVIEW + PUBLIC-AGGREGATE RECONSTRUCTION + CONDITIONAL FORMALIZATION IN PROGRESS. No new model trial administered.  
**Program:** VEY-004 Exposure and Independence; VEY-006 Team Cognition; HsH P1 (Nov 9).  
**Evidence classes:** LITERATURE RESULT; ARCHIVE OBSERVATION (prior VEY-011/OV-55); DERIVED AGGREGATE COUNT RECONSTRUCTION; INTERPRETATION; PROPOSED CONTROLLED TEST.

## Executive result

“Consensus” is not one mechanism. The literature and the current project record support at least four distinct pathways:

1. **Shared-source dependence:** agents inherit the same evidence or source error.
2. **Common-cue marginal shift:** a peer/authority label moves each reviewer’s individual response distribution; majority aggregation then amplifies that shift.
3. **Residual reviewer dependence:** observed panel error differs from the panel error predicted from condition-specific reviewer marginals.
4. **Evidence-bearing deliberation:** agents exchange reasons/evidence and can improve on passive aggregation, especially when model families are heterogeneous.

These pathways need separate interventions and separate estimands. VEY-011 is an archive observation of non-exposed outputs, not a peer-influence experiment. OV-55 is an assistant-authored analytic toy model, not an administered LLM experiment.

A second result concerns revision labels. On a set of answer-changing revisions, **a revision away from an initially correct answer is necessarily harmful** under a single-gold-answer scoring rule. But the complement, “initially wrong,” is not automatically beneficial: it includes wrong-to-wrong revisions. Public aggregate data from Qu et al. (2026) show this neutral/unsuccessful category can dominate under unanimous-wrong peer cues.

## 1. Primary literature reviewed

### A. Qu, Fu, Lu, Cheng & Hu (2026), “Easier to Mislead Than to Correct: Harmful and Beneficial Revision in LLM Conformity”

- arXiv: https://arxiv.org/abs/2606.01637 (v2, 2026-06-06).
- Public author repository: https://github.com/yibo-hu-lab/Easier-to-Mislead-Than-to-Correct
- Full paper read; author repository README and aggregate CSVs retrieved.
- Four open-weight model families, seven task families, peer-consensus conditions (mixed / unanimous-correct / unanimous-wrong), and authority framing (absent / present).
- The repository contains perturbation inputs and aggregate result CSVs, but not the full raw model-response corpus. Therefore the present calculation is an independent reconstruction from published aggregate tables, **not** a raw-output replay or fresh model run.

### B. Hu & Qu (2026), “Social Pressure Breaks Majority Voting in LLM Safety Panels”

- arXiv: https://arxiv.org/abs/2608.04415.
- Full paper read.
- Six LLM reviewers and six safety datasets, with 200 items per dataset; two-round exposure design.
- The manipulated peer cue is a simulated wrong-majority message or a silent-peer condition. This is a controlled label/social-cue intervention, not a natural multi-agent conversation with independently generated peer evidence.
- The paper reports that, under silent peers, observed panel false-alarm rate (43.0%) is close to the Poisson-binomial independence prediction (43.9%). Under wrong-peer exposure, observed and predicted panel false-alarm rates both reach 100%.
- Interpretation: the common cue’s effect on reviewer-specific marginal rates is sufficient to explain the panel collapse in that condition; an additional residual cross-reviewer dependence term is not required by that result. This does **not** establish that reviewers are generally independent. The paper separately reports a solo-baseline gap consistent with shared item difficulty.
- The exact per-reviewer raw outputs/code were not recovered in this pass; the panel comparison is reported from the paper, not independently recomputed.

### C. Hu (2026), “One Axis, No Brake: Self-Knowledge Limits Filtering Harmful Peer Conformity in LLMs”

- arXiv: https://arxiv.org/abs/2609.18998.
- Full paper read, including the revision-set definition and Proposition 1.
- In §2, the paper defines the revision set F as cases where the answer changes, and defines its binary valence label using initial correctness: V = 1 - correct_0.
- This gives a valid identity for the **harmful-vs-non-harmful** target: on F, an initially correct answer that changes must become incorrect. A filter that blocks all harmful revisions therefore needs information about initial correctness.
- But the complementary class (initially wrong) is not automatically “beneficial” in the outcome sense. It contains both wrong-to-correct and wrong-to-wrong revisions. The paper’s binary complement is therefore more precisely “non-harmful / initially-wrong revision” unless the analysis is restricted to revisions that change correctness status or checks final correctness.
- This is a construct/label interpretation boundary, not a refutation of the harmful-revision identity or of the self-knowledge result for harmful-vs-non-harmful filtering.

### D. Barrera-Lemarchand et al. (2026), “The Wisdom of Artificial Deliberative Crowds”

- arXiv: https://arxiv.org/abs/2609.22497.
- Full 30-page paper read.
- Three small models from different providers: Claude Haiku 4.5, GPT-5-nano, Gemini 3.1 Flash Lite.
- Four domains: visual quantity estimation; review of 100 NeurIPS 2024 submissions; monitoring of sabotage trajectories; 44 World Cup forecasting events.
- Three stages: independent estimates, group deliberation, private post-deliberation estimates.
- Heterogeneous three-model deliberation improved over passive pooling across the reported domains. Homogeneous groups of three copies of the same model did not improve over pooling that model’s independent outputs. The identity of the strongest model varied by task; expert dominance appeared in three of four domains.
- This is important counter-evidence to any blanket claim that peer interaction or consensus is inherently harmful. The intervention is evidence/reason-bearing cooperative deliberation, not merely exposure to a majority label.
- Limitations include one small model generation per provider, no fixed temperature or random seeds, sample-size decisions based on effect stability/cost rather than a prior power calculation, possible training exposure to NeurIPS papers despite cue removal, older safety trajectories, and data/code described as forthcoming on OSF or available on request.

## 2. Aggregate count reconstruction from Qu et al. public CSV

Source file:
- `all_results/rq1_A_desc_overall.csv`
- Git blob: `f75df47965a61b02ab818bd2c88d99c5ed54c380`

The published table gives, for each condition:
- N_total = 27,394
- N_initially_correct = 13,245
- N_initially_wrong = 14,149
- Revision_rate_pct over N_total
- Harmful_rate_pct over initially-correct records
- Beneficial_rate_pct over initially-wrong records

Reconstruction:
- N_revision = round(N_total × revision_rate / 100)
- N_harmful = round(N_initially_correct × harmful_rate / 100)
- N_beneficial = round(N_initially_wrong × beneficial_rate / 100)
- N_wrong→wrong = N_revision − N_harmful − N_beneficial

All six reconstructed values in each row land on integer counts to < 1e-8 residual from the printed percentages. The wrong→wrong count is a **derived residual**, not a directly printed raw-output count.

| Peer consensus | Authority | Total revisions | Correct→wrong (harmful) | Wrong→correct (beneficial) | Wrong→wrong (derived) | Wrong→wrong among revisions from initially-wrong answers |
|---|---|---:|---:|---:|---:|---:|
| Mixed | absent | 9,276 | 2,061 | 4,622 | 2,593 | 35.94% |
| Mixed | present | 10,296 | 2,729 | 4,300 | 3,267 | 43.17% |
| Unanimous correct | absent | 13,787 | 3,654 | 7,282 | 2,851 | 28.14% |
| Unanimous correct | present | 13,942 | 3,534 | 7,636 | 2,772 | 26.63% |
| Unanimous wrong | absent | 17,263 | 8,325 | 1,020 | 7,918 | 88.59% |
| Unanimous wrong | present | 17,824 | 8,613 | 1,046 | 8,165 | 88.64% |

Under unanimous-wrong peer cues, 7,918/8,938 (88.59%) and 8,165/9,211 (88.64%) of revisions from initially-wrong answers remain wrong. Those revisions are non-harmful relative to the initial answer but are not beneficial corrections.

This gives an empirical reason to keep three revision outcomes separate:
- correct→wrong;
- wrong→correct;
- wrong→wrong.

Unchanged answers are a fourth state outside the revision set.

### Denominator and evidence limitations

The table’s three rates use different denominators. The reconstruction relies on those definitions and on a single-gold-answer scoring rule. It does not establish semantic correctness beyond the benchmark keys. The author repository’s aggregate CSVs were available; raw response traces were not. No claim of independent raw-output re-scoring is made.

## 3. Formal proposition and precise boundary

For answer a₀, revised answer a₁, and gold answer g, on a revision a₀ ≠ a₁:

- Harmful: a₀ = g and a₁ ≠ g.
- Beneficial: a₀ ≠ g and a₁ = g.
- Unsuccessful: a₀ ≠ g and a₁ ≠ g.

Therefore:
- harmful iff initially correct (conditional on revision);
- non-harmful iff initially wrong (conditional on revision);
- non-harmful = beneficial OR unsuccessful;
- harmful and beneficial exhaust the revision set **only when correctness status changes**.

The local Lean module is being added to the existing HsH Orson P1 PR #850. Compilation and theorem-specific axiom inspection are pending; no proof success is claimed until exact-head CI completes. Lean checks the formalized classification only, not the papers’ source interpretation or empirical premises.

## 4. Synthesis: a four-mechanism model of apparent consensus

The evidence suggests a decomposition:

1. **Common source:** shared evidence can induce correlated errors even when reviewers never see each other’s answers.
2. **Common cue:** a shared peer/authority label can shift each reviewer’s marginal response probability; majority aggregation can amplify that shift.
3. **Residual dependence:** compare observed panel error with a Poisson-binomial prediction computed from reviewer-specific, condition-specific marginal error rates. The difference is a residual-dependence diagnostic, not by itself a causal estimate. Prefer item-conditional rates to pooled rates when item difficulty is shared.
4. **Information-bearing deliberation:** distinct models exchange reasons/evidence and can improve beyond passive aggregation. Model diversity appears to be an important boundary condition in the reviewed study.

A P1 manuscript should not collapse these into a single “consensus effect.” It should state which mechanism is observed, manipulated, or merely proposed.

## 5. Revised VEY-004 protocol cursor (proposed, not frozen or administered)

A staged design is preferable to one large confounded factorial:

**Stage A — label-cue effect**
- No-peer baseline.
- Length-matched neutral peer text.
- Correct-majority label cue.
- Incorrect-majority label cue.
- Cross authority framing (present / absent) as a separately randomized factor.
- Use objectively scored multi-option tasks so wrong→wrong revisions can occur.

**Stage B — source dependence**
- Disjoint-source versus common-source conditions, with source identity and source errors preserved.
- Do not mix source sharing with peer-label exposure in the same first-stage contrast.

**Stage C — evidence-bearing deliberation**
- Heterogeneous model families.
- Each agent contributes a reason and source locator, not just a vote.
- Compare independent pooling, cue-only exposure, and evidence-bearing deliberation.

Record model/provider/version, endpoint, date, prompt hash, decoding settings, seed where controllable, tool access, exact initial and peer messages, revision prompt, final answer, confidence, scorer/key version, and all failures. Blind the semantic adjudicator to condition. Preserve item clustering.

Primary outcomes:
- revision rate;
- harmful rate among initially-correct answers;
- beneficial rate among initially-wrong answers;
- wrong→wrong rate among initially-wrong revisions;
- reviewer-specific marginal error shift;
- observed panel error versus Poisson-binomial prediction;
- calibration and evidence-supported correction.

**Not administered:** no new model calls, borrowed-instance access, or human adjudication occurred in this turn. The protocol remains a proposed design for the Nov 2 freeze gate. Do not describe OV-55’s 40-task synthetic plan as an experiment; it was a toy proposal and was never run.

## 6. Internal provenance correction

The current Orson role charter refers to an “OV-49–OV-53 matched cognition test bank.” The located files OV-49, OV-53 and OV-54 identify OV-49–OV-53 as sandboxed geometry/finite-core work, not a cognition test bank. OV-55 is the located Orson cognition artifact: an assistant-authored shared-record toy model, explicitly marked as not an administered LLM test. Treat the role-charter pointer as unresolved until the intended test-bank source is recovered; do not retrofit OV-49–OV-53 into cognition evidence.

OV-55 defines Xᵢ = ZYᵢ and assumes all agents fail when a shared record is unreliable. This is a strong toy assumption to test, not a property established for real models.

## 7. Source access, tools, and costs

- SciSpace was available and used for discovery/triage; primary arXiv papers were then read directly.
- The public Qu et al. author repository was read; aggregate result CSVs were available, raw response logs were not.
- The Hu & Qu safety-panel paper was read; its linked code/data repository was not retrieved in this pass.
- The deliberative-crowd paper says raw outputs/transcripts and code will be available through OSF or on request; no such data package was retrieved.
- All four shared Mersearch request lanes were occupied. No request was overwritten or retriggered. Bounded GitHub searches were used as fallback, not represented as a Mersearch run. No original Nathan-authored passage on this precise LLM-cognition question was recovered; current direct user instruction and the Orson role charter supplied the present task authority.
- Existing HsH PR #850 and Math Hopper issue #578 were inspected; no new tooling, plugin, fork, or paid service was created or purchased.
- No H(s)H physical calculation or CODATA comparison was performed; this is Orson’s cognition remit.

## 8. Next cursor

1. Confirm exact-head Lean CI for the new three-outcome revision module and inspect every theorem-specific axiom output.
2. Keep VEY-004 QUEUED until the Nov 2 protocol is frozen and consented model access is available.
3. If no controlled model trial is feasible by the P1 gate, narrow the Nov 9 manuscript to a methods/literature + clearly bounded archive-observation paper. Do not imply that VEY-011 tested social influence.
4. Obtain the missing original Nathan cognition passage / intended OV-49–OV-53 test-bank locator through a free Mersearch lane or approved local pinned checkout when one becomes available.
5. Preserve Orson’s four-of-five substantive cognition target; no general-physics reassignment.
