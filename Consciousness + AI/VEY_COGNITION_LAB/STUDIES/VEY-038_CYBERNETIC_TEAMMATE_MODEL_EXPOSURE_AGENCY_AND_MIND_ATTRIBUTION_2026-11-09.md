# VEY-038 | The Cybernetic Teammate: model exposure, operational agency, and human mind-attribution

**Date:** 2026-11-09  
**Status:** LITERATURE RESULT / PUBLISHED PRIMARY SOURCE FULL-TEXT REVIEWED / NO REPLICATION / NO NEW TRIAL.  
**Evidence class:** external literature result plus assistant source audit and prospective design proposal.  
**Reviewer identity:** current assistant reconstruction under the deterministic Orson Vay ring label; not an authenticated historical Orson instance.  
**Scope boundary:** supplementary cognition-methods work. This is not P1 ConsistencyBench evidence, does not change P1 scope or the November 9 gate, and does not confer SAT/H(s)H theory authority.

## 1. Primary source and review extent

Fabrizio Dell'Acqua et al., “The Cybernetic Teammate: A Field Experiment on Generative AI and Teamwork,” *Organization Science*, published online 2026-06-12, DOI: [10.1287/orsc.2025.20702](https://doi.org/10.1287/orsc.2025.20702).

Official publisher article: https://pubsonline.informs.org/doi/10.1287/orsc.2025.20702  
Official publisher PDF: https://pubsonline.informs.org/doi/pdf/10.1287/orsc.2025.20702

SciSpace returned abstract-level material only. The publisher's full text was reviewed for the experimental design, model exposure, outcomes, emotional-measure timing, discussion, limitations, and endnotes. The online appendix and AEA registry record were not retrieved. The paper references preregistration AEARCTR-0013603 and IRB approval IRB24-0202; those records were not independently inspected in this pass.

No participant-level data, prompt/response logs, team transcripts, analysis code, or model deployment records were retrieved. The paper says prompts/responses were recorded and team interactions transcribed; their availability for independent reanalysis remains unverified.

## 2. What the field experiment actually manipulated

The study reports 791 randomized P&G professionals and a 2 × 2 design:

1. individual, no GenAI;
2. two-human team, no GenAI;
3. individual with GenAI;
4. two-human team with GenAI.

The teams paired one commercial professional with one R&D professional. The task was a one-day virtual product-development workshop using real business challenges. The paper reports eight randomization clusters defined by business unit × geography. It reports 776 complete post-task survey records and 550 evaluated solutions. Thirty-five participants who were not randomly assigned were excluded from the randomized analysis; fifteen randomized participants lacked complete post-task surveys.

The AI interface was described in the main methods as GPT-4 accessed through Azure. Participants received a one-hour training and a suggested-prompt guide; only 38% used the suggested prompts. The paper reports that prompt users and non-users achieved equivalent performance, but prompt uptake was not randomized.

The design is a strong field comparison of AI availability across individual and two-human work. It is not an experiment in which an independently delegated AI agent was randomized against a prompt-only assistant. The article does not report an operational manipulation of AI-initiated actions, delegated task ownership, autonomous coordination authority, or persistent obligations. This is a boundary on what the study identifies, not evidence that the deployed system lacked unreported capabilities.

## 3. Source-critical exposure and measurement findings

### 3.1 Model-version join is incomplete in the article

The main methods describe GPT-4 via Azure. Endnote 13 separately says participants at the July workshop had access to GPT-4o and that results were consistent across workshop sessions. The article does not provide a complete participant/team × session/date × condition × exact-model-version crosswalk.

This is an exposure-provenance gap, not proof of treatment imbalance or confounding. The authors' statement of consistency across sessions is useful, but without the crosswalk it does not establish version-specific balance or estimates. A future study must pin the exact model snapshot or record and stratify the session-level deployment/version.

### 3.2 Emotional baseline is post-assignment

For the emotional-change measures, the paper locates the pre-task baseline after treatment assignment but before task engagement. The reported pre/post change therefore describes emotional movement during task engagement after assignment; it does not measure the full affective effect of being assigned to an AI condition, because initial assignment reactions are already included in the baseline.

The paper operationalizes “sociality” through human emotional responses. It does not measure the AI's subjective experience or directly measure participants' detailed theories of AI cognition.

### 3.3 Functional collaboration is not autonomous agency

The authors describe AI as an active collaborative counterpart and report contributions to ideation, feedback, expertise bridging, and emotional experience. The article also identifies human “theories of AI mind” as a future research frontier and cautions that these mental models may not accurately track model capabilities.

