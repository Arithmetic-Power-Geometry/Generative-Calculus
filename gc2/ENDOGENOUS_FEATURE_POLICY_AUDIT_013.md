# GC-II Endogenous Feature-Policy Audit 013

## Status

**DECISIVE PRIOR-ART COLLISION / RESEARCH BOUNDARY.**

This audit asks whether replacing the static feature family in Audit 012 by features generated endogenously through admissible actions produces, by itself, a new Closure-Escape mechanism. In the finite deterministic specialization, it does not: the resulting object is an adaptive distinguishing/test policy (equivalently a finite active-information-gathering decision tree). The useful GC-II consequence is a precise boundary and an operational local-to-global lower bound, not a novelty claim for adaptive testing.

## Model

Let `T` be a finite set of hidden operational traces. Each trace `t` has required output `y(t)`. A policy sees an observation history. At each nonterminal history it may choose an admissible sensing/action `a`; executing `a` on trace `t` returns an observation `o_a(t)` and consumes resource cost `c(a) >= 0`. The policy must be **shared**: traces with identical histories receive the same next action. It succeeds when every leaf reached by the traces in that leaf has a single required output.

This explicitly couples:

- **R**: action/sensing budget;
- **I**: observations returned by actions;
- **A**: admissible action set;
- **L**: policy rules determining which actions may be selected after each history.

The static refinement theorem of Audit 012 is recovered when a fixed set of tests is selected nonadaptively and all their outcomes are exposed simultaneously.

## Theorem 13.1 — finite deterministic policy criterion

For a finite deterministic trace system and budget `B`, whole-envelope translation is possible iff there exists a rooted observation decision tree such that:

1. every internal node is labelled by an admissible action;
2. outgoing edges are labelled by the possible observations of that action;
3. along every root-to-leaf path, cumulative action cost is at most `B`;
4. every leaf is **target-pure**: all traces reaching it have the same required output.

### Proof

A successful shared policy induces exactly such a tree by unrolling its history-dependent action choices. Sharedness makes the next action a function of the common history, the budget condition gives (3), and correctness requires target-pure terminal histories, giving (4). Conversely, a tree satisfying (1)-(4) is itself a shared policy: follow the edge matching each observed response and output the unique target label at the reached pure leaf. QED.

**Classification:** PROVED, but the mechanism is imported/known in adaptive testing, decision-tree identification, active sensing, and POMDP-style information gathering.

## Corollary 13.2 — information lower bound

Suppose every admissible action has at most `q` possible observation outcomes and a starting observation fibre contains `m` distinct required target labels. Any successful worst-case policy needs depth

`d >= ceil(log_q m)`.

Reason: a depth-`d` q-ary tree has at most `q^d` leaves, while target purity requires at least `m` distinguishable terminal classes.

With unit action costs this gives a resource lower bound `B >= ceil(log_q m)`.

**Classification:** PROVED / IMPORTED-KNOWN counting mechanism.

## Minimal local-to-global witness

Take three traces `t0,t1,t2`, all initially observationally identical, with three different required outputs. Provide three unit-cost binary actions:

- `a0`: outcome 1 only on `t0`, else 0;
- `a1`: outcome 1 only on `t1`, else 0;
- `a2`: outcome 1 only on `t2`, else 0.

Every pair of traces is separable by some admissible one-step action. Nevertheless **no shared one-step policy succeeds**: whichever action is chosen, its zero branch contains two traces with different targets. A two-step adaptive policy succeeds (for example `a0`, then on outcome 0 use `a1`). Thus

`pairwise one-step separability != one-step whole-envelope convertibility`.

The exact worst-case budget is 2, matching `ceil(log_2 3)=2`.

This is a clean operational strengthening of the local-to-global warning, but not a new combinatorial phenomenon.

## Consequence for Omega_G

A defensible endogenous policy gap in this restricted model is

`Omega_policy(Q) = min_pi F(R(pi), I(pi), A(pi), L(pi))`

over successful shared policies `pi`, with `+infinity` if none exists. For pure unit sensing cost, its R-coordinate is the minimum worst-case decision-tree cost.

The zero-gap Closure-Escape statement remains valid only after the baseline context and zero-cost actions are specified carefully. Positive-definiteness of `F` is still required if `Omega=0` is to mean 'no augmentation'. Nonlinear cross-channel terms are allowed, but then triangle/subadditivity claims remain unavailable by Audit 010.

## Prior-art collision

The finite endogenous-feature specialization is squarely adjacent to established work on:

- adaptive distinguishing/separating sequences for finite-state systems;
- decision-tree/test-cover identification;
- active feature acquisition;
- active sensing and information-gathering POMDPs.

Therefore GC-II must **not** claim that history-dependent generation of distinguishing observations, or the decision-tree criterion above, is itself novel.

## Research implication

The remaining plausible GC-II frontier must involve structure absent from ordinary adaptive testing, for example one or more of:

1. transformations that change the capability envelope itself while simultaneously changing what can be observed;
2. coupled vector-resource budgets with noncommuting admissible transformations;
3. endogenous creation/removal of future actions and rules, not merely selection of tests from a fixed action alphabet;
4. whole-envelope approximation/error geometry across task-scale-error-budget coordinates;
5. a theorem relating such dynamic closure to GC-I projection irreducibility or translator complexity.

A Paper-II breakthrough should be sought there, not in relabelling active sensing or decision trees.
