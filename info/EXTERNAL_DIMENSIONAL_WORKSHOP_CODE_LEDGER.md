# External Dimensional Workshop — Unicode Code Ledger

**Status:** Bespoke experimental pilot. Local meanings only; no general recommendation implied.  
**Version:** 0.2  
**Updated:** 2026-11-24

## Grammar

Single Unicode code points represent phases, operators, components, or states. Adjacent tokens imply left-to-right succession. Structural operators preserve their defined semantics. The live signature carries codes; this ledger carries meanings. Memorization is unnecessary.

For live integrated-work signatures, square brackets group the subject components and their selected interpretive/method companions. Use the order **subject components → interpretive lens → method-source**. For example, `⊕[bhᛟd]` means integrated biology/history work read through the SAT/H(s)H lens and informed by the Dimensional Normalization paper. The bracket group is a compact scope bundle, not a new branch or operator.

For branches, `⑂{cu}` is equivalent to `⑂{A: Credenza | B: Unicode notation}` when component codes are defined and left-to-right order is sufficient. Where additional ordering labels are needed, uppercase labels indicate branch/order positions and lowercase tokens identify components: `⑂{AcBu}`.

No undefined placeholders. A code may refer to a real, identifiable, populated, extensible collection.

## Phase codes

| Glyph | Code point | Canonical meaning | Class | Scope / constraints |
|---|---|---|---|---|
| ⌖ | U+2316 | Orient | Phase | Recover context and exact Tock/Tick position; consult the workshop ledger, protocol and code ledger; choose the authorized archive-search route before substantive archive retrieval |
| ◉ | U+25C9 | Focus / select Tock | Phase | Select and bound the substantial work unit |
| ⌕ | U+2315 | Investigate | Phase | Locate and examine sources or concepts |
| ⧖ | U+2996 | Geometrize | Phase | Construct the geometric/dimensional account |
| ⤳ | U+2933 | Connect | Phase | Follow relevant connections |
| ▣ | U+25A3 | Record | Phase | Preserve durable result |
| ✓ | U+2713 | Verify | Phase | Verify claims, original-source locators, archive query/scope/engine, repository commits and exclusions, run manifest/receipt, coverage limits, result and durable storage/readback |
| ⇢ | U+21E2 | Deliberate transition / next | Operator | Explicit decision/transition point; not ordinary succession |

### Archive retrieval and verification under ⌖ / ✓

- **Mysearch is the first-choice direct-Nathan archive-search route when operational and validated.** Its current repository status record still says `SCAFFOLD ONLY / NOT VALIDATED / NOT YET A PRODUCTION SEARCH SERVICE`; do not report a Mysearch execution or rely on it as an available production route until that status changes and the route is actually accessible.
- **Until Mysearch is operational, use Mersearch as the active archive-search standard**, pinned to stable Mersearch 1.0. Follow `Satobloc/HsH/WORKSPACES/COMMON/MERSEARCH_WORKER_START_HERE.md`; search all three permitted repositories together by default: `Satobloc/SAT_THEORY_ARCHIVE_2023-25`, `Satobloc/HsH`, and `Satobloc/HSH_RESOURCES`. Preserve the distinct source status of HSH_RESOURCES as internal reference/toolkit material, not theory authority.
- Prefer the local pinned searcher for full, inspectable result sets. The GitHub Actions bridge's post-containment compact receipts are not exhaustive full-hit inventories. Never claim exhaustiveness from a compact receipt; report the searched roots, refs/SHAs, engine, query, exclusions, counts, receipt state and limitations.
- Use GitHub code search only as a documented fallback when Mysearch/Mersearch cannot actually be used. Label it as fallback search, not a Mysearch or Mersearch result, and disclose scope/coverage limitations. Do not silently substitute it.
- A search hit is not a source read. `✓` requires opening and inspecting the original matched source (or recording why it cannot be inspected), preserving exact locators and distinguishing searched, located, metadata-inventoried, read, and verified states.

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
| h | U+0068 | History and cultural lineage | Component | Nineteenth-century and early-twentieth-century dimensional thought, Victorian intellectual context, spiritualism, psychical research, science fiction, fandom and documented cultural reception |
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

