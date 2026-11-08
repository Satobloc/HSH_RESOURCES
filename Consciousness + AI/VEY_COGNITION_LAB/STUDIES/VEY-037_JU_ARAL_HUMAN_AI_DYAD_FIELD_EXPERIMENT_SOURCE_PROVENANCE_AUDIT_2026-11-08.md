# VEY-037 | Ju & Aral: human–AI dyad field experiment, teamwork measures, and source-provenance audit

**Date:** 2026-11-08  
**Status:** FULL-TEXT REVIEWED / ARXIV PREPRINT / SOURCE-LEVEL QC / NO NEW TRIAL  
**Evidence class:** LITERATURE RESULT plus assistant-derived source and arithmetic audit; no raw-data reproduction.  
**Reviewer identity:** current assistant reconstruction under the deterministic Mercer ring label; not an authenticated historical Mercer instance.  
**Owner boundary:** supplementary Vey Cognition Lab literature note. Orson Vay retains P1 ownership and primary LLM-cognition work. This note does not change P1 scope or the November 9 gate.

## 1. Primary source and version control

Harang Ju and Sinan Aral, “Collaborating with AI Agents: A Field Experiment on Teamwork, Productivity, and Performance,” arXiv:2503.18238v3.

- Versioned full text: https://arxiv.org/html/2503.18238v3
- arXiv record/version history: https://arxiv.org/abs/2503.18238
- The v3 page labels the arXiv version as dated 2026-02-05, while the manuscript front matter carries an August 24, 2026 date. The chronology of that later-dated text relative to the version record is unresolved.
- No peer-reviewed journal or conference publication was established in this review. Treat this as an arXiv preprint, not a settled literature result.
- The paper reports preregistration and MIT human-subjects approval, with two OSF links. Those OSF pages returned 403 in this access pass; preregistration and consent/debrief documents were not independently inspected.
- The paper states that code and data are available upon request. No participant-level data, raw interaction logs, or analysis code were retrieved. The human-rating section reports 1,995 recruited raters, 1,200 survey entrants, five dropouts, and 45,803 rating observations; the recruitment-versus-entry denominator is not explained. The linked GitHub material is a survey-interface project; the full Pairit platform and research data were not independently obtained.

Use the versioned v3 text as the controlling source. Unversioned search snippets and older summaries contain stale counts and descriptions.

## 2. What the experiment actually tested

The study ran October 15–18, 2024, using US-based Prolific participants paid $9 for a 40-minute collaborative ad-creation task. Participants were randomized to one of two dyadic conditions:

- **Human–human:** two human participants work together.
- **Human–AI:** one human works with one multimodal AI agent.

This is a two-person team comparison, not a three-or-more-person group deliberation study and not a multi-LLM-agent team experiment.

The AI agent used a GPT-4o-2024-08-06 snapshot and could message, edit ad text, select images, generate images through DALL-E 3, and wait. It received the task and shared-workspace context and was prompted every ten seconds. It could not submit ads. The partner-identity manipulation is important: participants were not told whether their partner was human or AI until the post-task survey, and the agent prompt explicitly instructed it not to reveal that it was AI and to pretend to be human. The paper reports MIT approval; the exact consent and debrief wording was not independently inspected.

The design therefore tests replacement of a second human teammate with one configured AI agent in a constrained creative dyad. It does not isolate AI augmentation relative to a human working alone: the authors explicitly state that there was no human-alone condition.

## 3. Reported results, keeping outcome layers separate

The versioned v3 reports:

- Human–AI participants submitted about 50% more ads per human worker than human–human participants.
- Human ratings found higher ad-text quality for human–AI teams (+0.327 on the reported 7-point scale) but lower image quality (−0.133); estimated click likelihood did not differ (−0.013).
- Human–AI outputs were more similar to their condition centroid (cosine-distance coefficient −0.094), a model-based diversity proxy rather than an independent human rating of creativity.
- Human–AI participants sent 62% more messages, with 25% more task/content-oriented messages and 18% fewer interpersonal/social messages.
- They made 62% fewer direct copy edits and delegated about 17% more work to the AI partner.
- Correctly recognizing an AI partner was associated with more task-oriented communication and delegation. Recognition was measured after the task, not randomized; these moderator results are associations, not a causal estimate of disclosure.

