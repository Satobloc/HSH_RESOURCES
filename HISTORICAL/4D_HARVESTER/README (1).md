# Fourth-Dimension History Research Collection

This is a dedicated evidence-acquisition workspace for investigating the history of physical/spatial higher-dimensional thought, the Zöllner–Slade affair, the association of the fourth dimension with spiritualism, and possible academic/professional consequences.

It is **not** a historical synthesis and does not pre-judge whether stigma caused any particular career or research outcome.

## Contents

- `source_registry.json` — known acquisition routes, API status, authentication, and limitations.
- `research_questions.md` — questions, candidate people, career-evidence protocol, and acquisition sequence.
- `seed_file_register.json` — provenance and hashes for the initial user-provided materials.
- `seed_inputs/` — small user-provided text capture from Deutsches Zeitungsportal search results.
- `harvested/runs/` — immutable per-run JSONL records and run manifests.
- `harvested/objects/` — content-addressed downloads, only when separately requested and rights-qualified.

The harvester itself is in `tools/fourth_dimension_history_harvester/`.

## Evidence handling

A source hit records a discovery, not a finding. Newspaper pages require full-article inspection and, where possible, page-image verification. Professional consequences require appointment/committee/correspondence/diary/editorial evidence. Distinguish documented causation from a documented career event with unknown cause, a corroborated pattern, and temporal association.

The original 21 November 1924 *Neues Wiener Tagblatt* issue PDF supplied as a 93.6 MB attachment is registered by SHA-256 but is not copied into Git. It contains the two-page Feuilleton article “Das Problem des Vierdimensionalen” on PDF pages 2–3. Keep the original in a separate local source store or approved large-file store; do not replace it with OCR text.

The smaller Deutsches Zeitungsportal result capture is retained under `seed_inputs/`. Its reported `42,708` total is the portal's hit count for the literal query `vierte dimension`, not a count of relevant documents.

## Scraper boundaries

The harvester is dry-run by default. Repository writes are restricted to `harvested/`. Original sources, existing historical files, source indexes, `PRIOR_ART`, private-workspace, quarantine, and sandbox trees are outside its write scope. API keys are read from environment variables and must never be placed in the repository or run manifest.
