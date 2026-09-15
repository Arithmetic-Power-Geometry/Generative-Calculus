# GC-II Audit 167 — Axiom Independence and Representation Boundary

Status date: 2026-09-16
Branch scope: `gc2-capability-accounting-lab` only. GC-I/main unchanged.

## Objective

Stress-test the proposed axioms for a capability-accounting functional before attempting a representation theorem.

Let `(X, >=, tensor, e)` be an operational quotient: `x >= y` means that `x` can realize/convert to `y`, `tensor` is parallel composition, and `e` is the neutral object. Consider `Q : X -> [0,infinity]` with candidate axioms:

- INV: operational invariance (well-defined on the quotient),
- NORM: `Q(e)=0`,
- MON: `x >= y => Q(x) >= Q(y)`,
- SUB: `Q(x tensor y) <= Q(x)+Q(y)`,
- ADD: `Q(x tensor y)=Q(x)+Q(y)` (stronger than SUB).

## Exact finite countermodels: the axioms do not force a unique scalar account

Take the free commutative resource monoid `X=N^2`, ordered componentwise, with `tensor=+` and `e=(0,0)`. Define

`Q_{a,b}(m,n)=a m + b n`, for `a,b >= 0`.

Every `Q_{a,b}` satisfies INV, NORM, MON and ADD. Hence even the strong package INV+NORM+MON+ADD admits a continuum of distinct scalar accounts whenever two independent resource directions exist. In particular, `Q_{1,0}`, `Q_{0,1}`, and `Q_{1,1}` all satisfy the same structural axioms but disagree on ordinary states.

Therefore:

**PROVED:** invariance + normalization + monotonicity + additivity does not imply uniqueness, canonicality, or a distinguished `Omega_G`.

This is not an edge pathology; it is the generic dual-cone phenomenon. A scalar account requires an extra calibration/normalization principle selecting a point/ray in the cone of monotones, or the theory must retain the whole family of monotones.

## Independence witnesses

All witnesses below are finite submonoids/order fragments sufficient to falsify implication between axioms.

1. NORM is not forced by MON+SUB: constant `Q(x)=1` is monotone and subadditive (`1 <= 2`) but `Q(e)!=0`.
2. MON is not forced by NORM+ADD: on `N` with ordinary addition/order, `Q(n)=-n` is normalized and additive but order-reversing (if codomain is allowed to be `R`). If nonnegativity is mandatory, use a finite ordered idempotent monoid `{e,a}` with `a tensor a=a`, `a>=e`, and `Q(e)=0,Q(a)=0`; this shows normalization/additive structure alone cannot enforce strict order reflection. For ordinary monotonicity failure with nonnegative codomain, add an incomparable algebraic generator and an externally specified order not respected by the homomorphism.
3. SUB is not forced by NORM+MON: on `N`, `Q(n)=n^2` is normalized and monotone but `Q(m+n) > Q(m)+Q(n)` for positive `m,n`.
4. ADD is not forced by NORM+MON+SUB: `Q(n)=min(n,1)` on `N` is normalized, monotone and subadditive, but not additive.
5. Separation/order reflection is not forced by INV+NORM+MON+ADD: `Q_{1,0}` maps `(0,0)` and `(0,1)` to the same value despite their operational difference.

## Positive finite representation result — but it is known structure

For a finite preorder `(X,>=)`, define for each `z in X`

`m_z(x)=1` if `x>=z`, else `0`.

Then each `m_z` is a `{0,1}`-valued monotone. Moreover,

`x>=y` iff `m_z(x)>=m_z(y)` for every `z`.

Proof: the forward implication is transitivity. Conversely choose `z=y`; reflexivity gives `m_y(y)=1`, so domination of all monotones forces `m_y(x)=1`, hence `x>=y`.

Thus the complete family of finite principal-upset monotones separates the operational preorder exactly.

**PROVED:** finite convertibility admits a complete finite family of computable binary monotones (at most `|X|`, fewer after quotient/redundancy elimination).

**IMPORTANT NOVELTY BOUNDARY:** this is an elementary order-theoretic representation, not a new GC theorem. It does, however, solve Paper-II item (6) in the finite operational quotient: a complete computable convertibility criterion exists, but the raw result is IMPORTED/KNOWN mathematics.

## Consequence for scalar Omega_G

A single scalar monotone can completely characterize convertibility only when the quotient preorder is representable by a total real-valued order with the required reflection property. In particular, if `x` and `y` are incomparable, no scalar `Q` satisfying

`x>=y iff Q(x)>=Q(y)`

can exist, because real values are total: either `Q(x)>=Q(y)` or `Q(y)>=Q(x)` (or both), forcing at least one false conversion.

Therefore a general GC-II convertibility theory must be vector/family-valued, partially ordered, or set-valued unless additional totality assumptions are imposed.

## Composition boundary

If the operational quotient with parallel composition is a commutative ordered monoid, additive monotones are precisely order-preserving monoid homomorphisms into an additive ordered codomain. Such monotones are standard in resource theories. Likewise, a directed cost with zero identities and subadditive composition is Lawvere-metric/weighted-category structure. Therefore neither ADD nor triangle/subcomposition axioms can support an independent novelty claim by themselves.

## Status ledger

| Candidate | Status | Reason |
|---|---|---|
| INV+NORM+MON+ADD uniquely determines scalar capability | FALSIFIED | `N^2` weighted-linear family |
| MON+NORM implies SUB | FALSIFIED | square-cost witness |
| MON+NORM+SUB implies ADD | FALSIFIED | saturated-cost witness |
| Scalar complete convertibility on arbitrary partial order | FALSIFIED | incomparable pair obstruction |
| Finite complete family of binary monotones | PROVED / IMPORTED-KNOWN | principal-upset separation |
| Additive monotones on ordered commutative monoids | IMPORTED/KNOWN | standard resource-theory structure |
| Triangle/subcomposition cost geometry | IMPORTED/KNOWN | Lawvere/weighted-category structure |
| Canonical GC-II scalar Omega_G from structural axioms alone | OPEN, with strong non-uniqueness obstruction | needs calibration or stronger GC-specific axiom |
| Minimal/redundancy-free operationally meaningful monotone basis | OPEN | possible structured target, novelty not established |

## Paper-II consequence

Do not seek a scalar representation theorem from generic invariance/monotonicity/composition axioms: even strong additivity leaves arbitrary dual weights, while partial convertibility prevents a single scalar from being complete. The defensible structural object is the **capability spectrum**: a separating family/cone of operational monotones, with scalar accounts arising only after an explicit calibration functional is chosen.

The next breakthrough gate is therefore sharper: determine whether budgeted operational closure supplies a GC-specific canonical generating/separating subset of the monotone cone, or a canonical dual envelope, whose structure is not already an instance of ordered-monoid/resource-theory duality. Test minimal bases on exact finite worlds and search for pairs with identical standard resource/simulation monotones but distinct GC closure spectra.