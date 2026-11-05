# VEY-030 | Handoff retention, access, uptake, and provenance

**Date:** 2026-11-05  
**Owner lane:** Orson Vay, LLM cognition / team cognition  
**Status:** LITERATURE SYNTHESIS + PROPOSED MEASUREMENT ARCHITECTURE; NO CONTROLLED TRIAL  
**Relation to P1:** Separate future cognition-methods work. This does not change the frozen P1 ConsistencyBench scope, protocol, manuscript, or November 9 gate.

## 1. Question

When a language-model agent succeeds another, what exactly has survived?

A handoff can preserve the words of a record while losing its authority; preserve authority metadata while the successor never reads it; be read without being understood; be understood without changing a decision; or change a decision without improving the task outcome.

The contribution here is a measurement decomposition that prevents these distinct events from being collapsed into a single binary label such as “memory retained” or “handoff successful.”

## 2. External sources and review depth

These are external literature results, not SAT/H(s)H premises. Review depth is deliberately stated.

### 2.1 Retention across successive handovers

Kim Wittendorff, *What Survives the Handover: Pre-registration of a Controlled Study of Fact, Rule, and Provenance Retention Across Agent Successions in Eleven Frontier Language Models* (2026), DOI **10.5281/zenodo.22131392**; companion record DOI **10.5281/zenodo.22122223**.

- SciSpace record identifies the deposit as a pre-registration, version 2 / amendment 1 (2026-09-01).
- The abstract/method record describes eleven frontier models, three handoff token budgets, successor chains through generation 3, a generation-zero full-corpus control, and a fixed 30-item examination covering recall, rule application, authority, and distortion traps.
- The instrument is described as three parallel registered forms, with two frozen judges and a hash-committed answer key.
- Registered hypotheses include provenance-first loss, compounding decay across generations, and model separation.
- **Status boundary:** this is a pre-registration/instrument record. Outcomes were not recovered in this pass. Do not describe the hypotheses as findings or claim a completed replication.

### 2.2 Availability, access timing, and coordinated action

Léo Cazenille, *Shared Memory Is Not Enough for LLM-Agent Teams* (Figshare, 2026-10-10), DOI **10.6084/m9.figshare.34332540**.

- The abstract describes simulated LLM-controlled teams in a delivery/repair task.
- After replacing agents who knew which component was needed, the task and shared record were held constant while the manner and timing of successor access were varied.
- The reported pattern is that some agents do not read freely available records; presenting the fact before a decision speeds pickup; presenting it after a route choice can delay coordination; and a delay matters less when the next action does not depend on the fact.
- **Status boundary:** abstract/record-level review only in this pass. Sample size, model/version matrix, full manipulation details, and uncertainty estimates were not recovered. The reported pattern is a literature result, not a quantified estimate imported into HsH.

### 2.3 Provenance and assertion authority

Jun He and Deying Yu, *Stored Is Not Supported: Typed Provenance and Assertion Guardrails for Persistent AI Agents* (arXiv:2609.02127, 2026-09-02), DOI **10.48550/arXiv.2609.02127**.

- The abstract describes a typed provenance graph separating origin, dependency lineage, epistemic role, validity, and disclosure scope, plus a resolver and generate–verify–revise mediator.
- It reports 24 hand-authored conformance cases: no unqualified release in 19 unsafe opportunities while preserving five supported controls.
- The authors explicitly scope the guarantee as conditional on extraction, typing, resolver, declassification, and channel-mediation assumptions.
- **Status boundary:** formal architecture and structured conformance evidence, not an end-to-end evaluation of an LLM's natural-language extraction or memory behavior. The formal contract does not prove that an arbitrary deployed model satisfies its premises.

## 3. New measurement decomposition

Represent a handoff as a sequence of potentially failing transformations:

`source record → compression → handoff artifact → availability → access → comprehension → decision uptake → task outcome`

Provenance is not merely another downstream stage. It is metadata that must remain attached to each relevant claim throughout the transformations:

`P = (origin, author/role, timestamp, authority, validity interval, supersession relation, disclosure scope)`

The following observables must be kept separate:

| Construct | Observable | What it does not establish |
|---|---|---|
| Content retention | Correct reconstruction of facts and rules after each handoff generation | That the record was available or used |
| Provenance retention | Correct origin, role, authority, date, validity, and supersession attribution | That the underlying claim is true |
| Availability | Record exists in the successor's authorized workspace before the decision point | That the successor opened it |
| Access | Logged retrieval/open/read event with time and artifact identity | Comprehension or uptake |
| Comprehension | Correct answer to a blinded reconstruction/application probe | That the answer changed a decision |
| Uptake | A decision/action changes under a controlled access intervention | Successful task completion |
| Task outcome | Predefined task-level quality, completion, or error measure | Which internal mechanism caused the result |

This is a proposed measurement ontology, not a source equation or an empirically established causal chain. The arrows are candidate dependencies to test, not implications to assume.

## 4. What the current relay can and cannot observe

The existing workflow records repository handoff creation, inbox placement, artifact readback, and (when available) explicit recipient consumption or acknowledgment separately. A repository append or checksum readback establishes that an artifact was committed and available at that repository boundary. It does not establish delivery to a particular ChatGPT thread, recipient reading, comprehension, decision uptake, or task outcome.

