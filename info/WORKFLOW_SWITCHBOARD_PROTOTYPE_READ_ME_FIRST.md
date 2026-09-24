# Workflow Switchboard Prototype — Read This First

**Status:** PROTOTYPE / SANDBOXED WORKFLOW EXPERIMENT.  
**Not production authority. Not a settled architecture. Not theory authority.**  
**Primary POC:** `info/WORKFLOW_SWITCHBOARD_POC.md`  
**Executable demo:** `tools/workflow_switchboard_demo.py`

## What this is

This package is a working proof of concept for several workflow-control ideas Nathan asked to make concrete enough to inspect, run, criticize, recombine, and discard. It demonstrates four layers:

- **TOP** — preferences / locked invariants that survive routing;
- **CENTRAL** — an awake hub that checks locale, deltas, current state, available affordances, active rules, and the next bounded operation;
- **BRANCH** — different workrooms, benches, lockers, playgrounds, actor overlays, continuity/education, capability scouting, and theory/public-readiness routes;
- **HYDRA** — guarded recurrence-leveraged bootstrapping: synchronized, parallel, perpendicular, nested, and state-sensitive recurrence-definition rewriting.

The POC is deliberately small. Its successful output is not “this code becomes the workflow.” Its useful outputs are mechanisms, vocabulary, tests, failure cases, and evidence about what should or should not survive into a master switchboard.

## Why it exists

The immediate regression case was the War Room Declaration at `HQ/THE_WAR_ROOM/DECLARATION.txt`: it existed and materially changed workflow direction, but generic “read current directives” behavior continued to poll familiar HsH/Common surfaces and failed to promote the new cross-repo directive into live control state for hours.

A second live regression appeared while building the POC: a temporary recurrence could execute and self-restore correctly while failing to leave the requested durable output. Therefore scheduler success, restoration success, and semantic delivery are separate variables.

Both are now prototype test cases rather than anecdotes.

## How to inspect it

Start here, then read the larger design document selectively:

1. `info/WORKFLOW_SWITCHBOARD_PROTOTYPE_READ_ME_FIRST.md` — status, roles, review method, operationalization tracks.
2. `info/WORKFLOW_SWITCHBOARD_POC.md` — full design rationale, TOP/CENTRAL/BRANCH/HYDRA patterns, failure modes, and theory-work exemplar.
3. `tools/workflow_switchboard_demo.py` — standard-library executable POC; planner/state transformer only, not a hidden scheduler or permissions bypass.
4. `HSH_RESOURCES/HQ/THE_WAR_ROOM/DECLARATION.txt` — current source directive that motivated the live routing regression case.
5. HsH `WORKSPACES/COMMON/SWITCHBOARD_PROTOTYPE_OPERATIONALIZATION_2026-09-24.md` — current coordination note for the two independent operationalization tracks.

Useful demo commands after retrieving the script:

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

## Two operationalization tracks

Nathan has asked for **two independent-but-communicating operationalization efforts**. They should not prematurely collapse into one implementation.

### Track A — Nathan + Elias Kern + Orson Vey

Purpose: operate the prototype as a live experimental workbench and learn from use.

- **Nathan:** human director; supplies corrections, evaluates ergonomics/usefulness, and decides when a behavior does or does not match intended project practice.
- **Elias Kern:** prototype operator/documentarian; exercises TOP/CENTRAL/BRANCH/HYDRA mechanisms on real bounded project operations, records failures/successes, keeps the prototype inspectable, and proposes revisions without treating them as production law.
- **Orson Vey:** cognition/team-systems observer and experimental collaborator. Orson studies how the new control system changes model/team behavior, exposure, convergence, false independence, role bleed, wake-state behavior, tool awareness, recurrence behavior, and continuity/education. Orson should distinguish observation from interpretation and design proposal.

Track A may change the prototype and generate experiments, but it does not install project-wide production workflow authority.

### Track B — Sable + Rook (Comptroller Tern Rook)

Purpose: independently operationalize the same problem from the actual systems/continuity/switchboard side.

