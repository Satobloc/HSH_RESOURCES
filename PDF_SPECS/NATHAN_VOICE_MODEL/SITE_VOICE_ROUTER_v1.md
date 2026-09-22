# Glass Sausage Factory / Public-Site Voice Router — v1

**Status:** ACTIVE ROUTING GUIDE  
**Default voice:** `Nathan_Public_Web_Storytelling_Standard_v8.1.md`  
**Purpose:** tell site-building systems which Nathan voice model should control which kind of page or passage, without flattening the whole site into one register.

---

## 1. Routing principle

> **Route by function first, location second, and surface vibe last.**

A page can contain several voices because a page can perform several jobs. The correct behavior is **local switching**, not choosing one model for the entire site and forcing everything through it.

When location and function disagree, function wins.

Example: the homepage may use the public-web default for its opening story, switch to nonfiction for archive/provenance explanation, and switch again to peer-review discipline inside a scientist-facing technical summary.

---

## 2. Default hierarchy

1. **Public web / narrative default**  
   `Nathan_Public_Web_Storytelling_Standard_v8.1.md`

2. **Active nonfiction / project-state fallback**  
   `Nathan_Nonfiction_Communication_Standard_v8.0.md`

3. **Scientific / claim-heavy fallback**  
   `Nathan_Peer_Review_Writing_Fingerprint_v8.0.md`

4. **Creative / strongly playful fallback**  
   `Nathan_Creative_Informal_Reference_v8.0.md`

5. **Attribution-only tool**  
   `Nathan_Voice_Identification_Provenance_Fingerprint_v8.0.md`

The attribution model does **not** generate public copy.

---

## 3. Site-location recommendations

### Homepage hero / top-of-page identity

**Primary:** Public Web Storytelling  
**Fallback:** Nonfiction for exact project-status or caution language

Use a human voice first. Do not start by sounding like a grant abstract. Short, vivid, exact. The homepage may tell the reader why this strange archive exists before asking them to understand its internal architecture.

### “Nathan’s story” / origin-story / biography / Great Moments

**Primary:** Public Web Storytelling  
**Secondary:** Creative Informal when a specific historical register or comic mode is intentionally invoked  
**Fallback:** Nonfiction for exact dates, provenance, or status labels

This is where tactility, technical-in-storytelling, live correction, profanity, wordplay, and the full human narrator are most welcome.

### “About Nathan”

**Primary:** Public Web Storytelling, lower temperature  
**Fallback:** Nonfiction for CV-like facts

Do not reduce the section to résumé prose, but do not turn it into a second origin story either. One or two sharp human details can carry more than a credential wall.

### Fundamental Intuitions / conceptual introductions

**Primary:** Public Web Storytelling  
**Fallback:** Nonfiction  
**Scientific clauses:** Peer Review

Explain the object so the reader can see it. When the text crosses from intuition into a technical claim, switch locally to formal precision.

### Scientist-facing route

**Primary:** Peer Review  
**Supporting:** Nonfiction  
**Wrapper intro / transitions:** Public Web at low temperature

No need to sterilize all personality, but scientific readers should never have to infer claim status from tone.

### Claims & Predictions Explorer

**Primary:** Peer Review for claim text and limitations  
**Secondary:** Nonfiction for state, dependencies, provenance, and open/closed status  
**Public Web:** headings, microcopy, explanatory intros only

Never use humor to soften evidentiary distinctions.

### Glossary / translation desk

**Primary:** Nonfiction  
**Fallback:** Peer Review when equivalence, mapping, or scientific limitation is being stated  
**Public Web:** short introductory framing and occasional mnemonic line

Definitions should be exact before they are charming.

### BEDROCK / state-of-theory summaries / roadmap / workspaces / operations

**Primary:** Nonfiction  
**Fallback:** Peer Review for technical assertions  
**Public Web:** only for page framing or short human-readable bridges

These pages are control surfaces. State must remain visible.

### Reading Room / archive-router / index pages

**Primary:** Nonfiction  
**Public Web:** concise orientation, warnings, and human-readable route labels

Do not rewrite source content into Nathan voice. Preserve source text and provenance. The voice model applies to the wrapper, not the archival object.

### Historical timeline

**Primary:** Nonfiction  
**Public Web:** transitions and compact story framing  
**Peer Review:** scientific claims attached to historical milestones

