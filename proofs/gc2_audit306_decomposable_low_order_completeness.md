# GC-II Audit 306 — Decomposable low-order completeness boundary

## Status

- Unrestricted fixed-order interaction summaries are complete: **FALSIFIED** by Audit 305.
- Junction-tree clique marginals determine the full joint operational law: **PROVED under the stated decomposability assumptions; mechanism IMPORTED/KNOWN**.
- Low-order accounting is complete for a fixed decomposable operational class of treewidth `w`: **PROVED**.
- Treewidth alone, without the Markov/decomposability assumption on the operational law: **NOT SUFFICIENT** (consistent with earlier Audit 281).
- Generic junction-tree factorization as GC-II novelty: **NOT CLAIMED**.

## Why this audit

Audit 305 proves that no interaction hierarchy stopped below full order can be universally complete over unrestricted operational objects. The scientifically useful next question is positive: which independently testable structural assumption makes bounded-order accounting complete?

This audit gives one exact answer.

## Setup

Let `X=(X_1,...,X_d)` be a finite operational feature vector and let `G` be a fixed decomposable/chordal graph with maximal cliques `C_1,...,C_m` arranged as a junction tree `T`. For each tree edge `(i,j)`, write `S_ij=C_i intersect C_j` for its separator.

Consider strictly positive joint laws `P` that are Markov/factorizing with respect to `G`. Strict positivity is used here only to keep the ratio formula literal and avoid zero-denominator bookkeeping; equivalent conditional-kernel formulations can weaken it.

The junction-tree identity is

`P(x) = [prod_i P_Ci(x_Ci)] / [prod_(i,j in E(T)) P_Sij(x_Sij)]`.

Separator marginals are themselves obtained by marginalizing either adjacent clique marginal, so a consistent collection of clique marginals determines every separator marginal.

## Theorem 306.1 — clique-marginal completeness

Let `P` and `Q` be strictly positive joint laws on the same finite feature space, both Markov with respect to the same fixed decomposable graph `G`. If

`P_C = Q_C`

for every maximal clique `C` of `G`, then

`P = Q`.

### Proof

For every junction-tree edge, equality of the adjacent clique marginals implies equality of the induced separator marginal. Apply the junction-tree factorization to `P` and `Q`. Every numerator clique factor agrees and every denominator separator factor agrees pointwise. Strict positivity makes each separator denominator positive. Hence `P(x)=Q(x)` for every joint assignment `x`. QED.

## Corollary 306.2 — bounded interaction order is complete under bounded decomposable width

If the largest clique has size at most `w+1`, then marginals of order at most `w+1` containing the maximal-clique marginals form a complete accounting certificate inside this model class.

Thus, for two systems known independently to lie in the same fixed decomposable class,

`Delta_C=0 for every maximal clique C  =>  P=Q`.

Consequently every task whose value depends only on the joint law has zero novelty gap between them. In particular, for any bounded measurable task `u`,

`E_P[u]=E_Q[u]`.

This is the exact positive boundary missing from Audit 305: high-order parity information can hide from all proper marginals only because the unrestricted law is not constrained to be reconstructed from those local marginals.

## Corollary 306.3 — tree case

For a tree-structured operational law (`w=1`), singleton and edge-pair marginals suffice. With a rooted tree this is equivalently

`P(x)=P_r(x_r) prod_(v != r) P(x_v | x_parent(v))`,

and each conditional is determined by its edge marginal and parent marginal under positivity. Hence pairwise accounting, which Audit 305 falsifies universally, becomes complete on this explicitly restricted class.

## What is and is not being claimed

The junction-tree reconstruction theorem, decomposable graphical models, running-intersection property, and treewidth machinery are established graphical-model theory: **IMPORTED/KNOWN**.

The retained GC-II result is the operational boundary statement:

`unrestricted joint operational object -> no fixed submaximal interaction order is complete` (Audit 305),

whereas

`fixed decomposable Markov class of width w -> clique marginals of order <= w+1 are complete` (Audit 306).

This does not claim that treewidth alone solves capability accounting. The factorization/Markov assumption is essential. A graph drawn over variables does not force an arbitrary joint law to obey it.

## Edge, degeneracy, and invariance audit

- One clique containing all variables: theorem is tautologically true but gives no compression; certificate order is `d`.
- Independent variables: `w=0`; singleton marginals suffice.
- Tree models: `w=1`; pairwise edge marginals suffice.
- Zero-probability separators: excluded by the stated positivity assumption; conditional-kernel/disintegration formulations should be used before claiming the zero-support extension.
- Relabeling variables or junction-tree cliques preserves the criterion.
- Different junction trees for the same decomposable graph give the same reconstructed joint law when clique marginals are consistent.
- The result is exact, not approximate. Approximate stability requires a separate quantitative analysis because small separator probabilities can amplify ratio perturbations.
- Composition: disjoint products of width-`w1` and width-`w2` decomposable systems remain decomposable with maximum clique size `max(w1+1,w2+1)`; adding cross-system couplings can increase width and therefore certificate order.

## Collision checks

This result intentionally collides with decomposable graphical models, junction-tree factorization, database/join decomposability, CSP width, and local-to-global consistency. The generic mathematical reconstruction mechanism is therefore not novel. The useful GC-II content is the sharp assumption-sensitive repair of the Audit-305 no-go and the warning that bounded width without an actual factorization constraint is insufficient.

## Reproducibility

`experiments/gc2_audit306_junction_tree_reconstruction.py` exactly checks the smallest nontrivial chain `A-B-C` using rational arithmetic over a finite exhaustive family of strictly positive root-clique distributions and positive conditional kernels. It verifies reconstruction from `AB`, `BC`, and `B` marginals via

`P(a,b,c)=P_AB(a,b) P_BC(b,c) / P_B(b)`.
