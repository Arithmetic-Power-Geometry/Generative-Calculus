# GC-II Audit 301 — finite-block exact-accounting redundancy

Status: **PROVED**, with classical set-cover approximation machinery explicitly marked **IMPORTED/KNOWN**.

## Scope

This audit sharpens Audit 299.  Let a finite feasible-action accounting instance be

\[
I=(Y,A,\{B(a)\}_{a\in A}),\qquad \bigcup_{a\in A}B(a)=Y,
\]

with nonempty finite target set `Y`.  `N(I)` is the minimum number of actions whose feasible sets cover `Y`, and `N_f(I)` is the fractional-cover LP optimum.  For the strict independent product used in Audits 298–300, write

\[
N_k=N(I^{\times k}),\qquad n=|Y|,\qquad q=N_f(I).
\]

Audit 299 proved `N_f(I^{×k})=q^k` and the asymptotic identity `lim_k N_k^{1/k}=q`.  The question here is finite-block redundancy: how quickly does exact integer accounting approach that rate?

## Theorem 301.1 — finite-block redundancy bound

For every integer `k>=1`,

\[
q^k\le N_k\le H_{n^k}\,q^k\le (1+k\ln n)q^k,
\]

where `H_m=sum_{j=1}^m 1/j` is the harmonic number.  Consequently, in base-two accounting bits,

\[
0\le \log_2 N_k-k\log_2 q
\le \log_2 H_{n^k}
\le \log_2(1+k\ln n).
\]

Equivalently, the per-copy redundancy obeys

\[
0\le {1\over k}\log_2N_k-\log_2q
\le {\log_2(1+k\ln n)\over k}
=O\!\left({\log k\over k}\right).
\]

### Proof

1. The lower bound is the LP relaxation: `N_f(I^{×k}) <= N(I^{×k})`.  Audit 299's tensor primal/dual proof gives `N_f(I^{×k})=q^k`; hence `q^k<=N_k`.
2. The product instance has exactly `n^k` targets.  The classical set-cover LP rounding/integrality-gap theorem gives, for any finite set-cover instance on `m` ground elements, `N <= H_m N_f`.  Apply it with `m=n^k` to obtain `N_k<=H_{n^k}q^k`.
3. The standard harmonic estimate `H_m<=1+ln m` gives `H_{n^k}<=1+ln(n^k)=1+k ln n`.
4. Taking base-two logarithms yields the bit-redundancy bound.  Division by `k` gives the per-copy rate.

No assumption of additivity of the integer accounting number is used.

## Edge and degenerate cases

- `n=1`: every feasible instance has `q=N_k=1`; the bound gives zero redundancy exactly.
- `q=1`: the theorem allows finite integer overhead but forces asymptotic rate zero; this is consistent with Audit 299.
- Empty `Y` is excluded because logarithmic rate for the conventional empty cover `N=0` is undefined.  It can be treated separately as a vacuous accounting problem.
- Duplicate actions do not change either optimum.
- Removing actions can only weakly increase `N_k` and `q`; adding actions can only weakly decrease them.  The theorem remains valid after either operation provided feasibility is retained.
- Relabelling targets/actions leaves all quantities invariant.

## Exact collision / sanity witness

For the Audit-298 triangle instance

\[
B_0=\{0,1\},\quad B_1=\{0,2\},\quad B_2=\{1,2\},
\]

we have `n=3`, `q=3/2`, and exact enumeration from Audit 299 gives

\[
N_1=2,\qquad N_2=3,\qquad N_3=5.
\]

The excess bits above the fractional baseline are respectively

\[
\log_2(4/3),\quad \log_2(4/3),\quad \log_2(40/27),
\]

all below `log2(H_{3^k})` and therefore below `log2(1+k ln 3)`.

Minimal reproducibility check:

```python
from fractions import Fraction
from math import log2, log

Ns = {1: 2, 2: 3, 3: 5}
q = Fraction(3, 2)
n = 3
for k, Nk in Ns.items():
    excess = log2(Nk / float(q**k))
    harmonic = sum(1/j for j in range(1, n**k + 1))
    assert excess >= -1e-12
    assert excess <= log2(harmonic) + 1e-12
    assert excess <= log2(1 + k*log(n)) + 1e-12
print('audit301: PASS')
```

## Interpretation

Audit 299 identified the exact regularized rate.  Audit 301 adds a universal finite-block guarantee: exact operational accounting needs at most `O(log k)` extra bits above the fractional asymptotic baseline for a block of `k` independent copies, hence only `O(log k/k)` extra bits per copy.

This is useful because the asymptotic theorem alone did not provide a convergence rate.  It also shows that the one-shot integrality obstruction cannot create a linear-in-`k` bit penalty under strict independent repetition.

## Prior-art collision discipline

The harmonic set-cover integrality-gap/rounding theorem and `H_m<=1+ln m` are classical and are **IMPORTED/KNOWN**.  Fractional hypergraph covering is likewise established mathematics.  Therefore GC-II must **not** claim invention of these combinatorial facts.  The GC-II contribution of this audit is only the operational corollary obtained after the exact capability-accounting reduction and Audit-299 tensorization: a finite-block redundancy law for this accounting semantics.

Nearby literatures to cite/check in Paper II: set cover and LP rounding; fractional hypergraph covers; rectangle/product covers; zero-error and nondeterministic communication covering quantities.  No novelty claim is made until a genuinely GC-specific dynamic/budgeted extension survives those collisions.

## Status ledger

- `N_f(I^{×k})=q^k`: **PROVED** in Audit 299.
- `q^k <= N_k`: **PROVED**.
- `N_k <= H_{n^k} q^k`: **PROVED using IMPORTED/KNOWN set-cover theory**.
- total excess description length `<= log2(1+k ln n)`: **PROVED**.
- per-copy redundancy `O(log k/k)`: **PROVED**.
- claim that finite-block redundancy can remain positive constant per copy: **FALSIFIED** for this strict independent-product model.
- extension to evolving budgeted closure with endogenous admissibility, information acquisition, generated actions/rules, or shared reusable resources: **OPEN**.

## Next attack

Return to Paper-II priority (1): determine the weakest dynamic/budgeted assumptions under which an analogue of this sublinear redundancy survives.  In particular, test whether shared reusable resources or endogenous action generation can make the block overhead extensive, which would separate genuinely generative operational closure from static hypergraph covering.