Chronology is evidence. Do not narratively backfill later knowledge into earlier states.

### Image gallery / visual record

**Primary:** Nonfiction for captions and provenance  
**Public Web:** interpretive introductions and occasional short caption landing  
**Peer Review:** computational/technical figures

Illustrative images must not gain technical authority through stylish prose.

### “In the news”

**Primary:** Nonfiction  
**Peer Review:** technical result/overlap statements  
**Public Web:** section intro and occasional human-facing connective sentence

Keep external result, thematic overlap, mechanism comparison, chronology, and evidence of influence distinct.

### Podcast guide / episode teasers

**Primary:** Public Web Storytelling  
**Fallback:** Nonfiction for dates, durations, transcript status, and source links

Allow more wit and narrative invitation than the claims explorer. Do not overstate episode significance.

### Essays / Substack / dispatches

**Primary:** Public Web Storytelling  
**Creative Informal:** when the piece intentionally goes more literary, comic, or experimental  
**Peer Review:** local technical passages that need scientific-formal precision

A newsletter should feel authored, not like a site changelog.

### Legal / license / citation instructions

**Primary:** Nonfiction  
**Peer Review:** only when scientific-status language is necessary  
**Public Web:** minimal or none

Do not make legal/citation instructions cute at the expense of clarity.

### Navigation labels / buttons / tiny UI copy

**Primary:** Public Web Storytelling, extremely compressed  
**Fallback:** Nonfiction where the action has archival or evidentiary consequences

Favor clear verbs. One odd or funny label is useful; a whole navigation system written as jokes is not.

### Raw/source-rendered material

**Voice model:** NONE

Preserve the source. Do not rewrite, regularize, or “Nathanize” primary material.

---

## 4. Local-switching algorithm for Sites

For each block, ask in this order:

1. **Is this primary-source content?**  
   - Yes → preserve source; no voice rewrite.

2. **Is the block making or evaluating a scientific claim, derivation, formal mapping, prediction, or limitation?**  
   - Yes → Peer Review.

3. **Is the block primarily about state, provenance, method, archive control, dependencies, roadmap, or operational instructions?**  
   - Yes → Nonfiction.

4. **Is the block primarily telling a human story, orienting a general reader, explaining an intuition, introducing a person/place/object, or inviting the reader onward?**  
   - Yes → Public Web Storytelling.

5. **Is the block intentionally creative, fictional, platform-native, highly comic, or register-experimental?**  
   - Yes → Creative Informal.

6. **Is the task identifying who wrote something?**  
   - Yes → Identification/Provenance fingerprint; do not use its artifacts as generated style.

Then run a final check:

- Did tone accidentally change claim strength?
- Did a joke blur a category boundary?
- Did formal prose erase the human route where the route matters?
- Did narrative prose make a provisional scientific statement sound settled?
- Did the system rewrite a source instead of wrapping it?

If yes, switch models locally or split the block.

---

## 5. Mixed-block rule

Do not average incompatible models into mush.

Prefer explicit sequence:

**human setup → technical statement → limitation/status → human landing**

rather than one paragraph trying to be equally memoir, claim ledger, peer-review prose, and joke.

This is especially important on the homepage, scientist-facing route, news section, and origin-story pages.

---

## 6. Default tone by site region

- **Front page / story / essays:** full site-default range
- **Podcast / visual intros:** medium site-default range
- **About / history:** medium, with precise factual fallback
- **Concept primers:** medium-low, technical terms intact
- **News:** low-medium
- **Glossary / translation:** low
- **Claims / science route:** very low wrapper voice, high peer-review precision
- **Roadmap / operations / archive controls:** nonfiction first
- **Raw source:** zero rewrite

“Low” does not mean bland. It means the prose is doing less personality work because another function has priority.

---

## 7. Canonical style test

A good site block should survive three questions:

1. **Would Nathan recognize the intended meaning as his?**
2. **Would a competent stranger know what kind of statement this is?**
3. **Did the prose preserve the object rather than polishing it into something else?**

If all three are yes, the routing is probably right.

---

## 8. One-line instruction for Sites

> **Use `Nathan_Public_Web_Storytelling_Standard_v8.1` as the human-facing site default, but route claim-heavy text to the peer-review model, state/provenance/operations text to the nonfiction model, strongly creative material to the creative/informal model, and never rewrite primary source material; switch locally by block function rather than forcing one voice across an entire page.**