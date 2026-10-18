# Geographic pattern analysis: full-distribution protocol
Date: 2026-10-18
Authority: Nathan Direct clarification.

## Scope correction
The original inquiry about Virginia (Minnesota), Clio (Iowa), and Hagerstown (Maryland) was exploratory curiosity about unfamiliar places, **not** an instruction to center the research on those three towns. Do not prioritize, discount, or interpret a locality simply because it was mentioned first. Evaluate every location in the context of the **entire observed distribution**, and let comparisons identify the most informative patterns.

## Unit of analysis and baselines
- Retain the original CSV data and nested country/state/city hierarchy, distinguishing total plays/engagement units from unique persons until platform metadata settles the metric.
- Construct a reproducible full-city/state/country table. Deduplicate by reporting source identity and avoid summing hierarchical percentages.
- Group localities into appropriate metropolitan/commuting regions; identify geolocation infrastructure artifacts separately (e.g., Ashburn).
- Compare against matched English-language podcast audience geography by platform and metric when available. Record source coverage and uncertainty. Use population-adjusted proxies only as explicitly provisional substitutes.
- Score research/university/biomedical activity, STEM employment, manufacturing/industry, technology, services, urbanicity, and distribution/network effects. Include negative controls and regions that appear underrepresented.
- Test model improvement of employment/R&D features beyond metro population, podcast propensity, home-region affinity, and geolocation uncertainty.
- Apply transparent small-sample uncertainty and multiple-comparison safeguards. Do not infer the identity or professional role of an individual listener.

## Priority policy
Rank candidate regions from the data using effect size, reporting-unit count, baseline deviation, geographic clustering, and potential measurement artifacts. The three originally noted towns remain eligible only under the same rules as all other locations.

## Current dataset
The verified single-folder consolidation is `EXPOSURE_STATS/AUDIENCE_METRICS/audience_metrics_complete.json` (84 CSVs). The separate cross-repository discovery catalogue requires an independent successful-run check before asserting three-repository completeness.
