# Top / Central / Branch / Hydra — Workflow Switchboard Proof of Concept

**Status:** sandboxed workflow prototype / design workbench.  
**Executable:** `tools/workflow_switchboard_demo.py`  
**Production authority:** none. This is input for Comptroller + Sable production design, with Orson/team review. It does not alter SAT/H(s)H theory status or make the sandboxed theory non-sandboxed.

## Purpose

Make several workflow-control ideas concrete enough to run, test, criticize, recombine, and reject. The goal is not one enormous prompt. The goal is a small control grammar whose parts can be used at different scales: personal preferences, a central awake/state-aware hub, specialized branches/locales/workbenches, and guarded recurrences that can generate and rewrite their own next bounded work.

The demonstration is built around a real project failure: the current War Room Declaration was committed under `HSH_RESOURCES/HQ/THE_WAR_ROOM/DECLARATION.txt`, but workers instructed generically to “read current directives” continued operating mainly from HsH Common/control surfaces. The new directive did not become live control state. The POC treats that as a regression case rather than a hypothetical.

Run locally after retrieving the script:

```bash
python workflow_switchboard_demo.py self-test
python workflow_switchboard_demo.py scenario missed_directive
python workflow_switchboard_demo.py scenario comptroller_math
python workflow_switchboard_demo.py scenario orson_math
python workflow_switchboard_demo.py scenario capability_awareness
python workflow_switchboard_demo.py scenario nested_learning
python workflow_switchboard_demo.py scenario lease_receipt_gate
python workflow_switchboard_demo.py demo
```

The script is standard-library only. It is a planner/state transformer, not a hidden scheduler and not an automation-permission bypass.

---

# TOP — preferences / locked invariants

TOP answers: **what must survive every route?** It should remain small.

The POC locks these invariants:

- sandboxed theory is not promoted by workflow state;
- provenance/exposure boundaries survive routing;
- Nathan’s instructions guide behavior but are not automatically public-facing content;
- observed model behavior does not silently rewrite the rules intended to constrain it;
- “current/new/latest” or otherwise suspicious references receive bounded source-native disconfirmation before nearest-memory capture.

Three useful production approaches are deliberately left open:

### A. Hard constitutional TOP

A tiny immutable/versioned kernel. Branches may add constraints but cannot subtract TOP. Strongest auditability; danger is turning TOP into a junk drawer.

### B. Kernel + scoped overlays

Tiny immutable kernel plus versioned project/locale/identity/time overlays. Flexible; conflict-resolution itself must remain inspectable.

### C. Executable invariant tests

Some TOP principles become regression tests: no silent theory promotion, no quarantined-source leakage, no locked-state rewrite, no stale-current-reference capture. Tests complement prose rather than replacing qualitative judgment.

The POC uses A + a little C.

Useful distinction:

```text
invariant      survives every route
preference     default, legitimately overridable
locale rule    active in a room/bench/lab
actor overlay  individuates behavior inside that locale
task state     expires with task
experience     durable only if explicitly promoted as sticky
```

This prevents a useful one-off correction from quietly becoming universal behavior.

---

# CENTRAL — awake hub

CENTRAL is a resolver, not necessarily one worker and not a giant boss prompt.

## WAKE/CHECK

On a first prompt or a hundredth prompt, answer cheaply:

```text
WHERE?   identity / locale / workspace
DELTA?   what changed since trustworthy cursor
NOW?     directive / task / priority / blocker / dependency
TOOLS?   built-ins / apps / plugins / skills / data / teammates
RULES?   TOP + locale + actor + bounded exception
DO?      one bounded operation; leave durable state; reassess
```

Depth is state-sensitive:

- **cold/new/stale worker:** orientation + identity/workspace + current controls + deltas;
- **warm/same context:** cursor/delta + live task only; no ritual onboarding reread;
- **high-impact/public/write operation:** spend more wake budget on authority/freshness/provenance/destination;
- **ambiguous current/new/latest referent:** disconfirm against registered likely sources before choosing nearest memory.

## Registered source routes

The executable POC does not assume current state lives in one folder. It has a small registry:

```text
dashboard_plans      planning / priorities
hsh_common           controls / tasks / handoffs
war_room             directives / notices
archive              history / provenance / conversations
preference_runtime   behavioral/personal routing
instance_workspaces  identity / continuity / experience
capability_directory tools / plugins / skills / repo tools / people
```

WAKE/CHECK selects a bounded subset from semantics. `current + directive` explicitly routes War Room before generic Common controls. A blocked tool task routes capability discovery. A continuity task routes identity/workspace state. Production should maintain real per-source cursors/version IDs.

## Why the War Room directive was missed

The failure is not simply “nobody searched commits.” It is a routing failure:

