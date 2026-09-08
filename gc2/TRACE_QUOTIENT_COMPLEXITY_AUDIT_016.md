# GC-II Trace-Quotient Complexity Audit 016

## Target
Strengthen the trace quotient from Audit 015 toward the GC-I local-to-global translator program without making a false novelty claim.

## Exact quotient complexity
For a deterministic finite operational world with primitive alphabet `Sigma`, let `~_G` denote future capability-cost equivalence of feasible prefixes. Define

`K_G = |Reach(Sigma*) / ~_G|`.

`K_G` is the number of states in the smallest deterministic exact capability-accounting machine whose state is sufficient to predict every future feasibility/capability/cost signature.

### Theorem (restricted finite deterministic specialization)
Every deterministic exact accounting machine preserving the complete future capability-cost signature has at least `K_G` internal states, and the quotient machine with one state per reachable `~_G` class has exactly `K_G` states.

### Proof
If two prefixes lie in distinct `~_G` classes, by definition some continuation distinguishes their feasibility, capability, or cost. Any exact accounting machine mapping them to the same internal state would evolve identically under that continuation and therefore fail on at least one of the two prefixes. Hence distinct `~_G` classes require distinct internal states, giving the lower bound. Conversely Audit 015 proves `~_G` is a right congruence and that future records are well-defined on its classes, so transitions on quotient classes yield an exact machine with `K_G` states. QED.

## Exponential family
Consider the regular future predicate `L_n = { w in {0,1}* : the n-th symbol from the right is 1 }`. There is an `(n+1)`-state NFA for `L_n`, while the deterministic future-equivalence quotient has `2^n` classes: the `2^n` binary suffixes of length `n` are pairwise distinguishable by suitable continuations. Therefore any deterministic exact future-accounting machine for this specialization requires at least `2^n` states.

This is a genuine local-description/global-deterministic-translator blow-up, but it is NOT a new GC-II theorem mechanism: it is the classical NFA-to-DFA/Myhill-Nerode exponential state-complexity phenomenon embedded in the GC-II trace semantics.

## Consequence for the research program
The mere existence of an exponential `K_G` family cannot be sold as the Paper-II breakthrough. A publishable GC-II strengthening must impose operational structure absent from ordinary automata -- e.g. vector budgets plus endogenous R/I/A/L changes, task-scale-error envelopes, or low-order/projection agreement inherited from GC-I -- and then prove a lower bound that is not just determinization in disguise.

A valid future target is therefore:

> Construct natural GC-II worlds `W_n,W'_n` whose prescribed low-order task/resource projections agree, but for which every exact shared operational translator/accounting quotient separating their whole envelopes has superpolynomial complexity under an explicitly stated translator model.

This target is OPEN. Any proof must be collision-checked against automata state complexity, communication complexity, branching programs/OBDDs, CSP/database width, marginal/contextuality reconstruction, and GC-I proper-projection irreducibility.

## Status
- Minimal exact deterministic accounting-state count equals `K_G`: **PROVED** in the finite deterministic trace specialization.
- Exponential `K_G` family: **IMPORTED/KNOWN** via Myhill-Nerode / subset-construction state complexity.
- Exponential lower bound as GC-II novelty: **FALSIFIED** if based only on generic nondeterminism-to-determinism.
- Structured GC-I-to-GC-II local-to-global translator lower bound beyond automata determinization: **OPEN**.
- Breakthrough status: **NONE**.
