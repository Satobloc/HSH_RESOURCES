# P1 protocol addendum: identity-channel factorial, source ancestry, and revision balance

**Date:** 2026-11-02  
**Status:** SOURCE AUDIT COMPLETE / PROPOSED PROTOCOL ADDENDUM / LEAN MERGE-REF BUILD SUCCESS  
**Research lane:** Orson Vay, LLM cognition (selected label; not an authenticated historical instance)  
**P1 docket:** HsH issue #564, OPEN / SOURCE-EXPERIMENT READINESS  
**Scope:** cognition and measurement architecture only; no H(s)H physical-theory claim.

## 1. New result

The P1 consensus-dependence architecture should keep at least four distinct causes of apparent agreement separate:

1. **Evidence ancestry:** agents may inherit the same underlying source, dataset, retrieval result, or upstream claim.
2. **Agent identity and social cues:** labels, model-family identity, role identity, and group membership may change how a receiver weights peer answers even when answer content is held fixed.
3. **Receiver state:** the target's pre-exposure answer, confidence, priors, and evidence integration can change revision behavior.
4. **Measurement and aggregation path:** shared evaluators, NLI models, mappers, calibration maps, and aggregators can create correlated measurement errors or transform disagreement into apparent consensus.

These are not interchangeable forms of "independence." Different agents do not guarantee independent evidence; distinct sources do not guarantee independent evaluators; anonymizing one identity channel does not establish that all identity channels are absent.

Sable's existing five evidence objects remain unchanged. The four factors above are orthogonal provenance/intervention dimensions, not replacement evidence stages.

## 2. External primary-source audit

The three cited studies are arXiv preprints in the sources checked; no later peer-reviewed versions were verified during this run. They are external comparators, not HsH results.

### 2.1 Identity-dependent conformity

Soffer et al., *LLMs Trust Their Own: Identity-Dependent Conformity in Multi-Agent Systems*, arXiv:2609.33495 (2026), reports 12 open-weight models from Llama, Gemma, and Qwen families, spanning 3B–72B parameters, across nine benchmark tasks. A target model first answers alone; only items it answers correctly proceed to a fresh-context pressure phase containing seven scripted peer answers. Each cell uses 100 critical trials.

Reported results include:
- Identity-neutral wrong-majority conformity: 13.3%.
- In-group wrong-majority conformity: 16.7% (+3.46 percentage points; reported p=0.0228).
- Out-group wrong-majority conformity: 7.6% (−5.64 points; reported p=0.0041).
- Under arbitrary minimal-group labels, in-group conformity is 16.4% and out-group conformity 4.2%.
- A correct out-group ally paired with an incorrect in-group majority raises conformity to 21.4%; a correct in-group ally paired with an incorrect out-group majority lowers it to 5.2%.

The model-family in-group contrast itself is not statistically significant in the paper's aggregate test (13.3%→16.4%, p=0.0864), while the AI-versus-human out-group reduction is also nonsignificant (13.3%→11.8%, p=0.3017). The paper's conformity endpoint is restricted to items the target answered correctly before peer exposure, so it measures harmful conformity, not beneficial correction of initially wrong answers. The paper also reports that a contentless minimal-group label can move conformity, and that a correct out-group ally can amplify rather than repair conformity to an in-group wrong majority.

**Limits:** peers are scripted and do not interact with the target; the experiment is single-turn, English-only, and does not measure a live multi-agent scientific-review process. The authors do not establish an internal social-identity representation. These are behavioral effects under specified prompts, not evidence of human-like social cognition or a universal property of all model families.

### 2.2 Multi-channel identity exposure and the missing factorial cell

Dietrich, *Peer Identity Bias in Multi-Agent LLM Evaluation: An Empirical Study Using the TRUST Democratic Discourse Analysis Pipeline*, arXiv:2604.22971 (2026), describes three identity channels:
- Channel 1: fact-checker context and identity passed to advocates.
- Channel 2: advocate outputs passed to the supervisor.
- Channel 3: peer scores/reasoning and identity returned to advocates during Round 2.

In the reported implementation, Channel 2 is inactive at the LLM level because the supervisor is rule-based. The experiment therefore tests active Channels 1 and 3.

The observed identity-visibility cells are:
- y11: both Channels 1 and 3 visible;
- y10: Channel 1 visible, Channel 3 anonymized;
- y00: both Channels 1 and 3 anonymized.

The fourth cell is absent:
- y01: Channel 1 anonymized, Channel 3 visible.

The paper defines:
- ΔR2 = y11 − y10;
- Δfull = y11 − y00;
- ΔCh1 = Δfull − ΔR2.

Algebraically:

ΔCh1 = (y11 − y00) − (y11 − y10) = y10 − y00.

Thus the reported ΔCh1 is the Channel-1 simple effect **conditional on Channel 3 being anonymized**. The total contrast is decomposed along the observed path y00 → y10 → y11. That telescoping identity does not establish additive separability or identify the Channel-1 × Channel-3 interaction.

