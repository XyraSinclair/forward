# `.forward/` — state schema

Forward keeps its memory in `.forward/` at the target repo's root. Everything
is plain text or JSONL: greppable, diffable, mergeable, committable. Commit
this directory — it is the project's accumulated strategic memory, and each
cycle makes the next cheaper.

## `intent.md`

Human-readable compiled intent. Format defined in the `intent-ledger` skill:
Mission / Flavor / Load-bearing intents / Current directions / Deliberate
limitations & trade-offs / Open questions / Supersessions. Kept under a page.

## `hunt.jsonl` — one object per probe

```json
{
  "ts": "2026-07-09T12:00:00Z",
  "area": "ingest/dedup",          // area partition is chosen per-repo; keep names stable
  "lens": "error-paths",           // correctness | duplication | dead-code | efficiency | interfaces | invariants | error-paths
  "finds": 2,                      // verified finds only; refuted candidates don't count
  "issues": ["half-written batch on SIGTERM", "retry drops idempotency key"],
  "head": "abc1234"                // git HEAD at probe time, for change-aware silence replay
}
```

Derived per-area state (by replay): `probes`, `finds`, `silence`
(consecutive zero-find probes since last find). An area's earned silence
survives across sessions but is discounted when `git diff --stat
<last-probe-head>..HEAD` shows the area changed.

## `worth.jsonl` — one object per appraised change/batch

```json
{
  "ts": "2026-07-09",
  "change": "idempotent ingest retries",
  "commits": ["abc123"],
  "dimension": "depth",            // which interview dimension this served
  "probes_spent": 9,
  "verdict": "loved",              // loved | fine | shrug | disliked
  "worth_probes": 40,              // value denominated in probes; ranking-derived is fine
  "appraiser": "user",             // user | self (self is provisional, overwritable)
  "note": "user: 'this was the thing silently corrupting batches'"
}
```

## `cycle.md`

Append-only log, one `## Cycle N — date` section per cycle: framing
paragraph, unease map, interview outcomes (or skip-reason), what shipped,
hunt statistics summary, and the named best candidate for the next cycle.

## Units

The common denominator is the **probe**: one focused attention-pass over one
area with one lens (~one subagent-task of effort). Spend (`probes_spent`),
value (`worth_probes`), and stopping thresholds (`3·V` of silence) all use
it, so value-per-spend is dimensionless and comparable across areas, cycles,
and repos. Probes are a proxy for tokens; count them honestly and
consistently rather than precisely.
