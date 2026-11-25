# Biological Mechanism 03 — Cellular Chirality, Actomyosin, and Left–Right Development

**Lane:** BIO / comparative-history lane  
**Created:** 2026-11-25  
**Status:** SYNTHESIZED / `χ` bite ready for ledger closure  
**Parent path:** `BIO:⟐βᛟvnχ@rmρk⊕[mbxᛟd]s`  
**Primary repository:** `Satobloc/HSH_RESOURCES`  
**Purpose:** Reconstruct Tee et al. (2015) at mechanism level, then compare it with independent actomyosin- and Myo1D-related systems that connect cell chirality to organismal laterality. This is a comparative biological study, not a change to H(s)H theory or worker policy.

## 1. Main result

There is no single universal “actomyosin chirality mechanism.” The sources instead show a family of related but non-identical ways in which actin organization, myosin-generated force, local polarity, and cell/tissue geometry can produce handed cellular behavior or contribute to embryonic left–right patterning.

The distinctions are decisive:

1. **Tee et al. (2015):** a radial/transverse actin-fibre network in circularly confined cultured fibroblasts spontaneously changes into a chiral cytoskeletal pattern. Myosin-IIA contractility powers transverse-fibre movement; formin-dependent radial growth and α-actinin-1 regulation participate in the organization and handedness selection. This is a cell-intrinsic cytoskeletal result, not an embryo laterality demonstration.
2. ***C. elegans* (Naganathan et al. 2014):** the actomyosin cortex generates active chiral torque and counter-rotating cortical flow. Modulating Rho-pathway activity changes the magnitude of the four-cell-stage cell-skew event that establishes embryonic left–right asymmetry. This is a direct developmental actomyosin mechanism, but it is not Tee’s radial/transverse fibre architecture.
3. **Drosophila:** Myo31DF/Myo1D, an unconventional class-I myosin, is required for normal handedness of several visceral structures. Planar cell-shape chirality in hindgut epithelium and tissue-level interactions connect cell-intrinsic handedness to organ morphogenesis.
4. **Zebrafish:** Myo1D and the PCP component Vangl2 regulate cilia orientation in Kupffer’s vesicle and thereby the directional organizer flow required for laterality. This is a connection from a Myo1D/PCP polarity system to a cilia-flow mechanism, not proof that the mouse node uses the same upstream regulator.
5. **Drosophila macrophages (Yamaguchi et al. 2026):** a newly published study reports Myo1D- and Myo1C-directed circumferential F-actin flows, in collaboration with Myosin2. The authors propose that Myo1D arranges actin filament polarity and Myo2 rotates the resulting structures. This supplies a recent molecular bridge between class-I unconventional myosins and class-II myosin-driven actin motion, but the inspected source is abstract-level and does not establish an organismal laterality role for macrophage flow.

**Synthesis:** the recurring motif is not a single molecular pathway. It is a class of non-equilibrium cytoskeletal systems in which handed filament architecture, motor-generated forces/torques, and geometrically organized boundary conditions can produce directional cellular motion or polarity. Which components are used, and how they are coupled to tissue and organ outcomes, differ by organism and tissue.

## 2. Tee et al. 2015 — radial/transverse fibre self-organization

**Primary source:** Yee Han Tee et al., “Cellular chirality arising from the self-organization of the actin cytoskeleton,” *Nature Cell Biology* 17 (2015), 445–457. DOI: https://doi.org/10.1038/ncb3137. Full-paper PDF inspected: https://proteinacrobaticslab.umn.edu/sites/proteinacrobaticslab.umn.edu/files/files/publications_31.pdf. PubMed record and abstract: https://pubmed.ncbi.nlm.nih.gov/25799062/.

### Experimental geometry

The authors studied human foreskin fibroblasts on circular fibronectin micropatterns (approximately 1,800 μm²). The confinement was chosen to maintain an approximately isotropic circular cell shape, reducing the ordinary directional biases associated with elongated cell geometry. Time-lapse imaging followed the spontaneous organization and movement of the actin cytoskeleton.

