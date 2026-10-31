# VEY-023 | Receiver-relative evidence integration, source provenance, and order effects

**Date:** 2026-10-31  
**Status:** PRIMARY ARXIV SOURCE REVIEWED / CONDITIONAL LEAN FORMALIZATION ADDED TO EXISTING HsH PR #850 / CI PENDING AT INITIAL NOTE / NO NEW MODEL TRIAL  
**Owner lane:** Orson Vay, LLM cognition  
**P1 effect:** methods/source advance only; P1 #564 remains SOURCE / EXPERIMENT READINESS.

## 1. Primary source

Sebastien Kawada and Manolis Kellis, “Evidence Integration in Large Language Models,” arXiv:2609.04290v1, submitted 2026-09-03.

- Abstract/metadata: https://arxiv.org/abs/2609.04290
- Full HTML: https://arxiv.org/html/2609.04290
- Relevant sections: §§3.1–3.6, §§5.1–5.6, §6.3, §7, §8.6, Appendix F.
- Status: arXiv preprint; no peer-reviewed journal publication identified in this review.
- No executable code repository or raw trial-data artifact was located in the inspected v1 source. This is a source review, not an independent trial-level reproduction.

Exact arXiv ID/title search in the current VEY source shelf returned no prior entry. Four shared Mersearch lanes were occupied; the source review used the official arXiv v1 document and bounded GitHub searches across HsH, SAT_THEORY_ARCHIVE_2023-25, and HSH_RESOURCES. It is not a completed Mersearch search.

## 2. Core result

The authors report >10 million trials, 12 LLMs from four families, and eight domains. Four domains are scientific tasks: quantum mechanics, physics, genetics, and molecular biology. The arithmetic core uses nine models; held-out/cross-domain work extends the panel.

The proposed receiver-relative law in §3.1 can be represented in scalar log-odds form:

`L'=(1+a)L+d`

where `L` is the receiver's pre-exposure candidate margin, `a` is a fitted receiver-prior weight parameter, and `d` is an evidence tilt. The distribution-level expression is:

`p_e(v|x) ∝ q(v|x)^(1+a) exp(φ_e(v))`.

The paper reports an arithmetic-panel prior weight `1+a` of approximately 0.20–0.65 across nine models. This is operationally identified from answer-slot log-probability margins, not a direct readout of a complete internal belief distribution and not a universal model constant.

Three findings are relevant:

1. Wrong candidates more congruent with the receiver's own answer landscape are adopted more readily than equally frequent errors that are less congruent.
2. Checking and using are separable. The paper reports adoption of invalid candidates after checking probes have rejected them: 93–100% in a propositional-constraint setting and up to 99.4% in held-out physical/life-science tasks. These are task-specific paper results, not deployment prevalence.
3. Claimed provenance, role-based provenance, and authenticated provenance differ. If the same writable transcript can arise under two claimed origins, origin cannot be perfectly identified from that transcript alone. Authentication must rely on a statistic unavailable to the transcript writer, e.g. an externally verified tag/MAC.

Mechanistic interventions report candidate admission, promotion, transport, and late answer-state integration. Verification representations can be decodable yet exert little causal influence on the final answer. The J-lens workspace separation is reported in two model families; broader knockout/steering work spans seven models.

## 3. Composition and order

The paper's §3.6 Eq. (23) gives, for a common receiver parameter `a`:

`L_12=(1+a)^2 L_0+(1+a)d_1+d_2`

and for reversed order:

`L_21=(1+a)^2 L_0+(1+a)d_2+d_1`.

Therefore:

`L_12-L_21=a(d_1-d_2)`.

The two orders commute for a rational receiver under this parameterization (`a=0`), or when the two evidence tilts are equal.

**Assistant-derived extension:** allow source-channel-specific receiver weights `a_1,a_2`:

`U_(a,d)(L)=(1+a)L+d`

then:

`U_(a2,d2)(U_(a1,d1)(L))-U_(a1,d1)(U_(a2,d2)(L))=a2*d1-a1*d2`.

Commutation is equivalent to `a_2 d_1=a_1 d_2`. This two-weight extension is a reconstruction motivated by the paper's source-channel discussion, not a verbatim empirical result.

The authors explicitly note that perfectly correlated sources should not be counted as independent evidence. Their displayed composition law needs the evidence tilt to depend on prior messages to capture source dependence fully; composition tests are limited to the arithmetic instrument.

## 4. Important distinctions

- VEY-020's `w_m` is a posterior-equivalent copy weight reconstructed from reported evidence-unit means.
- VEY-023's `a` is a receiver-prior reweighting parameter in an evidence-integration law.
- VEY-023's verification-recruitment gain `ρ` is distinct from checker competence, source reliability, and the existence of a verification representation.

These are different estimands. Do not merge them.

This paper is not a direct multi-agent peer-interaction experiment, not a replication of VEY-016/017, and not proof that a shared-source error caused a particular archived consensus. It adds a receiver-side mechanism that P1 should test separately from source ancestry and transmission.

## 5. Limitations

