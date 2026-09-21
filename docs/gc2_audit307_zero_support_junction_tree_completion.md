# GC-II Audit 307 — Zero-support junction-tree completion

## Question inherited from Audit 306

Audit 306 proved clique-marginal completeness for strictly positive laws in a fixed decomposable Markov class and left the zero-support extension open. This audit removes strict positivity.

## Setup

Let G be a finite decomposable undirected graph with maximal cliques C_1,...,C_m arranged as a junction tree T. For an oriented tree edge i->j write S_ij=C_i∩C_j. Let P be any probability law on the finite product state space that is globally Markov with respect to G. No positivity assumption is imposed.

For a separator assignment s with P_S(s)>0 define the usual conditional kernel

    K_{j|S}(x_{C_j\S}|s)=P_{C_j}(x_{C_j})/P_S(s).

If P_S(s)=0, every global configuration extending s has probability zero because P_S(s) is the sum of their nonnegative masses. Hence the value of K on that null separator state is irrelevant; set it arbitrarily to a normalized kernel. Equivalently, in the clique/separator ratio one may use the convention that a branch with zero separator marginal contributes zero rather than form 0/0.

## Theorem 307.1 — zero-support clique completeness

For finite state spaces, if P and Q are globally Markov with respect to the same decomposable graph G and

    P_C = Q_C for every maximal clique C,

then P=Q, without any strict-positivity assumption.

### Proof

Root the junction tree at C_1 and expose its cliques in a parent-before-child order. For each non-root clique C_j, let S_j be its separator from its parent and R_j=C_j\S_j.

The running-intersection property makes S_j separate R_j from all variables already exposed outside C_j. Global Markovity therefore gives, on every separator assignment s of positive probability,

    P(R_j=r | previously exposed variables)=P(R_j=r | S_j=s).

The latter conditional is determined by the clique marginal P_{C_j} and its separator marginal P_{S_j}, and P_{S_j} itself is obtained by marginalizing P_{C_j}. If P_{S_j}(s)=0, every global atom extending s has mass zero, so no undetermined conditional on that null event can alter the joint law.

Starting with the root marginal P_{C_1}, induction over the junction tree therefore uniquely determines the probability of every global atom. The same reconstruction applies to Q. Equal clique marginals imply equal root marginal, equal separator marginals, and equal positive-support child kernels at every step; null-separator branches are zero for both. Hence P=Q. QED.

## Corollary 307.2 — bounded-order completeness survives structural zeros

If G has treewidth w, maximal-clique marginals of order at most w+1 remain a complete account within the class of finite laws globally Markov with respect to that fixed decomposable graph, even when the law has zeros.

For a tree (w=1), node/edge marginals remain complete under the tree-Markov assumption even with deterministic or impossible states.

## Exact chain identity with zeros

For A-B-C and A ⟂ C | B,

    P(a,b,c) = 0                                      if P_B(b)=0,
               P_AB(a,b) P_BC(b,c) / P_B(b)          if P_B(b)>0.

There is no 0/0 ambiguity in the operational reconstruction: a zero separator marginal kills the entire branch.

## Edge and degeneracy audit

- Empty/zero separator states: harmless; all extending atoms have zero mass.
- Deterministic variables: allowed.
- Disconnected decomposable graphs: the empty separator encodes component independence under global Markovity; P_empty=1.
- Single clique: theorem reduces to the tautological statement that the full marginal is the joint law.
- Relabeling: invariant under bijective relabeling of states and variables.
- Monotonicity in supplied clique information: deleting a required clique marginal can destroy uniqueness; adding redundant separator marginals changes nothing.
- Composition: disjoint products preserve decomposability and the reconstruction property.
- Without the Markov/factorization assumption: false, as the lower-order collision audits already show.
- For nondecomposable graphs: clique marginals need not provide this junction-tree reconstruction; no claim is made.

## Prior-art collision discipline

The mathematical mechanism is established decomposable graphical-model / junction-tree theory. Standard references represent decomposable distributions through clique and separator marginals, and sources explicitly note that junction-tree factorization need not require positivity. Therefore the zero-support reconstruction mechanism is IMPORTED/KNOWN, not claimed as a new theorem of probability theory.

GC-II consequence only: Audit 306's structural completeness boundary does not depend on strict positivity. Structural zeros do not by themselves reopen the high-order accounting obstruction of Audit 305 when the fixed decomposable Markov assumption is valid.

## Status

- zero-support clique-marginal completeness: PROVED (mechanism IMPORTED/KNOWN)
- strict positivity as necessary for Audit-306 completeness: FALSIFIED
- tree pairwise completeness with structural zeros: PROVED under tree-Markov assumption
- unrestricted pairwise completeness: remains FALSIFIED
- approximate stability under perturbed/inexact clique marginals: OPEN
- robustness when the assumed graph/Markov structure is misspecified: OPEN

## Literature collision pointers

- Junction-tree/decomposable factorization by clique and separator marginals is standard graphical-model theory.
- A useful explicit prior-art statement is that the junction-tree factorization extends to decomposable graphs and does not require positivity (Duke STA345 lecture notes, citing classical graphical-model literature).
- This audit therefore makes no novelty claim for the underlying reconstruction theorem.
