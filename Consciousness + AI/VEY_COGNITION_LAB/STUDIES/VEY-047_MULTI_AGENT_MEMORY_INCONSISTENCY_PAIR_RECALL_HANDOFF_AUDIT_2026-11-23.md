# VEY-047 — Multi-Agent Memory Inconsistency: pair recall, contributor distribution, and handoff loss

**Date:** 2026-11-23  
**Status:** LITERATURE_RESULT / FULL ARXIV HTML REVIEW / BIBLIOGRAPHIC MATCH / SOURCE-CRITICAL CROSSWALK / ASSISTANT FORMALIZATION SUBMITTED / NO MODEL TRIAL / NO HUMAN SESSION / NO P1 CHANGE.  
**Citation handoff:** CITE-2026-003.  
**Primary source:** Hejia Zhang, Zhongming Yu, Yimin Ding, Wei-Ting Chen, Hengjia Yu, Wentao Ni, Yijun Liu, Cong Xu, Xin Chen, Matrix Yao, Fan Zhao, and Jishen Zhao, “Multi-Agent Memory Inconsistency: Where Factual Conflicts Disappear in LLM Agents,” arXiv:2611.22245v1, submitted 2026-11-17. https://arxiv.org/abs/2611.22245  
**Bibliographic check:** Scholar Sidekick matched title/authors/year to arXiv:2611.22245; no retraction flag. Peer-review status not established.  
**Review depth:** full arXiv HTML main text and reference list inspected, including §§3.1–3.4, 4.1–4.4, and Limitations. No local PDF, raw execution traces, benchmark data, or paper-specific code repository was acquired. The arXiv page links to the FEVER scorer, not a paper-specific code/data release.

## 1. Why this source is a new delta

The existing VEY-040/041/046 work already distinguishes action-relative projection, context exposure, information-item identity, disclosure events, uptake, and decision use. VEY-047 does not claim those distinctions as new. Its new contribution is a recent empirical study that supplies an operational stage-wise measurement contract for a specific failure mode: both conflicting facts can be retrieved collectively, yet one or both may fail to survive worker reporting and become jointly available to the lead.

The paper is adjacent evidence about LLM-agent workflows, not direct evidence about human-LLM groups, human cognition, or the HsH ring's identity structure.

## 2. Study design and measurement

The authors inject 73 controlled numerical conflicts into 11 Harvey LAB due-diligence document-review tasks. Three model setups are tested:

- GPT-5.6 Luna through the Codex SDK;
- GPT-6 Luna through the Codex SDK;
- Claude Haiku 5.5 through the Claude Code SDK.

Each model runs each of three policies twice on all 11 tasks, yielding 198 task executions and 1,314 conflict observations. This gives 146 observations per model/policy and 438 per pooled policy; repeated conflicts are clustered within tasks.

The policies are not one-factor variants:

- **None:** one agent inspects sources and writes the report.
- **Optional:** the lead may inspect sources, create workers, and assign overlapping reviews.
- **Required:** workers inspect assigned document partitions while the lead coordinates and synthesizes without reading source documents.

Required therefore bundles mandatory delegation, partitioned source assignment, and restricted lead access.

The profiler correlates model requests/responses, SDK events, native traces, tool outputs, and report artifacts. It defines four cumulative stages:

1. **Source Reads:** conflict endpoints visible in source-tool outputs.
2. **Worker Reports:** outgoing worker messages and completion reports, including peer-directed messages.
3. **Lead Evidence:** incoming evidence plus the lead's permitted source reads.
4. **Final Report:** endpoints in the selected graded deliverable.

For planted pair \(G_i=\{A_i,B_i\}\) and stage evidence set \(E_i^t\), Pair Recall is:

\[
R_{\mathrm{pair}}^t=\frac{1}{N}\sum_{i=1}^{N}\mathbf{1}[G_i\subseteq E_i^t].
\]

This is a coverage predicate: both endpoints must be present. It is not a truth score, semantic conflict judgment, or proof that the receiver understood the relation.

