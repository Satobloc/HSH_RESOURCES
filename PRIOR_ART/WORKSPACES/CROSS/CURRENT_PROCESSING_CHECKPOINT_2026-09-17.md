# Cross Processing Checkpoint — 2026-09-17

**Lane:** factual record / data compilation only. No causal or evidentiary judgment.

**Mandatory interlock:** before each collection bite, re-check `CONTINUITY.md` → `STRICT OPERATING INTERLOCK — evidence collection is not analysis`. Record what the source contains; do not decide what it supports, strengthens, weakens, confirms, implies, favors, undermines, establishes, or makes likely/unlikely. Work one bounded source/provenance target at a time.

## Durable ledgers

- `CROSS_SOURCE_GAPS.tsv` — source/provenance gaps and closed access problems.
- `CROSS_EXTERNAL_CHRONOLOGY.tsv` — external scientific chronology, dates and source metadata only.
- `CROSS_ARGUMENT_EVIDENCE_LEDGER.tsv.gz.b64` — compressed/base64 snapshot of the current full argument/evidence TSV.
  - Uncompressed local working file at snapshot time: `CROSS_ARGUMENT_EVIDENCE_LEDGER.tsv`
  - Size: 54,611 bytes
  - 84 lines including header = 83 records.
  - Restore: base64-decode, then gunzip.

## Feederized / directly accessible source state

- `Where is Velserbroek` raw conversation: source was named `.txt` but contents are ChatGPT JSON; byte-identical `.json` alias used for feeder parsing. Approximately 4.47 MB; 68 packets; `chatgpt-active-branch`; 485 mapping nodes / 423-message active branch.
- `ALDEN CROSS — raw (1).json`: approximately 13 MB; 186 packets.
- `ALDEN CROSS — raw (2).json`: Library raw-file materialization now succeeds. Local materialized path: `/mnt/data/cross_resume/ALDEN CROSS — raw (2).json`; size 13,613,028 bytes; parsed title `ALDEN CROSS`; 2,650 mapping nodes; 2,649 messages; 1,419 nodes on current active branch. Computed Git blob SHA `198f2acfab8930de315f6f84811efb1b94b2698d` exactly matches the previously recorded repository blob. The former oversize-access gap is CLOSED; direct bounded inspection is now permitted.
- Large-source feeder: `Satobloc/HsH/tools/large_document_feeder.py`.

## Current direct-source gaps / provenance state

See `CROSS_SOURCE_GAPS.tsv` for the detailed record.

1. **Google Trends normalization, 2026-06-05:** OPEN. Original Nathan correction turn and immediately following assistant reply remain unlocated. Existing later Cross/Geometry records are secondary to the missing original turn. Do not repeat the same broad phrase searches unless a new candidate source or exact locator surfaces.
2. **Spotify Search correction:** PARTIAL metadata gap. The direct source document is now located at `Satobloc/SAT_THEORY_ARCHIVE_2023-25/SAT PODCAST STATS/PODCAST - PODlod.txt`; it contains the exact Nathan correction wording. The document is compiled Q&A prose with `NATHAN:` labels, not a raw ChatGPT export, so it exposes no original authored-message ID/time. Earliest currently identified project attachment occurrence is 2026-06-01T09:45:58.033Z; do not treat that attachment time as authorship time. Repository path was uploaded 2026-09-04T20:20:18Z; likewise do not treat that upload time as authorship time.
3. **ALDEN CROSS — raw (2).json:** CLOSED as an access gap on 2026-09-17. Full raw file is materialized and byte-identity to the known repository blob has been verified.

## Controlling method

Packetize large source -> read bounded source sequence -> extract raw datum / claimant / argument / correction separately -> retain exact provenance -> deduplicate -> reconcile dates. Later summaries are not substitutes for directly available raw turns.

When a source is a compiled document rather than a raw conversation export, record that distinction explicitly. Do not invent direct-chat message metadata from a compiled `NATHAN:` transcript/Q&A block.

**Quarantine:** keep Cross material within `PRIOR_ART/WORKSPACES/CROSS/` unless Nathan explicitly releases it.
