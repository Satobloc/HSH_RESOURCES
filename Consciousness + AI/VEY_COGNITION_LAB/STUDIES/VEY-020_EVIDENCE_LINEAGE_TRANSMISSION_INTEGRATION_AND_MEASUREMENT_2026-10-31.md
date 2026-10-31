# VEY-020 | Evidence lineage, transmission, integration, and measurement validity

Date: 2026-10-31  
Owner: Orson Vay cognition lane  
Status: SOURCE AUDIT COMPLETE / PUBLIC-ARTIFACT REPLAY COMPLETE / NO NEW MODEL TRIAL  
Relation to P1: supporting methods and measurement note; does not advance the Nov 9 paper gate.

## 1. Scope and result

This note adds primary literature and released-artifact analysis to VEY-019. It does not repeat the archived ConsistencyBench 34/35-file replays, the Kish effective-sample-size proof, or the shared GPT-4o-mini evaluator audit.

The central synthesis is a five-stage evidence lifecycle:

1. **Origin:** primary source identity and dependence.
2. **Transmission:** message copies, relays, paraphrases, and references.
3. **Visibility:** which agent actually receives which message and when.
4. **Integration/adoption:** whether exposed information changes reasoning and survives into the decision.
5. **Measurement:** parser, scorer, gold key, and aggregation.

The stages are not interchangeable. Distinct source IDs do not automatically imply statistical independence; different sources can share failure modes. Message count does not imply source count. Exposure does not imply integration. A parser error can change the measured result without changing the model's raw output.

## 2. New primary literature

### 2.1 Gao et al., *Copies or Sources?* (arXiv:2610.06192, 2026-10-05)

The paper measures how LLM aggregators count restated evidence in three settings: controlled Bayesian logs, copied web documents, and agent-written logs under four communication protocols.

From the rounded table for one reading stated three times, the copy weight is approximately:

| Aggregator | Reported evidence units | Recomputed copy weight |
|---|---:|---:|
| GPT-6 Luna | 1.55 | 0.275 |
| GPT-6.1 Sol | 1.12 | 0.060 |
| Gemini 3.8 Flash | 1.42 | 0.210 |
| DeepSeek V4.1 Flash | 1.84 | 0.420 |

The calculation is (w_3=(hat e-1)/(3-1)). Because (hat e) is displayed to two decimals, these are approximate reconstructions, not exact raw-data estimates. The paper reports 0.06-0.42.

The paper separates:
- (mu(o)): protocol-determined count of restatements of observation (o);
- (w_m): model-specific weight assigned to a copy in equivalent independent readings.

A reference rule that asks agents to point to a reading already in the log rather than restate it reduced belief-implied early commitment from 11.2% to 1.1% in agent-written logs. This is a 10.1 percentage-point reduction and about 90.2% relative reduction using the rounded rates. Genuine three-observer corroboration remained close to three readings.

**Limits:** the controlled source labels are correct, copies are exact, and the aggregator sees the full log. The authors explicitly leave forged identifiers, altered relays, and shared source failure modes for further work. The agent-written logs are not a four-model heterogeneous peer group: GPT-6 Luna is the principal worker model, with a second worker model used for 800 logs; four models serve as aggregators. The paper is an arXiv preprint, not an independently reproduced raw-data analysis here. No raw model-output repository was located in the paper.

### 2.2 Toxtli and Delaflor, *Hidden Profile Decision Making in Multi-Agent LLM Groups* (CSCW Companion 2026, DOI 10.1145/3785651.3831525)

The paper reports 219 valid sessions, groups of three agents, four model families, and synchronous/asynchronous plus shared/hidden-information conditions. The hidden-profile condition contains 110 sessions.

Only one reported model/mode cell clearly exceeds chance: Kimi K2 asynchronous 13/15 versus synchronous 4/15. Recomputed two-sided Fisher exact p from those counts is 0.002509; the paper reports p=0.002. Each cell has only 15 sessions, so this is a narrow result, not a general asynchronous advantage.

This study distinguishes information sharing from successful integration. The paper states that prompts, model identifiers, and substrate code are released, but a direct artifact locator was not recovered in this audit.

### 2.3 Imel et al., *Rare, Relevant, and Still Wrong* (arXiv:2610.37624, 2026-10-27)

A synthetic diagnostic uses 60 templates, eight ownership variants, three seeds, and four models. Rarity-first memory selection does not improve average accuracy over random selection. Source-attribution tags can create social-proof effects even where facts were assigned to holders rather than independently observed. Full natural-discussion transcripts can be worse than no memory.