The network transitions from a peripheral circumferential actin rim to a radially organized pattern. The radial array subsequently develops a consistent tilt, accompanied by a tangential component of transverse-fibre movement, producing a handed or swirling pattern. In the reported observations, roughly 70% of videos showed the initial circumferential-to-radial transition, and around 80% of cells undergoing the radial-to-chiral transition showed the same direction of tilt in the experimental setup. These percentages are conditional on the observed experimental sequence and should not be read as an organism-wide prevalence.

### Two interacting fibre populations

| Feature | Radial fibres (RFs) | Transverse fibres (TFs) |
|---|---|---|
| Orientation | Extend radially inward from peripheral focal adhesions | Cross the radial fibres and move centripetally |
| Enrichment | α-actinin-1, zyxin, VASP | Myosin IIA |
| Main relevant behavior | Formin-dependent actin polymerization and centripetal growth | Myosin-IIA-dependent contractile movement |
| Mechanical role | Provide growing radial tracks and anchors at focal adhesions | Bind/interact with RFs and exert contractile forces |
| Chirality relevance | RF tilting is the visible directional reorganization | TF movement acquires a tangential component as RFs tilt |

The fibres interact at a closely apposed cytoskeletal layer. The paper reports mean RF growth of approximately 0.21 ± 0.09 μm/min and TF centripetal movement of approximately 0.35 ± 0.14 μm/min in the measured fibre pairs. The faster TF movement is consistent with a combination of centripetal movement along the growing radial array and motion relative to the radial fibres.

### Perturbations and causal interpretation

- **Formin inhibition:** SMIFH2 suppresses radial-fibre formation and reduces associated transverse-fibre movement; recovery after inhibitor removal supports a dynamic dependence on formin activity.
- **Myosin-II inhibition:** blebbistatin suppresses ATP-driven transverse-fibre movement. ATP supports TF movement in permeabilized-cell experiments, whereas non-hydrolysable AMPPNP does not, supporting a motor-dependent process.
- **Actin-nucleation perturbation:** Arp2/3 inhibition disrupts formation of the fibre system.
- **α-actinin-1 perturbation:** changing α-actinin-1 levels changes the handedness of cells that still undergo the radial-to-chiral transition; in some cases the sign of the swirl reverses.
- **Mechanical model:** transverse fibres bind dynamically along radial fibres. Myosin-IIA contraction drives movement and exerts both centripetal and tangential components of force. Those interactions bend/tilt radial fibres around their anchored ends, allowing collective alignment into a chiral pattern.

### A key separation: force generation versus handedness selection

Myosin-IIA is essential to the movement and self-organization of the TF/RF system, but the paper does not establish that myosin-IIA itself sets the sign of the chirality. The authors suggest that the directional bias may arise from the helical structure of actin filaments as formin drives polymerization, with α-actinin-dependent crosslinking and constraints controlling how tangential forces are transmitted. They specifically note that the direction-setting radial fibres are not myosin-containing in the studied arrangement.

This is best described as a **proposed physical explanation supported by perturbation and modelling**, not as a fully resolved molecular account of chirality selection.

### Scope

Tee et al. demonstrate spontaneous cell-intrinsic cytoskeletal chirality under a deliberately controlled micropattern geometry. They do not study an embryonic organizer, ciliary flow, Nodal signaling, or organ situs. The paper’s suggestion that this self-organizing machinery could potentially contribute to left–right asymmetry is a biologically motivated implication, not a demonstrated developmental lineage from these fibroblasts to an embryo.

## 3. *C. elegans* — actomyosin cortical torque in an actual embryonic symmetry-breaking event

**Primary source:** Sundar Ram Naganathan et al., “Active torque generation by the actomyosin cell cortex drives left–right symmetry breaking,” *eLife* 3:e04165 (2014), published 17 December 2014. DOI: https://doi.org/10.7554/eLife.04165. Open article/PDF: https://elifesciences.org/articles/04165 and https://elifesciences.org/articles/04165.pdf. PubMed Central record: https://pmc.ncbi.nlm.nih.gov/articles/PMC4269833/.

This paper combines a thin-film active chiral-fluid model with experiments in the nematode embryo. It reports that the actomyosin cortex produces active chiral torques and counter-rotating cortical flows. These flows depend on myosin activity and can be altered by mild changes to Rho-pathway signaling.

