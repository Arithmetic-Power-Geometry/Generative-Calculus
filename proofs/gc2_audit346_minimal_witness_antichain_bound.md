# GC-II Audit 346 — Minimal-witness antichain bound

## Status

- Minimal-witness antichain lemma: **PROVED**.
- Restricted Sperner diversity bound: **PROVED / IMPORTED-KNOWN combinatorics**.
- Resulting interaction-order bound: **PROVED**, but generally weaker than the exact witness-union rank rho and therefore not promoted as a breakthrough theorem.
- Four-coordinate bridge: **OPEN**.

## Setup

Fix a baseline operational closure B, a finite set E of m newly grounded operations, and a potentially novel ordered pair p. Let W_p be the family of inclusion-minimal subsets W subseteq E such that p is reachable in TC(B union W) but not in B. Define

- lambda_p = max{|W| : W in W_p}, with 0 if W_p is empty;
- nu_p = |W_p|;
- rho_p = | union_{W in W_p} W |.

Audit 343 proved that a nonzero pairwise Möbius coefficient j_p(T) can occur only when T is a union of members of W_p, hence |T| <= rho_p. Audit 345 used rho_p <= lambda_p nu_p.

## Lemma 1 — minimal witnesses form an antichain

For any W1,W2 in W_p, W1 subsetneq W2 is impossible. If it held, W2 would not be inclusion-minimal because W1 already succeeds. Thus W_p is an antichain in the Boolean lattice 2^E.

## Theorem 1 — diversity cannot be arbitrary once grounded support is fixed

Let m=|E|. Since W_p is an antichain and every member has size at most lambda_p, the restricted Sperner/LYM bound gives

nu_p <= max_{0 <= k <= lambda_p} binom(m,k).

Equivalently,

nu_p <= binom(m, min(lambda_p, floor(m/2)))

when lambda_p >= 1 (with the evident empty-family convention).

This is classical extremal-set combinatorics; GC-II imports the result rather than claiming novelty for Sperner/LYM.

## Corollary — grounded-support interaction ceiling

Combining Audit 345 with Theorem 1,

rho_p <= min{m, lambda_p nu_p}
      <= min{m, lambda_p * max_{0<=k<=lambda_p} binom(m,k)}.

Therefore j_p(T)=0 whenever

|T| > min{m, lambda_p nu_p}.

The explicit m ceiling is exact at the representation level because T subseteq E. The antichain theorem is useful mainly as a consistency constraint on proposed semantic coordinates: lambda and nu are not freely specifiable once the grounded support m is fixed.

## Edge and invariance checks

- E empty: W_p empty and all quantities vanish.
- lambda_p=0: only the empty witness could occur; for baseline-novel p this cannot be a successful witness, so W_p is empty.
- Duplicate syntax representing the same grounded operation must be quotiented before m is computed; otherwise m and the bound are representation-dependent.
- Relabelling operational states or grounded-operation identifiers preserves m, lambda_p, nu_p, rho_p and the inequalities.
- The theorem concerns finite grounded E; no finite-cardinality claim is made for infinite operation families.

## Scientific consequence

Audit 344 showed that locality lambda alone cannot control interaction order. Audit 345 repaired this with lambda times diversity nu. Audit 346 now shows that nu itself is constrained by the size m of the grounded operational support. This does **not** solve the Paper-II accounting problem: schema-count Delta A/Delta L need not control m (Audit 340). The remaining bridge must therefore charge semantic grounding/support or prove that the resource/information/interface/rule budget controls it.
