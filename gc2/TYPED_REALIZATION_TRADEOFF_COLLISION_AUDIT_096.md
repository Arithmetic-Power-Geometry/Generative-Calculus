# GC-II Audit 096 — Typed Realization Obstruction vs Classical Tradeoff Lower Bounds

## Scope

This audit follows Audit 095. It attacks the surviving proposal: obtain a non-tautological capability-accounting law by coupling memory, information/update, access and latency resources.

## Candidate law

Let a capability-preserving implementation have typed cost

c=(R_mem,I_update,A_access,L_latency).

A desired GC-II theorem would forbid part of this region through an independently proved structural inequality, rather than by defining the attainable envelope itself.

## Collision result

STATUS: DECISIVE FALSIFICATION of generic typed-product / generic typed-tradeoff novelty.

A theorem is not novel merely because it has a form such as

R_mem * L_latency >= g(n),

R_mem * A_access >= g(n),

I_comm * L_latency >= g(n),

or a nonlinear multivariate variant. Established computational models already prove structural resource tradeoffs of exactly this kind from independent combinatorial/information arguments.

Examples checked on 2026-09-12:

1. Borodin--Cook sorting lower bounds prove TIME*SPACE lower bounds in a very general sequential model.
2. Beame proves an Omega(n^2) time-space product lower bound for unique-elements/sorting in R-way branching programs.
3. Chen--Chakrabarti prove memory-game tradeoffs ST=Omega(n^2 log n) in an equality model and ST^2=Omega(n^3) in a more general model.
4. Fredman--Saks cell-probe theory explicitly separates representation memory, reads/probes and writes/updates, and derives tradeoffs among them.
5. Communication lower-bound theory for distributed-memory computation and synchronous simulation derives communication/time or message/time tradeoffs.

Thus coupling two or more typed GC coordinates through an independently derived lower bound is scientifically stronger than a Pareto definition, but the *generic form* of such a theorem is already standard complexity-theoretic territory.

## Proposition 096.1 — Embedding no-go

STATUS: PROVED.

Suppose a GC-II operational family F, after fixing its task semantics and admissible transformations, is faithfully reducible to a standard computational model M such that:

- GC memory cost R_mem is a monotone reparameterization of M-space S;
- GC latency L_latency is a monotone reparameterization of M-time T;
- GC access A_access is a monotone reparameterization of M-probes/accesses P when relevant;
- GC information/update I_update is a monotone reparameterization of M-communication/writes C when relevant; and
- capability success is exactly the success predicate of M.

Then every lower bound on (S,T,P,C) transfers to the corresponding GC typed coordinates by substitution. A GC statement obtained only this way is an imported specialization, not a new Generative Calculus law.

Proof: faithful reduction preserves feasible algorithms/protocols and success. If a GC implementation violated the transferred lower bound, its image under the reduction would violate the established M lower bound. Contradiction.

This proof is dimension-safe provided each reparameterization carries explicit units or is dimensionless; arbitrary multiplication of heterogeneous physical units without normalization is not allowed.

## Proposition 096.2 — Coordinate-renaming novelty test

STATUS: PROVED methodological criterion.

If deleting the GC labels R,I,A,L and replacing them with standard model resources (space, communication/update, probes, time) leaves the theorem and proof unchanged, the theorem cannot support a GC-II novelty claim by itself.

This does not say the theorem is unimportant. It says its novelty must come from an operational structure absent from the target standard model, or from a new lower-bound technique/consequence.

## Stress tests

### Degenerate resources

If one coordinate is unconstrained, the candidate may collapse to a known lower-dimensional tradeoff. Any claimed Omega_G must specify how this case behaves.

### Free computation

Cell-probe lower bounds remain meaningful even when internal computation is free. Therefore merely charging access separately from computation does not escape known theory.

### Composition

Known tradeoff bounds need not compose additively. GC-II cannot assume that two independent task bounds sum or multiply without a composition theorem.

### Monotonicity

Allowing more of any resource cannot reduce feasibility under the free-wasting convention, but the Pareto boundary need not be convex and scalarizations can miss nonconvex points.

### Invariance

A physically meaningful typed law must be invariant under changes of measurement units. Products or sums of heterogeneous coordinates require normalization/reference scales or a dimensionally valid physical relation.

## Consequence for Omega_G

A candidate Omega_G defined as violation/excess over a known time-space, probe-space, communication-time, or memory-distortion frontier is IMPORTED/KNOWN unless the GC operational boundary introduces an independently necessary structure not representable in that model.

Therefore the search target from Audit 095 must be strengthened again.

## Strong surviving target

OPEN: find a pair/family of finite operational systems for which all relevant standard reductions agree on their complete feasible tradeoff regions under the chosen boundary, yet GC budgeted operational closure differs because of a precisely stated cross-model compatibility constraint.

The word `compatibility` is essential. Merely collecting several known lower bounds into a vector does not suffice. A candidate must show that individually realizable resource certificates cannot be jointly realized by one operational implementation, and the obstruction must not already be an ordinary multi-resource complexity or scheduling constraint.

A useful next exact search is:

1. enumerate small finite transducers/protocols;
2. compute exact memory-state count, worst-case probes, communication/update bits and depth/latency for each implementation;
3. retain systems with matching coordinatewise minima and matching pairwise projected Pareto regions;
4. test whether their full four-coordinate feasible sets differ;
5. if they differ, determine whether the difference is simply a standard higher-order Pareto/tradeoff interaction;
6. only if a structural certificate survives that reduction, formulate Omega_G from the certificate rather than from the observed region.

This is OPEN and is not a breakthrough claim.

## Status

- generic nonlinear typed tradeoff as GC-II novelty: FALSIFIED
- transfer of standard lower bounds under faithful resource-preserving reduction: PROVED
- coordinate-renaming novelty test: PROVED methodological criterion
- standard time-space / probe-space / communication-time lower bounds: IMPORTED/KNOWN
- cross-model compatibility obstruction beyond ordinary multi-resource complexity: OPEN
- nontrivial Omega_G derived from such an obstruction: OPEN

## Scientific conclusion

Audit 096 removes another broad route: a structural resource inequality is not enough merely because GC writes its resources as R,I,A,L. Classical complexity theory already contains independently proved nonlinear tradeoff surfaces among memory, time, probes, writes and communication. GC-II now needs an obstruction to *joint operational compatibility* that survives faithful reductions to those models and yields a quantitative consequence not obtainable by coordinate renaming.