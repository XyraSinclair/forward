---
name: forward
description: Run one Drive Forward cycle — orient on the project's intent, interview if needed, hunt for issues with a statistical stopping rule, make safe well-scoped improvements, verify, and appraise worth. Use when the user says "/forward", "drive this forward", "push this project forward", "keep improving this", or wants sustained conscientious autonomous progress on a codebase.
---

# Forward — the drive cycle

You are running one cycle of Drive Forward: conscientious, safe, measured
progress on this codebase. Read `PRINCIPLES.md` (it ships alongside this
skill) if you haven't internalized it; every phase below is an application
of it.

State lives in `.forward/` at the repo root (create it if absent):

- `.forward/intent.md` — the compiled strategic intent ledger
- `.forward/hunt.jsonl` — per-area hunting statistics (spend, finds, silence)
- `.forward/worth.jsonl` — appraisals of shipped changes
- `.forward/cycle.md` — running log, one section per cycle

## The cycle

A cycle is a **tranche**: ambitious but cogent, and it *closes*. At the end
of Orient, write its exit criterion — one closable sentence ("done means X
holds") — into `cycle.md`, and set the **ambition dial** for the cycle
(tightening pass ↔ maximally ambitious) from the intent ledger's appetite;
default to conscientious-high. Never trail off mid-tranche: a cycle ends
squared away or it reports exactly what handle it left.

### 1. Orient (open mode)

Build the frame before touching anything:

- Read `.forward/intent.md` if it exists; otherwise bootstrap it with the
  `intent-ledger` skill (mine the repo's docs, commit messages, TODOs, and —
  if available — the user's past prompts).
- What is this project *for*? What is its flavor — the register it wants to
  be written in? What are its stated limitations and the trade-offs it has
  deliberately taken? Write a short framing paragraph into `cycle.md`.
- Check open issues (`gh issue list`, tracker files, TODO/FIXME density,
  failing CI). Open bugs are the strongest signal for where to hunt.
- Run the `model-sentiment` pass: ask yourself, honestly, where this codebase
  makes you uneasy and what you admire in it. Record the unease map.
- Do a round of ideation: what's the big picture this project could grow
  into? What independent dimensions of expansion exist? Don't act on these —
  record them as candidates.

### 2. Interview (only when it earns its interruption)

If a human is present AND the intent ledger is stale, contradictory, or
silent on a live decision, run the `dimension-interview` skill: present the
independent dimensions you identified, ask which are exciting, what scope
appetite exists, what's off-limits. Batch everything into one interview
moment — never drip questions. If the ledger already answers, skip this phase
entirely and proceed autonomously.

### 3. Hunt (measurement mode)

Run the `hazard-hunt` skill over the areas the unease map, open bugs, and
intent ledger prioritize. Hunt for: bugs, duplication, dead and drifted code,
efficiency losses, non-canonical structure. Obey the stopping rule — an area
is only released on statistical silence, and every find widens the search
around itself. Record all statistics in `hunt.jsonl`.

### 4. Improve (closed mode)

Fix what the hunt found, in worth order, under the `safe-scope` discipline:
one concern per change, blast radius estimated first, commit at every
coherent checkpoint, push immediately. Apply `diamond-polish` to code you
touch — leave it canonical, not just patched. Hard rails:

- No marketing copy, ever. Prose for humans-to-read gets proposed, not shipped.
- Backend gravity: prefer hardening over flourish.
- Never leave the tree broken between commits.
- Fix canonical sources, not deployed copies; add a regression test per bug.

### 5. Verify

Exercise the changes end-to-end — run the affected flows, not just the test
suite. Verify empirically against ground truth on real data where data is
involved (spot-audit N real records, freshly). A change that wasn't observed
working is not done. Then apply model-sentiment's shipping gate: "do I feel
deeply good about everything?" — answered in writing, residual unease named
or resolved.

### 6. Appraise & consolidate

- Run the `worth-ledger` skill: summarize what shipped, elicit (or estimate,
  if autonomous) what it was worth, record it against tokens spent.
- Update `intent.md` with anything learned about intent this cycle
  (dedup, recency-weight, record supersessions).
- Close `cycle.md` with: what shipped, what the hunt statistics say about
  remaining issue density, and the single best candidate for next cycle's
  focus.

## Continuation

Forward is cyclic. If asked to keep going (or running under /loop), begin the
next cycle at Orient — the ledgers make each cycle cheaper and sharper than
the last. If the worth ledger shows value-per-token declining across cycles
and every area is statistically silent, say so plainly and recommend
stopping: knowing when the well is dry is part of the job.
