# Longitudinal arXiv Topic Atlas

## Purpose

Build a neutral, SAT-independent map of how arXiv physics changes over time so later SAT/H(s)H comparisons have a longitudinal control rather than a single contemporary baseline.

This project does **not** decide what SAT is, what counts as an SAT move, or whether any external work is related to SAT. It records the changing external literature landscape.

## Core questions

1. Which arXiv subject categories exist in each period, and when do categories first appear, split, merge, alias, or substantially change scope?
2. How does the relative volume of broad physics areas and subfields change by year and decade?
3. Which themes, methods, explanatory styles, and foundational questions rise, fall, disappear, or reappear?
4. For any later comparison concept, what is the earliest located appearance in the sampled/harvested mainstream corpus, and is it plausibly a genuinely new appearance or a modern reappearance of an older literature?
5. Which apparent trends are artifacts of arXiv taxonomy changes rather than changes in physics itself?

## Evidence layers

### Layer A — official arXiv taxonomy/history

Track current and historical subject labels using official arXiv documentation, annual reports, roadmaps, and metadata. Record category creation, aliasing, merging, renaming, and scope changes where documentary evidence exists.

### Layer B — category prevalence

For each year, count or estimate:

- primary-category submissions;
- any-category/cross-list presence;
- share of physics corpus;
- category growth rate;
- cross-list network between categories.

Keep both native historical categories and a stable comparison taxonomy.

### Layer C — stable longitudinal comparison taxonomy

Because native arXiv categories change, map them to a deliberately coarse persistent layer. Initial candidate families:

- astrophysics/cosmology
- gravitation/relativity
- high-energy theory
- high-energy phenomenology/experiment/lattice
- nuclear physics
- condensed matter
- quantum physics/foundations/information
- atomic/molecular/optical
- plasma/fluids
- statistical/nonlinear/complex systems
- instrumentation/accelerators
- mathematical physics
- general/interdisciplinary physics

This mapping is a bibliometric convenience, not a claim about the correct ontology of physics. All mappings must remain reversible to native arXiv labels.

### Layer D — topic/theme dynamics

Within each year/period, derive topic distributions from titles + abstracts without SAT labels. Candidate methods:

- normalized keyword/keyphrase frequencies;
- TF-IDF / log-odds changes by period;
- embedding clustering/topic modeling;
- co-occurrence networks;
- changepoint detection;
- first-located and first-sustained appearances of concepts/phrases;
- disappearance and reappearance intervals.

Raw model-generated topic labels must remain descriptive until manually reviewed.

### Layer E — first appearance / modern reappearance ledger

For a later comparison concept, record separately:

- `EARLIEST-LOCATED-ARXIV` — earliest instance found in arXiv;
- `EARLIEST-LOCATED-MODERN` — earliest modern formulation found after a defined historical gap;
- `FIRST-SUSTAINED-CLUSTER` — first period where the concept appears repeatedly rather than as an isolated paper;
- `OLDER-PRIOR-ART-KNOWN` — known pre-arXiv or older literature exists;
- `SEARCH-INCOMPLETE` — priority cannot yet be claimed.

Never use `FIRST` without a scope qualifier. "Earliest located" is evidence; absolute historical priority requires a separate literature/provenance investigation.

## Comparison-ready fields

The atlas should eventually make it possible to compare any later Nathan-approved SAT structural package against external literature using neutral fields such as:

- date / period;
- native category + stable comparison family;
- title / abstract / authors;
- paper type where inferable (experiment, observation, theory, methods, review, instrumentation);
- physical domain / scale;
- mathematical machinery explicitly named;
- entities/structures explicitly modeled;
- explanatory relation claimed (emergence, reduction, effective description, unification, analogy, simulation, measurement, etc.);
- treatment of discreteness/continuity;
- treatment of geometry/topology;
- treatment of measurement/readout/observer;
- treatment of fundamental vs effective description;
- explicit relation to established frameworks;
- explicit novelty/prior-art language;
- whether an idea is proposed, demonstrated, constrained, falsified, reviewed, or merely mentioned.

These are comparison coordinates only. They do not become SAT features unless Nathan separately says so.

## Recommended temporal products

1. annual category table, 1991-present;
2. five-year and decade rollups;
3. category crosswalk/history ledger;
4. yearly top rising/falling terms and topics;
5. topic-family timelines;
6. first-located / reappearance ledger;
7. field/subfield trend summaries with uncertainty and taxonomy-change warnings;
8. frozen period-specific samples for reproducible comparisons.

## Immediate next build

Create a reproducible metadata harvester/sampler using the official arXiv OAI-PMH API, preserving native categories and dates. Start with a manageable annual sample for 1991-present, then add exact category counts where the API permits efficient counting. Maintain a separate taxonomy-change ledger from official arXiv documentation.