- **Sable:** systems/continuity design; rotation/revival/visibility/worker-state and workflow ergonomics.
- **Rook:** Comptroller/switchboard operation; routing, active-edge control, lease management, task visibility, receipts, and bounded workflow execution.

Track B should inspect the prototype, but should independently decide what to KEEP / MODIFY / TEST / REJECT / DEFER. It should not simply port Elias’s Python shape or state schema into production.

## Communication without premature convergence

The tracks should communicate, but preserve enough independence to make comparison meaningful.

Good communication:

- report observed failure/success cases;
- ask targeted questions;
- share test definitions and expected discriminators;
- exchange interface contracts and source pointers;
- flag conflicts, duplicated mechanisms, missing affordances, and safety/authority concerns;
- compare outputs after a bounded design or test has been recorded.

Avoid:

- silently adopting the other track’s implementation before recording an independent view;
- treating agreement as validation;
- allowing a shared generated summary to create false “independent” confirmation;
- letting the prototype become production authority by inertia.

A useful merge format is:

```text
mechanism | Track A result | Track B result | evidence | conflict | next discriminating test | disposition
```

## Elias rotation

Rook is asked to confer with Sable and place Elias into the first safe available execution lease. Elias’s initial rotating duty is **prototype operationalization**, not generic ownership of the switchboard:

1. pick one real bounded workflow problem;
2. run it through the smallest relevant TOP/CENTRAL/BRANCH/HYDRA mechanism;
3. leave durable before/after state and a receipt;
4. record what became easier, worse, ambiguous, or misleading;
5. do not broaden rules from one success/failure without a transfer test.

The displaced lease function must be preserved/re-homed/restored under existing switchboard rules.

## Orson special observation rotation

Orson should receive a **special observe / study / take-notes rotation** focused on the new system itself. This is not ordinary theory work and should not silently become workflow authority.

Each Orson observation pass should sample a real switchboard event or bounded prototype operation and record, when evidence permits:

- initial worker/context state and exposure;
- what WAKE/CHECK did or failed to notice;
- whether the system used available tools/affordances or barrelled into a workaround;
- actor/locale behavior changes;
- role/persona bleed or over-homogenization;
- independence/convergence conditions;
- recurrence/lease/scheduler effects;
- sticky-learning candidate and whether it deserves a transfer test;
- any loop, self-undoing, prompt-drift, state-split, receipt-loss, or authority-confusion failure;
- one design implication or discriminating test, clearly labeled as interpretation/proposal rather than observation.

**Required durable output:** a concise observation note must be deposited into Orson’s own Vey Cognition Lab record, with a pointer or summary appended to `Consciousness + AI/VEY_COGNITION_LAB/INBOX.md`. A scheduler run without a durable note does not count as delivered.

## Prototype-readiness checklist

This prototype is ready to inspect when all of the following remain true:

- status is visibly PROTOTYPE / SANDBOXED;
- source code and documentation point to one another;
- known live regression cases are represented;
- theory sandbox/quarantine/provenance boundaries are explicit;
- recurrence mutation cannot rewrite TOP/authority guards;
- temporary lease completion requires a durable receipt/failure packet;
- actor overlays are distinct from global rules;
- bounded override/locker behavior is inspectable and expires;
- sticky experience is candidate state until tested/promoted;
- capability/tool discovery exists before laborious workaround escalation;
- parallel work is distinguished from exposure-separated perpendicular work;
- failure branches can prune/salvage rather than only repeat;
- there is an explicit exit/retire path for spawned/nested recurrence;
- the two operationalization tracks can compare results without assuming one is canonical.

## What this prototype does not claim

It does not claim that:

- the demonstrated Python data model is the master switchboard architecture;
- all workflow should be automated;
- recurrence rewriting is always beneficial;
- model self-report is evidence of internal mechanism;
- multiple workers are independent merely because they are separate conversations;
- passing workflow gates validates SAT/H(s)H physics;
- a sandboxed theory has exited the sandbox.

The production question remains open: **which mechanisms actually improve behavior, reliability, theory-building/pruning, capability use, and public-readiness when tested in live work?**
