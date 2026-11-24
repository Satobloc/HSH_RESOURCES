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


## Full-plan signature grammar and current programme

The complete live plan uses:
`⌖◉▣✓@⊕{bh}⌖◉▣ρk⊕{mx}`

The entire planned sequence remains visible in the repeated signature. `@` marks the current position; it does not remove or hide future stages. `⊕{bh}` means coequal integrated biology/history inquiry. After that, `⌖◉▣` is the explicit reorientation, next-Tock selection and plan-recording sequence; `ρ` is the lessons-learned review/decision; `k` is category-theory reading; `⊕{mx}` is mathematics/category theory integrated with naturally emerging cross-disciplinary connections. Spaces between the two displayed stages are optional readability whitespace only; adjacency otherwise implies succession.


## Orientation assumptions (applies throughout the programme)

The orientation phase `⌖` includes the following standing interpretive assumptions. These are not separate workflow stages or additional glyphs; consult them whenever interpreting later stages:

1. **Dimensional reading:** Interpret the word **“higher” explicitly as “higher-dimensional”** wherever the context concerns dimensionality, spatial thought, geometry, or related mathematical/physical structures. Do not silently reduce “higher” to rank, abstraction, sophistication, or hierarchy. Preserve other meanings where the author clearly intends them, and record ambiguities rather than forcing the dimensional reading.
2. **Cross-disciplinary attention:** Actively look for connections that a source makes explicitly, implies, or supports by a straightforward, clearly explained extension. This includes biology and other sciences, mathematics, physics, computation/computer science, cognition, and any other field naturally indicated by the material. Distinguish explicit claims, implicit implications, and our own extensions.
3. **Biology remains active:** The biological perspective `b` remains in the working mix throughout the entire programme, including historical reading, category-theory reading, and subsequent cross-disciplinary exploration. It is not confined to the opening historical/biological Tock.
4. **Source fidelity:** Do not attribute a modern interpretation to a historical author unless the source supports it. Separate original terminology and claims from retrospective interpretation and contemporary extension.

These assumptions govern orientation at the beginning of each Tock and remain active during investigation, geometrization, connection-building, recording, and verification.


## 4D biology research distinctions (working classification)

| Code | Meaning | Diagnostic distinction |
|---|---|---|
| A | Additional spatial dimension in living matter | A genuinely extra spatial direction or motion affecting organic structure |
| B | Higher-space vital vehicle | A four-dimensional organism/vehicle or life-principle associated with a three-dimensional body |
| C | Effective/fractal internal dimension | Additional effective dimension of biological transport/network organization embedded in ordinary three-dimensional space |
| D | Space-time organism | Organism treated as spatially and temporally extended, with time/lifetime as a fourth dimension |

These letter labels are classification tags for reading notes only; they are not workflow glyphs and must not be inserted into the live signature without a separate assignment. Do not conflate A–D or infer historical influence without evidence.


## SAT/H(s)H interpretive lens and contemporary reconstruction character

| Glyph | Code point | Canonical meaning | Class | Scope |
|---|---|---|---|---|
| S | U+0053 | SAT/H(s)H interpretive lens | Interpretive mode | Read historical dimensional biology through the user's explicitly physical, four-dimensional SAT/H(s)H ontology. Applies to the integrated historical-biological inquiry and later synthesis. |
| β | U+03B2 | Biological modernization / contemporary reconstruction | Research mode | In the latter portion of the reading, deliberately revisit the historical picture using modern biology, genetics, physiology, evolution, developmental biology, neuroscience where relevant, and contemporary physics/mathematics. Reconnaissance and concept-space construction are permitted; full proof or quantitative validation is not a prerequisite at this stage. |

### SAT/H(s)H lens: reading rule

The SAT/H(s)H lens is not a generic appeal to “some higher-dimensional component.” When interpreting the relevant historical material, treat the working premise as literal physical extension in a four-dimensional ambient reality:

- Matter and organisms are physically extended structures in the four-dimensional universe, not merely three-dimensional objects supplemented by metaphorical or abstract temporal descriptions.
- The familiar three-dimensional “now” is a section/intersection/readout of that extended structure. It exposes only the portion intersected by the present time surface; it is not the whole object.
- The Minkowski/worldtube picture is to be read ontologically for purposes of this exploratory lens, not merely as a convenient diagram or bookkeeping device.
- Organisms may therefore be considered as physically extended four-dimensional structures with three-dimensional sections, and their persistence, development, reproduction, morphology, and biological relations can be examined as properties of those extended structures.
- Do not soften this premise into phrases such as “may have a four-dimensional component” or “in some higher-dimensional space.” State the physical extension directly when presenting the SAT/H(s)H interpretation.
- Keep the distinction between the historical author's actual claim and our interpretive reconstruction explicit. In particular, describe Hinton as an approximate precursor or nearby conceptual picture only to the extent supported by his text; do not claim that he possessed the later SAT ontology or its complete physical account.
- This interpretive premise is a declared working ontology of this workshop, not a claim that contemporary physics has independently established SAT/H(s)H.

### Two-pass reading within the integrated biology-history Tock

1. **Historical/source pass:** recover what the author said, what the author implied, and what can reasonably be inferred in context. Preserve terminology, qualifications, doubts, and historical setting.
2. **SAT/H(s)H interpretation pass:** ask how the source's organism, life process, symmetry, development, identity, or morphology would be represented if treated as a physically extended four-dimensional structure whose 3D present sections are intersections with a time surface.

### β phase: latter-half modernization

The latter portion of the reading adds a deliberate contemporary reconstruction pass. Use modern biology, genetics, physiology, evolution, developmental biology, morphology, physics, mathematics, and other relevant disciplines to update and expand the Hinton/SAT picture. This is reconnaissance and concept-space construction: develop plausible correspondences, candidate mechanisms, diagrams, analogies with explicit type labels, questions, and research avenues. Do not stall the exercise by requiring every proposed connection to be proven to publication-grade scientific rigor before it can be explored.

Maintain clear labels:
- **Historical claim:** directly present in the source.
- **Historical implication:** follows reasonably from the source's own argument, even if not stated in modern language.
- **SAT/H(s)H reinterpretation:** the source re-read through the workshop's literal four-dimensional ontology.
- **Modern biological correspondence:** a connection to established contemporary biology or physics, accurately characterized.
- **Reconnaissance conjecture:** a tentative proposed bridge or mechanism to explore, not yet demonstrated.

The β operation is exploratory, not a theory-validation or theory-promotion gate. Preserve scientific distinctions and mark uncertainty, but do not let proof obligations prematurely constrict the concept-space survey.
