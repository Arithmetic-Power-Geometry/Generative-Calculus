# GC-II Audit 080 — Pareto Frontier Composition Collision

Status: **PROVED collapse in the finite complete-state additive regime; FALSIFIED as standalone GC-II novelty; OPEN only beyond ordinary compositional state and multiobjective path theory**

Branch scope: `gc2-capability-accounting-lab` only. GC-I `main` is frozen.

## 1. Candidate under attack

Audit 079 left a set-valued typed conversion-frontier candidate. Let

`F(x,z) = Pareto{ c(P) : P is an admissible x->z realization }`,

with typed nonnegative additive cost `c(P) in R_+^d` (for GC-II, typically `d=4` for `R,I,A,L`). A proposed novelty source was failure of a fixed-intermediate composition relation such as

`F(x,z) = Pareto( F(x,y) + F(y,z) )`.

The question in this audit is whether the resulting defect survives reduction to ordinary multiobjective path composition once the operational state is complete.

## 2. Through-state frontier theorem

### Theorem 080.1 (exact through-state composition)

Let the operational model be a finite directed graph whose vertices are complete operational states. Assume sequentially composable transitions and additive vector edge costs in `R_+^d`. Let `F_y(x,z)` denote the Pareto frontier of all admissible x->z realizations constrained to pass through state `y`, where the pre-y and post-y realizations may be chosen independently once `y` is reached. Then

`F_y(x,z) = Pareto( F(x,y) + F(y,z) )`,

where `+` is the Minkowski sum.

**Proof.** Every realization constrained through `y` decomposes at the first designated occurrence of `y` into an x->y prefix and y->z suffix, so its cost is a sum `a+b`. Conversely, any admissible x->y realization and admissible y->z realization concatenate because `y` is a complete compositional state. Removing dominated prefix or suffix labels cannot create a new nondominated sum under componentwise nonnegative minimization, so Pareto filtering may be performed before or after the Minkowski sum. QED.

This is a standard multiobjective dynamic-programming/label-composition identity, not a new GC invariant.

## 3. Scalarized defect is exactly directed triangle slack

For every weight vector `w in R_+^d`, define the scalarized conversion distance

`d_w(x,z) = min_{a in F(x,z)} w dot a`.

Then Theorem 080.1 gives

`min_{c in F_y(x,z)} w dot c = d_w(x,y) + d_w(y,z)`.

Hence the weighted fixed-intermediate defect is

`Delta_y^w(x,z) = d_w(x,y) + d_w(y,z) - d_w(x,z) >= 0`.

This is exactly the triangle slack of the directed shortest-path cost induced by `w`. Therefore any GC-II claim based only on a positive weighted frontier-composition defect collapses to an ordinary waypoint/constrained-routing penalty.

Status: **PROVED**.

## 4. Convexified frontiers do not rescue novelty

If free randomization/convexification is admitted and one works with the closed convex upper image

`U(x,z) = cl(conv(F(x,z) + R_+^d))`,

then its supporting scalarizations over nonnegative `w` characterize the convex upper image. The fixed-y discrepancy is therefore characterized by the family of ordinary triangle slacks `Delta_y^w`.

If convexification is not admitted, weighted sums can miss unsupported Pareto points. That residual is ordinary nonconvex multiobjective geometry, not by itself a generative-calculus phenomenon.

Status: **FALSIFIED as standalone novelty source**.

## 5. Apparent composition failure diagnoses incomplete state

Suppose an x->y realization leaves a catalyst, memory state, reservoir level, correlation, interface configuration, or hidden history that affects which y->z realizations remain admissible. Then bare `y` was not a complete compositional state. Augmenting the state with the continuation-relevant variable restores ordinary composition at the augmented-state level.

This may cause severe state explosion or computational hardness, but state explosion/hardness is not evidence for a new invariant by itself.

This is the same lesson reached in Audits 072-075 from a different direction: a composition defect caused by omitted continuation-relevant variables is a modeling incompleteness, not a third form of physical capability.

## 6. Exact finite-world experiment

`experiments/gc2_frontier_composition_audit.py` exhaustively enumerates all `3^6 = 729` assignments of two-dimensional positive labels from

