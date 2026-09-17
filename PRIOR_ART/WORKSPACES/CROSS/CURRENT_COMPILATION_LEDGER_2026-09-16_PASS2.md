# Cross Current Compilation Ledger — Pass 2 — 2026-09-16

**Status:** working compilation; not conclusions  
**Lane:** Cross / quarantined  
**Purpose:** add newly inspected source-attribution, duplicate-control, and claim/hypothesis records without overwriting the first current ledger.

## Source-attribution controls verified

### SA01 — Four source classes
The current Cross source-attribution map distinguishes:
1. Nathan argument/question/correction;
2. LLM answer/hypothesis/narrative;
3. derivative summary / NotebookLM synthesis;
4. raw or near-raw analytics / external-source record.

Direct Nathan correction has priority for reconstructing Nathan's own position. Generated prose is not converted into Nathan's position merely because Nathan continued the conversation.

**Source:** `PRIOR_ART/WORKSPACES/CROSS/EXPOSURE_SOURCE_ATTRIBUTION_MAP.md`.

### SA02 — Blind-search role
The attribution map records a specific evidentiary distinction for blind/weakly guided search surveys: generated prose is not itself proof of field consensus, while the set of topics and sources surfaced by a weakly guided contemporary search remains a record of the publicly retrievable information environment under those prompts.

**Source:** same.

### SA03 — Duplicate controls
The following duplicate relationships are already recorded and should not be double-counted:
- `SAT RECON — Gg3.txt` and `SAT RECON — Goog.txt` are the same blob.
- `Debating  Listeners 2.txt` duplicates `Debating  LISTENERSHIP.txt`.
- `Debating AI Podcast.txt` duplicates `Debating AI Podcast Stats.txt`.

**Source:** `EXPOSURE_SOURCE_ATTRIBUTION_MAP.md`; `RECORD.md`.

### SA04 — Source-use classifications
Current classifications recorded in the Cross map:
- `PARADIGM - FALLOUT.txt`: primary for Nathan chronology/public-archive clarifications.
- `PARADIGM CHATTER [Blind Survey].txt`: primary for survey design; generated claims require source checking.
- `PARADIGM — Chatter.txt`: derivative/composite routing source unless unique Nathan turns are found.
- `SAT RECON — Gg1.txt`: generated calculation/reconstruction; low relevance to exposure arguments, potentially useful for dating claimed prediction/closure language.
- `SAT RECON — Gg2.txt`: generated reconstruction; direct Nathan turns, if any, must be separated from generated prose.
- `SAT RECON — Gg4.txt`: triaged generated search/reconstruction record; no explicit `NATHAN:` block located; see `SOURCE_TRIAGE_GG4_2026-09-17.md`.
- `SAT RECON — google4.txt`: triaged generated search/reconstruction record; substantially overlaps Gg4 and adds later search-answer material; see `SOURCE_TRIAGE_GOOGLE4_2026-09-17.md`.
- `SAT TO DO — Google py.txt`: triaged generated SAT Python simulation/audit bundle; not Google Trends provenance; see `SOURCE_TRIAGE_GOOGLE_PY_2026-09-17.md`.

---

## Nathan argument records already present but newly re-verified

### N22 — Podcast wayfinding enables topic/depth self-selection
**Claimant:** Nathan  
**Claim:** podcast visual/color/title organization was designed so listeners could select physics/science versus philosophy/consciousness material and anticipate heavier mathematical content.  
**Record status:** direct Nathan argument in `NATHAN_ARGUMENT_LEDGER.md`.

### N23 — Audience turnover across subject transition
**Claimant:** Nathan  
**Claim:** the shift from consciousness/epistemology into more science-based material likely drove off some of the earlier audience; the audience should not automatically be treated as one stable cohort evolving over time.  
**Record status:** direct Nathan argument in `NATHAN_ARGUMENT_LEDGER.md`.

### N24 — Podcast cadence gap tied to work shift
**Claimant:** Nathan  
**Claim:** a major podcast gap around late 2025 / early 2026 reflected attention moving into focused calculation and LLM-environment design as the science became more substantial to him.  
**Record status:** direct Nathan argument in `NATHAN_ARGUMENT_LEDGER.md`; exact full wording should be recovered from the source conversation when needed.

---

## Assistant/LLM reconstruction claims from `SAT RECON — Gg1.txt`

These are preserved as source claims only. They are not treated as validated physics and are not attributed to Nathan unless independently recovered from Nathan turns.

### R-GG1-01
**Claimant:** Assistant/LLM  
**Claim:** a 270° phase-step mechanism was said to follow from an A4 / quarter-turn holonomy construction.

### R-GG1-02
**Claimant:** Assistant/LLM  
**Claim:** a generated simulation was described as returning a 270° phase step and was labeled a PASS.

### R-GG1-03
**Claimant:** Assistant/LLM  
**Claim:** an asymmetric heat-capacity anomaly near a helium transition was proposed as a geometric consequence of the same holonomy construction.

### R-GG1-04
**Claimant:** Assistant/LLM  
**Claim:** a generated heat-capacity simulation was described as reproducing an asymmetric lambda-like peak and was labeled a PASS.

