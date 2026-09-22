# GC-II Audit 321 — Heterogeneous pairwise-to-joint extremal bound

## Scope
Finite deterministic diagnostic subclass. A current unresolved cell `B` contains `K` decision-critical classes (equivalently, quotient worlds by equal required decision). Tests have fixed nonnegative costs, deterministic outcomes, are globally admissible on the cell where used, and may be reused. This audit does **not** assume unit costs. State-dependent admissibility is not covered.

## Definitions
For a non-decision-homogeneous cell `B`, let

`V(B)` = minimum worst-case total cost of an adaptive test tree whose leaves are decision-homogeneous.

For two classes `x != x'` requiring different decisions, define their cheapest direct separating-test cost

`p(x,x') = min{ c(u) : Z_u(x) != Z_u(x') }`.

Let

`P(B) = max_{x != x'} p(x,x')`.

If some incompatible pair is not separable, set `P(B)=+infinity` and the finite theorem below is vacuous.

## Theorem 321.1 — exact universal heterogeneous-cost distortion
Assume `0 < P(B) < infinity`. If `B` contains `K >= 2` decision-critical classes, then

`P(B) <= V(B) <= (K-1) P(B)`.

Moreover the coefficient `K-1` is tight for every `K >= 2`.

### Proof: lower bound
Choose a pair `(x,x')` attaining `P(B)`. Any resolving decision tree must eventually separate this pair. Along their common history before separation, the first test that separates them has cost at least `p(x,x')=P(B)`. Hence the worst-case path cost is at least `P(B)`.

### Proof: upper bound
Induct on the number `K` of decision-critical classes in the current cell.

Base `K=1`: `V=0`.

For `K>=2`, choose any two distinct classes `a,b`. By definition of `P(B)`, there exists a test `u` separating them with `c(u)<=P(B)`. Apply `u` at the root. Every nonempty outcome cell contains at most `K-1` classes because `a,b` fall into different outcomes. Pairwise separating costs inside each outcome cell remain at most `P(B)`: the same globally admissible tests witnessing separation in `B` remain available in the restricted cell. By induction, every child cell `C` can be resolved at cost at most `(|C|-1)P(B) <= (K-2)P(B)`. Therefore

`V(B) <= P(B) + (K-2)P(B) = (K-1)P(B)`.

This proof permits binary or multi-outcome tests and arbitrary heterogeneous nonnegative costs.

### Tightness
Take `K` classes and singleton tests `u_i(x)=1[x=i]`, all with cost `p>0`. Then every pair is separated by a cost-`p` test, so `P=p`. An adversary can answer `0` to the first `K-1` useful singleton tests, forcing cost `(K-1)p`; sequential singleton testing attains it. Thus

`V/P = K-1`.

## Consequence for GC-II capability accounting
Audit 320's unit-cost extremal result is not a normalization artifact. In the fixed-admissibility deterministic subclass, the complete worst-case distortion between a maximum cheapest-pair witness account and one globally resolving adaptive policy is exactly `K-1`, even with heterogeneous test costs.

Therefore a pairwise closure-escape catalogue is a valid lower-bound certificate but is not a complete capability account. Any proposed `Omega_G` that substitutes `P` for joint adaptive resolution can understate operational cost by the exact worst-case factor `K-1`.

## Boundary / counterexample pressure
The induction uses one structural assumption critically: a test admissible on `B` remains admissible after conditioning to a child cell. With branch-relative or state-dependent authorization this heredity can fail. Then pairwise witnesses may be mutually incompatible and even finite `P` need not imply a finite joint resolver. That is the next target; no theorem is claimed here for non-hereditary admissibility.

Zero-cost tests: if `P=0`, the ratio `V/P` is undefined. Under the same finite/hereditary assumptions, the induction gives `V=0` when every incompatible pair has a zero-cost separator. The stated ratio theorem therefore uses `P>0`.

Infinite costs / inseparable pairs: excluded from the finite theorem and recorded as a closure blocker rather than assigned a finite gap.

## Composition and dimensions
`P` and `V` both have units of operational cost; `V/P` is dimensionless. Multiplying every test cost by `lambda>0` scales both `P` and `V` by `lambda`, leaving the distortion invariant. No additivity under independent composition is assumed or proved.

## Prior-art collision
The recurrence and identification-tree viewpoint belong to classical optimal decision-tree / active diagnosis theory. This audit does not claim decision-tree optimization as new. The GC-II use is a boundary result for pairwise versus jointly composable closure-escape accounting. Literature on optimal decision trees already treats test costs and adaptive identification; therefore novelty claims must be restricted to the GC-II interpretation and integration, not the combinatorial mechanism.

## Status ledger
- `P(B) <= V(B)`: **PROVED**.
- `V(B) <= (K-1)P(B)` under finite deterministic fixed/hereditary admissibility: **PROVED**.
- Tight coefficient `K-1` for every `K>=2`: **PROVED**.
- Unit-cost restriction of Audit 320: **REMOVED**.
- Decision-tree machinery: **IMPORTED/KNOWN**.
- Extension to branch-relative/non-hereditary admissibility: **OPEN**.
- Claim that finite pairwise witnesses always imply finite joint resolution without heredity: **NOT CLAIMED; attack next**.
