# H(s)H Toolkit Digestion Plan

`H(s)H_Toolkit/` is an active theorybuilding library, not merely another bibliography folder. The goal is to make mathematical machinery retrievable by **what problem it solves** while preserving the exact literature source.

## Source vs derived organization

Do not reorganize the source directory merely to fit a new taxonomy. Build a derived toolkit index/cards that may classify one source under several functions.

A paper on framed curves, for example, may be useful simultaneously for normal-bundle geometry, torsion, holonomy, elastic-rod mechanics, and boundary modes.

## Functional families

Initial retrieval families:

- differential and Lorentzian geometry;
- curves, framed curves, ribbons, rods, elastica, worldlines and worldtubes;
- topology, knots, braids and anyons;
- category theory, higher categories, representation theory and quantum groups;
- gauge theory, connections, holonomy and geometric phase;
- QFT and particle physics, including QCD/confinement;
- Clifford algebras, spinors and Dirac machinery;
- causal structure, foliations and signature change;
- dynamical systems, bifurcation, waves, defects and solitons;
- continuum mechanics, elasticity and effective media;
- statistical / condensed-matter analogues where structurally useful;
- numerical / formal methods.

These are retrieval labels, not claims that a source endorses H(s)H.

## Toolkit card

High-value sources should receive a compact structured card with:

- stable source ID/path/hash;
- citation;
- functional tags;
- standard mathematical object/result;
- prerequisites/assumptions;
- key definitions;
- useful equations or construction steps with page/section anchors;
- what type of problem the machinery solves;
- possible H(s)H use;
- limitations / mismatches;
- import status: standard machinery, analogy, constraint, comparison, or deliberate adaptation;
- review depth and continuation cursor.

The `possible H(s)H use` field is an analytical note. It must not be presented as something asserted by the source.

## Digestion levels

Use explicit coverage levels:

- `CATALOGED` — bibliographic identity/path only;
- `TRIAGED` — abstract/contents/first-pass relevance assessed;
- `PARTIAL` — useful sections/pages read and anchored;
- `FULL` — source read at the level needed for its toolkit role;
- `CARD` — structured toolkit card completed;
- `TESTED` — machinery actually exercised in a derivation/model or computational prototype.

This prevents a filename or machine tag from masquerading as source comprehension.

## Retrieval questions the toolkit should support

Examples:

- “What formalism handles rotation of a normal frame along a curve?”
- “What are standard ways for torsion to induce a geometric phase?”
- “What machinery represents braided multi-object states?”
- “What mathematical conditions cause a carrier/intersection manifold to change dimension?”
- “How do finite-radius tubes around curves behave under deformation?”
- “What standard confinement/flux-tube results constrain an H(s)H analogy?”

The answer should return a small set of source-backed tools with page anchors, not a list of hundreds of PDFs.

## Build sequence

1. Filter the existing HSH_RESOURCES bibliographic/index records to `H(s)H_Toolkit/`.
2. Merge duplicates by content identity without deleting source placements.
3. Apply broad functional tags using title/abstract/extracted text.
4. Generate bounded candidate lists by functional family.
5. Deep-read the highest-leverage sources and create cards.
6. Link cards to active HsH derivations/conversations where machinery is actually used.
7. Feed standard-background citation needs into the citation ledger.

## Theorybuilding discipline

The toolkit is most useful when it preserves the distinction:

**standard result from literature → deliberate imported tool → H(s)H-specific construction using that tool**

That chain should be visible whenever possible. It protects both the mathematical work and the later citation/priority audit.
