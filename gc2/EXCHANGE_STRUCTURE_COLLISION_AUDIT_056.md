# GC-II Audit 056 — Exchange-Structured Frontier Collision

Status date: 2026-09-10
Branch: `gc2-capability-accounting-lab`
Parent audit: 055

## Question

Can the failure of linear support completeness in Audit 055 be repaired by imposing an exchange/submodular law on the typed augmentation frontier, thereby producing a small independently computable complete certificate family that is genuinely GC-II-specific?

## Candidate structure

Let A(q) subset Z_+^d be the feasible typed augmentation vectors for an obligation q, with coordinates representing separately conserved resource/information/interface-action/law-installation quantities after physical normalization within each coordinate. A natural restriction is an exchange axiom: for x,y in A(q) and a coordinate i with x_i>y_i, there exists j with x_j<y_j such that

    x-e_i+e_j in A(q),   y+e_i-e_j in A(q).

Variants permit unequal total mass or generalized-polymatroid exchange.

If this held, one might hope that local exchange tests, submodular rank inequalities, or discrete Fenchel duals would provide an independently computable complete certificate for convertibility.

## Collision theorem

This route does not establish a GC-II breakthrough by itself. The displayed exchange axiom is the defining architecture of M-convex/discrete-polymatroid sets. In established discrete convex analysis, integer points of an integral base polyhedron are M-convex and correspond to integral submodular functions; exchange axioms, conjugacy, separation, and Fenchel-type duality are already part of that theory.

Therefore, whenever a GC typed augmentation frontier is assumed or proved to satisfy this standard exchange law and the proposed certificate is obtained from the associated submodular/base-polyhedron representation, the resulting complete certificate theorem is an IMPORTED/KNOWN specialization of discrete convex/polymatroid theory, not a new GC mechanism.

Status: PROVED as a reduction conditional on the stated standard exchange axiom; novelty route FALSIFIED in that class.

## Why this matters

Audit 055 showed that arbitrary nonconvex Pareto fronts can contain unsupported nondominated points, defeating ordinary nonnegative linear scalarizations. Exchange structure can repair tractability/completeness in important discrete classes, but precisely because it moves the frontier into a mature discrete-convex class. Thus "add exchange structure" solves the mathematical defect at the cost of collapsing the candidate novelty.

## Boundary checks

- Singleton A(q): exchange is vacuous; no generative consequence.
- One typed coordinate: convertibility is totally ordered; no multidimensional GC content.
- Constant-sum integral frontier satisfying symmetric exchange: standard M-convex/base-polyhedron architecture.
- Generalized exchange allowing varying totals: collides with M-natural-convex/generalized-polymatroid theory.
- Linear objective perturbations preserve the relevant established discrete-convex structure; this does not create a new invariant.
- Failure of exchange does not imply Omega_G>0; it merely exits this tractable class and can reproduce arbitrary discrete multiobjective optimization.
- A finite complete monotone family cannot be assumed universally: broad resource theories are known where no finite set completely determines all transformations.

## Consequence for Omega_G

Neither side of the dichotomy is currently a breakthrough certificate:

1. standard exchange holds -> strong dual/certificate machinery exists, but is imported from matroid/polymatroid/discrete convex analysis;
2. standard exchange fails -> arbitrary complementarity/nonconvexity returns, and failure alone carries no GC-specific novelty.

Hence Omega_G must not be defined as an "exchange defect" without an additional operational theorem connecting that defect to conserved task-scale-error-budget composition.

## Stronger surviving target: cross-obligation gluing obstruction

The next candidate should not ask whether each individual frontier A(q) is tractable. Instead consider a family of obligations Q with individually well-behaved typed frontiers A(q), and a joint-realization frontier A(Q). Define a gluing defect only after matching all singleton typed frontiers and their ordinary certificate structures:

    Gamma_G(Q) = obstruction to constructing one admissible joint realization whose restrictions realize every q in Q with the declared shared physical state/interface/law.

A valid breakthrough candidate would require a pair of systems S,T such that:

- every singleton obligation has matched typed frontier and matched standard monotones/certificates;
- every proper subfamily up to a declared order k has matched joint frontier;
- the full family differs operationally under the same conserved evaluator;
- the difference survives semantics-preserving physical compilers;
- the obstruction has an independently computable witness rather than being defined by non-convertibility itself;
- the witness cannot be reduced to contextuality/marginal consistency, database join/decomposability, CSP width, network coding, communication complexity, secret sharing, or ordinary higher-order interaction.

This is deliberately a kill-first target. Marginal/contextuality and database/CSP theories make collision risk high. No breakthrough claim is made.

## Prior-art collision record

The standard exchange route collides directly with:

- M-convex sets and integral base polyhedra;
- submodular functions and polymatroids;
- valuated matroids and multiple-exchange properties;
- Fenchel-type duality in discrete convex analysis.

Broad finite-monotone completeness also has known no-go results in general resource-theoretic settings, so GC-II must state a restricted operational class if it seeks a finite complete family.

## Final classification

- Standard exchange law on typed frontier: VALID restriction.
- Exchange -> M-convex/polymatroid certificate architecture: IMPORTED/KNOWN reduction.
- Exchange structure as standalone GC-II breakthrough: FALSIFIED.
- Exchange failure as Omega_G: FALSIFIED as an implication; failure is not sufficient.
- Cross-obligation gluing obstruction after all lower-order matching: OPEN, next kill-first target.

No change to GC-I/main is required.