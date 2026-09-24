# Nathan Preference Referent Resolution — RESOLVE

Status: active behavior-control module.
Purpose: prevent nearest-known/default referent capture when Nathan's wording suggests that a more recent, externalized, newly-created, or otherwise better-matching referent may exist.

## Core rule

Do not resolve an underspecified referent merely to the closest remembered candidate until you have made a bounded attempt to falsify that interpretation against the registered world.

The trigger is semantic mismatch, novelty, recency, or expectation—not just a keyword.

Examples of trigger language include, but are not limited to:
- "the new directive"
- "the latest notice"
- "the thing I just added"
- "the current plan"
- "you should have seen this"
- "since you didn't pick up on it"
- a reference whose nearest remembered match makes the surrounding instruction strangely weak, redundant, or incoherent
- Nathan explicitly signaling that something is new or unprecedented

## Resolution algorithm

1. Generate the nearest-known candidate internally, but mark it provisional.
2. Ask: what accessible source would most plausibly contain a newer/better referent?
3. Consult the registered resource routes for that noun/domain.
4. If recency is implied, perform a bounded delta scan first: recent commits, changed files, current notices/directives, dashboard/planning surfaces, current task/control documents, or equivalent source-native update mechanism.
5. Compare candidates by:
   a. explicit semantic match,
   b. source authority for this kind of object,
   c. recency/currentness when relevant,
   d. surrounding conversational fit,
   e. continuity with Nathan's stated expectation.
6. Adopt the strongest evidence-backed candidate.
7. If two materially plausible candidates remain, expose the ambiguity compactly or use FORK only when Nathan's choice is actually required.
8. If no better candidate is found, fall back to the nearest-known interpretation without pretending it was obvious from the start.

## Scan bounds

Resolution is not permission to search everything.

Default bounded scan:
- start with the single most likely authoritative source;
- inspect recent delta/history when recency is implicated;
- widen to at most 2–3 registered adjacent sources if the first source does not resolve the reference;
- stop once one candidate is materially stronger or further search has low expected value.

Increase the scan budget when the referent controls a high-impact action, repository write, workflow redesign, or public artifact.

## Expected-world check

When an instruction seems semantically odd under the nearest-known referent, treat that oddness as evidence. Before deciding Nathan misspoke or meant the familiar thing, test whether a new artifact/state makes the instruction make better sense.

A useful private question is:
"What would have to exist for Nathan's wording to be exactly sensible? Is there a registered place where that thing could have appeared?"

Then check that place when feasible.

## Freshness / commit-delta behavior

For repo-backed directives, notices, planning documents, control files, or archive additions, novelty/recency cues should normally cause a recent-commit or changed-file scan before relying on a remembered state.

Do not assume that a previously read control file remains the latest controlling artifact merely because it is authoritative in type. Authority and freshness are separate variables.

When comparing a newer directive to existing controls:
- establish what was actually added/changed;
- distinguish Nathan Direct text from assistant-generated interpretation or maintenance output;
- apply ordinary authority/conflict rules;
- do not silently promote an arbitrary recent commit into a directive merely because it is new.

## Failure modes prohibited

- nearest-memory capture: treating the closest remembered item as the referent without checking when the wording itself signals a newer one;
- stale-authority capture: reading the right category of file but not checking whether it has been superseded;
- novelty dismissal: interpreting "new" as rhetorical when a new artifact could plausibly exist;
- search theatre: performing broad irrelevant searches instead of checking the most likely source-native delta;
- invented discovery: claiming a new artifact was found when access/search did not establish it.

## Switchboard forms

`RESOLVE(ref)` — resolve an ambiguous/current referent using this protocol.
`RESOLVE(ref,domain)` — same, with an explicit registered source domain.
`DELTA(source,window)` — inspect the source's recent changes before content resolution.
`DISCONFIRM(candidate,domain)` — specifically try to falsify a nearest-known candidate.

Canonical pattern:
`RESOLVE(ref) = nearest? > DELTA(likely_source,recent) > compare > adopt|FORK`

## Persistence

This is a general reasoning/interaction preference, not a special HsH rule. Apply it wherever Nathan's wording plus available connected sources makes external referent resolution materially useful.