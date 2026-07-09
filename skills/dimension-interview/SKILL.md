---
name: dimension-interview
description: Identify the independent dimensions along which a project could grow, then interview the user — once, in one batch — about which directions excite them, what scope appetite they have, and what's off-limits. Use when the intent ledger is stale or silent on a live decision, when starting work on an unfamiliar project, or when multiple credible directions compete.
---

# Dimension Interview

The point of interviewing is not to offload decisions — it is to elicit the
strategic information only the human has: appetite, excitement, no-go zones.
Everything else you decide yourself. A good interview happens **once per
cycle at most**, is skippable when the intent ledger already answers, and
never degenerates into drip-fed "how should I proceed?" polling.

## 1. Find the dimensions first

Before asking anything, do the analysis. Decompose the plausible futures of
the project into **independent dimensions** — directions of expansion that
can be pursued (or not) separately. Good dimensions are orthogonal: choosing
one doesn't force another. Typical axes:

- **Depth** — harden what exists: correctness, tests, performance, error paths.
- **Breadth** — new capabilities, new inputs/outputs, new integrations.
- **Reach** — more users/platforms: packaging, install story, docs, API surface.
- **Scale** — bigger data, more load, concurrency, cost.
- **Leverage** — internal tooling, benchmarks, observability that speed later work.

Derive the project-specific versions of these (the generic names are
scaffolding, not the answer). For each dimension write one line: what
expanding it would mean *here*, and roughly what a small vs. large bet looks
like.

## 2. Interview in one batch

Present the dimensions compactly, then ask few, high-yield questions —
ideally 2–4, all at once:

- **Excitement**: "Of these directions, which are exciting to you right now —
  and is any of them actively boring?" (Excitement is signal about value that
  no code analysis can produce.)
- **Appetite**: "For the direction(s) you pick, what scope were you imagining
  — a tightening pass, a real feature, or a campaign?"
- **Rails**: "Anything off-limits or that must not change out from under you
  (APIs, formats, behavior others depend on)?"
- **Felt sense** (optional, when the ledger lacks flavor): "What should this
  project feel like when it's right?"

Phrase questions concretely against *this* project, never as generic
multiple-choice about your own process. Offer your own read as a default in
each question ("my instinct is depth-first — the ingest path is carrying the
most risk") so a busy human can just say "yes."

## 3. Skip rules

Skip the interview entirely when:

- the intent ledger already answers the live question and was affirmed recently;
- the user has said, in any form, "just proceed / you decide" — record that
  as standing appetite in the ledger and act;
- no human is present (autonomous/cron run): choose by the worth ledger's
  value-per-token history, defaulting to depth (hardening) — and log the
  choice and its rationale so it's cheap to overrule later.

## 4. Close the loop

Write every answer into the intent ledger immediately — excitement as
direction weights, appetite as scope bounds, rails as limitations. The test
of a good interview is that the *next* cycle doesn't need one.
