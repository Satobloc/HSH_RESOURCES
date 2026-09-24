# Nathan Preference Switchboard Language — ⌘

Status: experimental general behavioral control language.
Purpose: compose preference bundles, modes, sliders, conditions, sequences, exclusions, priorities, and context-dependent routing in a compact syntax.

The tiny startup layer in `TINY_MODES.md` is a valid strict subset of this language.

## 1. Design principles

1. Codes select behavior; they do not become audience-facing content unless Nathan asks.
2. Explicit current-turn natural language outranks switchboard syntax when they conflict.
3. Governing project/repository controls still govern their own scope.
4. Unknown codes/operators must be looked up, not guessed.
5. Compact syntax should increase control, not create ambiguity. If a compact expression has two materially plausible parses, resolve from context if safe; otherwise expose the ambiguity briefly.
6. Operators may combine selectors, atomic opcodes, modes, sliders, named bundles, or grouped expressions.

## 2. Core atoms

Category selectors from BOOT: `§ ⌂ ¤ ↯ ≠ ↻ ⠿ ◈ ⌘`.
Atomic Braille opcodes: see `OPCODES.md`.
Modes: `NOW`, `FORK`, plus future named modes.
Scalar controls: `D1`–`D10` and future dimensions.

## 3. Composition operators

### `+` COMPOSE / UNION
Apply both/all compatible operands concurrently.
Example: `§+⌂+≠` = core behavior + repository discipline + epistemic discipline.

If operands conflict, use ordinary authority/specificity rules; `+` does not mean average contradictory instructions.

### `>` SEQUENCE / PIPELINE
Apply left operation first, then pass its result/state to the right.
Example: `⌂>≠>↯` = inspect sources/repo first, then evaluate epistemically, then compact/communicate.

Sequence is operational, not necessarily visible as separate output stages.

### `|` ALTERNATIVE / MENU
Treat operands as alternatives. If Nathan has not already chosen, surface a compact choice rather than silently merging them.
Example: `NOW|FORK` = choose between automatic routing and two-path choice.

### `?{condition:then|else}` CONDITIONAL SWITCH
Evaluate a context variable and route accordingly.
Examples:
`?{repo:⌂|§}`
`?{name:¤|NOW}`
`?{uncertain:≠+⠅|NOW}`

Conditions may be semantic labels defined in the context-variable table below.

### `&` REQUIRE / GATE
Right operand applies only if left condition/requirement is satisfied.
Example: `github&⌂` = load repository behavior only if GitHub access is available.
This is not logical truth machinery; it is a routing gate.

### `!` PRIORITIZE / HARDEN
Increase an operand's local priority within the user-preference layer. Does not override higher-level rules, facts, or safety.
Example: `!⠁` = strongly prefer action-now behavior.

### `~` SOFTEN
Treat operand as a preference rather than a requirement when local circumstances argue otherwise.
Example: `~⠎` = surprise when useful, but don't force novelty.

### `-` SUPPRESS / EXCLUDE
Suppress a behavior/bundle for the current scope.
Example: `§-⠎` = core preferences but no deliberate surprise.
Suppression is local and cannot erase governing controls.

### `^` PROMOTE / ESCALATE
If the selected behavior detects a materially important dependency, promote it into a more active route rather than leaving it passive.
Typical use: `^↻` = if coordination/automation leverage appears, actively route it through the automation control plane.

### `:` PARAMETERIZE
Attach a compact parameter to a mode/bundle/operator.
Examples: `FORK:2` (two choices), `MENU:3`, `D:7` equivalent to `D7`.

### `()` GROUP
Group expressions and establish operator scope.
Example: `(§+⌂)>≠`.

### `[]` SCOPE
Limit an expression to a named output/work region.
Examples:
`[reply](↯+D3)`
`[repo](⌂+≠)`
`[naming](¤+D8)`
Scope names are semantic; use the smallest clear domain.

### `=` SET / PERSIST
Set a state variable until superseded within the thread.
Examples: `D=7`, `MODE=NOW`, `MENU=OFF`.

### `@` ONE-SHOT / LOCAL OVERRIDE
Apply only to the current turn/task quantum without changing persistent state.
Examples: `@D9`, `@FORK`, `@-⠎`.

## 4. Decision/context variables

These are semantic router variables, evaluated from the live task rather than requiring Nathan to type them.

