# GC-II Audit 140 — Raw Transcript Support Is Not Capability

## Claim tested
The candidate deficit D_G = log2(nominal transcript capacity) - log2(global realizable transcript support) was tested as a capability-sensitive quantity.

## Counterexample
Let task class c and nuisance bit n both lie in {0,1}, and let a deterministic binary sensor map (c,n) to {0,1}.

Informative sensor: f(c,n)=c. Its global support is {0,1}, so D_G=0. The class-conditioned supports are {0} and {1}; exact discrimination is possible.

Confounded sensor: f(0,0)=f(0,1)=f(1,0)=0 and f(1,1)=1. Its global support is also {0,1}, so D_G=0. But the class-conditioned supports are T_0={0} and T_1={0,1}. They overlap, so observation 0 cannot determine the class and exact discrimination is impossible.

Thus identical nominal capacity, global transcript cardinality, and raw deficit can coexist with different exact task capability. Global transcript support alone is therefore not capability sufficient.

## Exhaustive regression
The checker enumerates all 16 deterministic binary sensors on the four (class,nuisance) states. Fourteen have maximal global support size 2 and hence D_G=0. Of those fourteen, exactly two permit exact class discrimination and twelve do not.

## Correct structural direction
For exact discrimination, the relevant object is the family of class-conditioned transcript supports {T_c}. Exact one-shot discrimination requires T_c and T_c' to be disjoint for every distinct pair of classes. Equivalently, the class confusability graph must have no edges.

That structural object is already connected to established zero-error information theory, confusability graphs, comparison of statistical experiments, and observational equivalence. It is imported structure unless GC-II derives a genuinely new quantitative operational law from it.

## Ledger
- Raw global transcript support as capability invariant: FALSIFIED.
- Same-deficit/different-capability counterexample: PROVED.
- Exhaustive 16-sensor regression: PASS.
- Class-conditioned support/confusability criterion: IMPORTED/KNOWN.
- GC-specific novelty gap based on operational distinguishability under composition: OPEN.

## Next gate
A viable Omega_G must quantify how observations separate operationally relevant task classes, not merely how many transcripts occur. The next candidate should use task-conditioned confusability or distinguishability and be collision-tested against zero-error information theory, Blackwell-Le Cam comparison, communication complexity, and simulation preorders before any novelty claim.
