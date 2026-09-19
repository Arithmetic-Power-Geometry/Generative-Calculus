# GC-II Audit 244 — Replication obstruction for Omega_add

## Purpose
Stress-test Audit 239's exact incidence-repair gap as a candidate intrinsic Generative Novelty Gap. Audit 243 showed that typed operation counts do not calibrate its rate of decrease. This audit asks a more basic invariance question: does Omega_add preserve capability-equivalent replication of worlds?

## Replication operation
Fix a finite translator instance X=(W,p,g,M,L). For integer k>=1, define Rep_k(X) by replacing every world w by k clones (w,1),...,(w,k) with exactly the same projection, required decision, and admissible message list:

    p_k(w,j)=p(w),
    g_k(w,j)=g(w),
    L_k(w,j)=L(w).

No new observational distinction, required behavior, admissible action, or decoder obligation is introduced. A translator for X extends to every clone, and any translator for Rep_k(X) restricts to one representative of each clone class. Hence exact translator feasibility is invariant under Rep_k.

## Replication theorem for Omega_add — PROVED
For every finite X and integer k>=1,

    Omega_add(Rep_k(X)) = k Omega_add(X).

Proof. For any fixed fiber message-labeling lambda, the uncovered indicator of each original world is copied exactly k times, so its repair objective is multiplied by k. Minimizing over the same set of fiber labelings therefore multiplies every fiber optimum by k; summing fibers proves the identity.

## Decisive consequence — FALSIFIED as an intrinsic capability gap
Take the minimal ambiguous instance with two worlds, one projection fiber, decisions 0 and 1, M={0,1}, and L(w)={0} for both worlds. Then Omega_add=1. Rep_k has exactly the same translator feasibility structure up to duplicate indistinguishable obligations, but

    Omega_add(Rep_k)=k.

Therefore Omega_add is not invariant under multiplicity-free operational equivalence. It is an exact *extensive repair count* for the chosen world enumeration, but cannot be treated without qualification as an intrinsic Generative Novelty Gap measuring capability itself.

This also explains Audit 243's unbounded-refinement family: part of the n/2 growth is multiplicity sensitivity. A one-step projection refinement can erase many duplicated repair obligations even when the logical decision pattern is unchanged.

## Quotient repair gap — PROVED invariant under exact clones
Define clone equivalence

    w ~ w' iff p(w)=p(w'), g(w)=g(w'), and L(w)=L(w').

Let Q(X) contain one representative of each equivalence class and define

    Omega_Q(X) := Omega_add(Q(X)).

Then Omega_Q(Rep_k(X))=Omega_Q(X) for all k. This removes pure clone multiplicity while retaining distinct admissibility patterns.

However Omega_Q is NOT yet claimed as the correct GC-II novelty invariant. Quotienting can discard meaningful population mass, probabilities, reliability requirements, repeated physical agents, or repeated tasks when multiplicity is operationally real. The correct choice must be dictated by semantics: set-like worlds suggest quotienting; probabilistic worlds suggest normalized weights; physical repeated obligations may require an extensive measure.

## Weighted normalization alternative — CONDITIONAL
Given weights mu(w)>=0 with total mass 1, replace uncovered counts by uncovered mass and minimize over fiber labelings. Exact replication with each clone receiving mu(w)/k preserves the weighted gap. This is dimensionless and replication invariant, but introduces a distribution and therefore changes the operational question. It is closely related to expected-risk / weighted CSP objectives and is not claimed as novel.

## Edge cases
- Omega_add=0 remains 0 under every replication.
- Infeasibility caused by more required decisions in a fiber than messages remains infinite under replication.
- Relabeling worlds/messages/decisions/projection symbols leaves both feasibility and the replication identity unchanged.
- Partial replication scales only the objective contribution of the replicated clone class; this can change which labeling minimizes repair, so no global linear formula holds for arbitrary nonuniform replication.
- Exact translator bit requirement from Audits 234-235 is clone invariant because the number of distinct required decisions per projection fiber does not change.

## Prior-art collision boundary
Replication sensitivity versus normalized/quotiented objectives is a standard modeling distinction across optimization, probability, empirical risk, CSPs, and information theory. The mathematical scaling identity is therefore not claimed as a new generic theorem. Its importance here is diagnostic: it falsifies an over-strong interpretation of the current GC-II Omega candidate before Paper II builds accounting laws on it.

## Status ledger
- Exact translator feasibility invariant under exact world cloning: PROVED.
- Omega_add(Rep_k X)=k Omega_add(X): PROVED.
- Omega_add as replication-invariant intrinsic capability gap: FALSIFIED.
- Omega_add as extensive minimum incidence-repair count for a fixed enumerated world model: PROVED / retained.
- Clone-quotient Omega_Q replication invariance: PROVED.
- Weighted normalized repair gap replication invariance under mass splitting: PROVED / IMPORTED-KNOWN mechanism.
- Omega_Q or weighted gap as the unique/correct GC-II Generative Novelty Gap: OPEN.

## Paper-II implication
GC-II must state the ontology before defining Omega_G. If worlds are epistemic possibilities, exact duplicate worlds carry no additional capability content and Omega_G should be quotient/replication invariant. If worlds encode repeated physical obligations or probability mass, multiplicity can be meaningful and an extensive or weighted gap is appropriate. A purported universal capability-accounting theorem cannot silently mix these regimes.
