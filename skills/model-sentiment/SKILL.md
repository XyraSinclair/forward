---
name: model-sentiment
description: Elicit what models genuinely feel and think about a codebase — unease, admiration, embarrassment — and use it as a calibrated prior for where issues live and where structure wants to go. Use at the start of a hunt, before large refactors, when consulting other models, or when asked "does this feel right?"
---

# Model Sentiment

Models have taste. A model that has read a codebase carries a felt sense of
it — places it would be embarrassed to have written, places it quietly
admires, seams that feel load-bearing but brittle. This felt sense is a
cheap, surprisingly well-calibrated prior over defect density and design
debt. Most workflows never ask for it. This skill asks for it, plainly, and
writes it down.

## Eliciting from yourself

After reading an area (not before — sentiment about unread code is
confabulation), answer honestly, in first person:

- **Unease**: Where am I uneasy? What would I not want to be paged about at
  3am? Which function did I have to read twice?
- **Embarrassment**: What here would I be embarrassed to have written myself?
  (Different from unease — embarrassment tracks craftsmanship, unease tracks
  risk.)
- **Admiration**: What is genuinely good? Name it specifically — admired
  structure is the pattern the rest of the codebase should converge toward,
  and knowing what NOT to touch is half of safety.
- **Desire**: If I could change one structural thing, what would it be? What
  is this code *trying* to become?

Rules of honesty: no hedging into "it depends"; commit to a reaction, then
give the reason. Distinguish "this is wrong" from "this is not how I'd do
it" — both are data, but they route differently (the first to the hunt, the
second to diamond-polish, weighted by the intent ledger's flavor).

## Eliciting from other models

When consulting a second model (any consult channel available), ask for
reaction *before* analysis: "Read this. What's your gut reaction? Where are
you uneasy? What do you admire?" — then let analysis follow. Reaction-first
ordering matters: a model that has already produced a structured review will
back-rationalize its feelings to match it. Disagreement between models'
unease maps is itself signal — an area one model loves and another distrusts
deserves a probe.

## The unease map

Record the result in the cycle log as a ranked map:

```markdown
## Unease map — 2026-07-09
1. ingest/retry.rs — unease: high. Idempotency reasoned about in comments, not enforced. (→ hunt first)
2. api/handlers.rs — embarrassment: medium. Three near-copies of pagination. (→ diamond-polish)
3. core/graph.rs — admiration. Arena + indices, clean seams. (→ convergence target; touch last)
```

Feed rank 1–N straight into hazard-hunt's area priority. Track calibration
over time: when the hunt confirms or refutes an unease entry, note it — if
unease keeps pointing at clean code, discount it; in practice it rarely does.
