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


## Research sequence and ordering codes

| Glyph | Code point | Canonical meaning | Class | Scope |
|---|---|---|---|---|
| 0 | U+0030 | Setup and starting-ledger closeout | Tock component | Finish and verify initial ledger; closed when verified |
| 2 | U+0032 | Mathematics, category theory, geometric atlas | Tock component | First substantive literature/reconstruction programme |
| 1 | U+0031 | Biological applications | Tock component | Biological uses and mathematical models |
| 3 | U+0033 | Historical and cultural lineage | Tock component | Victorian dimensional thought through later cultural reception |
| 4 | U+0034 | Computation and modelling | Tock component | Computational implementations, simulations and tools |
| 5 | U+0035 | Cross-disciplinary science connections | Tock component | Connections and applications across sciences |
| 6 | U+0036 | Workshop evaluation and adaptation | Tock component | Evaluate and revise the pilot workflow and Credenza integration |

**Ordering convention:** these numeric tokens are the user's requested priority labels, not numerical sort order. The active sequence is explicitly `0 → 2 → 1 → 3 → 4 → 5 → 6`. Do not reorder numerically. The signature is read left to right.

## Current status and position

- `0` setup/starting-ledger closeout: provisionally complete; the initial ledger, protocol, reading-note template, code ledger and index have been created and read back. A final completeness review remains the acceptance check.
- `2` mathematics/category theory/geometric atlas: next.
- `1` biology: queued.
- `3` history/cultural lineage: queued.
- `4` computation/modelling: queued.
- `5` science bridges: queued.
- `6` workshop evaluation/adaptation: queued.

Position marker `@` precedes the next active component. The resulting current plan is `0@213456` only if setup is accepted complete; until that final check, use `@0213456`.

## Revised research programme codes

The current programme is two coequal starting streams, followed by mathematics/category theory, then natural cross-disciplinary extensions emerging from the reviewed material. Computer science is an explicit example of a cross-disciplinary connection, not a separate modelling programme.

| Glyph | Code point | Canonical meaning | Class | Scope |
|---|---|---|---|---|
| b | U+0062 | Biological applications | Tock component | Organismal biology, physiology, evolution, biological organization |
| h | U+0068 | Historical and cultural lineage | Tock component | Victorian higher-dimensional thought, spiritualism, psychical research, science fiction, fandom, time-binding |
| m | U+006D | Mathematics, category theory, geometric atlas | Tock component | Higher category theory, geometry, topology, homotopy and related mathematical structures |
| x | U+0078 | Cross-disciplinary connections | Tock component | Natural extensions arising from the literature under review, including computer science, computation where relevant, physics, cognition, information, and other sciences. This is exploratory, not a predetermined closed list. |

The programme order is **b and h coequal → m → x**. The two opening streams may be interwoven or investigated in parallel; neither is subordinate to the other. Mathematics/category theory follows those initial explorations. Cross-disciplinary investigation follows from connections actually encountered; do not prepopulate a rigid list of disciplines.

Retired from the active plan (but not deleted from history): `p` as a separate Computation/Modelling programme, `s` as a separately predetermined Science Bridges programme, and `w` as a scheduled final Workshop Systems phase. Workshop evaluation/adaptation remains an ongoing maintenance activity rather than a final research stage. Existing glyph definitions are retained in the ledger's history; do not silently reuse those glyphs for different meanings.


## Unity / intersection operator

| Glyph | Code point | Canonical meaning | Class | Scope / constraints |
|---|---|---|---|---|
| ∩ | U+2229 | Unity / intersection | Structural operator | Combines coequal, mutually intersecting or jointly constituted workstreams into one integrated inquiry. It does not denote independent parallel branches. Use within `u{...}` to mark a shared/intersectional starting set or work package. |

Distinction: `⑂` (fork) creates separately tracked branches; `∩` expresses coequal integration/intersection. The user’s intended `u` in earlier examples is a mnemonic for unity/intersection, but the actual Unicode operator is `∩`. Do not use the ASCII letter `u` as the operator when `∩` is intended.


## Refined sequence and review-point codes

| Glyph | Code point | Canonical meaning | Class | Scope |
|---|---|---|---|---|
| ⊕ | U+2295 | Integrated / coequal synthesis | Structural operator | Marks the integrated biology-history inquiry and any coequal synthesis; distinct from set intersection where literal set membership is not meant. |
| ρ | U+03C1 | Reorient and review | Phase | Review lessons from the preceding Tock, revise the next workflow if warranted, then establish the next direction. |
| k | U+006B | Category-theory reading programme | Component | Larger literature programme on category theory, higher categories, geometry and related foundations. |

The initial literature sequence is now:
1. Integrated coequal biology + history/cultural lineage, with deliberate attention to nineteenth-century and related historical treatments of biology, including material that may be retrospectively interpretable as biological or proto-biological.
2. Reorientation/review point: assess what the first integrated reading taught us, then decide whether and how to modify the next workflow.
3. Larger category-theory-related literature programme.

The review point is a genuine planned operation, not a placeholder. It may leave the following workflow unchanged if no revision is warranted.


## Current complete intended workflow

The user's currently intended full sequence is exactly:

`⌖◉▣✓@⊕{bh}ρk⊕{mx}`

Do not truncate this to the currently active first stage when reporting the overall plan.

Interpretation:
- `⌖◉▣✓`: completed setup/initial-ledger establishment and verification.
- `@`: current position, immediately before the first uncompleted operation.
- `⊕{bh}`: integrated, coequal biology and historical/cultural reading. Give particular attention to nineteenth-century and adjacent-era historical treatments of biology, including works that may be interpreted as biological even if not framed in modern biological terms. Keep authorial claims distinct from retrospective interpretation.
- `ρ`: reorientation checkpoint after that integrated reading. Review what was learned and decide whether to adjust the following workflow. The checkpoint is required; changes to the plan are optional.
- `k`: larger category-theory-related literature programme.
- `⊕{mx}`: subsequent integrated mathematics/category-theory/geometric work together with cross-disciplinary connections that arise naturally from the reviewed material. Computer science is one candidate connection; do not restrict this to computer science or predefine a closed list.

Important: the signature records the entire intended workflow, not just the active portion. The position marker indicates where execution currently stands. As the work advances, move `@` without deleting future stages. Revise the full signature only when the user changes the plan or the reorientation checkpoint yields an explicitly adopted change.
