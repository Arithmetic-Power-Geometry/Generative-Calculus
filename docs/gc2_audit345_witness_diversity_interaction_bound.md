# GC-II Audit 345 — Witness-diversity interaction bound

## Scope
This audit continues Audits 341–344 on the finite grounded-edge capability model. Let `B` be the baseline preorder, `E` a finite set of newly admitted grounded transitions, and for every baseline-novel ordered pair `p=(x,y)` let `W_p` be the antichain of inclusion-minimal subsets of `E` that make `p` reachable.

Define

- witness locality: `lambda = max_{p,W in W_p} |W|` (zero when there is no novelty),
- alternative-witness diversity: `nu = max_p |W_p|` (zero when there is no novelty),
- witness-union rank: `rho = max_p | union_{W in W_p} W|`.

Audit 343 proved that a pairwise interaction coefficient can be nonzero only on a set `T` that is a union of minimal witnesses for that pair. Audit 344 proved that `lambda` alone cannot bound interaction order.

## Theorem 345.1 — Product bound
For every finite grounded-edge system,

`rho <= lambda * nu`.

Consequently every global Möbius interaction coefficient `J_B(T)` vanishes whenever

`|T| > lambda * nu`.

### Proof
Fix a novel pair `p`. Its witness union obeys

`| union_{W in W_p} W| <= sum_{W in W_p}|W| <= |W_p| lambda <= nu lambda`.

Audit 343's witness-union support theorem says `j_p(T) != 0` only if `T` is a union of members of `W_p`; hence `|T| <= rho <= lambda nu`. Summing `j_p(T)` over pairs cannot create support at a set `T` for which every pairwise coefficient is zero. Therefore `J_B(T)=0` for `|T|>lambda nu`. QED.

## Corollary 345.2 — Exact fixed-order regime
If a family of operational systems has uniformly bounded witness locality `lambda <= L` and uniformly bounded alternative-witness diversity `nu <= N`, then its exact capability-accounting expansion truncates above order `LN`.

This is a sufficient condition, not a necessary one: witness unions may overlap strongly, and Möbius coefficients may cancel.

## Sharpness
The parallel-route family of Audit 344 has `m` pairwise-disjoint two-edge minimal witnesses for the endpoint capability. Thus `lambda=2`, `nu=m`, `rho=2m=lambda nu`, and its top coefficient at the full `2m`-edge set equals `(-1)^(m+1)`, so the product bound is attained for every `m>=1`.

Therefore neither factor can in general be deleted: Audit 344 already fixes `lambda=2` while `nu` and interaction order diverge; serial chains fix `nu=1` while `lambda` and interaction order diverge.

## Accounting consequence
The failure in Audit 344 is repaired at the semantic level by charging both (i) how many new operations one minimal realization needs and (ii) how many alternative minimal realizations a capability has. The pair `(lambda,nu)` controls interaction order even though either coordinate alone does not.

This does **not** yet produce a universal bridge from syntactic `(Delta R, Delta I, Delta A, Delta L)` to `(lambda,nu)`. In particular, succinct rule schemas may hide large grounding domains and large alternative-witness families (Audits 335 and 340). That bridge remains OPEN.

## Edge and invariance audit
- No novelty: take `lambda=nu=rho=0`; all nonempty interaction coefficients vanish.
- Unique-witness regime: `nu=1`, so interaction order is at most `lambda`, recovering Audit 343.
- Duplicate syntax that grounds to the same operational edge does not change `W_p`, hence does not change `lambda`, `nu`, or `rho`.
- State relabelling preserves all three quantities.
- Witness overlap can only lower `rho` relative to `lambda nu`.
- The bound is dimensionless: all quantities count grounded operations/witness support.
- Composition is nonadditive; the theorem bounds interaction support and does not assert additivity or nonnegativity.

## Prior-art / novelty discipline
The proof is elementary finite-set union counting combined with the classical Boolean-lattice Möbius/inclusion–exclusion machinery already marked IMPORTED/KNOWN in Audits 342–344. No novelty is claimed for those ingredients. The GC-II contribution here is the operational accounting consequence: local witness size becomes sufficient for exact finite-order truncation only when paired with bounded alternative-witness diversity.

## Status
- `rho <= lambda nu`: **PROVED**.
- `J_B(T)=0` for `|T|>lambda nu`: **PROVED**, conditional only on the finite grounded-edge model already formalized in Audits 341–343.
- Sharpness of the product bound: **PROVED** by the Audit-344 parallel-route family.
- `lambda` alone controls interaction order: **FALSIFIED** (Audit 344).
- `nu` alone controls interaction order: **FALSIFIED** by serial chains.
- Bridge from `(Delta R, Delta I, Delta A, Delta L)` to bounded `(lambda,nu)`: **OPEN**.
