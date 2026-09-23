# GC-II Audit 348 — Minimal-witness / minimal-obstruction blocker duality

## Status

- Minimal new-operation witnesses for one ordered capability pair form a clutter: **PROVED** (Audit 346).
- In the baseline-contracted directed-edge model, minimal witness sets and minimal operation-cut sets are blocker duals: **PROVED / IMPORTED-KNOWN mechanism**.
- Using arbitrary antichains as operational witness families: **still OPEN / not assumed** (Audit 347).
- A new sharp extremal diversity bound from blocker duality alone: **NOT CLAIMED**.

## Setup

Fix a finite baseline-contracted directed operational graph `G=(V,E)` and an ordered capability pair `(s,t)`. Here each member of `E` is one distinct newly grounded operation/transition. Baseline motion has already been contracted into the operational quotient, so a witness is represented by the set of new edges used by an `s-t` path.

Let `P_st` be the family of inclusion-minimal subsets `W subseteq E` such that the subgraph `(V,W)` contains an `s-t` directed path. Let `C_st` be the family of inclusion-minimal subsets `C subseteq E` whose deletion destroys every `s-t` directed path.

For a clutter `H` on ground set `E`, define its blocker

`b(H) = { inclusion-minimal T subseteq E : T intersects every H in H }`.

## Theorem — operational witness/obstruction duality

For the finite directed-edge model,

`C_st = b(P_st)`

and

`P_st = b(C_st)`.

### Proof

A set `C subseteq E` destroys all `s-t` paths iff it intersects the edge set of every `s-t` path. Because every finite `s-t` path contains an inclusion-minimal `s-t` witness, this is equivalent to `C` intersecting every member of `P_st`. Taking inclusion-minimal such `C` gives `C_st=b(P_st)`.

Conversely, finite blocker duality for clutters gives `b(b(H))=H`. Since `P_st` is a clutter, `P_st=b(C_st)`.

No probability, additivity, acyclicity, or uniqueness assumption is used. Parallel alternatives, cycles, and overlapping witnesses are allowed; cycles disappear from inclusion-minimal path witnesses by cycle deletion.

## Closure-escape criterion in dual form

For any supplied operation set `S subseteq E`, the capability `s -> t` is available exactly when

`exists W in P_st with W subseteq S`.

Equivalently, it is unavailable exactly when the missing-operation set `E \ S` contains a transversal obstruction sufficient to hit every witness. In particular, complete capability failure under edge deletion is certified by a member of `C_st`.

This supplies two exact finite certificates for the same operational question:

1. **constructive certificate:** a minimal witness/path;
2. **obstruction certificate:** a minimal cut/transversal.

The equivalence is useful for GC-II because witness diversity `nu=|P_st|` has a dual obstruction complexity `kappa=|C_st|`; either side can be exponentially larger than a compact graph description, so neither should be silently treated as a low-dimensional semantic charge.

## Relation to Audits 343–347

Audit 343 expresses nonlinear interaction coefficients through unions of minimal witnesses. Audit 348 shows that the same witness clutter is exactly recoverable from its minimal obstruction clutter. Therefore an interaction model based on witness unions can, in principle, be generated from obstruction data by blocker dualization, but this does **not** imply efficient enumeration.

Audit 347 remains necessary: blocker duality characterizes the dual of a *realized* path clutter; it does not prove that every abstract antichain is realizable as the path clutter of a directed operational graph with one unique grounded edge per operation.

## Complexity caution

Hypergraph transversal/blocker generation is a classical problem and can have exponential output. This audit therefore does not claim a polynomial complete monotone family. It identifies the exact dual certificate structure that any such compression would have to preserve.

## Edge and degeneracy checks

- If `s=t`, the empty path must be handled separately; for GC-II novelty pairs use `s != t`.
- If no `s-t` path exists in `G`, `P_st` is empty and blocker conventions require care; the theorem is used on the nondegenerate reachable case.
- Duplicate syntax denoting the same grounded edge must be quotient-identified before forming `E`.
- Relabelling vertices or grounded operations preserves the blocker relation.
- Adding irrelevant edges changes the ambient ground set but does not create a witness unless they participate in an `s-t` path; minimal cuts are interpreted relative to the chosen operational ground set.

## Scientific consequence

The next realizability target can be sharpened: characterize those clutters `H` for which both `H` and `b(H)` can simultaneously be represented as the minimal path and minimal cut families of one finite directed operational graph. Until such a characterization or sharper extremal theorem is obtained, the restricted Sperner ceiling from Audit 346 remains only an outer combinatorial bound.
