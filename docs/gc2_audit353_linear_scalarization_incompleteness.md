# GC-II Audit 353 — Linear scalarization is not a complete vector-capability certificate

## Question

Audit 351 identified the Pareto-minimal resource antichain as a complete certificate for all componentwise budgets, while Audit 352 showed that explicit antichain enumeration can be exponential. A natural compression attempt is to replace the antichain by all nonnegative weighted-sum optima.

For a finite attainable cost set C subset R_+^d define the linear scalarization profile

h_C(w) = min_{c in C} <w,c>,  w in R_+^d.

Can h_C determine every budget-feasibility query?

## Exact collision

Consider two two-resource operational systems with the same source and target and attainable path-cost sets

A = {(0,3),(3,0)},
B = {(0,3),(3,0),(2,2)}.

The extra vector (2,2) is Pareto-minimal in B: neither endpoint dominates it. Nevertheless, for every w=(a,b) in R_+^2,

h_A(w) = min(3a,3b).

Also

2a+2b >= 2 max(a,b) >= min(3a,3b)

is not the useful sharp comparison in all ratios; instead if a<=b then min(3a,3b)=3a and 2a+2b>=4a>=3a, while if b<=a the symmetric argument gives 2a+2b>=4b>=3b. Hence

h_B(w)=h_A(w) for every nonnegative w.

But at componentwise budget beta=(2,2), B is feasible and A is not. Therefore the full continuum of nonnegative linear scalarizations is not a complete invariant for vector budgeted closure.

## Theorem 353.1 — supported-profile incompleteness

There exist finite two-resource operational systems X and Y such that

1. h_X(w)=h_Y(w) for every w in R_+^2;
2. their Pareto-minimal requirement sets differ; and
3. some componentwise budget query has opposite answers in X and Y.

Thus no exact GC-II convertibility criterion that factors only through the full weighted-sum profile h can be complete for arbitrary finite vector-resource systems.

**Status: PROVED.**

## Geometry

The profile h_C exposes only supported efficient cost vectors, i.e. points visible to a supporting linear functional. The vector (2,2) is an unsupported nondominated requirement relative to endpoints (0,3) and (3,0). Componentwise budget feasibility depends on the upward closure C+R_+^d, not merely on the supported lower convex envelope.

This is a classical phenomenon in multiobjective optimization and multiobjective shortest paths. Accordingly, unsupported-efficient-point machinery is **IMPORTED/KNOWN**. The GC-II result is a boundary/no-go statement for the proposed complete-monotone compression, not a novelty claim for weighted-sum failure itself.

## Consequences for Paper II

- Audit 350: one additive resource -> one exact scalar threshold.
- Audit 351: vector resources -> exact Pareto antichain.
- Audit 352: the explicit antichain may be exponentially large.
- Audit 353: even the continuum of linear weighted-sum scalar thresholds can lose exact budget-feasibility information.

Therefore a structured complete criterion must retain unsupported Pareto requirements or use a genuinely complete nonlinear/constraint-based family (for example budget-indicator/epsilon-constraint style queries). Linear scalarization alone is insufficient.

## Edge and invariance checks

- Resource dimension: the obstruction already occurs at d=2.
- All costs are finite and nonnegative.
- The construction is acyclic and needs only three parallel source-target realizations.
- Zero weights are allowed; the equality still holds.
- Positive weights only do not repair completeness.
- Positive rescaling of either resource preserves the existence of a corresponding collision.
- Adding dominated attainable vectors changes neither budget frontier nor h.
- Relabeling paths/actions leaves the result invariant.

## Prior-art collision classification

Multiobjective path literature explicitly distinguishes supported efficient paths, obtainable by weighted shortest-path scalarization, from unsupported efficient paths that cannot be obtained that way. Hence the optimization mechanism is **IMPORTED/KNOWN**.

## Status ledger

| Claim | Status |
|---|---|
| Full nonnegative linear scalarization profile can be identical while exact budget feasibility differs | **PROVED** |
| Linear weighted-sum family is a complete GC-II vector convertibility criterion | **FALSIFIED** |
| Unsupported nondominated solutions exist in multiobjective path problems | **IMPORTED/KNOWN** |
| Pareto antichain is complete for all componentwise budgets | **PROVED (Audit 351)** |
| Polynomial-size exact nonlinear complete certificate for arbitrary vector systems | **OPEN** |
| GC-specific assumptions forcing every minimal requirement to be supported | **OPEN** |

## Reproduction

Run `python scripts/gc2_audit353_linear_scalarization_collision.py`. The script verifies the symbolic case split, a dense exact integer-weight grid, Pareto minimality, and the separating budget query, and writes the machine-readable result in `results/gc2_audit353_linear_scalarization_collision.json` when requested by the repository workflow.
