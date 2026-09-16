# GC-II Audit 189 — Joint-layer scalarization no-go

Status: PROVED for the no-go statement; IMPORTED/KNOWN mechanism for Pareto/MDL collisions; FALSIFIED as a universal scalar novelty law; OPEN for closure-coupled frontier laws.

## Question

After Audit 188, can semantic specification, acquisition evidence/interface, physical realization, and admissibility/rule change be combined into one intrinsic scalar cost whose value is a universal Generative Novelty Gap?

## Operational setup

For a capability-generating witness p define the nonnegative layer-cost vector

c(p) = (S(p), E(p), P(p), L(p)),

where S is semantic specification cost, E is evidence/acquisition cost relative to the admissible information interface, P is physical/resource realization cost, and L is admissibility/rule-change cost. Let G(p) denote the resulting closure gain (a set-valued or task-indexed gain, not assumed scalar).

The attainable accounting set for a target gain g is

C_g = { c(p) : G(p) >= g } subseteq R_+^4.

## Theorem 189.1 — independent-unit scalarization no-go

Suppose a proposed dimensionless scalar accounting law Q(c) is invariant under independent positive rescalings of the four layer units:

Q(alpha_S S, alpha_E E, alpha_P P, alpha_L L) = Q(S,E,P,L)

for every positive alpha_j and every strictly positive c. Then Q is constant on the positive orthant.

### Proof

For arbitrary strictly positive x,y choose alpha_j = y_j/x_j. Independent rescaling maps x to y. Invariance gives Q(y)=Q(x). Since x,y were arbitrary, Q is constant. QED.

This extends Audit 179 from a bound F to any scalar novelty/cost functional built directly from heterogeneous raw layer coordinates.

## Corollary 189.2 — weighted sums are conventions, not intrinsic laws

A weighted score

Q_w(c)=w_S S+w_E E+w_P P+w_L L

is meaningful only after fixing commensuration/normalization conventions. Changing a coordinate unit without contragrediently changing its weight changes the score. Therefore the weights are part of the operational specification, not universal constants supplied by GC-II.

## Exact finite collision

Consider two witnesses for the same closure gain g:

p: c(p)=(1,4,1,1)
q: c(q)=(4,1,1,1).

Neither dominates the other. With w=(1,0.1,1,1), p is preferred; with w=(0.1,1,1,1), q is preferred. Thus the operational system alone does not determine a unique scalar ordering unless a tradeoff policy is supplied.

More generally, any attainable set containing incomparable Pareto points has no canonical linear scalar ranking absent additional structure.

## Collision check

1. Multiobjective/Pareto optimization already treats heterogeneous objectives by attainable sets/frontiers and policy-dependent scalarizations. This mechanism is IMPORTED/KNOWN.
2. Two-part MDL and Kolmogorov structure functions already couple model-description and residual/data costs. Therefore a two-layer 'description + evidence' sum is not independently novel; unrestricted algorithmic versions inherit incomputability.
3. Query/decision-tree complexity covers evidence acquisition under fixed interfaces (Audit 185).
4. Dynamic data structures cover finite Markov interface update/query tradeoffs (Audit 186).
5. Resource theories cover monotone resource tradeoffs once free operations and resource coordinates are fixed.

## What survives

The representation-safe object is not a universal scalar but the closure-indexed attainable frontier

F_g = Min_Pareto C_g.

However F_g by itself is standard multiobjective geometry and is therefore not claimed as GC-II novelty.

The remaining GC-II target must exploit a relation between closure gain and movement of the attainable frontier. A candidate object is a closure-gain correspondence

K : g -> F_g,

or, for nested operational systems G subseteq G', a frontier displacement that is defined only after dimensionless operational gauges are justified. The breakthrough criterion is strict: prove a constraint on this correspondence that follows from generative closure/composition but is not a generic fact of Pareto optimization, MDL, resource monotones, query complexity, or dynamic data structures.

## Edge cases checked

- Zero coordinates: independent rescaling preserves zero/nonzero support; the constancy theorem applies separately on each support stratum.
- Shared physical dimensions: ratios may be legitimate and evade independent-rescaling assumptions; they require a physically justified common dimension.
- Already dimensionless coordinates: no-go does not prohibit dependence on them.
- Fixed exchange rates/weights: scalarization becomes valid but policy-relative, not intrinsic.
- Nonlinear scalarizations: the theorem applies equally if they are invariant under all independent coordinate rescalings.
- Composition: vector costs may compose additively, subadditively, or nonadditively; the no-go does not assume any of these.

## Ledger

- Universal raw heterogeneous scalar joint-layer novelty: FALSIFIED.
- Independent-unit scalarization no-go: PROVED.
- Policy-weighted scalarization: CONDITIONAL / IMPORTED-KNOWN.
- Pareto attainable frontier: IMPORTED/KNOWN.
- Two-part description+evidence novelty as a new principle: FALSIFIED by MDL/algorithmic-statistics collision.
- Closure-coupled frontier constraint beyond generic multiobjective theory: OPEN.

## Next attack

Search exact finite operational systems for a non-generic law relating nested closure gains to attainable-frontier displacement. In particular test whether closure composition imposes inequalities on frontier correspondences that fail for arbitrary set-valued multiobjective problems. Exhaustively enumerate small systems and actively search counterexamples before proposing a theorem.
