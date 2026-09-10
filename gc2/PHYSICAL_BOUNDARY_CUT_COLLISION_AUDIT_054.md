# GC-II Audit 054 — Physical Boundary-Cut Invariant Collision

Status date: 2026-09-10
Branch: `gc2-capability-accounting-lab`
Parent audit: 053

## Target

Audit 053 forced any defensible structural/execution novelty measure to be anchored to a conserved physical substrate rather than an arbitrary universal description language. The next candidate is therefore a boundary-crossing invariant: minimum physically charged capacity that must cross a conserved substrate boundary to realize a target capability.

## Restricted model

Let G=(V,E) be a finite directed operational network with source substrate s and target-capability node t. Each edge e carries a nonnegative scalar capacity c_e in one fixed physical unit. A feasible realization is a conserved s-t flow f satisfying 0<=f_e<=c_e and ordinary flow conservation at nonterminal nodes. Define

    Phi_G(s,t) = max feasible s-t flow,
    Kappa_G(s,t) = min_{s-t cuts C} sum_{e in C} c_e.

Then

    Phi_G(s,t) = Kappa_G(s,t).

This is exactly max-flow/min-cut, so in this scalar conserved-flow specialization the desired operational/geometric/computational equivalence already exists in classical network optimization.

Status: PROVED by reduction; IMPORTED/KNOWN mechanism.

## Closure-Escape interpretation

For a demanded capability rate d>=0:

1. operational criterion: there exists a feasible realization flow of value at least d;
2. geometric/separation criterion: every s-t cut has capacity at least d;
3. computational criterion: a max-flow algorithm returns value at least d.

These are equivalent in the restricted model. Thus a cut certificate is a genuine dual certificate of capability feasibility, but it is not a new GC-II theorem mechanism.

## No-Free-Capability interpretation

If some conserved boundary cut has total capacity < d, no admissible internal rearrangement can realize rate d without increasing capacity across at least one bottleneck cut or changing the declared operational model. This is a rigorous no-free-capability statement in the scalar conserved-flow class.

Again, it is max-flow/min-cut in GC language and must be classified IMPORTED/KNOWN rather than novel.

## Typed R/I/A/L obstruction

The GC-II target uses typed augmentation components (Delta R,Delta I,Delta A,Delta L). In general these are not commensurate. Therefore the expression

    sum_e c_e

is dimensionally invalid if an edge's capacity mixes incomparable resource, information, action/interface, and rule units without declared conversion laws.

A scalar physical cut theorem is consequently valid only after either:

- selecting one conserved physical unit;
- declaring conversion/exchange laws that map typed quantities into that unit; or
- replacing scalar cut capacity by a Pareto/vector object.

Status: dimensional restriction PROVED directly from typing assumptions.

## Why a vector/Pareto cut is not automatically a breakthrough

Moving from one commodity/unit to several typed components destroys the automatic scalar max-flow=min-cut equality. Multi-commodity and vector-resource flow models are established neighboring theories, and cut conditions can be necessary without being sufficient. Therefore merely defining a Pareto cut frontier does not establish a new GC-II duality theorem.

Likewise, complete finite monotone families cannot be assumed universally: unrestricted resource theories can require infinite separating families. GC-II must prove completeness only for a declared structured class.

## Exact collision result

Candidate claim:

    "A physically anchored minimum boundary-crossing rank/cut is the missing intrinsic Omega_G."

is FALSIFIED as a standalone breakthrough claim.

Reason: in its strongest exact scalar form it reduces to max-flow/min-cut; in typed/multicommodity form the exact duality is no longer automatic and enters established multicommodity/network-coding/resource-allocation territory.

## Surviving opportunity: endogenous conversion-coupled cut

The remaining potentially nontrivial object must include typed conversion laws as part of the conserved substrate. Let each local transformation e have a feasible conversion relation

    C_e subseteq R_+^4 x R_+^4

between incoming and outgoing typed capability carriers (R,I,A,L), rather than a scalar edge capacity. A global realization is a network-consistent assignment satisfying every local conversion relation and target obligation.

A candidate GC dual would need a separating functional lambda over typed carriers such that:

    primal capability feasible

iff

    every admissible lambda-boundary certificate dominates the target.

This resembles convex conic duality/resource conversion and is therefore OPEN, not novel. To become a GC-II breakthrough it must satisfy all of the following simultaneously:

1. lambda has physical dimensions or is explicitly normalized;
2. the dual certificate is complete for a meaningful nontrivial class;
3. the theorem permits nonlinear R/I/A/L conversion/coupling rather than assuming additivity;
4. the certificate is invariant under cost-preserving physical refinements/compilers;
5. the theorem specializes correctly to scalar max-flow/min-cut and the previously proved linear-rank frontier;
6. it supplies a genuine Closure-Escape and No-Free-Capability certificate;
7. a parametric finite family exhibits a separation not already equivalent to standard LP/conic duality, multicommodity flow, network coding, polymatroid bounds, Blackwell/resource convertibility, or simulation deficiency.

## Candidate mathematical form

For a fixed physically anchored finite substrate define a typed feasible augmentation set A_G(q) subseteq R_+^4 for obligation q. Its Pareto lower boundary is

    Omega_G(q) = Min_Pareto A_G(q).

For any nonnegative dimensionally normalized dual weight lambda in an admissible dual cone Lambda_G, define

    m_lambda(q) = inf_{a in A_G(q)} <lambda,a>.

Weak separation is immediate:

    <lambda,a> >= m_lambda(q)

for every feasible augmentation a. What is OPEN is a non-tautological theorem giving an independently computable Lambda_G for a structured GC class such that all these inequalities are also sufficient for feasibility/convertibility without first computing A_G(q).

This is now the strongest surviving route to program items (3), (4), (5), and (6).

## Edge checks

- d=0: feasibility is trivial and minimum scalar cut need not carry positive capacity.
- disconnected s,t: max flow and minimum cut value are both 0.
- infinite capacities: excluded in this finite real-valued audit unless treated as limits.
- negative capacities: inadmissible; would destroy ordinary flow semantics.
- typed quantities: cannot be added without conversion/normalization.
- nonlinear conversion: ordinary max-flow proof does not apply automatically.
- replenishment/catalysis: must appear explicitly in local conversion relations/state; otherwise the accounting silently imports capability.
- evaluator drift: target obligation is conserved throughout the comparison.

## Prior-art collision classification

- scalar flow/cut duality: IMPORTED/KNOWN;
- LP/conic separation: immediate collision for convex formulations;
- multicommodity/vector flow: major collision for typed carriers;
- network coding/polymatroid bounds: major collision when information is a carrier;
- resource-theory monotones: major collision for convertibility certificates;
- Blackwell/Le Cam: collision when the carrier is statistical information/experiment quality;
- simulation preorder: collision for behavioral conversion;
- contextuality/marginal/CSP/database width: must be checked if local consistency is proposed as sufficient for global realization.

## Final classification

- Physically anchored scalar boundary cut: VALID and PROVED, but IMPORTED/KNOWN.
- Scalar cut as intrinsic GC-II breakthrough: FALSIFIED.
- Typed Pareto boundary accounting: VALID candidate definition, OPEN.
- Universal exact vector max-flow/min-cut analogue: NOT CLAIMED.
- Independently computable complete dual certificate for nonlinear typed GC conversion: OPEN and now the priority target.
