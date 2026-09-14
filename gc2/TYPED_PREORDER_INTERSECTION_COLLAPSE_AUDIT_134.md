# GC-II Audit 134 — Typed-preorder intersection collapse

## Question
After Audit 133, can independently grounded typed free-operation families for resources/information/interfaces/rules produce a capability obstruction that is intrinsically outside ordinary multi-resource theory merely by intersecting those constraints?

## Theorem — Intersection of independently specified free-operation theories is again a free-operation theory
Let X be an operational state space. For each type i in {1,...,k}, let F_i be a family of transformations X->X satisfying:

1. id_X is in F_i;
2. if f,g are in F_i, then f o g is in F_i.

Define the jointly free family

    F_* = intersection_i F_i.

Then F_* contains id_X and is closed under composition. Hence it induces the ordinary convertibility preorder

    x >=_* y  iff  exists f in F_* with f(x)=y.

If every F_i additionally satisfies a common tensor/parallel-composition closure, F_* inherits that closure as well.

### Proof
The identity belongs to every F_i, so it belongs to their intersection. If f,g belong to F_*, then f,g belong to every F_i. Composition closure of every F_i gives f o g in every F_i, hence f o g in F_*. The tensor statement is identical. Reflexivity and transitivity of >=_* follow from identity and composition. QED.

## Consequence for GC-II
Operationally defining R,I,A,L first and then declaring a transformation jointly free exactly when it is free for every type does not escape resource-theory structure. It constructs another resource theory whose free transformations are F_R intersect F_I intersect F_A intersect F_L.

Therefore a proposed novelty gap or No-Free-Capability theorem whose only input is convertibility under this intersection cannot be claimed as non-resource-theoretic merely because several resource types are present or coupled. Nonlinear monotones, catalysts, incomplete scalar summaries, or nonadditive interactions may make the resulting resource theory difficult, but they do not change this closure fact.

This does not say that GC-II cannot be novel. It says the novelty must live in additional operational structure not reducible to a fixed jointly-free family and its induced preorder—for example a new independently justified task-indexed object, transformation-of-transformation structure, or quantitative law that survives comparison with existing multi-resource/process resource theories.

## Exact finite regression
`experiments/gc2_typed_preorder_intersection_audit.py` enumerates all deterministic transformations on a two-state space, then all subsets containing identity and closed under composition. There are exactly 6 such transformation monoids. It checks all 36 ordered pair intersections and all 216 ordered triple intersections. Every intersection is again a transformation monoid; there are 0 closure failures.

The finite enumeration is only a regression witness. The theorem above is general.

## Prior-art collision
This is standard resource-theory structure. Resource theories define free transformations and the induced convertibility preorder. Multiple notions of resourcefulness and relations among their preorders/monotones are already studied explicitly; see Coecke, Fritz & Spekkens, *A mathematical theory of resources* (Information and Computation 250, 2016), Chitambar & Gour, *Quantum resource theories* (Rev. Mod. Phys. 91, 025001, 2019), and Ying et al., *Conceptual and formal groundwork for the study of resource dependence relations* (arXiv:2407.00164, 2024). Multi-object resource theories also explicitly combine distinct resource-bearing object types (Ducuara, Lipka-Bartosik & Skrzypczyk, arXiv:2004.12898).

## Status
- intersection-closure theorem: **PROVED**
- induced joint convertibility preorder: **PROVED**
- two-state exhaustive regression: **PASS**
- typed-preorder intersection as escape from ordinary resource theory: **FALSIFIED**
- resource-theoretic free-operation/preorder machinery: **IMPORTED/KNOWN**
- GC-II-specific obstruction requiring structure beyond a fixed jointly-free family: **OPEN**

## Next gate
Do not search for novelty merely by adding more typed monotones or intersecting more free-operation classes. Attack a structure that ordinary fixed-preorder resource theory does not already absorb, and require an operationally measurable consequence. The strongest remaining candidate should be tested first against process resource theories, resource dependence relations, supermaps/combs, simulation preorders, contextual equivalence, and compilation into augmented state.
