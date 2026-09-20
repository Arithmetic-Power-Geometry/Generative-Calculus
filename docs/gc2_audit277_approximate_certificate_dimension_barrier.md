# GC-II Audit 277 — Approximate-certificate dimension barrier

## Status

- Fixed-factor representative-certificate lower bound: **PROVED**.
- Claim that multiplicative tolerance alone removes exponential certificate size when the number of accounting coordinates grows: **FALSIFIED**.
- Generic approximate-Pareto mechanism: **IMPORTED/KNOWN**.
- GC-II interpretation as a capability-accounting dimension barrier: **CONDITIONAL contribution**.

## Setting

For a finite attainable set `Y` in the positive orthant and `alpha >= 1`, call `S subseteq Y` an alpha-representative certificate when every `y in Y` has some `s in S` satisfying

`s_i <= alpha y_i` for every coordinate `i`.

This is the representative form of the multiplicative typed-budget certificate used in Audits 267 and 275–276.

## Theorem (fixed-factor exponential dimension barrier)

Fix `alpha >= 1` and choose any `r > alpha`. For dimension `d`, let `k=floor(d/2)` and, for every `k`-subset `T` of `[d]`, define `y^T in {1,r}^d` by

`y^T_i = r` if `i in T`, and `1` otherwise.

Let

`Y_d = { y^T : |T|=k }`.

Then every alpha-representative certificate `S subseteq Y_d` equals `Y_d`. Hence

`|S| >= binom(d,floor(d/2)) = Theta(2^d/sqrt(d))`.

### Proof

Take distinct `S,T` with `|S|=|T|=k`. Equal cardinality and inequality imply there exists `i in S \ T`. At that coordinate,

`y^S_i = r > alpha = alpha y^T_i`.

Therefore `y^S` does not alpha-dominate/cover `y^T` in the minimization convention. Since this holds for every distinct pair, no member of `Y_d` can represent any other member. Thus every target requires itself in a representative certificate, proving the cardinality bound. The middle-binomial asymptotic follows from the standard central-binomial estimate.

## Consequence for Audits 274–276

Audit 274 proved an exponential exact-certificate barrier. Audits 275–276 proved a geometric-grid upper bound for multiplicative approximation under bounded positive dynamic range (with exact handling of zero support). Audit 277 shows the complementary limitation: approximation controls **scale resolution**, but does not remove the **dimension curse**. The product-form upper bound from Audit 275 can therefore be exponentially large in the number of typed accounting coordinates, and this is not merely an artifact of that construction.

In particular, the informal statement “controlled Omega_G accounting can be compressed” requires a dimensional qualifier. For fixed dimension and bounded log dynamic range, geometric compression is finite and controlled. If dimension itself grows, fixed multiplicative tolerance alone does not guarantee subexponential representative certificates.

## Edge and invariance checks

- `alpha=1`: choose any `r>1`; the construction reduces to an exact separation family.
- `d=1`: `k=0`, so the family has one vector and the bound is trivial.
- No zero-coordinate pathology is used: every coordinate is strictly positive.
- Dynamic range is constant: `max/min = r`, independent of `d`.
- Coherent positive coordinate rescaling preserves every pairwise failure because both sides of `s_i <= alpha y_i` scale equally.
- The result is about representative certificates `S subseteq Y`; it does not claim a lower bound for arbitrary synthetic points not operationally attainable.

## Prior-art collision note

Approximate Pareto sets, their minimum cardinality, and lower bounds for multiple objectives are established multiobjective-optimization topics. Papadimitriou–Yannakakis-style epsilon-Pareto theory and later work on minimum approximate Pareto sets already make clear that objective dimension is structurally important. Therefore the combinatorial separation mechanism is not claimed as new mathematics. The GC-II value is the exact operational warning it supplies for typed capability accounting: bounded multiplicative novelty tolerance solves scale resolution but not unbounded accounting dimension.

## Next target

Seek a positive structural theorem replacing raw dimension by an operational width parameter: e.g. dependency/witness width `w` plus bounded positive log dynamic range implies an alpha-certificate whose size depends exponentially on `w` rather than ambient `d`. This would connect Audit 271's local-to-global translator bound to Audits 275–277's exactness/compression boundary.
