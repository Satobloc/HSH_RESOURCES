# PRIOR_ART and Related-Theory Comparison Protocol

Purpose: determine what external frameworks actually anticipate, parallel, constrain, or merely resemble SAT/H(s)H — claim by claim and construction by construction.

This is a triage and evidence protocol, not a novelty-awarding algorithm.

## 1. Use the right unit of comparison

Do not score generic ingredients as priority-relevant by themselves. Examples of weak overlap include:

- worldlines/worldtubes;
- braid groups;
- topology;
- holonomy;
- chirality;
- geometric phase;
- emergent geometry;
- extended objects;
- torsion;
- projection.

The interesting unit is a **compound construction**: which objects are combined, what dependency structure connects them, what the construction does, and what follows from it.

A useful comparison record therefore asks separately:

1. What are the primitives?
2. What geometric/topological relations are imposed?
3. What dynamics or variational rule is used?
4. What quantities are derived rather than assumed?
5. What physical/mathematical role is assigned to the construction?
6. What predictions/constraints/results follow?
7. By what date was this compound publicly formulated?

## 2. Evidence layers

For each external candidate, record similarity at distinct layers rather than one overall “looks similar” score:

| Layer | Question |
|---|---|
| vocabulary | Are the same words used? |
| object | Are the same mathematical objects present? |
| construction | Are the objects assembled in the same way? |
| kinematics | Do the same geometric operations/constraints occur? |
| dynamics | Is the evolution/action/selection rule substantially similar? |
| derivation | Are comparable quantities produced by comparable dependency chains? |
| interpretation | Are the structures assigned comparable roles? |
| result | Are the same nontrivial consequences obtained? |
| chronology | Which dated formulation appears first? |

Similarity at an earlier row does not imply similarity at later rows.

## 3. Disposition vocabulary

Use conservative dispositions:

- **antecedent — generic ingredient**: predates SAT/H(s)H but only at ingredient level;
- **antecedent — partial compound**: predates and contains a significant subset of a compound;
- **substantial antecedent candidate**: predates and appears close enough to require detailed source-to-source comparison;
- **independent rediscovery candidate**: evidence supports an earlier external construction and a later independent SAT/H(s)H formulation;
- **parallel / convergent development**: similar structures develop without an established priority implication;
- **later external parallel**: external formulation follows the dated SAT/H(s)H source;
- **constraint / comparison source**: important scientifically but not a priority analogue;
- **insufficient similarity**: shared vocabulary or ingredient without a comparable compound;
- **unresolved**: full source or chronology still needed.

Do not use “copied,” “influenced,” or similar causal language without separate evidence of access/transmission.

## 4. nLab reconnaissance

Do not begin by scraping every rendered page from `ncatlab.org`.

Preferred source:

- `https://github.com/ncatlab/nlab-content` — file-based Markdown+itex2MML mirror;
- `https://github.com/ncatlab/nlab-content-html` — rendered HTML mirror when useful.

The content mirror gives us a cleaner machine corpus and Git history. Direct nLab page retrieval is a fallback when a needed item is absent or rendered metadata matters.

### nLab ingest plan

Clone/fetch the mirror outside the canonical SAT/H(s)H source tree or into a clearly derived research workspace. Then build:

- page registry: page slug/title/path;
- outbound-link graph;
- reference/bibliography extraction where recoverable;
- page text search index;
- commit/revision chronology for selected pages;
- concept-neighborhood expansion from seed pages.

Do not treat a page's latest content as if all of it existed at the date of the page's first creation. Priority work requires revision/commit inspection for the specific language or construction.

### Seed families

Seed broadly enough to avoid SAT-terminology bias. Initial families should include, among others:

- braid groups, braided categories, braided geometry;
- anyons and modular tensor categories;
- spin networks / spin foams / loop approaches;
- quantum groups and representation-theoretic topology;
- knot/line/defect observables and Wilson lines;
- framed curves, normal bundles, ribbons and tubes;
- holonomy/geometric phase/parallel transport;
- topological defects, flux tubes, strings and string-net-like constructions;
- category/higher-category treatments of geometry and field theory.

These are search neighborhoods, not claims that any family is equivalent to SAT/H(s)H.

## 5. Candidate theory registry

Each theory/framework candidate should receive a stable record containing:

- candidate ID;
- name/family;
- earliest relevant source located;
- source date and revision date;
- DOI/arXiv/URL/bibliographic identity;
- exact source path in HSH_RESOURCES when archived;
- SAT/H(s)H compound(s) compared;
- layer-by-layer similarity notes;
- strongest apparent similarity;
- strongest disanalogy;
- chronology result;
- current disposition;
- confidence/review state;
- follow-up sources needed.

A compact matrix can rank **review priority**, but final dispositions need prose/source evidence.

## 6. Comparison discipline

When a candidate looks unusually close, split the work:

1. external-source reader: reconstruct the external framework without SAT language;
2. SAT/H(s)H source reader: reconstruct the dated SAT compound without importing the external framework;
3. comparator: compare the two reconstructions;
4. chronology check: independently verify dates/versions;
5. adversarial review: look specifically for older antecedents that would defeat a two-party priority comparison.

This prevents resemblance from being manufactured by translating both sources into the same vocabulary too early.

## 7. Outputs

Derived outputs should eventually include:

- `PRIOR_ART_CANDIDATES` registry;
- component/compound comparison matrix;
- nLab concept graph/index;
- source evidence cards;
- deep-review queue;
- chronology ledger;
- final priority-assessment notes that link back to dated SAT/H(s)H provenance.

All outputs remain revisable analytical artifacts. The preserved sources and exact dated formulations control the historical comparison.
