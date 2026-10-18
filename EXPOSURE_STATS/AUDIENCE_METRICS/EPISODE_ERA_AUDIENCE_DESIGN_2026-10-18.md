# Episode-era stratification for podcast audience geography
Date: 2026-10-18. Working analysis plan, not a causal inference.

## Verified archive surfaces
- Spotify ranking export: `EXPOSURE_STATS/PODCAST_EPs/DebatingA.I.OnScience_EpisodeRankings_all-time.csv` contains episode title, streams/downloads, publish date, rank and URI. Source was read directly.
- Cross-repository podcast registry: `EXPOSURE_STATS/PODCAST_GUIDE/EPISODES.csv`, `EPISODES.json`, `ANALYTICS_INVENTORY.csv`, `MANIFEST.json` and README. The existing builder `tools/build_cross_repo_podcast_guide.py` scans HSH_RESOURCES, HsH and the historical archive.
- `tools/update_cross_podcast_titles.py` populates chronological title rows in `EXPOSURE_STATS/CROSS_MASTER_CHRONOLOGY.md`.
- User's requested transition concerns early philosophy, epistemology and AI/LLM consciousness episodes and a later research/physics-intensive programme. Precise structural boundary **not yet independently located**, so do not choose one silently.

## Initial observations (publish-date cohorts, not listening dates)
A direct parse of the Spotify all-time episode ranking export identified 290 ranked episode records, including anomalies with future release dates. Example early Feb 2025 titles: *Starting At the End*, *On Consciousness*, *AI On Its Own Consciousness*, *AI vs Human Consciousness*, and *Radical Meta-Skepticism*. Some physics/filament material appears already on 2025-02-02, including *What Is Thought Made Of? [Filament Unification Intro]*. By late 2025 titles increasingly include explicit physics, and 2026 contains a dense SAT/physics technical catalogue. Thus **a phased thematic mixture**, not necessarily a single binary switchover.
Anomalous future publish dates in the export (2028–2034 throwback/time-capsule entries) must be flagged rather than treated as actual chronology through October 2026.

## Required model
1. Join all episode URIs to transcript sources, platform rank metrics, duration and publication dates, preserving source confidence and ambiguous joins.
2. Label episodes with multiple independent, non-exclusive axes: philosophy/epistemology, LLM consciousness/AI, SAT theoretical physics, high-technical/derivational, popular science, creative/miscellaneous. Human-check representative borderline items; do not assign based only on episode titles where transcripts exist.
3. Detect temporal changes in category prevalence with moving windows or change-point analysis. Candidate transition dates are hypotheses subject to archived episode-list evidence and manual source verification.
4. Keep publish-date cohorts distinct from listening-date cohorts: lifetime plays by date of publication do **not** reveal when or where the plays occurred. Replays, recommendations and publication-age bias matter.
5. To test the demographic/geographic transition, request comparable time-stamped listener geography and, ideally, episode-by-geography metrics. The current audience-geography consolidation is mostly all-time marginals, so an early-vs-late *geographic audience shift cannot presently be inferred*.
6. Model podcast-listening baselines by era and specialty; compare ordinary English-language shows, philosophy/AI shows, technical physics shows. Include Ohio home/self-listening sensitivity, local-network exposure, and age of episode.

## Existing tools
Use the podcast-guide builder and neutral Spotify-title chronology before creating a parallel episode database. Cross-repository input manifest and reproducible joins are mandatory. PRIOR_ART boundaries remain respected.

Status: title export and guide machinery read; exact previously discussed 'turning point' file not conclusively identified; no geo-by-era inference made.

## Clarification: transition and future-dated records (Nathan Direct, 2026-10-18)
No separate 'turning point document' was asserted. The user meant the thematic turning point that emerges from examining the actual episode list. Detect it from the chronology and transcripts; do not search for or posit a special document. Future-dated throwback / return-visit episodes are intentionally scheduled or parked for future publication, not yet released; retain their metadata but **exclude dates after the observation cutoff from historical release and listening analyses**. Do not classify those planned dates as archival mistakes. The early philosophical/epistemological/LLM-consciousness and later technical physics categories overlap across the catalogue; treat transition date as an empirical estimate, not a presupposed single cutoff.

## Late-catalogue trust is endogenous to technical content (Nathan Direct, 2026-10-18)
At roughly episode 100 or 300, repeat listeners' trust in the show cannot be modeled as an alternative to selecting for technical subject matter: the trust itself may have formed because of the technicality. Analyze a temporal pathway such as technical content -> selection/retention -> accumulated familiarity or trust -> listening to more opaque titles. An apparently title-insensitive established audience may therefore *strengthen*, not negate, the technical-interest selection hypothesis. Do not assume this causal pathway is proven; distinguish new and returning listeners if observable, and test temporal persistence across content difficulty. Avoid presenting content selection and loyalty as mutually exclusive hypotheses.