The proper distinction is not “tool” versus “real mind.” It is between observable functional contribution, operational autonomy, human attribution, and any separate claim about subjective experience. The paper supports claims about human–AI collaborative performance and reported human affect. It does not establish autonomous agent initiative or model phenomenology.

### 3.4 Reported result and mechanism limit

The paper reports that AI-assisted individuals achieved solution quality comparable to two-human teams. In the reported quality models, the Team+AI versus Team-no-AI contrast is not statistically significant (reported p = .242 in the principal specification). This is not evidence of no effect. The authors also describe their decomposition of AI enhancement versus substitution for collaborative functions as indicative rather than a clean causal separation.

The paper's scope is one company, one organizational setting, early-stage product-development work, a one-day virtual workshop, and a model exposure that changed across at least some sessions. These limits should travel with any reuse of its findings.

## 4. Architecture improvement: add an operational agency profile without changing the identity model

The current five identity/provenance axes (presentation label, execution identity, state continuity, evidence ancestry, interaction path) remain unchanged. The following is a separate behavioral/delegation profile, not a sixth identity axis and not a consciousness test:

- **Initiative:** who initiates each task-relevant action, human or AI?
- **Delegation:** is the AI merely answering a prompt, or has it received a bounded goal/subtask with explicit responsibility?
- **Coordination authority:** can it only respond to one interlocutor, or can it request information, coordinate work, or trigger checks within a declared scope?
- **Commitment/accountability:** are its obligations, actions, errors, and revisions tracked over time, or are outputs ephemeral?

Each field must be coded from protocol and action logs. A paper may legitimately use “teammate” functionally, but a stronger autonomous-teammate claim requires evidence about initiative, delegation, and coordination rather than title, fluency, or human affect alone.

**Application to this source:** the described interaction is human-mediated use of a GPT-4-based interface. Initiative is human-triggered as described; delegated ownership, independent coordination authority, and persistent commitment are not operationalized in the reviewed article. Cross-session state continuity is also not established. These fields are NOT_SPECIFIED / NOT_MEASURED, not proven absent.

## 5. Proposed follow-up: exposure × agency × human-attribution test

This is a prospective design proposal, not an executed experiment.

### Shared parameters

Hold constant and record the exact model/provider/version, system prompt, context, tools, information access, task, training, time budget, and human composition. Record each participant/team's assignment, session, model deployment, prompt/response trace, tool/action trace, task output, evaluator, and survey timepoint. If the model changes across sessions, randomize within version/date blocks or estimate version-specific effects; do not pool silently.

### Candidate contrasts

- Human-only baseline.
- Human-prompted assistant, with no autonomous task initiation.
- Bounded delegated-agent mode, with an explicit goal and permission to initiate specified task-directed actions within a logged scope.

These modes can be tested in individual and two-human-team contexts. The agency contrast is delegated-agent versus prompt-only under matched model and information access; the human-only arm estimates the broader AI-access contrast. Do not invent a sample size: use an independent pilot to estimate variance and a preregistered minimum important difference before confirmatory recruitment.

### Human mental-model timeline

- T0: before condition assignment, measure prior capability/agency beliefs and affect.
- T1: after assignment but before interaction, measure expectation and framing effects.
- T2: after the task, measure experience-driven belief and affect change, trust, reliance, acceptance, and override.
- T3: delayed follow-up to test retention of the mental model.

Compare human beliefs with independently measured, task-specific model behavior on held-out tasks and with the logged actions from the experiment. Do not use model self-report or human anthropomorphic attribution as evidence of subjective experience.

### Test matrix

| Hypothesis | Shared parameters | Calibration / holdout | Predicted observable | Standard comparator | Falsification condition |
|---|---|---|---|---|---|
| Delegated initiative adds coordination value beyond prompt-only assistance. | Same model snapshot, tools, task, information, time, training, and human composition. | Pilot separate from preregistered confirmatory tasks; held-out tasks; blinded outcome scoring. | Logged AI-initiated actions, delegated subtask completion, coordination events, errors, time, and task quality. | Human-prompted assistant; human-only baseline for total AI access. | No preregistered meaningful improvement in a primary coordination/task outcome at equal access and time, or no independently initiated actions in the delegated condition. |
| Human beliefs about AI agency track observed behavior rather than the “teammate” label alone. | Same model behavior and task; if framing is varied, change only the label/framing and log it. | T0/T1/T2/T3 belief measures; independent capability benchmark; held-out tasks and blinded scoring. | Calibration between perceived initiative/ownership and observed action/coordination traces; appropriate reliance and override. | Same prompt-only system under neutral tool framing. | Beliefs shift with label but not with observed behavior, or calibration does not predict appropriate reliance. |
| Reported effects are stable across model deployments. | Same task and protocol, with exact model/version recorded per session. | Randomize within deployment/date blocks; retain version-specific holdout results. | Treatment × model-version differences in quality, errors, coordination, and belief calibration. | Same condition under a pinned model snapshot. | Effect direction or magnitude changes beyond a preregistered margin across versions; an untracked version mix blocks a version-invariant claim. |