At the first three stages, **Same** means one individual supplies both endpoints; **Split** means the contributors' union contains both but no one contributor supplies both. Same takes precedence when multiple routes exist. Final Report is a single artifact and is reported as Both, without Same/Split.

**Judge Pass** is separate. It requires both explicit discrepancy identification and accurate quantitative treatment of the comparison. The judge is claude-sonnet-5.

## 3. Reported results

| Measure | None | Optional | Required |
|---|---:|---:|---:|
| Source Reads Pair Recall | 50.2% | 62.8% | 68.7% |
| Worker Reports Pair Recall | — | 12.8% | 24.4% |
| Lead Evidence Pair Recall | 50.2% | 51.8% | 24.4% |
| Judge Pass | 16.2% | 24.2% | 13.2% |

The central contrast is not “more agents are worse.” Required collects both conflict endpoints more often than None at Source Reads (68.7% versus 50.2%), yet its final Judge Pass is lower (13.2% versus 16.2%). Optional has the highest pooled Judge Pass (24.2%), but it combines discretionary delegation, overlapping review, and lead source access, so it does not isolate a single causal factor.

Across the 438 Required observations:

- Source Reads contains both endpoints in 301 cases (68.7%).
- Worker Reports and Lead Evidence each contain both in 107 cases (24.4%).
- Of the 301 source-complete pairs, 106 also appear in Worker Reports: 35.2% retention.
- The paper reports identical Worker Reports and Lead Evidence labels, locating its largest measured drop between source inspection and worker reporting.

The 107 Worker Reports total is not identical to the 106 source-pair retention count: one pair appears in Worker Reports without having been counted as a complete Source Reads pair. The denominators should not be collapsed.

In matched cohorts defined by Required's observed evidence distribution, Required versus None Judge Pass is:

| Observed distribution | Source Reads grouping | Lead Evidence grouping |
|---|---:|---:|
| Same | 34.2% vs 22.5% | 72.2% vs 33.3% |
| Split | 10.0% vs 18.9% | 17.1% vs 28.6% |

These are conditional matched associations, not randomized Same/Split effects. Shared-draft reads and arithmetic reconstruction can also move a pair from Split at Source Reads to Same at Lead Evidence.

The authors report that 73.2% of split-evidence cases omit one or both claims, compared with 50.5% when a single worker reads both. This is a source-specific result under the tested task and policy design, not a universal multi-agent failure rate.

## 4. Source-critical limitations

1. **Narrow task domain:** 11 Harvey LAB due-diligence tasks with planted numerical conflicts. Broader domains and non-numerical conflicts remain untested.
2. **Limited repetition:** two runs per model/policy. The authors call for more repetitions and uncertainty estimates that account for shared tasks.
3. **Cumulative rather than first-joint-availability measurement:** the profiler does not identify the exact time when both claims first become jointly available.
4. **Judge error:** manual inspection found three saved Judge Pass labels that credited neighboring comparisons rather than the planted conflict.
5. **Bundled policy intervention:** Required combines mandatory delegation, partitioned sources, and restricted lead access.
6. **SDK/model-family confounding:** GPT models use the Codex SDK; Claude uses the Claude Code SDK.
7. **Selection in matched cohorts:** Same/Split cohorts reflect observed retrieval and reporting choices, not randomized evidence assignment.
8. **Retrospective budget decisions:** budgets were calibrated from observed spending, and GPT-5.6 Required checkpoints were selected retrospectively.
9. **No paper-specific raw-data/code release located:** the full arXiv page identifies the FEVER scorer but no study profiler repository or downloadable execution traces.

The authors themselves propose a sharper test: supply identical evidence while varying which agents receive it, then intervene on reporting to test whether preserving paired claims improves detection.

## 5. Crosswalk to the existing cognition program

