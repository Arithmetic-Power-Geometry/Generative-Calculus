# GC-II Audit 239 — Minimum admissibility-repair gap

## Setup
Finite worlds W, projection p:W->Z, required decision g:W->D, finite message alphabet M, and admissibility lists L(w) subseteq M. An exact translator selects m(w) in L(w) such that (p(w),m(w)) determines g(w).

Only one primitive augmentation is charged in this audit: adding a missing incidence (w,a) to L. Each such edit has unit cost. p, g, W and M are fixed.

For a fiber z and labeling lambda_z:M -> D_z union {unused}, where D_z={g(w):p(w)=z}, require every d in D_z to label at least one message. Define

q_z(lambda)=#{w:p(w)=z and there is no a in L(w) with lambda_z(a)=g(w)}.

Define the directed admissibility-repair gap

Omega_add(L;p,g,M) = sum_z min_lambda q_z(lambda),

with Omega_add=infinity if some |D_z|>|M|.

## Theorem (exact repair formula) — PROVED
Omega_add equals the minimum number of missing world-message incidences that must be added to make an exact admissible translator feasible.

Proof. Fix a fiber and a feasible post-repair translator. Label each used message by the unique decision decoded from (z,message), extending unused messages arbitrarily/unused. Every original world not already incident to a message carrying its required decision needs at least one new incidence, giving the lower bound q_z(lambda). Conversely, for any supported labeling lambda, add one incidence from each deficient world to any message labeled by its required decision; then every world can select a correctly labeled admissible message. Fibers are decoder-independent and add, proving equality.

## Immediate properties
- Omega_add >= 0 and has units of incidence edits.
- Omega_add=0 iff the Audit-238 translator is already feasible. PROVED.
- Monotonicity: adding admissibility incidences cannot increase Omega_add. PROVED.
- Single-edit sensitivity: one added incidence reduces Omega_add by at most 1. Thus |drop|<=1 for a single addition. PROVED.
- Fiber composition: Omega_add is additive across disjoint projection fibers under this edit model. PROVED.
- Alphabet obstruction: if |D_z|>|M| for any fiber, incidence additions alone cannot repair feasibility, so Omega_add=infinity. PROVED.
- This is directed: it measures augmentation-to-feasibility, not a symmetric distance and not yet a reversibility invariant.

## Exact verification
`experiments/gc2_audit239_minimum_admissibility_repair.py` compares the formula against brute-force enumeration of every incidence superset for n=0,1,2,3 worlds, binary p/g, two messages, and all four possible lists per world: 4,369 instances. It also checks zero iff feasible and one-incidence monotonicity/1-Lipschitz behavior. Local independent execution: PASS on all 4,369 instances.

## Novelty / collision boundary
The GC interpretation is useful, but minimum repair of a finite constraint system is adjacent to established weighted/valued CSP, MaxSAT/minimum-violation, list-coloring/precoloring-extension, and cost-coloring formulations. Therefore the optimization mechanism itself is IMPORTED/KNOWN territory and is not claimed as a GC-II breakthrough.

The candidate GC-specific object is the typed extension in which R,I,A,L operations *generate* incidence edits with coupled costs/side effects. The present Omega_add is an exact base case and falsification oracle for any proposed coarser accounting law.

## Status ledger
- Exact incidence-repair formula: PROVED.
- Zero-gap iff exact translator feasible: PROVED.
- Monotonicity and single-addition 1-Lipschitz law: PROVED.
- Fiber additivity under fixed p,g,M and incidence-only edits: PROVED.
- Generic minimum-repair optimization as GC novelty: IMPORTED/KNOWN / NOT CLAIMED.
- Omega_add as full GC Generative Novelty Gap across R,I,A,L: OPEN / NOT CLAIMED.
- Typed operational closure inducing edits and a non-generic accounting bound: OPEN.
