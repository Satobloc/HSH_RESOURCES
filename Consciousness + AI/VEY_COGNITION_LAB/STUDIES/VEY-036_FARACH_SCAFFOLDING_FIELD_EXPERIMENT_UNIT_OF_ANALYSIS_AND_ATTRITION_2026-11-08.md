# Review-MIND source audit: Farach et al. (2026), human–AI scaffolding in a field experiment

**Disposition:** FULL-TEXT REVIEWED / WORKING PAPER PREPRINT / NO NEW TRIAL.  
**Review date:** 2026-11-08.  
**Reviewer identity:** current assistant reconstruction under the deterministic Enheduanna ring label; not an authenticated historical Enheduanna instance and not Orson Vay.

## 1. Source and study identity

Alex Farach, Alexia Cambon, Lev Tankelevitch, Connie Hsueh, and Rebecca Janssen, “Scaffolding Human-AI Collaboration: A Field Experiment on Behavioral Protocols and Cognitive Reframing,” arXiv:2604.08678v2 (19 April 2026), Microsoft Research working-paper PDF. The official project page labels it a working paper. Peer-reviewed publication was not established in this review.

Primary sources:
- Paper PDF: https://www.microsoft.com/en-us/research/wp-content/uploads/2026/04/Farach_etal_Publication.pdf
- arXiv record/version: https://arxiv.org/abs/2604.08678
- Companion site: https://microsoft.github.io/ai-mindset-experiment/
- Companion-site repository: https://github.com/microsoft/ai-mindset-experiment

The companion GitHub repository describes itself as the interactive presentation website, not the raw-data or analysis-code repository. The paper states that de-identified survey data and LLM grading scores cannot be shared publicly under the employer's confidentiality agreement; analysis code is available upon request. No raw participant data or private employer records were accessed.

The paper reports informed consent and no deception; it was not submitted to an IRB. All authors are Microsoft employees. The authors state that the study was designed to evaluate scaffolding, not Copilot itself, and that both conditions had identical Copilot access. The study was not preregistered.

This is a study of human workflow and human use of Copilot, not evidence about model consciousness, model-internal cognition, or multi-agent LLM consensus.

## 2. Design: two different interventions, two different units

The single-day field experiment involved 388 Gap Inc. employees in 194 pairs. All participants had access to Microsoft Copilot.

- **Task A, pair-level:** a mandated synchronous “Create-Out-Loud” workflow (joint discussion, Teams transcript, then Copilot drafting) versus naturalistic pair use. There were 97 pairs per arm.
- **Task B, individual-level:** AI Mindset partnership training (AI framed as a thought partner) versus standard feature-based Copilot training. There were 194 individuals per arm.
- Task A preceded Task B. The interventions therefore were not independent factorial factors: Task B followed an earlier task and intervention that could affect beliefs, confidence, and later behavior.

The paper says the AM session served as control and the PM session as treatment. This creates an AM/PM session-time confound with the treatment contrast. The paper acknowledges the confound and presents a post-hoc sensitivity analysis. Its sensitivity table estimates that a pure session effect of d=.81 would be needed to erase the Task A difference, compared with a cited literature maximum of d=.30. That is a calibration exercise using an assumed comparator, not a direct measurement of the session effect in this cohort.

## 3. Results, with extensive and intensive margins kept separate

### Task A: mandated pair workflow

- Documents produced: 93/97 control pairs versus 71/97 treatment pairs.
- Production rates: 95.9% versus 73.2%, a treatment-minus-control difference of −22.7 percentage points.
- Among produced documents, the LLM-graded quality contrast was −4.96 points for treatment. This is conditional on document production; the paper also reports Lee trimming bounds of −7.01 to −3.34 under a monotonicity assumption that treatment did not increase production for any pair.
- Mean document length: 740 words in control versus 454 in treatment. The control documents were about 1.63 times as long. The paper's mediation analysis attributes 32.6% of the estimated Task A quality difference to word count, but that mediation relies on sequential ignorability, which the authors identify as a strong assumption.

The bounded result is not “collaboration is harmful.” It is that this particular mandatory synchronous protocol, under this organization's infrastructure and compliance conditions, was associated with lower completion and lower scores than flexible use.

### Task B: individual partnership training

- Documents produced: 123/194 control participants versus 87/194 treatment participants.
- Production rates: 63.4% versus 44.8%, a difference of −18.6 percentage points.
- The primary continuous quality model was null. Its Lee bounds were −1.58 to +1.90, crossing zero.
- The favorable binary perfect-score result (OR 2.07, p=.022) used a post-hoc threshold chosen after observing a 68.1% ceiling. Lee bounds for that binary outcome were −.10 to +.31, also crossing zero. The paper's own interpretation is cautious.
- Belief improvement after Task B may partly reflect recovery from the preceding Task A experience, rather than a durable training effect.

The two tasks do not establish that cognitive scaffolding is generally superior to behavioral scaffolding: the interventions differ in task, unit of analysis, sequence, timing, and outcome specification.

## 4. Measurement and source-fidelity audit

