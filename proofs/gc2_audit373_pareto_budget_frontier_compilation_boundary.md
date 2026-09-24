# GC-II Audit 373 — Pareto budget frontier compilation boundary

## Question
Can the post-Audit-372 breakthrough be obtained by replacing a scalar interaction residual with the full multidimensional budget frontier of admissible derivations?

## Model
Let a finite operational system have state set (X), initial state (s), target set (T\subseteq X), and admissible directed transitions (e). Each transition carries a nonnegative typed cost vector
[
c(e)\in \mathbb{R}_{\ge 0}^{d}.
]
Coordinates may represent resource expenditure, information acquisition, interface/action expenditure, latency, or any other commensurately typed nonnegative budget coordinate.

For a finite derivation (p=e_1\cdots e_k), define
[
C(p)=\sum_{j=1}^{k}c(e_j).
]
Let
[
\mathcal U_T(s)=\{C(p):p:s\leadsto t, t\in T\}
]
and let (\mathcal F_T(s)=\operatorname{Min}_{\le}\mathcal U_T(s)) be its coordinatewise nondominated frontier.

For budget (b\in\mathbb R_{\ge0}^d), define the budgeted closure
[
\mathrm{Cl}_b(s)=\{x:\exists p:s\leadsto x, C(p)\le b\}.
]

## Theorem 373.1 — Exact frontier feasibility
For a finite operational system with nonnegative additive transition costs,
[
T\cap\mathrm{Cl}_b(s)\ne\varnothing
\quad\Longleftrightarrow\quad
\exists f\in\mathcal F_T(s): f\le b.
]

### Proof
The reverse implication is immediate from the definition of the frontier.

For the forward implication choose a feasible target-reaching path (p) with (C(p)\le b). Delete every directed cycle from (p). Because all coordinates of every edge cost are nonnegative, cycle deletion cannot increase any coordinate. The resulting simple target-reaching path (q) therefore satisfies (C(q)\le C(p)\le b).

There are finitely many simple paths in a finite graph. Hence among the costs of simple target-reaching paths dominated by (C(q)), at least one coordinatewise minimal element (f) exists. Any path cost strictly dominating (f) would, after cycle deletion, yield a simple path cost no larger and still strictly below (f), contradicting minimality. Thus (f\in\mathcal F_T(s)) and (f\le b). QED.

## Edge cases
- If (s\in T), the empty derivation gives (0\in\mathcal F_T(s)).
- If no target is reachable, both sides of the theorem are false and the frontier is empty.
- Zero-cost cycles do not invalidate the proof: deleting them preserves cost.
- Negative cost coordinates are excluded; otherwise cycle deletion need not preserve feasibility and negative cycles can destroy frontier minimality.
- The theorem is coordinate-type agnostic but does not permit adding quantities with incompatible physical dimensions inside one coordinate.

## Finite sufficient-state compilation
Suppose admissibility depends on a history variable (h), but there exists a finite sufficient statistic (q(h)\in Q) such that:
1. enabled actions depend only on current physical state and (q(h));
2. after action (a), the new statistic is a deterministic function of current state, statistic, action, and resulting observation;
3. transition cost is determined by that augmented transition.

Then form augmented states ((x,q)\in X\times Q). The history-dependent system is exactly a finite vector-cost reachability problem on the augmented graph, so Theorem 373.1 applies unchanged.

Therefore finite rule state, finite acquired-information state, finite interface mode, and finite memory do not by themselves escape the classical vector-cost/Pareto-reachability reduction.

## Collision / novelty status
The mathematical mechanism is not GC-specific. Resource-constrained shortest-path and multicriteria/multiobjective shortest-path theory already studies paths under resource bounds, nondominated labels, and Pareto-optimal path sets. State augmentation/product constructions are standard whenever history dependence admits a finite sufficient state.

Accordingly:
- exact frontier feasibility criterion: **PROVED**;
- nonnegative additive vector-cost Pareto mechanism: **IMPORTED/KNOWN**;
- full Pareto frontier as a novel GC-II replacement for scalar \(\Omega_G\): **FALSIFIED**;
- finite-state augmentation as a novelty escape: **FALSIFIED**;
- genuinely non-finitely-Markovizable endogenous admissibility with a GC-I envelope/projection theorem: **OPEN**.

## Consequence for Paper II
A breakthrough cannot consist only of adding more budget coordinates, using nonlinear scalarization, retaining the entire Pareto frontier, or appending finite rule/information/interface memory. Under the assumptions above those moves compile into established finite-state multicriteria reachability.

The surviving route must identify a stronger obstruction, for example an admissible generative language whose future rule set cannot be represented by any finite sufficient operational state for the family under study, and then prove an independently meaningful GC-I/GC-II structural consequence rather than merely restating infinite-state reachability.

## Prior-art anchors
- L. Di Puglia Pugliese and F. Guerriero, “A survey of resource constrained shortest path problems: Exact solution approaches,” *Networks* 62(3), 183–200 (2013), DOI 10.1002/net.21511.
- O. Salzman et al., “Heuristic-Search Approaches for the Multi-Objective Shortest-Path Problem: Progress and Research Opportunities,” *IJCAI 2023*, DOI 10.24963/ijcai.2023/757.

These anchors establish the collision class; they are not claimed to contain the GC terminology above.