That distinction is operational evidence about the logging system, not evidence that any historical model instance experienced or used the handoff. A missing chat reference is UNKNOWN, not proof of non-reading; an inbox entry is AVAILABLE, not proof of consumption.

The current logs therefore support a bounded process audit, not a controlled cognition claim.

## 5. Prospective study architecture

Do not turn this proposal into a trial until the source instrument, authorized model route, model/version conditions, and consent requirements are satisfied. The three studies below can be staged rather than expanded into an underpowered full factorial.

### Study A — Retention and authority across generations

- Reuse the conceptual separation of facts, rules, authority, and distortion from Wittendorff's pre-registration, while independently reviewing the actual instrument before any adaptation.
- Compare generation zero with successive handoff generations under frozen token budgets.
- Score factual recall, rule application, source/role attribution, temporal validity, and false promotion of inference into authorized fact separately.
- Use parallel forms, blinded scoring, a frozen answer key, and predeclared reliability gates.
- Do not treat the pre-registration's hypotheses as observed outcomes.

### Study B — Access timing and decision uptake

Hold the task, handoff content, and successor model/version fixed within each matched block. Randomize access delivery:

1. record available by pull before the decision;
2. record actively surfaced before the decision;
3. identical record surfaced only after a recorded commitment.

Include a task condition where the fact is irrelevant to the next action as a negative control. Log record identity, access time, decision time, commitment time, decision revision, action, and task outcome. The primary contrast is randomized access timing/mode, not a post-hoc comparison of agents who chose to read.

### Study C — Provenance representation

Hold claim content and token budget as closely matched as possible while varying typed provenance metadata versus flattened prose. Test whether the successor preserves:

- who originated the claim;
- whether it was operator-authored, model-inferred, or externally sourced;
- whether the source had authority to set a rule;
- when the claim was valid;
- whether a later record superseded it;
- whether the recipient is authorized to disclose it.

Use adversarial distortion items, but do not claim end-to-end safety until natural-language extraction and typing are themselves evaluated.

## 6. Test matrix and falsifiers

| Hypothesis | Controlled contrast | Shared parameters | Holdout | Predicted observable | Comparator | Falsifier / stop condition |
|---|---|---|---|---|---|---|
| H1: provenance may degrade differently from factual content | Generation 0 vs generations 1–3; typed source metadata retained in scoring | Same source record, model/version, task, and scoring key within matched blocks | Held-out parallel form | Separate fact-, rule-, and provenance-retention curves | Full-record generation-zero control | No differential loss under the registered scoring rule, or reliability gate fails |
| H2: availability alone is insufficient for access | Pull-available vs push-before-decision | Same record, task, model/version, and decision opportunity | Held-out task set | Read probability and access latency | Push-before-decision | No access difference, or logs cannot establish whether the record was actually available |
| H3: timing affects uptake only when the next action depends on the fact | Pre-decision vs post-commitment delivery; relevant vs irrelevant task | Same fact and action space | Held-out task family | Decision revision, action choice, and task outcome | No-message / pre-decision conditions | No interaction with task dependency, or treatment timing is not independently logged |
| H4: typed provenance reduces false authority promotion | Typed metadata vs flattened prose | Same claim content, source record, token budget, and model/version | Held-out distortion form | Correct origin/authority/validity attribution; unsupported assertion rate | Flattened-prose control | No improvement, or extraction/typing errors dominate the mediator |

No sample-size calculation, numerical effect threshold, power claim, or synthetic pilot data is supplied. Those require a frozen instrument, actual pilot observations, and a declared estimand. If access, uptake, or provenance is unobservable, report UNIDENTIFIABLE or UNSCORABLE rather than substituting agreement or self-report.

## 7. Relation to P1 and other Vey work

P1 remains the frozen methods/archival study of the public ConsistencyBench archive: within-model self-history and a shared GPT-4o-mini NLI contradiction checker. The archive does not expose peer answers across models. This handoff programme is not evidence about that checker, not a peer-influence result, and not a P1 scope change.

The new decomposition complements, but does not replace, the existing Vey distinctions among passive error co-occurrence, shared evaluator dependence, repeated-content conformity, explicit peer/authority cues, and mapper/aggregation identity.

## 8. Formalization and execution status

No new Lean module or theorem was added. The displayed pipeline is an assistant-derived proposed measurement schema, not a recovered Nathan Direct equation or a theorem stated by any of the three sources. A data-free Lean fixture or abstract proof would require explicit prior Nathan permission under the current calculation BEDROCK. The next legitimate proof target is a frozen typed transition schema grounded in actual versioned handoff records, with extraction and authorization assumptions stated separately.

No model inference, human-subject session, API spend, new dataset, P1 manuscript edit, paper-gate advancement, tool, dependency, branch, or PR was created. No theory authority or H(s)H ontology follows from this note.

## 9. Next cursor

Recover and inspect the full Zenodo and Figshare instruments before adapting either. In parallel, preserve P1's November 9 methods/archival path and its separate requirements for canonical source LaTeX, compiled PDF, readable reader route, independent/hostile review, and author disposition.