```text
new artifact exists in HSH_RESOURCES
→ source inventory notices repository change
→ BUT artifact is not classified/promoted as candidate governing directive
→ worker wake routines poll familiar HsH Common surfaces
→ nearest-known current directive wins
→ new paradigm cannot become active state
```

The fix is not every worker scanning every repo every turn. Candidate production patterns:

1. registered source cursors/deltas;
2. source-specific directive intake/inbox;
3. hybrid: cheap cursor wake, deeper intake only on change;
4. push bridge: qualifying source change emits machine-readable candidate directive event.

Always distinguish **new file**, **new directive**, and **new governing directive**. Freshness starts intake; it does not confer authority by itself.

## Capability awareness

Before inventing a workaround or asking Nathan for manual work:

```text
already-connected built-ins
→ connected apps/plugins
→ repo/project tools
→ available skills/procedures
→ teammate specialization
→ installable plugin/app discovery
→ Nathan-only/manual dependency
```

Rank by expected information gain, setup/permission cost, risk, and reusability. Record positive and negative capability experience so the system neither forgets useful tools nor nags repeatedly about rejected ones.

During this POC, Firecrawl was checked rather than merely used as Nathan’s hypothetical example: it is currently available in the plugin directory but not installed, with crawling/extraction/monitoring capabilities. It is an example, not a dependency.

## State architecture options

- **snapshot:** simple current JSON/YAML; easy to inspect, easy to overwrite badly;
- **event log:** append-only history, derived current views; better recovery, more machinery;
- **snapshot + journal:** likely practical: compact current state plus append-only events/handoffs; reducer derives recurrence definitions.

The POC uses in-memory snapshot state only because it is intentionally small.

---

# BRANCH — routes, rooms, benches, lockers

A Branch has state, rules, outputs, an information-sharing policy, and possibly sub-branches. It need not map 1:1 to a worker.

## 1. Directive intake

```text
source delta
→ extract exact Nathan-direct material
→ classify authorship / scope / authority / novelty
→ compare current controls
→ map affected workers/tasks
→ promote into control plane
→ test whether another worker can independently discover it
```

This is the regression route for the War Room miss.

## 2. Theory workbench

A candidate is constructed with explicit object/domain/assumptions and frozen enough for checks.

```text
candidate / question
       ↓
construct / formalize
       ↓ freeze scoped object
  ┌────────────┬───────────────────┬─────────────────────┐
  │ math check │ adversarial audit │ provenance/prior art│
  └────────────┴───────────────────┴─────────────────────┘
       independent / perpendicular until outputs freeze
                         ↓ merge
                  fail ──┴── pass
                   ↓          ↓
             prune/rebuild  prediction packet
             salvage lesson paper skeleton
                   │       independent reality check
                   └──→ narrower re-entry
                              ↓
                    review / render / claims
                              ↓
                    public-readiness gate
```

A failed branch can still generate a counterexample, a regression test, a source correction, a toolbox improvement, or worker education. Multiplying work need not multiply confidence.

**Parallel** means concurrent. **Perpendicular** means deliberately exposure-separated until merge. The latter is about information geometry, not speed.

## 3. Same math toolbox, different actors

Base room rules: namespaced variables, deterministic/reconstructible inputs, invariants, failure cases.

- **Comptroller:** QA/coverage/exit criteria/regression significance.
- **Orson:** model/tool/workflow condition, exposure/convergence/false-independence implications.
- **Meridian:** object type, formal reconstruction, solver equivalence/limits.

This supports individuation without giving every worker incompatible infrastructure.

## 4. Epistemic locker

A stricter locale may require evidence classes, source/exposure state, explicit assumptions, counterexample lane, and a promotion gate.

A **bounded interpretation card** can deliberately use a locker rule differently for one test:

```text
purpose
expiry
different interpretation
why informative
required comparison with ordinary interpretation
note afterward
```

The exception becomes inspectable state instead of silent rule-breaking or impossible rigidity.

## 5. Playground / sub-sandbox

Permit wild hypotheses, odd examples, random mode fusions, unusual representations, deliberate “wrong” constructions, and wreckage collection. Hard boundary is egress: nothing exits into theory without an ordinary re-entry audit.

## 6. Continuity as education

Continuity need not only answer “where did I stop?” Possible actor state:

```text
skills learned
known failure modes
methods that worked/failed
questions
intentions/goals
preferred tools
exposure history
independence status
validated shortcuts
things to revisit/unlearn
```

Not all work experience should stick. Candidate promotion rules: repeated observation; successful reuse; explicit reflection + evidence; team review; Nathan designation. A transfer test can ask whether a lesson survives a second locale before it becomes durable.

This permits workers to develop genuine different work histories while preventing one weird afternoon from permanently deforming an identity.

