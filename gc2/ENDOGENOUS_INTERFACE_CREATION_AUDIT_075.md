# GC-II Audit 075 — Endogenous Interface Creation Collapse

## Scope
Branch-only Paper-II audit. GC-I `main` remains frozen.

## Candidate inherited from Audit 074
Endogenous Interface Creation Lower Bound:

Omega_IF(q;S,H) = Min_Pareto { Delta : a substrate-realizable interface J of typed construction cost Delta makes q achievable from S }.

The intended escape from Audit 074 was to require J to be physically assembled from a lower-level substrate rather than supplied as a free oracle/sensor/actuator/grammar primitive.

## Result
**Status: FALSIFIED as a standalone novelty source whenever the substrate, assembly rules, interface semantics, task criterion, and typed construction ledger are fixed explicitly. A fixed-substrate interface-design collapse is PROVED.**

### Definition 075.1 — Fixed substrate design model
Let H=(V,Phi,A_H,c_H,Sem) consist of substrate configurations V, physically admissible assembly transformations Phi, candidate interface components/placements A_H, a typed cost ledger c_H with values in R_+^4=(R,I,A,L), and semantics Sem mapping a completed construction plus base system S to the induced observation/action kernel. Let q be a task with scale and error requirement.

A construction protocol pi is any finite admissible sequence of assembly transformations, optionally adaptive to observations generated during construction. Its terminal interface is J(pi). Define

Omega_IF(q;S,H) = Min_Pareto { c_H(pi) : q is achievable from S through J(pi) at the declared scale/error }.

No additivity across cost coordinates is assumed; c_H may be path-dependent provided the sufficient accounting state is part of V.

### Theorem 075.1 — Fixed-substrate interface-design collapse
For explicit H, computing or bounding Omega_IF is exactly a constrained design/reachability problem over substrate configurations. If V and the action/observation alphabets are finite, every adaptive construction protocol is representable in an ordinary finite contingent design graph (or finite MDP when stochastic). Terminal nodes are labelled by the interface kernels induced by Sem; feasibility is determined by the task criterion; path labels carry the same typed ledger.

There is therefore a cost- and task-preserving correspondence between endogenous-interface construction histories and ordinary design/reachability histories. In particular, the word `endogenous` creates no new invariant once the substrate and assembly physics are explicit.

**Proof.** Use substrate configuration, installed components, and any finite sufficient ledger/history statistic as the design state. Every permitted physical assembly step is an edge (or stochastic kernel) with exactly its original typed cost. Sem labels each terminal construction with its induced observation/action interface. A construction succeeds iff its terminal labelled interface makes q feasible at the declared scale/error. Mapping physical construction histories to paths is identity on the underlying sequence of substrate transformations; conversely every graph path is admissible by construction of Phi. Thus feasible histories and typed Pareto costs coincide. QED.

### Corollary 075.2 — Interface lower bounds are architecture-relative
No universal positive lower bound follows from the fact that an interface exposes a previously inaccessible distinction. The same external interface kernel can be free in H1, require one component in H2, or require a long distributed construction in H3. Hence neither the task nor the induced kernel alone determines Omega_IF.

### Corollary 075.3 — Free-interface degeneracy
If H contains a zero-cost construction producing a task-sufficient interface, then 0 belongs to Omega_IF. Therefore a No-Free-Capability theorem cannot be derived from interface creation semantics alone.

## Strong prior-art collision
The principal finite special cases are already recognizable design problems rather than a new calculus:

- For linear systems, choosing outputs/components so that required states or functions become observable is sensor-placement/functional-observability design. Published work gives necessary/sufficient observability characterizations and studies optimal placement.
- Constrained minimum sensor placement can be NP-complete/NP-hard; functional-observability placement is likewise NP-hard in important formulations. Thus computational hardness of constructing the interface is not by itself GC-II novelty.
- Unknown-input structural observability produces further minimum-placement hardness and approximation lower bounds.
- More generally, once component semantics and assembly constraints are fixed, circuit/network synthesis, experiment design, active sensing, actuator placement, communication-network design, and physical design optimization are direct collision classes.

