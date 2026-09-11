# GC-II Audit 063 — Conserved-Bottleneck Translator Collision

Status date: 2026-09-11
Branch: `gc2-capability-accounting-lab`
Parent audit: 062

## Candidate attacked

Audit 062 left a physically anchored translator target: local computation/recompilation is free, while quantities crossing an explicit boundary are charged in typed coordinates R,I,A,L. The hoped-for escape was a simultaneous cross-coordinate law that could not be obtained by applying ordinary communication/cut bounds coordinatewise.

## Formal finite model

Let a task q be implemented by a protocol P across a declared cut B. Associate the typed cost vector

    c_B(P) = (R_B(P), I_B(P), A_B(P), L_B(P))

with explicitly declared domains/units. Define the feasible cost set

    K_B(q,epsilon) = { c_B(P) : P admissibly realizes q with error <= epsilon }.

The physically meaningful object is the Pareto-minimal boundary-cost frontier

    Omega_B(q,epsilon) = Min_Pareto K_B(q,epsilon).

No sum R+I+A+L is permitted unless conversion coefficients/laws have independently been specified. A scalar lower bound may be formed only after choosing a dimensionally valid normalization or dual price vector.

## Collision theorem for explicit finite protocol classes

If the admissible protocol class is finite (or finitely encoded with decidable feasibility) and R,I,A,L are computable protocol costs, then Omega_B is exactly a multiobjective protocol-complexity frontier. Any proposed inequality

    Phi(R_B,I_B,A_B,L_B,n,epsilon) >= 0

is a resource tradeoff lower bound for that protocol model. The fact that the coordinates interact nonlinearly does not by itself create a new invariant: established communication/distributed-computation theory already proves non-coordinatewise tradeoffs, including communication-space, message-time, storage-computation-communication, and physical area-time/information-transfer bounds.

Therefore a theorem of the form 'a conserved boundary forces a nonlinear joint R,I,A,L tradeoff' is not sufficient for GC-II novelty. It must contain a structural ingredient not representable as an ordinary multi-resource protocol model.

Status: PROVED reduction for finite explicit protocol classes; collision IMPORTED/KNOWN.

## Concrete collision classes

1. Communication-space tradeoffs: established models prove product-type bounds such as C*S = Theta(f(n)) for specific problems. This already demonstrates that a nonlinear cross-coordinate law is not uniquely generative.
2. Message-time tradeoffs: synchronous distributed lower bounds can be transferred from communication complexity with explicit dependence on allowed rounds/time.
3. Storage-computation-communication tradeoffs: distributed computing has exact/tight frontiers in which storage and computation alter minimum communication.
4. Physical information-transfer tradeoffs: VLSI lower bounds derive area-time constraints from required information movement across physical regions.
5. Amortized/direct-sum communication: repeated tasks can have per-instance cost different from one-shot cost, so nonadditivity under scale is also established.

These collisions jointly kill the idea that simultaneous typed accounting, nonlinearity, or scale dependence alone is the missing GC-II theorem.

## Dimension/domain audit

- R,I,A,L remain typed; addition across coordinates is undefined absent an explicit conversion map.
- Zero-demand task: the frontier contains the zero vector when a null protocol is admissible.
- Infinite/free local computation: does not invalidate a boundary lower bound, but moves the model closer to communication complexity.
- Zero-capacity boundary: any task requiring cross-cut dependence is infeasible; this is a cut/reachability degeneracy, not novelty.
- Shared initial correlation/advice/catalyst: must be charged or declared free in the protocol model; otherwise apparent capability is hidden endowment.
- Error epsilon >= trivial-error threshold: lower bounds may collapse; epsilon must be part of the task domain.
- Parallel composition: frontier need not add; batching/coding/amortization can lower per-copy cost.
- Representation invariance: follows only when costs are attached to physical boundary events, not program descriptions.

## Classification

- Typed boundary Pareto frontier: VALID.
- Representation-robust physical boundary charging: VALID.
- Nonlinear joint resource tradeoff: VALID but not novel in general.
- Conserved-bottleneck translator theorem based only on multi-resource protocol costs: FALSIFIED as standalone GC-II breakthrough.
- Universal additive capability accounting: FALSIFIED/unsupported.
- A specifically generative structural law beyond protocol-resource tradeoffs: OPEN.

## Stronger surviving target — endogenous admissibility change

The previous audits repeatedly collapse because the admissible transformation/protocol set is fixed before optimization. GC-I/GC-II's potentially distinctive axis is instead that a system may spend typed resources to *change which transformations are admissible later* by acquiring/constructing an interface, action, rule, model, measurement, or evaluator.

Define a rule-indexed closure C_G(q; L) and an installation transition

    L --[delta R, delta I, delta A, delta L]--> L'.

The candidate generative gap is not merely the cost of executing q under fixed L', but the minimum typed cost of reaching an admissibility structure under which q enters closure:

    Omega_G(q | L0)
      = Min_Pareto { Delta : exists L' reachable from L0 at typed cost Delta and q in C_G(L') }.

Kill condition: if L' can simply be encoded as ordinary protocol state/action or as a purchased resource token, this reduces again to reachability/resource theory/MDP/CSP optimization and is not novel.

The next audit must therefore search for a nontrivial composition law for endogenous admissibility change: whether installing one capability changes the *conversion law itself* for later resources/tasks, while every installation and resulting rule change remains operationally observable and charged. This must be collision-tested against endogenous action-space MDPs, metareasoning, program synthesis, self-modifying systems, adaptive experiment design, resource theories with catalysts, and endogenous scientific inquiry.

No breakthrough is claimed in this audit.
