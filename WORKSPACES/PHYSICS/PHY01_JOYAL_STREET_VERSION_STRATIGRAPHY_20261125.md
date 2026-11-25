# PHY-01 Bite 16 — Joyal–Street version stratigraphy: 1985 / 1986 / 1993

**Lane:** PHYS · ⟐ HSH_RESOURCES comparative-history workspace  
**Lens:** ℬ, geometric braid → categorical structure and its mathematical-physics applications  
**Recorded:** 2026-11-25  
**State:** PARTIAL SOURCE-STRATIGRAPHY RESULT · 1985 report visually inspected at key primary-source pages; 1986 report text inspected as primary source; 1993 publication metadata and reproduced introduction/contents inspected; full linear reading of the 1985 report and complete 1993 article remains outstanding.  
**Cursor effect:** none. PHYS remains at Connect / ℬ. Do not advance the ticker on this partial bite.

## 1. Question

What changed as Joyal and Street's braided-monoidal programme moved from the 1985 Macquarie report (85-0067), through the revised 1986 report (860081), to the peer-reviewed 1993 article *Braided Tensor Categories*? In particular, did publication simply stabilize and extend the earlier construction, or did it reorganize the programme and omit some earlier material?

This matters to the wider PHYS question because the formal mathematical landscape is not necessarily a linear accumulation of increasingly general abstractions. Different versions may select, separate, deepen or omit different branches.

## 2. Source-state audit

| Source | Identity / access | State in this bite |
|---|---|---|
| Joyal & Street, *Braided monoidal categories*, Macquarie Math. Report 85-0067 (Dec. 1985) | Scanned 31-page report recovered from nLab: https://ncatlab.org/nlab/files/JoyalStreet-BraidedMonoidal85.pdf. Cover, introduction, Section 4 “Ribbons and braids” (printed p. 8½), and Section 5 “Coherence for braidings” (printed p. 14) screenshot-inspected. Full text extraction is poor and complete linear reading remains outstanding. | PARTIAL PRIMARY-SOURCE VISUAL INSPECTION |
| Joyal & Street, *Braided monoidal categories*, Macquarie Math. Report 860081 (Nov. 1986) | Full report recovered at https://ncatlab.org/nlab/files/JoyalStreet-BraidedMonoidal.pdf. Title page, introduction, braid-category construction, universal-property section, group-cohomology/categorical-group section and quadratic-form classification were inspected. Selected pages were screenshot-inspected. | READ / PRIMARY SOURCE |
| Joyal & Street, *Braided tensor categories*, *Advances in Mathematics* 102(1) (Nov. 1993), pp. 20–78, DOI 10.1006/aima.1993.1055 | Macquarie's publication record confirms authorship, peer-reviewed article status, journal, volume, issue, date, pagination and DOI. The original publisher full text could not be retrieved in this bite. The article's title, contents and a portion of its introduction appear reproduced in Gregory Moore's 2024 history-of-physics slide deck. | BIBLIOGRAPHICALLY VERIFIED; PARTIAL REPRODUCED TEXT; FULL ARTICLE NOT READ |
| John Baez / Michael Shulman, *Lectures on n-Categories and Cohomology* | Lecture-note discussion explicitly compares the unpublished 1986 report with the 1993 published paper and identifies a substantive omission. | SECONDARY HISTORICAL / MATHEMATICAL COMMENTARY |
| nLab, *braided monoidal category* | Entry explicitly warns that the published version does not completely supersede the Macquarie reports, which contain extra results; it lists both reports and the 1993 article. | SECONDARY NAVIGATION / CROSS-CHECK |
| Ross Street, publications and *An Australian Conspectus of Higher Categories* | Author retrospective / bibliography establishes the 1985 report as revised in 1986 and provides contextual history of the subsequent braid, ribbon and tortile developments. | AUTHOR RETROSPECTIVE / BIBLIOGRAPHIC CROSS-CHECK |


## 2A. New primary-source correction: the 1985 report already contains ribbons

