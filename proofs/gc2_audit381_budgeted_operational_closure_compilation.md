# GC-II Audit 381 — Budgeted operational closure compilation boundary

## Scope
Branch-only Paper-II audit. GC-I on `main` is frozen and unchanged.

## 1. Explicit operational model
A finite budgeted operational system is
\[
\mathcal O=(X,U,\delta,\rho,\iota,\alpha,\Lambda,B).
\]
Here:
- \(X\) is the operational state set;
- \(U\) is the set of admissible primitive transformations;
- \(\delta_u:X\rightharpoonup X\) is the partial state transition induced by primitive \(u\);
- \(\rho(u,x)\in\mathbb N^k\) is its nonnegative resource-consumption vector when admissible at \(x\);
- \(\iota(x)\) is the information exposed at state \(x\);
- \(\alpha(u,x)\) is the interface/action label exposed to the agent;
- \(\Lambda\) is the rule predicate deciding whether \(u\) is admissible from the current operational record;
- \(B\in\mathbb N^k\) is the componentwise resource budget.

An execution \(\pi=(u_1,\ldots,u_m)\) from \(x_0\) is legal when every partial transition exists and every rule test in \(\Lambda\) succeeds. Its accumulated resource is
\[
R(\pi)=\sum_{j=1}^m\rho(u_j,x_{j-1}).
\]
The budgeted operational closure is
\[
\operatorname{Cl}_{\mathcal O,B}(x_0)
=\{x_m:\exists\text{ legal }\pi:x_0\leadsto x_m,\ R(\pi)\le B\}.
\]

Information, interfaces/actions, and rules are therefore explicit parts of admissibility rather than being silently identified with numerical resources.

## 2. Theorem 381.1 — finite integer-budget closure compiles exactly to ordinary reachability
Assume that every variable needed by \(\Lambda\) has a finite operational memory state \(q\in Q\), and that its update under an admissible primitive is deterministic. Define the expanded state space
\[
\widehat X=X\times Q\times\prod_{j=1}^k\{0,1,\ldots,B_j\}.
\]
Write an expanded state as \((x,q,r)\), where \(r\) is cumulative resource consumption. Add an edge
\[
(x,q,r)\to(x',q',r+\rho(u,x))
\]
iff \(u\) is admissible under \(\Lambda\), \(x'=\delta_u(x)\), \(q'\) is the rule-memory update, and \(r+\rho(u,x)\le B\).

Then
\[
y\in\operatorname{Cl}_{\mathcal O,B}(x_0)
\iff
\exists q,r\le B:\ (y,q,r)\text{ is reachable from }(x_0,q_0,0)\text{ in }\widehat X.
\]

**Status: PROVED.**

### Proof
Forward direction: lift each step of a legal budget-feasible execution to its expanded state. Nonnegative integer resource accumulation keeps every lifted resource coordinate inside the finite budget box, and the rule-memory coordinate records exactly the information needed by \(\Lambda\). Thus the lifted execution is a path in \(\widehat X\).

Reverse direction: every edge of \(\widehat X\) was inserted only for an admissible primitive, with the correct physical transition, rule-memory update and resource increment. Projecting a path in \(\widehat X\) onto its primitive labels therefore yields a legal execution in \(\mathcal O\); the terminal resource coordinate is at most \(B\). QED.

## 3. Corollary 381.2 — finite compilation size
\[
|\widehat X|\le |X||Q|\prod_{j=1}^k(B_j+1).
\]
Thus the construction is finite but generally pseudo-polynomial in numerically encoded budgets and exponential in the number of independently tracked resource dimensions.

**Status: PROVED.**

This is a representation bound, not a claim of an efficient algorithm in the bit-length of \(B\).

## 4. Corollary 381.3 — finite-memory information/interfaces/rules do not by themselves escape reachability
Any finite information/interface/rule history sufficient to decide future admissibility can be folded into \(Q\). Therefore adding such finite operational bookkeeping to budgeted closure does not, by itself, create a new mathematical species of closure: it produces reachability on a product-state graph.

**Status: PROVED as a compilation statement; novelty as generic GC-II mechanism: FALSIFIED.**

This does not say that a compact GC representation is useless. It says that a claimed breakthrough must exploit structure that is lost or expensive under the compilation, rather than merely rename the expanded reachability problem.

## 5. Boundary / edge-case audit
- Zero budget: only zero-consumption admissible transitions can move away from the initial state.
- Zero-cost cycles: represented exactly; they do not consume the finite resource coordinate.
- Self-loops and duplicate actions: preserved if action identity matters in \(Q\); otherwise quotienting them may be safe only after proving behavioral equivalence.
- Multiple resources: componentwise budget feasibility is represented exactly.
- State-dependent resource consumption: allowed because \(\rho(u,x)\) is evaluated at the source state.
- History-dependent rules: covered iff a finite sufficient memory \(Q\) exists.
- Nondeterministic transitions: the theorem extends by adding every admissible successor edge; the deterministic notation is only for economy.
- Negative/replenishable resources: NOT covered by the finite-box theorem without an explicit bounded-state model; resource coordinates can otherwise leave the box or cycle.
- Continuous resources: NOT finitely compiled by this construction without discretization or a separate finite quotient.
- Unbounded memory/information: NOT covered.
- Composition: product composition can multiply \(|Q|\) and resource-state dimensions; no additive complexity law is claimed.

## 6. Prior-art collision
The generic mechanism is established constrained-path / dynamic-programming territory. Resource-constrained shortest-path methods explicitly carry resource-consumption labels, extend them along arcs, test feasibility, and use dominance. Consequently Theorem 381.1 is retained as a GC-II normalization/boundary lemma, not as a novelty claim.

**Status: IMPORTED/KNOWN mechanism; exact GC-II formulation PROVED; novelty claim rejected.**

## 7. Consequence for Omega_G and Closure-Escape
A candidate \(\Omega_G\) that is solely a function of reachability in \(\widehat X\), or solely of the set \(\operatorname{Cl}_{\mathcal O,B}(x)\), cannot claim novelty merely from the presence of resources, information, interfaces, actions, or finite admissibility rules. Those have already been compiled into the transition system.

The surviving breakthrough gate is therefore:

> derive a compact GC quantity from frozen GC-I envelope/projection structure that predicts a property of budgeted operation without first constructing/solving the expanded reachability instance, and prove a nontrivial advantage or separation (representation size, query/translator burden, compositional certificate, or matched-system distinction).

**Status: OPEN.**

## 8. Status ledger
| Candidate/result | Status |
|---|---|
| Explicit finite budgeted operational closure model | PROVED / definition |
| Exact expanded-state reachability equivalence | PROVED |
| Finite compilation-size bound | PROVED |
| Finite-memory rule/interface bookkeeping as generic escape from reachability | FALSIFIED |
| Generic mechanism | IMPORTED/KNOWN |
| GC-specific compact non-tautological closure certificate | OPEN |
| Nontrivial \(\Omega_G\) surviving expanded-state compilation | OPEN |
