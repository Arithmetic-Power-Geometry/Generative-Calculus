# GC-II Audit 347 — Witness-antichain realizability caution

## Status

- Minimal witness families are antichains: **PROVED** (Audit 346).
- Restricted Sperner diversity ceiling for arbitrary antichains: **IMPORTED/KNOWN**.
- Treating every antichain as realizable by directed operational reachability: **UNJUSTIFIED / OPEN**.
- Using the Sperner ceiling as a sharp reachability bound: **NOT CLAIMED**.

## Why this audit is needed

Audit 346 correctly gives a universal combinatorial ceiling for a minimal-witness family on a ground set of `m` newly grounded operations when every witness has size at most `lambda`. But the operational witnesses in the present GC-II reachability model are not arbitrary subsets: after baseline contraction/cycle deletion, they must arise from directed source-target witness paths (or baseline-interleaved macro-paths). Therefore the class of realizable witness hypergraphs can be strictly smaller than the class of all antichains.

The safe implication is one-way:

> operational minimal-witness family => antichain => restricted Sperner ceiling.

The converse is not assumed.

## Immediate consequence

The Audit-346 bound

`nu <= max_{0 <= k <= lambda} binom(m,k)`

is a valid outer bound, but it must not be advertised as a tight operational capability-accounting law without a realizability theorem or matching operational extremizers.

This matters because Paper II seeks semantic capability accounting rather than a merely set-theoretic envelope. Any future use of `nu` should distinguish:

1. arbitrary-antichain diversity;
2. directed-path witness diversity;
3. baseline-interleaved operational witness diversity.

## Next mathematical target

Characterize, or tightly bound, the hypergraphs realizable as inclusion-minimal new-operation witness sets for one ordered capability pair `(s,t)` under a fixed baseline preorder. A useful result would either:

- give necessary and sufficient realizability conditions; or
- derive an operationally sharper extremal bound on `nu` in terms of `(q,m,lambda)`.

Until then, Audit 346 remains a consistency constraint rather than a breakthrough quantitative bridge from `(Delta R, Delta I, Delta A, Delta L)` to `Omega_G`.
