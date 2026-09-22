# Open-Ended Document Probe / Triage / De-Reconstruction / Reconstruction

Status: seed spec for a standalone, document-dump-first workflow.

## Goal

As soon as a new document dump arrives, run a broad first-pass process that does **not** assume in advance what the documents are, what their internal structure is, what their importance is, or what the final reconstruction should look like.

The desired behavior is:

`probe -> triage -> first-try de/reconstruct -> editor-facing summary -> review queue`

The output should be useful immediately to an LLM or human editor, but should avoid hard conclusions where the evidence is still thin.

## Why FLC is a good baseline

The *Floating Liars' Club* scans are a useful "possibly difficult" benchmark because they combine:

- scanned/image-heavy PDFs;
- prose, illustration, page furniture and ads on the same pages;
- issue-level and story-level structures;
- design elements that may itself carry narrative/comic function;
- uncertain OCR quality;
- page-order / continuation / attribution questions;
- multiple contributors and roles;
- useful context distributed outside the scan itself.

A workflow that handles FLC sensibly should transfer well to many other mixed historical / creative / research document dumps without becoming FLC-specific.

## Operating posture

### Open-ended first
Do not begin by forcing files into a fixed taxonomy beyond basic media / format facts.

### Triage before exhaustive extraction
The first pass should identify what deserves deeper attention and why. It should not spend equal effort on every file.

### Deconstruct before reconstruct
First identify pieces and relations that appear to exist:
- files;
- pages;
- sections;
- repeated elements;
- names;
- titles;
- dates;
- visual clusters;
- likely continuities;
- possible duplicates / variants;
- cross-file and cross-archive references.

Only then propose larger units such as issues, stories, chapters, packets, timelines or editions.

### First-try reconstruction is provisional
The system may propose a best current reading of structure, ordering, boundaries or relationships, but must label it as a working reconstruction rather than a settled conclusion.

### Editor-facing output
The primary first-pass product is not a giant machine dump. It is a concise but substantive editorial orientation that tells the next reader:
- what seems to be here;
- how the material appears to be organized;
- what looks important or unusual;
- what remains ambiguous;
- what should be read next;
- which automatic inferences should not yet be trusted.

## Seed workflow

### 1. Intake / inventory
Record:
- file path / attachment identity;
- extension / media type;
- byte size;
- content hash where available;
- page count / dimensions where applicable;
- native-readable vs extraction/OCR-needed state.

Do not infer significance from filenames alone.

### 2. Probe
Take a bounded sample appropriate to the corpus:
- first / last pages;
- table-of-contents-like pages;
- visually atypical pages;
- random middle pages;
- high-text and high-image pages;
- duplicate / near-duplicate candidates;
- obvious headers, titles, bylines, dates and names.

The probe should be broad enough to discover the corpus's own structure before choosing deeper adapters.

### 3. Triage
Assign provisional work queues such as:
- likely key / central;
- structural / navigational;
- ordinary content;
- image-heavy / visual-analysis-needed;
- OCR-poor / manual-read-needed;
- duplicate / version-family;
- attribution / provenance question;
- ambiguous / unknown;
- likely low-priority for current goal.

These are workflow labels, not quality judgments.

### 4. Deconstruction pass
Build candidate components and links:
- page / section boundaries;
- title/byline pairs;
- repeated headers / footers / page furniture;
- visual-region clusters;
- illustrations / ads / tables / forms / diagrams;
- names / dates / locations / organizations;
- continuity links between pages;
- repeated phrases and motifs;
- source-to-derived text/image links.

### 5. First reconstruction pass
Attempt a minimal coherent model of the dump:
- likely top-level containers;
- likely ordering;
- likely subdocument boundaries;
- likely contributor / role relationships where supported;
- likely relationship among repeated elements;
- obvious missing or uncertain pieces.

Every inference should retain confidence and evidence locators.

### 6. Cross-archive probe
When useful, search all three project repositories for exact names, titles, phrases, dates and provenance clues before escalating ambiguity.

Use existing locator-aware retrieval machinery where possible. Cross-archive hits are contextual evidence candidates, not automatic overrides of the source dump.

### 7. Editor-facing summary
Produce a compact orientation with these sections:

#### What arrived
A descriptive inventory of the dump.

#### What it appears to contain
Current provisional structural reading.

#### Strong signals
Patterns supported by multiple pages/files or clear source evidence.

#### Weak / ambiguous signals
Things worth noticing but not yet concluding.

#### Difficult or unusual material
Pages / files that defeat ordinary extraction, segmentation or classification.

#### Suggested next reading / review order
A short queue, not an exhaustive to-do list.

#### Reconstruction sketch
A provisional map of how the pieces may fit together.

#### Do-not-conclude-yet
Explicit warning list for tempting but unsupported interpretations.

## Output contract

The first run should ideally emit:

1. machine-readable inventory / page manifest;
2. probe log with exact source locators;
3. triage queue;
4. provisional structure graph or table;
5. editor-facing summary;
6. unresolved questions / review queue.

The editor-facing summary should cite / link exact source locations wherever practical.

## Confidence / review language

Prefer:
- `observed`
- `strong candidate`
- `working reconstruction`
- `weak candidate`
- `unresolved`
- `manual review required`

Avoid language that turns a first-pass pattern into a historical, authorial, semantic or provenance fact.

## Automation boundary

Automation may:
- inventory;
- hash;
- extract;
- OCR;
- cluster;
- search;
- rank;
- detect repeated structure;
- nominate boundaries;
- propose relationships;
- summarize provisional findings.

Automation should not silently decide:
- authorship from style;
- intent;
- literary quality;
- definitive chronology from weak dating evidence;
- that visually similar items are the same object;
- that missing search results imply absence;
- that OCR wording is authoritative;
- that a plausible reconstruction is the only reconstruction.

## FLC benchmark questions

A baseline run on the FLC dump should be able to surface, without being told all of this in advance:

- that the files are periodical issues rather than independent story PDFs;
- that there are recurring contributors and roles;
- that page furniture / ads / illustrations matter structurally;
- that stories span multiple pages and may require boundary reconstruction;
- that some image-heavy pages deserve direct visual review;
- that the magazine has issue-level editorial / contents / contributor material;
- that a simple OCR-only representation would lose meaningful information;
- which pages / relationships are still uncertain.

It does **not** need to infer the full social history or authorial intentions on first pass.

## First implementation target

Keep the standalone prototype small:

1. point it at a folder / document dump;
2. build inventory + accessibility state;
3. sample/probe the corpus;
4. generate bounded automatic page/file descriptors;
5. run exact / structural search across the dump and, where configured, across the three archives;
6. create one provisional reconstruction table;
7. write one editor-facing summary plus review queue.

FLC can then be used as the initial difficult-case benchmark. The benchmark should measure whether the summary gives a new editor a useful mental map quickly, not whether the system reproduces every manual judgment.
