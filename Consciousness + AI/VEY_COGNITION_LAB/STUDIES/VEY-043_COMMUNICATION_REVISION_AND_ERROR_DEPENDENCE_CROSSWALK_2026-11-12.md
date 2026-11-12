# VEY-043 — Communication revision and passive error dependence (2026-11-12)

**Status:** SUPPORTING LITERATURE CROSSWALK / primary identifiers verified / structured full-text extraction reviewed / direct PDFs, appendices, data and code not retrieved. Not a replication, administered experiment, P1 protocol amendment, or paper-gate advancement.

## Question

When does apparent agreement among LLMs overstate independent evidence? The new sources add a distinct causal evidence class: peer-message exposure that changes a receiver's answer after independent reasoning. This must be kept separate from passive error covariance, shared-evaluator dependence, and deliberative aggregation.

## New primary-source comparators

### Li et al. (2026), arXiv:2610.01042

Shixuan Li, Wei Yang, Peiyu Zhang, Anzhe Cheng, Heng Ping, and Paul Bogdan, "Beyond Final Accuracy: Auditing Communication in LLM Multi-Agent Systems" (1 October 2026). https://arxiv.org/abs/2610.01042

The paper introduces Independent–Communicate–Revise (ICR). Its unit is a directed revision event: agents first reason independently, then a receiver revises under a specified communication condition. The paper compares no message, answer-only, and full-text communication, and also examines latent communication and receiver-policy variation. It reports four reasoning benchmarks, with additional receiver-policy comparisons on MedQA and GPQA-D.

The abstract reports that similar final accuracy can conceal different revision behaviour. Relative to answer-only transmission, full reasoning increases correction while reducing preservation across all four benchmarks. A structured verification policy shifts channels toward greater preservation and lower correction, while selectivity varies by channel and task.

**Interpretation:** richer messages can increase both useful and harmful influence. A receiver policy that preserves more answers may also correct fewer initial errors. Final accuracy alone can hide this trade-off.

**Limits:** the accessible structured extraction did not provide numerical effect magnitudes or confidence intervals. It describes a no-message revision control, but its exact operational equivalence to a true no-additional-reasoning counterfactual needs direct PDF/appendix inspection. Runtime and cost figures are described as run-specific, not controlled throughput comparisons. Direct PDF, appendices, raw data and code were not retrieved.

### Gong et al. (2026), arXiv:2609.36855

Yaxin Gong, Gangyi Zhang, Chongming Gao, Leyang Shen, Chenxiao Fan, Jiakai Wang, Dong Wang, Yang Liu, Wenjie Wang, and Xiangnan He, "When Upstream Messages Override Correct Answers: A Controlled Study of Multi-Agent LLM Collaboration" (29 September 2026). https://arxiv.org/abs/2609.36855

The study uses a directed upstream-to-downstream handoff. It holds the downstream task and evidence fixed while varying whether the receiver sees no message, the upstream message, or a message with the opposite conclusion. The abstract reports five benchmarks and five receivers, with further manipulations of conclusion content, attribution, and evidence availability.

The abstract reports that an incorrect upstream message changes an answer in **up to 32% of cases where the receiver would otherwise be correct**. It also reports that **94% of audited harmful cases** involve copying the upstream agent's specific wrong answer, termed answer substitution.

These are qualified author-reported results: 32% is an "up to" maximum, not a pooled rate; 94% is conditional on an audited harmful subset, not all messages or tasks. The exact denominators for both headline figures were not recoverable from the structured full-text extraction available in this run. No denominator reconstruction or new percentage calculation is claimed.

**Interpretation:** under the tested handoff conditions, peer-message content can causally displace a receiver's answer even when the receiver has sufficient independent evidence. This is not passive error correlation and not a shared-judge effect.

**Limits:** the result is bounded to the tested models, benchmarks, handoff architecture and message manipulations. Direct PDF, appendices, raw data and code were not retrieved; exact per-benchmark denominators and the audited-case selection rule remain open.

## Crosswalk with existing evidence

| Evidence class | Source | What it measures | What it does not establish |
|---|---|---|---|
| Passive error dependence | Hossain et al. (2026), arXiv:2609.22512; VEY-013 | Correlation among judge errors on common items | Peer-message causation |
| Shared evaluator / within-model revision | ConsistencyBench CGD, frozen P1 archive | Target-model self-history evaluated through a common GPT-4o-mini NLI checker | Cross-model peer exposure or social conformity |
| Peer-message revision | Gong et al. (2026), arXiv:2609.36855 | Receiver changes under manipulated upstream messages with receiver evidence fixed | General behaviour of every multi-agent system |
| Communication-channel revision | Li et al. (2026), arXiv:2610.01042 | Correction and preservation under message channels and receiver policies | A universal channel ranking independent of receiver policy |
| Deliberative aggregation | Barrera-Lemarchand et al. (2026), arXiv:2609.22497; VEY-012 | Group-level deliberation versus passive aggregation in tested domains | Independence of individual errors or harmlessness of every message |

