# Nathan Voice / Communication Model — Index, Purpose, and Authority

**Purpose:** control which voice-model documents are used for which task. The directory now separates two operational goals that should not be conflated:

1. **write scientific prose for peer review in Nathan’s likely mature formal voice**;
2. **identify/provenance Nathan-authored material in mixed corpora** (with occasional communication/emulation use).

These purposes overlap in evidence but have different targets. The peer-review fingerprint should not imitate conversational artifacts merely because they are useful for identification.

---

## Operational priority

### PRIORITY 1 — PEER-REVIEW WRITING

`Nathan_Peer_Review_Writing_Fingerprint_v0.1.md`

- **Status:** PROVISIONAL ACTIVE FINGERPRINT
- **Purpose:** primary voice target for drafting, revising, or evaluating scientific manuscripts, formal theory papers, peer-review submissions, and manuscript-style technical prose
- **Use first when:** the question is “How should Nathan write this for scientific strangers / reviewers?”
- **Authority:** direct Nathan calibration + cross-register corpus + 1999 genuine formal-science sample + mature formal argumentative evidence + reduced-fluency/cross-language structural evidence
- **Important limitation:** no substantial modern peer-reviewed scientific manuscript written entirely by Nathan has yet served as final calibration
- **Supersedes for this purpose:** `Nathan_Formal_Scientific_Transfer_v0.1.md`

**Core rule:** the target is not “Nathan cleaned up.” It is Nathan’s communicative machinery operating under peer-review constraints.

### PRIORITY 2 — IDENTIFICATION / PROVENANCE

`Nathan_Voice_Identification_Provenance_Fingerprint_v0.1.md`

- **Status:** PROVISIONAL ACTIVE IDENTIFICATION FINGERPRINT
- **Purpose:** speaker/author attribution support in mixed SAT/H(s)H conversations and documents; distinguish likely Nathan material from assistant, NotebookLM, source text, transcription artifacts, and mixed passages
- **Secondary use:** occasional recognizable emulation/translation of difficult material for Nathan when that would aid communication
- **Use first when:** the question is “Is this Nathan?” / “Which parts are Nathan?” / “What production source best explains this wording?”
- **Not the default style source for peer-review writing.**

**Core rule:** identify deep structural behavior before surface mannerisms; ellipses, typos, spelling, coinages, and cadence are supporting evidence only after their production cause is understood.

---

## Supporting active documents

### General nonfiction / active repo communication

`Nathan_Nonfiction_Communication_Standard_v0.1.md`

- **Status:** PROVISIONAL ACTIVE DRAFT
- **Purpose:** communication with Nathan, repo coordination, directives, summaries, reconstruction planning, methodological discussion
- **Role:** supporting source-side communication standard; lower priority than the dedicated peer-review fingerprint for manuscript prose and lower priority than the identification fingerprint for provenance decisions

### Earlier formal transfer specification

`Nathan_Formal_Scientific_Transfer_v0.1.md`

- **Status:** SUPERSEDED FOR ACTIVE PEER-REVIEW VOICE; RETAINED AS DEVELOPMENT HISTORY / SUPPORTING TRANSFER NOTES
- **Purpose:** earlier protocol for converting Nathan’s nonfiction reasoning structure into formal scientific prose
- **Current role:** historical scaffold and supporting checklist only
- **Superseded by:** `Nathan_Peer_Review_Writing_Fingerprint_v0.1.md`
- **Reason:** the evidence base is now materially richer, including genuine formal-science writing, mature formal prose, direct Nathan metalinguistic calibration, and cross-language stress-test material

---

## Reference-only / creative + informal voice

`Nathan_Creative_Informal_Reference_v0.1.md`

- **Status:** REFERENCE ONLY
- **Purpose:** creative writing, informal voice emulation, narrative analysis, historical style comparison
- **Do not use as the primary style source for formal scientific writing or provenance attribution except where a cross-register structural habit is independently supported.**

---

## Legacy combined models

- `Nathan_Voice_Model_v7.md` — combined synthesis immediately preceding the operational split; retain for provenance/development history
- `Nathan_Voice_Model_v6.md`
- `Nathan_Voice_Model_v1.md`
- `NATHAN VOICE ANALYSIS.txt`

These files are not deleted or silently rewritten. They record how the model developed and may contain observations not yet promoted into an active-purpose fingerprint.

---

## Evidence / authority hierarchy

For voice-model interpretation, use roughly this order:

1. **newer direct Nathan correction or instruction**;
2. **direct Nathan explanation of his own wording / communicative intent**;
3. **verified mature Nathan-authored prose in a relevant genre**;
4. **verified Nathan-authored prose in adjacent genres, with genre limitations stated**;
5. **cross-register / cross-language evidence for deep structural habits**;
6. **assistant inference from mixed corpus**;
7. **surface-frequency observations without production provenance**.

Direct Nathan correction outranks all model inference.

A recurrent artifact is not automatically a voice preference. Always test whether it arose from deliberate wording, VTT/transcription, typo, automated generation, platform formatting, performed character voice, outside source material, or another model.

---

## Purpose firewall

### If the task is peer-review writing

Use, in order:

1. `Nathan_Peer_Review_Writing_Fingerprint_v0.1.md`
2. `Nathan_Nonfiction_Communication_Standard_v0.1.md` as supporting structure
3. older models only as provenance/evidence

Do **not** mechanically import identification markers such as typos, ellipsis density, dictation residue, or chat fragments.

### If the task is provenance / voice identification

Use, in order:

1. `Nathan_Voice_Identification_Provenance_Fingerprint_v0.1.md`
2. source metadata and causal-production evidence
3. legacy voice models / creative reference as supporting comparison where appropriate

Do **not** treat resemblance to the peer-review fingerprint as proof of Nathan authorship.

### If the task is creative or informal emulation

Use `Nathan_Creative_Informal_Reference_v0.1.md` plus the identification fingerprint’s cautions about register, production cause, and accidental artifacts.

---

## Version lifecycle

- `v0.x` — working/provisional; open to substantial revision
- `v1.0` — first Nathan-approved active standard for that specific purpose
- `v1.x` — backward-compatible clarification/addition
- `v2.0+` — material conceptual revision

A version number is purpose-specific. Peer-review and identification tracks may reach `v1.0` independently.

**Do not promote any document to `v1.0` merely because it has been committed or used successfully once. Explicit Nathan approval is required.**

---

## Current state

**Primary current development target:** peer-review writing fingerprint.  
**Secondary current development target:** voice identification / provenance fingerprint.  
**Supporting track:** general nonfiction communication.  
**Reference track:** creative/informal voice.  
**Legacy:** earlier combined and transfer models retained for auditability.