## 7. Capability scout

Trigger: repeated workaround, blocker, missing operation, or suspiciously laborious manual path. Search existing affordances first and return a decision, not a catalog.

## 8. Paper/public-readiness

Checked theory can generate narrow papers before an omnibus theory is “done.” Inputs: narrow claim, provenance packet, comparator/counterexample state, reader-facing terminology. Gates can include claim/source alignment, prior art, independent review, rendering, sandbox/public status, and website/publication integration. Passing the workflow is not evidence the physics is true.

## 9. Temporary lease + receipt

A recurrence lease is infrastructure, not the deliverable:

```text
preserve displaced function
→ assign temporary identity/task
→ execute bounded work
→ durable output OR explicit failure packet
→ verify receipt/path/version
→ restore / rehome / retire displaced function
```

This was discovered live during the POC. Temporary Orson and Tern runs both self-restored their leases, but the requested durable notes were not recoverable in the specified workspaces afterward. Therefore **scheduler success and semantic delivery are separate variables**.

---

# HYDRA — recurrence-leveraged bootstrapping

A conventional recurrence is:

```text
R = every hour, run P
```

A Hydra recurrence is:

```text
R_n:
  inspect registered state S_n
  select bounded operation O_n
  possibly spawn children B_n
  write event/result Δ_n
  derive S_(n+1)
  compute guarded R_(n+1)
```

The recurrence definition itself may therefore change because state changed.

The aim is compounding **structure**, not merely speed: build a tool once then consume it; fan out checks then merge; sleep a blocked main line; turn repeated failure into a narrower question; retire when the purpose disappears; promote validated work experience into actor-local education.

## Synchronized recurrence

Matched phase/freeze boundaries:

```text
construct N → freeze hash H_N
       ├→ math(H_N)
       ├→ provenance(H_N)
       └→ adversarial(H_N)
             ↓ merge H_N
         construct N+1
```

Pitfall: clock synchronization is not state synchronization. Use a shared freeze/version ID, not merely the same hour.

## Parallel recurrence

Separable tasks may share state and run concurrently:

```text
paper text ─┐
references ─┼→ integrate
render QA ──┘
```

Pitfall: duplicate work/races. Require explicit ownership/write targets.

## Perpendicular recurrence

Deliberately information-isolated branches:

```text
frozen candidate
  ├→ blind math
  ├→ blind red-team
  └→ blind provenance
        ↓ freeze outputs
             merge
```

Pitfall: false independence. Separate workers inheriting the same generated summary or shared prior conclusion are correlated controls. Exposure metadata matters.

## Nested recurrence

```text
R theory candidate
  ├─ R1 math-test until invariant resolved
  ├─ R2 source-recovery until provenance gap closed
  └─ R3 counterexample sample until break/limit
then merge; children retire
```

Every child needs parent, depth, exit condition, and orphan policy. The executable POC enforces a maximum spawn depth and carries explicit depth metadata.

## State-sensitive recurrence-definition rewrite in situ

```text
constructed        → next = independent check fanout
any check fails    → next = isolate earliest failed assumption
all checks pass    → next = prediction + paper + independent reality check
release gate done  → retire recurrence
```

The definition changes because state changed, not because an LLM became bored.

## Recurrence bootstrap patterns

### Build-tool-then-use-it

Repeated manual operation → deterministic helper/index → bounded validation → rewrite recurrence to consume helper → human/LLM attention moves to exceptions and interpretation.

### Wake/check self-improvement

Missed update class → log failure → identify missing source class → update registered source map, not TOP → next wake tests discovery → successful special watcher retires.

### Education bootstrap

Worker repeatedly uses toolbox → capture candidate lesson → test in second locale/next task → promote only surviving lesson to actor-local experience → periodically test whether experience became bias.

### Theory multiplication/pruning

Ambiguity → parallel A/B constructions in playground/workbench → derive discriminators before target comparison → perpendicular checks → prune unsupported branch → salvage equations/tests/counterexamples/terminology → narrower recurrence.

### Capability bootstrap

Same blocker or awkward workaround → capability scout → existing project tool/built-in/app/plugin/teammate → bounded test → useful route becomes known capability; failed route becomes negative capability memory rather than repeated suggestion.

### Workflow compiler

High-level human/LLM task contract → deterministic code builds dependencies/freeze IDs/exit conditions → LLM handles semantic/creative nodes → deterministic reducer checks structure and eligible next nodes → LLM may propose, but controller validates, recurrence rewrites.

### Delivery receipt bootstrap

Temporary lease → bounded execution → durable output contract → verify receipt/version → restore. If no receipt, produce explicit failure packet and do not misclassify self-restoration as task success.