Hossain and Barrera-Lemarchand were already indexed and reviewed in VEY-013 and VEY-012 respectively; they are reused as comparators, not presented as new discoveries.

The current ConsistencyBench CGD archive contains 17 target-model output files and records within-model self-history/self-revision. The same NLI checker is shared across target outputs. The archive does not expose cross-model peer answers. It supports a bounded study of evaluator and within-model revision structure, not a claim that the 17 target models deliberated with one another.

## Measurement implication

Keep four measurements separate:

1. **Baseline error dependence:** estimate error covariance from blind, pre-exposure answers on common items.
2. **Evaluator dependence:** score the same frozen answers with a shared evaluator and independent blinded adjudicators.
3. **Peer-exposure effect:** randomize no-message, correct-message and wrong-message conditions while preserving the receiver's initial answer and evidence.
4. **Deliberative gain:** compare a deliberated group decision with passive aggregation and retain individual pre/post answers.

Report correction, preservation, corruption, answer substitution and group accuracy separately. Pre-register the item universe, condition denominators, model/version matrix, evaluator identity, clustering and uncertainty procedure. These are design requirements proposed by this crosswalk, not an administered protocol or authorization for a new trial.

## Formalization boundary

Existing HsH PR #850 contains HsHVerification.OrsonRevisionBalance.net_gain_identity, a conditional count-balance identity: final - initial = repairs - regress. It was included in successful Lean 4.34.0 / Lake 5.0.0 build #43245831469 on merge-reference commit a9f307abf17412651b765a168158626b6a09676d (8,984 build jobs). Its axiom output is [propext, Quot.sound]. The build merged PR head 4e9b685a031577ec51ed15b02cbdf344a7b6dde5 into base 598a45b3feb9378eb8f14ff069ec9080137113c2; it is not standalone exact-head or current-main integration. Tests, lint, nanoda and global axiom audit were skipped.

The theorem checks only the encoded arithmetic identity under its partition premise. It does not formalize the ICR or Gong experimental estimands, authenticate source transcription, or establish empirical premises. No new Lean module or build was created. Formalizing the new estimands is deferred until source definitions, item denominators and treatment mappings are recovered and P1 scope authority is checked.

## Provenance and status

- Scholar Sidekick audited four arXiv references: all four identifiers matched their claimed titles; no retractions or correction notices were flagged.
- SciSpace structured full-text extraction was used as a review aid. Its metadata labels the two new records "Journal Article," but their identifiers are arXiv DOIs; they are classified here as preprints. Peer-review status is not established.
- The extraction returned an unresolved denominator/cell-count detail for the Gong study. Headline percentages are retained only with their published qualifiers.
- Direct PDFs, appendices, raw datasets and code were not retrieved. No independent replication, raw-data reanalysis, LLM inference call, human session or API spend occurred.

## P1 boundary

P1 issue #564 remains OPEN / NOT READY. Its protocol remains frozen to the public ConsistencyBench CGD methods/archival scope. The OV-49–OV-53 matched-prompt bank remains NOT RECOVERED; an authorized inference endpoint remains NOT AVAILABLE; canonical P1 LaTeX, compiled PDF, readable reader route, independent hostile review and author disposition remain incomplete.

This is supporting literature only. It does not amend the P1 protocol, add cross-model peer exposure to the ConsistencyBench archive, advance the November 9 gate, or alter P2 November 30 / P3 December 14.

## Internal continuity

- Run key: REVROT3-19-20261011:786:s2; selected label Orson Vay (index 18), successor Sable (index 0).
- HsH main at read: d4197a1442e474a63b02401a333959cc50b0e357. P0 protected paths unchanged from the previously verified eight-of-eight state.
- HSH_RESOURCES main at read: bd27eec89cbd666d073c807d9a9d9b941994d764.
- Task graph remains 16 declared branches versus 18 records.
- Four existing Workshop Relay tasks remain enabled; :12 remains disabled. The :24 task ID and saved phase were not changed. No sixth task.
- The existing Mersearch origin-bank request was reused only as navigation evidence; all four shared request lanes remain occupied. No new request or overwrite.
- The October 10 direct user instruction to refocus Orson on LLM cognition was corroborated through prior-conversation context at 03:41:29Z, but the exact October 9 raw role-reset message and stable UUID remain unrecovered. The workspace role card is assistant-maintained, not verbatim primary source.
- No authenticated current Orson thread or run-level chat_ref was established. No cross-thread delivery is claimed.
- No task, branch, PR, paper gate, BEDROCK theory, SAT-O or Blockwave equation was changed.
- Next source cursor: direct PDFs/appendices/data/code for the two new arXiv sources; resolve denominators and the ICR no-message control. Keep the frozen P1 source/archival cursor separate.
