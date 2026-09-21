# GC-II Audit 291 — Computational barrier for optimal lossy capability accounting

## Scope
Branch-only Paper-II audit. GC-I/main is unchanged.

## Starting point
Audit 290 proved that for finite attainable states `Y`, decoder actions `A`, and tolerance `epsilon`, the minimum number of deterministic summary states is the minimum cover number of the feasible-action sets

`B_epsilon(a) = { y in Y : ell(y,a) <= epsilon }`.

## Theorem 291.1 — exact computational equivalence
For explicitly represented finite feasible-action systems, computing the minimum number `N_epsilon` of worst-case-epsilon-faithful summary states is exactly SET COVER.

**Status: PROVED, with the generic SET COVER problem IMPORTED/KNOWN.**

### Proof
Audit 290 already maps every accounting instance to the set-cover instance with universe `Y` and set family `{B_epsilon(a): a in A}`; the optima are identical.

Conversely, given an arbitrary finite SET COVER instance `(U,S)`, construct an accounting instance with `Y=U`, one decoder action `a_S` for each `S in S`, tolerance `epsilon=0`, and loss

`ell(u,a_S)=0` if `u in S`, and `1` otherwise.

Then `B_0(a_S)=S` exactly. Therefore every set-cover instance is an exact zero-loss accounting instance and the optimum values coincide. The transformations in both directions are polynomial in the explicit incidence representation.

Hence exact optimal finite lossy capability accounting is NP-hard. Its decision version (`N_epsilon <= k?`) is NP-complete for explicit finite incidence input: a chosen list of at most `k` actions is a polynomially checkable certificate.

## Corollary 291.2 — approximation barrier is inherited, not novel
Any approximation algorithm or hardness result for general SET COVER transfers immediately to unrestricted explicit feasible-action accounting. In particular, the classical logarithmic approximation landscape applies. This is IMPORTED/KNOWN algorithmic theory, not a GC-II novelty claim.

## Consequence for the Paper-II program
Audit 290 identified the correct finite object (a feasible-action hypergraph). Audit 291 now blocks a second shortcut: there cannot be a general efficient exact complete capability-accounting algorithm merely because the operational semantics have been reduced to finite feasible-action sets, unless P=NP.

The scientifically useful next target is therefore structural: identify operational assumptions that force tractable set systems (for example interval/laminar/convex/Helly-like structure, bounded frequency, bounded incidence width, or another independently measurable restriction), and prove the resulting criterion without defining the restriction in terms of the desired cover number itself.

## Domain and edge-case audit
- Empty `Y`: conventionally needs zero summary states; excluded from the NP-hardness reduction without loss.
- Uncovered target: `N_epsilon=infinity`; the reduction may restrict to ordinary coverable SET COVER instances.
- Duplicate actions/sets: harmless.
- Universal action: gives `N_epsilon=1`.
- Tolerance: hardness already holds at exact `epsilon=0`; no approximation tolerance is needed.
- Loss dimensions: binary dimensionless loss `{0,1}`; threshold `epsilon=0` has the same loss domain.
- Monotonicity: enlarging feasible sets cannot increase `N_epsilon`; inherited from set cover.
- Relabeling invariance: bijections of states/actions preserve the incidence hypergraph and `N_epsilon`.
- Composition: no additive/product law is claimed; arbitrary product composition can create nontrivial cover interactions.

## Prior-art collision status
The computational result is deliberately classified as IMPORTED/KNOWN at the combinatorial level. SET COVER is classical NP-hard optimization; Feige (JACM 1998, DOI 10.1145/285055.285059) establishes the classical near-logarithmic approximation threshold under its stated complexity assumption. Audit 291's role is to transfer that barrier exactly into the GC-II operational accounting object proved in Audit 290, not to claim a new complexity theorem.

## Status ledger
- finite lossy accounting optimum = feasible-action cover: **PROVED (Audit 290)**
- converse realization of every SET COVER instance as zero-loss capability accounting: **PROVED**
- exact accounting optimization NP-hard: **PROVED / IMPORTED mechanism**
- decision form NP-complete for explicit finite incidence input: **PROVED / IMPORTED mechanism**
- generic logarithmic approximation landscape: **IMPORTED/KNOWN**
- tractable non-tautological operational subclass: **OPEN**
- Helly/pairwise shortcut without additional assumptions: **FALSIFIED (Audit 290)**
