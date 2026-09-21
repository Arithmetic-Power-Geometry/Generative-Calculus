# GC-II Audit 299 — regularized product accounting rate

## Scope
This audit continues Audit 298 for a finite feasible-action accounting instance I=(Y,A,{B(a)}). It does not modify GC-I foundations.

Let N(I) be the minimum number of feasible-action sets B(a) needed to cover Y. For the strict Cartesian product I×J, targets are Y_I×Y_J and feasible sets are B_I(a)×B_J(b). Write I^{×k} for the k-fold product and N_k=N(I^{×k}).

Define the fractional account number

N_f(I)=min sum_a x_a
subject to sum_{a:y in B(a)} x_a >= 1 for every y in Y, x_a >= 0.

Its LP dual is

N_f(I)=max sum_y z_y
subject to sum_{y in B(a)} z_y <= 1 for every a, z_y >= 0.

All quantities are dimensionless counts/weights.

## Theorem 299A — existence of the regularized accounting rate [PROVED]
For every finite feasible instance,

R_inf(I) := lim_{k->infinity} (1/k) log N_k

exists and equals inf_{k>=1}(1/k)log N_k.

### Proof
Audit 298 gives N(I×J)<=N(I)N(J). Hence N_{k+l}<=N_k N_l, so a_k=log N_k is subadditive. Fekete's lemma gives existence of the limit and the infimum formula. Degenerate empty Y is excluded from the logarithmic rate; it has N=0 and should be handled separately. For every nonempty feasible instance N_k>=1, so the logarithm is defined.

## Theorem 299B — exact asymptotic collapse to the fractional account [PROVED]
For every finite nonempty feasible instance,

R_inf(I) = log N_f(I).

Equivalently,

lim_{k->infinity} N(I^{×k})^{1/k} = N_f(I).

### Proof
1. Fractional multiplicativity. Let x and x' be optimal fractional covers for I and J. The product weights x_a x'_b form a feasible fractional cover of I×J, proving N_f(I×J)<=N_f(I)N_f(J). Conversely, let z and z' be optimal dual fractional packings. Product weights z_y z'_{y'} are feasible for the product dual, proving the reverse inequality. Therefore

N_f(I×J)=N_f(I)N_f(J),

and N_f(I^{×k})=N_f(I)^k.

2. Lower bound. LP relaxation gives

N_k >= N_f(I)^k.

3. Upper bound. The classical finite set-cover LP integrality-gap bound gives, for a universe of M elements,

N <= H_M N_f,

where H_M is the M-th harmonic number. The k-fold target universe has |Y|^k elements, hence

N_k <= H_{|Y|^k} N_f(I)^k.

4. Take logarithms and divide by k:

log N_f(I) <= (1/k)log N_k <= log N_f(I)+(1/k)log H_{|Y|^k}.

Since H_m <= 1+log m, log H_{|Y|^k}=O(log k), and the final term tends to zero. Squeeze gives the result.

## Corollary 299C — finite integrality can disappear per copy [PROVED]
Audit 298 showed N(I×I)<N(I)^2 can occur. Audit 299 strengthens this: the asymptotic per-copy exact-account cost is governed by the fractional cover, not the one-shot integer cover. If N_f(I)<N(I), then

R_inf(I)=log N_f(I)<log N(I).

Thus independent repetition can produce a strict asymptotic accounting advantage even though every block is still covered exactly (zero operational loss).

## Exact triangle witness [PROVED]
For Y={0,1,2} and feasible sets {0,1},{0,2},{1,2},

N(I)=2,   N_f(I)=3/2.

A primal fractional certificate assigns weight 1/2 to each action; a dual certificate assigns weight 1/2 to each target. For every k, product certificates give

N_f(I^{×k})=(3/2)^k.

Exact enumeration gives N_1=2, N_2=3, N_3=5. Hence the one-shot rate log 2 regularizes to log(3/2).

## Checks
- Domains/dimensions: N and N_f are dimensionless; logarithm base only rescales the rate.
- Degenerate empty target universe: N=0, so logarithmic regularization is not defined without a convention; excluded explicitly.
- Universal action: N=N_f=1 and R_inf=0.
- Monotonicity: adding feasible actions cannot increase N or N_f.
- Relabeling invariance: all quantities depend only on the incidence set system.
- Composition: integer N is submultiplicative (Audit 298); fractional N_f is exactly multiplicative.
- Edge cases: duplicate actions do not change either optimum; uncovered targets make the instance infeasible and are excluded.

## Prior-art collision / novelty discipline
The ingredients are established: finite set cover, its fractional LP and dual, logarithmic/harmonic integrality-gap bounds, product/tensor arguments, and Fekete subadditivity. Therefore these ingredients are IMPORTED/KNOWN and no generic combinatorial novelty is claimed. The GC-II contribution is the operational interpretation and the exact consequence for repeated capability accounting: the regularized exact account rate equals the logarithm of the fractional feasible-action cover number.

This should be presented as a structural GC-II theorem/corollary built from known combinatorial machinery, not as invention of fractional cover theory.

## Status
- Existence of R_inf: PROVED.
- Fractional product multiplicativity: PROVED.
- R_inf=log N_f: PROVED using IMPORTED/KNOWN set-cover integrality-gap theory.
- Triangle N_1,N_2,N_3=2,3,5: EXACTLY VERIFIED.
- Generic claim that one-shot log N is the asymptotic accounting rate: FALSIFIED whenever N_f<N.
- Novelty of the underlying fractional/tensor machinery: IMPORTED/KNOWN.
- Extension from static feasible-action incidence to budgeted operational closure with transformations/information/actions changing across rounds: OPEN.