The first direct visual inspection of the 1985 report changes the earlier version map materially.

- The 1985 report is not merely an early string-braid precursor. Its Section 4 is explicitly titled **“Ribbons and braids.”**
- It records: **“Fred Linton provided the following example”** after a lecture on the paper. Linton's example defines a monoidal category whose arrows are braids on ribbons rather than strings, with ribbon twisting allowed. Each ribbon has two edges that act as strings, giving a faithful strict monoidal functor to the string-braid category by sending n ribbons to 2n strings.
- The purpose of this construction in the 1985 report is specific: it is a **counterexample** showing that axioms B3–B7 of Proposition 1 do not imply B1 or B2. It is not yet the later general theory of balanced/tortile categories.
- The 1985 report also already contains Section 5, “Coherence for braidings,” and its Theorem 4 states the universal/free braided-category property. Thus neither the coherence theorem nor the mere ribbon-braid idea should be described as first appearing in 1986 or 1993.
- The 1986 report's introduction explicitly refers to the “non-example suggested by F.E.J. Linton” and places it among the examples distinguishing braiding axioms. The 1985 report's “Fred Linton” and the 1986 report's “F.E.J. Linton” are consistent with the category theorist Fred Linton; no connection to Charles Howard Hinton is established or implied.

**Important distinction:** the 1985 ribbon example is a diagnostic countermodel. The later balanced/tortile programme turns ribbon twisting and duality into systematic categorical structure. These are related stages, not identical constructions.

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


## 5A. Version-stratigraphy correction after direct 1985 inspection

The previous description of the 1985 precursor as “not read” is superseded. Key pages have now been visually inspected directly. The accurate comparison is:

| Feature | 1985 report 85-0067 | 1986 report 860081 | 1993 article |
|---|---|---|---|
| Braided monoidal category / distinction from symmetry | Present in introduction and formal axioms | Present and expanded | Central subject |
| Braid category and configuration-space construction | Present | Present, with developed exposition | Retained and embedded in wider tensor-category programme |
| Free braided-category theorem / coherence | Already present in Section 5 | Present as main result of Section 4 | Retained and developed in categorical framework |
| Ribbon-braid construction | Present as Linton's counterexample in Section 4 | Present as Linton's non-example in Section 2 | Ribbon/twist structure develops into balanced categories; not the same role |
| Crossed modules, categorical groups, H^3 and quadratic classification | Not established by the inspected 1985 pages; complete absence not yet certified by linear collation | Substantial Sections 6–7 | Selective braided categorical-group treatment; secondary sources say general 2-group classification is omitted |
| Balanced categories and autonomy | Not yet identified as systematic sections in 1985 | Not yet established as full programme in the report | Explicit Sections 6–7 |

This table is deliberately conservative: “not yet identified” is not equivalent to proof of absence. The 1985 report's full 31 pages still need linear collation, and the 1993 full text still needs direct reading.

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

### Primary mathematical sources
- Joyal, A. & Street, *Braided monoidal categories*, Macquarie Mathematics Report 85-0067 (December 1985). PDF: https://ncatlab.org/nlab/files/JoyalStreet-BraidedMonoidal85.pdf
  - Cover/title page: report identity and date.
  - Printed p. 8½, Section 4 “Ribbons and braids”: Fred Linton's ribbon-braid counterexample, ribbon twist and faithful functor to the string-braid category.
  - Printed p. 14, Section 5 “Coherence for braidings”: Theorem 4/free braided-category universal property.
  - Visual inspection only for these pages; the scan's OCR/text extraction is poor and complete linear reading remains open.
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


## 9. Bite 17 addendum — classification shift and access audit

**Recorded:** 2026-11-25 · **State:** PRIMARY 1986 REPORT RE-READ AT INTRODUCTION/DEFINITIONAL LEVEL; SECONDARY CLASSIFICATION COMPARISON VERIFIED; FULL 1985/1993 COLLATION STILL OPEN. **Ticker:** unchanged.