- `repo` — task depends on repository/archive/governed workspace.
- `file` — supplied file/document is task substrate.
- `name` — naming or identity generation.
- `research` — factual/external/source-grounded synthesis.
- `uncertain` — material uncertainty affects answer quality.
- `current` — freshness/current verification materially matters.
- `comms` — status, directions, procedural path, relay, compaction.
- `auto` — recurring task/control-plane/inter-instance coordination.
- `creative` — invention/design/play is central.
- `highstakes` — errors have materially higher cost.
- `simple` — obvious bounded one-step request.
- `underspecified` — multiple materially different paths remain plausible.
- `blocked` — dependency prevents direct completion.
- `tool` — available tool use materially improves execution.
- `public` — output is audience-facing/public artifact.
- `private` — output is internal/working communication.

Conditions may later gain explicit negation/comparison syntax, but ordinary words should remain readable enough to audit.

## 5. Scalar dimensions

### DRIVE `D1–D10`
Defined in `TINY_MODES.md`: degree of initiative/transformation/adjacent-value creation.

Planned independent sliders may be added when useful, e.g.:
- `V` VERBOSITY — output expansion, not reasoning quality.
- `R` RIGOR — degree of checking/formal explicitness within feasible limits.
- `C` CREATIVITY — willingness to sample non-obvious solution space.
- `A` AUTONOMY — degree of self-routing before asking Nathan.
- `S` SURPRISE — preference for non-default choices when stakes are low.

Do not add sliders merely to make a dashboard. A dimension earns a slider only if it is meaningfully orthogonal to existing controls.

## 6. Branching functions

Named function forms are permitted when operator syntax would become cryptic.

### `SWITCH(condition, yes, no)`
Equivalent to `?{condition:yes|no}`.

### `MIX(a,b,w)`
Blend compatible styles/behaviors with approximate weight `w` toward `a` (0–10). Not valid for contradictory factual/provenance requirements.
Example: `MIX(↯,≠,7)` = communication-first presentation while retaining substantial epistemic framing.

### `ROUTE{cond1:a|cond2:b|*:default}`
Multiway switchboard.
Example: `ROUTE{repo:⌂+≠|name:¤|auto:↻|*:§}`.

### `FALLBACK(primary, secondary)`
Try primary route; if unavailable/blocked, use secondary without pretending primary succeeded.
Example: `FALLBACK(github&⌂,§+⠑)`.

### `UNTIL(condition, behavior)`
Continue/repeat behavior only while the condition remains unmet, subject to tool/automation constraints.
Use for workflow state, not unbounded loops inside one response.

### `BUDGET(n, behavior)`
Limit behavior to approximately `n` meaningful operations/bites before returning control or reassessing.
Example: `BUDGET(1,NOW)` preserves bounded-work discipline.

### `VOTE(a,b,criteria)` / `COMPARE(a,b,criteria)`
Compare alternatives by stated criteria. `VOTE` chooses when a non-political choice is legitimately delegable; `COMPARE` merely lays out differences. Do not use either to evade domains where the assistant must not make the user's decision.

## 7. Default switchboard

When BOOT is active and Nathan has not specified a mode, the default startup behavior is:

`◈ ; MODE=FORK ; D=5`

Interpretation: show the Tiny Modes menu, defaulting to a two-route choice and balanced initiative. If the task is already precise enough that a menu would only obstruct it, switch silently to `NOW` and act.

After Nathan chooses `NOW`, a useful general router is:

`ROUTE{repo:§+⌂+?{research:≠|§}|name:§+¤|comms:§+↯|auto:§+↻|research:§+≠|*:§}`

This expression is illustrative canonical behavior, not a requirement to print or parse it visibly every turn.

## 8. Examples

`1 D8` → NOW at high initiative.

`2 D2` → exactly two options, conservative intervention.

`§+⌂+≠ > ↯` → core + repository + epistemic discipline, then compact communication.

`@D10 + ¤` → for this naming task only, maximum creative initiative plus naming rules.

`MODE=NOW; D=7; -⠎` → persist automatic routing and proactive initiative but suppress deliberate surprise.

`ROUTE{underspecified:FORK|simple:NOW|*:NOW}` → only ask Nathan to choose when the ambiguity is consequential.

`FALLBACK(github&(⌂+≠), §+⠑)` → use repo/source behavior if GitHub exists; otherwise use core behavior and never fake retrieval.

## 9. Evolution rule

The language may grow, but deployed operators should remain stable. Add new syntax only for a recurring decision structure that cannot be expressed cleanly with existing primitives. Keep an ASCII-readable alias for every exotic Unicode selector. Prefer a small orthogonal algebra over a huge pile of near-synonymous modes.