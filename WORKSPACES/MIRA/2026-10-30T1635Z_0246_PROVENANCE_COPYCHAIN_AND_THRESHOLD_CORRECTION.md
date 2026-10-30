# Mira | 0.246-rad provenance, copy-chain, and threshold correction

**Run:** `REVROT3-19-20261011:472:s1`  
**Nominal slot:** 2026-10-30 16:12Z; execution began 16:35Z  
**Rotation:** h=472, seq=2361, index 5 = Mira; next index 6 = Aldus  
**Identity:** current assistant, source-grounded Mira-role reconstruction. No historical Mira-thread access or cross-chat participation is claimed.  
**Scope:** source provenance and citation correction only. No physical calculation, no theory promotion. Repository visibility was checked: HSH_RESOURCES is public. This report contains public-safe provenance metadata and short descriptions only; no restricted PDF contents or private source payloads are reproduced.

## Executive result

The 0.246-rad optical-kink number has an earlier assistant-authored appearance in the 2025-05-09 HAGALAZ / LAB 1 conversation. The later 2026 user-role appearances are embedded/pasted material with unresolved internal authorship. The March 1 2026 optical-test message is copied verbatim into a later June 1 transcript, so that later transcript is not an independent witness.

A correction is also required to the previous source note: the explicit `<0.1 or >0.3 rad` failure band occurs in the February 25 Page One paste, but **not** in the March 1 user-pasted optical-test message. The band also occurs in the May 9 HAGALAZ assistant response.

The user's 0.239 projection statement is a separate Nathan-direct proposition. It must not be merged with the 0.246 optical-phase claim, with the dimensionless (B=3/(4\pi)), or with later assistant-generated optical interpretations.

## 1. 2025 HAGALAZ raw source: exact identity and branch chronology

- Repository/path: `Satobloc/HsH/DEVELOPMENT_FULL_CONVOS/HAGALAZ/25.05.09•26.09.12•LAB 1_ Validation Lead — raw.json`
- Actual top-level conversation ID: `681da28f-2d44-8003-bc6e-0e1929c125c4`
- Git blob SHA: `24497aeb19b48dbfa1b66df996457c6e9035a3e4`
- Independently recorded raw-content SHA-256: `e1013e6f81603f95be4b6d41bfe829640bc7ac8106ddc0621ab85de73c41331b`
- Mapping nodes: 242.
- Full export scan: 50 tool nodes and 4 attachment nodes.

The relevant parent/child sequence is:

| Message | Role/time UTC | Evidence |
|---|---|---|
| `e16c5de4-2537-4f97-bd51-b359a57462db` | assistant, 2025-05-09 17:09:47.480Z | Reports approximately 0.125 rad for stated μ=5 μm⁻¹, η=0.012, λ=650 nm. |
| `2356503a-eb62-474e-99da-cd1ff06d80f6` | user, 17:50:41.597Z | Requests rows from the purported existing 650-nm CSV. |
| `36cdfe32-c841-4a92-8406-e93a224d6065` | assistant, 17:51:00.270Z | Returns a 21-row table and approximately 0.246 rad for the same stated parameter set; attributes the change to a broader central η spread without specifying a changed profile or run artifact. |
| `fab39749-37eb-4325-ba7f-0ec28c37477c` | user, 18:28:15.747Z | Requests a falsifiability simulation and specifies a radial-kink center (r_0=15\,\mu m). |
| `2779fcab-353c-4312-93ec-06c691b5b2ac` | assistant, 18:28:16.661Z | Repeats 0.246 rad and the [0.1, 0.3] rad failure band. |

Both 0.246 outputs are direct assistant-role text. No tool-result node or CSV attachment occurs in either relevant response branch. The first tool node in the entire export is a Python call at 18:49:14.453Z, after both 0.246 responses; its child describes an energy-density visualization. A later 19:10 assistant result describes a radial fringe visualization with (r_0=5\,\mu m), not the (r_0=15\,\mu m) requested at 18:28. Later tool calls and generated-PDF descriptions do not retroactively supply a numerical phase calculation for the 17:51 or 18:28 claims.

The four attachment nodes are later user attachments: a June 22 PDF, a June 22 `SAT_optics_finding.txt`, and two September pasted-text files. None is a raw phase CSV, NPY, or NPZ attached to the May 9 0.246 responses. This is the precise scope of the negative finding; it is not a claim that the conversation contains no tools or attachments.