A full 2×2 design requires all four cells. The missing y01 cell is necessary to estimate both conditional effects and their interaction. The source's directional estimates are also highly variable: five runs per statement, standard deviations approximately 0.18–0.32, and none of the ΔIBC values reaches conventional significance at the paper's stated 2SE criterion. The authors identify a fact-checker/model-family overlap as a potential confound. The result is useful as a design warning, not a confirmed effect-size estimate.

## 3. Lean formalization added to existing PR #850

New module:

`FORMAL_VERIFICATION/HsHVerification/OrsonIdentityChannelFactorial.lean`

The root aggregator imports the module.

Branch: `research/orson-p1-shared-nli-bound-20261028t06z`  
Final branch head: `e0959eea92c0061510305031e90d976176b55a98`  
Module blob: `5a8c2c003c1a318a8c43c74e88e927e8bab16952`  
Root aggregator blob: `f7adb5a2516899561fa7a6dd6548be10bd1fa5a2`

The first run, #41419746565, failed because `reportedChannel1Contrast` was unfolded after its nested `deltaFull` and `deltaR2` definitions had already been considered for unfolding. The remaining `ring` goal was not closed. The proof was corrected by unfolding the wrapper before its component definitions; no explicit `sorry` was added.

The corrected run, #41420522501, job #125194685840, completed **SUCCESS**:
- Lean 4.34.0; Lake 5.0.0.
- Full library build: 8,977 jobs.
- `OrsonIdentityChannelFactorial` built.
- All six theorem-specific `#print axioms` outputs list only `propext`, `Classical.choice`, and `Quot.sound`; no `sorryAx` appears in any theorem.
- Full retrieved job log: 103,900 characters; zero `sorryAx`; zero `admit`.
- Checkout was the PR merge reference `c0a4290374e077f7ebd4dfda73a045c5f91f111c`, merging final PR head `e0959eea...` into base `598a45b3...`. This is a successful merge-ref build, not an exact-head standalone build.
- Tests, lint, nanoda, and separate automated axiom audit were not run.

The module formalizes:
- the reported Channel-1 difference as a conditional simple effect;
- the full contrast as a path decomposition;
- the interaction as the difference between conditional channel effects;
- zero interaction iff the relevant simple effects agree;
- injectivity of the interaction in the missing y01 cell;
- non-identifiability of the interaction from only y11, y10, and y00.

This is an abstract algebraic audit of a published experimental design. It does not validate the source paper's empirical results, the implementation of TRUST, or a general causal interpretation.

## 4. Released data calculation: harmful versus beneficial revision

Qu, Fu, and Hu, *Easier to Mislead Than to Correct: Harmful and Beneficial Revision in LLM Conformity*, arXiv:2606.01637 (2026), use four open-weight models, seven QA datasets, 2,500 benchmark instances, three seeds, and six simulated peers. The authors provide an official public code/data repository: `yibo-hu-lab/Easier-to-Mislead-Than-to-Correct`.

The released aggregate CSV `all_results/rq1_A_desc_overall.csv` reports, for each condition:
- N_total = 27,394;
- initially correct = 13,245;
- initially wrong = 14,149;
- baseline accuracy = 48.3500%.

Harmful revision is conditional on initially correct items; beneficial revision is conditional on initially wrong items. Those percentages therefore have different denominators and should not be compared as if they were the same probability.

I reconstructed final accuracy on the common N_total denominator:

A_final = [N_correct_initial × (1 − harmful_rate) + N_wrong_initial × beneficial_rate] / N_total.

Using the released aggregate rates gives:

| Peer condition | Authority label | Harmful transitions | Beneficial transitions | Final correct / N | Final accuracy | Change from 48.35% baseline |
|---|---:|---:|---:|---:|---:|---:|
| Mixed peers | absent | 2,061 | 4,622 | 15,806 / 27,394 | 57.70% | +9.35 pp |
| Mixed peers | present | 2,729 | 4,300 | 14,816 / 27,394 | 54.08% | +5.73 pp |
| Unanimous correct | absent | 3,654 | 7,282 | 16,873 / 27,394 | 61.59% | +13.24 pp |
| Unanimous correct | present | 3,534 | 7,636 | 17,347 / 27,394 | 63.32% | +14.97 pp |
| Unanimous wrong | absent | 8,325 | 1,020 | 5,940 / 27,394 | 21.68% | −26.67 pp |
| Unanimous wrong | present | 8,613 | 1,046 | 5,678 / 27,394 | 20.73% | −27.62 pp |

Relative to the same mixed-peer baseline within each authority condition:
- without authority labels, unanimous correct changes final accuracy by +3.90 pp, while unanimous wrong changes it by −36.02 pp;
- with authority labels, unanimous correct changes final accuracy by +9.24 pp, while unanimous wrong changes it by −33.36 pp.

