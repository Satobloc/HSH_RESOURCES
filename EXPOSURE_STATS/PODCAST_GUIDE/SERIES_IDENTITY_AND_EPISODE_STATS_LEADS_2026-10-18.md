# Podcast series identity and per-episode analytics retrieval leads
Date: 2026-10-18. User-supplied series identification is authoritative for cataloguing.

## Series normalization
- **DAI / Debating AI / Debating A.I. / Debating A.I. On Science / Debating A.I. On the Future of Physics / The New Physics**: aliases and successive titles of the **same main podcast**. Episode identities use Spotify episode URI where present; do not split a rename into a separate show.
- **SAT Field Notebook / Scalar-Angular Theory: Field Notes**: **separate, smaller podcast**. Do not merge its plays, listeners, follower counts, rankings, or audience geography with the main podcast merely because subjects and creator overlap. Keep explicit series ID and optional related-concept links.
- Series identity on a particular imported file should still be checked where ambiguous. Preserve its raw title and historical display-name alongside canonical series ID.

## Confirmed source files with episode-level measurements
1. `Satobloc/HSH_RESOURCES/EXPOSURE_STATS/PODCAST_EPs/DebatingA.I.OnScience_EpisodeRankings_all-time.csv` contains 290 episode rows, titles, per-episode streams/downloads, publication date, ranking, Spotify URI. It is a **main-series** episode dataset.
2. `Satobloc/SAT_THEORY_ARCHIVE_2023-25/DEBATING AI PODCAST/DebatingA.I.OntheFutureofPhysics_TrendsChart_PlaysAndDownloads_First7Days.csv` contains per-episode first-seven-days plays/downloads and relative performance. Several near-duplicate versions also appear in `DEBATING AI PODCAST TRANSCRIPTS/` and `DEBATING AI TRANSCRIPTS CONT/`; fingerprint snapshots and deduplicate by data identity while preserving provenance.
3. `Satobloc/SAT_THEORY_ARCHIVE_2023-25/2026/SAT — PODCAST/Debating AI Stats.txt` (approximately 195k characters) is a TXT OCR transcription of Spotify screenshots containing per-episode data delineated by `| ### |`. Its opening section reports 1,306 show plays, 16 followers, and specific early episodes including *On Consciousness* with 32 plays, *The Equivalence Principle* with 26, and *Starting At the End* with 38. It is a historical snapshot, **not** necessarily comparable to later rankings without source dates and definitions.
4. `Satobloc/SAT_THEORY_ARCHIVE_2023-25/SAT PODCAST STATS/PODCAST - Podcast stats.txt` (approximately 191k characters) contains similar screenshot-derived text and episode statistics. Check likely duplicate/overlapping original before treating it as independent.
5. `Satobloc/SAT_THEORY_ARCHIVE_2023-25/2026/SAT — PODCAST/Debating AI Stats 2.txt` and `DEBATING AI PODCAST/SAT DAI — stats STAT_chunked.txt` are additional candidates for recovering disordered per-episode screenshot metrics.
6. `Satobloc/HSH_RESOURCES/EXPOSURE_STATS/PODCAST_GUIDE/` is the existing cross-repository episode registry with `EPISODES.csv`, `EPISODES.json`, `ANALYTICS_INVENTORY.csv`, `SOURCE_INVENTORY.csv`, and `MANIFEST.json`. Reuse it instead of inventing a competing index.

## Extraction discipline
- Separate series as above; preserve source repository, path, blob/content hash, snapshot capture date (or unknown), episode URI and title, publication date, measured interval, metric name, amount, and confidence/OCR reliability.
- Do not interpret early snapshot counts, all-time rankings and first-week counts as independent or additive if overlapping.
- Parse OCR `| ### |` episode boundaries, but independently check where the source notes say boundaries are unreliable. Do not treat explanatory prose about analytics as measured data.
- Future scheduled return-visit episodes are not published and should not enter observed release-period comparisons.
- Use resulting episode/time panel to model genre-transition audience behavior; a geo-by-episode cross-tab is still not established from the currently verified sources.