`{(1,3),(2,2),(3,1)}`

to the six directed edges of the complete three-state graph. For three ordered `(source,target,waypoint)` triples and five nonnegative scalarizations

`(1,0), (0,1), (1,1), (1,2), (2,1)`,

it computes exact scalar shortest paths and tests

`d_w(s,y) + d_w(y,t) - d_w(s,t) >= 0`.

Results:

- graph assignments: `729`;
- scalarization/waypoint tests: `10,935`;
- triangle-slack violations: `0`;
- zero slack: `648`;
- positive slack: `10,287`;
- maximum observed slack: `9`.

The generated summary is stored in `results/gc2_frontier_composition_audit.csv`.

These are exact finite consistency checks, not novelty evidence.

## 7. Prior-art collision

The collision is direct:

1. Multiobjective shortest-path algorithms explicitly maintain nondominated label/frontier sets at states and compose labels under path extension.
2. Pareto-set Minkowski sums and dominance filtering are already standard computational objects in multiobjective optimization.
3. Recent temporal multiobjective shortest-path work studies even non-monotone/non-isotone objectives using label-correcting methods and identifies cases where cycles must be handled explicitly.

Relevant current references checked in this audit include:

- Bazgan, Kager, Thielen & Vanderpooten, *Networks* 85(1), 2025, DOI 10.1002/net.22253 — general label-setting algorithm and tractability analysis for multiobjective temporal shortest paths.
- Marica, Thielen & Wittmann, SAND 2026, DOI 10.4230/LIPIcs.SAND.2026.17 — label-correcting algorithms for multiobjective temporal shortest paths without assuming monotonicity/isotonicity.
- Karathanasis, Kontogiannis & Zaroliagis, 2025, arXiv:2508.20689 — dominance filtering for unions and Minkowski sums of Pareto sets.

Accordingly, neither Pareto-frontier composition nor its fixed-waypoint failure is a defensible standalone GC-II breakthrough claim.

## 8. Falsification boundary

The following candidate statement is rejected:

> A strict inclusion between an unrestricted typed conversion frontier and a fixed-intermediate Minkowski-composed frontier constitutes a new generative capability obstruction.

Under the assumptions above, strict inclusion only says that constraining the realization to pass through `y` worsens or removes some efficient alternatives. Scalarized, this is ordinary triangle slack. Set-valued, it is ordinary constrained multiobjective routing/dynamic programming.

Status: **FALSIFIED**.

## 9. What remains scientifically nontrivial

A surviving Paper-II target must no longer be merely a path/frontier defect. It must concern a property that remains after:

- complete-state augmentation;
- ordinary sequential/parallel composition;
- Pareto/Minkowski dynamic programming;
- convexification/free randomization when declared;
- catalysts and asymptotic conversion when declared;
- scalar and complete monotone families already known to the resource theory.

One possible remaining direction is a **budget-indexed closure complexity separation**: two operational theories can agree on all ordinary endpoint convertibility relations and all fixed-budget Pareto frontiers up to a declared scale, yet differ provably in the minimal description/computation required to generate the entire task-scale-error-budget closure as the budget/scale grows. That direction is **OPEN**, but it must be collision-tested against parametric optimization, automata/minimal realization, extension complexity, communication/query complexity, Kolmogorov/description complexity, and succinct-representation lower bounds before any novelty claim.

## 10. Status table

| Claim | Status |
|---|---|
| through-state Pareto frontier equals Pareto of Minkowski-composed subfrontiers in the complete-state additive regime | PROVED |
| every nonnegative scalarization of the fixed-waypoint defect is directed triangle slack | PROVED |
| exhaustive 729-graph / 10,935-test finite experiment has zero triangle-slack violations | NUMERICALLY SUPPORTED / exact enumeration |
| positive fixed-waypoint frontier-composition defect is standalone GC-II novelty | FALSIFIED |
| convexification makes the weighted defect a new invariant | FALSIFIED |
| continuation incompatibility with the same nominal intermediate state proves new physics | FALSIFIED unless complete-state augmentation also fails for a specified reason |
| budget-indexed closure complexity separation after ordinary conversion theory is quotiented out | OPEN |

No breakthrough claim is made in Audit 080.
