# PHY-01 Bite 16 — Joyal–Street version stratigraphy: 1985 / 1986 / 1993

**Lane:** PHYS · ⟐ HSH_RESOURCES comparative-history workspace  
**Lens:** ℬ, geometric braid → categorical structure and its mathematical-physics applications  
**Recorded:** 2026-11-25  
**State:** PARTIAL SOURCE-STRATIGRAPHY RESULT · 1986 report inspected as primary source; 1993 publication metadata and reproduced introduction/contents inspected; 1985 precursor and complete 1993 article not yet directly inspected.  
**Cursor effect:** none. PHYS remains at Connect / ℬ. Do not advance the ticker on this partial bite.

## 1. Question

What changed as Joyal and Street's braided-monoidal programme moved from the 1985 Macquarie report (85-0067), through the revised 1986 report (860081), to the peer-reviewed 1993 article *Braided Tensor Categories*? In particular, did publication simply stabilize and extend the earlier construction, or did it reorganize the programme and omit some earlier material?

This matters to the wider PHYS question because the formal mathematical landscape is not necessarily a linear accumulation of increasingly general abstractions. Different versions may select, separate, deepen or omit different branches.

## 2. Source-state audit

| Source | Identity / access | State in this bite |
|---|---|---|
| Joyal & Street, *Braided monoidal categories*, Macquarie Math. Report 85-0067 (Dec. 1985) | nLab and later bibliographies identify a 31-page precursor. Ross Street's publication list identifies it alongside the revised 1986 report. The linked university PDF endpoints timed out / were inaccessible during this bite. | LOCATED; NOT READ |
| Joyal & Street, *Braided monoidal categories*, Macquarie Math. Report 860081 (Nov. 1986) | Full report recovered at https://ncatlab.org/nlab/files/JoyalStreet-BraidedMonoidal.pdf. Title page, introduction, braid-category construction, universal-property section, group-cohomology/categorical-group section and quadratic-form classification were inspected. Selected pages were screenshot-inspected. | READ / PRIMARY SOURCE |
| Joyal & Street, *Braided tensor categories*, *Advances in Mathematics* 102(1) (Nov. 1993), pp. 20–78, DOI 10.1006/aima.1993.1055 | Macquarie's publication record confirms authorship, peer-reviewed article status, journal, volume, issue, date, pagination and DOI. The original publisher full text could not be retrieved in this bite. The article's title, contents and a portion of its introduction appear reproduced in Gregory Moore's 2024 history-of-physics slide deck. | BIBLIOGRAPHICALLY VERIFIED; PARTIAL REPRODUCED TEXT; FULL ARTICLE NOT READ |
| John Baez / Michael Shulman, *Lectures on n-Categories and Cohomology* | Lecture-note discussion explicitly compares the unpublished 1986 report with the 1993 published paper and identifies a substantive omission. | SECONDARY HISTORICAL / MATHEMATICAL COMMENTARY |
| nLab, *braided monoidal category* | Entry explicitly warns that the published version does not completely supersede the Macquarie reports, which contain extra results; it lists both reports and the 1993 article. | SECONDARY NAVIGATION / CROSS-CHECK |
| Ross Street, publications and *An Australian Conspectus of Higher Categories* | Author retrospective / bibliography establishes the 1985 report as revised in 1986 and provides contextual history of the subsequent braid, ribbon and tortile developments. | AUTHOR RETROSPECTIVE / BIBLIOGRAPHIC CROSS-CHECK |

## 3. What the 1986 primary report actually builds

### 3.1 Braid as a configuration-space fundamental group

Joyal and Street define the braid group B_n as the fundamental group of the configuration space of n-element subsets of the Euclidean plane, with distinct points. A loop in configuration space is represented by the moving strands of a braid. The report then defines addition/juxtaposition of braids and packages the braid groups into the braid category:

- objects are natural numbers, interpreted as strand counts;
- endomorphisms of n are elements of B_n;
- composition is braid-group multiplication;
- tensor product is juxtaposition, both on objects and arrows.

This is the exact geometric starting point. A braid diagram is not merely a suggestive drawing: it represents a homotopy class of loops in a specified configuration space.

### 3.2 Braiding is not symmetry

A braiding is a natural family of isomorphisms c_{A,B}: A⊗B → B⊗A satisfying the two hexagon constraints. A symmetry is a braiding with the additional involutivity condition: exchanging and then exchanging back gives the identity. The report stresses that many important examples are braided but not symmetric, including examples arising in homotopy and cohomology.

