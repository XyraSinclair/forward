---
name: hazard-hunt
description: Hunt a codebase for issues (bugs, duplication, drift, inefficiency) under a statistical stopping rule — issues beget issues, and an area is only released after enough clean spend that the remaining rate is provably low. Use when hunting bugs, auditing an area, deciding whether to keep looking, or when someone asks "is this clean yet?"
---

# Hazard Hunt

The deep principle: **finding an issue is evidence of more issues.** Defects
cluster. So hunting is not a checklist to complete — it is a measurement
process with a statistically principled stopping rule. Most reviewers stop
when the fix list feels long. That is exactly backwards: a long fix list
means the hazard rate is high and you should keep going.

## The model

Treat issue discovery in an **area** (a module, subsystem, idiom, or concern
— you choose the partition, and record it) as arrivals in token-time.

- Spend is measured in **probes**. One probe = one focused review pass over
  one area with one lens (~one agent-attention-unit). Probes are your token
  proxy; count them honestly.
- Per area, track: `probes` (total), `finds` (total issues), and
  `silence` (consecutive probes since the last find).

The observed hazard for an area is `λ = finds / probes`.

## The stopping rule

Let `V` = the value of an average issue in this area, denominated in probes
(from the worth ledger if one exists; default `V = 3` — a typical issue is
worth about three probes of effort).

- **Never-hit area** (finds = 0): release after `probes ≥ 3` clean probes for
  low-stakes areas, `probes ≥ 3·V` for load-bearing ones. (Rule of three:
  after `t` clean probes the 95% upper bound on the rate is `3/t`; hunting
  pays while `λ·V > 1`.)
- **Hit area** (finds > 0): release only when `silence ≥ 3·V`. Every find
  resets `silence` to zero. Yes, this means a hot area can absorb many
  probes. That is the point — it is the areas that keep yielding that
  deserve the spend.
- **Escalation on find**: a find doesn't just reset the clock — it widens
  the neighborhood. Immediately probe: the same file end to end; the same
  idiom everywhere it occurs in the repo (grep for it); the same class of
  mistake in sibling modules. Clusters are found by following the first
  member home.

**Probe integrity.** Silence only counts from a trusted instrument. A probe
whose tooling is suspect — a grep that might have been rewritten, a check
that collapses "error" and "no match" into one exit path, a sample that
didn't actually reach ground truth — counts as *no probe at all*, not as a
clean one. When a result surprises you toward "clean", re-run it through the
rawest instrument available before letting it advance the silence clock.

Never stop because you are bored, because the list is long, or because you
"covered" the files. Stop only on silence or on an explicit budget ceiling —
and if a budget ends the hunt early, say so: report which areas were released
on silence and which were merely truncated. Silent truncation reads as
"clean" and is a lie.

## Lenses

Rotate lenses across probes so consecutive probes of an area are not
redundant: correctness / edge cases; duplication (same logic twice, drifted
copies); dead code and stale docs; efficiency (needless allocation, O(n²)
lurking, chatty IO); interface sharpness (leaky abstractions, boolean
parameters, stringly-typed seams); invariants that are assumed but never
checked; error paths (what happens when this fails halfway?); and the
**empirical spot-audit** — pull N real records/outputs and verify them
against ground truth by hand (does the stored tweet match the live URL? does
the cache entry match a fresh compute?). Data poisoning and silent drift are
invisible to code review; only fresh empirical sampling finds them, and a
single failed sample is a find that resets the clock like any other.

Seed the area priority from: open bugs (strongest signal — an open bug marks
a hot area by definition), the unease map from `model-sentiment`, recent
churn (`git log --stat`), and the intent ledger's load-bearing paths.

## Ledger

Persist statistics to `.forward/hunt.jsonl`, one JSON object per probe:

```json
{"ts":"2026-07-09T12:00:00Z","area":"ingest/dedup","lens":"error-paths","finds":2,"issues":["half-written batch on SIGTERM","retry drops idempotency key"],"head":"abc1234"}
```

Cumulative per-area state is derived by replay, so past sessions' spend
counts toward today's silence thresholds. Before hunting, replay the ledger:
an area that earned its silence last week and hasn't changed since
(`git diff --stat <then>..HEAD`) stays released; an area that changed gets
its clock partially reset.

## Fan-out

At scale, run probes as parallel subagents (Workflow or Agent tool), one
area×lens per agent, and apply the stopping rule in the orchestrator between
rounds — loop-until-dry, where "dry" is defined by the silence thresholds
above, not by a fixed round count. Adversarially verify finds before counting
them: a refuted find does not reset the clock.
