# GC-II Audit 305 — Higher-order interaction obstruction

## Status

- Proper-marginal indistinguishability theorem: **PROVED**.
- Pairwise-complete accounting suffices in unrestricted systems: **FALSIFIED**.
- Any fixed interaction truncation below full order suffices universally: **FALSIFIED**.
- Parity / k-wise-independence mechanism: **IMPORTED/KNOWN**; not claimed as new.
- GC-II consequence for capability accounting: **PROVED**.

## Setup

Let the operational feature object have `d >= 2` binary channels,

`x=(x_1,...,x_d) in {0,1}^d`.

Define the even- and odd-parity supports

`E_d={x : sum_i x_i = 0 (mod 2)}`,

`O_d={x : sum_i x_i = 1 (mod 2)}`.

Equip each support with the uniform distribution.  The independently fixed task is

`u_even(x)=1[sum_i x_i = 0 (mod 2)]`.

For reachable-set value `V_u(C)=max_{x in C} u(x)`, we have

`V_u(E_d)=1` and `V_u(O_d)=0`.

The same separation holds for uniform-support expectation: the values are 1 and 0.

## Theorem 305.1 — all proper marginals collide

For every proper coordinate subset `S subsetneq {1,...,d}`, the marginal of the uniform distribution on `E_d` projected to `S` is exactly uniform on `{0,1}^{|S|}`.  The same is true for `O_d`.  Hence the two systems have identical marginals of every order `0,...,d-1`, despite a unit gap on `u_even`.

### Proof

Fix a proper subset `S` of size `s<d` and an assignment `a in {0,1}^s`.  There are `d-s >= 1` unobserved bits.  After fixing `a`, exactly half of their `2^(d-s)` assignments complete the total vector to even parity and exactly half complete it to odd parity.  Thus each `a` has `2^(d-s-1)` completions in `E_d` and the same number in `O_d`.  Since both supports have size `2^(d-1)`,

`P_E[X_S=a]=P_O[X_S=a]=2^(-s)`.

This holds for every proper `S` and `a`. QED.

## Corollary 305.2 — pairwise repair of Audit 304 is insufficient

At `d=3`, all singleton and pairwise marginals of `E_3` and `O_3` are identical, but `u_even` separates them by one. Therefore an accounting law that records all one-channel changes and all pairwise coupling changes can still report zero change while operational novelty is positive.

In particular, a proposed repair

`Omega_G <= F(Delta_i, Delta_ij)`

with `F(0)=0` is impossible for unrestricted three-channel operational systems whenever `Delta_i` and `Delta_ij` depend only on singleton and pairwise marginals.

## Corollary 305.3 — no universal bounded-order truncation

For every `k>=1`, choose `d=k+1`.  Then `E_d` and `O_d` agree on every marginal involving at most `k` channels but differ maximally on the parity task. Therefore no universal capability-accounting summary truncated at any fixed interaction order `k<d` can be complete over unrestricted `d`-channel systems.

This does **not** imply that full exponential joint tables are always necessary. Structural assumptions can make low-order summaries complete: factorization, bounded graphical width, decomposability, restricted task classes, or other independently justified constraints may collapse the required interaction order. Determining the weakest useful such conditions remains **OPEN**.

## Consequence for the Paper-II bound

Audit 304 showed that separate channel marginals cannot support a faithful universal `F(Delta R,Delta I,Delta A,Delta L)` law. Audit 305 strengthens this: simply appending pairwise interaction deltas is not a universal repair, and neither is any interaction hierarchy stopped strictly below the maximum order in an unrestricted system.

The defensible directions are therefore:

1. use a discrepancy on the full joint operational object;
2. use a complete hierarchy through the interaction order required by the task/system class; or
3. prove structural assumptions under which a lower-order hierarchy is complete.

## Edge and degeneracy checks

- `d=1`: excluded from the proper-interaction statement because there is no nonempty lower-order marginal carrying channel information; the parity supports are singletons.
- `d=2`: recovers Audit 304's correlated/anticorrelated witness; singleton marginals coincide.
- `d=3`: singleton and pairwise marginals coincide; this is the minimal witness against pairwise-complete accounting.
- Relabeling coordinates preserves the result.
- Complementing one coordinate swaps `E_d` and `O_d`; hence the obstruction is symmetric.
- Cartesian duplication does not remove the collision unless the summary includes an order capable of seeing the parity constraint.
- The theorem concerns unrestricted joint operational objects; it makes no claim against model classes where the joint is uniquely determined by low-order marginals.

## Prior-art collision discipline

The mathematical mechanism is classical: parity/XOR examples exhibit pairwise or, more generally, `(d-1)`-wise independence without full mutual independence, and marginal-problem/statistical-interaction literatures explicitly study information absent from lower-order marginals. Accordingly, the parity construction, k-wise-independence phenomenon, and generic statement that proper marginals need not determine a joint distribution are **IMPORTED/KNOWN**.

The retained GC-II result is narrower and operational: after Audit 304, a finite-order interaction repair of capability accounting is provably incomplete in the unrestricted typed closure. This is a design constraint on any claimed quantitative novelty bound, not a claim to have invented higher-order interactions.

## Reproducibility

`experiments/gc2_audit305_parity_marginal_hierarchy.py` exhaustively verifies, for `d=2,...,7`, equality of every proper-coordinate marginal between the even- and odd-parity supports and the unit task-value separation.
