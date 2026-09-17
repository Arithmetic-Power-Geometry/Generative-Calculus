# GC-II Audit 210 — substrate lower-bound transport

## Candidate
Let a GC capability instance `x` admit a semantics-preserving reduction `rho` to a substrate problem `P`. Let `C_G(pi;x)` be GC implementation cost and `C_P(rho(pi);rho(x))` the substrate cost of the reduced implementation. Assume constants `alpha>0`, `beta>=0` such that every admissible GC implementation satisfies

`C_P(rho(pi);rho(x)) <= alpha C_G(pi;x) + beta`.

If every correct substrate implementation has cost at least `L_P(rho(x))`, then every correct GC implementation obeys

`C_G(pi;x) >= max(0,(L_P(rho(x))-beta)/alpha)`.

Hence the optimal GC cost satisfies the same bound.

## Proof
Correctness preservation makes `rho(pi)` a correct substrate implementation. Therefore `L_P <= C_P(rho(pi))`. Cost domination gives `C_P(rho(pi)) <= alpha C_G(pi)+beta`. Combining and rearranging yields `C_G(pi) >= (L_P-beta)/alpha`; nonnegative costs add the maximum with zero. Taking the infimum over correct GC implementations preserves the lower bound. QED.

## Audit
- Domains: `alpha>0`; `beta,L_P,C_G,C_P >=0`.
- Dimensions: `alpha` converts GC-cost units to substrate-cost units; `beta` has substrate-cost units.
- Degenerate `L_P<=beta`: only the trivial zero lower bound remains.
- Monotonicity: increasing `L_P` strengthens; increasing `alpha` or `beta` weakens.
- Composition: no additive composition theorem follows without additional assumptions on reductions/costs.
- Representation: invariant only under reductions preserving correctness and the stated cost domination.
- Counterexample gate: without cost domination, a zero-GC-cost implementation may map to arbitrarily costly substrate behavior, so no bound follows.

## Novelty collision
The theorem is a generic complexity/lower-bound reduction: distributed-computing literature already transports communication-complexity lower bounds through simulation/reduction theorems. Therefore the abstract transport theorem is not a GC-II breakthrough. A GC-specific result would need a nontrivial theorem deriving the reduction and cost domination from GC closure structure rather than assuming them.

## Status
- substrate lower-bound transport inequality: **PROVED / IMPORTED-KNOWN mechanism**
- abstract transport theorem as GC-II novelty: **FALSIFIED**
- universal positive lower bound without cost domination: **FALSIFIED**
- GC-structural derivation of a substrate reduction/cost domination: **OPEN**