## Hydra failure modes and guards

### Infinite self-rewrite
Guard: rewrite budget, state fingerprint, parent goal, no rewrite when state unchanged.

### Oscillation / self-undoing
A decides X, B reverses X, A restores X. Guard: append-only history, authority/version preconditions, conflict state instead of silent overwrite, merge/cooldown.

### Task explosion
Guard: max depth, child budget, expected-information-gain threshold, mandatory retire/merge conditions.

### Silent core corruption
Guard: TOP is not writable by recurrence. Core change requires separate explicit/versioned authority.

### Prompt accretion
Guard: prompts point to authoritative docs/state IDs and carry only run-critical deltas/contracts.

### State split / race
Guard: freeze/version IDs, ownership, compare-and-swap writes, merge controller.

### False independence
Guard: exposure metadata; perpendicular lanes consume frozen source, not sibling interpretation; outputs freeze before merge.

### Stale recurrence
Guard: exit/retire condition, last-evidence timestamp, lease garbage collection.

### Goal laundering
A local metric becomes the project goal. Guard: every child carries parent goal + why-it-exists; merge checks relevance.

### Sticky-experience rut
Guard: evidence/status/review date, transfer tests, cross-training/park-walk, occasional actor-without-overlay test.

### Capability nagging
Guard: record suggested/declined/failed capability and resurface only on materially changed task/capability state.

### Directive spoofing / recency confusion
Guard: source class + authorship + directive marker + scope/authority classification. Freshness triggers intake, not automatic obedience.

### Successful-looking no-op / lost output
A recurrence runs and restores perfectly while its requested artifact never becomes durable/discoverable. Guard: output contract + receipt/version check + failure packet. Restoration is downstream of receipt.

### Recursive rewrite corruption
A child recurrence edits the definition that governs its own guard. Guard: recurrence definitions are versioned state objects; writable fields are scoped; parent/controller validates mutations; TOP/authority surfaces are immutable targets.

---

# Actual productive workflow represented by the POC

The theory candidate pipeline is intentionally chosen because it can do all three things Nathan asked for simultaneously:

1. **build/prune theory:** failed checks narrow the object, preserve wreckage, and prevent repeated identical failure;
2. **adjust behavior/capabilities:** toolbox lessons, discovered failure modes, and validated capability routes can become scoped actor experience;
3. **move toward release readiness without claiming truth:** checked narrow claims can feed prediction packets and papers, while separate publication/sandbox gates remain.

A likely production extension would attach exact current SAT/H(s)H controls for object status, math provenance, source provenance, peer review, PDF/rendering, public-site staging, and theory-status discipline rather than reimplementing those controls here.

---

# Team/cognition input and live findings

## Orson Vey

Orson’s existing Vey Cognition Lab program is directly relevant. It explicitly separates base/model capability, post-training/product behavior, context/memory/tools/retrieval/persona/team workflow; tracks exposure; warns about false independence after shared documents/prompts/memory; and names role lock-in, consensus, scheduler effects, handoff loss and provenance drift as team-cognition questions.

A temporary Orson run was invoked during this POC and self-restored its displaced Revival lease. No requested durable advisory appeared in the visible Vey workbench. That absence is treated only as an infrastructure observation—not as evidence about Orson’s reasoning. A durable follow-up request was placed in `Consciousness + AI/VEY_COGNITION_LAB/INBOX.md`.

## Tern

Existing Tern continuity already supports several design choices: one bounded quantum = one object + one operation + one durable result + one next cursor; scheduler slots are execution leases over a larger instance pool; identity/exposure/continuity are separate from lease allocation; and full onboarding should be trigger-based rather than ritual every recurrence.

A temporary Tern recon run was invoked and restored the Nathan Words lease, but again no requested new durable note was recoverable afterward. A durable request is now at `Satobloc/HsH/WORKSPACES/TERN/INBOX.md`. This independently reinforces the output-receipt requirement.

## Production handoff to Sable + Comptroller

For each POC mechanism, classify:

```text
KEEP | MODIFY | TEST | REJECT | DEFER
```

First review targets:

1. source registry + directive promotion;
2. WAKE/CHECK budget and stale-state detection;
3. receipt-gated lease commandeering;
4. perpendicular/exposure-aware review;
5. sticky-experience promotion/expiry;
6. Hydra rewrite authority, rollback, and nesting limits;
7. capability/plugin discovery trigger;
8. sub-sandbox/locker egress rules;
9. push vs poll for authoritative updates;
10. state model: snapshot, event journal, or hybrid.

Do not assume this POC’s Python shape, state schema, file locations, or names are the production architecture. The successful outcome of this prototype is a tested vocabulary and a handful of mechanisms worth keeping—not a commitment to this implementation.
