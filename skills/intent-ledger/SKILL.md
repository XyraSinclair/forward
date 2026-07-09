---
name: intent-ledger
description: Capture and compile a project's strategic intent from the stream of prompts, corrections, and decisions over time — deduplicating, weighting recent statements over old, and recording supersessions instead of silently forgetting. Use when bootstrapping .forward/intent.md, when intent seems contradictory or stale, or when the user's direction has shifted.
---

# Intent Ledger

A project's strategic intent doesn't arrive as a spec. It arrives as a stream:
prompts, voice notes, corrections mid-task, offhand asides, reversals. Left
uncompiled, this stream is noise — agents rediscover intent from scratch every
session, or worse, act on a stale reading. The ledger compiles the stream.

Lives at `.forward/intent.md`. Two concerns: the **compiled current view**
agents actually read (Mission, Flavor, Load-bearing intents, Current
directions, Limitations, Open questions — the headings under Format below)
and the **supersession trail** (what was overruled, by what, when).

## Compilation rules

1. **Latest wins on conflict.** When two statements disagree, the more recent
   one governs. But the loser is moved to Supersessions with a date and a
   one-line note — never silently deleted. Superseded intent is information:
   it maps how the human's thinking moved and prevents re-proposing rejected
   directions.
2. **Dedup by meaning, not wording.** The same intent stated five ways is one
   entry, phrased once, well. Prefer the human's own vocabulary when it's
   distinctive — flavor words are intent too.
3. **Weight by recency and repetition.** A theme the human keeps returning to
   is load-bearing; mark it. A single old aside is background.
4. **Separate intent from prescription.** "Make ingest robust" is intent;
   "use a retry queue" was one day's suggested means. Record intent as
   durable, means as current-best-known and revisable.
5. **Record the flavor.** Alongside goals, capture the project's register:
   what it should feel like, what it must never become, taste constraints
   ("boring primitives", "no config sprawl", "CLI-first"). Flavor disambiguates
   a thousand small decisions that goals never reach.
6. **Capture limitations and trade-offs as first-class.** What the project
   deliberately does NOT do, and which trade-offs were consciously taken, are
   the most violated kind of intent. List them explicitly.

## Sources, in priority order

1. Direct prompts and interview answers in the current session.
2. Past session transcripts, if a search tool over them exists (mine the
   *user's* messages, not the assistant's).
3. Repo artifacts: README, docs, ADRs, commit messages (subject lines over
   bodies), issue titles, TODO/FIXME comments.
4. Inference from the code itself — weakest source; mark inferred entries
   `(inferred)` so a human can correct them cheaply.

## Format

```markdown
# Intent — <project>          (compiled 2026-07-09)

## Mission
One paragraph. What this is for, who it serves, what winning looks like.

## Flavor
- Register and taste constraints, in the human's own words where possible.

## Load-bearing intents        <!-- repeated/recent themes, marked ★ -->
- ★ <intent> (last affirmed 2026-07-08)

## Current directions
- <direction> — appetite: <small/medium/large>, from interview 2026-07-05

## Deliberate limitations & trade-offs
- Does NOT <x>; chose <a> over <b> because <reason>.

## Open questions
- <things the ledger cannot resolve; feed these to the next interview>

## Supersessions
- 2026-07-08: "<old intent>" overruled by "<new intent>".
```

## Discipline

Update the ledger at the end of every cycle, not continuously — compilation
is a batch job. Keep Current Intent under a page: it is read by every future
agent, so every line is a perpetual tax; admit a line only when its lifetime
value beats its lifetime read cost. When the ledger and the human disagree,
the human is right and the ledger gets a supersession entry.