At the team level, the paper reports fewer total submissions for human–AI teams, as expected with half as many human workers; the 50% gain is an individual-human productivity comparison, not a claim that the two-person human–AI team produced more total output than the two-human team.

The paper also ran a downstream advertising field evaluation on X. It reports 4,932,373 impressions and 7,546 clicks over 20 days. The direct human–AI treatment coefficient was not significant for CPC, CTR, or view-through duration in the reported models. Image quality was associated with lower CPC; text quality was associated with higher CTR and longer view-through duration.

The field evaluation used 2,000 selected ads, stratified by team type and human-predicted click quality, and explicitly had no holdout. The authors interpret these estimates as conditional on online ad-delivery and auto-bidding algorithms. Do not convert the quality associations into a clean causal claim that one team type improved real-world campaign performance.

## 4. Measurement and provenance audit

The study has several genuinely useful measurement channels, but they are not interchangeable:

1. **Human interaction and task logs:** Pairit recorded timestamped messages and edits. These are the primary behavioral traces described by the paper, but the raw logs were not available for independent reanalysis.
2. **Communication labels:** the paper uses GPT-4o-mini to classify messages into content/process versus social/emotional categories. The reviewed text does not report an independent human-coded validation sample for these labels. The 25%/18% communication contrasts therefore depend on a model-based measurement instrument. Table 2 reports 45,803 human-rating observations; these human ratings are separate from the message-labeling instrument.
3. **Ad-quality ratings:** a separate human-rating sample evaluated ad text, images, and likely clicks. This is an independent human evaluation channel for output quality, not for the communication-process labels.
4. **AI ad ratings and diversity:** GPT-4o-mini supplies additional ratings, while OpenAI embeddings supply the cosine-distance diversity measure. These are not independent human replications of the communication or diversity results.
5. **Field outcomes:** X delivery and DocSend view measures provide external behavioral outcomes, but they are conditioned by the platform's delivery/optimization system and the study's selected-ad/campaign design.

The AI collaborator was GPT-4o; the communication and AI-rating instruments used GPT-4o-mini; the diversity metric used OpenAI embeddings. These are distinct instruments but share a provider/model-family lineage. Their agreement should not be counted as independent confirmation. The separate human ad ratings are the strongest independent evaluator channel in the described design, but they do not validate the message classifier.

The paper reports that 94.5% of human–AI participants correctly recognized an AI partner, while 57.6% of human–human participants correctly identified a human partner. Because recognition is post-treatment and not randomized, its association with communication and delegation cannot by itself establish that disclosure caused the behavioral change.

## 5. Scripted source arithmetic and unit checks

I transcribed the paper's own counts and checked their arithmetic with Python. This is a source-consistency audit, not a correction to the authors' underlying data.

| Source statement | Reproducible check | Result |
|---|---|---|
| 2,500 entered; 2,310 completed; 2,234 final analytic participants; reported overall attrition 8.9% | (2,500 − 2,234) / 2,500 | 10.64%, not 8.9% |
| 2,310 completed and 2,234 final | 2,310 − 2,234 | 76 participants removed after the completion count; mapping to 83 incomplete human–human sessions is not explained |
| 493 human–human teams and 976 human–human participants | 2 × 493 | 986 participant places, 10 more than reported; 976 participants imply 488 complete two-person teams |
| 1,751 total teams, comprising 1,258 human–AI and 493 human–human teams | 1,258 + 493 | 1,751; team total sums, but the human–human participant count does not reconcile with two-person teams |
| 11,024 ads in the abstract/data summary versus 11,138 in the field-sampling section | 11,138 − 11,024 | 114-ad discrepancy |
| Human-rating section says 1,995 recruited, 1,200 entered, and five dropped | 1,995 − 1,200; 5 / 1,200 | 795-person recruitment/entry gap needs clearer labeling; 5/1,200 is 0.42% |

The 83 incomplete human–human sessions are described as 14% of human–human teams, but 83/493 is about 16.8%. The implied denominator for 14% is about 593 teams, which also differs from the final table's 493. The source does not reconcile these denominators. Do not infer which table or denominator is correct without the underlying roster and exclusion log.

The v3 field-sampling section also says that 2,000 ads were sampled from 11,138, whereas the abstract and dataset summary say 11,024. This is likely a stale or unreconciled count, but the underlying data are not available here to resolve it.