**Source handling note:** the source uses strong terms such as “proved,” “verified,” and “PASS”; those words are historical attributes of the generated answer, not Cross judgments.

---

## Assistant/LLM reconstruction claims from `SAT RECON — Gg2.txt`

### R-GG2-01 — electron anomalous magnetic moment
**Claimant:** Assistant/LLM  
**Claim:** the electron anomalous magnetic moment was proposed to arise from “timesheet nutation” / extra geometric path length of an electron helix.

### R-GG2-02 — numerical g-2 comparison
**Claimant:** Assistant/LLM  
**Claim:** the source gives a proposed SAT electron anomaly of approximately `0.00114942` against an empirical value of approximately `0.00115965`, and describes the sub-1% difference as evidence of “Constraint Rigidity.”

### R-GG2-03 — critical-velocity construction
**Claimant:** Assistant/LLM  
**Claim:** a critical velocity `v_crit = (3 / 4π)c ≈ 0.238732c` was asserted as a geometric invariant.

### R-GG2-04 — obscuration threshold
**Claimant:** Assistant/LLM  
**Claim:** the source associates the critical-velocity construction with an obscuration angle of `14.1° ≈ 0.246091 rad` and a proposed loss of ordinary electromagnetic visibility above the threshold.

### R-GG2-05 — macroscopic navigation extensions
**Claimant:** Assistant/LLM  
**Claim:** the same reconstruction extrapolates the SAT geometry into speculative spacecraft/navigation mechanisms including “time feathering,” a “dark matter vessel phase,” teleological pull, and a re-entry/topological phase condition.

**Source handling note:** these are generated reconstruction/speculation claims. They are useful for dating what claims existed in the archive, not as external evidence.

---

## Source-level Google Trends / search provenance status

### GT-PROV01
`SAT TO DO — Google py.txt` has now been directly triaged. It is a 33,610-byte generated SAT Python simulation/audit bundle containing numbered `Google Py` code blocks. Full-file inspection found no Google Trends query/output and no `Trends`, `pytrends`, `TrendReq`, or `interest_over_time` retrieval material. It is therefore not Google Trends provenance. See `SOURCE_TRIAGE_GOOGLE_PY_2026-09-17.md`.

### GT-PROV02
`SAT RECON — Gg4.txt` has now been directly triaged. It is a broad generated web/search trend survey plus later reconstruction, with no explicit `NATHAN:` speaker block located. It preserves generated candidate claims and source trails. See `SOURCE_TRIAGE_GG4_2026-09-17.md`.

### GT-PROV03
`SAT RECON — google4.txt` has now been directly triaged. It substantially reproduces Gg4 and continues with additional generated searches/reconstructions covering antecedents, worldline/equation material, SAT/Blockwave terminology, filament terminology, and a Nathan McKnight podcast-search conflict. No unique direct Nathan turn was identified. See `SOURCE_TRIAGE_GOOGLE4_2026-09-17.md`.

### GT-PROV04
Current direct GitHub code search for the literal control term `paraglider` and for several remembered Trends phrases returned no result. Absence from GitHub code search is therefore not being treated as absence from the raw conversations/screenshots.

### GT-PROV05
The `EXPOSURE_STATS/SAT_IMPACT/` directory contains repository image files `trends.PNG` and `trends2.PNG`. Their content has not yet been inspected in this pass. They are candidate direct visual-source records for the Google Trends provenance lane and should be handled as images rather than inferred from filenames alone.

---

## Work-record controls re-verified

### WR01
The Cross work record states that the current job is collection and chronology only until Nathan explicitly authorizes interpretation. It prohibits present causal/significance judgments, similarity scores, and inferences of influence/copying/convergence/awareness/priority/novelty/independence from the diffusion data.

### WR02
The same record confirms existing mechanical transcript artifacts:
- `CROSS_TRANSCRIPT_CATALOG.csv`
- `CROSS_TRANSCRIPT_KEYWORD_HITS.csv`
- `CROSS_TRANSCRIPT_KEYWORD_MATRIX.csv`
- `CROSS_TRANSCRIPT_KEYWORD_INDEX.md`

The record says the index reports 13 transcript-like files, 81 literal keyword phrases, and 342 episode-keyword hit rows. This is mechanical indexing only.

### WR03
Current Cross raw-conversation extraction remains incomplete. The feeder/chunking mechanism expected by Nathan has not yet been located by current GitHub code search under the literal term `feeder`; this is recorded as a retrieval/tooling gap, not evidence that no feeder exists.

---

## Next raw-compilation targets

1. Locate or recover the conversation feeder/chunker so large raw JSON exports can be inspected in bounded slices.
2. Recover the exact Google Trends visual-inspection turns, including chart settings, term groupings, normalization correction, controls, and Nathan/assistant turn sequence.
3. Inspect `EXPOSURE_STATS/SAT_IMPACT/trends.PNG` and `trends2.PNG` as a bounded image-source pair; record only visible chart metadata/terms/values and provenance.
4. Continue source-deduplication before counting repeated summaries or screenshots as independent evidence.

**Quarantine:** this pass remains inside `PRIOR_ART/WORKSPACES/CROSS/` unless Nathan explicitly releases it.
