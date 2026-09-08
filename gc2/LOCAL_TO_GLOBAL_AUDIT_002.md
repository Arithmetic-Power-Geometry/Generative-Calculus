# GC-II Local-to-Global Audit 002

Date: 2026-09-08

## Executive result

**DECISIVE REDIRECTION.** The naive candidate

`r_G(A,B)=k => no faithful translator using only <k-local primitives exists`

is **false without strong restrictions on composition/depth/communication**. Bounded-arity primitives can compose to compute globally dependent functions such as parity (e.g. a binary XOR tree), so primitive arity alone is not an obstruction. Ancillas/adaptivity make the unrestricted statement even less defensible.

This is a useful falsification: GC-II must not claim that high projection-distinguishing order by itself forces high primitive arity.

## Exact finite check

For the even- and odd-parity relations on `{0,1}^m`, exhaustive enumeration for `m=2,...,7` confirms:

- every projection onto fewer than `m` coordinates is the full projected cube for both relations;
- the first distinguishing projection has order exactly `m`;
- joining/intersecting all proper projections reconstructs the entire Boolean cube, not either parity relation.

Thus the GC-I projection obstruction is correct as a relation-reconstruction fact, but it does **not** imply a translator lower bound unless the translator model is independently resource-restricted.

## Prior-art collision

The unrestricted direction collides with mature areas:

1. Database theory already studies lossless join reconstruction and join dependencies: a relation need not be recoverable from its proper projections.
2. CSP/local-consistency theory explicitly separates local consistency information from global solvability and studies consistency reductions.
3. Circuit complexity supplies genuine resource-sensitive parity lower bounds only after circuit resources are specified (depth, gate set, size, geometry, ancillas, etc.). Recent QAC0 results likewise show parity lower bounds/tradeoffs under explicit depth/ancilla/locality restrictions.

Therefore `r_G` alone is not a novel operational lower-bound theorem.

## Strongest surviving GC-II target

Replace arity-only obstruction by a **resource-accounted reconstruction/translation complexity**.

For an envelope `E`, observation family `P_<k(E)` (all permitted projections/observations below order k), translator class `H`, and resource budget `B`, define provisionally

`K_G(E | P_<k(E); H) = inf { C_H(tau) : tau(P_<k(E)) = E }`,

with `+infinity` if no admissible reconstruction exists.

For approximate reconstruction use

`K_G^eps(E | P_<k(E); H) = inf { C_H(tau) : D_G(tau(P_<k(E)), E) <= eps }`.

This quantity is only worth retaining if `C_H`, `D_G`, and the observation interface are specified independently of the target relation and if the resulting lower bound is not merely a known circuit/database/CSP complexity measure.

### Candidate theorem target

Seek a family of **whole task-scale-error-budget envelopes**, not bare parity relations, for which all standard low-order/fixed-task summaries match but

`K_G^eps(E_n | P_<k(E_n); H_n) >= f(n,k,eps)`

under a natural translator model `H_n`, while a comparison family has asymptotically smaller reconstruction/translation cost.

The desired novelty is the coupling of task identity + scale + error + vector resources + one globally realizable translator. A parity-only lower bound is insufficient because it will inherit known circuit/CSP/database results.

## Required next falsification tests

1. Define at least two natural translator models: bounded-depth local circuits and sequential/adaptive translators with explicit communication/memory costs.
2. Check whether the proposed `K_G` reduces exactly to circuit size/depth, communication complexity, extension complexity, CSP width, or join-decomposition complexity in each specialization.
3. Search finite envelopes where fixed-task Pareto frontiers, all <k projections, and scalar resource summaries match, yet globally realizable translation costs differ.
4. Require a quantitative consequence on a task-scale-error-budget family before promoting any breakthrough candidate.

## Status ledger update

- Proper-projection parity obstruction: **PROVED / KNOWN mathematical mechanism**.
- `r_G=k => primitive arity >= k`: **FALSIFIED** in unrestricted compositional translator classes.
- Arity-only translator obstruction: **DROPPED as breakthrough route**.
- Resource-accounted reconstruction complexity `K_G`: **OPEN / PROVISIONAL**.
- Quantitative whole-envelope separation theorem: **OPEN; highest-priority surviving target**.

## Breakthrough status

No breakthrough claim. The current run removed an invalid inference and sharpened the target to a resource-sensitive whole-envelope reconstruction lower bound.