# Drive Forward

A small suite of agent skills that drive a project forward — conscientiously,
safely, and measurably. Drop it into a codebase, run `/forward`, and get
cycles of principled progress: intent compiled from your prompts over time,
issues hunted with a statistical stopping rule, changes shipped well-scoped
and verified, worth measured instead of assumed.

Forward is not a task runner and not an autocomplete for ambition. It is a
**drive loop**: the discipline an excellent, trusted engineer applies when
told "make this project better, and keep making it better."

## The cycle

```
        ┌──────────────────────────────────────────────┐
        │                                              │
   Orient ──► Interview ──► Hunt ──► Improve ──► Verify ──► Appraise
   (frame,    (dimensions,  (issues   (safe,      (drive     (worth per
    intent,    appetite —    beget     scoped,     the real   token; feed
    unease)    if needed)    issues)   canonical)  flow)      back)
```

Open mode feels things out — framing, ideation, questions, sentiment. Closed
mode ships — small, reversible, verified changes. The cycle alternates them
on purpose: all-open never ships, all-closed ships the wrong thing.

## The skills

| Skill | What it carries |
|---|---|
| **forward** | The orchestrator. One cycle end-to-end; loops if asked. |
| **intent-ledger** | Compiles strategic intent from prompts over time — dedup, recency-weighted, supersessions recorded, nothing silently forgotten. |
| **dimension-interview** | Finds the independent directions a project could grow in, and asks the human — once, in one batch — which excite them and with what appetite. |
| **hazard-hunt** | Issue hunting as measurement. Issues beget issues; an area is released only after statistically meaningful silence, never boredom. |
| **model-sentiment** | Asks models what they honestly feel about the code — unease, embarrassment, admiration — and uses it as a prior for where to look. |
| **safe-scope** | Blast radius before edits, one concern per change, reversible checkpoints, commit early / push immediately. |
| **diamond-polish** | Raises touched code toward canonical form — the von Neumann test and the Feynman test, applied behavior-preservingly. |
| **worth-ledger** | Did you actually like the changes? What were they worth, per token spent? The measurement that calibrates everything else. |

The principles behind them live in [PRINCIPLES.md](PRINCIPLES.md). The one to
read first: **issues beget issues** — finding a bug raises the estimated rate
of remaining bugs, so you search harder, and you only stop when silence has
been statistically earned (rule of three: after `t` clean spend, the 95%
bound on the remaining rate is `3/t`).

## Install

Into one project:

```sh
./install.sh /path/to/your/repo        # copies skills into .claude/skills/
```

For all projects: `./install.sh --user` (copies into `~/.claude/skills/`).
The repo also carries a `.claude-plugin/plugin.json`, so it can be installed
as a Claude Code plugin from a marketplace that lists it.

Then, in a Claude Code session inside your project:

```
/forward
```

(Installed as a *plugin* rather than via install.sh, skills are namespaced:
the command is `/forward:forward`.)

State accumulates in `.forward/` at your repo root (intent ledger, hunt
statistics, worth ledger, cycle log — schema in
[docs/ledger-schema.md](docs/ledger-schema.md)). Commit it — it is the
project's memory, and each cycle makes the next one cheaper and sharper.

## Hard rails

A few rules are absolute, not vibes:

- **No marketing copy.** Prose meant to persuade humans is proposed, never
  shipped autonomously. Effort has backend gravity: hardening over flourish.
- **Well-scoped or not at all.** No sprawling diffs, no smuggled scope, no
  broken tree between commits. Work is committed and pushed the moment it's
  real.
- **Stop only on evidence.** Hunts end on statistical silence or an explicit,
  reported budget ceiling — never silently truncated.
- **Measure worth.** Probes spent and value returned are always reported
  together. Never quote one without the denominator.

## Benchmarks

`benchmarks/` contains the elicitation protocol for evaluating Forward
itself: after cycles on a real repo, the owner appraises shipped changes
(loved / fine / shrug / disliked, plus relative worth), producing
value-per-token curves. A drive loop that can't show its curve is marketing —
see hard rail #1.

## Flavor

Forward's skills guide with intent and grant leeway, rather than scripting
steps. They assume the model on the other end is capable and honest, ask it
what it thinks and feels, and hold it to a few sharp rails. That is the
prompting style Forward is distilled from, and the style it perpetuates. See
[docs/voice.md](docs/voice.md).
