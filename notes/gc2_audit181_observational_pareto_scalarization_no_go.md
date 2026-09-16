# GC-II Audit 181 — Observational Pareto normalization and scalarization boundary

Status: **PROVED boundary result; naive observational gauge novelty FALSIFIED.**

## Target after Audit 180
Audit 180 required intrinsic scales to be defined on externally observable closure behavior, not on primitive implementation granularity. This audit tests the strongest natural construction: use the complete set of externally achievable multi-resource costs for a task.

## Observable closure cost set
Fix an external task tau and d nonnegative accounting coordinates (e.g. resource, information, action/interface, rule-change burden after units are declared). Let

C_tau = { c(p) in R_+^d : p externally realizes tau }.

Let U_tau = cl(C_tau + R_+^d) be the closed upper image. Internal state splitting, insertion of silent zero-cost states, and cost-preserving subdivision leave C_tau and U_tau unchanged provided external traces and accumulated cost vectors are preserved.

Thus U_tau passes the representation-refinement gate that killed atomic scales in Audit 180.

## Proposition 1 (representation invariance)
If two operational presentations are externally cost-trace equivalent for tau, then they have identical U_tau.

Proof: equivalence gives the same achievable external cost vectors; adding the same nonnegative orthant and taking closure preserves equality. QED.

## Scalar support family
For every nonnegative weight vector w in R_+^d define

m_tau(w) = inf_{c in U_tau} <w,c>.

This is unit-covariant: under diagonal coordinate rescaling c' = D c, the same physical scalar evaluation is represented by w' = D^{-T}w, giving <w',c'>=<w,c>.

If U_tau is closed and convex, the family {m_tau(w): w>=0} determines its supported lower boundary (equivalently its convex upper image). Therefore any proposed scalar observational gauge depending only on linear weighted minimum costs factors through this support data and cannot contain more information than the convex Pareto geometry.

## Theorem (linear-scalarization no-go)
Let Phi(U_tau) be any invariant computed solely from the collection of weighted minima m_tau(w) over w>=0. If two tasks have identical m_tau(w) for all w>=0, then Phi is identical. In particular Phi cannot distinguish nonconvex achievable-set structure erased by convexification.

Proof: immediate functional factorization through the map U -> (w -> m_U(w)). QED.

## Exact collision
Take two achievable cost sets in R_+^2:

A = {(0,2),(2,0)}
B = {(0,2),(1,1),(2,0)}.

For every w=(w1,w2)>=0,

min_{a in A}<w,a> = min(2w1,2w2).

For B the extra point gives w1+w2, but w1+w2 >= 2 min(w1,w2), so

min_{b in B}<w,b> = min(2w1,2w2)

as well. Hence all nonnegative linear scalarizations collide although B contains an additional attainable balanced realization (1,1). The full nonconvex observable sets differ.

This is decisive against claiming a family of weighted closure minima, a support function, or a Minkowski/support gauge as an independently new GC-II invariant.

## Consequence for Omega_G
A candidate Omega_G based only on normalized weighted minimum costs is at most a scalarization of the observable Pareto/upper-image geometry. It is useful operationally but belongs to established multiobjective optimization / convex support machinery.

A potentially stronger object is the nonconvex observational closure spectrum itself, including unsupported Pareto points and composition law. But merely retaining the full Pareto set is also standard multiobjective optimization; novelty would require a theorem about how closure composition creates/destroys attainable capability that is not reducible to Minkowski sums, dynamic programming, or resource-theory convertibility.

## Composition check
For independent sequential stages whose cost vectors add and whose feasible witnesses concatenate without cross-stage constraints, achievable sets satisfy

C_{tau1;tau2} subseteq C_tau1 + C_tau2,

with equality only when every independently feasible pair of witnesses is composable. Strict inclusion is therefore a candidate location for genuine closure interaction: interface/rule compatibility can forbid cost-vector combinations that ordinary independent Minkowski accounting predicts.

Define the compatibility defect set

Delta_C(tau1,tau2) = (C_tau1 + C_tau2) \ C_{tau1;tau2}.

This is representation-invariant under external cost-trace equivalence. However its novelty is **OPEN**: it may reduce to constrained path composition, relational composition, CSP compatibility, or resource-theory restrictions.

## Edge and degeneration checks
- Empty C_tau (unreachable task): U_tau empty; weighted infimum is +infinity by convention.
- Zero-cost realization: origin belongs to U_tau and all nonnegative weighted minima are zero, so scalarization loses all higher-cost alternatives.
- Zero weight coordinates: intentionally ignore those coordinates and increase collision risk.
- Nonconvex C_tau: weighted minima expose only supported geometry; exact collision above proves information loss.
- Convex closed upper images: support/separation machinery can be complete for the convex geometry; this is imported convex analysis, not GC novelty.
- Unit changes: handled contragrediently by weights.
- Cost-preserving primitive refinement: leaves C_tau unchanged.
- Composition: Minkowski addition is valid only under independent composability; cross-interface restrictions can make inclusion strict.

## Prior-art collision ledger
- Multiobjective shortest paths explicitly compute Pareto-optimal path cost vectors: **IMPORTED/KNOWN**.
- Linear/norm scalarization of multiobjective problems: **IMPORTED/KNOWN**.
- Convex support/separation and gauges: **IMPORTED/KNOWN**.
- Complete monotone families for convertibility in resource theories: strong collision; finite complete families can fail in general resource theories.

## Ledger
- Observable achievable cost set U_tau as refinement-invariant object: **PROVED**.
- Weighted-minimum/support family as complete descriptor of convex upper image under standard closed-convex assumptions: **IMPORTED/KNOWN**.
- Weighted observational gauge as independent GC-II breakthrough: **FALSIFIED**.
- Linear scalarizations recovering arbitrary nonconvex attainable structure: **FALSIFIED by exact collision**.
- Full Pareto/attainable closure spectrum: **IMPORTED/KNOWN mechanism unless coupled to a new closure theorem**.
- Compatibility defect Delta_C under sequential composition: **OPEN candidate**, not claimed novel.

## Next gate
Attack Delta_C. Construct exact finite systems with identical marginal attainable cost sets C_tau1 and C_tau2 but different sequential attainable set C_{tau1;tau2}. Then determine the weakest additional interface/rule information required to predict the composition. Seek a lower bound on that missing compositional information and collision-check it against relational composition, database join dependencies, CSP width, automata products, communication complexity, and contextuality. A GC-II advance requires more than observing strict Minkowski failure; it needs a nontrivial invariant or theorem quantifying the information/capability lost by marginal closure summaries.