# GC-II Test Report 003

Date: 2026-09-08
Branch: `gc2-capability-accounting-lab`

## Executive conclusion

No breakthrough claim is justified yet. The present test round produced three useful outcomes: (i) the GC-I parity/projection obstruction was independently extended and rechecked through dimension m=10; (ii) the unrestricted translator-arity conjecture remains decisively falsified because binary XOR composition realizes global parity with arity 2; and (iii) the reachable-envelope transport law survives a 20,000-trial deterministic randomized audit under nonnegative additive path costs, while an explicit superadditive-composition counterexample confirms that a composition-cost assumption is essential.

The strongest surviving GC-II research target remains a resource-accounted whole-envelope reconstruction/translation complexity, not projection order by itself.

## Test A — Proper-projection parity audit

For each m=2,...,10, define the even- and odd-parity relations on `{0,1}^m`.

Verified exactly:

1. Every projection onto every strict subset of coordinates is identical for the two relations.
2. The relations themselves are different and disjoint.
3. Reconstruction from all `(m-1)`-coordinate projections yields the entire Boolean cube `{0,1}^m`, not either parity relation.

Exact rows:

| m | size of each parity relation | reconstruction from all proper projections | binary XOR tree depth | binary XOR gate count |
|---:|---:|---:|---:|---:|
| 2 | 2 | 4 | 1 | 1 |
| 3 | 4 | 8 | 2 | 2 |
| 4 | 8 | 16 | 2 | 3 |
| 5 | 16 | 32 | 3 | 4 |
| 6 | 32 | 64 | 3 | 5 |
| 7 | 64 | 128 | 3 | 6 |
| 8 | 128 | 256 | 3 | 7 |
| 9 | 256 | 512 | 4 | 8 |
| 10 | 512 | 1024 | 4 | 9 |

Status: **PROVED / computationally reverified; mathematical mechanism known.**

## Test B — Translator-arity conjecture

Candidate rejected:

`r_G(A,B)=k => every faithful translator must use primitive arity >= k`.

Counter-mechanism: global parity of m inputs is computable by a tree of binary XOR gates. Thus primitive arity is fixed at 2 while the projection-distinguishing order is m. The tree uses `m-1` binary XOR gates and depth `ceil(log2 m)`.

Status: **FALSIFIED for unrestricted compositional translators.**

What survives is the possibility of a lower bound only after an independently specified resource model is fixed (depth, communication, memory, geometry, allowed gates, error, etc.).

## Test C — Reachable-envelope transport audit

Finite operational worlds were instantiated as random directed graphs with 3--8 states and nonnegative integer edge costs 0--9. For a state x, `R_x(B)` is the set of states reachable with shortest-path cost at most B.

With deterministic seed `20260908`, 20,000 random worlds/transitions were generated. Among them, 11,441 sampled `(x,y)` pairs were reachable. Across those cases, 36,171 individual memberships in `R_y(B)` were checked against

`R_y(B) subseteq R_x(B + c_xy)`.

Observed violations: **0**.

This is computational confirmation only; the reason is path concatenation/triangle-type subadditivity, so this test does not establish novelty.

Status: **NUMERICALLY VERIFIED in the finite path-cost specialization; theorem mechanism inherited from composition/subadditivity.**

## Test D — Necessity of composition-cost control

Explicit counterexample to any transport theorem lacking a subadditive composition hypothesis:

- `c(x,y)=1`,
- `c(y,t)=1`,
- but the admissible composed realization `x->t` is charged cost 3,
- choose `B=1`.

Then `t in R_y(1)` but `t notin R_x(2)`.

Therefore a theorem of the form

`R_y(B) subseteq R_x(B+c_xy)`

requires an assumption ensuring that composing `x->y` and `y->t` costs no more than the appropriately combined budget.

Status: **COUNTEREXAMPLE / assumption confirmed necessary.**

## Consequence for the No-Free-Capability target

The current proposed statement

`Delta R = Delta I = Delta A = Delta L = 0 => Omega_G = 0`

cannot be treated as a theorem until world evolution itself is restricted. If two world descriptions are allowed to change their task/capability relation exogenously while `R,I,A,L` are held nominally fixed, the implication can fail by construction. Therefore Paper II must define an admissible world-transition operator (or dynamical closure) before the statement becomes meaningful.

This is a conceptual requirement, not merely notation.

## Consequence for Omega_G

A simple set residual such as

`|E_1 \ Cl(E_0)| / |E_1|`

is useful as a finite benchmark diagnostic but is not a credible novelty claim. A GC-native `Omega_G` must incorporate task identity, scale, error, vector resources, and one globally realizable translator, and should have operationally useful equivalent characterizations or quantitative bounds.

## Strongest surviving theorem target

Define an independently specified translator model `H_n`, cost `C_H`, observation family `P_<k`, and operational discrepancy `D_G`. Then seek a family of whole envelopes for which

`K_G^eps(E_n | P_<k(E_n); H_n) >= f(n,k,eps)`

while a matched comparison family has asymptotically smaller cost, despite agreement on fixed-task Pareto data, low-order projections, and conventional scalar summaries.

This is only a **BREAKTHROUGH CANDIDATE TARGET**, not a result.

## Prior-art implications

The current audit must continue to treat complete-monotone characterizations with caution: general quantum resource theory already contains strong impossibility results for finite complete monotone families, and generic convertibility-via-monotones is mature resource-theory machinery. Likewise, projection/join reconstruction is mature database theory and parity complexity is mature circuit complexity. GC-II novelty, if any, must come from a theorem coupling the whole task-scale-error-vector-resource envelope with a single globally realizable translation and yielding a quantitative consequence not inherited from those specializations.

## Current status

- Operational closure: **OPEN**
- Generative Novelty Gap `Omega_G`: **OPEN / requires nontrivial operational definition**
- Closure-Escape theorem: **OPEN**
- No-Free-Capability theorem: **OPEN / admissible world evolution must be specified first**
- Quantitative accounting bound: **OPEN**
- Complete convertibility: **OPEN / high prior-art collision risk**
- Projection irreducibility: **PROVED mechanism / not itself novel**
- Arity-only translator lower bound: **FALSIFIED**
- Resource-accounted reconstruction complexity `K_G`: **OPEN / highest-priority surviving route**
- Finite parity audit m=2..10: **PASS**
- Random reachable-transport audit: **PASS, 36,171 memberships, 0 violations**
- Breakthrough status: **NONE YET**

## Reproduction

Run:

`python gc2/tests/test_gc2_finite_audit.py`

The script uses only the Python standard library and a fixed random seed.
