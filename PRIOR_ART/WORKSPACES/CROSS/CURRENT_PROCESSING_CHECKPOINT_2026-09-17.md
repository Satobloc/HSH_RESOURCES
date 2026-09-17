# Cross Processing Checkpoint — 2026-09-17

**Lane:** factual record / data compilation only. No causal or evidentiary judgment.

## Durable ledgers

- `CROSS_SOURCE_GAPS.tsv` — unresolved source/provenance gaps.
- `CROSS_EXTERNAL_CHRONOLOGY.tsv` — external scientific chronology, dates and source metadata only.
- `CROSS_ARGUMENT_EVIDENCE_LEDGER.tsv.gz.b64` — compressed/base64 snapshot of the current full argument/evidence TSV.
  - Uncompressed local working file at snapshot time: `CROSS_ARGUMENT_EVIDENCE_LEDGER.tsv`
  - Size: 54,611 bytes
  - 84 lines including header = 83 records.
  - Restore: base64-decode, then gunzip.

## Feederized source state

- `Where is Velserbroek` raw conversation: source was named `.txt` but contents are ChatGPT JSON; byte-identical `.json` alias used for feeder parsing. Approximately 4.47 MB; 68 packets; `chatgpt-active-branch`; 485 mapping nodes / 423-message active branch.
- `ALDEN CROSS — raw (1).json`: approximately 13 MB; 186 packets.
- Large-source feeder: `Satobloc/HsH/tools/large_document_feeder.py`.

## Current unresolved direct-source gaps

See `CROSS_SOURCE_GAPS.tsv`. Important current gaps:
1. Original 2026-06-05 Google Trends normalization turn.
2. Original Nathan Spotify-Search correction turn.
3. `ALDEN CROSS — raw (2).json`: canonical GitHub path and blob SHA known, but full fetch currently fails with `BUFFER_OVERFLOW_ERROR`; do not claim direct inspection.

## Controlling method

Packetize large source -> read bounded source sequence -> extract raw datum / claimant / argument / correction separately -> retain exact provenance -> deduplicate -> reconcile dates. Later summaries are not substitutes for directly available raw turns.

**Quarantine:** keep Cross material within `PRIOR_ART/WORKSPACES/CROSS/` unless Nathan explicitly releases it.
