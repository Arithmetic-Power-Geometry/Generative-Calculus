# GC-II Audit 337 — topology-sensitive amplification envelope

## Status

- Walk-envelope bound: **PROVED**.
- Strict improvement over the Audit-336 uniform branching envelope on some systems: **PROVED**.
- Generic path/walk-counting mechanism: **IMPORTED/KNOWN** graph theory.
- Claim that this is a new graph-theoretic theorem: **NOT MADE**.
- Bridge from `(Delta R, Delta I, Delta A, Delta L)` to the operational macro-transition matrix: **OPEN**.

## Setup

Let `Q={1,...,q}` be the finite operational quotient after baseline closure. Let `M` be the 0/1 adjacency matrix of the new baseline-saturated macro-step relation: `M_xy=1` iff one new macro-step can take class `x` to class `y`. A policy may use at most `h` new macro-steps. Baseline-novel reachability excludes the source class itself and any pair already available in the baseline relation.

For source `x`, define the length-at-most-`h` walk count

`W_h(x) = sum_{ell=1}^h (M^ell 1)_x`.

This counts walks, not distinct endpoints.

## Theorem 337.1 — walk envelope

Let `Omega_pair^(h)` be the number of baseline-novel ordered pairs obtainable with at most `h` new macro-steps. Then

`Omega_pair^(h) <= sum_x min(q-1, W_h(x)).`

A baseline-aware refinement replaces `q-1` by the number `u_0(x)` of target classes not already reachable from `x` under the baseline closure:

`Omega_pair^(h) <= sum_x min(u_0(x), W_h(x)).`

### Proof

Fix `x`. Every newly reachable target `z` has at least one macro-walk from `x` of some length `1 <= ell <= h`. Choosing one witnessing walk for every distinct novel target injects those targets into a subset of the set of all length-at-most-`h` walks only at the level of cardinality: the number of distinct endpoints cannot exceed the number of witnessing walks. It also cannot exceed the number `u_0(x)` of targets not already baseline-reachable. Therefore the number of novel targets from `x` is at most `min(u_0(x),W_h(x))`. Sum over sources. QED.

## Corollary 337.2 — Audit 336 recovered

If every row of `M` has at most `beta` ones, then `(M^ell 1)_x <= beta^ell`. Hence

`W_h(x) <= sum_{ell=1}^h beta^ell`

and Theorem 337.1 implies the Audit-336 bound

`Omega_pair^(h) <= q min(q-1, sum_{ell=1}^h beta^ell)`

when only the uniform state-count cap is used.

Thus Audit 336 is the degree-only relaxation of a topology-sensitive bound.

## Why this matters for GC-II

Audit 335 showed that reusable schemas can generate unbounded raw pair novelty when opportunity-space size and reuse depth grow. Audit 336 repaired this with `(q,beta,h)`. Audit 337 shows that `beta` is still a lossy summary: two systems with the same `q,beta,h` can have sharply different amplification because the arrangement of macro-transitions controls repeated composability. The operational transition geometry, or a justified compression of it, is therefore the natural intermediate accounting object.

This does **not** yet restore a theorem of the form `Omega_G <= F(Delta R,Delta I,Delta A,Delta L)`. Any such bridge must constrain `M` (or a sufficient invariant of `M`) from those deltas without representation-dependent rule counting.

## Edge and invariance checks

- `h=0`: both sides are zero.
- `M=0`: both sides are zero.
- Self-loops may increase walk counts but cannot create false violations because walks only upper-bound distinct endpoints.
- Cycles are allowed.
- Relabelling operational classes conjugates `M` by a permutation matrix and preserves the summed envelope.
- Duplicate syntactic rule names do not change `M`, so the bound is invariant to pure rule duplication.
- Composition is nonadditive: powers of `M` explicitly retain interaction among successive macro-steps.

## Prior-art boundary

Matrix powers counting directed walks, transitive closure/reachability, and degree/diameter growth bounds are classical. The theorem is used here as an exact architectural refinement of GC-II capability accounting, not claimed as new graph theory. The remaining potentially novel target is a representation-stable theorem connecting resource/information/interface/rule increments to a constrained operational transition geometry and then to novelty.