The authors state:
- the reliability frontier is estimated only for the candidate distributions studied;
- prior weight is measured from answer-slot margins only where those probabilities are available;
- the candidate-locality law is exact for candidate adoption but approximates the full answer distribution;
- composition-law tests are limited to the arithmetic instrument;
- mechanistic interventions cover fewer models than behavioral experiments;
- J-lens separation is replicated in two model families;
- scientific-domain tasks use synthetic problems with exact oracles;
- prevalence in deployed retrieval systems, laboratories, human reports, and autonomous scientific agents remains to be measured.

The >10M trial count is author-reported; no raw-trial artifact was independently retrieved here. No trial-level reanalysis is claimed.

## 6. P1 design update

Retain the existing five-stage VEY-020 lifecycle: origin, transmission, visibility, integration/adoption, measurement. Enrich integration/adoption with receiver state and checking/control separation.

A future matched experiment should randomize, while holding candidate truth and task difficulty fixed:
- same-origin repetition versus independently sourced evidence;
- receiver-congruent versus receiver-incongruent wrong candidates, with pre-exposure support measured before exposure;
- message order;
- verification verdict present/absent, while measuring checker competence separately from whether the verdict controls the final action;
- transcript-only provenance labels versus externally authenticated source identity.

Measure per-agent context snapshots, source/message IDs, parent IDs, exposure time/order, candidate support before exposure, candidate truth, checker verdict, final action, raw output, and independent scoring. Provider/model names alone do not establish independent evidence or independent state. Use independent keys or blinded human adjudication for open-ended tasks; do not rely on a shared LLM judge as sole scorer.

## 7. Formalization pointer and epistemic status

Existing HsH PR #850 was reused; no new branch or PR:

- Branch: `research/orson-p1-shared-nli-bound-20261028t06z`
- Module: `FORMAL_VERIFICATION/HsHVerification/OrsonEvidenceCompositionLaw.lean`
- Module blob: `1b71e858bd954be2df56de82c40cdb9a3e6cbdb2`
- Root import blob: `8d9817accf811d002f3e43ce0fdcce18613eeec2`
- Commit: `4bb05c762a91176e034a2d1246c5e06713b1495b`
- Lean Actions #41244151207 was in progress at initial note creation; verify the exact head and all theorem-specific axiom outputs before claiming compilation.

Six conditional theorems formalize two-channel composition, order difference, and commutation conditions. Lean checks only the encoded scalar algebra. It does not validate the empirical law, fitted parameters, internal model mechanism, provenance authenticity, source independence, or applicability to peer interaction.

## 8. P1 readiness and source recovery

P1 issue #564 remains OPEN / SOURCE–EXPERIMENT READINESS. The original OV-49–OV-53 matched neutral-versus-false-authority answer-keyed bank remains UNRECOVERED; located OV-49–OV-53 pointers are geometry/finite-core artifacts. The exact original October 9 user-role message establishing the Orson specialist assignment and its conversation/message UUID also remain unrecovered. The live role charter is an operational record, not a substitute for the raw message.

All four Mersearch request lanes were occupied. No request was overwritten or duplicated. Bounded repository search did not recover the bank or original user message; this is not proof of global absence.

Local feasibility check found no Ollama/vLLM/llama-server/llamafile, no CUDA device, CPU-only PyTorch, no Transformers/vLLM/llama.cpp/Ollama runtime, and no provider API credentials in the execution environment. No model inference, human-subject session, API spend, or new trial occurred.

Recommendation remains: at the November 2 protocol freeze, if the bank and authorized inference route remain unavailable, freeze the November 9 P1 as methods/archival synthesis, not an administered experiment. Recommendation only; no gate advanced.

## 9. No project promotion

No BEDROCK change, no theory promotion, no SAT-O/Blockwave edit, no physical calculation, no CODATA comparison, no new tooling, no automation/task/ID/cadence change.


## Execution amendment 01 | 2026-10-31

- Initial Lean run #41244151207 failed in the equal-channel commutation proof (unsolved additive-normalization goal; sorryAx appeared in that failed run).
- Repair build #41244476754 succeeded with 8,975 build jobs on merge-reference commit 24a14402057420f3c5b00f64123db2b432330768. PR-branch and merge-reference blobs matched for the module and root aggregator. Complete log: zero sorryAx; theorem-specific outputs used standard propext, Classical.choice, and Quot.sound. Tests, lint, nanoda, and separate automated axiom audit were not run.
- Linter cleanup was then pushed. Current PR #850 head fb44ce3bd3ac240142345e2613031b24e6a57e52; module blob 1e05539c4f215785e9760dec2f7a98fd6a68610d; root blob 8d9817accf811d002f3e43ce0fdcce18613eeec2. Fresh run #41244897947 is IN_PROGRESS at checkout; do not claim the cleaned final head compiled until the complete log and axiom outputs are read.
- From the reported arithmetic prior weight 1+a approximately [0.20,0.65], a approximately [-0.80,-0.35]. Under the equal-channel order identity, the conditional magnitude is approximately 0.35–0.80 times |d1-d2|. This is a coefficient bound, not an observed order-effect size; no absolute tilt gap was supplied.
- Publisher intake #1172 succeeded (run #41244723168); exact readback of the sole published artifact matched its payload. The two earlier SHA-mismatch intake issues #1170/#1171 were closed not-planned and wrote no artifact.
- P1 #564 remains SOURCE / EXPERIMENT READINESS. No trial, model call, human subject, API spend, or paper-gate advancement.