This distinction is structural, not terminological. It is why the braid group appears in place of the permutation group in the relevant mathematical setting.

### 3.3 The universal categorical construction

Theorem 4 states that for a braided monoidal category V, evaluation at the single generating object identifies braided monoidal functors from the braid category B into V with objects of V (an equivalence; for strict monoidal V, an isomorphism). The authors describe B as the free braided strict monoidal category on the one-object, one-arrow category.

The associated coherence theorem says, in substance, that diagrams built from associativity and braiding commute whenever their associated braids are equal. This is a precise bridge:

configuration-space loops → braid group → braid category → universal braided-monoidal structure → representations in other braided monoidal categories.

The geometric braid data are not simply discarded by the categorical formulation. Their composition and equality conditions govern the coherence equations.

### 3.4 The larger homotopy / categorical-group programme

The 1986 report does not stop at the free braid category. Its later sections develop a separate, deeper branch:

- Section 6 treats H^3(G,M), group cohomology and crossed modules through categorical groups / compact monoidal groupoids and coherence.
- Section 7 treats the braided case for abelian groups. Braiding corresponds to an abelian 3-cocycle, and the trace of that cocycle yields a quadratic function. The classification theorem identifies equivalence classes of compact braided monoidal groupoids with the relevant quadratic data.

This is not an additional physical spatial dimension. It is higher categorical structure: objects, arrows, transformations between functors, and 2-category/biequivalence-level classification. It connects braid structure with algebraic topology and homotopy 3-types.

## 4. What can currently be said about the 1993 publication

The Macquarie University record confirms that *Braided tensor categories* is the peer-reviewed 1993 article in *Advances in Mathematics* 102(1), pages 20–78.

The reproduced table of contents lists:

1. Tensor categories
2. Braidings and Yang–Baxter operators
3. Braided categorical groups
4. A braiding for representations of the finite general linear groups
5. Abstract categorical aspects of braidings
6. Balanced tensor categories
7. Autonomy

The reproduced introduction gives a first-person account of how the subject widened after the 1986 report:

- Freyd's 1986 talk on joint work with Yetter presented a tangle category that was braided, autonomous and free in a relevant sense.
- Drinfeld's 1986 International Congress talk on quantum groups supplied quasitriangular bialgebras as new examples of braided structures.
- By mid-1987, the authors were studying tangles of ribbons rather than strings. This led to balanced tensor categories, where braiding is supplemented by a twist on each object.
- Incorporating dual objects led to tortile tensor categories.

This is an important shift in the programme: the mathematical examples and applications were broadening through knot/tangle theory and quantum groups, and the formalism acquired ribbon/twist and duality structure.

## 5. The important publication difference: a selective reorganization, not a simple superset

Baez and Shulman's lecture notes explicitly observe that the 1986 Macquarie report describes the whole 2-category of categorical groups / 2-groups using group cohomology, while the published 1993 paper leaves out that general classification and moves directly to the classification of braided 2-groups.

This is consistent with two other observations:

- the 1986 report has a full Section 6 on H^3(G,M), categorical groups and crossed modules, followed by Section 7 on the braided/abelian refinement and quadratic forms;
- nLab explicitly warns that the 1993 published version does not completely supersede the Macquarie reports, which contain extra results.

**Working conclusion:** the 1993 paper is not to be treated as a complete replacement for the 1985/1986 reports. The publication reorganizes and develops the braided tensor-category programme around further examples and structures, while at least some broader categorical-group classification material remains a distinctive feature of the earlier reports. The 1986 report therefore remains a necessary source for the complete mathematical terrain.

Do not overstate the comparison yet: the 1985 report and complete 1993 article have not been directly collated here. The precise changes between 1985 and 1986, and the full scope of what the 1993 article retains or omits, remain open.

## 6. Relevance to the larger PHYS / SAT-H(s)H investigation

This bite reinforces a central method for decoding the higher-category landscape:

1. Begin with the concrete geometry (here, paths of configurations of points in a plane).
2. Identify the topological object (the fundamental group of configuration space).
3. Recover the algebraic presentation (generators, relations, composition).
4. See how it is packaged categorically (objects, morphisms, tensor product, braiding).
5. Follow which information is preserved by universal properties and coherence.
6. Track the further higher-categorical layers (categorical groups, 2-cells, biequivalence, cohomological classification).
7. Trace the new examples and physical applications (tangles, quantum groups, representations, ribbon structures).

