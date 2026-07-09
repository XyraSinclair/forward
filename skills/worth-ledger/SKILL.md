---
name: worth-ledger
description: Measure whether shipped changes were actually liked and what they were worth — elicit valuations from the user, record worth against tokens spent, and feed the results back into stopping thresholds and direction weights. Use at the end of a cycle, after a batch of changes lands, or when deciding where effort pays.
---

# Worth Ledger

Unmeasured improvement is indistinguishable from motion. The worth ledger
closes the loop: every cycle's output gets appraised — was it liked? what was
it worth? — and the appraisal recalibrates everything upstream: the hunt's
stopping threshold `V`, the interview's direction weights, and the honest
answer to "is this project still paying for attention?"

Lives at `.forward/worth.jsonl`, one JSON object per appraised change or batch:

```json
{"ts":"2026-07-09","change":"idempotent ingest retries","commits":["abc123"],"probes_spent":9,"verdict":"loved","worth_probes":40,"note":"user: 'this was the thing silently corrupting batches'"}
```

`worth_probes` denominates value in the same unit as spend (probes ≈ one
focused attention-unit), so value-per-token is a dimensionless ratio you can
compare across areas, cycles, and projects.

## Eliciting from the user

Appraisal is one light moment per cycle, batched — never a survey after every
diff. Show the shipped changes compactly (one line each, with the observable
effect, not the implementation), then ask two things:

- **Verdict** per change or batch: loved / fine / shrug / disliked. "Shrug"
  is a real answer and important to make cheap to give — a user who must
  praise everything gives you no signal.
- **Worth**, anchored concretely: "Which of these would you have paid a
  dedicated hour for? Which shouldn't I have bothered with?" Relative
  ranking beats absolute numbers; people rank reliably and estimate poorly.

If the user engages beyond the batch question, mine the conversation — a
spontaneous "oh that one was great" is the highest-fidelity datum the ledger
ever gets. If no human is available, self-appraise conservatively, mark
`"appraiser":"self"`, and let a later human verdict overwrite it.

## Feeding back

- **Stopping threshold**: per area, `V` = total `worth_probes` returned by
  the area's appraised changes ÷ total finds those changes addressed —
  probes of value per find. High-worth areas earn longer hunts (silence
  threshold `3·V` grows); persistently shrug-rated areas get released sooner.
- **Direction weights**: sum worth by dimension (depth/breadth/reach/...).
  A dimension whose changes keep landing "loved" is where the next
  autonomous cycle defaults; a dimension the user keeps shrugging at is
  evidence the interview's excitement answer has gone stale — re-ask it.
- **The project-level curve**: value-per-probe across cycles is the health
  metric. Declining curve + statistical silence everywhere = the well is dry;
  say so and recommend stopping. A rising curve after a find-rich cycle is
  the hazard principle working — report it as license to keep spending.

## Benchmarking honesty

The ledger is also the anti-slop instrument: it makes "the agent did a lot"
and "the agent did a lot of *good*" distinguishable. Report both numbers,
always — probes spent and worth returned — and never quote one without the
denominator.
