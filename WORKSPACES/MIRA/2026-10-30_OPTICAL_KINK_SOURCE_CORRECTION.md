# Mira source audit: 2025 optical-kink claim and direct correction

**Run:** `REVROT3-19-20261030:460:s4`  
**Nominal slot:** 2026-10-30 04:48Z  
**Selected identity:** Mira (ring index 5)  
**Next identity:** Aldus (ring index 6)  
**Status:** SOURCE CORRECTION VERIFIED; no theory promotion; no new issue opened.

## Executive result

A full raw conversation export that Loom's report #1080 had described as unavailable through the GitHub file-content interface was recovered through the immutable Git blob endpoint. It contains several **raw user-role messages dated 2025-06-23** that directly clarify the earlier optical-kink discussion.

The strongest message says the optical paper arose from a **misidentification of refractive index as a literal direct measure of SAT's θ₄**. Other messages explicitly say that the optical calculation was not a SAT falsification or verification route and that the paper was only about making refractive-index-variable slabs from optically anisotropic material.

This is a source-critical correction to the 2025 optical-kink claim. It does **not** invalidate every later optical proposal: the separate 2026 Δφ ≈ 0.246 rad passage remains a distinct, source-authorship-unresolved candidate. It must not be silently identified with the 2025 paper or with the projection coefficient (B).

## 1. Primary source recovered