At the four-cell stage, chiral cortical flow accompanies the asymmetric skewing of the ABa and ABp cells. Weak perturbation of the Rho pathway changes both the flow magnitude and the degree of skew:

| Condition | ABa skew angle | Relative to control mean |
|---|---:|---:|
| Non-RNAi control | 23.6° ± 3.7° | Reference |
| `ect-2` RNAi | 15.8° ± 4.9° | About 33% lower |
| `rga-3` RNAi | 37.8° ± 6.1° | About 60% higher |

The percentages are simple comparisons of the reported group means, not separately reported effect estimates. The authors also report corresponding changes in counter-rotating cortical-flow velocity. The perturbations therefore connect the magnitude of active torque/cortical flow with the magnitude of the four-cell skew event.

**Why this is important:** unlike Tee’s cultured fibroblast system, this study directly links actomyosin-generated chiral flow to a defined embryonic left–right symmetry-breaking event. But the physical architecture differs: it is a contractile cortical layer generating active torque and counter-rotating flow, not a radial/transverse stress-fibre network.

This is a direct example of actomyosin-based developmental laterality, not evidence that the Tee mechanism is universal.

## 4. Drosophila — Myo1D, planar cell chirality, and organ morphogenesis

### Myo31DF/Myo1D and visceral handedness

**Primary source:** Shunya Hozumi et al., “An unconventional myosin in Drosophila reverses the default handedness in visceral organs,” *Nature* 440 (2006), 798–802. DOI: https://doi.org/10.1038/nature04625. PubMed record: https://pubmed.ncbi.nlm.nih.gov/16598258/.

Drosophila Myo31DF encodes an unconventional type-I myosin commonly referred to in this literature as Myo1D/Myosin ID. Loss of Myo31DF reverses, rather than simply randomizes, the handedness of the embryonic gut and adult visceral structures including gut and testes. Myo31DF is required in the embryonic hindgut epithelium, and disruption of actin filaments in that epithelium randomizes gut handedness. The result establishes a requirement for an actin-associated motor in this invertebrate laterality system.

The organ and tissue details matter: Myo1D is not merely a motor that twists a pre-existing organ. It acts before or during the relevant laterality program and participates in establishing the handed developmental information.

### Planar cell-shape chirality

**Primary source:** Kiichiro Taniguchi et al., “Chirality in planar cell shape contributes to left-right asymmetric epithelial morphogenesis,” *Science* 333 (2011), 339–341. DOI: https://doi.org/10.1126/science.1200940. PubMed record: https://pubmed.ncbi.nlm.nih.gov/21764746/.

The hindgut epithelium exhibits planar cell-shape chirality (PCC): individual epithelial cells adopt a handed shape within the plane of the tissue. The study links this planar chirality to directional rotation of the hindgut epithelial tube. DE-cadherin localization is asymmetric at cell boundaries, and Myosin ID/Myo1D affects PCC and the handed morphogenetic outcome.

### Cell-autonomous patterning with multicellular mechanics

**Primary source:** Ryo Hatori et al., “Left–right asymmetry is formed in individual cells by intrinsic cell chirality,” *Mechanisms of Development* 133 (2014), 146–162. DOI: https://doi.org/10.1016/j.mod.2014.04.002. PubMed record: https://pubmed.ncbi.nlm.nih.gov/24800645/.

Mosaic experiments indicate that Myo31DF-dependent cell-shape chirality is established within individual cells. However, mechanical interactions among neighboring cells contribute to formation or maintenance of the in-vivo pattern. The reported amount and static distribution of F-actin and Myosin II did not differ between wild-type and Myo31DF-mutant cells in the compared conditions, suggesting that static abundance alone does not account for the phenotype.

**Cross-scale interpretation:** the Drosophila evidence connects a Myo1D-dependent cellular handedness program to planar epithelial geometry and tissue/organ morphogenesis. It is not identical to Tee’s RF/TF pattern, and the fact that both systems involve actin organization does not make their molecular mechanisms equivalent.

## 5. Zebrafish — Myo1D / PCP / cilia orientation / organizer flow

**Primary source:** “Myosin1D is an evolutionarily conserved regulator of animal left–right asymmetry,” *Nature Communications* 9 (2018), 1942. DOI: https://doi.org/10.1038/s41467-018-04284-8. Open PMC record: https://pmc.ncbi.nlm.nih.gov/articles/PMC5955935/.