### 9.1 A more precise account of what the 1993 publication leaves out

The Baez–Shulman lecture notes make the contrast more specific than the shorthand “the 1993 paper omits the 2-group classification” can suggest:

- The 1986 report classifies categorical groups (their term for 2-groups) using group cohomology, including the general (H^3(G,M)) data, and describes the whole 2-category of such structures.
- The 1993 paper does not simply reproduce that general classification. It moves to **braided 2-groups**, which Baez–Shulman describe as corresponding, morally, to connected pointed homotopy types with only (pi_2) and (pi_3) nontrivial.
- The corresponding classification is then expressed through (H^4(K(G,2),A)), rather than (H^3(K(G,1),A)=H^3(G,A)).

This is a meaningful shift of homotopy level, not merely a shorter presentation of the same theorem. It also shows why the distinction between ordinary categorical groups and braided categorical groups matters: the added braiding changes the homotopy-theoretic object being classified.

**Epistemic boundary:** this is a direct reading of Baez–Shulman's explicit secondary comparison, not yet a direct theorem-by-theorem reading of the 1993 article. Their notes describe the lectures as informal and explicitly say they gloss over precision. Use the statement as a strong navigation clue, not as a substitute for the original paper.

### 9.2 1986 definitional checks from the report itself

A fresh pass through the 1986 report's introduction and opening definitions confirms:

- A monoidal category has tensor product, unit, associator and unit constraints.
- A braiding is a natural family of isomorphisms (c_{A,B}:A\otimes B\to B\otimes A) satisfying two hexagon conditions.
- A symmetry is a braiding with the additional involutivity condition. The report explicitly says not every braiding is a symmetry.
- The braid group (B_n) is introduced as the fundamental group of the configuration space of (n)-element subsets of the Euclidean plane.
- The braid category packages strand counts as objects and braid groups as endomorphisms; tensor product is juxtaposition.
- The free braided monoidal category on one generator and the coherence theorem are already part of the 1986 report's central construction.

These checks reinforce that “braided” is not a loose synonym for “intertwined.” It is a precise natural isomorphism plus coherence constraints, and its non-involutivity is what distinguishes it from symmetry.

### 9.3 1993 full-text access attempts

The publisher's author page identifies the article as **Open archive** and offers “View PDF,” but the ScienceDirect page returned 403 on direct opening. The PDF endpoint and the Elsevier API text/XML endpoints were not retrievable through the available web access. The Macquarie research record confirms the bibliographic identity and peer-reviewed status but does not expose the article text. The bishtref mirror also returned 403.

The 2024 Rutgers slides remain a partial reproduction of the title, contents and introduction, not the complete article. The full 1993 text therefore remains **NOT READ**.

### 9.4 Current comparison, sharpened

| Layer | 1986 report | 1993 publication, as currently evidenced |
|---|---|---|
| Ordinary categorical groups / 2-groups | General (H^3(G,M))-based classification and 2-categorical treatment | General classification not carried over in the same form, according to Baez–Shulman |
| Braided categorical groups / braided 2-groups | Braided/abelian refinement and quadratic-form classification | Becomes a central classification target; homotopy interpretation shifts to connected pointed 3-types with (pi_2,pi_3), associated with (H^4(K(G,2),A)) |
| Ribbon/twist and duality | Earlier ribbon-braid counterexample; not yet the later systematic programme | Explicit balanced tensor categories and autonomy; author retrospective traces the ribbon/tortile development |
| Mathematical physics examples | Homotopy/cohomology examples and braid category | Finite general linear group representations, Yang–Baxter operators, and wider knot/tangle/quantum-group context |

The last column is deliberately marked “as currently evidenced”: the 1993 full paper has not been read directly, so detailed theorem statements and exact retention of individual constructions remain unverified.

### 9.5 Next operation

Keep the version-family closure open. Prioritize obtaining the 1993 article through an alternate institutional or author-hosted route, and continue the 1985 report's page-by-page collation. Do not branch into the wider Freyd–Yetter/Drinfeld/Witten history until the source comparison is adequately closed.