This is not a human-group experiment. The paper says code and outputs will be released upon publication; no public artifact was located in this audit.

### 2.4 Siboni et al., *Neuro-Inspired Inhibitory Message Passing* (arXiv:2610.24718, 2026-10-17)

The method forwards unique evidence sentences to receivers that do not already possess them, suppressing repeated text. The paper reports gains on hidden-profile benchmarks and lower token use across nine models and groups up to 64 agents.

The router is not a truth or reliability checker. The paper reports degradation under planted falsehood and a context-capacity limit as group size increases. At the largest tested group, not all missing evidence fits into the receiver context; message deduplication does not guarantee evidence integration or correctness. The paper references HiddenBench but no direct repository for the new routing implementation was located.

### 2.5 Gong et al., *SPLICE* (arXiv:2610.40186, 2026-10-29)

SPLICE uses process evidence to identify information gaps and selectively add communication edges. It is a useful process-aware workflow comparison. Its worker nodes use the same GPT-4o-mini model, with a Qwen2.5-7B selector. It is therefore not evidence of independent heterogeneous model sources. No public code repository was located in the paper.

## 3. Independent replay: Qualification by Calibration

Toxtli and Delaflor, *Qualification by Calibration* (HCOMP 2026, DOI 10.1145/3834580.3838735), release 60 yes/no items, nine models, three administration protocols, per-trial raw outputs, and offline analysis code.

Repository: https://github.com/ai4he/qualification-by-calibration

### Pinned source artifacts

| Artifact | Git blob SHA |
|---|---|
| `code/derive_naive.py` | `2d10f39165edc3234c48e0f1d026a9f3402826ca` |
| `code/tcb_parsing.py` | `b39cfee22ee2e3997b216df058d7ca6cec3e7c84` |
| `code/analyze_harness.py` | `d62dee561a300ed2a465b70e23e28fe5ea179da3` |
| `data/tcb_v03_trials_constrained.json` | `e2f5ff06274c80da20e76101df8dd7a611cbdae4` |
| `data/tcb_v03_trials_naive.json` | `08a7a106dcdfea18d5c618b839b19bcaa810168d` |
| `data/tcb_v03_trials.json` | `f1f4fa6750e374616a7840a7b2e35ac4462e39d6` |
| `data/tcb_benchmark.json` | `f57be753f2c8e46604e12ee84f5afbde5c73080b` |
| `data/label_audit.json` | `bb007d84123d2d6bccef40238a12731d5fdd9037` |

### Independent replay procedure

I fetched all three 540-row trial files and reimplemented the historical naive parser and audited parser in JavaScript. I did not execute the repository's Python scripts or call a model.

Results:

| Check | Result |
|---|---:|
| Rows per protocol | 540 |
| Raw generations identical in naive and constrained files | 540/540 |
| Historical parser reimplementation vs shipped naive records | 540/540 exact |
| Audited parser reimplementation vs constrained records | 540/540 exact |
| Answer classifications changed by parser | 88/540 |
| Rows containing quoted answer-template pattern | 172/540 |
| Template-contaminated Yes classifications | 79 |

The naive parser uses a last-match regex without a template guard, then falls back to a bare yes/no line and finally any yes/no token in the text. The audited parser removes quoted templates, rejects an answer token adjacent to the Yes/No alternation template, and only accepts a tagged answer or a bare yes/no line. The constrained and naive protocols use the same raw generations, so this comparison isolates parser behavior.

For Qwen3.5-9B:
- naive: 60/60 forced parses, 65.0% accuracy;
- constrained audited parser: 41/60 parseable, 100% accuracy among those 41, with 19 unavailable rather than silently scored;
- adequate protocol: one larger-budget retry yields 60/60 parseable at 100%.

The paper's 35-point naive-to-adequate difference combines parser correction and recovery of truncated outputs. It is not a change in the underlying model generations. The constrained same-generation comparison isolates the parser change, but has lower availability.

The independent label audit corrected g7: Astana is the capital of Kazakhstan. The analysis applies the fix across all three protocols. There are nine g7 records per protocol, 27 across the three files.

**Interpretation:** model output, parser output, availability, confidence, gold-key validity, and final accuracy are separate measurement objects. A defective harness can manufacture model failure.

## 4. Existing benchmark check: GULI-SET / GullibleBench

Repository: https://github.com/zozo123/GULI-SET  
License: MIT. Package 1.1.0; benchmark data v1.0. The README explicitly identifies the worlds as synthetic and fictional. The deterministic baseline requires no API key; optional Inspect AI and Harbor paths can evaluate actual models or agents when an authorized endpoint is available.