In zebrafish, Myo1D is required for normal function of the left–right organizer, Kupffer’s vesicle (KV). It affects orientation of organizer cilia and interacts functionally with the planar-cell-polarity component Vangl2. The balance of Myo1D and Vangl2 activities is important for cilia orientation, directional KV flow, and subsequent laterality. Mutant embryos show disordered or reduced flow and laterality phenotypes, while cilia motility itself was not the primary defect reported in the cited study.

This provides a concrete bridge from a Myo1D/PCP polarity system to a cilia-driven organizer mechanism. It is not a direct transfer of Tee’s fibre mechanics into the organizer: the observed downstream geometrical output is ciliary orientation and directional fluid flow.

A second, distinct zebrafish Myo1D function was reported in “Vertebrate myosin 1d regulates left–right organizer morphogenesis and laterality,” *Nature Communications* 9 (2018), 3381. DOI: https://doi.org/10.1038/s41467-018-05866-2. The study links Myo1d to Kupffer’s-vesicle morphogenesis and directed vacuolar trafficking; maternal-zygotic mutants can form small or dysmorphic KV lumens. This should not be collapsed into the cilia-orientation/Vangl2 result. It indicates that Myo1D may support organizer function through more than one cellular process.

**Important species boundary:** zebrafish data show a Myo1D/PCP contribution to cilia-driven organizer flow. The mouse-node mechanism reconstructed in BIO bite `n` is supported through its own ciliary tilt, directional-flow, sensory-cilia, Pkd2/calcium, Dand5, and Nodal evidence. The sources inspected here do not establish Myo1D as the upstream determinant of mouse nodal cilia orientation.

## 6. New 2026 bridge — Myo1D and Myo2 cooperate in circumferential actin flow

**Primary source:** Asuka Yamaguchi et al., “Myosin1D directs circumferential F-actin flow to define cell chirality,” *Journal of Cell Biology* 225(10), e202509125 (issue date 5 October 2026; published online 25 August 2026). DOI: https://doi.org/10.1083/jcb.202509125. Publisher record: https://rupress.org/jcb/article-abstract/225/10/e202509125/282976/Myosin1D-directs-circumferential-F-actin-flow-to. PubMed: https://pubmed.ncbi.nlm.nih.gov/42640253/.

The available publisher/PubMed abstract reports that:
- Drosophila Myo1D and Myo1C direct clockwise and counterclockwise circumferential F-actin flows, respectively, in macrophages, in collaboration with Myosin2 (Myo2).
- In an in-vitro motility assay, Myo1C produced random F-actin flow, whereas Myo1D triggered self-organization of F-actin into a rotating ring.
- The authors infer that Myo1D aligns actin filaments into a circular arrangement with barbed-end-to-pointed-end polarity in a preferred direction.
- Their proposed model assigns Myo1D a role in organizing the polarized F-actin structure and Myo2 a role in rotating it.

**Reading state:** abstract and bibliographic metadata inspected; full article text and figures were not accessible through the publisher page in this pass. Thus the specific experimental sequence, perturbation details, and figure-level limitations remain open.

**Why this changes the comparison:** the Tee paper’s myosin-IIA-driven TF motion and the newer Myo1D/Myo2 model are not the same architecture, but both involve a class-II myosin contributing contractile movement in a system whose directional organization depends on actin architecture. The newer study gives a molecular precedent in which a class-I myosin (Myo1D) helps organize actin polarity while a class-II myosin (Myo2) drives rotation. This is a more specific point of contact than the broad statement that both papers study actomyosin.

It does **not** show that Tee’s cultured fibroblasts use Myo1D, that Myo1D is the handedness-setting component in the Tee setup, or that macrophage circumferential flow is itself an embryonic laterality signal. Those would require direct evidence.

## 7. Mechanism comparison

