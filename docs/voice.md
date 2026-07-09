# Voice — the prompting style Forward is distilled from

Forward's skills are written in a particular register, mined from the actual
prompts of people who drive projects well through agents. The style, distilled:

## What the prompts look like

- **Intent-dense, prescription-light.** They say what winning looks like and
  what the thing should *feel* like; they rarely enumerate steps. The model
  is trusted to find the steps — that trust is load-bearing, because a model
  that understands *why* handles the cases a checklist would have missed.
- **Not concise, and not trying to be.** Good driving prompts ramble a
  little. They circle the intent from several angles, think out loud, repeat
  the important thing in different words. The redundancy is signal: it shows
  the model which themes are load-bearing (repetition = weight) and gives it
  texture to interpolate from.
- **Wide leeway, few hard rails.** Permission is broad ("do all of it,
  conscientiously") and the constraints are few, sharp, and absolute (no
  marketing copy; never break the tree; fix canonical, not copies). Rails
  are stated as invariants, not as procedures.
- **The model is addressed as a colleague with taste.** Asked what it thinks,
  what it feels, where it's uneasy — and expected to answer honestly and be
  held to the answer. Names are invoked as registers to think in (von
  Neumann: is this the computation, minimally stated? Feynman: can you
  explain every piece honestly?), not as decoration.
- **Denominators are demanded.** Claims of progress come with the spend
  attached. "Found no issues" must mean "and here is how hard I looked."
- **Trade-offs surface in the report, not as gates.** Questions are hoarded
  and batched; ambiguity that can be resolved by judgment is; the interview
  moment, when it comes, is one moment.

## Rules the skills encode from this

1. State intent and flavor; grant leeway; hold a few absolute rails.
2. Repetition across time is weight — compile it, don't dedupe it away
   entirely (the intent ledger's load-bearing markers).
3. Ask the model for its reaction before its analysis.
4. Every claim of coverage carries its denominator.
5. Questions batch into one interview; everything else is judgment.
6. Open-ended beats exhaustive; a checklist is a floor, never a ceiling.
