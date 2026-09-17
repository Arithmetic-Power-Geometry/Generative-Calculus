# GC-II Audit 195 — Endogenous locality/reconfiguration collision

Status: **DECISIVE FALSIFICATION / PRIOR-ART COLLISION**

Parent inspected: `315e336431e48b8ca5d25e137b73c82233d907aa` (Audit 194).

## Candidate attacked

Audit 194 left open the possibility that GC-II novelty might arise when locality itself participates in changing which transformations are admissible, rather than merely constraining communication for a fixed function.

A minimal formalization is a state `(x,G)` where `x` is computational/physical state and `G` is the current interaction graph. The admissible local action set is graph-dependent,

`A(x,G) = {a : locality/interface preconditions of a hold in G}`,

and reconfiguration actions `rho` change the graph,

`rho : (x,G) -> (x',G')`.

Thus reconfiguration can change future admissibility because generally `A(x,G) != A(x',G')`.

## Collision

This mechanism is already explicitly present in the literature on **actively dynamic networks**: distributed entities may actively modify their communication network and exploit network reconfiguration while computing a task. Consequently, the bare principle

> endogenous topology change alters the set of admissible future local interactions

is not a GC-II-specific Closure-Escape mechanism.

A second, very recent collision is **reconfiguration of temporal networks under reachability constraints** (Michail, Skretas, Tennigkeit, Verma, arXiv:2608.02227, submitted 3 Aug 2026), which studies atomic changes to temporal-network labels while preserving reachability and proves a polynomial/PSPACE-hard transition depending on the number of sources.

Related temporal-graph work also studies optimizing reachability sets by modifying/delaying edge availability, and dynamic data structures maintain temporal reachability under contact insertion.

## Exact reduction observation

Any finite GC model whose only endogenous admissibility change is determined by a finite graph/topology state can be represented extensionally as an actively dynamic network transition system by taking the GC configuration `(x,G)` as the distributed configuration and every GC topology-changing primitive as a permitted network-reconfiguration transition. Conversely, an actively dynamic network is an instance of such a GC operational model.

Therefore topology-dependent admissibility plus endogenous graph reconfiguration, without an additional non-network generative constraint, cannot establish independent novelty.

## Ledger

- Graph-dependent admissible action set: **FORMALIZED**.
- Endogenous reconfiguration can change future admissibility: **PROVED by definition/transition semantics**, but not novel.
- Endogenous topology change as the missing GC-II Closure-Escape mechanism: **FALSIFIED / IMPORTED-KNOWN mechanism**.
- Finite graph-state operational compilation to actively dynamic networks: **PROVED at extensional transition-system level**.
- A GC-II theorem requiring joint generation of new semantics *and* new admissibility relations not reducible to graph-state reconfiguration: **OPEN**.

## Prior-art anchors

1. O. Michail, G. Skretas, P. G. Spirakis, “Distributed computation and reconfiguration in actively dynamic networks,” *Distributed Computing* 35, 185–206 (2022), DOI: 10.1007/s00446-021-00415-5.
2. O. Michail, G. Skretas, G. Tennigkeit, S. Verma, “Reconfiguration of Temporal Networks under Reachability Constraints,” arXiv:2608.02227 (3 Aug 2026).
3. “Optimizing reachability sets in temporal graphs by delaying,” *Information and Computation*, DOI: 10.1016/j.ic.2022.104890.

## Next gate

Do **not** pursue topology reconfiguration alone. The next candidate must couple at least two changing levels: the system must acquire a transformation whose semantics was not previously realizable *and* that acquisition must alter the admissibility/compatibility relation for future transformations. The theorem must distinguish this joint semantic–admissibility generation from ordinary dynamic-network reconfiguration, dynamic data structures, program synthesis, and fixed-state transition compilation.