| System | Chiral structure or variable | Force/motion source | Direct developmental relevance | What is actually shared |
|---|---|---|---|---|
| Tee fibroblasts | Radial/transverse fibre network; collective RF tilt and TF tangential drift | Myosin-IIA contractility, formin-dependent RF growth | Cell-intrinsic pattern only; embryo-level role proposed, not shown | Actin network geometry coupled to motor-driven motion |
| *C. elegans* embryo | Chiral actomyosin cortex and counter-rotating cortical flow | Active cortical torque dependent on myosin and Rho signaling | Direct contribution to the four-cell embryonic L–R skew event | Actomyosin force/torque generates a handed flow with developmental consequences |
| Drosophila hindgut | Myo1D-dependent planar cell-shape chirality and epithelial handedness | Myo1D/actin-dependent cell behavior plus cell-cell mechanics | Direct connection to gut handedness and epithelial morphogenesis | Intrinsic cell chirality is coupled to tissue-level mechanical organization |
| Zebrafish KV | Myo1D/PCP-dependent cilia orientation and organizer geometry | Ciliary motility generates flow; Myo1D/Vangl2 regulate the orientation/organizer system | Direct contribution to organizer flow and embryo laterality | Actin-associated motor/polarity machinery couples into a flow-generating organizer |
| Drosophila macrophages, 2026 | Circumferential F-actin flow and polarized actin ring | Myo1D/Myo1C collaborate with Myo2 | Cellular chirality result; organ-level role is proposed, not demonstrated by abstract alone | A class-I myosin can organize actin polarity while a class-II myosin drives rotation |

### Molecular distinction

Tee et al. identify **non-muscle myosin IIA**, a class-II myosin, as enriched in transverse fibres. Drosophila Myo31DF/Myo1D is an unconventional **class-I myosin**. They are not the same motor. The 2026 Yamaguchi abstract explicitly provides an example of a class-I Myo1D acting together with a class-II Myo2, showing that distinct myosin classes can cooperate within one chiral actin-flow system.

### Developmental distinction

- Tee: demonstrated cell-scale chirality in cultured fibroblasts.
- Naganathan: direct actomyosin-based embryonic symmetry-breaking movement in *C. elegans*.
- Drosophila: Myo1D-dependent cell chirality coupled to organ morphogenesis.
- Zebrafish: Myo1D/PCP affects ciliary orientation and organizer flow, linking cell polarity to cilia-mediated axis determination.
- Mouse: a well-supported nodal-cilia flow and mechanosensory pathway from BIO bite `n`; no evidence in this comparison establishes that Tee’s RF/TF mechanism or Drosophila Myo1D is the mouse node’s causal mechanism.

The commonality is therefore **structural and mechanistic at a family resemblance level**, not proof of one universal pathway. The components must remain attached to their specific system, tissue, developmental stage, and experimentally established link.

## 8. BIO / SAT-H(s)H interpretive boundary

For the current `χ` bite, the result is biological: it distinguishes mechanisms of cellular chirality and demonstrates where they do or do not connect to organismal laterality.

Under the stipulated SAT/H(s)H reading, each evolving cell, actin network, cortical flow, ciliary arrangement, organizer, and morphogenetic event can be represented as part of a W-extended developmental history. That representation can preserve temporal continuity and relations between successive configurations. It does not alter the biological evidence, supply an extra mechanism, or make the different systems equivalent.

The next bite `r` is where that worldtube mapping should be made explicitly. This note does not attempt to complete it.

## 9. Conclusions and open questions

### Supported conclusions

1. Cytoskeletal chirality can arise spontaneously from actin-network self-organization under suitable cell geometry.
2. Actomyosin-generated torque can directly participate in embryonic left–right symmetry breaking, as shown in *C. elegans*.
3. Myo1D-dependent intrinsic cell chirality is associated with invertebrate organ laterality and epithelial morphogenesis in Drosophila.
4. Myo1D/PCP can connect cytoskeletal polarity to cilia orientation and directional organizer flow in zebrafish.
5. A 2026 Drosophila macrophage study proposes a specific cooperative arrangement in which Myo1D organizes actin polarity and Myo2 drives circumferential rotation.

### Unresolved questions

