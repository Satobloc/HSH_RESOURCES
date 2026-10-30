# VEY-017 | GRAIL multi-peer extension: source-level feasibility and isolation contract

**Date:** 2026-10-30 22:36Z  
**Run:** `REVROT3-19-20261011:478:s3`  
**Selected identity:** Orson Vay, ring index 18; next Sable, ring index 0.  
**Identity status:** Current assistant reconstruction in the selected Orson specialist lane. No authenticated historical Orson ChatGPT thread or live continuation destination was established.  
**Status:** COMPLETE-AS-STAGE / SOURCE-CODE AUDIT / DESIGN PROPOSAL. No LLM trial, human-subject experiment, or platform modification.  
**Owner lane:** Vey Cognition Lab. Preserve Orson's LLM-cognition remit and the November 9 P1 gate.

## 1. Question and bounded result

Can the existing Group-AI Interaction Laboratory (GRAIL) support a replicated human-plus-multiple-LLM-peer study of shared-source dependence and apparent consensus without building a new group-chat platform?

**Answer:** GRAIL is a credible research-platform base, but its current main implementation is a single shared LLM facilitator. It does not instantiate multiple independently stateful LLM peer participants. The distinction is visible in the source code, not merely inferred from the README.

This is a source-level architecture finding. It is not an observed cognitive effect, a successful experiment, or evidence that multiple LLMs are independent.

## 2. Primary source and exact code audit

Repository: https://github.com/microsoft/group_ai_lab  
Current inspected main commit: `c7a2077281fed73f492a29ab187a7b86875203d8` (2026-09-30 README citation update).

Exact source identities:

| File | Blob | Relevant locations |
|---|---|---|
| `server/src/callbacks.js` | `45669e5664349a1fc10cad5fc07324b82f3c9181` | 8, 11, 16, 90-129, 133-224, 226-293 |
| `server/src/LLMConfig.js` | `7b18c41ff613a24f69245861c8e29edee6290372` | 1-35 |
| `.empirica/treatments.yaml` | `31cff9bdb7b638e1381382ef0fb4d1feca04a447` | 1-70 |
| `README.md` | `167ca0f03be467e48a66e2f4262e62da1eec897a` | Overview, setup, treatments, logging, consent, license |

### Source observations

1. `callbacks.js:11` declares one module-level `openaiModel` from the environment. `getLLMResponse` at line 16 uses that same model and endpoint for each request.
2. `onGameStart` at line 90 initializes one game-level `llmLog` array. Under LLM facilitation, ordinary player objects receive human task content; the LLM is not instantiated as a set of player objects with separate state.
3. `onStageStart` at line 133 installs one facilitator interval for the LLM treatment. The request payload at lines 169-181 is built from the entire game chat transcript, preceded by one facilitator system prompt and meeting/time context.
4. A successful intervention is appended at lines 189-192 with the single sender identity `id: "ai"`, `name: "Facilitator"`.
5. The participant-tag path at lines 226-290 uses the same global model and facilitator prompt, again appending the same facilitator identity.
6. `LLMConfig.js` defines one LLM facilitator prompt and one human-facilitator prompt. It does not define per-agent roles, private histories, or per-agent source bundles.
7. `treatments.yaml` offers `facilitation = none | human | LLM`, player counts 5 or 6, and ordinary task factors. It has no multi-agent count, source-sharing factor, peer-visibility factor, or per-agent model assignment.
8. The README explicitly describes a shared LLM system. It says the game-level `llmLog` stores timestamp, model, full request payload, response, and trigger mode. This is useful provenance infrastructure, but the current log has no per-agent identity because the code has one facilitator.
9. The default consent form is a placeholder and must be replaced with an IRB-approved form before deployment. GRAIL requires the researcher's own LLM endpoint/API key and hosting; MIT licensing does not remove those operational costs.