**Return cursor:** Connect / ℬ. No ticker advance.


## 10. Bite 17 continuation — expanded visual inspection of the 1985 scan

The 1985 scan is now visually inspected beyond the cover and the two previously noted key pages. Newly inspected leaves include the introduction (unnumbered front matter), printed pp. 1–9 and the inserted-looking half-page numbered 8½.

### Directly observed on the 1985 pages

- The introductory discussion explicitly frames the project as relaxing the symmetry requirement while retaining natural isomorphisms and coherence. It situates the work in relation to Mac Lane coherence, Eilenberg–Kelly, and the Eckmann–Hilton argument.
- The opening formal section defines a braiding by a natural family of isomorphisms (c_{A,B}:A\otimes B\to B\otimes A) satisfying two diagrams/hexagon conditions, and distinguishes it from symmetry by the additional involutivity condition.
- The report already gives examples of braided structures that are not symmetric, including a graded-module example parameterized by an invertible element (k\in K), with symmetry requiring (k^2=1).
- The braid-category discussion defines the braid group through the fundamental group of the configuration space of n-element subsets of a Euclidean plane, gives the Artin generators and braid relations, and describes braid addition as juxtaposition. It then packages the braid groups into a category whose objects are natural numbers and whose hom-sets are braid groups for equal strand counts (empty otherwise), with tensor product by addition/juxtaposition.
- The ribbon-braid counterexample is visible on the inserted-looking printed p. 8½. It attributes the example to Fred Linton, allows twisting of ribbons, regards each ribbon's two edges as strings, and gives a faithful strict monoidal functor sending n ribbons to 2n strings. The example satisfies selected later-listed diagrams while failing B1/B2; it is a diagnostic counterexample, not yet the systematic balanced/tortile theory.

### Source-layout caution

The scan's pagination/section ordering is not entirely straightforward: the inspected leaves include a printed p. 8½ headed “4. Ribbons and braids,” while the next sequential printed leaf p. 9 begins “§3. Multiplications on monoidal categories.” Do not silently normalize this into a clean linear section sequence. The report's own introduction gives a section roadmap that should be reconciled against the scan's apparent inserted leaf(s) and the remaining pages. This is another reason not to mark the 1985 report fully collated.

### Consequence for the chronology

The configuration-space braid group, its generators/relations, juxtaposition, and the categorical braid object are already present in the 1985 report. They are not innovations first appearing in 1986. The 1986 report should be treated as a substantial revision/expansion of an already established geometric and categorical construction, not as its first formulation.

**Visual locators:** 1985 report PDF pages 1–9 and inserted p. 8½, especially the braid-category definition and Artin relations (printed pp. 5–8), ribbon counterexample (printed p. 8½), and opening multiplication discussion (printed p. 9): https://ncatlab.org/nlab/files/JoyalStreet-BraidedMonoidal85.pdf. The PDF's text extraction is poor; these are direct visual inspections.

**State:** PARTIAL PRIMARY-SOURCE VISUAL INSPECTION; full page-by-page collation remains open. No ticker advance.


## 11. Bite 17 continuation — 1985 programme through convolution

Visual inspection now extends through the main body and references of the 1985 scan (printed pp. 1–23 and references pp. 25–26; the scan has nonstandard inserted leaves/pagination). This closes most of the report's substantive contents at the level of visual reading, though not a full transcription or line-by-line proof audit.

### 11.1 The 1985 report's mathematical architecture

The inspected pages establish the following sequence of content:

1. **Braiding axioms and examples.** A braiding is a natural isomorphism (c_{A,B}:A\otimes B\to B\otimes A) satisfying B1/B2; symmetry adds involutivity. Examples include graded modules with a scalar parameter and the braid category.
2. **Braid category.** The braid group is the fundamental group of the configuration space of finite subsets of the Euclidean plane. The report gives generators and Artin braid relations, braid addition by juxtaposition, and the category with natural numbers as objects and braid groups as endomorphisms.
3. **Multiplications on monoidal categories.** A multiplication is treated as a strong monoidal functor (V\times V\to V) with a pseudo-identity. Proposition 2 constructs a braiding from such a multiplication; Proposition 3 runs the construction in the other direction. The authors explicitly connect this to a generalized Eckmann–Hilton argument. This is a key conceptual result: braiding is not merely imported as a geometric diagram but can arise from a second compatible multiplication.
4. **Ribbon-braid counterexample.** The inserted-looking printed p. 8½ leaf, attributed to Fred Linton, allows ribbons to twist and maps each ribbon to its two edge strings. It demonstrates the independence/non-implication of selected braiding axioms.
5. **Coherence / free construction.** Theorem 4 states the free braided monoidal category on one generator, with evaluation at the generator giving the relevant equivalence of categories. The proof uses the braid relations and faithfulness of the braid interpretation to establish coherence. The report's printed p. 14 is headed “5A. Coherence for braidings,” so the coherence result is directly located in the scan.
6. **Categories enriched over braided monoidal categories.** Section 5 treats enriched categories and proves the required enriched structure from the braiding axioms.
7. **Convolution and bilinearity.** Section 6 develops convolution constructions and notes that convolution can transport braided monoidal structure. Proposition 7 gives a completeness result for a suitable convolution category. The graded-module example is revisited through convolution.

The section/pagination sequence contains an apparent inserted p. 8½ leaf and duplicated-looking section numbering in the scan. The report's introductory roadmap and the actual leaf order should remain separately recorded until a clean source copy or author copy resolves the layout. The content above is based on the visible headings and propositions, not a reconstructed clean typeset edition.

### 11.2 What this changes in the 1985/1986 comparison

The 1985 report already contains much more than the isolated braid-category definition:
- the configuration-space and Artin-presentation geometry;
- the free braided category and coherence theorem;
- the generalized Eckmann–Hilton / multiplication ↔ braiding bridge;
- a ribbon-braid counterexample;
- enrichment over braided monoidal categories; and
- convolution constructions.

Therefore the 1986 report's novelty should not be summarized as “it introduces braids/categories.” The direct comparison now points to a substantial expansion and formal development of an already broad programme, with the most conspicuous new branch in 1986 being categorical groups, crossed modules, group cohomology and quadratic-form classification. A full diff still requires systematic collation of every 1985 and 1986 proposition and example.

### 11.3 Current 1985 source state

**State:** SUBSTANTIVE VISUAL INSPECTION OF MAIN BODY AND REFERENCES; NOT A FULL LINEAR TRANSCRIPTION OR PROOF AUDIT. The 1985 report can now be treated as a primary source for the main programme and the claims above, but exact wording and proof details should be checked against a clean copy before fine-grained theorem comparison.

**Visual locators:** 1985 PDF printed pp. 5–8 (configuration-space braid category, generators/relations, juxtaposition and categorical packaging); printed p. 8½ (Fred Linton ribbon counterexample); printed pp. 9–18 (multiplication/braiding, coherence/free construction); printed pp. 19–21 (enrichment); printed pp. 22–23 (convolution); references pp. 25–26. PDF: https://ncatlab.org/nlab/files/JoyalStreet-BraidedMonoidal85.pdf.

**Cursor:** unchanged. Complete 1986/1993 collation and direct 1993 reading remain open.


## 12. Bite 18 — proposition-level 1985/1986 collation: first comparison matrix

**Recorded:** 2026-11-25 · **State:** DIRECT VISUAL COLLATION OF THE 1985 REPORT'S MAIN SECTION SEQUENCE AGAINST THE 1986 REPORT'S INTRODUCTION AND PRIMARY SECTIONS 1–7; NOT A COMPLETE PROOF-BY-PROOF DIFF. **Cursor:** unchanged at Connect / ℬ.

### 12.1 A key source correction: 1985 already has the homotopy bridge in embryo

