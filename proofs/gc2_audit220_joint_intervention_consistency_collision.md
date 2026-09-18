# GC-II Audit 220 — joint intervention consistency collision

## Target
Audit 219 left open whether a family of interventions can be individually realizable while shared latent consistency prevents any single global realization, and whether that obstruction survives known marginal/contextuality/database/CSP theory.

## Setup
Let a finite family of intervention contexts be a hypergraph H=(V,E). For each context e in E let R_e be the set of locally admissible assignments on e. Call the family overlap-consistent when for every e,f the projections of R_e and R_f to e intersect f agree. Call it globally realizable when there exists a relation R on V whose projection to every e is R_e (or, for the weaker feasibility form, at least one global assignment whose restrictions lie in every R_e).

This is exactly a local-to-global consistency / marginal-extension problem once the operational datum is the family {R_e} and its context hypergraph.

## Minimal cyclic obstruction
Take binary variables x,y,z and contexts {x,y}, {y,z}, {x,z}. Define

R_xy = {(0,0),(1,1)},
R_yz = {(0,0),(1,1)},
R_xz = {(0,1),(1,0)}.

Every one-variable projection is {0,1}; hence every pair of context relations is overlap-consistent. But a global assignment would require x=y and y=z, hence x=z, while R_xz requires x!=z. Therefore no global realization exists.

### Theorem 220.1 — pairwise intervention consistency does not imply global realizability
There exists a finite binary three-context intervention family whose every overlapping pair is consistent but which admits no global realization.

Proof: the parity triangle above. QED.

Status: **PROVED**, but **IMPORTED/KNOWN mechanism** after collision check.

## Structural collision
The obstruction is not GC-specific. Classical database theory characterizes when pairwise consistency implies global consistency: acyclic context/schema hypergraphs have the local-to-global property for relations, while cyclic hypergraphs admit counterexamples. The same local/global extension pattern occurs in marginal problems and contextuality, where a compatible family of local distributions/sections may fail to admit one global distribution/section. CSP local-consistency theory studies the corresponding gap for constraint networks.

Consequently, merely renaming contexts as interventions and the global object as a generative realization does not create a new theorem.

## Theorem 220.2 — representation collapse of the bare joint-consistency candidate
Suppose a GC joint-intervention specification contains no operational structure beyond (i) a context hypergraph H and (ii) a local admissible relation R_e for each context. Then existence of a single GC realization consistent with every intervention is exactly the corresponding global-consistency feasibility problem for {R_e}. Any invariant depending only on this datum factors through that established consistency problem.

Proof: by hypothesis the GC realization condition is precisely existence of a global assignment/relation whose restrictions satisfy the local relations. The identity encoding maps instances and witnesses in both directions. QED.

Status: **PROVED** under the stated representation hypothesis; GC-specific novelty of bare joint consistency **FALSIFIED**.

## Edge/degeneracy audit
- One context: local and global feasibility coincide.
- Disjoint contexts: any choices combine, so no consistency obstruction exists.
- Acyclic context hypergraphs: standard database local-to-global theory supplies broad positive extension results for pairwise-consistent relations; no GC novelty follows from this fact.
- Cyclic contexts: the parity triangle gives the smallest clean Boolean obstruction with three pair contexts.
- Empty local relation: infeasibility is already local and therefore is not a local-to-global gap.
- Pairwise nonempty intersections are weaker than equality of overlap projections; the example satisfies the stronger equality condition.
- Relabeling variables, values, or contexts preserves the obstruction.
- Independent replication composes the obstruction but does not change its theoretical source.

## Exact finite test
`experiments/gc2_audit220_parity_triangle.py` enumerates all eight global Boolean assignments, verifies equality of every overlap projection, and confirms that zero assignments satisfy all three relations. It also deletes each one of the three constraints in turn and confirms satisfiability, certifying minimality with respect to constraint deletion for this example.

## Prior-art boundary
Collision checks for this audit include:
- relational database local-to-global consistency and acyclic hypergraphs (Beeri-Fagin-Maier-Yannakakis lineage; modern Atserias-Kolaitis generalizations),
- Vorob'ev-style marginal consistency,
- contextuality/global-section formulations,
- CSP local consistency and structural width.

The candidate therefore does **not** survive as a Paper-II breakthrough in its bare form.

## Ledger
- Pairwise-compatible but globally impossible intervention family: **PROVED / IMPORTED-KNOWN mechanism**.
- Minimal parity-triangle witness: **PROVED**.
- Bare joint-intervention consistency as GC-specific novelty: **FALSIFIED**.
- Acyclic-hypergraph local-to-global mechanism: **IMPORTED/KNOWN**.
- Contextuality/marginal/CSP collision: **IMPORTED/KNOWN boundary**.
- A GC-specific survivor must add operational structure not preserved by the identity reduction to static local relations, e.g. budgeted sequential generation of the contexts themselves, endogenous availability of contexts, or path-dependent intervention admissibility, and must then survive dynamic CSP/planning/game/process-theory collisions: **OPEN**.

## Consequence
The Paper-II search must not claim local-vs-global intervention incompatibility itself. The next defensible target is **dynamic consistency under endogenous context generation**: whether a budgeted generative process can create or unlock a context family whose extension obstruction cannot be represented by one static hypergraph of local relations without losing operational cost/order information. This target must be tested against dynamic CSP, planning, games, process semantics, and adaptive contextuality before any novelty claim.