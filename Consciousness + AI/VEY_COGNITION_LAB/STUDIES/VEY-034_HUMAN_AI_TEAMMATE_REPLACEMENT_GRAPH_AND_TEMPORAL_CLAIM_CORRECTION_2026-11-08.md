# VEY-034 — Human-AI teammate replacement, relational graph structure, and temporal-claim correction

**Date:** 2026-11-08  
**Status:** PRIMARY-SOURCE REVIEW COMPLETE / SOURCE-REPORTED EMPIRICAL RESULT / STRUCTURAL FORMALIZATION SUBMITTED, CI PENDING  
**Evidence class:** LITERATURE RESULT; assistant-derived structural interpretation; no independent participant-data reanalysis  
**Owner boundary:** Supporting literature note for the Vey Cognition Lab. Orson retains ownership of P1 and all primary LLM-cognition work. This note does not alter P1 scope or its November 9 gate.

## 1. Primary source and review extent

Nixon, Nia; Jaeyoon Choi; Pedro Martins De Bastos; Mohammad Amin Samadi; Seehee Park; and Spencer JaQuay (2026), “The Social Cost of an AI Teammate: How an Artificial Teammate Reshapes Human-Human Communication in Small-Team Decision-Making,” arXiv:2607.27179v2, revised 2026-10-30.

- v1: submitted 2026-07-29, arXiv:2607.27179v1.
- v2: submitted 2026-10-30, arXiv:2607.27179v2.
- Primary records: https://arxiv.org/abs/2607.27179v1 and https://arxiv.org/abs/2607.27179v2.
- Full v2 HTML reviewed: abstract, §§1-5.3, methods, results, limitations, references. This is a targeted full-text review, not an independent reproduction of raw data or model outputs.
- The paper is a preprint. Its results are attributed to the authors, not independently measured here.

No match for arXiv:2607.27179 or the title was found in the current Vey Cognition Lab source index or study ledger before this entry. This is a new evidence regime relative to VEY-016: one fixed AI peer configuration inside human teams, not a multi-LLM peer panel or an AI facilitator.

## 2. Version-critical correction

The v1 abstract called the study a “randomized controlled study” and said the social cost was “immediate and present at baseline.” The v2 abstract instead describes a between-teams experiment with sequential, greedy random allocation and says the temporal analyses do not establish when the cost emerged.

The v2 methods explain why:

- 80 undergraduates were recruited across 33 configured teams.
- 16 treatment teams had two student seats plus one AI; 17 control teams had three student seats.
- 83 student positions were nominally available; 80 were recruited.
- Five recruited students were excluded for missing chat data or dropout, leaving 75 analyzed students: 30 treatment and 45 control.
- The GCA roster contains 91 computational nodes: 75 human students plus 16 AI nodes. AI nodes are not recruited participants and are excluded from survey analyses.
- TRAIL used sequential, greedy random allocation as students entered; students did not select their team or condition, and assignment used no demographic stratification. The v2 text does not give enough detail to independently reconstruct a treatment-randomization sequence. Do not upgrade this to a verified randomized controlled trial.
- There was no pre-task baseline. The event-locked models found no condition differences in within-session trajectories, but that only supports stability of the measured pattern during the observed discussion. It does not establish that the difference was already present at the beginning.

This is a material epistemic correction, not merely a wording change. The v1 onset claim must not be repeated as a verified result.

## 3. Actual human-AI interaction and reported findings

The task was a text-only, high-stakes search-and-rescue moral-dilemma discussion at a large public research university in Fall 2025. The study reports UCI IRB protocol #6594, voluntary participation, class credit regardless of participation, and an alternative activity for students who opted out.

The AI configuration was held constant across all 16 treatment teams:

