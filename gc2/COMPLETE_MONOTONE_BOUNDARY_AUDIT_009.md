# GC-II Complete-Monotone Boundary Audit 009

## Question
Can step (6) seek a *finite* family of scalar monotones that is complete for GC-II convertibility without restricting the operational class?

## Result
**DECISIVE BOUNDARY / FALSIFICATION of the unrestricted finite-monotone target.**

For a finite preorder, a finite complete family always exists, but the canonical construction is tautological and therefore does not constitute a substantive GC-II theorem. In unrestricted resource-theoretic settings, a finite complete family cannot be expected in general: Datta, Ganardi, Kondra & Streltsov, *Phys. Rev. Lett.* 130, 240204 (2023), prove that for any quantum resource theory containing resource-free pure states there is no finite set of resource monotones that completely determines all state transformations.

Therefore GC-II must not claim or pursue a universal finite complete monotone criterion. Step (6) is repaired to: seek a finite/computable/dual complete family only for an explicitly structured operational subclass, or allow an infinite/separating family in the general theory.

## Proposition 1 — finite-preorder canonical completeness
Let `(X, >=)` be a finite preorder. For every `z in X`, define

`M_z(x) = 1{ x >= z }`.

Then each `M_z` is monotone: if `x >= y` and `M_z(y)=1`, transitivity gives `x >= z`, hence `M_z(x)=1`. Moreover

`x >= y  iff  M_z(x) >= M_z(y) for every z in X`.

The forward direction is monotonicity. For the reverse direction choose `z=y`; reflexivity gives `M_y(y)=1`, hence `M_y(x)=1`, so `x>=y`.

Status: **PROVED but tautological/KNOWN-order-theoretic construction**. It simply encodes principal lower sets and gives no compression of the preorder.

## Corollary — quotient reduction
If `x~y` iff `x>=y` and `y>=x`, the same construction may be indexed by equivalence classes in the quotient poset. This removes duplicate monotones but remains an order encoding, not a structural characterization.

## Why this matters for GC-II
A useful convertibility theorem must do more than restate reachability. It should derive completeness from a smaller or computable family tied to operational structure: e.g. support/dual witnesses, cut inequalities, deficiencies, graph invariants, or task-indexed tests. The family must be shown sufficient, not merely necessary.

## Prior-art collision checks
- Ordered commutative monoids/resource convertibility already formalize transformations by preorders and monotones (Fritz, 2015).
- Majorization supplies complete convertibility criteria in important structured subclasses.
- Resource theories can require infinite/discontinuous monotone families; the 2023 PRL result rules out a universal finite-complete expectation for a broad quantum class.
- Catalysis can alter convertibility and must be declared explicitly; catalytic relative majorization and quantum-thermodynamic catalysis show that ignoring catalysts can change the order.
- Zero-error functional compression uses characteristic/confusability graphs and chromatic/fractional-chromatic quantities, so any translator-specific dual criterion must be collision-checked there.

## Repaired research target
1. Specify a structured GC-II translator class `C` (finite deterministic, stochastic finite-state, bounded-memory, or LP-representable).
2. Define its convertibility relation with R/I/A/L semantics fixed.
3. Seek a family `{M_i}` whose size/description is polynomial or otherwise structurally compressed relative to the state space.
4. Prove both directions of `X ->_C Y iff M_i(X)>=M_i(Y) for all i`.
5. Test catalysts, tensor/compositional closure, approximation/error, and resource budgets separately.
6. If no finite family exists, seek a separation oracle or dual optimization criterion rather than forcing scalar monotones.

## Status ledger impact
- Universal finite complete convertibility criterion: **FALSIFIED as a defensible general target**.
- Finite-preorder canonical indicator family: **PROVED / IMPORTED-KNOWN / tautological**.
- Structured compressed finite/computable criterion: **OPEN**.
- Infinite or dual separating criterion: **OPEN**.

No breakthrough claim is made. The advance is a decisive pruning of an overbroad theorem target before it contaminates Paper II.