A bounded static scan of the exact 293-line `callbacks.js` blob found: one global model declaration; one response-function definition and two call sites; two facilitator sender append sites; two full-chat transcript mappings; zero `agentId` identifiers; and zero `agentState` / `agentStates` / `agentContext` identifiers in that file. This is source inspection, not execution of GRAIL or a runtime test.

### Interpretation

Repeated calls to one facilitator model are not multiple peer agents. Giving several calls different display names would also be insufficient if they receive the same complete transcript and share one mutable context. The existing system's observable flow is:

`group chat -> one full-transcript prompt -> one configured model -> one Facilitator sender`.

That architecture supports a shared-facilitator experiment, not an independently stateful multi-peer-agent experiment.

## 3. Minimum adaptation contract

Reuse GRAIL's Empirica session, treatment, consent/survey, chat, export and request-logging infrastructure. Do not build a new group-chat platform. A multi-peer extension would need the following explicit elements:

- **Agent configuration:** stable `agent_id`, exact resolved model/version, prompt version/hash, assigned evidence-bundle hash, and visibility policy for each agent.
- **Separate state:** an independent context/history per agent, not a view over the global chat by default.
- **Visibility enforcement:** every message supplied to an agent must have a recorded message ID and an explicit visibility reason. The no-peer-exposure condition must not leak another agent's output through a forwarded human message or a shared summary.
- **Turn scheduler:** deterministic and logged selection of which agent acts, when, and under what visibility policy.
- **Distinct chat identities:** messages should identify the originating agent, rather than collapsing all outputs into `ai / Facilitator`.
- **Per-request lineage:** group/session ID, agent ID, provider request ID where exposed, model revision, prompt hash, source-bundle hash, visible message IDs, context hash, request/response timestamps, raw payload/response under approved data controls, and output hash.
- **State-isolation audit:** a post-run check that reconstructs each agent's actual input ancestry and detects accidental cross-agent state or message leakage.

The term **independent agent** should be avoided unless its intended level is specified. Separate API request contexts do not imply independent model weights, independent training data, independent system prompts, or independent evidence. Use the narrower label **state-isolated agent session** unless stronger independence is demonstrated.

## 4. Discriminating experiment design

The causal distinction needed for P1 is between shared evidence and direct peer exposure. They are separate factors.

A minimal proposed design is a 2 x 2:

| Evidence exposure | Peer outputs hidden | Peer outputs exposed after baseline |
|---|---|---|
| Shared evidence bundle | Common-source / no-peer condition | Common-source plus peer-exposure condition |
| Disjoint, difficulty-matched evidence bundles | Separate-source / no-peer condition | Separate-source plus peer-exposure condition |

Protocol outline:

1. All agents first submit a sealed answer, rationale, and confidence before seeing peer outputs.
2. The assigned peer-exposure intervention is then applied. The no-exposure arm remains blind to peer outputs; the exposure arm receives a predeclared, logged subset or all of them.
3. Each agent submits a second answer and confidence. Record both revisions and whether consensus moved toward or away from correctness.
4. Randomize and replicate at the **group/session** level. Multiple sessions per condition are necessary; turns and participant-message rows are nested observations, not independent group replications.
5. Use independently adjudicated correctness as a primary outcome. Measure consensus, confidence/calibration, and error dependence separately. Do not use an embedding similarity score as a substitute for truth.
6. Hold model family, resolved model version, prompt template, task difficulty, and evaluation procedure fixed where the factor is not intentionally manipulated. Record common model weights and common prompts as dependencies, not independent evidence.
7. Include the existing single shared-facilitator condition as a distinct comparator. It is not interchangeable with multiple peer agents.

No sample-size calculation is supplied. It requires a real pilot or suitable empirical variance estimates, an identified group-level estimand, and the planned number of conditions. No invented group counts, effect sizes, or power inputs are introduced.

## 5. Connection to current P1 evidence

The existing evidence map already distinguishes three different objects:

