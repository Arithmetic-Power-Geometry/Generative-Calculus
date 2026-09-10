# GC-II Audit 046 — Demand-Weighted Frontier Collision

Status date: 2026-09-10
Branch: `gc2-capability-accounting-lab`
Parent audit: 045

## Question

Does replacing raw convertibility-set expansion by a conserved-demand-weighted capability frontier produce a nontrivial GC-II novelty gap, Closure-Escape theorem, or No-Free-Capability law?

## Setup

Let Q be a fixed reference-obligation space with probability measure mu. Let P_A(b) be the policies realizable under admissible transformation class A and typed budget b=(b_R,b_I,b_A,b_L). For each q in Q let ell_q(p) be a declared loss. Define the demand-weighted risk

J_mu(p) = integral_Q ell_q(p) d mu(q)

and the optimal risk

V_A(mu,b) = inf_{p in P_A(b)} J_mu(p).

For an extension A subseteq A', define the scalar frontier improvement

Delta_mu(A,A';b) = V_A(mu,b) - V_A'(mu,b).

For multiple conserved loss coordinates ell^(1),...,ell^(m), define instead the Pareto set of achievable expected-loss vectors under P_A(b).

All losses are required to have declared codomains/units. Heterogeneous physical units are not added unless an explicit utility/scalarization is supplied.

## Exact reduction

For fixed Q, mu, losses, policy class and typed budget, V_A(mu,b) is exactly the value function of a constrained statistical/operational decision problem: choose an admissible policy p to minimize expected loss subject to resource constraints. Enlarging A to A' merely enlarges the feasible decision set from P_A(b) to P_A'(b).

Therefore Delta_mu is exactly the reduction in the optimal expected loss caused by enlarging the feasible policy/action/information class. No additional GC-specific mathematical structure appears in this scalar quantity.

If the extension supplies information rather than actions, the same construction is a value-of-information/Bayes-risk reduction. If it supplies controls/actions, it is a constrained value-function improvement. If multiple losses are retained without scalarization, the object is the ordinary shift of a multiobjective/Pareto feasible frontier.

Status: **PROVED exact reduction under the stated fixed-demand assumptions; IMPORTED/KNOWN mechanism; standalone novelty FALSIFIED**.

## Monotonicity and edge cases

Assume A subseteq A' and extension does not delete old policies or tighten b. Then P_A(b) subseteq P_A'(b), hence

V_A'(mu,b) <= V_A(mu,b)

and Delta_mu >= 0 whenever the infima exist in the extended real line.

Degenerate cases:

- mu supported only on obligations for which old and new optima coincide: Delta_mu=0 despite latent new capability elsewhere.
- zero loss: Delta_mu=0 for every extension.
- empty old feasible set: V_A may be +infinity, so a finite arithmetic gap is undefined/infinite; this must not be reported as a finite novelty magnitude.
- negative or utility-valued objectives: sign conventions must be fixed before interpreting improvement.
- heterogeneous losses: no canonical scalar Delta exists without a declared utility/scalarization; Pareto comparison is the invariant alternative.
- nonattained infimum: use inf rather than min; monotonicity still holds.
- endogenous mu or evaluator drift: excluded here because Audit 038 already showed that changing the judging standard can manufacture apparent capability.

Status: **PROVED checks**.

## Composition behavior

Delta_mu is not generally additive under sequential extensions. For A0 subseteq A1 subseteq A2,

V_A0 - V_A2 = (V_A0 - V_A1) + (V_A1 - V_A2)

is an algebraic telescoping identity only when all three values use the same mu, loss, budget semantics and horizon. It does not imply that the physical causes or typed resource contributions are additive. Synergy and redundancy can make marginal improvements depend strongly on extension order.

Therefore no bound of the form

Delta_mu <= F(Delta R,Delta I,Delta A,Delta L)

follows from demand weighting alone. To obtain such a bound one must impose structural regularity linking resource increments to the feasible-policy map and the loss geometry (for example Lipschitz/sensitivity, information constraints, channel restrictions, control authority, or a declared simulation model). Without such assumptions, a fixed-size rule or information increment can have arbitrarily large value after rescaling the loss, and bounded loss merely gives the trivial range bound.

Status: **PROVED obstruction to an assumption-free quantitative accounting law**.

## Collision boundary

Classical Bayesian decision theory defines optimal decisions by minimizing expected loss and Bayes risk. Value-of-information analysis measures the decrease in optimized expected loss after acquiring information. Constrained optimization and optimal control likewise measure changes in optimal value under enlarged action/control sets or relaxed constraints. Multiobjective optimization represents nonscalarized tradeoffs by Pareto fronts.

Accordingly, merely renaming an expected-loss/Pareto frontier improvement as Generative Novelty Gap does not establish novelty.

Status: **IMPORTED/KNOWN collision; novelty claim rejected**.

## Decisive result

For fixed conserved demands, evaluator, losses, horizon and budget semantics, a demand-weighted capability-frontier shift is exactly an optimized-loss/value-function shift over an enlarged feasible policy class. It is therefore not, by itself, a GC-II breakthrough object.

In particular, demand weighting repairs Audit 045's cardinality pathology but does not escape decision theory, value of information/control, or constrained multiobjective optimization.

Status: **FALSIFIED as standalone Omega_G / Closure-Escape / No-Free-Capability route**.

## What survives

The next candidate must not be merely another scalar value improvement. A sharper unresolved object is a **resource-to-capability response law** for a *family* of conserved obligations, budgets and horizons:

V_S(mu,b,h),

viewed as a full response surface rather than one optimized value. The scientific question is whether there exists a representation-invariant obstruction relating changes of this whole surface to typed R,I,A,L interventions after quotienting away ordinary decision-theoretic, simulation, information and control reductions.

A severe next kill test is to compare the complete response surface against (i) value functions and convex/concave conjugates, (ii) Blackwell/Le Cam experiment comparison over all decision problems, (iii) complete resource-theoretic monotone families, and (iv) constrained-control viability/value functions. If the full surface is already complete data for one of those established comparison theories, it is not GC-specific.

Status: **OPEN**.