`⌖◉▣✓@⊕[bhᛟd]β ⌖◉▣ρk⊕[mbxᛟd]`

Do not truncate this to the currently active first stage when reporting the overall plan.

Interpretation:
- `⌖◉▣✓`: completed setup/initial-ledger establishment and verification.
- `@`: current position, immediately before the first uncompleted operation.
- `⊕[bhᛟd]β`: integrated, coequal biology and historical/cultural reading, with the SAT/H(s)H interpretive lens and Dimensional Normalization method companion; β marks the latter-half contemporary biological reconstruction pass. Give particular attention to nineteenth-century and early-twentieth-century historical treatments of biology. Keep authorial claims distinct from retrospective interpretation.
- `ρ`: reorientation checkpoint after that integrated reading. Review what was learned and decide whether to adjust the following workflow. The checkpoint is required; changes to the plan are optional.
- `k`: larger category-theory-related literature programme.
- `⊕[mbxᛟd]`: subsequent integrated mathematics/category-theory/geometric work, with biology kept active and cross-disciplinary connections arising naturally from the reviewed material, using the SAT/H(s)H lens and Dimensional Normalization method companion. Computer science is one candidate connection; do not restrict this to computer science or predefine a closed list.

Important: the signature records the entire intended workflow, not just the active portion. The position marker indicates where execution currently stands. As the work advances, move `@` without deleting future stages. Revise the full signature only when the user changes the plan or the reorientation checkpoint yields an explicitly adopted change.


## Full-plan signature grammar and current programme

The complete live plan uses:
`⌖◉▣✓@⊕[bhᛟd]β ⌖◉▣ρk⊕[mbxᛟd]`

The entire planned sequence remains visible in the repeated signature. `@` marks the current position; it does not remove or hide future stages. `⊕[bhᛟd]` means coequal integrated biology/history inquiry, read through the SAT/H(s)H lens `ᛟ` and using the Dimensional Normalization paper `d` as a companion methodological reference. `β` marks the latter-half contemporary biological reconstruction pass. After that, `⌖◉▣` is the explicit reorientation, next-Tock selection and plan-recording sequence; `ρ` is the lessons-learned review/decision; `k` is category-theory reading; `⊕[mbxᛟd]` is mathematics/category theory integrated with the continuing biological perspective and naturally emerging cross-disciplinary connections, also read through `ᛟ` and informed by `d`. Spaces between the two displayed stages are readability whitespace only; adjacency otherwise implies succession.


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
| ᛟ | U+16DF | SAT/H(s)H interpretive lens | Interpretive mode | Read the relevant historical, biological, mathematical and cross-disciplinary material through the user's stipulated physical four-dimensional SAT/H(s)H ontology, while keeping source claims distinct from our reinterpretation. |
| β | U+03B2 | Biological modernization / contemporary reconstruction | Research mode | In the latter portion of the integrated biology-history reading, revisit the historical picture using modern biology, genetics, physiology, evolution, developmental biology, neuroscience where relevant, and contemporary physics/mathematics. Reconnaissance and concept-space construction are permitted; full proof or quantitative validation is not a prerequisite at this stage. |
| d | U+0064 | Dimensional Normalization paper | Method-source component | Companion methodological source: Nathan McKnight & Janus C. Sol, “Metric Symmetry to Reveal the Grain” (2026-09-09 draft), archived as `DIMENSIONAL_NORMALIZATION.pdf`, `.tex`, and `_AUTO_EXTRACTED_TEXT/DIMENSIONAL_NORMALIZATION.txt` in `Satobloc/SAT_THEORY_ARCHIVE_2023-25`. Use its frozen normalization/residual-audit method where equations or formal models make it useful; it is not a historical biological source or an ontological authority. |

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


## Interpretive and modernization codes

