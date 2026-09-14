# Nathan Formal Scientific Transfer — v0.1

**Track:** 1 — Active repo work / nonfiction
**Status:** PROVISIONAL TRANSFER SPECIFICATION
**Authority:** inferential; based on direct Nathan instructions and nonfiction communication structure, **not yet calibrated against Nathan-authored formal scientific papers**
**Purpose:** convert Nathan’s working nonfiction reasoning architecture into formal scientific prose without copying informal surface mannerisms

---

## 1. Core transfer rule

Formalization should be a **surface and organizational transformation, not a conceptual rewrite**.

Preserve:

- scope boundaries
- category distinctions
- epistemic status
- source/provenance hierarchy
- assumptions
- unresolved questions
- exceptions
- supersession/history
- test/failure criteria
- explicit separation between reconstruction and new development

Regularize:

- punctuation
- syntax
- paragraph structure
- terminology introduction
- notation
- citation form
- sectioning
- repetition
- informal self-correction
- platform-specific shorthand

The result should be cleaner than Nathan’s working prose without erasing the logic carried by the roughness.

---

## 2. What should transfer directly into scientific writing

### 2.1 Scope declaration

A paper or section should state what it is and is not claiming before technical momentum begins.

Examples of the underlying move:

- reconstructed historical SAT vs current H(s)H
- kinematic model vs physical claim
- formal analogy vs ontological identity
- sandbox derivation vs promoted result
- current definition vs superseded terminology

**Scientific implementation:** scope paragraph, assumptions subsection, model-domain statement, or explicit caveat tied to the exact claim.

### 2.2 Authority and evidence hierarchy

Where evidence types differ, the hierarchy should be visible.

**Scientific implementation:** distinguish among:

- definitions/axioms
- derived consequences
- numerical assumptions
- empirical inputs
- literature comparisons
- conjectures
- historical source claims
- author interpretation

Do not merge them into one declarative register.

### 2.3 Contrastive definition

Nathan frequently secures a concept by saying what nearby concept it is **not**.

**Scientific implementation:** use concise boundary-setting sentences where confusion is likely.

Example shape:

> Here X denotes ____. It should not be identified with Y; Y enters only as ____.

This is preferable to allowing a familiar standard term to silently import unwanted ontology.

### 2.4 Explicit exception handling

Informal Nathan often embeds exceptions in parentheses or subordinate clauses.

**Scientific implementation:** move significant exceptions into:

- a separate sentence
- a condition attached to an equation
- a lemma/remark
- a limitations paragraph
- a table of regimes

Do not delete them merely to improve flow.

### 2.5 Visible unresolved state

Formal prose should distinguish:

- established within the model
- derived but unchecked
- numerically verified
- empirically constrained
- conjectural
- open
- superseded

This can be encoded by wording, subsection labels, tables, or status notes, but should not depend on reader inference.

### 2.6 Reconstruction history where relevant

If a current object evolved through materially different definitions, and the history matters to provenance or interpretation, preserve that development explicitly.

**Scientific implementation:** current definition in the main line; historical/superseded forms in a provenance note, appendix, or development subsection.

### 2.7 Goalposts and failure conditions

A derivation should say what result would count as success or failure when that is not obvious.

**Scientific implementation:** define observables, consistency conditions, dimensional checks, limiting cases, benchmark comparisons, or falsifying outcomes before interpreting results.

### 2.8 Translation without identity collapse

Nathan often works across representations.

**Scientific implementation:** every map among representations should specify:

- source representation
- target representation
- transformation rule
- preserved quantities/relations
- information lost or added
- whether equivalence is exact, approximate, heuristic, or merely diagrammatic

---

## 3. What should normally NOT transfer literally

Do not automatically import into a paper:

- ellipses as thought pauses
- VTT artifacts
- conversational “I mean…” repairs
- abrupt chat-style pivots
- emojis/status glyphs
- improvised spellings
- audience-address phrases
- mock-dialogue with imagined objections unless rhetorically justified
- casual profanity
- playful names that have not become stable technical terms
- long parenthetical stacks where formal decomposition is clearer

These may reveal the logic of the source, but the scientific version should encode that logic in standard scholarly form.

---

## 4. Informal-to-formal transformation map

### Working correction

Informal:

> No, that’s not quite right. X is doing A here, not B… although in the coarse-grained case you might treat it like B.

Formal:

> X is defined here by A rather than B. A B-like description may be introduced only under the stated coarse-graining approximation.

### Embedded uncertainty

Informal:

> I think this is probably the right way to do it, but I don’t know if the second term survives exactly.

Formal:

> We adopt this construction provisionally. The persistence of the second term has not yet been established and is treated as an open consistency condition.

### Parenthetical exception

Informal:

> We can use this almost everywhere (except at the bifurcation, obviously, where the carrier collapses and the whole parameterization changes).

Formal:

> The parameterization is valid away from the bifurcation. At the bifurcation, the carrier collapses and a separate local treatment is required.

### Historical correction

Informal:

> We used to call this X, but that’s really the old SAT version; in H(s)H it’s Y, except some old docs still use X.

Formal:

> Earlier SAT documents use the term X. In the current H(s)H formulation the corresponding object is Y. Historical quotations retain the original terminology.

---

## 5. Recommended paper architecture pending direct formal samples

This is a provisional architecture derived from Nathan’s communication priorities, not yet a demonstrated personal paper format.

For theory/reconstruction papers:

1. **Abstract** — claim, domain, method, principal result/status; no hype
2. **Plain-English section summary** where useful for archive/reconstruction work
3. **Scope and status** — historical/current; reconstructed/new; physical/non-physical; tentative/approved
4. **Definitions and notation** — boundary-setting definitions first
5. **Source/provenance or assumptions** as appropriate
6. **Formal construction / methods**
7. **Derivations** with stated checks and domains
8. **Consistency / limiting-case tests**
9. **Results**
10. **Comparison / interpretation** with representation boundaries explicit
11. **Limitations and unresolved questions**
12. **Conclusion** restricted to what was actually established
13. **Appendices** for historical variants, long derivations, provenance maps, or alternate representations

This structure should be revised once Nathan supplies genuine formal scientific examples.

---

## 6. Tone target

Pending formal samples, use:

- precise rather than ceremonious
- direct rather than promotional
- confident where derivation warrants it
- explicitly uncertain where it does not
- low on generic throat-clearing
- low on rhetorical hype
- terminology-rich only where each term compresses a stable concept
- willing to state “not established” or “outside scope” plainly

Avoid generic AI-scientific phrases such as:

- “This groundbreaking framework…”
- “It is important to note that…” when no specific importance follows
- “Intriguingly…” as routine decoration
- “These findings may pave the way…” without a concrete mechanism

---

## 7. Citation/provenance transfer

For archive-derived scientific work, citation is not cosmetic.

Preserve distinctions among:

- direct Nathan statement
- assistant reconstruction
- mathematical derivation
- standard external source
- empirical dataset/constant
- historical SAT definition
- current H(s)H definition

When a direct author statement is doing definitional work, quote or cite it closely enough that the reader can audit whether the formal restatement changed meaning.

---

## 8. Calibration firewall

**Do not call this a Nathan scientific-writing style model yet.**

At present it is a **transfer protocol** from known Nathan nonfiction structure into competent formal scientific prose.

A true formal voice model requires direct examples of Nathan-authored scientific papers, reports, formal essays, technical manuscripts, or comparable finished prose.

When such examples arrive, compare them against this transfer specification and classify each rule as:

- confirmed
- modified
- rejected
- register-specific
- still unknown

---

**Version rule:** v0.x remains provisional. Promote to v1.0 only after direct formal-science calibration and explicit Nathan approval.
