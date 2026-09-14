# GC-II Audit 141 — Confusability Composition Synergy Collides with Zero-Error Theory

## Candidate tested
After Audit 140 falsified raw transcript support, the next natural candidate is a capability novelty gap based on improvement of exact distinguishability under composition. For a confusability graph G define the one-shot exact distinguishability count as alpha(G), and a two-copy composition gap

Omega_2(G) = log2 alpha(G strong-product G) - 2 log2 alpha(G).

A positive Omega_2 would appear to quantify capability that is unavailable from the naive product of one-shot distinguishability counts.

## Exact counterexample to novelty
Take the pentagon confusability graph C5. Exact enumeration gives alpha(C5)=2. Its strong square has 25 vertices and 100 edges. The checker finds the independent set

(0,0), (1,2), (2,4), (3,1), (4,3)

of size 5 and exhaustively checks all C(25,6)=177100 six-subsets, finding no independent six-set. Hence

alpha(C5 strong-product C5)=5 > 4=alpha(C5)^2,

and

Omega_2(C5)=log2(5/4)=0.32192809488736235 bits > 0.

Thus a strictly positive composition distinguishability gap already occurs in ordinary zero-error confusability theory. The phenomenon is the classical supermultiplicativity behind Shannon graph capacity, not a GC-II-specific generative effect.

## Scope
This does not falsify the possibility of a GC-II novelty gap. It falsifies novelty claims for any Omega_G whose only content is supermultiplicative exact distinguishability under independent/block composition. A surviving GC-II quantity must depend on additional operational structure not erased by reduction to the induced confusability graph and its graph products.

## Prior-art collision
In zero-error information theory, vertices are messages, edges encode confusability, one-shot zero-error code size is alpha(G), repeated independent uses are modeled by strong graph powers, and Shannon capacity regularizes alpha(G^n). The C5 strict gap is canonical. Recent work continues to study composition laws and strict supermultiplicativity for graph products, confirming that composition synergy at this graph level is active established theory rather than a new GC mechanism.

## Ledger
- Positive two-copy distinguishability gap for C5: PROVED / exact finite enumeration.
- Omega_2(C5)=log2(5/4): PROVED.
- Composition synergy based only on confusability-graph independence numbers as GC-II novelty: FALSIFIED.
- Strong-product / Shannon-capacity mechanism: IMPORTED/KNOWN.
- GC-specific operational distinguishability gap surviving graph reduction: OPEN.

## Next gate
Search for two finite operational worlds with the same induced one-shot confusability graph (and therefore the same ordinary zero-error graph invariants) but different capability under admissible GC composition because resource, action/interface, rule, or history constraints alter which graph-product witnesses are operationally realizable. If such a pair survives augmented-state compilation and process/resource-theory reductions, it would establish that the GC carrier contains operational information genuinely lost by ordinary confusability graphs. Otherwise the distinguishability route collapses into zero-error information theory.
