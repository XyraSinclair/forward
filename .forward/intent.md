# Intent — forward          (compiled 2026-07-09)

## Mission
A small suite of skills — a program people can run in their codebase — that
drives a project forward conscientiously and safely: compiles strategic
intent from prompts over time, cycles between open feeling-out and closed
improvement, hunts issues hard, ships well-scoped safe changes, and measures
whether people actually liked them.

## Flavor
- "Principled in a couple of beautiful ways" — few principles, held absolutely.
- Open-ended guidance over scripts: "guide models, give them a lot of leeway
  to drive things forward" — with some hard rules.
- Skills + a workflow, not a platform. Boring primitives; plain text state.

## Load-bearing intents
- ★ Issues beget issues: finds-per-token is evidence of more; stop hunting an
  area only after statistically meaningful clean spend. "Something really
  important for us to ace here." (founding prompt, 2026-07-09)
- ★ Capture strategic intent from prompts over time; dedup inconsistencies;
  weight the latest more. (founding prompt)
- ★ Changes must be safe and well-scoped. (founding prompt)
- ★ Ask models what they feel and think. (founding prompt)
- ★ Good enough that we're excited to run it purely on itself; commit and
  push before and after. (2026-07-09, mid-build)
- Benchmarks: elicit whether people actually liked the changes and what they
  were worth. (founding prompt)
- Interview the user lightly: independent dimensions, which are exciting,
  what scope appetite. (founding prompt)
- Mine the author's prompts for voice/flavor and encode it. (founding
  prompt; done — docs/voice.md)

## Current directions
- Depth (self-hardening via dogfood cycles) — appetite: standing.
- Reach (installable by others: install.sh + plugin manifest) — appetite:
  small, already served.

## Deliberate limitations & trade-offs
- AIs don't write marketing copy; backend gravity over flourish.
- Probes as token-proxy: honest and consistent over precise. Chose
  comparability across sessions over exact token accounting.
- Prose-as-program: skills are the implementation; no runtime code beyond
  install.sh. Chose auditability over machinery.

## Open questions
- Should the hunt fan-out ship as a ready-made Workflow script file, or stay
  described in hazard-hunt? (candidate for next cycle)
- Repo name settled as `forward` ("Forward or Drive Forward" — both offered;
  repo `forward`, title Drive Forward).

## Supersessions
- (none yet)
