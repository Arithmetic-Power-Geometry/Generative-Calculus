# GC-II Audit 047 — Complete Response-Surface Collision

Status date: 2026-09-10
Branch: `gc2-capability-accounting-lab`
Parent audit: 046

## Question

Does replacing a scalar demand-weighted improvement by the complete resource-to-capability response surface

V_S(mu,b,h)

over conserved decision problems/demands mu, typed budgets b=(b_R,b_I,b_A,b_L), and horizons h produce a GC-specific complete invariant or breakthrough object?

## Setup

Fix a system S with conserved evaluator/evidence semantics. For every admissible decision problem d=(Q,mu,ell), typed budget b and horizon h, define

V_S(d,b,h) = inf_{p in P_S(b,h)} E_mu[ell_q(p)].

No heterogeneous physical resource coordinates are added. The response object is the indexed family

R(S) = { V_S(d,b,h) : d in D, b in B, h in H }.

The family is representation-invariant only after D, budget semantics, horizon semantics, and admissible policy semantics are fixed extensionally.

## Exact collision on information-only submodels

Restrict S to a statistical experiment: the intervention changes only the observation/information channel, while state space, action semantics and losses are conserved. If D contains all relevant decision problems, comparison of V_S over all d is exactly the classical comparison-of-experiments architecture: one experiment is more informative precisely when it yields no worse optimized decision value for the complete decision class, under the standard hypotheses of the comparison theorem.

Thus the complete decision-response surface is not new in this submodel. It is a re-indexed complete operational comparison family.

Status: **PROVED reduction for the stated statistical-experiment submodel; IMPORTED/KNOWN collision**.

## Resource-theoretic collision

For a fixed admissible transformation class, a complete family of monotones characterizes the conversion preorder. The response family over all tests/decision functionals can itself act as such a complete separating family when the test class is rich enough. There is no general reason to expect a finite complete family: known resource theories can require infinite or discontinuous families, while particular convex dynamical resource theories admit complete families and computational formulations.

Therefore merely elevating GC-II from one scalar monotone to the entire family of optimized test values does not establish a new mathematical mechanism.

Status: **IMPORTED/KNOWN structural collision**.

## Control/viability collision

When S is a controlled dynamical system and d encodes target/safety loss, V_S(d,b,h) is an ordinary constrained finite-horizon value function. Reachability and viability sets can be represented as level/sublevel sets of suitable value functions under established hypotheses. Hence retaining all budgets and horizons does not by itself escape optimal-control/reachability theory.

Status: **IMPORTED/KNOWN collision on controlled-dynamics submodels**.

## Decisive null theorem

Let two systems S and T have identical complete response families under the same conserved index semantics:

V_S(d,b,h) = V_T(d,b,h) for all d,b,h.

Then any purported GC novelty functional Omega that factors only through this response family,

Omega(S,T) = f(R(S),R(T)),

and obeys identity of indiscernibles on its arguments must satisfy

Omega(S,T)=0.

This is mathematically immediate but scientifically decisive: no GC-II breakthrough can be extracted solely by nonlinear post-processing, differentiation, integration, geometry, or scalarization of a complete response surface that is already operationally identical.

Status: **PROVED null result; methodological filter, not a novelty claim**.

## Edge and domain checks

- Empty feasible sets may give +infinity; equality and order are then interpreted in the extended reals.
- Loss rescaling changes numerical values but not the underlying comparison if the complete decision class is transformed consistently; arbitrary rescaling prevents universal magnitude claims.
- Increasing a componentwise budget weakly enlarges the feasible policy set only if the resource semantics are monotone; under that assumption V is nonincreasing in each budget coordinate for loss minimization.
- Increasing horizon is not intrinsically monotone: extra time may help when policies may stop/idle, but can hurt under mandatory exposure, deadlines, accumulating risk or horizon-dependent evaluators. No horizon monotonicity is assumed without an embedding rule.
- Composition is not additive. Product/parallel systems can exhibit synergy, redundancy and shared-resource coupling.
- A finite sampled grid of d,b,h is not a complete response surface and cannot support a completeness claim.
- Equality of response surfaces is meaningful only with conserved evaluator, evidence, interface and resource semantics; otherwise evaluator drift or unit changes can manufacture equality/difference.

Status: **PROVED checks/qualifications**.

## Consequence for Omega_G

The candidate

Omega_G = distance(R(S),R(T))

is not GC-specific without additional structure. On information-only submodels it reduces to comparison of experiments/deficiency-style operational comparison; on controlled submodels it reduces to families of value/reachability functions; under fixed free transformations it is a complete-monotone-style construction.

Therefore the full response-surface route is **FALSIFIED as a standalone Paper-II breakthrough mechanism**.

## What survives: intervention-relative mixed response

The remaining gap is not another summary of outcomes. GC-II must account for the *joint intervention mechanism* that changes the attainable response family. Define an intervention delta=(delta_R,delta_I,delta_A,delta_L) as a typed change in resource supply, information channel, action/interface authority and admissible-rule structure, and define the mixed finite difference

M_S(delta1,delta2;d,b,h)
 = V_{S+delta1+delta2}(d,b,h)
   - V_{S+delta1}(d,b,h)
   - V_{S+delta2}(d,b,h)
   + V_S(d,b,h).

This quantity detects interaction/synergy or antagonism between interventions, but **no novelty is claimed**: mixed differences/Hessians, supermodularity/submodularity, complementarity, interaction information and control coupling are obvious collision classes.

The next severe test is narrower: search for a representation-invariant *interaction obstruction* that (a) vanishes under independent product composition, (b) is invariant under cost/semantics-preserving compilation, (c) cannot be generated by evaluator drift, (d) admits an exact finite-world witness and lower bound, and (e) survives reductions to ordinary supermodularity, interaction information, communication complexity, circuit/gate synergy, resource-theory catalysis/activation and constrained-control coupling.

Status: **OPEN**.

## Prior-art boundary used in this audit

Relevant established boundaries checked in this run include Blackwell-style comparison of experiments over all decision problems, general-state-space extensions of Blackwell comparison, complete resource monotone families (including results showing finite completeness can fail), and value-function/reachability characterizations in constrained control. These collisions are treated as novelty exclusions, not as GC results.

## Final classification

- Complete response family R(S): **VALID / representation-sensitive unless semantics fixed**.
- Information-only restriction: **IMPORTED/KNOWN comparison-of-experiments mechanism**.
- Fixed-free-operation restriction: **IMPORTED/KNOWN complete-monotone mechanism**.
- Controlled-dynamics restriction: **IMPORTED/KNOWN value/reachability mechanism**.
- Complete response surface as standalone Omega_G breakthrough: **FALSIFIED**.
- Interaction obstruction beyond standard complementarity/catalysis/coupling: **OPEN**.