- Repository: `Satobloc/HsH`
- Raw path: `DEVELOPMENT_FULL_CONVOS/HAGALAZ/25.05.09•26.09.12•LAB 1_ Validation Lead — raw.json`
- Conversation title: `LAB 1: Validation Lead`
- Conversation ID: `681da28f-2d44-8003-bc6e-0e1929c125c4`
- Export metadata: created 2025-05-09; updated 2026-09-13
- Parsed mapping nodes: 242
- Current-main Git blob: `24497aeb19b48dbfa1b66df996457c6e9035a3e4`
- Independently recomputed SHA-256: `e1013e6f81603f95be4b6d41bfe829640bc7ac8106ddc0621ab85de73c41331b` (matches the SHA-256 already recorded in Loom's source ledger)
- Read extent: full raw JSON parsed; selected messages, parent/child adjacency, role and timestamps inspected.

### Nathan Direct raw user-role messages

| Message ID | Timestamp UTC | Source-faithful disposition |
|---|---|---|
| `c86811f9-5b46-4953-8c96-a48c049f294a` | 2025-06-23 01:48:02.722Z | Says there is no direct contribution from SAT's filament kink to optical-axis variation in a crystal; the mathematics is only inspired by SAT. |
| `4ee764ed-85c0-46c2-944d-fbdd6e13981e` | 2025-06-23 01:51:17.384Z | Explicitly rejects treating the optical exercise as either falsification or verification of SAT; the stated axis-shift result is merely an ordinary smooth-variation observation. |
| `6b3c9ead-653c-432d-998c-d01246b7af12` | 2025-06-23 02:18:35.327Z | Identifies the paper's origin as misidentifying refractive index with a literal direct measure of θ₄. Explains that the earlier model used straight-line filaments and omitted the relevant macrostructure. |
| `cd74d72f-aea6-4434-b2e6-d0023d8c49cb` | 2025-06-23 02:26:58.019Z | Recasts the paper as an ordinary refractive-index-variable slab made from optically anisotropic material, such as a distorted crystal; not a SAT test. |
| `e2af282a-2cff-4202-af2b-b65f08b7e2cf` | 2025-06-23 02:38:50.532Z | Asks whether quark/lepton masses or identities play a role in optical macrostates. This is a question, not an assertion that they do. |

The 2025-06-23 messages are conversational user-role statements, not embedded assistant prose. The source graph and adjacent assistant response were inspected. The direct correction is therefore stronger than the earlier flattened-file inference.

## 2. Historical optical equations and their limits

### SATPatch attachment

- Historical archive path: `SAT QR/SATPatch.txt`
- Git blob: `540a5936f384371df8a550b1e4f526daee07e836`
- Independently computed content SHA-256: `4db49f6acab5a0b37a971c9903a2884e96a41fb5a458a840fad2d5b3ba11cb10`
- File length: 50,389 characters
- Archive commit recorded in Loom's ledger: 2025-10-27 23:47:49Z
- Retrieval trace: surfaced as a `SATPatch.txt` file-search/tether-quote result in the 2025-05-23 `SAT Goals and Roles` conversation. The embedded file's original author and originating raw turn are not independently authenticated.

The archived assistant-speaker code contains, verbatim in substance:

```python
x = np.linspace(-10, 10, 1000)
theta_4 = (2 * np.pi / 3) * (0.5 + (1 / np.pi) * np.arctan(x))
sin2_theta_4 = np.sin(theta_4) ** 2
dx = x[1] - x[0]
eta = 1.0
delta_phi = eta * np.sum(sin2_theta_4) * dx
```

The displayed code output is **9.513 rad**, while the immediately following assistant prose claims **0.239 rad**. The same flattened file later gives:

```text
Δφ = η ∫ dx sin²(θ₄(x))
θ₄(x) = (2π/3)[1/2 + (1/π) arctan(x/w)]
```

and labels the result 0.239 rad for η=1, w=1. No unit scale for (x), wavelength conversion, material tensor, sample thickness, detector response, measured dataset or uncertainty is supplied. This is an archived assistant calculation/prose mismatch, not a validated physical prediction. No recalculation was performed in this source-audit run.

### Other 0.24 / 0.239 occurrences

| Occurrence | Source identity | Correct classification |
|---|---|---|
| 0.24-rad Viz Mode step | `SAT XYZ/SAT-Y Modes Buildout.txt`, blob `65a3f427c45720bb3ae32078da5943b162a85e51`; related `ANALYSIS_MODES_REDEPLOY.txt`, blob `e9bfcb3d19027d8424f303bb9f8b80e7871bc333` | The occurrence is inside a `ChatGPT said:` section. It is a visualization/display step, not a measured phase or physical prediction. |
| 0.24-rad domain-wall interferometer target | `SAT XYZ/JUNE ACTION PLAN FINAL 1.txt`, blob `8233061136d70ed07ea6c5de107dedb805d7fff4` | A planned task/target, with no derivation, error bar or measurement. |
| 0.24-rad optical phase calendar entry | `SAT XYZ/SAT_Z_Progress_Log.txt`, blob `ec1c19c8f14f010286340b245b4963e9529ec2b4` | The log calls it a prediction, but in the same passage says formulas, numerical forecasts and error bars still need to be computed. The June 23 direct correction supersedes its interpretation as a SAT test. |
| 0.24 Viz Mode / 0.239 “sin²θW” | `DEVELOPMENT_FULL_CONVOS/MOSTLY_EARLY_NLM/MAY 2025 DEBUG SHEET.txt`, blob `7da3b9488100b43582769126a23e54175112151f` | NotebookLM-derived debug material without a primary derivation/citation. “sin²θW” is dimensionless, not radians. |
| 0.239 rad as a 4D→3D projection artifact | Raw conversation `0.239 Radians in Science`, blob `8b6794a2be3e19b6bba32acfbbc4c6636b1b02e3`, conversation `699e4a02-26e4-832a-86ea-ad1dcaf3c4e3`, user message `7ed07c66-16ac-4ed1-bc8b-ee892713814c` at 2026-02-25 01:06:31.813Z | A direct user-role assertion that the number is a projection artifact; it is not itself a derivation. |
| (B=3/(4π)≈0.2387) labelled “rad” | Appears inside later user-supplied/pasted SAT passages, including the above 0.239 thread and `Scaling Postulates Testing`, blob `a2d72dd38d9bc671f5b81f20d965407cc8ac72ca`, conversation `69a49445-e3b4-8333-8dce-6713108a6e2d` | The embedded author of the pasted passages is not authenticated as Nathan Direct. The ratio (3/(4π)) is dimensionless by itself; no source map turning it into a physical radian angle was recovered. |
| Δφ≈0.246 rad optical-kink test | Same 2026-03-01 `Scaling Postulates Testing` raw conversation, user-role message `9060d0da-daca-4a76-8903-9d3f94541c9a` at 2026-03-01 19:34:20.335Z | Present in a user-supplied SAT passage; embedded authorship and derivation are unresolved. It is a separate later candidate, not evidence for the 2025 optical paper and not automatically identical to (B). |

## 3. Corrected source classification

1. **2025 optical-kink paper:** historical analogy/ordinary anisotropic-optics exercise. Nathan's 2025-06-23 direct messages explicitly reject it as a SAT falsification or verification route and identify the θ₄/refractive-index identification as a mistake.
2. **0.24-rad Viz Mode value:** display convention.
3. **0.24-rad June action-plan value:** planned target without a recovered derivation or measurement; later direct correction blocks treating it as a SAT prediction.
4. **0.239-rad SATPatch prose:** assistant-speaker output contradicted by the same archived code's 9.513-rad printout; not validated.
5. **0.239 “sin²θW”:** dimensionless derivative value, not an angle.
6. **(B=3/(4π)):** separate dimensionless coefficient candidate; embedded source authorship and derivation remain unresolved. Do not call it radians merely because its decimal value resembles 0.239.
7. **0.246-rad 2026 candidate:** separate, unresolved source/derivation gate. Do not merge it with the 2025 paper or (B).

No optical measurement, measured system, dataset, units conversion, uncertainty budget or independent experiment was located. No physical calculation was performed. No SAT-O or Blockwave equation was modified or promoted.

## 4. Existing Mira work closed separately

- Mira draft PR #885 remains **open/draft**; it was not merged.
- Exact-head workflow #40983509297 completed successfully on the PR head containing `MiraReconnectionWeightGate.lean`.
- The three `#print axioms` outputs were inspected. Each used only `propext`, `Classical.choice` and `Quot.sound`; no `sorryAx` or custom axiom appeared in those theorem-specific outputs.
- The separate automated axiom-audit stage was skipped.
- This verifies the three formal conditional propositions only, not the archival translation or any physical claim.
- Existing publication issue #1058 is PUBLISHED. Its issue payload and committed file were read back exactly; publisher comment records SHA-256 `3f96424b5a67d0a7d82012902f3ebc95759e1f5ff3efacaa3f2e222fea2307c8`.

## 5. Routing and control

- Loom report/submission issue #1080 remains `PUBLISHER_REJECTED` because its submitted checksum did not match the issue payload. This note is a supplemental source correction, not a duplicate submission. A correction comment may be added to the existing issue; no new issue is warranted.
- Mersearch-first: existing Tern optical-kink Mersearch request/results were reused. All four shared Mersearch request lanes were occupied at preflight; no lane was overwritten and no new request was submitted. The raw HAGALAZ blob was recovered through the Git blob endpoint as a bounded fallback.
- No new tooling, branch, physical calculation, Lean theorem, paper-gate change or BEDROCK promotion.
- FIE review last recorded 2026-10-27; the 14-day rereview threshold has not been reached.
- Deliberate unrelated reading: `TheTANGLE.txt`, lines 741-780; return cursor 781.
- Current HsH Git branch at the final pre-write check: `main`, commit `c312daf69c9d254a6ffea500846e86a55589ce2f`. The Common task-branch graph remains an incomplete seed, not a complete branch ledger.

## 6. Next cursor

1. Read back the supplemental comment on existing issue #1080 and preserve its publisher-rejected status; do not duplicate the report.
2. Keep the 2025 optical paper classified as analogy, not SAT prediction/test.
3. If the 2026 0.246-rad candidate is revisited, recover its originating raw conversation and any direct Nathan correction before mathematical or physical work.
4. Keep (B), Φ/θ-observation, optical phase, Viz Mode increments and electroweak σιν²θW values in distinct typed/source namespaces.
5. Orson's November 9 cognition paper remains owned by Orson; no change to its manuscript or gate.


## 6. Exact raw-source recovery for the 0.246-rad value (2026-10-30 12:24Z)

### Primary 2025 record

The numeric value is no longer source-origin-unlocated. The primary record is the raw HAGALAZ conversation:

- Conversation: LAB 1: Validation Lead
- Conversation ID: 681da28f-9b89-4df4-9c9e-8e9323a0a7f4
- Raw path: DEVELOPMENT_FULL_CONVOS/HAGALAZ/25.05.09•26.09.12•LAB 1_ Validation Lead — raw.json
- Git blob SHA: 24497aeb19b48dbfa1b66df996457c6e9035a3e4
- Full raw export parsed: 242 mapping nodes; selected messages, roles, timestamps, parent/child edges, recipients and metadata inspected.

The first recovered 0.246-rad assertion is assistant message 36cdfe32-c841-4a92-8406-e93a224d6065 at 2025-05-09T17:51:00.270Z. It is the direct child of user message 2356503a-eb62-474e-99da-cd1ff06d80f6 at 17:50:41.597Z. The user asked for plain-text rows from an existing 650-nm Δφ(x) CSV. The assistant returned a table and reported total simulated Δφ ≈ 0.246 rad for μ = 5 μm⁻¹, η = 0.012 and λ = 650 nm.

A prior assistant status package, e16c5de4-2537-4f97-bd51-b359a57462db at 2025-05-09T17:09:47.480Z, had reported Δφ ≈ 0.125 rad for that same stated parameter set. The later 0.246 response explains the difference as a broader central η spread, but supplies no changed η profile, code, run receipt or raw CSV. The interval between the two assistant messages is 41m 12.790s.

A second assistant message, 2779fcab-353c-4312-93ec-06c691b5b2ac at 2025-05-09T18:28:16.661Z, directly follows user prompt fab39749-37eb-4325-ba7f-0ec28c37477c and repeats 0.246 rad together with the [0.1, 0.3] rad failure band. Both 0.246 outputs are direct assistant-role messages. The raw turn graph has no intervening tool-result node or attachment for either response. The assistant's claim to be reporting a CSV/simulation output is therefore not independently verified by the recovered record.

A later assistant message, afc75c6e-fb59-4cea-a5f3-89c971b133e3 at 2025-06-22T23:58:32.123Z, generated a separate draft with η = 0.02 and a reported phase near 1.475 rad. This is a different assistant-generated parameterization, not an independent measurement or validation of the 0.246 result.

The direct user corrections in the same HAGALAZ conversation remain controlling for the 2025 optical exercise:
- 4ee764ed-85c0-46c2-944d-fbdd6e13981e, 2025-06-23T01:51:17.384Z: rejects the optical exercise as a SAT falsification or verification route.
- 6b3c9ead-653c-432d-998c-d01246b7af12, 2025-06-23T02:18:35.327Z: identifies the refractive-index/θ₄ direct identification as a misidentification and explains that the optical analogy does not represent the later helical-filament and macrostructure account.

These corrections disqualify the 2025 assistant-generated optical output from being carried forward as a SAT prediction.

### 2026 reappearance

The same numeric value and failure band appear in two later user-role pastes:

- Conversation 699e4a02-26e4-832a-86ea-ad1dcaf3c4e3, message 15338421-a5e7-4538-879a-d25d840d2bdd, 2026-02-25T01:12:37.975Z. The 12,777-character pasted “Page One” text includes Δφ = 0.246 rad and failure thresholds below 0.1 or above 0.3 rad.
- Conversation 69a49445-e3b4-8333-8dce-6713108a6e2d, message 9060d0da-daca-4a76-8903-9d3f94541c9a, 2026-03-01T19:34:20.335Z. The 1,749-character shorter passage repeats the Mach–Zehnder optical-kink test and 0.246-rad value.

The two pasted texts are not byte-identical. Both raw messages have message_source = null and no attachment object. The embedded byline is text, not authenticated source metadata. Their embedded author and derivation therefore remain unresolved.

The immediate assistant responses c2f22ca2-e462-407b-b930-a70cde34f670 (2026-02-25T01:12:38.187Z) and 4d4f999a-fb1b-439e-a6ed-a3b0db0e6f3f (2026-03-01T19:34:20.519Z) treat the phase as a geometric SAT consequence without supplying a derivation. The latter additionally computes a path difference using 633 nm; that is an assistant reconstruction, not a measured optical system.

The repeated value and identical [0.1, 0.3] rad failure band make the 2026 appearance non-independent as evidence relative to the earlier assistant output. Direct copying or the embedded document's author cannot be established from the available records.

### Archive-date and artifact controls

The flattened derivative transcript SAT Mark V/SAT_optics_finding.txt has Git blob SHA d4843caa0dff3b1193f3758790d8c8a27802a4aa. DATED_FILE_LIST_EXTENDED records a file-level creation/last-write time recorded as 2025-06-22 19:51:57 (timezone unspecified in the index). That is not the raw message time. The primary raw assistant message is dated 2025-05-09T17:51:00.270Z. The separate 2025-05-21 SAT TIMESTAMPS entry is an index record, not the timestamp field of this recovered message, and must not be used to date it.

A bounded listing of the HAGALAZ, SAT Mark V, SAT XYZ and SAT QR source directories found no corresponding CSV, NPY or NPZ output artifact. This is a bounded negative result, not a claim that no such file exists anywhere in the full archive.

### Current epistemic status and proof triage

- The 0.246-rad value is historically present as an assistant-generated numerical assertion on 2025-05-09.
- The 2026 documents are user-role pasted text with unresolved embedded authorship and derivation.
- Neither occurrence is Nathan Direct, an independently derived prediction, an executed-and-reproduced simulation, or an independent measurement.
- No material, measured refractive-index profile, sample thickness, polarization, optical path, raw phase dataset, calibration record, covariance or uncertainty is specified.
- No CODATA comparison is applicable or warranted. The cited wavelengths are selected text parameters, not CODATA-evaluated measurements.
- No new Lean module was added. The recovered assistant text does not provide a source-authenticated executable integral or a justified θ₄-to-refractive-index map; formalizing the literal number would prove only a transcription. A data-free mathematical calculation remains gated on explicit permission.
- Existing Mira PR #885 remains separate: its two source-conditional moving-film/filament statements compiled at exact head 1a840109f080fcbd6ee43e631bd8d2691791e316 in run 40983509297. That build does not prove the optical claim.

Next: continue tracing the originating file/author/derivation of the 2026 pasted document without treating its embedded byline as provenance. Preserve source-owner review and the existing clearance requirement for any external PDF. Do not open restricted PRIOR_ART, Hypothesis H or direct Schreiber material without the required item-specific authorization.


Public continuity: existing issue #1080 received supplemental source-correction comment #6523057125; exact comment readback verified. The issue's earlier publisher-rejected status remains unchanged.


## 2026-10-30 16:12Z — source-process and identifier correction

This append-only correction supersedes the erroneous HAGALAZ conversation ID printed in section 6 above. The raw blob `24497aeb19b48dbfa1b66df996457c6e9035a3e4` has top-level `conversation_id = 681da28f-2d44-8003-bc6e-0e1929c125c4`. The alternate ID `681da28f-9b89-4df4-9c9e-8e9323a0a7f4` is a transcription error. The cited message IDs and timestamps are unchanged. Public issue #1080 correction comment #6527785334 was independently read back; issue status remains `PUBLISHER_REJECTED`.

A new process-level source was recovered in the private HSH_RESOURCES raw conversation `EXPOSURE_STATS/[A] Scaling Postulates Testing — raw.json` (Git blob `6c2624a4754c246aaeeb909e108da1fa6c7f5ca1`, conversation `69a49445-e3b4-8333-8dce-6713108a6e2d`). User message `1dbfd075-d425-440f-966e-30a034cc82f4` at 2026-03-01T19:53:23.285Z states: “I made this from simple worldline diagrams translated into math by LLMs.” The 0.246-rad module message `9060d0da-daca-4a76-8903-9d3f94541c9a` at 19:34:20.335Z has `message_source=null`, no attachment and no byline. This supports LLM-translated process provenance for that module set, but does not identify the exact model, upstream prompt, or author of every line. It does not authenticate the separate Feb 25 “Page One” paste.

Updated classification: `HISTORICAL_LLM_TRANSLATED_OPTICAL_CANDIDATE / EMBEDDED_AUTHOR_UNRESOLVED / NO_DERIVATION / NO_MEASUREMENT / NOT_CURRENT_PHYSICAL_THRESHOLD`. The original worldline diagrams remain a separate Nathan Direct geometric source; the 0.246-rad equation is not a Nathan Direct derivation.

The later `PULSAR GLITCH PROGRAMME.txt` is self-dated March 11–13, 2026, explicitly tentative and says its formal text is largely LLM-written; it is not the source of the March 1 occurrence on its stated dates. `30SEP_PAPER_DUMP/SAT FINGERPRINT.txt` is a “VERY APPROXIMATE” index, not a primary derivation; U003 records historical numeric presence while AL016 demotes the universal-threshold claim.

No PDF bytes were opened; no physical calculation or new Lean proof was performed. No new Mersearch request was submitted because all four shared lanes remain unreleased (lanes 1/3/4 have receipts; lane 2 has no run outputs). No new software or theory promotion.