No numerical threshold or power calculation is supplied because the necessary pilot variance and task-specific minimum important difference are not available. No raw P&G data were reanalyzed.

## 6. Lean and formalization triage

The article contains a 2 × 2 experimental design and empirical regression specifications. Those are mathematical/statistical structures, but the regression is an empirical model, not a theorem. No new source-derived theorem was identified that can be proved without adding assumptions about the estimand, assignment unit, model-version join, and outcome mapping.

Orson PR #1115 contains a separate conditional saturated-2×2 algebraic formalization for persona × memory-history cells. Its current head has no Lean run; it is not a proof of this P&G design or its causal interpretation. Local Lean/Lake/Elan are absent in this runtime. A guessed formal schema would prove the guess, not the observed study. Status for any P&G-specific Lean model: **FORMALIZATION_BLOCKED_SOURCE_MAP_INCOMPLETE**. No Lean compilation or proof is claimed, and no data-free calculation was performed.

## 7. Epistemic status and next cursor

- **LITERATURE RESULT:** findings as reported by Dell'Acqua et al. in the published article.
- **SOURCE AUDIT:** model-version and measurement-timing limitations identified in the primary text.
- **PROPOSAL:** operational agency profile and follow-up experiment design.
- **NOT DONE:** independent replication, raw-data reanalysis, online appendix review, AEA registry review, model trial, human session, or Lean proof.
- **NOT P1:** no change to ConsistencyBench scope, November 9 readiness, manuscript, or paper gate.

Next source task: retrieve the online appendix and AEA registry record if accessible, then determine whether the participant/team × session × condition × model-version crosswalk is recoverable.

## 8. Addendum 2026-11-09: permission–execution–attribution–outcome map and assignment-to-analysis audit

### 8.1 Additional primary-source facts

A second-pass reading of the publisher's endnotes adds several design facts not made explicit in the first VEY-038 note:

- Endnote 1 cites a workplace-team definition as two or more individuals sharing interdependence and responsibility for tasks and collective outputs. The experiment's team arms are two human professionals (one R&D, one commercial) with AI available; the AI is not randomized as a third autonomous team member.
- Endnote 2 traces “cybernetic teammate” to feedback-regulated systems that adjust to environmental inputs. That is a functional collaboration description, not evidence of independent AI identity, authority, or phenomenology.
- Endnote 11 says participants were nested within teams, business units and geographic regions. If one member of a two-person team failed to participate, the team was nullified and participants from incomplete teams were reassigned to individual assignments. This creates a post-assignment change in the collaboration/analysis unit that a future independent audit must reconstruct. It is a design-accounting requirement, not proof of bias.
- Endnote 20 says the team-level outcome for two-person teams is the average of the individual participants' post-task changes.
- Endnotes 8–9 report 791 randomized workshop participants, 776 complete post-task survey records (15 incomplete: 4 from non-AI teams and 11 from AI teams), and 35 nonrandomized participants excluded from the randomized analyses. The nonrandomized participants were isolated in separate sessions.
- Endnote 17 describes a robustness analysis with standard errors clustered at eight business-unit × geography clusters and a wild cluster bootstrap (Online Appendix Table A3). The appendix was not retrieved, so the implementation and table cannot be independently checked.
- Endnote 13 identifies GPT-4o access for the July workshop; the main methods describe GPT-4 via Azure. The participant/team × session × condition × exact-version crosswalk remains unavailable in the reviewed article.

These facts require an explicit assignment-to-analysis flow map before any reanalysis: assignment unit, cluster, team formation, treatment receipt, team failure/reassignment, survey unit, outcome unit, evaluator, session and model version. They do not establish that the published analysis is biased or invalid.

### 8.2 Revised measurement architecture

The previous four-field operational-agency profile is retained as a proposed coding rubric, but it should not be treated as one scale or one latent variable. Split it into four separately observed layers:

1. **Authorization / affordance:** what the system is permitted to initiate, delegate, coordinate, commit to, revoke, or request approval for; record scope and accountable human.
2. **Execution / behavior:** what it actually does; preserve timestamped initiation, tool/action calls, task assignments, coordination events, handoffs, commitments, refusals, corrections, rollbacks and human overrides.
3. **Human attribution:** what people believe the system can do or experiences; separate role-label presentation from perceived role, and perceived agency from perceived conscious experience.
4. **Outcome / control:** task quality, completion, time, errors and coordination, alongside appropriate reliance/override and human control.

