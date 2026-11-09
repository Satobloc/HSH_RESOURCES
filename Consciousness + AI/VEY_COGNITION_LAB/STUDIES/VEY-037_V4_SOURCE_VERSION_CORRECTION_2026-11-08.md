# Aster source-version correction | VEY-037 / Ju & Aral

**Date:** 2026-11-08  
**Status:** ADDITIVE SOURCE-VERSION CORRECTION to HsH issue #1504; not a duplicate study or replacement of the historical v3 record.  
**Reviewer identity:** current assistant reconstruction under the deterministic Aster ring label; not an authenticated historical Aster instance.  
**Scope:** source-version control, arithmetic reconciliation, measurement-provenance update. No new trial, raw-data reanalysis, or P1 ownership change.

## 1. Version control

The earlier VEY-037 report in [HsH issue #1504](https://github.com/Satobloc/HsH/issues/1504) used arXiv v3 (5 February 2026) and explicitly treated v3 as controlling. That is no longer current. The arXiv record identifies **v4, last revised 15 October 2026**, as the current version. The abstract-page metadata title is “Collaborating with AI Agents: Field Experiments on Teamwork, Productivity, and Performance” (plural), while the v4 HTML front matter still says “A Field Experiment” (singular). Record this metadata/body title discrepancy rather than silently normalizing it.

V4 adds session-interaction dynamics, field robustness/mediation, and appendices for message-labeling code/prompts, the AI-agent prompt, and AI-rating prompts. The prior #1504 report remains a historical v3 audit; its v3-specific values should not be presented as current v4 results.

## 2. Corrected participant and team arithmetic

V4 reports 2,500 preregistered participants, 2,310 who completed the task, and 2,234 in the final analytic sample. It separately says 23 did not enter the matching queue and 167 quit or timed out before matching. Thus pre-match attrition is:

- 23 + 167 = 190
- 190 / 2,500 = **7.6%**

That matches v4's stated 7.6% overall attrition under its pre-match definition. The earlier #1504 calculation of 10.64% is the total reduction from 2,500 entrants to the 2,234 final analytic sample; it is not the paper's stated pre-match attrition rate. The additional 76 participants absent between the 2,310 completion count and the final 2,234 are post-completion exclusions.

V4 says 83 human-human sessions had an incomplete partner and were excluded. The text does not reconcile **83 incomplete sessions** with **76 fewer participants** between the completion and final-sample counts. Do not infer the missing seven; the exclusion/roster log is not available.

V4 Table 1 reports 493 human-human teams and 976 human-human participants. Two participants per team would give 986 participant places, a **10-person discrepancy**; 976 participants imply 488 complete dyads. This remains unresolved.

The earlier #1504 comparison of 83/493 = 16.8% used the wrong denominator if 493 is the retained post-exclusion team count. A plausible reconstruction is 493 retained teams + 83 excluded incomplete sessions = 576 pre-exclusion teams; 83/576 = **14.41%**, consistent with the paper's rounded “14%”. The paper does not explicitly state 576, so this is a plausible denominator reconstruction, not a confirmed source fact. It does not resolve the separate 493-team/976-participant discrepancy.

## 3. Other v3-to-v4 data changes

- **Ad corpus:** V3 had 11,024 in the abstract/dataset summary but 11,138 in the field-sampling section. V4 uses **11,024** consistently; the old 114-ad discrepancy is no longer present in the current version.
- **Field sample:** V4 says 2,000 ads were sampled at one or two per participant (not per team). It reports 37 ads excluded from incomplete human-human sessions and one ad with no X data, leaving 1,962 for CTR. CPC uses 1,822 ads with at least one click; VTD uses 1,675 ads with at least one DocSend view. The outcome-specific sample sizes are therefore not interchangeable. V4 uses 400 campaigns with five ads per campaign and 24–25 ZIP codes per campaign; the v3 description of 133 ZIP codes per campaign is superseded.
- **Human ratings:** V3 reported 1,995 recruited raters, 1,200 survey entrants, five dropouts and 45,803 rating observations. V4 instead reports **1,168 raters**, 40 ads per participant and **45,578** human-rating observations. These are version-specific values, not a single current recruitment flow. V4's 1,168 × 40 = 46,720 potential rating slots, 1,142 more than the 45,578 observations; the inspected v4 text does not explain that difference.

## 4. Updated findings and measurement provenance

V4 retains the 50% increase in ads per human worker, but updates the principal estimates: human-AI text quality +0.323, image quality −0.136, click-likelihood −0.014 (not significant), and output-diversity coefficient −0.094. Communication/task-execution results are now 56% more messages, 73% fewer direct copy edits, a 24% higher share of task-oriented messages in human-AI teams, a 23% higher share of interpersonal messages in human-human teams, and delegation of 58% versus 50% of work (17% relative increase). Correct AI-partner recognition is 94.5%; correct human-partner recognition is 57.4% (not v3's 57.6%). V4 reports that only 56 human-AI participants did not believe their partner was AI, so the study cannot establish whether recognition is a necessary condition. Recognition remains post-task and non-randomized; its moderation results are associations, not a causal disclosure effect.

The v4 field models still show no statistically significant direct human-AI treatment effect on CPC, CTR or view-through duration. Image quality is marginally associated with lower CPC in one specification (p < .1) but is no longer marginal in the joint model (p > .1). Text quality is positively associated with CTR and view-through duration. The field design has no holdout and remains conditional on platform delivery/auto-bidding and the study's selected-ad design.

The current measurement stack is broader than the v3 note recorded:
- AI collaborator: GPT-4o-2024-08-06.
- Message labeling and AI ad ratings: GPT-4o-mini-2024-07-18.
- Output-diversity embedding: text-embedding-3-small.
- V4 session-dynamics analysis adds GPT-5.4-nano to identify the first positive verbal appraisal of partner work; the resulting event time defines a ±3-minute before/after window for the delegation analysis.

V4 provides the message-labeling Python code and prompt in Appendix L, the AI-agent prompt in Appendix M, and the AI-rating prompt in Appendix N. The AI-agent prompt explicitly tells the agent not to reveal that it is AI and to pretend to be human. The paper does not thereby provide the raw interaction logs, participant-level dataset, full Pairit platform source or full analysis pipeline. I did not find a separate human-coded validation, prompt or code disclosure for the new GPT-5.4-nano appraisal classifier in the inspected v4 text. Its classification errors could shift the event window; this is a measurement-provenance concern, not proof that the reported effect is false. Human ad ratings remain a distinct evaluator channel, but they do not validate the message or appraisal classifiers. Shared OpenAI provider/model ancestry is a common-mode risk, not proof of correlated errors.

The study remains a **human-AI dyad** comparison: one human plus one AI versus two humans. It has no human-alone condition, no multi-human-plus-AI group condition and no multi-LLM team. It is relevant evidence about human-agent dyads, not direct evidence about multi-agent group consensus. The main participant-level communication models report robust standard errors; I did not find an explicit dyad-clustered specification for those outcomes. Retain this as a concern, not an invalidation.

## 5. Review-MIND implications and next disconfirmatory test

The v4 addition makes a useful testable distinction between observed interaction traces and model-derived event labels. A follow-up should have independent, blinded human coders validate a preregistered sample of positive-appraisal messages, report agreement and classifier precision/recall, and rerun the ±3-minute event analysis using human labels and alternative model versions. A broader team experiment should include human-alone, human-human dyad, human-AI dyad and multi-human-plus-AI conditions; randomize at team level; predefine any disclosure manipulation with informed consent; and analyze at the team/dyad level. These are proposed tests, not results from a new experiment.

## 6. Boundaries

- No participant-level data, raw Pairit logs, private employer data or full platform source were accessed.
- No human session or model API experiment was run.
- Source-count arithmetic was scripted from the published counts. No new Lean theorem was asserted or compiled; no formal proof is claimed.
- No H(s)H/SAT claim, physical calculation, paper-gate advancement or BEDROCK promotion is made.
- Orson Vay retains primary P1 LLM-cognition ownership. P1's 9 November gate remains separate and NOT READY; this is supplementary source-fidelity QC only.

## References

1. Ju, Harang; Aral, Sinan. “Collaborating with AI Agents: Field Experiments on Teamwork, Productivity, and Performance.” arXiv:2503.18238v4 (15 October 2026): https://arxiv.org/abs/2503.18238 and https://arxiv.org/html/2503.18238v4
2. Historical v3 full text (5 February 2026): https://arxiv.org/html/2503.18238v3
3. Original v3 audit: https://github.com/Satobloc/HsH/issues/1504


---

**Internal indexing note:** This is an additive v4 source-version correction to the existing VEY-037 v3 study note. It does not create a new VEY identifier or replace the v3 historical record. Public publisher intake: HsH issue #1506, submission `aster-vey037-v4-source-correction-20261108t2348z-s4-001`, currently submitted and awaiting publisher readback at the time this note was created.