| Glyph | Code point | Canonical meaning | Class | Scope |
|---|---|---|---|---|
| S | U+0053 | SAT/H(s)H interpretive lens | Interpretive mode | Read historical dimensional biology through the workshop's literal physical 4D ontology: matter and organisms are extended in 4D; the familiar 3D present is their section/intersection with the time surface. |
| β | U+03B2 | Contemporary biological reconstruction | Research mode | Latter-half reconnaissance pass updating the historical/Hinton picture with modern biology, genetics, physiology, evolution, developmental biology, physics, mathematics and other relevant disciplines. Exploratory, not a proof or validation gate. |

### ᛟ — SAT/H(s)H lens

Do not dilute this lens into “may have a four-dimensional component” or “in some higher-dimensional space.” The working premise is literal physical extension of matter and organisms in a four-dimensional ambient universe. The ordinary three-dimensional “now” is a section/intersection/readout of that extended structure at the time surface; it reveals only the portion intersected at that moment, not the whole object. Read the Minkowski/worldtube representation ontologically for this exploratory reconstruction, not merely as diagrammatic bookkeeping.

Historical source fidelity still applies. First record what Hinton or another author explicitly claims, implies, and leaves unresolved. Then state the SAT/H(s)H reinterpretation as our extension. Do not attribute the developed SAT ontology to Hinton. “Approximate precursor” or “nearby conceptual picture” is permissible only with a clear account of the resemblance and the difference. This is a workshop working ontology, not a claim that contemporary physics has independently established SAT/H(s)H.

### β — modernization pass

β marks the latter-half operation of revisiting and tentatively updating the historical/Hinton picture using contemporary science. Its purpose is broad reconnaissance and concept-space construction. Candidate correspondences, conceptual maps, proposed mechanisms and research questions may be developed without first proving every detail to publication-grade rigor. Accuracy and uncertainty labels remain necessary; premature proof demands must not prevent exploratory mapping.

Use these provenance labels in reading notes:
- **Historical claim**
- **Historical implication**
- **SAT/H(s)H reinterpretation**
- **Modern biological/physical correspondence**
- **Reconnaissance conjecture**

β is not an empirical-validation gate or theory-promotion operation.


## Lowercase designation convention

**Adopted 2026-11-24.** Use lowercase letters for all newly assigned workshop component, lens, mode, and collection designations. Reserve uppercase letters for possible future organizational labels, ordering systems, hierarchy markers, or branch-position labels. The user's joke “higher capitalization” is a mnemonic for keeping uppercase available for higher-level organization.

- Existing lowercase codes retain their meanings.
- The earlier uppercase `S` designation for the SAT/H(s)H lens is superseded by `ᛟ` (U+16DF), the user's selected replacement.
- The legacy lowercase `s` remains the retired Science Bridges component label from the earlier programme design; it is **not** reused for the SAT/H(s)H lens.
- The lowercase Greek beta (β) remains the contemporary biological modernization-pass character.
- Do not use `S` or `s` as the current SAT/H(s)H lens code. Preserve their historical assignments/supersession rather than silently reassigning them.
- Uppercase labels may be introduced later when a real ordering or organizational need arises; do not prepopulate hypothetical labels in the live signature.

## Victorian-first historical scope and later-lineage filter

The historical reading emphasis is Victorian material and its immediate intellectual environment. Later works may enter the historical lineage only when there is a clear basis for interpreting them as a natural extension, reception, transformation, or continuation of the Victorian material. Do not let the historical inquiry drift into a general survey of every later use of “fourth dimension.”

Modern scientific material may still be brought in during the separate β modernization/reconstruction pass. Distinguish this contemporary scientific update from historical lineage.

## Parked contemporary comparison: fractal dimensionality

West–Brown–Enquist's “The Fourth Dimension of Life” and related fractal/network-dimension approaches are **not** to be treated as already expressing the workshop's literal four-dimensional ontology. Their “fourth dimension” refers to an effective/fractal dimension of transport/network organization within ordinary three-dimensional organisms, not straightforwardly to physical extension along the workshop's fourth, orthogonal w direction.

Keep this material parked as a possible later reinterpretation, not a core historical source and not an equivalent 4D ontology. The open conjectural question is whether fractal biological organization could be re-read in relation to literal four-dimensional processes, or to an interdimensional connection in the precise physical sense below.