- How much of the handedness-selection mechanism proposed by Tee et al. is attributable to actin helical polymerization, crosslinker geometry, or other factors?
- Does the 2026 Myo1D/Myo2 macrophage system share any molecular implementation with Tee’s fibroblast RF/TF network, beyond the broad division between actin organization and class-II-myosin-driven movement?
- Which Myo1D effects in zebrafish KV are primary for cilia orientation, and which arise indirectly through organizer lumen morphogenesis or trafficking?
- Which components of the Myo1D/PCP framework are conserved across vertebrates, and which are species-specific?
- What, if anything, does the worldtube representation make structurally explicit beyond the known time-dependent biological histories? This is reserved for `r`.

### Decision

**`χ` COMPLETE.** The evidence supports a family of distinct actomyosin/cytoskeletal chirality mechanisms, including two direct developmental examples and a clear Myo1D/PCP-to-cilia-flow intersection. It does not support a universal actomyosin pathway, and it does not connect Tee’s cultured-cell system directly to mouse nodal laterality.

## 10. Search route and provenance

The user’s preferred search hierarchy is Mysearch first, with Mersearch used to establish current queue/line status. Live archive documentation currently states that Mysearch remains an implementation scaffold, not a production-validated search service. Its implementation plan requires an independently addressable ingress, durable status/queue receipt, validated three-repository execution, provenance and result verification. Those conditions have not been met in the current records.

Mersearch stable 1.0 is therefore the documented operational archive-search route, but its four canonical request lanes were all occupied during this pass:
- Lane 1: `calder-angle-geometry-source-fidelity-20261102-1337`.
- Lane 2: `phy01-internal-first-worldtube-hinton-highercats-20261125-01`.
- Lane 3: `calder-iri-worldtube-geometry-fidelity-20261104t2230z-s0-001`.
- Lane 4: `kestrel-finite-core-geometry-source-fidelity-20261102-2200`.

All four live request files retained `status: requested`; request-specific manifest paths were not present at the time checked. No BIO request was submitted and no other lane was modified. The queue observation is an occupancy snapshot, not a claim about serial position within a single line.

GitHub code search was used only as a disclosed fallback to locate and inspect archive navigation/status records and the current Mersearch request files. It was not represented as a Mysearch or Mersearch scientific search result. Contemporary biological source discovery was performed through external literature search; original papers and source limitations are identified above.

## 11. Source inventory and reading status

| Source | Role in comparison | Reading status in this bite |
|---|---|---|
| Tee et al. 2015, *Nature Cell Biology*, DOI 10.1038/ncb3137 | Primary experimental paper on RF/TF actin-network self-organization | Full paper PDF read; PubMed abstract also checked |
| Naganathan et al. 2014, *eLife*, DOI 10.7554/eLife.04165 | Primary experimental/theoretical paper on actomyosin cortical torque and embryonic L–R skew | Abstract and primary result excerpts inspected; detailed full-text reading remains partial |
| Hozumi et al. 2006, *Nature*, DOI 10.1038/nature04625 | Primary Myo31DF/Myo1D visceral-organ laterality paper | Abstract and primary result summary inspected |
| Taniguchi et al. 2011, *Science*, DOI 10.1126/science.1200940 | Primary planar cell-shape chirality / epithelial morphogenesis paper | Abstract inspected |
| Hatori et al. 2014, *Mechanisms of Development*, DOI 10.1016/j.mod.2014.04.002 | Primary mosaic analysis of intrinsic cell chirality and cell-cell mechanics | Abstract/result summary inspected |
| Juan et al. 2018, *Nature Communications*, DOI 10.1038/s41467-018-04284-8 | Primary zebrafish Myo1D/PCP/cilia-orientation/KV-flow paper | Abstract and relevant source sections inspected through open PMC record |
| Saydmohammed et al. 2018, *Nature Communications*, DOI 10.1038/s41467-018-05866-2 | Primary Myo1D/KV morphogenesis and vacuolar-trafficking paper | Search-indexed results and abstract-level source inspected |
| Yamaguchi et al. 2026, *Journal of Cell Biology*, DOI 10.1083/jcb.202509125 | Primary, recent Myo1D/Myo1C/Myo2 circumferential actin-flow paper | Abstract and metadata inspected; full text/figures inaccessible in this pass |

---

**Lane boundary:** This is a BIO-lane comparative-history result stored in HSH_RESOURCES. It does not amend H(s)H BEDROCK, main theory, worker instructions, or the independent PHYS/GIT cursors.