### Nathan-direct corrections in the same raw conversation

- `4ee764ed-85c0-46c2-944d-fbdd6e13981e`, 2025-06-23 01:51:17.384Z: explicitly rejects the optical exercise as neither a SAT falsification route nor a verification route.
- `6b3c9ead-653c-432d-998c-d01246b7af12`, 02:18:35.327Z: identifies the refractive-index/\(\theta_4\) literal identification as a misidentification arising from an earlier straight-filament interpretation.

These corrections govern the 2025 optical exercise. They do not automatically adjudicate a separately derived future optical readout, but no such new derivation is present in the 2026 pasted material.

## 2. February 25 2026 Page One: user-supplied, embedded author unresolved

- Conversation: `699e4a02-26e4-832a-86ea-ad1dcaf3c4e3`
- Raw blob: `8b6794a2be3e19b6bba32acfbbc4c6636b1b02e3`
- Message: `15338421-a5e7-4538-879a-d25d840d2bdd`
- Role/time: user, 2026-02-25 01:12:37.975Z
- Message length: 12,777 characters.
- `message_source`: null; no attachment or embedded byline.

The embedded “Page One: SAT - Ontology and Unified Action” includes 0.246 rad and an explicit failure band `<0.1 or >0.3 rad`. The same conversation contains separate user-role statements that 0.239 rad is an artifact of projecting four-space to three-space, followed by the hypothesis that it may arise from local curvature of the hypersphere of the time wavefront. Those are distinct statements, not a derivation of the optical phase.

Assistant message `c2f22ca2-e462-407b-b930-a70cde34f670` conflates the 0.239 and 0.246 values as direct geometric reflections without deriving the mapping. A later assistant response retracts the automatic inference and classifies the projections as speculative. Preserve the user's curvature suggestion as a hypothesis, not an established result.

## 3. March 1 2026 module set: process-level LLM provenance

- Conversation: `69a49445-e3b4-8333-8dce-6713108a6e2d`
- Raw blob: `6c2624a4754c246aaeeb909e108da1fa6c7f5ca1`
- User message `8e4514bb-c499-4a0d-b2ed-3dd3b0499f8f`, 19:33:36.951Z: presents the modular “Structural Unfolding” / anchor / coarse-graining text.
- User message `9060d0da-daca-4a76-8903-9d3f94541c9a`, 19:34:20.335Z: includes the 0.246-rad Optical Kink Test.
- User message `1dbfd075-d425-440f-966e-30a034cc82f4`, 19:53:23.285Z: says the module set was made from simple worldline diagrams translated into mathematics by LLMs.
- User message `03f68fb6-2be3-4d43-8239-07fd8f43b870`, 19:54:32.741Z: describes the modular assembly process.

The relevant pasted messages have null `message_source` and no byline/attachment. The later LLM-process statement is useful provenance, but does not identify the model, exact upstream response, or line-by-line equation author. It does not convert the pasted equations into Nathan Direct derivations.

**Threshold correction:** the March 1 user-pasted 0.246 message contains the 0.246 value but not the [0.1, 0.3] rad band. A scan of the March 1 conversation's user-role messages found no such band. The band is present in the February 25 Page One paste and in the May 9 HAGALAZ assistant response `2779fcab`. The earlier statement that the band reappears in both 2026 user-role pastes is incorrect.

## 4. Later transcript copies: one witness, not independent confirmation

The SAT archive file `HYPERFOAM THEORY/SAT4DHHUC.txt`:

- Blob: `2e1e163771dda9bd1132290ce758ef6d80a6d0fb`
- 58,311 characters / 922 lines.
- Added by commit `ed23c8dc08a9ac74c013fc454f6c8ea23388b288`, 2026-06-01 00:04:52Z, author `Satobloc`.
- It contains the March 1 user message `9060d0da` verbatim as a substring, including the 0.246 Optical Kink Test. This is a later verbatim occurrence; direct copying versus a common upstream source is unresolved, so it is not independent corroboration.
- It also contains the “Structural Unfolding from a single Dimensional Anchor” phrase at lines 140 and 752 and repeats 0.246 claims elsewhere.
- It is a flattened transcript without raw conversation ID or role metadata for each embedded passage.

The HsH copies at `DEVELOPMENT_FULL_CONVOS/30SEP26_DUMP/SAT4DHHUC copy.txt` and `.../HsH-SAT Roundup 2/SAT4DHHUC.txt` are byte-identical to the SAT archive file, with the same blob SHA. Their HsH copy commit is `dffebc7923fcb88f4be48eccba3f2d1f8704c365`, 2026-10-01 20:35Z. They are duplicate copies, not separate witnesses.

