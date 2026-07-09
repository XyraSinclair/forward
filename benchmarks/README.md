# Benchmarks — did they actually like it?

Forward's claim is not "the agent did a lot", it is "the agent did a lot of
*good*, per token". These benchmarks make that claim testable on real repos
with real owners. No synthetic tasks: the unit of evaluation is a cycle run
on a project someone actually cares about, appraised by that someone.

## Protocol

1. **Baseline.** Pick a live repo. Record: open bug count, test status, the
   owner's one-paragraph description of what they wish were better.
2. **Run.** Execute N Forward cycles (N ≥ 3 recommended — the ledgers need a
   cycle or two to warm up). All `.forward/` state is the run's trace.
3. **Blind appraisal.** Present the owner every shipped change as one line of
   observable effect (never implementation detail), in shuffled order,
   without probe costs attached. Collect:
   - verdict per change: `loved | fine | shrug | disliked`
   - relative worth: "rank these; which would you have paid a dedicated hour
     for; which shouldn't have happened?"
4. **Score.** From verdicts + ranks + `hunt.jsonl` spend, compute the
   metrics below. Costs are revealed to the owner only *after* appraisal.

## Metrics

- **Worth per probe** — Σ`worth_probes` / Σ`probes_spent`. The headline. > 1
  means the loop returned more value than attention it consumed.
- **Verdict distribution** — loved:fine:shrug:disliked. A loop optimizing
  volume shows a fat shrug tail; a conscientious one is thin-tailed with
  nonzero *disliked* honestly reported.
- **Hazard calibration** — did areas the loop kept hunting actually keep
  yielding? Plot finds against cumulative probes per area: the curve should
  be convex-then-flat, with release points sitting on the flat. Releases
  followed by owner-discovered bugs in that area are calibration failures;
  count them.
- **Sentiment calibration** — fraction of unease-map top-3 entries that
  produced verified finds. Measures whether asking the model what it feels
  is pulling its weight.
- **Intent fidelity** — owner re-reads `intent.md`: "is this what you meant?"
  scored agree / minor-drift / wrong. Drift here poisons everything
  downstream, so it is a first-class number.
- **Interview efficiency** — questions asked per cycle (lower is better,
  given fidelity holds). The best interview is the one the ledger made
  unnecessary.

## Reporting

One markdown report per run in `benchmarks/runs/<repo>-<date>.md`: baseline,
cycles run, metric table, the owner's verbatim reactions, and — always —
both numbers together: probes spent and worth returned. Never one without
the denominator.
