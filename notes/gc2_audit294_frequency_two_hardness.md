# GC-II Audit 294 — Frequency-two hardness of exact lossy capability accounting

## Question
Does a very small per-target decoder ambiguity restore tractability after Audits 290–293?

## Setup
For finite attainable states `Y`, decoder actions `A`, loss `ell`, and tolerance `epsilon`, define

`B_epsilon(a) = { y in Y : ell(y,a) <= epsilon }`.

The target frequency is

`f(y) = |{a in A : y in B_epsilon(a)}|`.

Audit 290 proved that the minimum deterministic worst-case faithful account size is the minimum number of feasible-action sets covering `Y`.

## Theorem candidate — Frequency-two hardness

**PROVED (conditional only on the imported classical NP-completeness of VERTEX COVER).**

Exact minimum-state worst-case capability accounting remains NP-hard even under all of the following restrictions simultaneously:

1. binary dimensionless loss `ell in {0,1}`;
2. exact tolerance `epsilon = 0`;
3. every attainable target is feasible under exactly two decoder actions, i.e. `f(y)=2`.

The corresponding decision problem is NP-complete for explicit finite incidence input.

### Reduction
Take an arbitrary simple undirected graph `G=(V,E)` with no self-loops. Construct:

- one attainable state `y_e` for each edge `e in E`;
- one decoder action `a_v` for each vertex `v in V`;
- `ell(y_e,a_v)=0` iff vertex `v` is incident to edge `e`, and `1` otherwise;
- `epsilon=0`.

Then every target `y_{uv}` is feasible under exactly the two actions `a_u,a_v`. A collection of decoder actions covers all attainable targets iff the corresponding vertices cover every edge. Hence

`N_0(instance(G)) = tau(G)`, 

where `tau(G)` is the minimum vertex-cover number.

The construction is polynomial in `|V|+|E|`. Membership of the accounting decision problem in NP follows by checking a proposed action set against the explicit incidence table. Therefore classical VERTEX-COVER NP-completeness transfers exactly.

## Boundary / anti-overclaim

This falsifies the tempting statement

> bounded target frequency, even frequency two, implies polynomial-time exact capability accounting.

It does **not** imply that every frequency-two subclass is hard. Under this reduction, if the action-incidence graph is bipartite, the problem is minimum vertex cover on a bipartite graph and is polynomial-time solvable via the classical Konig/matching structure. Thus frequency alone is insufficient; global incidence structure matters.

Frequency one is trivial: each target has a unique feasible action, so every action required by at least one target is forced. Hence the unrestricted complexity transition is already sharp in the frequency parameter:

- `max f <= 1`: polynomial/trivial;
- `max f <= 2`: NP-hard in general.

## Dimensional/domain audit

- Loss is dimensionless and binary; no unit mismatch.
- `epsilon=0` is in the loss domain.
- Empty-edge graph maps to `Y=empty` and optimum `0`.
- Isolated graph vertices create actions covering no target and do not affect the optimum.
- Parallel edges are unnecessary; the proof uses simple graphs.
- Self-loops are excluded because they would have frequency one, although they do not threaten hardness after preprocessing.
- Monotonicity: adding decoder actions cannot increase the cover optimum; the reduction uses exactly one action per graph vertex.
- Relabeling invariance: graph isomorphisms induce accounting-instance isomorphisms and preserve the optimum.
- Composition: no closure claim is made. Disjoint union gives additive vertex-cover/accounting optima, but arbitrary operational composition may add cross-incidences.

## Prior-art collision audit

The computational mechanism is **IMPORTED/KNOWN**: minimum VERTEX COVER is classical NP-complete, and the incidence duality here is the standard relationship between covering edges by vertices and a frequency-two set-cover instance. No novelty is claimed for that combinatorial fact.

The GC-II consequence is a structural negative result for the capability-accounting program: local decoder ambiguity bounded by two is not enough to yield a tractable complete accounting criterion. Any tractability theorem must exploit stronger global operational incidence structure (for example bipartiteness, interval structure, bounded treewidth plus a suitable representation, or another independently testable restriction).

## Exact finite verification

`experiments/gc2_audit294_frequency_two_verifier.py` enumerates all labeled simple graphs through five vertices, constructs the accounting incidence instance, brute-forces both minimum vertex cover and minimum action cover, verifies equality, verifies exact target frequency two, and checks empty/isolated/disconnected boundary cases.

## Status

- frequency-two reduction: **PROVED**;
- exact accounting NP-hard under target frequency exactly two: **PROVED via IMPORTED/KNOWN VERTEX-COVER hardness**;
- decision version NP-complete on explicit incidence input: **PROVED via IMPORTED/KNOWN complexity theory**;
- bounded-frequency-implies-tractable conjecture: **FALSIFIED**;
- frequency-one exact tractability: **PROVED**;
- generic Vertex Cover / frequency-two Set Cover mechanism: **IMPORTED/KNOWN**;
- strongest operationally natural global incidence condition supporting complete tractability: **OPEN**.