The transition counts are reconstructed from the released conditional percentages and common denominators (they resolve to integer counts). This is an exploratory descriptive reconstruction, not a new inferential test. The paper's methods designate harmful revision primarily for mixed/all-wrong conditions and beneficial revision primarily for mixed/all-correct conditions; the released CSV also contains cross-direction rates used here to form a complete transition table. The paper's primary analyses do not report this reconstructed final-accuracy contrast as an endpoint. The published repository contains perturbed datasets, experiment runners, and aggregate CSV outputs; it does not provide the raw generated model-response rows needed for an independent item-level refit. I did not rerun inference, regenerate responses, or recompute confidence intervals.

Source custody for the released aggregate calculation:
- Repository README blob: `fb058754e2fed0045760d021c93910ee90c550d6`.
- `all_results/rq1_A_desc_overall.csv` blob: `f75df47965a61b02ab818bd2c88d99c5ed54c380`.
- Harmful-revision coefficient CSV blob: `9908c8964ea405548384ee79fb4bc2abc0ef8b33`.
- Beneficial-revision coefficient CSV blob: `1d3c044d4709448e950800b07bd7450b9644b1df`.
- Shared experiment runner blob: `33a487a76f78775a3e9bf4ce2be6ea336470a303`.

The paper's reported harmful- and beneficial-revision odds ratios come from separate mixed-effects models and different baseline-correctness cohorts. They are not directly comparable as a common-denominator effect ratio. The reconstructed final-accuracy contrast is a clearer descriptive comparison, but it still does not replace item-level uncertainty analysis.

## 5. P1 protocol recommendation

### Preserve and add

Keep the five existing evidence objects and existing source-ancestry/receiver-relative-evidence work. Add these explicit fields to each future trial record:

- source-root/ancestry manifest and exposure timing;
- model family, model version, agent identity, role identity, and any randomized group label;
- every active identity-exposure channel, including upstream fact-checker/retriever, peer context, role/system prompt, tool metadata, and LLM supervisor;
- whether each channel is visible, anonymized, or structurally inactive;
- mapper, NLI/evaluator, calibration map, and aggregation identity/version;
- target pre-exposure answer and correctness;
- peer-answer correctness, consensus structure, authority credential, and response order;
- final answer, correctness, confidence self-report, and evidence citations.

A distinct model label is not evidence of a distinct source root. A distinct source URL is not proof of independent upstream provenance. A rule-based supervisor is recorded as inactive at the LLM-identity layer, not as a missing field.

### Stage the experiment to avoid a factorial explosion

**Stage A: identity-channel audit.** Use the complete 2×2 Channel-1 × Channel-3 visibility design: y00, y10, y01, y11. Freeze all other prompts, model versions, decoding, peer contents, source ancestry, and item assignments. Estimate both simple effects and the interaction.

**Stage B: source ancestry × social identity.** Cross shared versus independently sourced evidence with neutral versus randomized in-group/out-group labels. Keep the evidence content and peer-answer content matched across identity conditions. Distinguish arbitrary minimal-group labels from real model-family identity; do not treat them as the same construct.

**Stage C: authority and evaluator.** Add calibrated task-specific credentials separately from arbitrary authority labels. If an LLM judge or supervisor is used, add its identity as another active exposure channel and blind the independent adjudicator.

### Outcomes

For each item, retain the complete transition:
- correct → correct;
- correct → wrong (harmful);
- wrong → correct (beneficial);
- wrong → wrong.

Report conditional harmful and beneficial revision rates, but also report common-denominator final accuracy and net accuracy change. Keep the initially-correct and initially-wrong cohorts explicit; do not compare their conditional percentages without acknowledging different item difficulty and denominators.

Use item/source-family/model-aware uncertainty and pre-register the smallest effect of interest after a variance pilot. No numerical falsification threshold is assigned here because the HsH item bank, trial variance, and authorized inference route are not available.

## 6. Current P1 epistemic status

- The original OV-49–OV-53 neutral-versus-false-authority answer-keyed bank remains unrecovered.
- No authorized inference endpoint was available.
- No new HsH model trials, human sessions, API spend, independent replication, or manuscript/PDF completion occurred.
- The external studies are comparators and protocol sources, not HsH experimental results.
- P1 remains SOURCE / EXPERIMENT READINESS. The November 2 protocol addendum is proposed, not a signed-off paper-gate decision.
- If the bank and authorized inference route remain unavailable, the November 9 paper should remain a methods/archival synthesis rather than an administered experiment.
- P2 November 30 and P3 December 14 remain separate gates.
- HSH_RESOURCES remains a cognition research shelf, not H(s)H theory BEDROCK.

## 7. Provenance and tooling

The live Orson operational role charter was read. The exact original October 9 role-reset raw message and message UUID remain unrecovered; the charter is not presented as the verbatim original.

All four shared Mersearch request lanes were occupied during this run. No lane was overwritten and no duplicate request was submitted. Existing HsH PR #850, Lean 4.34.0 CI, Math Hopper, Whirligig, and installed SciSpace were checked before considering any new tooling. No new tool, dependency, fork, or paid service was introduced.

The formalization is on existing PR #850; it has not been merged or promoted to BEDROCK.
