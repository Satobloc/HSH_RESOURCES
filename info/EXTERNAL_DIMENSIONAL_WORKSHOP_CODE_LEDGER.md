# External Dimensional Workshop — Unicode Code Ledger

**Status:** Bespoke experimental pilot. Local meanings only; no general recommendation implied.  
**Version:** 0.1  
**Updated:** 2026-11-24

## Grammar

Single Unicode code points represent phases, operators, components, or states. Adjacent tokens imply left-to-right succession. Structural operators preserve their defined semantics. The live signature carries codes; this ledger carries meanings. Memorization is unnecessary.

For branches, `⑂{cu}` is equivalent to `⑂{A: Credenza | B: Unicode notation}` when component codes are defined and left-to-right order is sufficient. Where additional ordering labels are needed, uppercase labels indicate branch/order positions and lowercase tokens identify components: `⑂{AcBu}`.

No undefined placeholders. A code may refer to a real, identifiable, populated, extensible collection.

## Phase codes

| Glyph | Code point | Canonical meaning | Class | Scope / constraints |
|---|---|---|---|---|
| ⌖ | U+2316 | Orient | Phase | Recover relevant context and position |
| ◉ | U+25C9 | Focus / select Tock | Phase | Select and bound the substantial work unit |
| ⌕ | U+2315 | Investigate | Phase | Locate and examine sources or concepts |
| ⧖ | U+2996 | Geometrize | Phase | Construct the geometric/dimensional account |
| ⤳ | U+2933 | Connect | Phase | Follow relevant connections |
| ▣ | U+25A3 | Record | Phase | Preserve durable result |
| ✓ | U+2713 | Verify | Phase | Check claims, locators, result, and storage |
| ⇢ | U+21E2 | Deliberate transition / next | Operator | Explicit decision/transition point; not ordinary succession |

## Compound workflow operators

| Glyph | Code point | Canonical meaning | Class | Scope / constraints |
|---|---|---|---|---|
| ⑂ | U+2442 | Fork | Operator | Split into independently tracked branches |
| ⑃ | U+2443 | Rejoin | Operator | Reconcile branch outputs before shared continuation |
| ⟳ | U+27F3 | Cycle | Operator | Repeat a delimited sequence to an exit condition |
| … | U+2026 | Await | Operator | Suspend marked path pending specified event/condition |
| ■ | U+25A0 | Halt | Operator/state | Stop a path; annotation or ledger state distinguishes complete, cancelled, parked |

## Component codes

| Glyph | Code point | Canonical meaning | Class | Scope |
|---|---|---|---|---|
| c | U+0063 | Credenza system | Component | Navigation, routing, work tray, cubbies, continuity and attention |
| u | U+0075 | Unicode workflow notation | Component | Compact phase/operator language and live workflow signature |

## Defined collections

None registered yet. Add a collection only when it exists as an identifiable, populated list or registry. It may remain extensible.

## State and Tock tracking

Tock is the higher-level bounded work package; Tick is a subordinate operation or position marker within it. The Credenza routes and preserves Tocks; the Unicode string describes their internal Tick structure. Tock completion requires a durable result and recorded next cursor. The live signature is the Tick-level compact representation; the ledger stores full Tock status and history.


## Change control

Never silently reassign a glyph. Add new codes with meanings, code points, class, scope, date/version, and syntax constraints. For changed meanings, retain a supersession record.

## Research-domain component codes

| Glyph | Code point | Canonical meaning | Class | Scope |
|---|---|---|---|---|
| m | U+006D | Mathematics / category theory | Component | Category theory, geometry, topology, higher structures |
| b | U+0062 | Biology | Component | Organismal biology, physiology, evolution, biological organization |
| h | U+0068 | History and cultural lineage | Component | Victorian dimensional thought, spiritualism, science fiction, fandom, time-binding |
| p | U+0070 | Computation | Component | Computational models, simulations, programming, computational tools |
| s | U+0073 | Science bridges | Component | Cross-disciplinary applications and connections |
| w | U+0077 | Workshop systems | Component | Credenza, notation, methods, workflow experiments and infrastructure |

## Tock codes

| Glyph | Code point | Canonical meaning | Class | Scope |
|---|---|---|---|---|
| t | U+0074 | Initial workshop Tock | Tock | Complete starting ledger and establish the ordered research programme |

## Position marker

| Glyph | Code point | Canonical meaning | Class | Scope |
|---|---|---|---|---|
| @ | U+0040 | Current position marker | State marker | Prefixes the next uncompleted item in the active Tock/Tick sequence. It does not itself add a workflow operation. |

**Placement rule:** place `@` immediately before the next uncompleted token. The preceding tokens are completed; the following tokens remain. For a compound branch, place it before the next branch or operation to execute. If the next item is itself a compound structure, place it before that structure.

