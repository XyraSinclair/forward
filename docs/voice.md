# Voice — the prompting style Forward is distilled from

Forward's skills are written in a particular register, mined from several
hundred real prompts by people who drive projects well through agents. The
patterns below are what actually recurs in prompts that produced good
sustained work — and they are the style Forward's own skills use and
perpetuate.

## What the prompts look like

- **Intent-dense, prescription-light.** They name the quality of the end
  state — "squared away", "canonical", "diamond-grade", "from the book" —
  and let the agent choose the path. Almost never a step list. A model that
  understands *why* handles the cases a checklist would have missed.
- **Exit criteria instead of procedures.** Work is bounded by a closable
  condition ("don't come back until X holds"), not by a sequence of steps.
  The unit of work is a **tranche**: ambitious but cogent, and it *closes*.
- **Wide leeway, few hard rails.** Permission is broad ("do everything that
  makes sense; you know what's best") and the constraints are few, sharp,
  and absolute: never destroy latest work; commit and push before and after
  anything risky; don't touch the named file. Rails are invariants, not
  procedures.
- **Ambition is an explicit dial.** "What's the maximally ambitious version?"
  and "an order of magnitude more conscientiousness" both appear — the
  prompt says how hard to push, then gets out of the way.
- **The model is addressed as a respected mind with taste.** Asked what it
  thinks, what it admires, and — the signature move — *what still feels
  weird*. Weirdness-detection is used as a primary bug-finding instrument,
  and "do you feel deeply good about everything?" is a real pre-deploy gate,
  not politeness. In return, extreme ownership is expected.
- **Spirits, not rubrics.** Taste and ambition are calibrated by naming
  exemplars to think in the register of — von Neumann (is this the
  computation, minimally stated?), Feynman (can you explain every piece
  honestly?) — rather than enumerating criteria.
- **Safety is conscientiousness plus ritual plus fresh audits** — never
  permission-seeking. Commit-and-push as rhythm, empirical spot-checks of
  real data against ground truth ("audit 20 of them against the source"),
  invited red-teaming. Questions back at the human are a failure mode unless
  the blocker is irreducibly theirs.
- **Not concise, and not trying to be.** The good driving prompts are
  scrappy — voice-note casual, circling the intent from several angles,
  repeating the load-bearing theme in different words. The redundancy *is*
  the weighting: what gets repeated is what matters. Forward's intent ledger
  compiles repetition into weight rather than deduplicating it away.
- **Crispness is for sub-delegation.** The same voice flips to contract mode
  when scoping a bounded worker task: exact file list, exact focus, exact
  output shape, word limit. Open-endedness is for the trusted lead;
  contracts are for workers. Forward's skills do the same — open-ended
  orchestrator, tightly-specified probe subagents.

## Rules the skills encode from this

1. State intent and end-state quality; grant leeway; hold a few absolute rails.
2. Bound work by exit criteria and close tranches — never trail off mid-thought.
3. Set the ambition dial explicitly per cycle; default to conscientious-high.
4. Ask the model what feels weird before asking it to analyze; treat felt
   unease as a defect prior and "feels deeply good" as a shipping gate.
5. Repetition across time is weight — compile it, don't flatten it.
6. Every claim of coverage carries its denominator.
7. Questions batch into one interview; everything else is judgment.
8. Verify empirically against ground truth, on real data, freshly.
9. Open-ended for the lead, contract-mode for workers.