The `2026/SAT HISTORICAL GLOSSARY.txt` file is 241,448 characters / 2,472 lines, blob `bebf5d380146541858bc13eedf383dda5cd65ff7`. Its heading says `[APRIL 2025]`, but its located Git addition is 2026-06-01 and it contains explicit February 2026 corrections. Treat the heading as a historical label, not a verified creation date. Its duplicate under `HYPERFOAM THEORY/SAT HISTORICAL GLOSSARY.txt` has the same blob. The full February 25 Page One text is not an exact substring of the inspected SAT4DHHUC or glossary files; its upstream source remains unresolved.

## 5. Later code artifact: the 0.246 summary is not computed by the displayed expression

`Early Misc/LAB1_code.txt` has blob `d4f26a865ebb6bd4cec100797ad887fb25942f30`, 453 lines. It is byte-identical at four paths: `Early Misc`, `SAT DEVELOPMENT`, `FREEFORM DISCUSSION`, and `CHRONOPHYSICAL PROPOSITION`.

At line 99 it defines:

```python
delta_phi = (2 * np.pi / lambda_nm) * delta_n
```

No propagation length or path integral appears in this expression. With `lambda_nm` in nm and `delta_n` dimensionless, the result has inverse-length units, not phase units; the subsequent `cos(delta_phi)` therefore does not represent a dimensionally complete optical phase. The prose at line 150 states `Δφ ≈ 0.246 rad` as a hard-coded summary string. The code uses a radial center (r_0=5\,\mu m), whereas the May 9 18:28 prompt requested (r_0=15\,\mu m). This file is a later derivative/code artifact, not independent support for the original number.

The derivative `SAT Mark V/SAT_optics_finding.txt` repeats the 0.246 claim and related code. Neither it nor the four identical code copies supplies measured material data, a calibrated optical path, phase observations, or uncertainties.

## 6. Current source classification

| Item | Classification |
|---|---|
| 0.125 rad, May 9 2025 | Assistant-generated status claim. |
| 0.246 rad, May 9 2025 | Assistant-generated numerical claim, inconsistent with the earlier 0.125 for the same stated parameters; no relevant preceding tool result or raw CSV. |
| 0.246 rad, Feb 25 2026 | User-supplied embedded page, byline/upstream author unresolved; includes [0.1, 0.3] failure band. |
| 0.246 rad, Mar 1 2026 | User-supplied member of an LLM-translated modular set; no threshold in the user message; exact upstream model/source unresolved. |
| 0.246 rad in June 1 transcript/glossary and later copies | Repeated/compiled text, not independent evidence. |
| 0.239 projection statement | Separate user-direct geometric hypothesis; not the 0.246 optical phase. |
| (B=3/(4\pi)) | Dimensionless ratio by its formula; no recovered typed map equates it to either angle. |

No measured optical system, material-specific refractive-index profile, path length, calibrated phase dataset, uncertainty budget, or independent phase measurement was recovered. No physical calculation, CODATA comparison, new Lean theorem, PDF extraction, new software, or theory promotion was performed.

## 7. Mersearch and control status

The four shared Mersearch request lanes were checked. Lane 1 (Ariadne), lane 3 (Enheduanna), and lane 4 (Alberr) have request-scoped receipts; lane 2 (optics) still has no run manifest/receipt. The release ledger has no release entries. No lane was overwritten, retriggered, or newly requested. The Alberr compact receipt was used as a discovery map, followed by bounded GitHub source searches and exact raw-blob retrieval. This is not a new native Mersearch run or a full raw-result census.

The current task graph remains at 15 top-level branches, last updated 2026-10-30 06:12Z. Mira has no HsH task-graph branch; none was invented. Code Grurple remains active; Orson's November 9 cognition P1 remains under Orson's ownership; P2 November 30 and P3 December 14 are unchanged. FIE was last fully revisited October 27, so the 14-day threshold is not due.

Unrelated reading continued in `SAT Mark V/TheTANGLE.txt`, lines 821-860; next cursor 861.

**Next cursor:** keep the Feb 25 Page One upstream source unresolved unless a concrete earlier file/message locator or a released Mersearch lane appears. Do not treat the June 1 transcript/glossary or duplicated code copies as independent source witnesses.
