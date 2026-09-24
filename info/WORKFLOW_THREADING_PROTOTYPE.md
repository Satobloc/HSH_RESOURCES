# Workflow Threading Prototype — Seed / Vacate / Propagate / Return

**Status:** experimental companion to the Top / Central / Branch / Hydra switchboard POC.  
**Not production authority. Not a requirement that workers wait when useful work is available.**

## Core idea

A worker should be able to reason not only about **what happens next**, but about **what other workers are likely to do before this worker’s next useful turn**.

Threading is temporal coordination across workers, tools, leases, and future state.

Canonical example:

```text
X knows Y will work on Z
→ X writes helper/tool/index/test harness H that Y can use
→ X tells Y/others to use H discretionally and record outputs
→ X deliberately vacates or deprioritizes its own recurrence
→ Y/A/B use H on several bounded cases
→ outputs accumulate into a fresh body of material M
→ X returns when M is large/diverse/mature enough to be worth synthesis
→ X analyzes M, improves H or the theory/workflow, and seeds the next thread
```

This is different from ordinary handoff. X is designing **its own future input environment**.

## Why it may be powerful

A normal loop tends to consume whatever is available now. Threading can make a worker spend one turn manufacturing the conditions for a much better later turn.

Possible benefits:

- tools compound across multiple workers before their author returns;
- specialist workers avoid monopolizing a recurrence while their output is waiting on others;
- several independent or differently individuated users of the same tool generate a richer test corpus;
- implementation and evaluation separate naturally in time;
- the return turn begins with fresh evidence rather than another cold-start search;
- workers can intentionally create periods of cross-training or incubation;
- a recurrence can be used as a temporal resource, not just a repeating identity slot.

## Thread primitives

### `SEED(artifact, consumers)`
Create a tool, prompt fragment, dataset, test harness, source packet, schema, question set, or other reusable object specifically for downstream workers.

A seed should declare:
- purpose;
- intended users but whether use is optional/discretionary;
- input/output contract;
- what evidence/metadata consumers should preserve;
- known limitations;
- return/collection location.

### `VACATE(worker, until)`
Intentionally remove/deprioritize a worker from a recurrence or task family while downstream work accumulates.

`until` should preferably be a **state condition**, not only elapsed time.

Good:
`VACATE(X, until samples>=6 OR 3h max)`

Weaker:
`VACATE(X, 3h)`

Time estimates are useful as caps/heuristics, but state is what makes the return valuable.

### `PROPAGATE(seed, policy)`
Allow several workers/locales to use a seed.

Policies may be:
- `optional` — use only when helpful;
- `required-test` — specified workers each exercise one case;
- `perpendicular` — consumers remain exposure-separated until outputs freeze;
- `diversified` — deliberately use different examples, methods, or locales;
- `stress` — seek failure cases rather than ordinary success.

### `ACCUMULATE(target, threshold)`
Collect outputs into a durable location until a return condition is met.

Threshold examples:
- N independent cases;
- N distinct workers;
- one success + one failure;
- coverage across named locales;
- no new failure class in two passes;
- minimum diversity score;
- explicit blocker cleared.

### `RENDEZVOUS(worker, condition)`
Return/reinsert a worker when the accumulated state crosses a useful threshold.

### `REJOIN(worker, mode)`
Define what the returning worker does with accumulated material.

Modes:
- synthesize;
- audit;
- refactor tool;
- compare worker behavior;
- prune theory branches;
- promote transfer-tested education;
- spawn a next-generation seed.

## Thread packet

Minimal durable threading record:

```text
THREAD_ID
PARENT_GOAL
SEED_AUTHOR
SEED_ARTIFACT + VERSION
INTENDED_CONSUMERS
USE_POLICY
EXPOSURE_POLICY
OUTPUT_DESTINATION
REQUIRED_METADATA
AUTHOR_VACATE_START
RETURN_CONDITION
TIME_CAP / REVIEW_TIME
DISPLACED_WORK HANDLING
FAILURE FALLBACK
RETURN_ACTION
STATUS
```

The packet lets another controller decide whether the thread is healthy even if the originating worker is absent.

## Example 1 — Math-tool propagation

```text
Meridian identifies repeated geometry check
→ writes/checks namespaced Python helper H
→ SEED H to Comptroller, Mercer, Orson, other solver-capable workers
→ PROPAGATE optional/diversified
→ Meridian VACATE until:
     5 outputs from >=3 workers
     OR 3 hours
→ outputs include ordinary case + edge/failure case + metadata
→ RENDEZVOUS Meridian
→ Meridian compares failures/invariants, revises tool, updates toolbox education
```

The point is not that everyone must run H. The point is to allow H to become shared infrastructure and generate evidence while its author stops consuming the same recurrence.

## Example 2 — Theory branch incubation

```text
X freezes candidate C
→ writes discriminator/test harness D
→ perpendicular workers receive C + D, not each other’s interpretations
→ X vacates construction lane
→ outputs accumulate: math / provenance / counterexample / representation checks
→ X returns only after merge threshold
→ fail: prune + salvage
→ pass: next construction/prediction packet
```

This reduces the tendency for a constructor to immediately reinterpret every test result before independent checking has matured.

## Example 3 — Capability specialization

