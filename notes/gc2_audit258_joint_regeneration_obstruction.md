# GC-II Audit 258 — Joint-regeneration obstruction

## Status

- Per-atom regeneration costs as a complete semantic reversibility invariant: **FALSIFIED**.
- Joint capability regeneration can exceed every singleton regeneration cost: **PROVED by exact counterexample**.
- Any bound using only singleton regeneration costs and no interaction term: **FALSIFIED**.
- Hypergraph/joint-task regeneration profile as a complete invariant: **OPEN**.
- Generic task/resource conversion and nonadditive interaction mechanisms: **IMPORTED/KNOWN**; no novelty claim is made for those mechanisms.

## Setup

Fix a finite operational transition system with nonnegative edge costs. Let semantic atoms be `a,b,...`. For a state `x` and atom set `T`, define the exact regeneration cost

\[
C_x(T)=\inf\{c(\pi):\pi\text{ starts at }x\text{ and ends in a state whose signature contains }T\},
\]

with `+infinity` when no such path exists. This definition is operational once the target predicate `T subseteq S(z)` is fixed.

A tempting repair after Audit 257 is to replace raw lost-atom counts by singleton regeneration costs `C_x({a})`, perhaps using their maximum rather than their sum so exact aliases do not multiply the score.

## Exact obstruction

Take states `s,u,v,t` and zero-cost edges

- `s -> u`,
- `s -> v`,

with signatures

- `S(s)=empty`,
- `S(u)={a}`,
- `S(v)={b}`,
- `S(t)={a,b}`,

and no path from `s,u,v` to `t` and no edge joining the `a` and `b` branches.

Then

\[
C_s(\{a\})=0,\qquad C_s(\{b\})=0,
\]

but

\[
C_s(\{a,b\})=+\infty.
\]

Thus every atom is individually free to regenerate while their conjunction is impossible to regenerate.

A finite-gap variant adds one edge `s -> t` of cost `K>0`. Then

\[
C_s(\{a\})=C_s(\{b\})=0,\qquad C_s(\{a,b\})=K.
\]

Since `K` is arbitrary, there is no finite universal function `f` satisfying

\[
C_x(T)\le f((C_x(\{a\}))_{a\in T})
\]

for this operational class. In particular, max, sum, and every other function of singleton costs alone fail.

## Interaction quantity

For finite values define the joint regeneration excess

\[
J_x(T)=C_x(T)-\max_{a\in T}C_x(\{a\}).
\]

The counterexample has `J_s({a,b})=K`, while both singleton costs are zero. `J` therefore detects a genuine conjunction/interface obstruction missed by singleton accounting. It is not yet proposed as an intrinsic GC invariant: its behavior under semantic reparameterization, quotienting, composition, catalysts, and generator extension remains open.

## Consequences for GC-II

1. Audit 257's move from atom counts to regeneration cost is insufficient if regeneration is evaluated atom-by-atom.
2. A representation-invariant reversibility theory must account for **jointly demanded capability predicates**, not merely primitive coordinates.
3. Any proposed `R/I/A/L` capability bound needs interaction terms whenever successful capability requires simultaneous resources/information/actions/rules.
4. A plausible next object is a task-indexed regeneration profile `T -> C_x(T)` on operationally meaningful target predicates, followed by quotient/minimal-basis analysis. The full profile is intentionally not called novel: it is a task/value-function construction and collides with established planning/resource-conversion ideas.

## Edge cases

- `T=empty`: `C_x(T)=0`.
- Singleton `T`: no interaction excess by definition.
- Unreachable joint target: `C_x(T)=+infinity`; subtraction-based `J` should be treated in the extended reals rather than as a finite scalar.
- Adding admissible operations can only weakly decrease `C_x(T)` when existing costs/transitions are retained.
- Scaling every edge cost by `lambda>=0` scales every finite `C_x(T)` and finite `J_x(T)` by `lambda`.
- Exact alias duplication does not by itself solve the conjunction problem; whether aliases denote one operational predicate or multiple independently required predicates must be fixed before measurement.

## Novelty discipline

The scientific value of this audit is a no-go boundary for the GC-II candidate invariant, not a claim that joint-task nonseparability is new. Resource theories, planning/value functions, CSP/database interaction, and communication/information theory already contain nonseparable and contextual constraints. GC-II must derive any claimed novelty from its specific typed generative closure structure and a theorem not reducible to those established mechanisms.