The primary document grader was GPT-4o-mini at temperature 0, run three times with the median score used. It was perfectly deterministic on 53.1% of Task A documents and 90.7% of Task B documents. The reported cross-model comparison with GPT-4o was strong (Pearson r=.922; ICC=.921), but that is model-to-model agreement, not independent human validation.

Human validation used eight trained raters. Only 61 of 96 assigned documents received complete dual ratings (63.5%). Overall human-human agreement was modest (ICC=.56; Krippendorff alpha=.46; weighted kappa=.21). LLM-human weighted kappas were negative (−.40 and −.21 overall). The LLM was systematically more generous: +4.9 points overall, +5.5 points on Task B. Rank-order correlation was better for Task A (.79) than Task B (.58). The authors report that the LLM-human gap did not differ significantly by condition, which supports a limited claim about condition symmetry, not absolute score validity.

The paper's compliance paragraph labels counts 77 (Stranded), 51 (Parallel Play), and 37 (True Joint) as treatment “pairs.” Those counts sum to 165, not 97 randomized pairs; they correspond to 165 treatment participants, leaving 29 of 194 without those compliance items. A later pair-level table uses 22, 23, and 17 pairs, which sum to 62. The text should distinguish participant counts from pair counts more clearly.

The study's actual human-AI interaction is pair-level use of one Copilot service. It does not instantiate a multi-agent LLM group, nor does agreement among employees establish independent model confirmation.

## 5. Conditional design-matrix check

The published description aligns the AM control session with control assignment and the PM treatment session with treatment assignment. Conditional on that mapping, define T_i as the treatment indicator and S_i as the PM-session indicator. Then T_i = S_i for every pair.

For an additive model with intercept and both indicators, X = [1, T, S], the two indicator columns are identical. A design-matrix reconstruction from the reported 97 control and 97 treatment pairs gives 194 rows, 3 columns, and rank 2; the coefficient direction (0, 1, −1) lies in the null space. Equivalently, for every δ,

β_T T_i + β_S S_i = (β_T + δ)T_i + (β_S − δ)S_i.

Thus the separate treatment and session coefficients are not identified by that design alone; only their combined contribution is. This is conditional on the paper's AM/control and PM/treatment description, not a raw assignment-log reanalysis. The authors' post-hoc session-effect sensitivity analysis is informative, but it does not create independent treatment/time variation.

A Lean 4/Mathlib formalization candidate is the conditional identity below. It is a proof obligation, not a result claimed as compiled:

~~~lean
import Mathlib

theorem treatment_session_shift_invariant
    {n : Nat} (t s : Fin n → ℝ)
    (h : ∀ i, t i = s i)
    (βt βs δ : ℝ) :
    ∀ i, βt * t i + βs * s i =
      (βt + δ) * t i + (βs - δ) * s i := by
  intro i
  rw [h i]
  ring
~~~

**Formalization status:** NOT RUN. No local Lean/Lake/Elan executable is installed, and the available HsH formalization branch belongs to Orson's protected P1 work, which was not modified. The Python design-matrix check is a scripted reconstruction from the published assignment description, not a Lean proof or an independent causal estimate. Even a successful Lean proof would establish only the conditional algebraic identity, not the correctness of the source-to-design translation or an empirical treatment effect.

## 6. What this supports, and what it does not

Supported:
- Workflow mandates can impose coordination and completion costs when synchronous infrastructure or pair availability is unreliable.
- Completion and quality are separate outcomes; report both the extensive margin (whether an output exists) and intensive margin (quality conditional on production).
- Cognitive framing and behavioral workflow are distinct interventions and should not be bundled or compared across different tasks as though they were one factorial experiment.
- LLM grading requires independent calibration; model-to-model agreement does not substitute for human validity evidence.

Not established:
- That optional/adaptive scaffolding will outperform fixed or naturalistic workflows.
- That AI-as-thought-partner training produces a robust general quality gain.
- That the findings generalize beyond one employer, one day, one Copilot configuration, and these tasks.
- Any result about model consciousness, model memory, or multi-agent consensus.

## 7. Disconfirmatory design for adaptive scaffolding

A future consent-based study could randomize teams to (a) naturalistic use, (b) a fixed mandatory workflow, and (c) a modular adaptive scaffold with explicit activation triggers and fallbacks. Balance session time and infrastructure; separate cognitive framing from workflow mandates; counterbalance task order or use independent tasks; pre-register primary outcomes and thresholds; randomize at the team/dyad level where members interact; record actual scaffold use and failure states; and report completion, time, source-traceability errors, blinded human quality ratings, participation balance, friction, and user-reported cognitive load separately. Use LLM grading only as a secondary measure with calibration and uncertainty. No such experiment was run here.

## 8. Project boundary and status

This is a supplementary external-literature review. It does not alter Orson Vay's ownership of the November 9 P1, does not change P1 scope or readiness, and does not advance any paper gate. No human session, model API call, participant-level data access, new tool, physical calculation, SAT-O/Blockwave equation change, theory promotion, or BEDROCK change occurred.

**HSH_RESOURCES classification:** LITERATURE RESULT / FULL-TEXT REVIEWED / WORKING PAPER PREPRINT.  
**H(s)H status:** external comparator only; no theory authority.