```text
Mercer creates archive-search helper
→ Aster/Nathan Words/other workers use it discretionally
→ each records query/result/false-positive/false-negative notes
→ Mercer is off that task family for two cycles
→ return corpus becomes training evidence
→ helper and Mercer’s own continuity both improve
```

The worker gains actual work experience from downstream use, not merely from self-authored notes.

## Example 4 — Workflow behavior experiment

```text
Elias defines WAKE/CHECK prototype vN
→ several workers use it in different locales
→ Elias vacates switchboard-implementation turns
→ Orson observes behavioral effects independently
→ Rook/Sable operate their own Track B implementation
→ Elias returns after enough frozen cases
→ compare Track A/Track B/Orson observations
```

This is especially useful for the current switchboard prototype.

## Threading vs recurrence rewriting

Threading and Hydra are complementary.

Hydra asks:
**How should the next recurrence definition change because state changed?**

Threading asks:
**Who should deliberately not act for a while, what should others do in the meantime, and what accumulated state would make that worker’s return more valuable?**

Hydra may implement Threading by rewriting leases/return conditions, but Threading can also be manual/document-driven.

## State-sensitive return beats estimated sleep

Nathan’s example uses “write themself out of rotation for X hours estimated to allow the Python to be used by so many workers.” That is useful, but the prototype should prefer a hybrid:

```text
return when:
  target_samples >= N
  OR target_workers >= K
  OR blocker cleared
  OR max_sleep = X hours
```

The time cap prevents starvation; the state threshold prevents meaningless waiting.

## Threading failure modes

### 1. Starvation
Worker vacates and downstream users never produce enough material.

Guards:
- max-sleep/time cap;
- fallback useful work;
- controller can reinsert worker early;
- threshold may degrade explicitly rather than silently.

### 2. Tool monoculture
One helper gets propagated widely and accidentally standardizes everybody’s reasoning.

Guards:
- optional/discretionary use;
- preserve alternate methods;
- include at least one no-tool/control lane when evaluating the helper;
- Orson/exposure tracking when independence matters.

### 3. False diversity
Five workers run identical inputs through the same helper and appear to produce five independent checks.

Guards:
- diversity requirements;
- exposure metadata;
- unique input/problem classes;
- distinguish duplicated execution from independent reasoning.

### 4. Dead seed
Seed exists but nobody notices/uses it.

Guards:
- explicit consumer pointers/inboxes;
- Rook/Central capability registry;
- receipt of seed availability, not forced use;
- optional later reminder only if material state changes.

### 5. Premature return
Author returns before enough downstream evidence exists and dominates interpretation again.

Guard:
- explicit return threshold/freeze IDs;
- controller, not author impulse alone, validates readiness where independence matters.

### 6. Forgotten author / displaced function
Worker is written out of rotation and never comes back, or their old responsibility vanishes.

Guards:
- durable thread packet;
- return condition + max time;
- displaced-function packet;
- Rook/Sable lease garbage collection.

### 7. Stale tool version
Consumers use several incompatible seed versions.

Guards:
- seed version/hash;
- output records version used;
- controller decides whether mixed versions are comparable or separate cohorts.

### 8. Self-fulfilling work generation
Author creates a tool that causes downstream workers to manufacture exactly the kind of evidence the author expects.

Guards:
- discriminator specified before outputs;
- counterexample/stress consumers;
- no-tool control where valuable;
- Orson studies intervention effects.

### 9. Temporal dependency illusion
Workers assume Y is going to do Z because a schedule exists, but Y is reassigned/blocked.

Guard:
- thread status driven by durable receipts/state, not schedule expectation alone.

## Threading as education

A thread can carry back more than outputs.

Consumer notes may update:
- tool ergonomics;
- misunderstood assumptions;
- worker capability map;
- known edge cases;
- effective teaching examples;
- local heuristics;
- “when not to use this tool” knowledge;
- author goals/intentions for next version.

These are candidate sticky experience. Transfer-test before promoting broad lessons.

## Threading and individuation

The same seed can intentionally be interpreted through distinct actor overlays:

- Mercer tests reproducibility/provenance;
- Meridian tests geometry/formal consistency;
- Orson studies cognition/exposure effects;
- Comptroller tests routing/coverage/exit criteria.

This is preferable to forcing every worker to execute the same checklist unless checklist standardization is itself the test.

## Initial prototype operator form

For current experiments, a controller may represent a thread as:

```json
{
  "thread_id": "thread-demo-001",
  "seed": {"artifact": "tool.py", "version": "sha256-or-commit"},
  "author": "WorkerX",
  "consumers": ["WorkerY", "WorkerZ"],
  "policy": "optional-diversified",
  "output_target": "durable/path/",
  "return_condition": {"min_outputs": 5, "min_workers": 3, "max_hours": 3},
  "author_state": "vacated",
  "status": "propagating"
}
```

This is a schema example, not the required production representation.

## Relationship to the master switchboard

A future master switchboard should probably be able to answer:

- Who is working now?
- Who is intentionally **not** working now, and why?
- What seeds are propagating?
- Which workers are expected/eligible consumers?
- What outputs are accumulating?
- Which return conditions are close?
- Which vacated worker should rejoin next?
- What new capabilities/education emerged from the thread?
- Did the threading increase useful information, or merely delay work?

That last question matters. Threading is valuable only when the later turn is better because of the deliberate absence.