For SAT/H(s)H, this gives us a rigorous *comparison protocol*, not a pre-assigned result. The SAT filament/worldtube construction may eventually define a constrained realization, representation or substructure in part of this landscape; that cannot be concluded from the common word “braid.” The native SAT/H(s)H object/core geometry gate ◈ remains independently open.

The deeper lesson is that “higher category theory” here is not an unbounded container of arbitrary relations. It is a controlled system of objects, morphisms, higher transformations, coherence and equivalence. Some geometry becomes portable by abstraction; some detail is generalized, suppressed or omitted; different published and unpublished versions preserve different slices of the architecture.

## 7. Open questions and next bite

- **JS-V01:** Recover and read the 1985 report 85-0067 directly. Compare it against 1986 860081 and record the precise revisions, additions and deletions.
- **JS-V02:** Obtain the full original 1993 paper (DOI 10.1006/aima.1993.1055) and compare all seven sections against the 1986 report, especially Sections 3, 6 and 7.
- **JS-V03:** Verify exactly which classification the 1993 paper retains for braided categorical groups and how its equivalence/biequivalence-level statement relates to the 1986 report's H^3(G,M) and abelian 3-cocycle/quadratic-form treatment.
- **JS-V04:** Trace the transition from string braids to ribbon/tangle, balanced and tortile categories, and identify precisely how twist and duality enlarge the admissible diagrammatics.
- **JS-V05:** Separate the 1986 Freyd–Yetter and Drinfeld stimulus from the original 1985/1986 development. Track documentary transmission through citations and author recollections; do not collapse parallel contributions.

**Return:** remain at Connect / ℬ. Next bite should close JS-V01 and JS-V02, not branch prematurely into the full Drinfeld–Witten or computational-network histories.

## 8. Source map and exact locators

### Primary mathematical source
- Joyal, A. & Street, R., *Braided monoidal categories*, Macquarie Mathematics Report 860081 (November 1986). PDF: https://ncatlab.org/nlab/files/JoyalStreet-BraidedMonoidal.pdf
  - Title page and report identity: PDF cover; printed front matter.
  - Braiding versus symmetry and programme overview: printed front matter pp. ii–vii.
  - Braid group as configuration-space fundamental group; braid category and juxtaposition: printed pp. 5–6.
  - Free braided monoidal category / Theorem 4 and coherence: printed pp. 17–19.
  - Group cohomology, categorical groups and crossed modules: printed pp. 24–33.
  - Abelian 3-cocycles and quadratic forms: printed pp. 34–37.

### 1993 publication record / reproduced article excerpt
- Macquarie University, *Braided tensor categories* publication record: https://researchers.mq.edu.au/en/publications/braided-tensor-categories/
- DOI: https://doi.org/10.1006/aima.1993.1055
- Gregory Moore, *From Rational Conformal Field Theories to Modular Tensor Categories to Nonabelions* (26 September 2024), Rutgers PDF: https://www.physics.rutgers.edu/~gmoore/From-RCFT-To-MTC-20240926-FINAL.pdf
  - Slides/PDF extracted-text segment reproducing the Joyal–Street 1993 title, contents and portion of introduction. The PDF screenshot endpoint rejected the full large file; this reproduction was inspected as text only, not visually verified.
  
### Secondary comparison and author bibliography
- John Baez and Michael Shulman, *Lectures on n-Categories and Cohomology*: https://www.math.uchicago.edu/~may/IMA/Incoming/Baez/cohomology.pdf
  - Explicit note that the 1993 publication leaves out the general 2-group classification in the 1986 report and moves to braided 2-groups.
- nLab, *braided monoidal category*: https://ncatlab.org/nlab/show/braided%20monoidal%20category
  - Warns that the 1993 publication does not fully supersede the Macquarie reports, which contain additional results.
- Ross Street, Publications: https://science.mq.edu.au/~street/Publications.html
  - Lists 85-0067 (1985) and 860081 (1986) as precursor and revision; lists the 1993 article.
- Ross Street, *An Australian Conspectus of Higher Categories*: https://www.math.uchicago.edu/~may/IMA/Incoming/Street/Street.pdf
  - First-person historical account of Freyd/Yetter, Drinfeld, ribbon braids, balanced/tortile categories and related developments.

**Reading-state rule:** a bibliographic record, reproduced excerpt, or secondary comparison is not a substitute for reading the complete 1985 and 1993 papers. Keep those gaps visible until closed.