## Literal “rounding the corner of time” / orthogonal-w connection

The user proposes exploring whether some biological or physical processes can “round the corner of time”: a process whose structural or informational relationships are not exhausted by progression along the familiar time direction, but involve the orthogonal w direction in the four-dimensional structure. The phrase “interdimensional connection” is intended literally, not as spiritualist or metaphorical language.

Treat this as a reconnaissance conjecture. Potential questions include:
- What is the precise geometric meaning of “rounding the corner of time” in the current SAT/H(s)H coordinate conventions?
- How could a process carry structural or informational relationships into or along orthogonal w?
- What would count as a physical connection rather than a metaphor, coordinate relabeling, projection artifact, or ordinary causal propagation?
- Could fractal biological organization, recursive structure, or scale-spanning transport networks provide useful modern comparison points without conflating effective fractal dimension with a literal ambient dimension?
- What observable or conceptual distinctions would separate an ordinary worldtube/time-surface interaction from a genuinely orthogonal-w connection?

Keep the current SAT/H(s)H coordinate and metric conventions explicit. The archive contains differing historical conventions, including Minkowski-style language and later ++++ / cw=t / w-as-fourth-spatial-dimension descriptions; do not silently merge these. “Orthogonal w” is a working geometric description whose type and metric must be checked against the particular source/version under discussion.

This idea belongs in the exploratory concept-space. It does not establish nonlocal influence, retrocausation, information transfer, or a physical mechanism. Do not dismiss it merely because the phrase has rhetorical baggage; interpret the user's intended geometry literally and formulate the question carefully.


## Time is the W axis; no separate bridge

**Adopted 2026-11-24 from direct user clarification.** In the user's current SAT/H(s)H interpretation, time is the traditional Minkowski W axis, orthogonal to X, Y, and Z. The W axis is also, distinctly, the direction of motion/propagation of the time action. Preserve both aspects without splitting them into an axis plus a separate temporal process.

The user's relational formulation is deliberately symmetric: X is to Y as Y is to Z, X is to Z, and each spatial axis is related to W in the same general dimensional sense. Do not treat W as an alien region, separate domain, or extra destination that ordinary time must somehow reach.

Consequences for this workshop's language:
- If a process happens in time, its physical four-dimensional structure is extended along W. That is the ordinary implication of taking time as the W axis.
- Do not describe time as a bridge between 3D and some separate fourth-dimensional place. Time itself is the W direction / propagation direction; **there is no additional bridge**.
- Do not suggest that a process needs a special interdimensional crossing merely because it has temporal extension. Its extension along W is already part of what it means for it to happen in time.
- Reserve “rounding the corner of time” or “orthogonal-w connection” for a more specific conjecture only if a distinction beyond ordinary extension along W is actually intended and defined. Do not use those phrases to reintroduce a false separation between time and W.
- Distinguish the coordinate axis/dimensional direction W from the direction of propagation of the time action as conceptual aspects that are related but not interchangeable in every sentence. Do not collapse this distinction, but do not detach them into independent entities either.
- The familiar three-dimensional “now” is an intersection/section of physically extended four-dimensional structure; it is not an object that must be connected to a separate temporal realm.

This clarification governs all subsequent SAT/H(s)H reinterpretation, including the reading of Hinton. It supersedes any earlier workshop wording that implied a temporal bridge, a separate temporal region, or a necessary transition from ordinary time into W.


## Corrected temporal ontology: W is time; no separate bridge

**Adopted 2026-11-24 from direct user clarification.** In the current SAT/H(s)H interpretation, time is the traditional Minkowski W axis, orthogonal to X, Y, and Z. W is also, distinctly, the direction of motion/propagation of the time action. Preserve both aspects without splitting them into an axis plus an independent temporal process.

The dimensional relation is symmetric: X is to Y as Y is to Z, X is to Z, and each spatial axis is related to W in the same general dimensional sense. Do not treat W as an alien region, separate realm, or destination that ordinary time must bridge into.

