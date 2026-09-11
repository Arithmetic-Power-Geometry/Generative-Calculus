# GC-II Audit 074 — Minimal Operational Model Extension Cost Collapse

## Scope
Branch-only Paper-II audit. GC-I `main` remains frozen.

## Candidate inherited from Audit 073
Seek a nontrivial typed cost for extending an operational model M to M' by installing new admissible primitives generated from a fixed meta-operational grammar G.

## Result
**Status: FALSIFIED as a standalone novelty source in the finite explicit case. A meta-grammar collapse theorem is PROVED. The unrestricted/computable case reduces to established synthesis/oracle/description-complexity questions unless extra physical structure is supplied.**

### Definition 074.1 — Explicit extension grammar
Let M=(X,T,Q,c) be an operational model with state space X, admissible transformations T, task family Q, and typed ledger c:T* -> R_+^4 with coordinates (R,I,A,L). Let G be a finite explicit grammar whose productions install primitives e in a finite set E. Each production has explicit preconditions, state update, installation cost d(e) in R_+^4, and a declared effect on the subsequently admissible transformation set.

An extended configuration is z=(x,U), where x in X and U subseteq E is the set of installed primitives. Let T_U denote the transformations available after U has been installed.

### Theorem 074.1 — Finite meta-grammar collapse
For finite X,E and explicit G, every protocol that alternates ordinary actions with model-extension actions is exactly representable as an ordinary fixed operational model on

Z = X x 2^E.

The fixed transition relation contains (i) ordinary transitions (x,U)->(x',U) for actions in T_U and (ii) installation transitions (x,U)->(x',U union {e}) whenever the corresponding production of G is enabled. Assign the same typed costs to corresponding transitions.

Then there is a cost-preserving bijection between histories of the extension semantics and histories of the fixed augmented-state semantics. Consequently they have identical task success/error sets, typed budget frontiers, composition behavior, reversibility properties defined on histories, and Pareto-minimal extension costs.

**Proof.** Map each extension history to the sequence of pairs consisting of its physical state and the set of primitives installed so far. Every ordinary step is legal exactly when it is present in T_U; every grammar production is represented by its installation transition. Conversely, every augmented transition decodes uniquely to one permitted ordinary or installation step. Induction on history length gives a bijection of finite histories. Because transition costs and task observations are copied, cumulative typed ledgers and task/error values are preserved coordinatewise. No additivity between resource dimensions, convexity, scalarization, or probabilistic assumption is required. QED.

### Corollary 074.2 — No novelty from naming a transition 'model extension'
In a finite explicit grammar, Minimal Operational Model Extension Cost is an ordinary shortest/Pareto reachability cost in an augmented state graph. Calling an installed primitive a change of operational model rather than a state transition does not create a new invariant.

### Proposition 074.3 — Free-extension degeneracy
If G permits installation of every task-solving primitive at zero typed cost, then Omega_ext=0 for every reachable target task. Hence any No-Free-Capability theorem requires explicit nonzero restrictions/costs on extension productions; it cannot follow from the word 'extension' alone.

### Proposition 074.4 — Grammar-relative underdetermination
The same endpoint pair (M,M') does not determine Omega_ext. Two grammars G1,G2 may generate exactly the same M' from M but assign different required intermediate interfaces, information, computation, or physical installation steps, producing different Pareto costs. Therefore no universal endpoint-only function

Omega_ext = F(M,M')

exists without fixing the extension architecture and ledger.

### Infinite/computable case
If G is an unbounded computable generator of primitives, the finite 2^E construction is unavailable as a finite graph, but this alone is not a GC-II breakthrough. Depending on the chosen semantics, finding/constructing an extension becomes program synthesis/search, description or time-bounded complexity, oracle/query complexity, advice complexity, planning, or reachability in an infinite-state system. If an extension supplies an oracle/advice primitive for free, its capability is assumed at the accounting boundary rather than generated.

Thus a purported universal law-generation theorem must distinguish physical generation from semantic access to a primitive.

## Prior-art collision audit
- **Resource theories:** free/costly transformations and their sequential/parallel composition are already the basic mathematical architecture of resource conversion. Adding a finite installable primitive as another charged transformation remains inside that architecture.
- **Reachability/planning:** finite installation state U turns extension selection into ordinary augmented-state reachability with vector costs.
- **Oracle/query complexity:** granting a new query primitive changes the computational access model; query complexity measures use of such access rather than deriving its physical installation cost.
- **Advice complexity:** supplied nonuniform information can increase computational capability, but the model explicitly declares the advice resource.
- **Program synthesis/algorithmic information:** when the primitive itself must be generated from a description, synthesis/search and description/runtime complexity become immediate reductions.

No collision check located evidence that the bare distinction between 'changing the model' and 'changing augmented state' escapes these reductions.

## Edge-case and theorem audit
- Empty E: reduces exactly to M.
- Zero-cost installations: allowed; exposes degeneracy rather than invalidating theorem.
- Irreversible installation: encoded by omitting uninstall transitions.
- Reversible installation: encoded with explicit inverse transition and its typed cost.
- Installation dependencies: encoded in grammar preconditions.
- Nonlinear/path-dependent costs: append sufficient ledger/history state; finite exact collapse holds whenever that sufficient state is finite and explicit.
- Stochastic transitions: replace edges by kernels on Z; history-law equivalence is preserved.
- Continuous X: finite-E model-extension label still collapses into X x 2^E, although numerical reachability may be difficult.
- Composition: product systems carry installed-set state explicitly; no new composition principle is created by the label 'extension'.
- Representation change: equivalent encodings of E do not alter the operational history set if transition semantics and ledgers are preserved.
- Unbounded E: theorem's finite-state conclusion does not apply; only the semantic reduction warning applies.

## Consequence for Paper II
Do not market Minimal Operational Model Extension Cost itself as the GC-II breakthrough. In the explicit finite regime it is ordinary typed reachability/resource conversion on an augmented state. In the unrestricted regime it is underdetermined until a physical generation architecture is fixed, after which established synthesis/complexity theories become immediate collision targets.

## New surviving target — Endogenous Interface Creation Lower Bound
The remaining crack is not 'install a primitive' but whether a system can **physically create a new interface that exposes previously inaccessible distinctions**, when the interface must itself be built from a fixed lower-level substrate and its cost cannot be hidden as a free oracle, advice string, sensor, actuator, or grammar production.

Candidate quantity:

Omega_IF(q;S,H) = Min_Pareto { Delta : a substrate-realizable interface J of typed construction cost Delta makes q achievable from S }.

For content, H must specify the lower-level substrate, locality/causality constraints, permissible assembly operations, observation/action semantics, and typed construction ledger. This candidate is **OPEN**, not a breakthrough claim.

Immediate kill tests: sensor/actuator placement and observability/controllability, experimental design, communication complexity, measurement resource theories, circuit/network synthesis, causal discovery, active perception, and physical design optimization. A genuine GC-II result would require a lower bound that couples interface construction to the full task-scale-error-budget closure and survives reduction to those theories.

## Status ledger
- Minimal Operational Model Extension Cost as standalone novelty source: **FALSIFIED** in finite explicit regime.
- Finite Meta-Grammar Collapse Theorem: **PROVED** under Definition 074.1.
- Universal endpoint-only extension cost F(M,M'): **FALSIFIED** without grammar/architecture assumptions.
- No-Free-Capability from extension semantics alone: **FALSIFIED** by free-extension degeneracy.
- Infinite/computable extension novelty: **OPEN**, with strong prior-art reductions.
- Endogenous Interface Creation Lower Bound: **OPEN**.