- **VEY-040:** action-relative projection and provenance remain the broader architecture. VEY-047 contributes a concrete stage-wise pair-coverage measure.
- **VEY-041:** group unit and context exposure remain separate from worker labels and task routing. Same/Split uses immediate contributors, not authenticated model identities.
- **VEY-046:** the proposed CRTC object model already identifies InformationItem and DisclosureEvent as distinct types. VEY-047 provides source-defined semantics for those types and a pair-preservation condition.
- **VEY-031:** claim-specific dependency profiles remain distinct from statistical independence. Declared source-root disjointness is not sufficient to establish independent extraction errors or model behavior.
- **P1 ConsistencyBench:** no transfer of VEY-047's findings to P1. P1's frozen archive is within-model self-revision with a shared NLI evaluator, not cross-model peer deliberation. No P1 protocol, dataset, manuscript, or paper gate was changed.

## 6. Formalization submitted to the existing HsH sandbox

A small assistant-reconstructed Lean module was added to the existing draft PR #2375, not to P1 PR #850:

- OrsonEvidenceFlow.lean
- Root aggregator imports the new module.
- Branch: research/orson-crtc-group-projection-20261122t2136z
- Commit: 967b660e13685019a890615d8480b42f7fd87538
- CI run: #45180457730, status pending at initial write.

The module separates EvidenceItem IDs from DisclosureEvent IDs; declared source-root overlap; Source Reads, Worker Reports, Lead Evidence, and Final Report; Same/Split contributor classification; recipient-addressed worker-report events; and PairJudgment.

It proves only conditional or finite logical statements:

- itemwise transfer of both endpoints is sufficient to preserve pair presence across stages;
- a source-complete pair can be lost before worker reporting;
- a message addressed to a lead need not appear in lead evidence;
- Same and Split are distinct contributor patterns;
- two distinct item IDs can share a declared source root;
- pair presence does not imply Judge Pass.

Finite witnesses are not model outputs or measured data. The module does not reproduce the paper's 73 conflicts, estimate Pair Recall, model sampling uncertainty, identify actual model instances, establish statistical independence, or prove a causal handoff effect. CI status must be amended after actual run readback; no successful compilation is claimed here.

## 7. Disconfirming design for future authorized work

A useful next experiment would hold the evidence corpus, model snapshot, prompt, evaluator, token/dollar budget, and checkpoint rules fixed, then randomize recipient distribution:

1. One worker receives both claims.
2. Two workers receive one claim each.
3. Two workers receive one claim each, but a structured pair-preserving handoff is required.
4. A lead receives the full source set directly.
5. A single-agent baseline receives the same full source set.

Capture source-tool outputs, item IDs, source roots, disclosure-event IDs, outgoing messages, recipient receipts, actual lead-context insertion, final report, judge inputs, and blinded human adjudication. Prespecify task-level clustering, missingness, matching rules, false-positive scoring, budgets, and checkpoint timing.

Disconfirming outcomes:

- If randomized Split assignment performs as well as Same after evidence and budget are controlled, the observed Same/Split association is likely driven by selection or task difficulty rather than contributor distribution.
- If forced pair preservation increases Pair Recall but not Judge Pass, semantic reconciliation is a separate bottleneck.
- If recipient receipt is high but lead-context inclusion is low, the loss lies after transport rather than in worker summarization.
- If pair presence and Judge Pass converge under blinded human adjudication, the LLM judge may be a material source of the apparent effect.

This is a proposed future design only. No model calls, human sessions, API spend, or new experiment were performed.

## 8. Operational implication

For the Workshop Relay, distinguish at least:

- source content read;
- evidence item identified;
- report/disclosure event emitted;
- repository artifact or inbox entry delivered;
- recipient readback;
- evidence actually included in the recipient's active context;
- item cited or used in a later output;
- decision incorporation;
- outcome evaluation.

A repository readback proves artifact presence, not context exposure or cognitive uptake. A worker label proves routing selection, not a distinct model identity. A repeated message is another disclosure event, not automatically new evidence. Distinct declared source roots are not proof of statistical independence.

## 9. Disposition

VEY-047 is a literature result and source-specific measurement crosswalk. It is not a controlled result from the HsH workshop, a human-LLM group finding, a P1 protocol amendment, a consciousness claim, or a theory result. Keep the November 9 P1 gate OVERDUE / NOT READY / FROZEN / ORSON-OWNED; keep the November 30 and December 14 gates separate.