Consequences:
- If a process happens in time, its physical four-dimensional structure is extended along W. This is the ordinary implication of taking time as the W axis.
- There is no additional bridge between 3D structure and W. Time itself is the W direction and direction of temporal propagation.
- Do not describe ordinary temporal extension as a special interdimensional crossing.
- Reserve “rounding the corner of time” or “orthogonal-w connection” for a more specific conjecture only if a distinction beyond ordinary extension along W is actually intended and defined.
- Distinguish the coordinate axis/dimensional direction W from the direction of propagation of the time action as conceptual aspects that are related but not interchangeable in every sentence. Do not collapse them, but do not detach them into independent entities either.
- The familiar 3D present is an intersection/section of physically extended 4D structure, not an object that must be connected to a separate temporal realm.

This clarification governs all subsequent SAT/H(s)H interpretation, including Hinton. It supersedes earlier wording that implied a temporal bridge, separate temporal region, or necessary transition into W.

### w=ct and equal status of dimensions

The user's current statement is that w=ct everywhere and at all times and places, with time measured in meters. Unless a source or argument justifies a difference, X, Y, Z, and W are unified coordinate axes of the same space and should be treated alike dimensionally. The directly observed distinguishing feature is that W carries an obligatory motion/expansion vector, or possibly a rotation vector. Do not silently decide between motion/expansion and rotation; retain the alternative as unresolved.

The user further proposes that universal scientific invariants and laws, including Newton's laws, are universal throughout the block-universe model. Time/W is involved in exerting or transmitting force in the ordinary way along W, while apparent differences arise from the obligate vector attached to W. Treat this as the current interpretive proposal to explore, not as a completed derivation. Do not reintroduce a time/space ontological split merely because conventional notation or interpretation does so. Preserve the user's W-metric and unit convention when reconstructing this view; check signature/metric details against the particular SAT/H(s)H version rather than assume the conventional Lorentzian metric has already been adopted.


## Foundational SAT/H(s)H axiom status: W/time and four-dimensional physical extension

**Epistemic status: FOUNDATIONAL WORKSHOP ASSUMPTION, not an open question or optional hypothesis.** The following is the user's stipulated ontology for this workshop and governs all interpretation unless the user explicitly revises it. Do not recast it as a question, conjecture, candidate model, or item awaiting validation.

1. **Four-dimensional physical space:** X, Y, Z, and W are the unified axes of the physical space. Unless a specific reason is supplied, they are dimensionally alike and stand in symmetric dimensional relations.
2. **Time is W:** W is the traditional Minkowski time axis, orthogonal to X, Y, and Z. Time is measured in meters under the convention w=ct. There is no ontological separation between time and place.
3. **Temporal propagation:** W is also, distinctly, the direction of motion/propagation of the time action. The coordinate direction and the propagation direction are conceptually distinguishable aspects of the same foundational arrangement, not separate entities.
4. **Obligate W-vector:** The directly observed distinction associated with W is its obligatory motion/expansion vector, with rotation retained as an alternative characterization. This vector accounts for the apparent distinctions associated with W; do not treat it as evidence that W is a different kind of dimension.
5. **No bridge:** Time itself is W. There is no separate temporal region, process, destination, or bridge between ordinary space and W. Any process that happens in time is physically extended along W. Its extension along W is already intrinsic to its temporal existence.
6. **Block-universe scope:** Universal scientific invariants and laws, including Newton's laws, are taken to be universal throughout the block-universe model. Time/W participates in exerting or transmitting force in the ordinary way along W; apparent differences arise from the obligatory vector associated with W.
7. **Present section:** The familiar three-dimensional present is an intersection/section of physically extended four-dimensional structures. It is not the complete structure and does not need to connect to a separate temporal domain.

### Consequence for interpretation and language