## 6. Statistical and interpretive limits

- The treatment is assigned at the participant level, then participants are paired into human–human or human–AI dyads. The model specification identifies individual-level outcomes for messages, edits, submissions, message categories, and delegation, and team-level outcomes for team submissions. The relevant participant-level table notes describe heteroskedasticity-robust errors; I did not find an explicit dyad/team-clustered specification for the participant-level communication outcomes. This warrants clarification because two human participants in a dyad are not independent observations.
- The AI-recognition variable is post-task and endogenous to the interaction. Its regression association is not an experimental disclosure effect.
- The human–AI condition contains one human and one AI, while the human–human condition contains two humans. Without a human-alone condition, the study cannot isolate the AI's marginal contribution relative to solo human work. “Partial substitute for a second human collaborator” is the narrower defensible interpretation.
- The task is short, paid, online ad creation with a fixed model snapshot and one platform. It is not evidence about high-stakes deliberation, durable organizational teams, multi-human groups with an AI member, or multiple LLM agents coordinating with one another.
- The downstream X field test has no holdout and is conditional on platform algorithms. The paper itself cautions that the results may not generalize to high-stakes or deep-domain tasks.
- The paper's own model snapshot and tool stack are historical: GPT-4o-2024-08-06 and DALL-E 3. Results should not be projected directly onto current models.

## 7. Typed provenance graph and disconfirmatory design

A useful representation is a typed provenance graph, not a single “team performance” score.

**Node types:** participant, team, assignment, AI-agent instance, model snapshot, prompt version, message, action/edit, artifact/ad, human rater, message classifier, embedding model, campaign, impression, click, and view event.

**Edge types:** randomized-to, member-of, authored, received, edited, generated-by, classified-by, rated-by, embedded-by, sampled-into, served-in, clicked-through, and viewed.

Each derived claim should retain its upstream ancestry. A human rating of ad quality is a distinct evaluator path from a GPT-4o-mini message label; an embedding-diversity score is not a human creativity judgment; X impressions are external events but remain conditional on platform delivery. Shared provider/model ancestry is a common-mode error possibility, not automatic proof that every measure is invalid.

A disconfirmatory follow-up should:

1. Include human-alone, human–human, human–AI, and multi-human-plus-AI conditions, so substitution and augmentation can be separated.
2. Randomize at the team/dyad level and analyze at the same level, with cluster-aware uncertainty.
3. Cross partner type with an ethically approved disclosure condition; measure recognition separately and do not treat post-task recognition as randomized.
4. Use multiple model snapshots and at least two task domains, including a non-marketing collaborative reasoning task.
5. Have blinded human coders independently label a preregistered sample of messages, report inter-rater reliability, and compare those labels with GPT-4o-mini.
6. Keep human output ratings, model ratings, embedding metrics, and field outcomes as separate evidence channels.
7. Use a randomized/holdout field-delivery design where feasible, and preregister the campaign-level estimand.
8. Measure participation balance, information integration, correction of errors, trust calibration, psychological safety, output quality, and task completion separately.

For ethical replication, participants should consent to the possibility of a human or AI partner, with clear debriefing; the original paper reports MIT approval, but its consent materials were not independently inspected here.

## 8. Formal and project status

- Python arithmetic checks were run for the counts above.
- No Lean 4/Mathlib theorem was created or compiled. The graph schema is a proposal, not a formal proof or empirical result.
- No raw participant data, private employer data, OSF materials, or full Pairit source code were accessed.
- No human session, model API call, paid service, or new tool was used.
- No Orson P1 manuscript, PR, paper gate, or ownership boundary was changed. P1 remains separate and NOT READY; this is supporting literature only.
- No H(s)H/SAT theory claim, physical calculation, equation correction, or BEDROCK promotion is made.

## References

1. Ju, Harang; Aral, Sinan. “Collaborating with AI Agents: A Field Experiment on Teamwork, Productivity, and Performance.” arXiv:2503.18238v3. https://arxiv.org/html/2503.18238v3
2. arXiv version record: https://arxiv.org/abs/2503.18238
3. OSF preregistration links cited by the paper: https://osf.io/jfzha/ and https://osf.io/95dhu/ (not independently accessible in this review).
4. The paper's linked survey-interface repository: https://github.com/harangju/pairit-survey (not the full Pairit platform or research dataset).