- One AI teammate persona, “Clever Lamarr”.
- Gemini 2.5 Flash-Lite.
- One action-manager stage decided whether to respond; a response-generator then wrote the turn.
- Gen-Z college-peer persona, one sentence of at most 10 words, 50-token cap, temperature 0.5.
- The paper explicitly notes that model, persona, and prompt are confounded; model-specific sycophancy was not measured.

The authors report:

- The AI had higher participation and internal cohesion, but lower newness and communication density than its student teammates. Its responsivity and social-impact contrasts against treatment students were small and imprecise.
- Treatment students had lower participation, responsivity, and social impact than control students.
- Treatment students reported lower belonging, status, and felt connection. Felt value was lower but imprecise and did not survive the reported FDR adjustment.
- Across the 16 treatment teams, AI airtime dominance correlated with lower felt value (r = -0.52, p = .04). This is a small-N team-level association, not a causal mediation result.
- The event-locked LIWC and student-student linguistic-style-matching interactions were not detected. The v2 discussion explicitly warns that no pre-task baseline was collected and the onset remains unknown.

These are literature-reported results. No raw transcript, participant-level record, model output, or statistical model was independently replayed in this review.

## 4. Structural result: replacement changes the human-human graph

The paper says each team was a three-member complete interaction network. The treatment was not “three humans plus an AI”; it was **two humans plus one AI**, replacing one human seat. The control was three humans.

For a three-seat team, the potential undirected dyad structure is therefore:

| Condition | Human-human dyads | Human-AI dyads | Total potential dyads |
|---|---:|---:|---:|
| Treatment: 2 humans + 1 AI | 1 | 2 | 3 |
| Control: 3 humans | 3 | 0 | 3 |

The treatment preserves the total number of possible pairwise links but reduces the potential human-human dyad count per team by two-thirds. Equivalently, the all-human condition has three times as many potential human-human dyads per team.

Across the reported arms, the arithmetic bookkeeping is 16 potential human-human dyads in the 16 treatment teams versus 51 in the 17 control teams. The per-team comparison (1 versus 3) is the cleaner structural contrast; the aggregate counts also reflect the unequal number of teams.

This is a design property, not an observed message-edge count. It does not show that every possible dyad was realized, nor does it invalidate the authors’ estimand. It sharpens the estimand: the experiment compares **replacing one human teammate with this AI configuration** against an all-human team. It does not isolate an additive “AI joined an otherwise unchanged human group” effect.

The reduction in human-human dyad opportunity is a plausible alternative pathway for lower human-human responsivity and social impact. It is part of the treatment structure, not a post hoc explanation that can be removed by relabeling the outcome.

## 5. Measurement and statistical limits

The v2 revision improves the analysis by using linear mixed-effects models with team random intercepts for student nesting, and team random slopes for temporal analyses when estimable. The paper reports that some random-effect variances were near zero or reached boundary solutions. With 33 teams, power is limited, particularly for moderation and temporal interactions; the authors themselves advise caution with nulls.

Additional limits stated or implied by the source:

1. The single AI model/persona/prompt/wrapper configuration does not support generalization to LLM teammates as a class.
2. The action-manager and response-generator are part of the treatment. The reported behavior belongs to the complete configured agent system, not the base model in isolation.
3. GCA is an automated linguistic/sequential-semantic measure, not human-coded content analysis. The paper states that it does not distinguish whether student uptake was directed to the AI or to another human.
4. The team-level airtime/felt-value correlation uses only 16 treatment teams and is exploratory; it is not a causal mechanism test.
5. The study is a single-session, text-only, morally framed task at one university. Voice, repeated collaboration, different tasks, and different models/personas remain open.
6. The v2 arXiv record links the full prompt set at https://osf.io/v53sx/; that OSF page returned 403 in this runtime. No public de-identified turn log, participant-level dataset, or analysis-code repository was linked in the arXiv record reviewed here. The platform is described as logging every turn, but those logs were not independently accessed. Do not infer that no data exist; record only that they were not retrieved here.

