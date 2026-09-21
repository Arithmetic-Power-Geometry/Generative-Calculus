# GC-II Audit 288 — Exact typed-budget sufficiency criterion

## Status

**PROVED** for finite attainable typed-cost sets.  The generic factorization/sufficient-statistic idea is **IMPORTED/KNOWN**; the point here is the exact consequence for the GC-II budget-query semantics after Audit 287.

## Setup

Let `Y` be a finite subset of `R_+^d` of attainable typed cost vectors.  For every typed budget `q in R_+^d`, define the feasibility decision

`D_q(y) = 1[y <= q]`,

with coordinatewise order.  Let `L:Y -> S` be any scalar or compressed resource account.  Call `L` **exactly budget-sufficient** when every `D_q` factors through `L`: for every q there is `phi_q:S->{0,1}` such that

`D_q = phi_q o L` on Y.

No linearity, continuity, or attainability of decoded summaries is assumed.

## Theorem 288.1 — all-budget sufficiency iff injectivity

For finite `Y`, the following are equivalent:

1. `L` is exactly budget-sufficient for the full family `{D_q : q in R_+^d}`.
2. `L` is injective on `Y`.
3. Every fiber of `L` contains exactly one attainable typed vector.

### Proof

`(2) => (1)`: because Y is finite, define `phi_q(L(y)) := D_q(y)` on `L(Y)`; injectivity makes this well-defined. Extend arbitrarily outside `L(Y)`.

`(1) => (2)`: suppose `y != y'` and `L(y)=L(y')`. If `y' not<= y`, budget `q=y` gives `D_q(y)=1` and `D_q(y')=0`. Otherwise `y'<=y`; since the vectors are distinct, `y not<=y'`, and budget `q=y'` gives the reverse distinction. Thus some typed budget distinguishes every distinct pair. Such a decision cannot factor through a map that identifies that pair. Contradiction.

`(2) <=> (3)` is immediate.

## Corollary 288.2 — exact accounting-state lower bound

Any exact account preserving **all** typed budget-feasibility decisions must expose at least

`|L(Y)| >= |Y|`

distinct account states.  If stored in fixed-length binary form, it requires at least

`ceil(log2 |Y|)` bits.

For the independent-deposition family of Audits 280–287, `|Y_m|=2^m`, hence every exact all-budget-sufficient account needs at least `2^m` states and `m=d/2` bits.

Audit 287's additive scalar `sum_i y_i = m(r+1)` has one state, so it is maximally insufficient for this family: it collapses all `2^m` typed vectors.

## Important anti-overclaim: scalar dimension is not the issue

A real-valued scalar can be injective on any finite Y if arbitrary precision and arbitrary encoding are allowed. Therefore **one scalar coordinate does not itself imply information loss**. What matters is whether the account is injective (for the full typed-budget query family), or more generally how many decision-distinct fibers it merges. Any Paper-II information bound must charge account precision/cardinality or an operationally constrained encoding class, not merely the number of scalar fields.

This also prevents a false inference from Audit 287: `sum_i y_i` fails, but not every scalarization must fail.

## Restricted query family

For a restricted set Q of budgets, exact sufficiency is equivalent to

`L(y)=L(y') => D_q(y)=D_q(y') for every q in Q`.

This is the standard factorization-through-fibers criterion and is therefore **IMPORTED/KNOWN** in spirit.  The full typed-budget family is special because it separates every pair of distinct vectors, reducing the criterion to injectivity.

## Edge and composition audit

- Singleton Y: one state is sufficient; theorem is exact.
- Duplicate operational histories producing the same typed vector: no distinction is required at the typed-budget layer; theorem acts on vectors, not histories.
- Zero coordinates: proof is unchanged.
- Comparable and incomparable pairs: both are separated by choosing one member itself as the budget; both cases are explicitly covered in the proof.
- Monotonicity: every D_q is monotone under coordinatewise cost decrease in the expected direction.
- Relabeling/permutation of typed coordinates: criterion is invariant when budgets are permuted consistently.
- Cartesian composition: `|Y1 x Y2|=|Y1||Y2|`, so exact state lower bounds multiply and bit lower bounds add when all product vectors are attainable.
- Degenerate scalar: constant L is sufficient iff |Y|=1 for the full typed-budget family.

## Prior-art collision assessment

The abstract statement that a statistic/representation is sufficient for a decision family iff the decisions are constant on its fibers is standard factorization/equivalence-class machinery. Multiobjective scalarization and multiutility representation are also established. **Do not claim those as new.**

The GC-II value is the operational sharpening forced by Audits 287–288: for the complete family of coordinatewise resource budgets, decision equivalence is equality of typed cost vectors. Consequently any exact resource account preserving all such admissibility decisions must retain the full attainable typed-state cardinality, even though a chosen exact additive aggregate may have only one value.

## Consequence for the Paper-II accounting bound

A candidate `Omega_G <= F(Delta R, Delta I, Delta A, Delta L)` cannot safely interpret `Delta R` as an unconstrained aggregate scalar.  For exact all-budget claims, `Delta R` must retain a separating representation of typed resource states, or the theorem must explicitly restrict the downstream budget/query family and prove sufficiency relative to it.

## Labels

- Full typed-budget family separates all distinct typed vectors: **PROVED**.
- Exact all-budget scalar/account sufficiency iff injectivity on Y: **PROVED**.
- `ceil(log2 |Y|)` fixed-length state lower bound: **PROVED**.
- Audit-287 sum scalar is insufficient on the independent-deposition family: **PROVED**.
- Generic fiber-factorization/sufficient-statistic principle: **IMPORTED/KNOWN**.
- Claim that every one-dimensional real scalarization loses typed information: **FALSIFIED / NOT CLAIMED**.
- Approximate/decision-relative analogue with a nontrivial rate-distortion-style bound: **OPEN**.
