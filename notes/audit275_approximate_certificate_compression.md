# GC-II Audit 275 — Approximate capability-certificate compression

## Scope

Finite nonnegative typed-cost semantics from Audits 265–274. This audit asks whether the exponential exact-certificate lower bound of Audit 274 survives when a controlled multiplicative novelty tolerance is allowed.

## Definition

For finite nonempty attainable sets `S,Y subset R_+^d`, write

`Omega(S,Y) = inf { alpha >= 1 : for every y in Y there exists s in S with s <= alpha y coordinatewise }`.

Thus `Omega(S,Y) <= 1+eps` means that `S` is a `(1+eps)` operational capability certificate for `Y`.

## Theorem 275.1 — bounded-dynamic-range compression

Assume every coordinate of every `y in Y` lies in `[m,M]`, with `0 < m <= M < infinity`, and let `alpha=1+eps>1`. Partition each coordinate into multiplicative bins

`[m alpha^k, m alpha^(k+1))`.

Choose one representative from each occupied d-dimensional bin. Let the resulting set be `S`.

Then

`Omega(S,Y) <= alpha`, 

and

`|S| <= (1 + floor(log_alpha(M/m)))^d`.

A boundary-safe equivalent bound is `|S| <= (1 + ceil(log_alpha(M/m)))^d`.

### Proof

If `s` and `y` occupy the same bin, then for every coordinate i,

`m alpha^k <= s_i < m alpha^(k+1)` and `m alpha^k <= y_i`.

Hence `s_i < alpha y_i`, so `s <= alpha y`. Every `y` has a representative in its occupied bin, proving the approximation claim. The bin-count bound follows independently in each coordinate.

Status: **PROVED**.

## Corollary 275.2 — exactness/compression separation

Audit 274 gives finite families whose exact explicit principal-upset certificate has size

`binom(d,floor(d/2)) = Theta(2^d/sqrt(d))`.

Theorem 275.1 shows that, after imposing a positive coordinate floor and finite dynamic range, controlled multiplicative tolerance admits a finite logarithmic-grid certificate. Therefore exact exponential frontier size does not by itself imply approximate incompressibility.

Status: **PROVED** as a consequence of Audit 274 + Theorem 275.1.

## Necessity of scale assumptions

The positive floor is substantive, not cosmetic. Audit 273 already proves that absolute perturbations near zero can have unbounded multiplicative novelty. If zero coordinates are admitted, a multiplicative grid must treat zero-support patterns separately; without a positive lower scale on nonzero entries, no finite bound depending only on `M/m` is meaningful because `m` is undefined/zero.

Status: **PROVED/previously established obstruction**.

## Invariance and monotonicity

- `Omega` and the construction are dimensionless.
- Coherent positive rescaling of each coordinate leaves multiplicative approximation relations unchanged if the corresponding coordinate floor/range is rescaled with it.
- Increasing `eps` weakly decreases the number of bins required.
- Removing dominated targets cannot make the approximation requirement harder.

Status: **PROVED**.

## Composition

Combined with Audit 270, successive approximate certificates compose multiplicatively: if `Omega(S,Y)<=a` and `Omega(Y,Z)<=b`, then `Omega(S,Z)<=ab`. Thus repeated compression has an explicit accumulated error budget.

Status: **PROVED** by Audit 270.

## Prior-art collision

The generic mathematical mechanism is **IMPORTED/KNOWN**. Multiplicative epsilon-Pareto sets and logarithmic objective-space discretization are established in multiobjective optimization; Papadimitriou–Yannakakis and later work establish polynomial-size approximate Pareto sets under standard bounded-encoding assumptions. Diakonikolas–Yannakakis study minimum-size approximate Pareto sets. No novelty claim is made for multiplicative gridding itself.

The GC-II-specific value is narrower: this supplies the controlled-error counterpart to Audit 274's exact capability-certificate barrier and connects certificate compression directly to the already-defined operational novelty gauge `Omega_G`.

## Collision / failure tests

1. `eps -> 0`: bin count diverges, consistent with Audit 274 exact incompressibility.
2. `m -> 0`: dynamic range diverges; no contradiction with Audit 273.
3. `M=m`: one bin suffices.
4. `d=1`: ordinary multiplicative interval cover.
5. Coordinatewise positive unit changes: invariant.
6. Empty target set: vacuous certificate; excluded from theorem statement to avoid irrelevant logarithmic conventions.

## Research status after Audit 275

- Exact explicit certificate can require exponential size: **PROVED** (Audit 274).
- `(1+eps)` certificate under positive bounded dynamic range admits logarithmic-grid compression: **PROVED**.
- Generic epsilon-Pareto mechanism: **IMPORTED/KNOWN**.
- GC-II exactness/compression interpretation: **VALIDATED operational corollary**, not claimed as new generic optimization theory.
- Sharp minimum certificate size for GC-II structural subclasses: **OPEN**.
- Compression bounds using dependency width / witness width rather than ambient dimension: **OPEN** and higher priority.
- Approximate certificates with zero coordinates and support-pattern structure: **OPEN** beyond trivial support splitting.
