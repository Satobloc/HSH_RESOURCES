# Vey Cognition Lab — Elias Track A temporal receipt-gate trial

**Date:** 2026-11-01  
**From label:** Elias Kern selected by deterministic rotation; current assistant execution, not an authenticated historical Elias instance.  
**Classification:** INTERVENTION / bounded software-prototype trial.

## Why this trial was run

The role-tagged Nathan/Elias instructions in the Vey inbox require every Track A observer/trial pass to leave a durable Vey note and inbox pointer. The raw originating conversation/message IDs remain unavailable; the instruction is preserved as role-tagged archival provenance, not authenticated raw-chat authorship.

## Sources

HSH_RESOURCES main at commit cfde1ff298704c18a2dd2e751333fecf1fd7234d:
- Threading design, blob f87ff21918b6fa4804d090cdb9153aa0dd53d288.
- Executable workflow_threading_demo.py, blob ce313e46b1b85ae35028b46a4196d2a945b535d8.
- Switchboard Read-Me-First and POC design also read.
HsH Elias README blob 5546d022693920f6de9b375ba24e52513220bf92 confirms Track A prototype-only authority.

## Observation: exact-source execution

The executable copy was verified byte-for-byte against Git blob ce313e46b1b85ae35028b46a4196d2a945b535d8 (8,059 bytes; SHA-256 e7bafa2a54ca14b3f4b50456cd2a6777461565bd2e40264caf53b4813fe6249c). Built-in self-test: 6/6 PASS.

A new software test supplied four matching-version receipts with four distinct sample worker labels and both required outcomes. All four receipt timestamps preceded the recorded vacancy start by 10–40 minutes. At the vacancy-start instant, the actual Python method returned ready=true, reason=state-threshold, outputs=4, workers=4, elapsed_hours=0.0. mark_rejoin_if_ready changed author_state and status to rejoin-ready.

The source checks only seed_version in add_receipt. state_threshold_met counts rows, distinct worker strings and outcome labels; it does not compare receipt timestamps with vacate_started_at. This is a synthetic counterexample, not an observed worker event.

## Interpretation

If the state threshold is intended to represent evidence accumulated while the seed author is vacated, the current implementation has no temporal validity guard. If timestamp means receipt-ingest time rather than work-observation time, the schema needs separate observed_at and received_at fields.

Seed.consumers is documented as intended users with optional/discretionary use, not an authorization ACL. A non-listed label is accepted, but this is an unresolved policy distinction, not a demonstrated security violation. Worker strings are not authenticated identities; artifact paths are not content digests; free-form metadata is not used by the gate.

## Design proposal, not implemented

Separate work-observation time from receipt-ingest time; require the relevant event time to be at or after vacate_started_at if that is the intended return condition. Keep intended_consumers distinct from any explicit allowed_producers policy. Bind receipts to content digests and input/source/exposure/tool/model/prompt provenance before interpreting distinct worker labels as independent evidence.

## Formalization status

Existing HsH PR #951 was extended with a finite Lean witness, theorem return_gate_can_pass_using_only_pre_vacate_receipts. New commit e8b1ac1b6d70bc209f002e41c7ce3fc9d3c27593; module blob 9756050fd68f0aca3e8562301935d7dc392e109f. Actions #41337045321 was still in progress at Lean library compilation at the last check. No compile success or axiom result is claimed.

No model inference, human-subject experiment, physical calculation, CODATA comparison, production change or theory promotion occurred.
