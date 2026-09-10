# GC-II Audit 055 — Typed Pareto Dual Incompleteness

Status date: 2026-09-10
Branch: `gc2-capability-accounting-lab`
Parent audit: 054

## Question

Can the typed augmentation frontier be characterized completely by linear physically-normalized dual certificates

    m_lambda(q) = inf_{a in A_G(q)} <lambda,a>

without first computing the feasible augmentation set A_G(q)?

## Typed domain

Let augmentation vectors lie in R_+^d, with coordinates representing separately normalized resource/information/interface/rule expenditures after units have been fixed. The order is componentwise. A point a is Pareto-minimal when no distinct feasible a' <= a exists. No addition of physically incompatible coordinates is assumed until a dual covector lambda with reciprocal units is explicitly supplied.

## Exact finite counterexample

Consider the finite feasible augmentation set

    A = {(0,2), (1,3/2), (2,0)}.

All three points are Pareto-minimal: none componentwise dominates another.

For every nonnegative linear dual lambda=(lambda_1,lambda_2), the middle point b=(1,3/2) is never a strict minimizer of <lambda,a>.

Proof. For b to beat a=(0,2),

    lambda_1 + (3/2)lambda_2 <= 2 lambda_2,

hence lambda_1 <= (1/2)lambda_2.

For b to beat c=(2,0),

    lambda_1 + (3/2)lambda_2 <= 2 lambda_1,

hence (3/2)lambda_2 <= lambda_1.

Together these require (3/2)lambda_2 <= lambda_1 <= (1/2)lambda_2, impossible for lambda_2>0. For lambda_2=0, comparison with a gives lambda_1<=0, so only the zero covector ties everything. Thus b is an unsupported Pareto point invisible to every nontrivial nonnegative weighted-sum certificate.

Status: PROVED.

## Consequence

The Audit-054 candidate equivalence

    a in A_G(q) iff <lambda,a> >= m_lambda(q) for all lambda in Lambda_G

cannot be expected to recover an arbitrary discrete/nonconvex typed capability frontier when Lambda_G consists only of ordinary linear scalarizations. Linear support data determines the relevant convex lower image/support envelope, not arbitrary unsupported Pareto structure.

Therefore a universal GC-II complete-monotone theorem based only on nonnegative weighted sums is FALSIFIED.

## Why this is not a GC breakthrough

This obstruction is classical multiobjective optimization: weighted sums recover supported nondominated points and can miss unsupported nondominated points on nonconvex/discrete fronts. Weighted Tchebycheff or epsilon-constraint constructions can recover broader Pareto sets, but that moves the mechanism into established vector/multiobjective optimization rather than producing a uniquely generative calculus invariant.

Status: IMPORTED/KNOWN mechanism.

## Edge checks

- d=1: no unsupported tradeoff phenomenon; scalar ordering suffices.
- Convex closed upper image: separation/support-function duality can recover the convex frontier under standard assumptions; this audit does not contradict convex duality.
- Discrete/nonconvex feasible sets: unsupported Pareto points can occur, as the exact three-point witness shows.
- Zero dual lambda=0 carries no separating information.
- Rescaling a coordinate changes numerical lambda reciprocally; dimensional consistency therefore requires a declared normalization/dual-unit convention.
- A nonlinear or epsilon-constraint certificate can detect the middle point, so the theorem is specifically a no-go for linear-support completeness, not for every possible oracle/certificate family.
- Enumerating one indicator monotone per feasible/down-set state is tautologically complete but scientifically circular, as already identified in earlier complete-monotone audits.

## Stronger structural lesson

There is a trilemma for the desired GC-II convertibility criterion:

1. linear dual certificates are independently meaningful and computationally attractive but incomplete on general nonconvex/discrete frontiers;
2. sufficiently rich nonlinear scalarizations can become complete but collide with established multiobjective/vector optimization;
3. arbitrary indicator/separation families are complete but merely encode the feasible set/closure and are tautological.

A publishable GC-II theorem therefore needs a restricted operational class whose primitive structure forces a nontrivial geometry and yields a small independently computable certificate family that is neither generic convex duality nor an encoding of closure.

## Next target

Search for a GC-specific restricted class in which typed augmentation feasibility has additional algebraic structure induced jointly by task, scale, error and budget composition. Candidate requirements:

- certificate computed from primitive transformations, not from precomputed closure;
- exact for the restricted class;
- preserves physical units via typed duals;
- handles composition without assuming additive R/I/A/L conversion;
- produces a lower bound or forbidden pattern absent when any essential task-scale-error-budget coupling is ablated;
- collision-test against polymatroids/submodularity, matroids, network coding, CSP/database width, Blackwell/resource convertibility, conic/vector optimization and contextual marginal problems.

A promising kill-first candidate is whether compositional GC frontiers obey any exchange/submodular inequality. If yes, test whether it is merely polymatroid/matroid structure; if no, record a minimal counterexample and do not force the claim.

## Final classification

- Typed Pareto frontier as representation of incomparable augmentation costs: VALID.
- Exact three-point unsupported witness: PROVED.
- Completeness of nonnegative linear dual scalarizations for arbitrary GC frontiers: FALSIFIED.
- Convex-frontier duality: IMPORTED/KNOWN.
- Nonlinear/Tchebycheff/epsilon-constraint recovery: IMPORTED/KNOWN multiobjective optimization.
- Small independently computable GC-specific complete certificate family: OPEN.
