# GC-II Audit 262 — Exact single-generator novelty sensitivity

## Scope
This audit isolates a defensible operational Generative Novelty Gap for a *fixed* finite nonnegative-cost transition system and proves the exact sensitivity law for adjoining one admissible transformation. It is a baseline theorem, not a claim that shortest-path sensitivity is new mathematics.

Let `G=(X,E,c)` be a finite directed operational system, `F subset X` a target set, and

`V_G(x;F) = inf{ c(pi) : pi is a G-path from x to F }`,

with value `+infinity` if `F` is unreachable. For a budget `B`, `Cl_G^B(F)={x:V_G(x;F)<=B}`.

For an extension `H` with `E subseteq E_H`, define the cost-valued novelty gain

`Omega_G^H(x;F) = V_G(x;F)-V_H(x;F)`

when both values are finite. For extended-real cases, use the ordered pair `(V_G,V_H)` rather than undefined `infinity-infinity`; in particular baseline-unreachable / extension-reachable is an escape event of infinite baseline deficit.

## Theorem 262.1 — exact one-transformation law
Let `e=(u,v)` be a new admissible edge of cost `k>=0`, and `G+e` the system obtained by adding only `e`. Then

`V_{G+e}(x;F) = min( V_G(x;F), d_G(x,u)+k+V_G(v;F) )`,

with the usual extended-real conventions.

### Proof
Any optimal `G+e` path either does not use `e`, in which case its cost is at least `V_G(x;F)`, or uses `e`. A minimum-cost path can be chosen simple after deletion of nonnegative-cost cycles. Since `e` is a single directed edge, a simple path uses it at most once. Its prefix from `x` to `u` and suffix from `v` to `F` use only baseline edges and therefore cost at least `d_G(x,u)` and `V_G(v;F)`. Conversely, concatenating baseline minimizers for those two pieces with `e` attains the second term whenever finite. Taking the minimum proves the identity. QED.

For finite baseline value this yields the exact scalar novelty gap

`Omega_e(x;F) = max(0, V_G(x;F) - d_G(x,u)-k-V_G(v;F))`.

Thus a new transformation is capability-relevant at `(x,F)` iff it violates the baseline Bellman inequality strongly enough to improve the target value.

## Corollary 262.2 — exact budgeted Closure-Escape interval
Write `q=d_G(x,u)+k+V_G(v;F)`. A previously excluded state `x` enters the budget-`B` closure after adding `e` iff

`q <= B < V_G(x;F)`.

Hence the edge does not merely say whether closure expands: it gives the exact budget interval on which the expansion occurs.

## Corollary 262.3 — dual certificate interpretation
Audit 254 gives baseline feasible potentials `phi` with `phi(a)-phi(b)<=c(a,b)` on every baseline edge. Adding `e=(u,v,k)` adds exactly one dual constraint

`phi(u)-phi(v)<=k`.

If every baseline optimal potential already satisfies this constraint, the edge cannot improve the value. If the primal second term above is smaller than `V_G(x;F)`, the extension removes enough of the baseline dual feasible region to lower the optimum. This is ordinary shortest-path LP sensitivity in GC-II language.

## Multi-edge warning: novelty is contextual
The exact one-edge formula must not be extrapolated to additive generator accounting. Two new edges can be jointly useful although neither is useful alone.

Example: baseline has states `s,u,v,t`, target `{t}`, and only baseline edge `s->t` of cost 10. Add `e1:s->u` cost 0 and `e2:u->t` cost 0. Individually, `V=10` because each incomplete extension leaves the new route unfinished. Jointly, `V=0`. Therefore

`Omega_{e1}=Omega_{e2}=0` but `Omega_{ {e1,e2} }=10`.

So per-transformation novelty scores are context dependent; no universal additive sum of singleton gains can equal multi-generator novelty.

## Checks
- **Dimensions:** all finite terms have cost units; `Omega` has cost units.
- **Degenerate target:** if `x in F`, all values are zero and gain is zero.
- **Unreachable prefix/suffix:** second term is `+infinity`, so the new edge is irrelevant.
- **Zero-cost edges:** allowed; proof uses nonnegative, not strictly positive, costs.
- **Monotonicity:** generator inclusion cannot increase `V`.
- **Cost scaling:** multiplying all costs and `B` by `lambda>0` multiplies finite `V` and `Omega` by `lambda` and preserves closure membership.
- **Composition:** singleton sensitivity is not additive under arbitrary extension composition; explicit synergy counterexample above.
- **Known-theory reduction:** this is dynamic shortest-path / LP sensitivity and Bellman-potential machinery; mechanism is IMPORTED/KNOWN.

## Status ledger
- Budgeted operational closure on finite nonnegative systems: **PROVED / IMPORTED-KNOWN mechanism**.
- `Omega_G^H` as extension-induced cost improvement: **CONDITIONAL definition** (useful operational candidate, not yet canonical GC novelty).
- Exact one-edge sensitivity law: **PROVED / IMPORTED-KNOWN mechanism**.
- Exact budget interval for single-edge Closure-Escape: **PROVED**.
- Additivity of singleton generator novelty: **FALSIFIED**.
- Context-independent per-generator capability accounting: **FALSIFIED in unrestricted systems**.
- GC-specific novelty surviving representation/generator refactoring: **OPEN**.

## Novelty discipline
Shortest-path edge insertion sensitivity, Bellman inequalities, and LP duality are established. The result is retained as an exact baseline and falsification instrument. Any Paper-II novelty claim must go beyond relabeling these known facts, most plausibly by proving a representation-stable invariant or a structural theorem for coupled R/I/A/L generator extensions.