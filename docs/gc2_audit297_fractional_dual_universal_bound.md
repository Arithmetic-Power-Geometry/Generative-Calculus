# GC-II Audit 297 — Universal fractional-dual accounting bound

## Target
Extend Audit 296 beyond bipartite frequency-two incidence without falsely treating the LP dual as complete.

## Finite operational accounting instance
Let `Y` be the finite set of targets and `A` the finite decoder-action set. At tolerance epsilon define

B_epsilon(a) = { y in Y : ell(y,a) <= epsilon }.

Audit 290 identifies the exact worst-case account size N_epsilon with the minimum feasible-action cover.

Define target frequency

f(y) = |{a in A : y in B_epsilon(a)}|,

and assume 1 <= f(y) <= f for all y (uncovered targets are infeasible and excluded from the theorem).

The fractional relaxation is

P* = min sum_a x_a
subject to sum_{a:y in B_epsilon(a)} x_a >= 1 for every y,
x_a >= 0.

Its dual is

D* = max sum_y z_y
subject to sum_{y in B_epsilon(a)} z_y <= 1 for every a,
z_y >= 0.

Finite LP duality gives P*=D*.

## Theorem 297.1 — universal bounded-frequency rounding certificate
For every finite feasible instance with maximum target frequency f,

D* = P* <= N_epsilon <= f P* = f D*.

Hence the fractional dual is always a multiplicative f-certificate of exact capability-account size.

### Proof
The lower bound P* <= N_epsilon is relaxation.

Let x* be an optimal fractional cover and choose

C = {a : x*_a >= 1/f}.

For every target y, at most f actions contain y and their x*-weights sum to at least 1. Therefore at least one incident action has x*_a >= 1/f, so C covers Y. Moreover, for every selected a, 1 <= f x*_a. Thus

|C| <= f sum_a x*_a = f P*.

Since N_epsilon is the minimum integral cover, N_epsilon <= |C| <= fP*. QED.

## Edge and degenerate cases
- Empty Y: N=P*=D*=0.
- Any uncovered target: no finite account exists; theorem hypothesis fails explicitly.
- f=1: N=P*=D* exactly.
- f=2: universal factor-2 certificate; Audit 296 strengthens this to equality on bipartite incidence graphs.
- Duplicate targets or duplicate actions do not invalidate the proof.
- Zero-weight actions are never selected by the threshold unless required through another positive coordinate.

## Composition / monotonicity
Adding decoder actions can decrease both N and P*, but can increase maximum frequency f; therefore fP* is a certificate, not a monotone under arbitrary interface enrichment. Removing feasible incidences may increase N/P* or make the instance infeasible. The theorem is invariant under relabeling targets/actions and duplication of identical target constraints, although duplicated targets alter the dual representation without altering the primal optimum.

## Tightness warning
The factor f is a general rounding guarantee, not asserted optimal. For frequency two, graph vertex-cover theory gives the sharper classical integrality-gap bound <=2, with bipartite equality N=P*. Odd cycles from Audit 296 show strict N>P* already at f=2.

## Prior-art collision status
The theorem is the standard bounded-frequency set-cover LP rounding argument and is therefore **IMPORTED/KNOWN mathematics**, not a novelty claim. Its GC-II role is structural: it turns an efficiently computable fractional dual into a certified quantitative interval for operational account size even where exact dual completeness fails.

This matters for Paper-II item (6): a complete scalar dual generally fails, but a bounded-frequency operational interface yields a finite computable certificate family with explicit approximation factor.

## Status
- `P*=D* <= N_epsilon`: **PROVED** (finite LP duality + relaxation; imported machinery).
- `N_epsilon <= f P*`: **PROVED** by threshold rounding.
- Exact dual completeness for arbitrary incidence: **FALSIFIED** already by Audit 296.
- Equality for bipartite frequency-two incidence: **PROVED** in Audit 296 via imported Kőnig/TU theory.
- Factor f optimality: **NOT CLAIMED / OPEN here**.
- Novelty of bounded-frequency LP rounding: **IMPORTED/KNOWN**.

## Paper-II consequence
Do not state that the fractional dual is universally complete. The defensible hierarchy is

exact on integral subclasses (e.g. bipartite frequency-two) -> bounded-factor certificate under bounded target frequency -> unrestricted set-cover hardness.
