# GC-II Audit 264 — Boundary-kernel contextual equivalence

## Scope
Audit 263 proved invariance only for private serial refinement. This audit gives the exact compositional equivalence for the finite nonnegative-cost shortest-path semantics used by the current GC-II operational baseline. The mechanism is standard shortest-path/min-plus algebra and is **not claimed as new mathematics**. Its role is to define a canonical implementation quotient that future `Omega_G`, reversibility, and R/I/A/L accounting candidates must respect.

## Definitions
A finite operational module is `M=(V,E,c,B)`, where edge costs are nonnegative and `B subseteq V` is the exposed boundary/interface. Internal states are `V\B`. Its **boundary cost kernel** is

`K_M(i,j)=d_M(i,j)` for `i,j in B`, with `+infinity` for unreachable pairs.

A context `C` may contain arbitrary additional states and nonnegative-cost edges but may meet `M` only at `B`; in particular it has no edge incident to an internal state of `M`. The gluing `C[M]` is the union along the common boundary.

Two modules with the same labelled boundary are **cost-contextually equivalent**, `M ~=_B N`, when every such context has the same shortest-path distances between all context-visible states (the context states together with `B`) after gluing.

## Theorem 264.1 — boundary-kernel replacement
If `K_M=K_N`, then `M ~=_B N`.

### Proof
Take any finite path in `C[M]` whose endpoints are context-visible. Decompose it into maximal excursions through internal states of `M`. Every such excursion enters at some `i in B` and leaves at some `j in B`; its cost is at least `K_M(i,j)`. Because the graph is finite with nonnegative costs, whenever `K_M(i,j)<infinity` a shortest boundary-to-boundary walk attaining that value exists. Replace each module excursion by a shortest `i`-to-`j` walk in `N`. Since `K_N=K_M`, the replacement does not increase cost. Thus `d_{C[N]}<=d_{C[M]}` on visible endpoints. Interchanging `M,N` gives the reverse inequality. Hence all visible distances are equal. QED.

The proof also shows that `M` can be replaced by the canonical complete directed boundary graph having edge `i->j` of weight `K_M(i,j)` whenever the kernel entry is finite.

## Theorem 264.2 — completeness of the boundary kernel
`M ~=_B N` **iff** `K_M=K_N`.

### Proof of necessity
Sufficiency is Theorem 264.1. Conversely, if some `K_M(i,j) != K_N(i,j)`, attach two fresh visible probe states `s,t` with zero-cost edges `s->i` and `j->t`, and no other probe edges. Then `d(s,t)=K(i,j)` in the glued system, so the context distinguishes the modules. QED.

Thus the boundary distance kernel is a complete finite certificate for this costed contextual semantics.

## Corollary 264.3 — budgeted closure and capability-value congruence
For every context-visible start `x`, visible target `F`, and budget `B0>=0`, replacing a module by another module with the same boundary kernel preserves

`V(x;F)=min_{f in F} d(x,f)`

and therefore preserves membership in `Cl^{B0}(F)`.

## Corollary 264.4 — Omega descends to the quotient
For the Audit-262 finite scalar novelty gap `Omega=V_baseline-V_extension` whenever both terms are finite, independently replacing the baseline and extension implementations by modules having the same respective boundary kernels leaves `Omega` unchanged in every external context. Therefore this `Omega` is representation-stable under a substantially broader class than Audit 263 serial subdivision.

## Why this is stronger than Audit 263
Private serial refinement is only one way to preserve `K_M`. Internal graphs may now differ arbitrarily in state count, topology, parallel routes, zero-cost structure, and generator decomposition. They are indistinguishable to every permitted external shortest-path capability query exactly when their exposed boundary kernels agree.

## Boundary / falsification conditions
The theorem intentionally fails if a context can access an internal state: then the declared boundary was incomplete. It also does not preserve observables beyond cost/reachability (path counts, labels, probability laws, internal information, latency distributions, energy vectors, action traces). For such semantics the interface summary must be enriched; scalar boundary distances are not complete.

Negative costs are excluded. With negative cycles, shortest-path values may be `-infinity` and the finite-attainment argument and current GC-II budget semantics require reformulation.

## Checks
- **Dimensions:** every kernel entry, path value, budget and finite `Omega` has cost units.
- **Unreachable pairs:** represented by `+infinity`; the proof preserves them.
- **Zero-cost edges/cycles:** allowed; nonnegativity preserves well-defined minima.
- **Degenerate boundary:** empty/singleton boundaries are valid but carry little/no transfer information.
- **Monotonicity:** adding admissible edges can only decrease kernel entries and capability values.
- **Composition:** contextual equivalence is a congruence under repeated gluing at declared boundaries.
- **Invariance:** exact for all scalar shortest-path capability queries at exposed interfaces.
- **Refinement:** Audit 263 is recovered because private serial refinement preserves the boundary kernel.

## Exact finite verification
`experiments/gc2_audit264_boundary_kernel_contextual_equivalence.py` enumerates all 4,096 directed three-state modules with two exposed boundary states, where each possible non-loop edge is absent or has cost `0,1,2`. Each module is replaced by its canonical boundary kernel. It then enumerates all 729 one-external-state contexts whose possible visible edges are absent or have cost `0,2`. It checks all nine ordered visible-state distances for every module/context pair: **26,873,856 exact equalities**, with no counterexample. A separate probe test verifies necessity by distinguishing unequal kernels.

## Prior-art / novelty discipline
The algebraic mechanism is established shortest-path theory: all-pairs distances are naturally expressed over the min-plus/tropical semiring, and graph/network reduction by terminal behavior is an established idea. This audit therefore labels the generic kernel/compositional mechanism **IMPORTED/KNOWN**. The GC-II contribution at this stage is methodological: it identifies the exact quotient required by the present costed operational semantics and prevents representation-dependent novelty claims. A genuinely GC-specific advance would require extending the interface summary to typed R/I/A/L semantics or proving a nontrivial bound/invariant on that richer quotient.

## Status ledger
- Boundary-kernel equality implies contextual equivalence for scalar cost semantics: **PROVED / IMPORTED-KNOWN mechanism**.
- Boundary-kernel equality is necessary for equivalence against all boundary-only contexts: **PROVED**.
- Boundary kernel is a complete certificate for finite cost-contextual equivalence: **PROVED / IMPORTED-KNOWN mechanism**.
- Budgeted closure/value invariance under kernel-equivalent replacement: **PROVED**.
- Audit-262 finite `Omega` descends to this quotient: **PROVED**.
- Scalar kernel complete for typed information/action/rule observables: **FALSIFIED / not implied**.
- Canonical typed R/I/A/L contextual quotient: **OPEN**.
- Nontrivial GC-specific quantitative theorem on the richer quotient: **OPEN**.
