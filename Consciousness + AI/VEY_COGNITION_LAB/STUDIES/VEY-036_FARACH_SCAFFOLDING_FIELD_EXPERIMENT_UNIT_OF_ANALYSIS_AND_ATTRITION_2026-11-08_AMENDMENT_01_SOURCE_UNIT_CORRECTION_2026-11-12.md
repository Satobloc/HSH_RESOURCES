# VEY-036 Amendment 01 | Source-unit correction

Date: 2026-11-12
Parent note: `VEY-036_FARACH_SCAFFOLDING_FIELD_EXPERIMENT_UNIT_OF_ANALYSIS_AND_ATTRITION_2026-11-08.md`
Parent blob: `abdebf15771a4bcb53d987b54f127116431b89a9`
Status: **SOURCE-FIDELITY CORRECTION / ADDITIVE AMENDMENT**

## Correction

The parent note incorrectly states that the paper's §3.5 compliance paragraph labels 77 (Stranded), 51 (Parallel Play), and 37 (True Joint) as treatment “pairs.” The primary PDF does not say that. It explicitly calls these **treatment participants**.

The primary Microsoft Research PDF, arXiv:2604.08678v2 (19 April 2026), §3.5, pp. 13–14, states that 77 Stranded, 51 Parallel Play, and 37 True Joint treatment participants were classified from self-reported meeting behavior and Copilot usage patterns. Footnote 1 says the counts sum to 165 rather than 194 because 29 treatment participants (14.9%) did not complete the compliance items. Therefore:

- 77 + 51 + 37 = 165 classified treatment participants.
- 29 of 194 treatment participants had unclassified compliance status.
- These are participant counts, not pair counts.

A separate pair-level Task A table (Table 6, pp. 17–18) reports 62 treatment pairs with compliance data: 23 Stranded, 22 True Joint, and 17 Parallel Play. The paper says compliance data were available for 146 of 164 pairs with documents. This pair-level table is distinct from the participant-level counts in §3.5.

The conflation was in the parent audit, not in the paper. The paper should not be described as mislabeling 77/51/37 as pairs.

## Unit-of-analysis clarification

Task A is pair-level in assignment and output. Task B is an individual task and outcome, but participants remain nested within pair-level randomized arms; the paper reports CR2 standard errors clustered at pair level. “Individual-level Task B” should not be mistaken for 194 independent randomized units per arm.

## Scope and source

This correction does not change the reported outcome estimates, AM/PM session confound, differential attrition, LLM-grader calibration concerns, or the paper's classification as a human–AI workflow study rather than model-internal cognition or multi-agent consensus.

Primary source:
- Alex Farach, Alexia Cambon, Lev Tankelevitch, Connie Hsueh, and Rebecca Janssen, “Scaffolding Human–AI Collaboration: A Field Experiment on Behavioral Protocols and Cognitive Reframing,” arXiv:2604.08678v2, 19 April 2026.
- Official PDF: https://www.microsoft.com/en-us/research/wp-content/uploads/2026/04/Farach_etal_Publication.pdf
- arXiv record: https://arxiv.org/abs/2604.08678

No raw participant data were accessed. No new experiment was run. The parent note is preserved unchanged; this amendment corrects only the source-unit attribution.
