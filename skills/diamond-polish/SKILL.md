---
name: diamond-polish
description: Raise touched code toward canonical, diamond-grade form — deduplicate, simplify isomorphically, remove efficiency losses, sharpen interfaces — guided by the von Neumann and Feynman tests. Use when improving code quality, hunting duplication, refactoring, or when code works but doesn't yet deserve to exist in its current shape.
---

# Diamond Polish

Canonical code — code that looks like the *only* reasonable way to state the
computation — is not an aesthetic luxury. It is the cheapest code to verify,
the hardest to introduce bugs into, and the form every future agent reads
fastest. Polish is how touched code is left better than found, and it is
behavior-preserving by construction: polish that changes behavior is a bug
by definition, and gets its own scoped change instead.

## The two tests

- **The von Neumann test**: is this the computation, minimally stated? Strip
  the incidental: dead branches, defensive checks against impossible states,
  configuration nobody sets, generality nobody uses. What remains should be
  the problem's own structure showing through. If the algorithm has a known
  canonical form, use it and name it.
- **The Feynman test**: can you explain why every piece is there — honestly,
  from first principles, to a sharp student? Any line whose justification is
  "it was like that", "just in case", or "the framework wants it" is a
  candidate for deletion or a comment-worthy discovery. What you cannot
  explain, you may not keep unexamined.

## The passes

Applied to code you are already touching (polish rides along with real work;
it is rarely a standalone campaign unless the appetite says so):

1. **Deduplicate.** Same logic twice is a bug that hasn't diverged yet;
   *almost*-same logic twice usually already has — diff the copies, the delta
   is often an unfixed bug in one of them (report it to the hunt). Merge to
   one canonical site. Threshold: duplication of *decision* logic is always
   worth merging; duplication of trivial glue often is not — a bad
   abstraction is worse than modest repetition.
2. **Simplify isomorphically.** Flatten nesting, collapse boolean plumbing
   into the conditions they encode, replace state machines hand-rolled in
   flags with explicit enums/types, delete indirection with a single caller.
   Every step behavior-preserving; every step verifiable by the existing tests
   (if the tests can't tell, that's a hunt find about the tests).
3. **De-loss efficiency.** Remove losses, don't chase wins: needless
   allocation and copying, O(n²) hiding in a loop-with-lookup, chatty IO that
   batches trivially, recomputation of invariants. Real *optimization* beyond
   loss-removal needs a profile first and belongs in its own scoped change.
4. **Sharpen interfaces.** Boring primitives at the seams; make illegal
   states unrepresentable where the type system allows; boolean parameters
   become two functions or an enum; stringly-typed seams get types. Public
   interfaces only sharpen under an explicit compatibility plan (safe-scope).

## Restraint

The flavor section of the intent ledger governs taste calls — canonical form
in a "boring, obvious" codebase differs from canonical form in a
research-grade one. Do not average the shape away: a weird-looking piece of
code that is weird because the *problem* is weird has passed the von Neumann
test and must be left alone (add the explaining comment it deserved). And
polish obeys the same silence rule as hunting: when passes over an area stop
finding anything, stop polishing it.
