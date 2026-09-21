# GC-II Audit 287 — scalarization collapse of typed capability accounting

Status: **PROVED / decisive falsification of scalar-budget extension**

## Question

Audit 286 proved an exponential persistent-summary lower bound for conservative, multiplicatively tight summaries of *typed* capability costs. Does the same obstruction survive if downstream accounting exposes only one exact scalar resource budget?

No.

## Construction

Fix `m >= 1`, `d = 2m`, and `r > 1`. For each bit string `b in {0,1}^m`, define an attainable typed cost vector `y^b in R_+^(2m)` by placing in pair `j`

- `(r,1)` if `b_j=1`,
- `(1,r)` if `b_j=0`.

There are `2^m` attainable typed vectors. For multiplicative tolerance `alpha < r`, Audit 286 shows that no conservative alpha-tight typed synthetic center can cover two distinct members, so the typed conservative certificate number is `2^m`.

Now expose only the scalarized resource functional

`L(y) = sum_{i=1}^{2m} y_i`.

Every attainable vector has exactly one `r` and one `1` in each pair. Hence

`L(y^b) = m(r+1)`

for every `b`. Therefore all `2^m` operationally distinct typed configurations have the same exact scalar cost. A one-state scalar summary storing `m(r+1)` is exact: it has approximation factor 1, not merely alpha.

Thus

`C_typed,cons,alpha(Y_m) = 2^m`, while `C_scalar,exact,L(Y_m) = 1`.

Equivalently, with `d=2m`, exact scalarization can collapse an exponential typed accounting requirement by a factor `2^(d/2)`.

## Theorem candidate (proved)

**Typed-to-scalar collapse theorem.** For every `m >= 1` and every `alpha >= 1`, choose `r > alpha`. There exists a finite attainable set `Y_m subset R_+^(2m)` such that:

1. every conservative alpha-tight typed summary requires at least `2^m` states;
2. the exact additive scalar budget `L(y)=sum_i y_i` is constant on `Y_m`, and therefore admits a one-state exact summary.

### Proof

Part 1 is Audit 286's pairwise interval-separation argument. Distinct bit strings differ in some pair. At one coordinate the two targets have values `r` and `1`. A common conservative alpha-tight center would need simultaneously `z_i >= r` and `z_i <= alpha`, impossible because `r > alpha`.

For part 2, each pair contributes `r+1` to `L`, independently of orientation, so `L(y)=m(r+1)` for all attainable vectors. One scalar state therefore represents every target exactly. QED.

## Stress checks

- Domains/dimensions: `Y_m subset R_+^(2m)`; `L: R_+^(2m) -> R_+`.
- Degenerate `m=0`: singleton empty configuration; both certificate counts are 1. Main theorem states `m>=1`.
- Sharpness for typed separation: at `r=alpha`, Audit 286's common typed center exists; strict `r>alpha` is required for that lower bound.
- Scalar exactness: independent of alpha and r; it follows from pairwise conservation of `r+1`.
- Unit rescaling: multiplying all typed costs by any `c>0` preserves both the typed separation ratio and scalar collapse.
- Composition: Cartesian composition of modules multiplies typed distinguishable configurations (`2^m`) while scalar contributions add (`m(r+1)`). This is the source of the exponential/exact contrast.
- Monotonicity caveat: `L` is coordinatewise monotone but non-injective. Monotonicity therefore does not protect typed capability information.
- Non-additive scalarizations: not covered by this theorem. The result falsifies any claim that a single exact additive aggregate is generically sufficient for typed capability accounting.

## Interpretation

The Audit-286 memory lower bound is not merely about numerical precision. It depends on retaining *resource type*. Exact knowledge of total resource consumption can erase which resource/interface coordinate carries the cost. Consequently, a scalar budget can certify aggregate expenditure while failing to preserve typed feasibility for downstream actions.

This gives a clean GC-II warning for any proposed `Omega_G <= F(Delta R,...)` law: if `Delta R` is scalarized before operational closure is evaluated, the bound can identify systems whose typed capability sets differ exponentially. A defensible capability-accounting bound must either retain a sufficient typed resource/interface representation or explicitly prove that the chosen scalarization is sufficient for the downstream admissible-action family.

## Prior-art collision status

The mathematical mechanism is **IMPORTED/KNOWN territory**: weighted-sum/scalarization in multiobjective optimization is many-to-one and can lose Pareto/tradeoff information; resource theories likewise distinguish multiple monotones/resources when one scalar monotone is incomplete. No novelty claim is made for non-injectivity of scalarization.

The GC-II-specific surviving statement is the exact operational separation between (i) conservative typed witness accounting and (ii) exact aggregate-budget accounting on the same attainable family, with an exponential certificate ratio.

## Status ledger

- Exponential conservative typed requirement: **PROVED** (Audit 286, reused).
- One-state exact additive scalar summary: **PROVED**.
- Exponential typed/scalar certificate separation: **PROVED**.
- Claim that exact scalar budget accounting preserves typed capability distinctions: **FALSIFIED**.
- Generic scalarization information loss: **IMPORTED/KNOWN**.
- Characterization of when a scalarization is sufficient for a specified downstream action/query family: **OPEN** and now the preferred next target.