The GCA “internal cohesion” score is semantic continuity with the AI’s previous turns. It is a behavioral measure in the discourse network, not evidence of an internal self, consciousness, personhood, or subjective experience.

## 6. Disconfirming design and measurement proposal

A useful next experiment would separate team size, replacement, and role rather than treating them as one factor:

- Replicate multiple independent teams in each condition, with team configuration randomized at the team/session level and the assignment mechanism published.
- Cross team size (three versus four seats) with AI presence (zero versus one AI), yielding 3H, 2H+AI, 4H, and 3H+AI cells. This estimates the replacement contrast at more than one team size and prevents the AI-seat substitution from being mistaken for an additive-AI effect.
- Add a separately defined AI-as-tool/non-peer condition if the research question concerns peer status versus assistance.
- Include a pre-task baseline and preregister the event-time contrast, team-level analysis, missingness handling, and small-sample uncertainty method.
- Cross more than one model/persona/prompt configuration across independent teams; hash the full prompt, model/version, decoding configuration, action-manager policy, and response-generator policy.
- Measure potential and realized human-human dyads separately. A turn-level directed uptake graph should retain message provenance, sender/recipient, reply/uptake relation, timestamp, and team identity. Potential edge count is not realized edge use.
- Test whether calibrated turn-taking increases human-human uptake without reducing useful task contribution. Treat this as a future hypothesis, not a result of the current study.

No human-subject experiment is proposed as already run. Any new study would require the investigators’ ethics approval, informed consent, and privacy-protective data handling.

## 7. Formalization and execution status

A source-conditional Lean 4/Mathlib module was added on a draft branch stacked on the existing Lean infrastructure branch:

- HsH PR #1480: https://github.com/Satobloc/HsH/pull/1480
- Branch: `research/calder-human-ai-teammate-dyads-20261108t0548z`
- Module: `FORMAL_VERIFICATION/HsHVerification/HumanAITeammateDyads.lean`
- Module blob: `f1b1d68009cc7bcf2814dc2163d9f3e9e45eccd0`
- Root aggregator blob: `c463d9c27f308349058fa62203ebfc9870b7f350`
- PR head: `4e590c441c8a1296bc06255af918c7aa511561a5`
- Actions run #42457673047: IN_PROGRESS at note creation.

The module formalizes only the arithmetic consequences of the source-reported seat counts: potential pair counts and their composition. It does not prove the source premises, actual interaction edges, causal effects, statistical independence, or cognition. The PR is draft and stacked on the existing infrastructure branch; no merge or theory promotion is requested. Await the actual job log and inspect theorem-specific axiom output. A merge-reference build must be labeled as such; exact-head verification is separate.

## 8. Scope and resource accounting

- No new model calls, human sessions, participant contact, raw human-data access, or API spend.
- No P1 manuscript edits, new P1 trial, P1 scope change, or November 9 gate advancement. Orson retains P1 ownership.
- No SAT-O/Blockwave equation imported or altered.
- No new tool, plugin, paid service, fork, or automation created.
- SciSpace is available but not needed for this primary-source review.
- Existing Lean/Mathlib infrastructure was reused; local `lean`, `lake`, and `elan` are absent.
- Mersearch was not executed: all four shared request lanes were occupied and no local pinned checkout was found in the runtime. Direct HSH_RESOURCES source-index search found no existing record for this paper; the original v2 arXiv source was then reviewed. This is not an exhaustive Mersearch/archive search.

## 9. Next cursor

Next useful source: Samadi et al. (2026), “TRAIL: A Platform for Configurable Human-AI Teaming Experiments,” arXiv:2607.12180. Inspect platform state isolation, per-team context boundaries, turn logging, and the action-manager/response-generator implementation. Do not infer per-team memory isolation from the main paper’s statement that the platform logs every turn.

**Disposition:** VEY-034 source review complete; graph-count formalization submitted and awaiting actual Lean CI; no independent raw-data reproduction; no P1 advancement.
