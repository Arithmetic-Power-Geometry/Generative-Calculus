# GC-II Audit 255 — Exact reversibility-gap boundary and dual certificate

## Scope

This audit attacks Paper-II item (8) using the exact finite fixed-generator model of Audit 254. The aim is to determine what can and cannot be claimed for a reversibility-gap invariant before attaching GC-specific novelty.

## 1. Directed operational distance

Let `X` be finite and let every admissible transition have cost `c(e)>=0` in one declared budget unit. For states `x,y`, define

\[
d(x,y)=\inf_{\pi:x\leadsto y}\sum_{e\in\pi}c(e),
\]

with `d(x,y)=+infinity` if `y` is unreachable from `x`.

On any mutually reachable pair with finite distances define the signed reversibility gap

\[
\Gamma(x,y)=d(x,y)-d(y,x),
\]

and the nonnegative asymmetry magnitude

\[
A(x,y)=|d(x,y)-d(y,x)|.
\]

Dimensions: both have the same unit as operational cost.

## 2. Exact elementary properties

### Proposition 255.1 — antisymmetry and relabeling invariance — PROVED

For finite mutually reachable pairs,

\[
\Gamma(y,x)=-\Gamma(x,y),\qquad A(y,x)=A(x,y).
\]

Any cost-preserving operational graph isomorphism preserves `d`, hence preserves `Gamma` and `A`.

### Proposition 255.2 — zero gap is not operational reversibility — PROVED

`Gamma(x,y)=0` means only equality of the two optimal scalar costs. It does **not** imply that a forward optimal execution has an inverse, that individual operations are reversible, or that forward/backward path structures coincide.

Counterexample: states `x,a,y,b` with unit edges `x->a->y` and `y->b->x`, and no reverse edge for any of those four edges. Then `d(x,y)=d(y,x)=2`, so `Gamma=0`, while neither optimal path is the edgewise inverse of the other.

Therefore the scalar gap is a cost-asymmetry statistic, not by itself a complete reversibility invariant.

## 3. Exact dual expression

Audit 254 gives, for singleton target `{y}`,

\[
d(x,y)=\sup_{\phi\in\Phi}\bigl(\phi(x)-\phi(y)\bigr),
\]

where `Phi` is the family satisfying `phi(u)-phi(v)<=c(u,v)` on every admissible edge.

Hence for finite mutually reachable pairs,

\[
\boxed{\Gamma(x,y)=
\sup_{\phi\in\Phi}(\phi(x)-\phi(y))-
\sup_{\phi\in\Phi}(\phi(y)-\phi(x)).}
\]

This is exact, but its mechanism is shortest-path duality and is therefore IMPORTED/KNOWN.

## 4. Cycle interpretation

For any mutually reachable pair,

\[
d(x,y)+d(y,x)
\]

is the minimum cost of a closed operational walk constrained to visit both `x` and `y` (allowing different optimal paths in the two directions). Define the round-trip burden

\[
C_{rt}(x,y)=d(x,y)+d(y,x).
\]

Then whenever `C_rt>0`, a dimensionless normalized directional asymmetry is

\[
\alpha(x,y)=\frac{|d(x,y)-d(y,x)|}{d(x,y)+d(y,x)}\in[0,1].
\]

If both distances are zero, set `alpha=0` by convention. This normalization is scale invariant under `c -> lambda c`, `lambda>0`.

### Proposition 255.3 — bounds — PROVED

For finite nonnegative distances,

\[
0\le A(x,y)\le C_{rt}(x,y),\qquad 0\le\alpha(x,y)\le1.
\]

Equality `alpha=1` occurs exactly when one directional optimal cost is zero and the other is positive.

## 5. Decisive composition test

A tempting claim is that reversibility asymmetry should be additive under independent composition. This is false for the absolute gap `A` because signed gaps can cancel.

For two independent product systems with additive transition costs and fully separable reachability,

\[
d_{12}((x_1,x_2),(y_1,y_2))=d_1(x_1,y_1)+d_2(x_2,y_2).
\]

Therefore

\[
\boxed{\Gamma_{12}=\Gamma_1+\Gamma_2}
\]

but

\[
A_{12}=|\Gamma_1+\Gamma_2|\le A_1+A_2,
\]

with strict cancellation possible.

Example: component 1 has forward/backward costs `(1,2)`, hence `Gamma_1=-1`; component 2 has `(2,1)`, hence `Gamma_2=+1`. Jointly, forward and backward costs are both `3`, so `Gamma_12=0` and `A_12=0`, despite both components being directionally asymmetric.

Thus `A` is subadditive under independent additive composition, not additive. The signed `Gamma` is additive in this restricted product regime but can be negative and is orientation-dependent.

## 6. Reachability edge cases

If exactly one direction is unreachable, the extended gap has infinite magnitude; this records one-way convertibility rather than a finite inefficiency. If neither direction is reachable, `infinity-infinity` is undefined, so `Gamma` must not be assigned a scalar value. A robust implementation therefore reports the pair

`(d(x,y), d(y,x))`

first, and derives `Gamma`, `A`, and `alpha` only when mathematically defined.

## 7. Prior-art collision boundary

Directed shortest-path distance is a quasimetric and its asymmetry is established directed-metric structure. Resource theories also study reversible versus irreversible interconversion and forward/reverse conversion rates or costs. Therefore none of the following should be claimed as generic GC novelty:

- directed distance asymmetry;
- forward-minus-backward conversion cost;
- round-trip cost;
- normalized directional asymmetry;
- additive signed asymmetry under a Cartesian product whose directed distances themselves add.

The GC-II novelty target must instead involve a specifically generative obstruction — for example, a gap derived from projection irreducibility, typed generator restrictions, or capability-producing versus capability-erasing transformations — and it must separate systems having identical ordinary directed-distance asymmetry.

## 8. Ledger

| Claim | Status |
|---|---|
| `Gamma=d_forward-d_reverse` well-defined for finite mutually reachable pairs | PROVED / definition |
| antisymmetry of `Gamma` | PROVED |
| symmetry of `A=|Gamma|` | PROVED |
| `Gamma=0` implies structural reversibility | FALSIFIED |
| exact dual representation from Audit 254 potentials | PROVED / IMPORTED-KNOWN mechanism |
| `C_rt=d_forward+d_reverse` minimum constrained round-trip cost | PROVED |
| normalized `alpha` lies in `[0,1]` and is cost-scale invariant | PROVED |
| signed `Gamma` additive under independent additive product composition | PROVED / restricted regime |
| absolute `A` additive under that composition | FALSIFIED; only subadditive |
| generic directed-distance asymmetry as GC novelty | IMPORTED/KNOWN |
| GC-specific reversibility invariant beyond ordinary directed quasimetric asymmetry | OPEN |

## 9. Consequence for Paper II

The naive reversibility-gap candidate is now bounded sharply: ordinary forward/reverse cost asymmetry is useful as a baseline diagnostic but is not a new GC invariant and is not complete for operational reversibility. The next viable target is a **generative reversibility defect** that remains nonzero in examples with `d(x,y)=d(y,x)` but whose forward and reverse transformations differ in projection loss, information access, admissible interfaces, or rule-generation requirements. Such an invariant must be collision-tested against ordinary directed quasimetrics and resource-theoretic irreversibility before any novelty claim.