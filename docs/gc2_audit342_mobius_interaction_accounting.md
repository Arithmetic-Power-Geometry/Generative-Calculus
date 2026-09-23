# GC-II Audit 342 — Exact Möbius interaction accounting

## Scope
This audit attacks the multi-capability interaction problem left open by Audit 341. GC-I on `main` is untouched.

## Setup
Let `B` be a finite baseline reachability preorder on state set `Q`, and let `E` be a finite set of newly grounded directed transitions. For `S ⊆ E`, define

`N_B(S) = TC(B ∪ S) \ B`, and `f_B(S)=|N_B(S)|`.

Thus `f_B(∅)=0` and the raw Generative Novelty Gap is `Omega_pair(E|B)=f_B(E)`.

For every nonempty `S⊆E`, define the interaction coefficient

`J_B(S) = Σ_{T⊆S} (-1)^(|S|-|T|) f_B(T)`.

## Theorem 342.1 — Exact interaction decomposition [PROVED]
For every finite `E`,

`Omega_pair(E|B) = Σ_{∅≠S⊆E} J_B(S)`.

### Proof
This is Möbius inversion on the Boolean subset lattice. By definition `J` is the Möbius transform of `f`; inversion gives `f(S)=Σ_{T⊆S}J(T)`. Since `f(∅)=J(∅)=0`, substituting `S=E` proves the identity. No independence, additivity, acyclicity, antisymmetry, or disjointness assumption is used.

## Theorem 342.2 — First-order term recovers Audit 341 [PROVED]
For a singleton `S={e}`, `J_B({e})=f_B({e})`. Hence if `e=(u,v)` is absent from `B`, Audit 341 gives

`J_B({e}) = |(Pred_B(u) × Succ_B(v)) \ B|`.

Thus Audit 341 is exactly the first-order sector of the interaction expansion.

## Theorem 342.3 — Interaction coefficients are signed [PROVED]
Higher-order interaction is not universally synergistic.

Positive example: let `B` be identity on `{0,1,2}`, `e1=(0,1)`, `e2=(1,2)`. Then `f({e1})=f({e2})=1`, while `f({e1,e2})=3` because `(0,2)` appears only compositionally. Therefore `J({e1,e2})=+1`.

Negative example: let baseline contain identity plus `0→1`, and add `e1=(0,2)`, `e2=(1,2)`. Then `f({e1})=1`, `f({e2})=2`, and `f({e1,e2})=2`; therefore `J({e1,e2})=-1`. The negative coefficient records overlap/redundancy rather than capability loss.

Consequently any universal GC-II accounting ansatz requiring all nonlinear interaction terms to be nonnegative is falsified.

## Theorem 342.4 — No fixed interaction-order truncation is universally exact [PROVED]
For every `k≥2`, take identity baseline on states `0,...,k` and new edges `e_i=(i-1,i)`, `i=1,...,k`. The endpoint capability `0→k` exists only when all `k` new edges are present. Its indicator set-function has a nonzero order-`k` Möbius coefficient. Therefore arbitrarily high interaction order is required as system size grows.

This is consistent with the earlier unbounded-interaction warning in Audit 226, now tied directly to raw novelty accounting.

## Structural consequences
1. The exact nonlinear expansion exists without assuming additivity.
2. `J_B(S)` is contextual: it depends on baseline closure `B`, not only on the syntax of `S`.
3. Signed terms separate synergy (`J>0`) from overlap/redundancy (`J<0`), but the sign is an inclusion–exclusion property and must not be interpreted automatically as physical benefit/harm.
4. Exact accounting can be exponentially large (`2^|E|-1` coefficients). A useful Paper-II theorem therefore needs structural conditions that force high-order `J_B(S)` to vanish, decay, or admit a compact dual representation.

## Edge/degenerate checks
- `E=∅`: both sides are zero.
- Duplicate syntax denoting the same grounded edge must be quotient-deduplicated before defining `E`; otherwise coefficients become representation-dependent.
- Self-loops already in a reflexive baseline contribute zero.
- Cycles and non-antisymmetric baselines are allowed because only transitive closure is used.
- Relabelling states preserves all `f_B(S)` and hence all `J_B(S)`.
- Monotonicity: `f_B(S)` is monotone in `S`; individual `J_B(S)` need not be nonnegative.

## Prior-art collision status
The transform itself is classical Möbius inversion / inclusion–exclusion on the Boolean lattice and is therefore **IMPORTED/KNOWN**. The reachability mechanism is classical transitive closure. No novelty is claimed for either. The GC-II contribution at this stage is architectural: it supplies an exact, falsifiable nonlinear accounting language connecting Audit 341's contextual single-edge exposure to arbitrary finite sets of newly grounded capabilities, and it proves that interaction signs and orders cannot be restricted universally.

## Status
- exact Möbius decomposition: **PROVED / IMPORTED-KNOWN mechanism**
- Audit-341 first-order recovery: **PROVED**
- universal nonnegative interaction coefficients: **FALSIFIED**
- universal fixed-order truncation: **FALSIFIED**
- compact structural conditions for bounded interaction order: **OPEN**
- bridge from `(Delta R, Delta I, Delta A, Delta L)` to bounded/decaying interaction spectrum: **OPEN**
