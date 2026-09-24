# Workflow Threading Operators — Concurrency/Dataflow Vocabulary

**Status:** experimental companion vocabulary for `WORKFLOW_THREADING_PROTOTYPE.md`.  
**Prototype only; operator names are not production API commitments.**

Nathan’s seed/vacate/return idea maps naturally onto concurrency/dataflow concepts. These names may make complicated temporal coordination easier to express and inspect.

## Core operators

### `SPAWN(task_or_thread)`
Create one or more downstream bounded work threads without requiring the spawning worker to remain active.

Use when the work can proceed independently enough to justify parallel or deferred execution.

### `YIELD(worker, reason, return_condition)`
The current worker intentionally gives up its execution lease/task-family presence because additional self-work has lower expected value than letting downstream state mature.

`YIELD` should state:
- why absence is productive;
- displaced-function handling;
- return condition;
- maximum absence/time cap;
- fallback if no downstream progress occurs.

### `AWAIT(condition)`
Do not spend active recurrence cycles repeatedly checking the same unresolved dependency. Reinsert only when a durable state change or bounded polling rule says the awaited condition changed.

Examples:
- `AWAIT(samples>=5 OR 3h)`
- `AWAIT(provenance_packet.version > v7)`
- `AWAIT(blocker=cleared)`

This is a workflow primitive, not literal asynchronous background execution by the model.

### `JOIN(thread_set, merge_rule)`
Merge frozen outputs from several threads after their required exit/receipt conditions are satisfied.

A JOIN should specify:
- required/optional children;
- version/freeze IDs;
- exposure/independence status;
- conflict handling;
- what counts as sufficient completion;
- whether failed children still contribute salvage evidence.

### `BARRIER(condition_or_version)`
Prevent a set of workers from advancing past a stage until a shared state boundary is satisfied.

Useful for:
- freeze-before-independent-checks;
- do-not-read-siblings-before-output-freeze;
- do-not-publish-before-review receipts;
- do-not-rewrite recurrence before state version N.

A barrier should not become a deadlock trap: include timeout/escalation/fallback.

### `BACKPRESSURE(source, limit)`
Slow or stop upstream generation when downstream capacity is saturated or unprocessed outputs exceed a threshold.

Examples:
- stop spawning new theory candidates when five unchecked candidates already exist;
- stop archive extraction when theorist-feed backlog exceeds review capacity;
- stop generating helper variants until existing versions have enough test coverage.

Backpressure is important because productive branching can otherwise become task pollution.

### `FUTURE(id, expected_artifact)`
A durable promise-like placeholder saying that a later worker/thread is expected to produce a specific artifact/state.

A FUTURE is not treated as completed evidence. It becomes fulfilled only by a durable receipt/version.

### `CANCEL(thread, reason)`
Explicitly stop a thread whose value has collapsed, whose parent goal changed, or whose work has been superseded. Preserve useful partial outputs and provenance rather than silently abandoning them.

### `TIMEOUT(thread, fallback)`
Bound waiting/vacation. Timeouts should trigger reassessment, not automatically declare the downstream work failed.

## Canonical threaded pattern

```text
SEED(H)
→ SPAWN(Y_use_H, Z_stress_H, O_observe_H)
→ YIELD(X, "downstream evidence now higher value", samples>=5 OR 3h)
→ AWAIT(receipts>=5 OR timeout)
→ BARRIER(freeze_id=H_v1)
→ JOIN(children, preserve_disagreement)
→ REJOIN(X, synthesize/refactor/prune)
```

## Example — helper tool with backpressure

```text
X writes tool H_v1
→ SPAWN 4 discretionary consumers
→ YIELD X
→ outputs arrive
→ if pending_unreviewed_outputs > 8:
     BACKPRESSURE(H_v1, stop_new_consumers)
→ if >=3 workers + success + failure:
     JOIN
→ X REJOINs to revise H_v2
```

## Example — theory candidate generation

```text
constructor SPAWN candidate A, B, C
→ independent check lanes
→ BACKPRESSURE when unchecked_candidates >= 3
→ BARRIER on frozen candidate versions
→ JOIN evidence
→ CANCEL unsupported candidates with salvage
→ only then SPAWN next generation
```

## Example — planned future dependency

Worker X knows Y is scheduled/expected to produce Z.

Bad:
`X assumes Z will exist by next hour.`

Better:

```text
FUTURE(Z_packet, expected path/version contract)
→ X prepares helper H that consumes Z_packet
→ X YIELDs
→ switchboard watches durable receipt, not schedule expectation
→ receipt fulfills FUTURE
→ X REJOINs and runs H against actual Z
```

This avoids the temporal-dependency illusion: schedule ≠ delivered artifact.

## Operator-composition notes

These operators can combine with the existing switchboard language conceptually:

- `SPAWN(A|B|C)` — create alternative/parallel children;
- `SPAWN(A+B)` — create composed child work;
- `@YIELD(...)` — one-shot temporal override;
- `[math]BARRIER(freeze=v4)` — scope barrier to math lane;
- `FALLBACK(AWAIT(x), TIMEOUT(...))` — bounded wait;
- `ROUTE{backlog-high:BACKPRESSURE|*:SPAWN}` — state-sensitive generation control.

Exact syntax is still experimental.

## What threading adds to the master switchboard

Without temporal/thread operators, the switchboard mostly decides **who should do what now**.

With them, it can also decide:

- who should deliberately stop;
- which future artifacts should be prepared for now;
- what work should incubate before synthesis;
- when fan-out has become excessive;
- when downstream evidence is mature enough to bring a specialist back;
- when to merge, cancel, or throttle branches;
- whether a recurrence is waiting on time, state, or merely assumption.

That makes recurrence leases closer to a managed dataflow graph than a row of repeating cron jobs.
