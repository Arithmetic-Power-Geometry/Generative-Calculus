# GC-II Audit 028 — Succinctness Collision Boundary

## Status
**DECISIVE FALSIFICATION of generic succinctness as a standalone GC-II novelty route.**

## Question
Audit 027 left open the possibility that a succinct structural rewrite/translator model could yield a GC-II breakthrough because explicit compilation of its structural configurations may be exponentially larger than the succinct description.

## Boundary theorem
Let `M` be any representation formalism in which an instance of description length `n` denotes an explicit finite transition/configuration graph `G_M`, and suppose `G_M` may contain `2^{Theta(n)}` distinguishable configurations. Then an exponential gap between `|M|` and the size of the explicitly compiled graph is not, by itself, a GC-II phenomenon.

### Proof
The claimed separation uses only two facts:
1. a compact description denotes an exponentially larger explicit graph; and
2. the property of interest is evaluated on the denoted graph.

Neither fact refers essentially to GC task-scale-error envelopes, R/I/A/L coupling, closure escape, or capability accounting. Removing all GC annotations leaves the same succinct-versus-explicit representation gap. Therefore the bare exponential compilation gap cannot certify GC-II novelty. QED.

## Prior-art collision
Succinct graph representations are a mature complexity-theoretic mechanism. Karpinski and Wagner (1988) explicitly study graph problems under succinct multigraph representations and report complexity blow-ups caused by the compressed presentation. Later work studies bounded-depth succinct encodings and upward translation phenomena, and hierarchical graph descriptions can encode very large graphs compactly while algorithms operate without full expansion.

Therefore the candidate claim

> “GC structural descriptions are exponentially smaller than their explicit configuration graphs, hence GC-II has a novel structural complexity theorem”

is **FALSIFIED as a novelty claim**.

## What survives
A defensible GC-II theorem must establish a separation that disappears when GC-specific semantics are removed. The next target is therefore not representation succinctness alone but **semantic capability-accounting complexity**.

Fix a representation class `M` and a GC observation family `O_G` containing task, scale, error, budget, information, interface/action and rule semantics. Define the exact whole-envelope translator complexity

`K_G^M(X,Y) = min{|P|_M : P is an admissible translator and O_G(P(X)) = O_G(Y)}`,

with `+infinity` if no admissible translator exists.

This definition is only a research object; it is not claimed novel or complete.

## Required separation criterion
A future breakthrough candidate must exhibit a parametric family `(X_n,Y_n)` satisfying all of the following:

1. `X_n,Y_n` have polynomial-size descriptions in the fixed model `M`.
2. All prescribed low-order/taskwise summaries agree.
3. Every exact admissible whole-envelope translator has superpolynomial/exponential `M`-description complexity, or incurs a proved nontrivial R/I/A/L augmentation lower bound.
4. The lower bound survives arbitrary explicit-state renaming and admissible representation-preserving recodings.
5. The lower bound fails or collapses after deleting at least one essential GC semantic ingredient (for example vector-budget coupling, endogenous information/action/rule acquisition, or task-scale-error requirements). This is the **GC-essentiality test**.
6. The proof does not reduce merely to known determinization, generic succinct-graph expansion, circuit lower bounds, communication complexity, graph-edit distance, planning, CSP/database width, simulation/bisimulation, or algorithmic-information incompressibility.

## Dimensional correction to Omega_G^struct
Audit 027 provisionally wrote a scalar sum of operational cost and description length. That expression is dimensionally unjustified unless a conversion rate is specified. The safe primitive is the Pareto-valued quantity

`Omega_G^struct = (Delta R, Delta I, Delta A, Delta L, K_G^M)`.

A scalarization is admissible only after declaring dimensionless normalizations and weights (or a utility/cost functional) as part of the operational context. This prevents an arbitrary coding-length unit from being added directly to physical/resource units.

## Edge and degeneracy checks
- If `X=Y`, identity is admissible only if the model explicitly includes identity; otherwise zero gap must not be assumed.
- A verbose encoding can artificially inflate `K_G^M`; hence `M` must be fixed before asymptotic claims.
- Universal Turing-machine/Kolmogorov descriptions introduce machine-dependent additive constants and undecidability; they are unsuitable as the primary finite experimental metric.
- Explicit compilation can be exponential while translation is constant-size; compilation size is therefore not a lower bound on translator size.
- If low-order summaries already distinguish the pair, no local-to-global separation has been shown.
- If the lower bound remains unchanged after erasing all GC annotations, it fails the GC-essentiality test.

## Status delta
- Generic succinct structural compilation gap: **IMPORTED/KNOWN; FALSIFIED as standalone GC-II novelty route**.
- Pareto-valued representation-aware structural gap: **OPEN research object**.
- GC-essential semantic translator lower bound: **OPEN / highest-priority asymptotic target**.
- Breakthrough status: **NONE YET**.

## Next exact experiment
Construct small rewrite systems with identical unlabeled configuration graphs but different GC annotations. Exhaustively enumerate bounded translator programs under a fixed tiny DSL. Search for pairs whose minimum translator size/cost separates only after R/I/A/L and task-scale-error-budget semantics are imposed. This controls for generic graph succinctness by holding the underlying graph fixed.
