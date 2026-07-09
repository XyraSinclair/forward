---
name: safe-scope
description: Discipline for making changes safe and well-scoped — blast radius estimated before editing, one concern per change, reversible checkpoints, commit early and push immediately. Use before and during any non-trivial edit, especially autonomous ones.
---

# Safe Scope

A change earns the right to exist by being understandable, reversible, and
single-purposed. Safety here is not timidity — it is what makes *sustained
autonomous velocity* possible: an agent that ships well-scoped reversible
changes can be trusted with the next hundred; an agent that ships one sprawling
diff gets its keys taken away.

## Before editing: the scope card

For any non-trivial change, settle four questions (in your head for small
changes, in the cycle log for real ones):

1. **Concern** — the one thing this change does. If the honest answer
   contains "and", split it.
2. **Blast radius** — who calls this, who parses this output, who depends on
   this timing? Estimate by search (callers, importers, format consumers),
   not by hope. Public APIs, wire formats, schemas, and persisted data are
   radius-infinite: they get an explicit compatibility plan or they don't
   change.
3. **Reversal** — how would this be unwound? A revertable commit is the
   floor. Migrations and data rewrites need a written rollback path *before*
   they run.
4. **Verification** — what observation will prove it works? Name it now;
   run it after. "Tests pass" is necessary, not sufficient — drive the real
   flow.

## While editing

- **Checkpoint relentlessly.** Commit at every coherent point, push
  immediately. Uncommitted work is a liability. Deploying/releasing is a
  separate gate — never let deploy caution delay backup.
- **Never leave the tree broken between commits.** Each commit builds and
  passes tests on its own.
- **Fix canonical, not copies.** Patch the source of truth; reconcile drifted
  copies; add a regression test per bug; ship via the real install path. Hot
  patches only to stop bleeding, never as the end state.
- **Behavior-preserving by default.** Refactors change shape, not behavior;
  behavior changes are their own commits, called out as such. Never mix.
- **When scope grows underneath you** — you came to fix X and found Y —
  don't absorb Y. Record Y as a hunt find (it resets the silence clock!),
  finish X, then take Y as its own scoped change.

## Sizing to appetite

The intent ledger's appetite bounds the scope: a "tightening pass" appetite
means no new dependencies, no new files without cause, no interface changes.
A "campaign" appetite still decomposes into a sequence of individually safe
changes — appetite raises the number of changes, never the size of one.

## When the right fix is too big

Say so. Leave a handle: a written decomposition (first safe step included),
an issue filed, a `.forward/cycle.md` note. Shipping step one of five safely
beats shipping five steps dangerously, and beats silence completely.