The 1985 report's introduction explicitly says the work was generated by the confluence of (i) a conversation involving A. Carboni, F.W. Lawvere and R.F.C. Walters in Sydney (January 1984), and (ii) joint work of M. Tierney and the first author. It describes the homotopy-3-type motivation: arc-connected, simply connected spaces could be represented by what the authors would call braided groups in Cat, using a Gray tensor-product construction whose coherence proof used braid groups.

The 1985 Section 2 also contains a concrete construction headed “Homotopy structure of the 2-sphere.” Thus the homotopy connection is not a wholly new 1986 invention. What is new in the 1986 presentation is the systematic crossed-module/bracket framework and its connection to group cohomology and categorical-group classification.

### 12.2 Directly observed section architecture

| 1985 handwritten report 85-0067 | 1986 typed report 860081 | Comparison |
|---|---|---|
| §1 Braiding axioms and consequences B3–B7 | §1 Braiding axioms and consequences | Same foundational structure; 1986 typed exposition and consolidates axiom-dependence discussion |
| §2 Examples: graded modules; homotopy structure of the 2-sphere | §2 Examples: graded modules; braid category; Linton non-example; crossed modules with bracket; Day convolution | 1986 broadens/reorganizes the example gallery. The 2-sphere construction is already in 1985; the 1986 report supplies a more general crossed-module/bracket treatment and additional examples |
| §3 The braid category (configuration space, Artin generators/relations, juxtaposition, categorical packaging) | Braid category is integrated into §2's examples and then used centrally in §4 | Reorganization of exposition, not first introduction in 1986 |
| §4 Ribbons and braids (inserted-looking printed p. 8½; Fred Linton counterexample) | Linton non-example incorporated in §2 | Same diagnostic role; moved into the example sequence |
| §3 Multiplications on monoidal categories (printed p. 9 onward; numbering overlaps because of the inserted leaf) | §3 Multiplications on monoidal categories | Core Propositions 2 and 3 retained; 1986 gives a cleaner typed exposition and explicitly summarizes the equivalence of 2-categories BMC and Mult(MC) |
| §5A Coherence for braidings (Theorem 4/free braided category) | §4 Coherence for braidings (Theorem 4) | Same central free-category/coherence result; 1986 develops the 2-monadic formulation more explicitly |
| §5 Categories enriched over braided monoidal categories (Propositions 5 and 6) | §5 Categories enriched over braided monoidal categories (Propositions 5 and 6) | Substantially retained. The 1986 report states the precise obstruction to using symmetric-case Mac Lane coherence and replaces it with consequences B5/B6 of Proposition 1 |
| §6 Convolution and bilinearity (Day convolution; Proposition 7) | Convolution appears as an example in §2, with the general multiplication/braiding discussion following in §3 | Reorganized and integrated into the example gallery; the presheaf convolution construction remains |
| No corresponding full section in the inspected 1985 body for general H³/categorical-group classification | §6 Cohomology of groups; §7 quadratic functions and compact braided monoidal groupoids | Major 1986 expansion: categorical groups/crossed modules, a 2-category H³, biequivalence with compact monoidal groupoids, then classification of compact braided monoidal groupoids by quadratic functions |

The 1985 report's section numbering is genuinely irregular: the ribbon example is printed as §4 on p. 8½, followed by printed p. 9 headed §3. Preserve the physical page labels and the authors' introductory roadmap rather than inventing a normalized sequence.

### 12.3 The multiplication ↔ braiding result: same theorem, stronger categorical packaging

The 1985 report already states:
- Proposition 2: a braiding on a monoidal category defines a multiplication (a strong monoidal binary operation with pseudo-identity).
- Proposition 3: a multiplication defines a braiding; the two constructions are inverse up to the stated isomorphism.
- The resulting 2-category of braided monoidal categories is equivalent to the corresponding 2-category of monoidal categories with multiplication.