Accordingly, neither `physically built sensor` nor `minimum interface cost` should be marketed as a GC-II breakthrough without a theorem that survives these reductions.

## Edge/counterexample audit
- Empty task requirement: zero construction can be feasible; Omega_IF may contain 0.
- Already observable task: no new interface is required.
- Free sensor primitive: exposes the free-interface degeneracy.
- Multiple incomparable constructions: Omega_IF is Pareto-valued, not necessarily a scalar.
- Nonadditive resource interactions: permitted by carrying the exact path ledger; collapse does not require coordinate additivity.
- Irreversible assembly: omit inverse edges.
- Reversible assembly: include inverse operations and their actual costs.
- Adaptive construction: contingent histories/MDP policies represent it.
- Stochastic sensor quality: Sem is a kernel; task feasibility is evaluated at the required error.
- Continuous substrate: the semantic collapse remains, although exact finite enumeration no longer follows.
- Representation changes: renaming components/configurations preserves Omega_IF when Phi, Sem and c_H are transported isomorphically.
- Composition: composing substrates/interfaces yields the corresponding product/interconnected design problem; composition alone does not escape the reduction.

## Consequence for Omega_G and Paper II
Endogenous Interface Creation is useful as an application-level typed accounting problem but is **not** yet a nontrivial Generative Novelty Gap. In a fixed explicit substrate it is design optimization/reachability; without a fixed substrate its cost is underdetermined.

This kills the candidate as a standalone breakthrough rather than forcing a novelty claim from engineering difficulty.

## New surviving target — Operational Local-to-Global Translator Lower Bound
The next attack returns to the strongest GC-I-specific structure requested in the Paper-II program: projection irreducibility.

Let a global task q_n depend on an n-part system while an admissible interface family exposes only local views of order at most k<n. Define a translator as a physically admissible protocol that, using those local interfaces plus typed augmentation Delta, reproduces the global task behavior to error epsilon. Candidate:

Lambda_G(n,k,epsilon) = Min_Pareto { Delta : a local-interface translator achieves q_n within epsilon }.

The target theorem is **not** merely that local marginals fail to determine a global object; that collides with marginal/contextuality/database/CSP phenomena. The only potentially GC-II-specific result would be a quantitative operational lower bound on the typed augmentation needed to cross from locally indistinguishable states to a global task distinction, invariant under re-encoding and stated relative to an explicit interface class.

### Immediate kill tests
1. Communication complexity: if Lambda_G is just communication needed to compute a distributed function, classify it IMPORTED/KNOWN.
2. Query/decision-tree complexity: if local views are ordinary oracle queries, reduce to query lower bounds.
3. Marginal reconstruction/contextuality: if the obstruction is only non-uniqueness of global distributions from marginals, classify it IMPORTED/KNOWN.
4. Database join/decomposability and CSP width: test whether k-local consistency/global inconsistency already supplies the exact obstruction.
5. Coding/distributed computation: test parity and other global functions against known linear/query/communication bounds.
6. Tensor/network realization: test whether translator cost is rank/bond-dimension/treewidth in disguise.

A breakthrough candidate can survive only if the full task-scale-error-budget statement yields a theorem not exhausted by one of these established complexity/consistency measures.

## Status ledger
- Endogenous Interface Creation Lower Bound as standalone novelty: **FALSIFIED** for fixed explicit substrates.
- Fixed-Substrate Interface-Design Collapse Theorem: **PROVED** under Definition 075.1.
- Architecture-independent Omega_IF from task/interface kernel alone: **FALSIFIED**.
- No-Free-Capability from interface creation alone: **FALSIFIED** by zero-cost-interface counterexample.
- Sensor/actuator/observability specializations: **IMPORTED/KNOWN** collision class.
- Operational Local-to-Global Translator Lower Bound Lambda_G: **OPEN**.
