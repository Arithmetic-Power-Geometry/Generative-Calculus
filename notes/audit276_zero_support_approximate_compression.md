# GC-II Audit 276 — Zero-support approximate capability compression

## Scope

Audit 275 proved multiplicative certificate compression under a strictly positive coordinate floor. This audit removes the global positivity assumption while retaining a positive floor only for nonzero entries. The point is operational: zero typed cost is qualitatively different from arbitrarily small positive cost under multiplicative capability accounting.

## Setup

Let `Y subset R_+^d` be finite and nonempty. Fix `alpha>1`. Assume that, for each coordinate `i`, every positive value occurring in that coordinate lies in `[m_i,M_i]`, where `0<m_i<=M_i<infinity`; zero is also allowed.

For each coordinate use one exact zero symbol plus multiplicative positive bins

`[m_i alpha^k, m_i alpha^(k+1))`.

Choose one representative from every occupied product cell (zero symbols included), and call the selected set `S`.

Define

`Omega(S,Y)=inf { beta>=1 : for every y in Y there exists s in S with s<=beta y coordinatewise }`.

## Theorem 276.1 — support-safe compression

The selected representatives satisfy

`Omega(S,Y)<=alpha`.

If

`K_i = 1 + floor(log_alpha(M_i/m_i))`

is the number of positive bins intersecting `[m_i,M_i]`, then

`|S| <= product_i (K_i+1)`.

For a common range `[m,M]`,

`|S| <= (2 + floor(log_alpha(M/m)))^d`.

### Proof

Take any target `y in Y` and the representative `s` of its occupied product cell.

If `y_i=0`, the cell uses the exact zero symbol, hence `s_i=0=alpha y_i`.

If `y_i>0`, then `s_i` and `y_i` lie in the same positive multiplicative bin, so

`s_i < alpha y_i`.

Therefore `s<=alpha y` coordinatewise. Since every occupied cell contributes a representative, every target is covered and `Omega(S,Y)<=alpha`.

Coordinate `i` has at most `K_i` positive symbols plus one zero symbol. Multiplying the per-coordinate possibilities gives the cardinality bound.

Status: **PROVED**.

## Corollary 276.2 — zeros do not by themselves destroy finite compression

Audit 275's global positive floor is stronger than necessary. Exact zeros can be admitted without losing finite multiplicative compression, provided every *positive* entry is bounded away from zero. The obstruction is instead an accumulation of arbitrarily small positive scales.

Status: **PROVED**.

## Proposition 276.3 — why support must be treated exactly

For multiplicative domination, if `y_i=0`, every certificate `s` covering `y` must satisfy `s_i=0`. Thus no positive representative, however small, can approximate a zero target coordinate at any finite multiplicative factor.

Status: **PROVED**.

This is the operational discontinuity between zero cost and positive cost.

## Necessity of a positive floor on nonzero entries

If positive values are allowed to approach zero with fixed upper scale, the number of multiplicative bins needed for a fixed `alpha` is unbounded. In one dimension, the family `{M alpha^{-j}: j=0,...,N}` occupies `N+1` successive scales. Hence there is no cardinality bound depending only on `d`, `M`, and `alpha` that is uniform over arbitrarily small positive entries.

Status: **PROVED**.

## Edge cases and invariance

- `M_i=m_i`: coordinate `i` has exactly two possible symbols, zero and one positive bin.
- All-zero target: it is covered only by an all-zero representative; the construction preserves it exactly.
- A coordinate identically zero can be deleted from the effective dimension, tightening the bound.
- Positive coordinatewise unit rescaling preserves zero support and multiplicative coverage when `m_i,M_i` are rescaled coherently.
- Increasing `alpha` weakly reduces the number of positive bins.
- Empty `Y` is vacuous and excluded only to avoid irrelevant extrema conventions.

Status: **PROVED**.

## Composition

Audit 270's staged law remains applicable: if a support-safe compressed certificate has factor `a` and a subsequent approximation has factor `b`, the composed certificate has factor at most `ab`. Zero coordinates cause no exception because finite multiplicative domination already forces exact zero support where required.

Status: **PROVED** by Audit 270 plus Theorem 276.1.

## Prior-art collision

The generic mechanism is **IMPORTED/KNOWN**. Multiplicative epsilon-Pareto sets and geometric objective-space discretization are established in multiobjective optimization. In particular, the Papadimitriou–Yannakakis line of work establishes polynomial-cardinality approximate Pareto sets under positive-valued/bounded-encoding assumptions, and later work studies minimum-cardinality approximate Pareto sets. No novelty claim is made for geometric gridding.

The GC-II-specific value is narrower: Audit 276 identifies the exact operational role of zero typed costs in the `Omega_G` semantics. Zeros require support-exact treatment, but they are not themselves the source of approximate incompressibility; arbitrarily many unresolved positive scales are.

## Research status after Audit 276

- Positive-floor approximate compression: **PROVED** (Audit 275).
- Zero-support extension with positive floor on nonzero entries: **PROVED**.
- Exact support requirement at zero coordinates: **PROVED**.
- Uniform compression with arbitrarily small positive entries and no encoding/scale bound: **FALSIFIED**.
- Generic epsilon-Pareto gridding: **IMPORTED/KNOWN**.
- Dependency-width rather than ambient-dimension compression: **OPEN** and remains the higher-value structural target.
- Sharp lower bounds for support-stratified approximate certificates: **OPEN**.
