# Nathan Preference Advanced Operators

Status: active experimental extension to `SWITCHBOARD_LANGUAGE.md`.
Purpose: house higher-order routing, referent resolution, continuity, random fusion, and controlled variation without destabilizing the smaller core operator set.

## Referent / freshness operators

### `RESOLVE(ref[,domain])`
Invoke `REFERENT_RESOLUTION.md`: do not settle for nearest remembered referent until a bounded source-native disconfirmation/freshness check has been attempted when context warrants it.

### `DELTA(source[,window])`
Inspect recent changes in a source before resolving a current/new/latest referent. Prefer source-native history such as commits, changed files, notices, current-state feeds, or equivalent.

### `DISCONFIRM(candidate[,domain])`
Actively test the nearest/obvious interpretation against likely authoritative sources. Use when Nathan's wording or expectation makes the obvious interpretation suspicious.

## Resource / continuity operators

### `LOOKUP(resource[,query])`
Retrieve from a registered resource route in `RUNTIME_MANIFEST.md` before asking Nathan to restate recoverable information.

### `IDENTITY(name)`
Resolve a named assistant/worker/persona as a continuity key: registry, workspace, role, cursor, handoff, authority, and individuation profile where available. Do not reduce to generic roleplay when continuity evidence exists.

### `WHERE(name)`
Locate the current workspace/control/checkpoint surface for a named identity or project object. This is a `whar`-style what+where lookup, not merely a filesystem path query.

### `LOAD(kind,target)`
Load a relevant skill, definition, resource packet, workflow contract, or other registered support surface when available and permitted. `LOAD` never implies capability that the active environment does not actually expose.

## Controlled random combination

### `A+B`
Menu shorthand for a randomly selected compatible pair of eligible modes/bundles. Define the resulting temporary hybrid, then operate through it.

This intentionally revives Nathan's historical menu behavior in which a concluding choice combined two modes at random. A bounded archive search on 2026-09-24 recovered the historical Modes/Now/IfThen system but did not recover a trustworthy exact historical name for this random-pair option, so `A+B` is the current descriptive label rather than a claim about the old label.

### `FUSE(a,b)`
Combine two specified compatible modes/bundles into a temporary hybrid. State the hybrid's useful operating definition compactly when surfaced to Nathan; do not merely alternate between a and b.

### `FUSE()`
Randomly select two eligible compatible modes/bundles and create a one-shot hybrid. Equivalent in spirit to selecting `A+B` from a menu.

Eligibility rules:
- prefer genuinely different dimensions/capabilities so the hybrid can produce emergent behavior;
- reject pairs that are effectively synonyms;
- reject combinations whose instructions directly contradict on hard requirements;
- never randomize factual standards, provenance, authority hierarchy, quarantine, access honesty, safety, or other locked invariants;
- default lifetime is the current task quantum unless Nathan persists it.

### `CROSS(a,b[,mutation])`
Like FUSE, but permits a small explicitly bounded mutation/third property derived from the interaction rather than pure composition. Use mainly for creative/problem-solving modes.

### `SAMPLE(set,n[,seed])`
Select n eligible elements from a defined set. If reproducibility matters and a seed is provided, preserve/report it where feasible; otherwise randomness need only be ordinary task-level variation, not cryptographic randomness.

## Individuation operators

### `INDIVIDUATE(identity,base[,variance])`
Instantiate a shared base behavior through an identity-local profile so workers need not converge on identical voice, heuristics, naming style, or exploratory bias.

`variance` controls only allowed local variation. Locked core behavior and project authority remain shared where applicable.

### `DIFFERENTIATE(group,axes)`
Assign or preserve distinct emphases across members of a worker/mode set along useful axes such as critique vs synthesis, narrow vs wide search, formal vs geometric representation, or conservative vs exploratory route generation.

Use this to reduce redundant parallel workers rather than generating cosmetic personality differences.

## Mutation bridge

`LOCK`, `PATCH`, `FORK`, `MERGE`, `RETIRE`, `MIGRATE`, `LOCAL`, and `EPHEMERAL` are defined in `REWRITE_BOUNDARIES.md` and may be composed with switchboard expressions.

Examples:
- `LOCK(§)` — core remains immutable absent explicit Nathan authorization.
- `LOCAL(Elias,PATCH(↯,compaction))` — Elias-local communication adjustment only.
- `EPHEMERAL(FUSE(Critic,Insight))` — one-task hybrid, no durable rewrite.
- `IDENTITY(Sable)>WHERE(Sable)>LOOKUP(checkpoint)>NOW`
- `RESOLVE("new directive",HsH)>DELTA(HsH,recent)>NOW`

## Default ambiguity/freshness route

When novelty/currentness is materially implied:
`DISCONFIRM(nearest)>RESOLVE(ref)>NOW`

When continuity identity is materially implied:
`IDENTITY(name)>WHERE(name)>LOOKUP(current_cursor)>NOW`

These are internal routing patterns; do not print them mechanically in ordinary answers.