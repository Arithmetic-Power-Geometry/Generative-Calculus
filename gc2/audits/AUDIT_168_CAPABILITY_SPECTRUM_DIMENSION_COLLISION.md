# GC-II Audit 168 — Capability-Spectrum Dimension Collision

Status date: 2026-09-16
Branch scope: `gc2-capability-accounting-lab` only. GC-I/main unchanged.

## Objective

Attack the Audit-167 breakthrough gate: determine whether the smallest separating capability spectrum / dual envelope induced by budgeted operational closure is a new invariant, or whether its abstract finite form collapses to known order-representation dimensions.

## Setup

Let `P=(X, >=)` be the finite operational quotient after fixing the admissible transformations, resource/information/interface/law rules and the budget convention. A separating real-valued capability spectrum is a family

`M={m_1,...,m_d}`, `m_i:X->R`,

such that every `m_i` is monotone and

`x >= y  iff  m_i(x) >= m_i(y) for all i`.

Define the abstract spectrum dimension

`sdim(P)=min |M|`

over all such finite real-valued separating monotone families.

## Theorem — exact finite collapse to order/monotone dimension

For every finite poset `P`, `sdim(P)` is exactly the least `d` for which `P` order-embeds into `R^d` with the product order. This is the standard order/monotone-dimension representation problem, not a new GC-specific invariant.

Proof. A separating family gives the map

`Phi(x)=(m_1(x),...,m_d(x))`.

The separation condition is precisely

`x >= y iff Phi(x) >=_prod Phi(y)`,

so `Phi` is an order embedding into a product of `d` chains. Conversely, any such embedding has coordinate projections that are real-valued monotones and jointly separate the order. Minimizing `d` on either side gives equality. QED.

Therefore the raw proposal

`minimal number of scalar monotones needed to characterize finite GC convertibility`

is **FALSIFIED as independent novelty**: it is order/monotone dimension after quotienting by operational equivalence.

## Strong finite stress cases

1. **Chain.** `sdim=1`. One scalar coordinate completely represents convertibility.
2. **Nontrivial antichain.** One scalar cannot order-reflect incomparability because the real order is total. Two coordinates suffice for every finite antichain by assigning increasing rank in one coordinate and decreasing rank in the other. Hence `sdim=2` for antichains of size at least 2.
3. **Standard example `S_n`.** Let elements be `a_1,...,a_n,b_1,...,b_n`, with `a_i < b_j` iff `i != j`. Its order dimension is `n`; therefore the number of scalar capability coordinates required for complete separation can grow linearly even though the poset has only `2n` elements.
4. **Singleton.** Depending on whether the empty product is admitted, the representation dimension is conventionally 1 or can be treated as 0 under a GC normalization convention. This convention must be stated explicitly; it carries no substantive capability content.

## Composition behavior

For product operational orders, ordinary order dimension is subadditive:

`sdim(P x Q) <= sdim(P)+sdim(Q)`

by concatenating separating coordinates. Equality need not hold. Thus even a non-additive spectrum dimension under parallel composition is not by itself evidence of GC-specific generativity.

## Consequence for Audit 167

Audit 167 proved that a single scalar cannot completely represent arbitrary partial convertibility and proposed a minimal/separating capability spectrum. Audit 168 now closes the *unrestricted* version of that route:

- complete finite monotone family: known order representation;
- minimum number of arbitrary real-valued coordinates: known order/monotone dimension;
- growth of required coordinates: also known in resource/GPT settings, where post-processing orders can have infinite monotone dimension.

The GC-specific candidate must therefore restrict what counts as an admissible coordinate. Arbitrary monotones are too expressive.

## Surviving sharper object

Define, only provisionally,

`bdim_G(P) = min{|M| : M subseteq C_G and M separates P}`,

where `C_G` is **not** the set of all monotones, but a rigorously generated class of *closure-witness observables* obtainable from the same operational rules and budgets as the system: e.g. threshold closure indicators, minimum admissible witness costs, or dual certificates produced by a specified closure construction.

This can be new only if all of the following are proved:

1. `C_G` is defined independently of the target pair being separated (no lookup-table cheating).
2. Every member is operationally obtainable/computable under explicit assumptions.
3. `C_G` is strictly smaller than arbitrary monotones on some finite quotient.
4. It still separates a nontrivial class of GC systems.
5. `bdim_G` or its envelope has a theorem not reducible to order dimension, resource-theory monotone dimension, Blackwell/Le Cam deficiency, simulation metrics, CSP/database width, or communication complexity.
6. Exact finite searches exhibit a pair/family with identical standard coarse invariants but different closure-witness spectra; the distinction must survive relabeling and operational equivalence.

Until these gates pass, `bdim_G` is **OPEN / NOT A NOVELTY CLAIM**.

## Status ledger

| Candidate | Status | Reason |
|---|---|---|
| Minimal arbitrary separating scalar spectrum | FALSIFIED as independent novelty | exactly finite order/monotone dimension |
| Coordinate embedding criterion | PROVED / IMPORTED-KNOWN | product-of-chains representation |
| Chain requires one coordinate | PROVED |
| Finite nontrivial antichain requires two coordinates | PROVED |
| `S_n` requires `n` coordinates | IMPORTED/KNOWN standard order-dimension example |
| Spectrum dimension subadditivity under product | PROVED / IMPORTED-KNOWN |
| Arbitrary monotone spectrum as GC-II breakthrough | FALSIFIED |
| Operationally generated closure-witness spectrum `C_G` | OPEN | requires restrictive, non-circular definition |
| Restricted closure-witness dimension `bdim_G` | OPEN | novelty unestablished |

## Paper-II consequence

Do not claim that replacing scalar `Omega_G` by an unrestricted minimal monotone vector solves the novelty problem. The abstract object is classical order dimension. The next scientifically defensible attack is to define a *restricted operationally generated witness class* from budgeted closure itself and prove either (a) a new representation/separation theorem for that restricted class, or (b) a no-go theorem showing exactly when such closure-generated witnesses cannot separate convertibility. Exact finite enumeration should precede any novelty claim.