The 1986 report retains Propositions 2 and 3 and makes the 2-categorical equivalence explicit in its section summary. It also foregrounds the generalized Eckmann–Hilton argument as the conceptual explanation: a second multiplication compatible up to coherent isomorphism yields braiding rather than necessarily symmetry.

This is a refinement and clearer structural placement, not a new discovery first made in 1986.

### 12.4 Coherence: same free object, expanded monadic context

Both reports establish the braid category as the free braided strict monoidal category on one generator and use faithfulness of the braid interpretation to obtain coherence: diagrams built from associativity and braiding commute when their underlying braids agree.

The 1986 report adds a more explicit 2-monadic description: braided strict monoidal categories are algebras for a 2-monad on Cat, with braided monoidal categories as pseudo-algebras; the braid category represents the theory in this sense. The 1985 report already points toward the free construction and coherence, but the 1986 version makes the categorical-theory packaging more explicit.

### 12.5 The homotopy/crossed-module extension: from special model to general structure

The 1985 report's introductory historical note and “Homotopy structure of the 2-sphere” example establish that homotopy 3-types were part of the programme from the beginning. The 1986 report's Example 4 makes the general algebraic interface explicit:
- crossed modules are treated as groups in Cat / strict monoidal categories;
- a braiding corresponds to a bracket operation on the crossed module;
- the bracket has the properties of an abstract commutator and, in the appropriate notation, a bilinear operation;
- the Samelson bracket is identified as the familiar homotopy-theoretic structure;
- a special integer example is related to the algebraic model of the homotopy 3-type of the 2-sphere.

The new 1986 contribution is therefore best described as **generalization and formal integration** of a homotopy-motivated example into the categorical-group / crossed-module framework, not the first appearance of homotopy motivation.

### 12.6 Strongest current difference

The most consequential new 1986 material is not the braid category, the free braided category, coherence, multiplication/braiding correspondence, enrichment or Day convolution. Those are already present in 1985. The major extension is the new categorical-group classification programme:
1. a 2-category H³ whose objects include groups, modules and normalized 3-cocycles;
2. a construction of monoidal categories from these data;
3. a biequivalence between H³ and compact monoidal groupoids;
4. the interpretation through crossed modules; and
5. classification of compact braided monoidal groupoids by abelian groups and quadratic functions arising as traces of braidings.

The exact relationship between this 1986 general classification and the 1993 braided-2-group / H⁴(K(G,2),A) treatment remains a separate direct-reading task.

### 12.7 Primary-source locators

**1985 report 85-0067** (handwritten scan): https://ncatlab.org/nlab/files/JoyalStreet-BraidedMonoidal85.pdf
- Introductory historical note and section roadmap: PDF page 2 (front matter marked iv–v).
- “Homotopy structure of the 2-sphere”: printed p. 4.
- Configuration-space braid group, Artin generators and relations, juxtaposition, braid category: printed pp. 5–8.
- Fred Linton ribbon counterexample: printed p. 8½.
- Multiplications on monoidal categories, Propositions 2 and 3: printed pp. 9–13.
- Coherence / Theorem 4: printed pp. 14–18.
- Enriched categories, Propositions 5 and 6: printed pp. 19–21.
- Convolution and bilinearity, Proposition 7: printed pp. 22–23.
- The 1985 scan's irregular inserted leaf/section numbering is retained as a source caveat.

**1986 report 860081** (typed scan): https://ncatlab.org/nlab/files/JoyalStreet-BraidedMonoidal.pdf
- Introductory section roadmap and historical framing: PDF lines 24–421.
- Braid axioms and examples: printed pp. 1–5 / PDF lines 422–870.
- Crossed modules and bracket operations: printed pp. 9–11 / PDF lines 870–960.
- Day convolution: printed pp. 11–12 / PDF lines 964–993.
- Multiplication and Propositions 2–3: printed pp. 12–16 / PDF lines 994–1213.
- Free braided category, Theorem 4, 2-monadic framing and coherence: printed pp. 16–20 / PDF lines 1215–1423.
- Enrichment, Propositions 5–6: printed pp. 21–24 / PDF lines 1424–1526.
- H³ / categorical groups: Section 6, beginning printed p. 24 / PDF lines 1527 onward.
- Quadratic classification: Section 7, concluding sections / PDF lines 370–397 of introduction and approximately 2124–2431 in body.

