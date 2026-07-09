# `.forward/` — state schema

Forward keeps its memory in `.forward/` at the target repo's root. Everything
is plain text or JSONL: greppable, diffable, mergeable, committable. Commit
this directory — it is the project's accumulated strategic memory, and each
cycle makes the next cheaper.

Validate mechanically with `scripts/validate-ledgers.py` (ships with the
Forward repo; the forward skill runs it at Appraise). Rules preached here and
not machine-checked have historically been violated within one cycle.

## `intent.md`

Human-readable compiled intent. Format defined in the `intent-ledger` skill:
Mission / Flavor / Load-bearing intents / Current directions / Deliberate
limitations & trade-offs / Open questions / Supersessions. Kept under a page.

## `hunt.jsonl` — one object per probe

Each line is one strictly-valid JSON object (no comments, no multi-line
pretty-printing in the file itself). Example line:

```json
{"ts":"2026-07-09T22:45:25Z","area":"ingest/dedup","lens":"error-paths","finds":2,"issues":["half-written batch on SIGTERM","retry drops idempotency key"],"head":"abc1234","source":"self"}
```

Field rules:

- `ts` — ISO-8601, stamped **when the probe runs**. If the true time was not
  captured, `null` plus a `ts_note` explaining why; a reconstructed
  timestamp is a false receipt and worse than a null.
- `area` — **atomic**, stable name; never compound (`a+b` breaks per-area
  replay). Choose the partition once per repo and keep it.
- `lens` — closed vocabulary: `correctness | duplication | drift | dead-code
  | efficiency | interfaces | invariants | error-paths | spot-audit`.
  Extending the vocabulary requires updating this enum (and the validator)
  in the same commit as the first record using it.
- `finds` — count of **verified** finds only; `issues` — one string each.
- `head` — git HEAD when the probe ran, for change-aware silence replay.
- `source` — who probed: `self`, or a named external agent/judge/user.
  External finds count fully (they reset silence like any find — harder,
  in fact: an outsider finding what you missed is evidence about your lenses).

Derived per-area state (by replay): `probes`, `finds`, `silence`
(consecutive zero-find probes since last find). An area's earned silence
survives across sessions but is discounted when `git diff --stat
<last-probe-head>..HEAD` shows the area changed.

## `worth.jsonl` — one object per appraised change/batch

```json
{"ts":"2026-07-09","change":"idempotent ingest retries","commits":["abc123"],"area":"ingest/retry","finds_addressed":2,"dimension":"depth","probes_spent":9,"verdict":"loved","worth_probes":40,"appraiser":"user","note":"user: 'this was the thing silently corrupting batches'"}
```

Field rules:

- `commits` — real hashes. `"pending"` is valid only in an uncommitted
  working tree; committing a worth record with `"pending"` in it is a
  schema violation (it happened in cycle 1; the validator now rejects it).
- `area` + `finds_addressed` — link back to hunt.jsonl so the calibration
  `V = Σ worth_probes / Σ finds_addressed` is computable by replay.
- `verdict` ∈ `loved | fine | shrug | disliked`.
- `worth_probes` — elicited magnitude when available; otherwise the default
  verdict anchors (disliked 0, shrug 1, fine 3, loved 9) with
  `"anchors":true`. Self-appraisals (`appraiser:"self"`) are provisional,
  conservative by rule (when unsure between two verdicts, take the lower),
  and overwritable by a user verdict.
- `dimension` — which interview dimension the change served.

## `cycle.md`

Append-only log, one `## Cycle N — date` section per cycle: framing
paragraph, unease map, interview outcomes (or skip-reason), what shipped,
hunt statistics summary, and the named best candidate for the next cycle.
Corrections to a past cycle's claims go in a dated `### Corrections`
subsection under that cycle — never silent edits.

## Units

The common denominator is the **probe**: one focused attention-pass over one
area with one lens (~one subagent-task of effort). Spend (`probes_spent`),
value (`worth_probes`), and stopping thresholds (`3·V` of silence) all use
it, so value-per-spend is dimensionless and comparable across areas, cycles,
and repos. Probes are a proxy for tokens; count them honestly and
consistently rather than precisely — and count them **as they happen**, not
at write-up.