- **ConsistencyBench:** 17 archived model result files, a common question-blind GPT-4o-mini checker within each model's revision path, and post-hoc cross-model aggregation. The inspected source does not feed peer models' answers into another model. It supports archival scoring and dependency analysis, not a causal peer-influence experiment.
- **Chen et al. (2026), arXiv:2609.02122:** a direct mixed human/multi-LLM peer-interaction study as reported. VEY-016 records the source-level inference that the eight conditions likely correspond to one session per condition; independent group replication and per-agent context ancestry are not auditable from the released package.
- **Alsobay et al. / GRAIL:** a replicated human-group study with a shared LLM facilitator, not multiple LLM peer participants. GRAIL is a reusable platform base, but its current code must be extended before it can instantiate the preceding study design.

The original answer-keyed neutral-versus-false-authority bank referred to by the Orson role charter remains **UNRECOVERED**. Located OV-49 through OV-53 artifacts are geometry/finite-core work. OV-55/56 and OV-100 are assistant-authored analytical or synthetic artifacts, not administered LLM trials. Do not retrofit these materials into cognition evidence. P1 issue #564 remains open and its scope should stay archival/methodological unless the actual trial bank and authorized model/participant path are recovered.

## 6. Universal shape-to-Lean triage

The proposed visibility/state architecture contains a directed message-lineage structure. A possible invariant is: an agent's context may contain a peer message only when the experiment's visibility policy authorizes that message.

**Status:** `FORMALIZATION_BLOCKED_DEFINITION / BLOCKED_PENDING_NATHAN_PERMISSION`.

The current GRAIL source does not define multiple agent states or a peer-visibility policy, so a faithful source-derived proposition is not yet present. Formalizing a proposed finite state/visibility model would be a data-free abstraction; no specific prior permission for that calculation/model was located. No Lean module was written or run. This is not a Lean failure or proof.

The existing HsH PR #1115 is separate. Its compiled conditional group/session-identifiability theorem does not formalize GRAIL, agent independence, or peer influence. Lean compilation, source translation, experimental implementation, and empirical validation remain distinct gates.

## 7. Operational feasibility and limits

- GRAIL is MIT-licensed and uses Empirica v1.12.0. Reuse/adaptation is preferable to a new platform.
- A targeted current-main source search found no multi-peer implementation in the main code. The earlier VEY-016 note records five repository forks but no exhaustive fork-by-fork audit; no fork-completeness claim is made here.
- The repository requires a user-supplied LLM endpoint/API key and a deployed server. The current run had no authorized provider call path, participant recruitment, or deployed experiment environment. No API calls, human sessions, hosting, recruitment, or paid costs occurred.
- Real costs cannot be estimated until provider/model, groups per condition, agents per group, turns, context sizes, recruitment and hosting are specified.
- The default consent form is not deployment-ready. Human-subject review, consent, privacy/security controls, data retention and access policy are prerequisites.

## 8. Disposition and next cursor

**What changed:** the GRAIL suitability claim is now pinned to exact source code and commit. The next engineering task is a bounded fork design for per-agent state isolation and exposure logging, not a new platform build.

**What did not change:** no P1 experiment was administered; no human data were collected; no manuscript, PDF/reader, P1 gate, BEDROCK entry, external GRAIL repository, or HsH PR was modified; no physical calculation was made.

**Next actions:**
1. Complete the new Mersearch lane-1 source search for the original Orson test bank. Do not call it complete until its request-scoped manifest and receipt are read back.
2. Keep P1 #564 in source/experiment-readiness status. If the original bank remains unrecovered and no authorized model path is available, prefer a narrow archival/methodological paper over invented trials.
3. If a real peer-agent study is later authorized, fork/adapt GRAIL with the minimum isolation/logging contract above, then pilot and estimate group-level variance before sample-size planning.
4. Recover a real answer-keyed task bank and external adjudication procedure before claiming correctness or shared-source effects.

**Source extent:** GRAIL README, server callbacks, prompt config and treatment YAML fetched from current main; VEY-016 and current P1 issue/PR state read; Orson charter and prior receipts read. No runtime deployment or external model call.