**Author retrospective:** Ross Street, *An Australian Conspectus of Higher Categories*, https://www.math.uchicago.edu/~may/IMA/Incoming/Street/Street.pdf. Use as retrospective testimony, not a substitute for the reports.

**State:** first proposition-level comparison matrix established. The 1985 scan is substantively visually inspected; the 1986 report's typed primary text has been checked against the matrix. A complete proof-by-proof textual diff and the full 1993 paper remain outstanding. No ticker advance.


## 13. Bite 18 continuation — the 1993 introduction is now recoverable as reproduced primary text

A more complete 2024 Rutgers slide-deck text extraction has been located. Gregory Moore reproduces the 1993 article's title page, contents and opening introduction, including the authors' first-person account of the programme's widening after the 1986 report. This is **reproduced primary text inside a secondary presentation**, not the complete original article and not an independently accessed publisher PDF.

### 13.1 What the reproduced 1993 introduction says

The article's own introduction identifies two 1986 stimuli:
- Peter Freyd's Cambridge Category Theory Conference talk on joint work with David Yetter, where their tangle category was found to be braided, autonomous and free in a relevant sense.
- Vladimir Drinfeld's International Congress talk on quantum groups, where quasitriangular bialgebras supplied new examples of braided structures.

The reproduced introduction then dates a further step to mid-1987:
- Joyal and Street turned from string tangles to ribbon tangles.
- This led to balanced tensor categories, which add a twist on each object to the braiding.
- Incorporating dual objects led to tortile tensor categories.

This is stronger than a later historian's inference: it is the authors' own retrospective explanation as printed in their article, although accessed here through Moore's reproduction. It supports a sequence in which the 1985/1986 report's string-braid programme is widened by new tangle and quantum-group examples, then by ribbon twists and duality.

### 13.2 Contents of the 1993 article, as reproduced

The slide-deck reproduction gives the article's seven sections:
1. Tensor categories.
2. Braidings and Yang–Baxter operators.
3. Braided categorical groups.
4. A braiding for representations of the finite general linear groups.
5. Abstract categorical aspects of braidings.
6. Balanced tensor categories.
7. Autonomy.

The contents confirm that the 1993 paper is not merely a reprint of the 1986 report. It places tensor categories, Yang–Baxter operators, representation theory, abstract categorical structure, balanced structure and autonomy into one publication architecture.

### 13.3 Evidence boundary

The slide deck itself explicitly warns that its historical account is focused mostly on Moore's own role and that memory is unreliable. That caveat applies to Moore's recollections, not to the literal article text he reproduces. Keep the two evidence types separate:
- The title, contents and reproduced Joyal–Street introduction are primary text quoted/reproduced in a secondary venue.
- Moore's broader chronology and recollections are secondary eyewitness testimony and should be triangulated.
- The complete 1993 article remains **NOT READ**. No claims about the full proofs, exact theorem statements, or every retained/omitted result should be upgraded on the basis of the excerpt.

### 13.4 Source locator

Gregory Moore, *From Rational Conformal Field Theories to Modular Tensor Categories to Nonabelions* (Rutgers, 26 September 2024), PDF: https://www.physics.rutgers.edu/~gmoore/From-RCFT-To-MTC-20240926-FINAL.pdf.
- PDF extracted-text lines 1540–1571 reproduce the 1993 title, contents and opening introduction.
- Lines 14–20 state the author's explicit scope/memory caveats.
- The slide deck's broader chronology begins at lines 28–35 and should be treated as a perspective rather than a complete history.

**Current source-family result:** the 1985/1986 comparison is now established at section/proposition-architecture level. The 1993 article's own introduction and contents are recoverable in reproduction, but the original complete article remains outstanding. No ticker advance.
