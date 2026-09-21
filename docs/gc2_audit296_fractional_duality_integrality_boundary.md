# GC-II Audit 296 — Fractional dual certificates and the bipartite integrality boundary

## Scope
This audit continues Audits 294–295 for zero-loss finite capability accounting with target frequency exactly two. GC-I/main is not modified.

## Operational model
Let A be the finite decoder-action set and Y the finite target set. Each target y is feasible under exactly two distinct actions. Associate to y={u,v} an edge uv of a simple action-incidence graph G=(A,E). A persistent exact account is a subset C⊆A such that every target has at least one feasible selected decoder. Hence its minimum state count is the vertex-cover number τ(G).

## Fractional accounting relaxation
Introduce x_a≥0 for each decoder action a and solve

    P(G):  minimize  Σ_a x_a
           subject to x_u+x_v ≥ 1   for every target/edge uv.

Its LP dual is

    D(G):  maximize  Σ_e z_e
           subject to Σ_{e incident to a} z_e ≤ 1  for every action a,
                      z_e≥0.

Weak/strong LP duality gives P*=D*. Any integral primal feasible point is an exact account; any integral dual feasible point is a matching. Thus D* is a computable fractional packing lower certificate for exact accounting.

## Theorem 296.1 — exact dual certificate on bipartite incidence
If G is bipartite, the edge/vertex incidence matrix is totally unimodular. Therefore P and D have integral optima for integral right-hand sides, and

    N_0 = τ(G) = P*(G) = D*(G) = ν(G).

So Audit 295 admits a stronger operational reading: a maximum set of pairwise action-disjoint targets is a complete lower certificate for the minimum number of decoder states, and LP duality closes the certificate gap exactly.

Status: PROVED, using imported total-unimodularity/Kőnig–Egerváry theory.

## Theorem 296.2 — odd-cycle obstruction
For an odd cycle C_(2k+1), setting x_a=1/2 at every cycle action is primal-feasible with value (2k+1)/2. The exact account requires k+1 actions. Hence

    τ(C_(2k+1)) - P*(C_(2k+1)) = 1/2,

and

    τ(C_(2k+1))/P*(C_(2k+1)) = (2k+2)/(2k+1) > 1.

Therefore the integral dual-certificate identity from Theorem 296.1 cannot be extended to unrestricted frequency-two incidence graphs.

Status: PROVED.

## Corollary 296.3 — universal exactness boundary
For this frequency-two accounting class, bipartiteness is sufficient for exactness of the natural fractional accounting LP for every nonnegative action-cost vector. Conversely, if G is non-bipartite it contains an odd cycle; by assigning zero cost to off-cycle actions and positive unit cost on the chosen odd cycle (and selecting zero-cost outside actions where needed), one obtains a weighted instance exposing the odd-cycle fractional obstruction. Thus universal weighted LP exactness is tied to the bipartite/TU incidence structure.

Status: PROVED modulo the standard imported characterization of bipartite graph incidence matrices / vertex-cover polyhedral integrality.

## Edge and degeneracy checks
- E=∅: primal and dual values are 0; exact account is empty.
- Disconnected graphs: objectives and certificates decompose additively by connected component.
- Isolated actions: irrelevant to all three optima.
- Duplicate targets: do not change the cover constraints; multiplicity can change a naively defined packing only if duplicates are incorrectly treated as distinct parallel edges, so the operational quotient must deduplicate identical feasibility pairs before invoking simple-graph matching.
- Frequency-one targets: preprocess as forced actions; the residual frequency-two graph receives the theorem.
- Triangle: τ=2 while fractional optimum=3/2, the smallest obstruction.
- Even cycles: bipartite; no integrality gap.
- Composition: disjoint union preserves exactness; arbitrary cross-interface composition can create odd cycles and therefore does not preserve the certificate identity without a maintained bipartition.

## Novelty / collision audit
The graph theory, LP duality, total unimodularity, Kőnig–Egerváry equality, and odd-cycle obstruction are IMPORTED/KNOWN. This audit does not claim them as new mathematics. The GC-II contribution is the operational identification of a complete *dual capability-accounting certificate* in the frequency-two bipartite regime, together with an exact structural obstruction showing why the same certificate ceases to be complete after global incidence loses bipartiteness.

This is compatible with the prior collision map: unrestricted feasible-action systems reduce to SET COVER (Audit 291); interval systems are tractable (Audit 292); two-dimensional products restore hardness (Audit 293); frequency two reduces to vertex cover (Audit 294); bipartite frequency two is tractable (Audit 295). Audit 296 adds a finite/computable/dual-monotone certificate layer rather than another hardness result.

## Paper-II implication
For structured complete convertibility/accounting criteria, the correct target is not merely a scalar monotone. In this regime the pair

    (primal cover certificate, dual packing certificate)

is complete exactly when the operational incidence matrix has the required integrality structure. This supplies a concrete model for GC-II's broader search for finite/computable/dual monotone families: completeness can be an integrality property of the operational interface, not a property of a single score.

## Status ledger
- frequency-two account = vertex cover: PROVED (Audit 294)
- bipartite frequency-two account = matching: PROVED (Audit 295 / imported Kőnig)
- fractional primal/dual operational formulation: PROVED
- bipartite zero integrality gap: PROVED via IMPORTED/KNOWN TU theory
- odd-cycle fractional obstruction: PROVED
- unrestricted integral dual certificate completeness: FALSIFIED
- extension to higher-frequency hypergraph incidence: OPEN
