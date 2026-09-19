# GC-II Audit 263 — Serial-refinement invariance boundary for operational novelty

## Scope
Audit 262 left representation/generator refactoring invariance open. This audit proves one exact invariance class and records its boundary. The mechanism is graph/path equivalence and is not claimed as new mathematics.

Let `G=(X,E,c)` be a finite directed system with nonnegative costs. Pick an edge `e=(u,v)` of cost `k`. A **serial refinement** replaces `e` by a fresh state `z` and edges `(u,z)` of cost `a>=0`, `(z,v)` of cost `b>=0`, with `a+b=k`; `z` has no other incident edges. Call the refined system `R_e(G)`.

## Theorem 263.1 — exact value invariance on original states
For every pair of original states `x,y in X`,

`d_G(x,y)=d_{R_e(G)}(x,y)`.

Consequently, for every target `F subseteq X` containing only original states,

`V_G(x;F)=V_{R_e(G)}(x;F)` for all `x in X`.

### Proof
Map every `G` path to a refined path by replacing each traversal of `e` by `u->z->v`. Cost is unchanged because `a+b=k`. Conversely, because `z` is fresh and has exactly one incoming and one outgoing edge, every refined path between original states that visits `z` must traverse `u->z->v`; contract this pair to `e`, again preserving cost. Thus there is a cost-preserving correspondence between walks with original endpoints. Taking infima proves the distance identity, and minimising over `f in F` proves the target-value identity. QED.

## Corollary 263.2 — budgeted closure invariance
For every `B>=0`, membership of original states in `Cl_G^B(F)` is unchanged by serial refinement.

## Theorem 263.3 — Omega invariance under coherent refactoring
Let `G subseteq H` be baseline/extension systems on original state set `X`, with the same costs on baseline edges. Apply any finite sequence of serial refinements to baseline edges in both systems coherently, and independently refine extension-only edges in `H`. For original `x` and `F subseteq X`, whenever the finite scalar gap is defined,

`Omega_G^H(x;F)=Omega_{R(G)}^{R(H)}(x;F)`.

This follows immediately because both baseline and extension target values are individually preserved.

Thus Audit 262's cost-valued novelty is invariant to a nontrivial class of generator-language refactorings: splitting an operation into arbitrarily many private serial microsteps while preserving total cost cannot manufacture novelty.

## Boundary / counterexamples
The private-helper condition is essential. If the inserted state is exposed to another edge, subdivision can create new routes and alter capability. Example: baseline `u->v` cost 2 and `u->t` cost 10. Splitting `u->v` as `u->z` cost 1, `z->v` cost 1 preserves the original behavior only while `z` is private. Adding `z->t` cost 0 changes `V(u;{t})` to 1. This is not a mere refactoring; it changes the interface/action graph.

Likewise, targets containing the fresh helper state are not representation-equivalent tasks, so the theorem intentionally excludes them.

## Checks
- **Dimensions:** `a,b,k,B,V,Omega` all have cost units.
- **Zero-cost pieces:** allowed, including `a=0` or `b=0`.
- **Self loops:** the statement is cleanest for `u!=v`; self-loop subdivision is value-irrelevant under nonnegative costs but is not needed.
- **Unreachable states:** reachability among original states is preserved exactly.
- **Degenerate target:** empty targets remain unreachable; nonempty original-state targets satisfy the theorem.
- **Monotonicity:** unchanged; refinement neither improves nor worsens values on original states.
- **Composition:** arbitrary finite serial refinements compose by induction.
- **Invariance:** exact under private serial refinement; false once helper nodes acquire external interfaces.

## Status ledger
- Original-state shortest-path/value invariance under private serial refinement: **PROVED / IMPORTED-KNOWN mechanism**.
- Budgeted closure invariance under such refinement: **PROVED**.
- Audit-262 `Omega` invariance under coherent private serial refactoring: **PROVED**.
- Invariance under arbitrary generator refactoring: **OPEN / false without an operational-equivalence restriction**.
- Private-helper condition dispensable: **FALSIFIED**.
- Canonical GC-specific equivalence class for R/I/A/L implementations: **OPEN**.

## Novelty discipline
This is standard path-preserving graph refinement in mechanism. Its role is methodological: it establishes a minimum representation-stability test that any GC-II novelty or reversibility invariant should pass. The next target is a broader operational equivalence (e.g. cost-preserving simulation/bisimulation at exposed interfaces) and a proof that the proposed accounting descends to its quotient.