- State these as premises, not questions. They are not awaiting a decision about whether time might be W, whether processes might extend along W, or whether a bridge is needed.
- Do not phrase ordinary temporal extension as an “interdimensional crossing,” “rounding the corner into W,” or a process that must somehow enter a fourth-dimensional region. Such language contradicts the axiom.
- A phrase like “rounding the corner of time” may only be used for a genuinely additional, specifically defined geometric phenomenon beyond the ordinary W-extension already implied by temporal existence. It must not be used to redescribe time itself as a bridge.
- Do not introduce caveats that downgrade the ontology to “working hypothesis,” “proposed interpretation,” “possible mechanism,” or “unproven premise.” The ontology is foundational by user stipulation. Scientific or mathematical questions may concern its consequences, formal expression, compatibility, or explanatory reach, but not whether the workshop should assume it.
- Keep mathematical discipline about coordinate conventions and equations, but do not let unresolved formal details unsettle the stipulated ontology.
- Historical authors such as Hinton are interpreted from this foundation while maintaining source fidelity: distinguish their original claims from our SAT/H(s)H reading. Do not attribute the complete ontology to them.
- Modern biology and physics are brought into the reconnaissance to elaborate and update the consequences of the ontology, not to decide whether the ontology is allowed as the workshop's starting premise.

This section supersedes any contrary phrasing elsewhere in the workshop records, especially language that describes the W-axis ontology as a conjecture, asks whether ordinary temporal extension involves W, or treats W as a separate dimension requiring a bridge.


## Universal coordinate conversion identities

**Foundational convention, confirmed 2026-11-24:** the coordinate relations are universal across all systems:

\[
c = wt, \qquad ct = w, \qquad cw = t.
\]

These are to be preserved as the user's stipulated conversion identities in every coordinate system / reference system under consideration. Do not silently replace them with a convention that applies only in a selected frame, region, epoch, or subsystem. Do not “correct” or normalize the identities into a different expression; retain the exact three relations as stated.

They are part of the foundational SAT/H(s)H coordinate ontology and are not posed as questions or optional hypotheses. Any later formal reconstruction must carry these identities explicitly and examine their mathematical consequences without weakening their stipulated universality.


## Foundational scalar relation: c = wt

**Adopted 2026-11-24 as a foundational SAT/H(s)H relation, applying in all systems.** The governing relation is:

```
c = wt
w = c/t
t = c/w
```

These are the same relation expressed in three algebraically equivalent forms. Preserve the symbols and ordering exactly. This clarification **supersedes the earlier workshop statement w=ct**; do not retain w=ct as a simultaneous axiom or silently substitute it when restating the relation.

Treat this as foundational, not as a question or conjecture. Any subsequent formalization must use this relation as given and examine its consequences consistently. Do not infer additional unit assignments or reinterpret the symbols beyond the user's definitions without an explicit source or clarification. Where dimensional analysis is performed, state the assumed meanings and units of c, w, and t explicitly and check them against this governing relation.

This relation applies in all systems. Do not restrict it to a particular coordinate frame, local region, or special physical regime.


## Correction: restore standard c, t, w relation

**Correction dated 2026-11-24.** The immediately preceding entry `c = wt` was written after the user said they meant the standard physics use, then recognized they may have misstated it. It is superseded and must not be treated as a foundational SAT/H(s)H relation.

The standard relation for light-travel distance is:

```
w = c t
t = w / c
c = w / t
```

Here:
- `c` is the speed of light (distance per unit time),
- `t` is elapsed time,
- `w` is the corresponding light-travel distance / time-coordinate length.

In relativity it is common to define a length-valued time coordinate, often written `ct` (or `T=ct`), so time is represented in distance units. This does not mean ordinary SI time itself has changed units; it means the coordinate `ct` has units of length. With units where c=1, the numerical value of the conversion factor is absorbed into the unit convention.

The earlier formula `c = wt` is dimensionally inconsistent under the standard meanings of c (L/T), w (L), and t (T); it would have units L·T, not L/T. Do not use its rearrangements `w=c/t` or `t=c/w`.

**Important notation caution:** if the workshop's W coordinate is the Minkowski time coordinate expressed as a length, write `W=ct` or explicitly define `W\equiv ct`. Avoid switching between lowercase `w` and uppercase `W` without defining whether one is a scalar coordinate value and the other an axis label. The user's broader SAT/H(s)H ontology that W is the time axis remains foundational; this correction only restores the standard dimensional relation used to express that time coordinate in length units.