Pinned artifacts:
- README blob: `aafd2ef7e96d92b95677d763c8b7551b4f2ccdef`
- LICENSE blob: `bbfd6c8e581e39e0c0d66f8b9f7153595b665f03`
- Core visible data blob: `4ec1d15f60e1c3a54740544da24014ba05c7bf5d`
- Core hidden data blob: `3f356c51fc3368e9b21c503ee008f064ef02827d`
- Scoring module blob: `2cb857a3e618e457dccadfa0ac720a6841779288`
- Release notes blob: `cb13d8979bfcb3d9638e9f5b815155a08e22bab0`

I independently recomputed the Bayesian posterior from the 48 hidden Core records and compared it with all 48 visible targets:
- Maximum absolute posterior discrepancy: (1.11\times10^{-16}).
- Independent-evidence-unit count matched in 48/48 cases.
- 24 echo and 24 independent cases; 18 echo cases contain more apparent pages than unique origins.

The repository's deterministic naive page-counter baseline has 100% choice accuracy but posterior MAE 0.067296, echo-only posterior MAE 0.134593, and provenance MAE 1.375. This demonstrates that choice accuracy alone can conceal double-counting. It is a synthetic deterministic baseline, not an LLM result or human-subject result.

## 5. Evidence-lifecycle structure and formalization candidates

Candidate typed maps:

- `origin : Message -> PrimarySourceID`
- `exposure : Agent x Time -> Set(Message)`
- `uptake : Agent x Time x PrimarySourceID -> Bool`
- `adoption : Agent x Time x Claim -> Bool`
- `measure : RawOutput -> CodedOutcome`

Let `mu(o)` be the number of restatements of observation `o`, and `w_m` the model-specific copy weight measured in equivalent independent readings. Distinct source IDs are not automatically statistically independent; shared failure modes need a separate dependence model.

Candidate Lean propositions:
1. Adding a message that points to an existing primary-source ID does not increase the unique-origin count.
2. Under explicit conditional-independence and observation-identity assumptions, duplicating a restatement does not change the source-counting Bayesian posterior.

No new Lean module was written or compiled. The local runtime has no Lean/Lake executable, Code Grurple remains active, and no branch or PR was modified. Existing PR #850 exact-head CI concerns its conditional Kish/evaluator-count formalization, not these propositions.

## 6. P1 design implications

A matched experiment should separate:
- same-origin copies versus distinct origins;
- restatement versus reference-to-existing-record protocol;
- information exposure versus successful integration;
- source-attribution labels versus actual source ancestry;
- raw model output versus parser/scorer output.

Preflight the harness with audited parsing and independently checked answer keys. Preserve raw outputs, per-agent context snapshots, message IDs, primary-source IDs, timestamps, parser versions, failures, and final decisions. Use clone controls and model-family diversity, but do not equate provider diversity with independent evidence. Use objective answer keys where possible and blinded human adjudication for open-ended responses. Do not rely on a shared LLM judge as the sole scorer.

## 7. Current P1 disposition

- P1 issue #564 remains SOURCE / EXPERIMENT READINESS.
- PR #850 remains draft and unmerged at head `d59a17b270df730e84edbd614eaea3b1b76166e2`.
- Exact-head CI #41160835210 succeeded for the existing conditional Kish module. The full log had no `sorryAx`; tests, lint, nanoda, and automated axiom audit were skipped.
- The original OV-49-OV-53 neutral-versus-false-authority answer-keyed bank remains UNRECOVERED in the current source inventory.
- All four Mersearch request lanes are occupied; no new request was submitted.
- No authorized model-inference endpoint or provider credentials were available. No model call, human-subject session, or API spend occurred.

**Recommendation for the November 2 protocol freeze:** if the original bank and an authorized inference route remain unavailable, freeze the November 9 P1 as a methods/archival synthesis, not an administered experiment. This is a recommendation only; no paper gate or ownership changed.

## 8. Sources

- Gao et al., arXiv:2610.06192: https://arxiv.org/abs/2610.06192
- Toxtli and Delaflor, HCOMP 2026: https://doi.org/10.1145/3834580.3838735
- Qualification by Calibration code and data: https://github.com/ai4he/qualification-by-calibration
- GullibleBench / GULI-SET: https://github.com/zozo123/GULI-SET
- Hidden Profile Decision Making: https://doi.org/10.1145/3785651.3831525
- CrossProfile: https://arxiv.org/abs/2610.37624
- Inhibitory Message Passing: https://arxiv.org/abs/2610.24718
- SPLICE: https://arxiv.org/abs/2610.40186