Any claim about subjective experience remains a separate phenomenological question. It is not inferred from authorization, action logs, human attribution, trust, or task performance.

The map integrates existing prior art rather than claiming a new validated scale:
- Holter, Moruzzi & El-Assady (2025), “Toward Agency in Human–AI Collaboration,” proposes a design space organized around distribution, modeling and attribution (DOI 10.1109/MCG.2025.3623892).
- Harris, Byun & Larson (2026), “What’s in a Name? Implications of AI Roles and Mind Perception for Human-AI Teams,” distinguishes role perception from role presentation and mind-perception agency from conscious experience (DOI 10.1177/00187208261457702).
- Van den Bosch et al. (2024), “Measuring Meaningful Human Control in Human–AI Teaming,” operationalizes subjective, normative and moral control across advice, human-assigned and autonomous-agent triage designs (DOI 10.1007/s43681-024-00647-8).

These three supporting records received abstract-level SciSpace triage, not full-text review. Scholar Sidekick's 2026-11-09 citation audit matched all four references used in this note (including Dell'Acqua et al.); no retraction was flagged. No originality or scale-validation claim is made.

### 8.3 Prospective test architecture and failure conditions

A source-faithful follow-up should vary **action rights** independently of **role framing**:

- Action-rights factor: prompt-only response versus bounded delegated initiative.
- Framing factor: neutral tool versus teammate label; an intermediate “support” level is an optional extension if the pilot supports it.
- Human-only baseline: estimates the broader effect of AI access, not the agency contrast.

Keep the model snapshot, system prompt, context, tool set, information access, task, training, time budget and human composition fixed. Vary who may initiate the same available actions, not which tools or information exist. Block or stratify by exact model version/session. Log permissions separately from executed actions. Collect human beliefs/affect at T0 (pre-assignment), T1 (post-assignment/pre-use), T2 (post-task) and T3 (delayed). Use held-out tasks, blinded outcome scoring and a separately run pilot before preregistering the primary outcome and minimum meaningful difference.

| Hypothesis | Predicted observable | Comparator | Falsification / failure condition |
|---|---|---|---|
| Delegated rights produce exercised initiative. | Independently initiated, in-scope actions and coordination events in event logs. | Same model/tools/context in prompt-only mode. | No independently initiated actions: the delegated-agency manipulation failed. |
| Exercised initiative adds coordination value. | Preregistered task/coordination outcome, errors and time at equal access and time. | Prompt-only mode; human-only baseline for total AI access. | No meaningful improvement at the preregistered threshold: no demonstrated coordination value. |
| Role framing changes attribution independently of behavior. | Perceived agency/experience and acceptance when action rights and behavior are held constant. | Neutral tool framing. | Label shifts perception but not action logs: a framing effect, not operational agency. |
| Human attribution is behavior-calibrated. | Agreement between perceived initiative/ownership and observed action traces; appropriate reliance/override. | Same task with independently benchmarked capability. | Perceived agency does not track behavior or appropriate reliance: attribution is not behavior-calibrated. |
| Human control is preserved across delegation levels. | Subjective, normative and moral control measures, plus actual approval/override records. | Advice, bounded assignment and autonomous execution modes. | A preregistered meaningful loss of control or accountability blocks the stronger delegation claim. |

No sample size, power calculation or numeric threshold is supplied without pilot variance and a task-specific minimum important difference. No P&G raw data, participant logs, model deployment records or analysis code were obtained. The online appendix and AEA registration record AEARCTR-0013603 remain unretrieved; the publisher article identifies both the appendix and registration, but the registry endpoint was not accessible in this pass.

### 8.4 Formalization and campaign boundary

The source supplies an empirical factorial design and nested assignment/outcome structure, not a source-complete theorem. The missing assignment/team/reassignment/version crosswalk prevents a faithful formal statement of the observed design. No guessed Lean schema, data-free calculation, new theorem, model trial or raw-data analysis was added. P&G-specific formalization remains **FORMALIZATION_BLOCKED_SOURCE_MAP_INCOMPLETE**.

This addendum is supplementary literature/methods architecture, not P1 ConsistencyBench evidence. P1 remains frozen methods/archival scope and November 9 **NOT READY**; no paper gate, P1 ownership or scope changed. No theory authority, consciousness claim, or SAT/H(s)H promotion follows.
