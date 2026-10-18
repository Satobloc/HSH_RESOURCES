# Preliminary geographic reconstruction | 2026-10-18

**Scope:** The New Physics, original audience-metrics export only.  
**Source:** `EXPOSURE_STATS/AUDIENCE_METRICS/audience_metrics_complete.json` (84 source CSVs, 262 data rows, including 76 all-time geography exports).  
**Status:** Reconstructed counts are internally consistent with published percentages; original platform metric unit and whether reporting units equal unique people remain unverified.

## Denominators recovered

- All-time country-level: `N = 1461`. The 28 country/territory integer counts sum to 1461.
- United States country count: `1380 / 1461 = 94.45585215605749%`.
- US state-level geocoded denominator: `N = 1355`, internally reproduced by **all 32** state/DC percentages and summing to 1355, leaving 25 US country-level units without state assignment in this export.
- Recent 2026-09-19 to 2026-10-18 US state distribution: denominator consistent with `N = 38`, split Ohio 30, Virginia 5, Washington 2, New Jersey 1. The precise metric and independent population count require source context.

All percent-to-count reconstructions use `round(percent * denominator / 100)`, and must be checked for integral agreement and sum to denominator. A fractional reduction in percentage can admit multiples of an inferred denominator, so the integer interpretation is calibrated by the country total and nested hierarchy, not a claim of unique listeners.

## US states, reconstructed reporting units, all time

| State | Units |
| --- | ---: |
| Ohio | 837 |
| North Carolina | 165 |
| Utah | 81 |
| Arizona | 33 |
| Illinois | 24 |
| Pennsylvania | 24 |
| Mississippi | 23 |
| Washington | 22 |
| Oregon | 18 |
| Virginia | 18 |
| Texas | 14 |
| New Jersey | 14 |
| West Virginia | 12 |
| Massachusetts | 10 |
| New York | 9 |
| California | 8 |

Remaining states appear in the source file `TheNewPhysics_GeoLocationAllPlatforms_all-time (47).csv`, preserved losslessly in the consolidated dataset.

## The three named towns

| State | State units | City in matching drilldown | City % | Implied city units |
| --- | ---: | --- | ---: | ---: |
| Maryland | 2 | Hagerstown (file 70) | 100 | 2 |
| Iowa | 1 | Clio (file 72) | 100 | 1 |
| Minnesota | 1 | Virginia (file 74) | 100 | 1 |

These are location-attributed reporting units, not verified residents, listener identities, or unique individuals. Small-town appearance alone cannot establish statistically extraordinary audience penetration because geolocation inference, differential baselines, discovery paths, repeated activity, and selection bias all matter.

## Next questions

1. Recover geography drilldown ancestry for every country/state/city node and compare child sums to parent counts. The unnamed numbered files make correct parentage inference and source-provenance retention essential.
2. Distinguish episodes, plays/streams, unique listeners, downloads, and device-level events using original export metadata.
3. Separate all-time, last-30-day and Spotify-specific reporting windows and populations.
4. Compare non-Ohio locations to realistic podcast geographic baselines with small-sample uncertainty.
5. Do not merge metrics from other archives unless source fingerprint and metric equivalence are verified.

## Cross-repository compilation status

The source repository contains `tools/build_cross_archive_audience_catalog.py` and `.github/workflows/cross-archive-audience-catalog.yml`, configured to run daily. **As checked 2026-10-18, `EXPOSURE_STATS/AUDIENCE_METRICS/cross_archive_audience_catalog.json` is absent.** Thus completion/compilation across all three archives is NOT VERIFIED; configuration does not equal successful output. An attempt to query the Actions run collection through the GitHub connector was rejected as an unsupported endpoint; a public-web interface attempt also failed. Inspect the workflow execution via GitHub Actions and repair any failed job, then independently verify the file content/coverage before promoting the build status.

Do not claim cross-archive completeness yet.
