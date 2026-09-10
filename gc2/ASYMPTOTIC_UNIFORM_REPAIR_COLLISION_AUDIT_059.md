# GC-II Audit 059 — Asymptotic Uniform Repair Collision

Status date: 2026-09-11
Branch: `gc2-capability-accounting-lab`
Parent audit: 058

## Question

Can the surviving idea from Audit 058 — a uniform law for repair cost under repeated composition, task scale, error tolerance, and budget — serve as a standalone GC-II breakthrough mechanism?

## Setup

For an operational obligation q and n-fold composition q^{\otimes n}, let C_n(q,epsilon) be a physically typed repair frontier: the Pareto-minimal augmentations a=(Delta R,Delta I,Delta A,Delta L) that make the n-copy obligation achievable at error at most epsilon. Typed coordinates are not summed unless a physical conversion law is explicitly supplied.

A scalarized regularized rate may be defined only after choosing a dimensionally valid nonnegative physical price functional lambda:

    rho_lambda(q,epsilon) = liminf_{n->infinity} (1/n) inf_{a in C_n(q,epsilon)} <lambda,a>.

This is a valid asymptotic quantity, but validity is not novelty.

## Collision theorem

Assume a class of GC objects is closed under a parallel composition operation tensor and an alternative/direct-sum operation plus, and assume a preorder <= represents admissible simulation/convertibility. If a proposed uniform repair law is characterized solely by real-valued maps phi that are monotone under <=, additive under plus, multiplicative (or log-additive) under tensor, and normalized on a declared unit, then the architecture is an instance of an asymptotic-spectrum/resource-regularization construction rather than a new GC-specific mechanism.

Proof: the stated axioms are precisely the algebraic data of an ordered commutative semiring (or its logarithmic/additive variant) together with monotone semiring homomorphisms. Repeated composition induces regularized/asymptotic rates. Any theorem deriving convertibility from all such phi therefore specializes to the established asymptotic-spectrum template. Removing multiplicativity does not rescue novelty: regularized monotones and asymptotic conversion rates are standard in resource theories. QED at the level of reduction architecture.

Status: PROVED reduction under the stated semiring/regularization assumptions; mechanism IMPORTED/KNOWN.

## Important non-collapse

This does NOT prove that every GC task-scale-error-budget law is reducible to an asymptotic spectrum. The reduction requires composition operations satisfying the declared algebraic laws and a preorder compatible with them. History-dependent interfaces, shared catalysts, nonseparable budgets, endogenous changes of the admissible transformation set, or nonassociative/context-dependent composition can violate those assumptions. Such violations, however, are not automatically novel; each must be physically motivated and collision-tested separately.

## Direct-sum/direct-product warning

A universal claim C_n = n C_1 is false without model-specific assumptions. Direct-sum and direct-product behavior is highly model dependent: strong theorems exist in some query/communication settings, while direct sum can fail in other communication models. Therefore GC-II must not assume linear scaling as a general law.

Status: unrestricted linear-scaling claim FALSIFIED as a universal GC principle.

## Dimensional and edge checks

- n=1 recovers the one-instance repair problem.
- A free q gives zero regularized rate only when zero augmentation is feasible for every n under the same conserved substrate.
- liminf is used because a limit need not exist without sub/superadditivity.
- Fekete-style limit claims require an explicitly proved subadditive scalarized sequence.
- lambda may combine typed coordinates only when its coefficients carry reciprocal physical units or are declared exchange prices; otherwise <lambda,a> is dimensionally meaningless.
- Catalysts/shared side information can make per-copy costs sublinear and must be included in the substrate state.
- Superactivation can make a joint object feasible although components are individually infeasible; this does not violate accounting if composition itself exposes an admissible joint transformation.
- Correlated error criteria differ from per-copy error and cannot be silently substituted.

## Consequence for Omega_G

Neither regularization nor failure of naive additivity is sufficient for Omega_G>0. A candidate novelty gap based only on asymptotic per-copy repair, direct-sum violation, or spectral monotones collides with established complexity/resource/asymptotic-spectrum machinery.

Status: asymptotic uniform repair as standalone breakthrough route FALSIFIED.

## Surviving target

The next candidate must use a GC-specific conserved coupling that is absent from ordinary ordered-semiring regularization. A precise kill-first target is a **composition-defect tensor/frontier** measuring the irreducible difference between (i) independently composed task-scale-error-budget closures and (ii) the closure of the physically coupled composite, while charging every shared interface, catalyst, information source and rule installation.

The candidate must satisfy:

1. zero defect for genuinely independent Cartesian/tensor composition;
2. invariance under cost-preserving physical equivalence;
3. monotonicity under declared free simulations;
4. explicit nonzero finite examples obtained without changing evaluator semantics;
5. a lower bound not reducible to mutual information/total correlation, communication complexity, interaction information, synergy/PID, contextuality, network coding, catalytic resource theory, or generic nonadditivity;
6. a composition theorem across scale/error/budget rather than a renamed instance optimizer.

Until such a family survives those collisions, it remains OPEN and must not be called a breakthrough.

## Final classification

- Typed asymptotic repair frontier: VALID definition.
- Scalar regularized rate after dimensional pricing: VALID definition.
- Semiring spectral characterization: IMPORTED/KNOWN architecture.
- Universal linear direct-sum law: FALSIFIED without extra assumptions.
- Asymptotic uniform repair as standalone GC novelty: FALSIFIED.
- GC-specific composition-defect invariant: OPEN, next target.
