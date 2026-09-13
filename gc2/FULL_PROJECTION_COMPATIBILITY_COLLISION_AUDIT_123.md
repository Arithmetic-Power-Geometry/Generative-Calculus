# GC-II Audit 123 — Full Projection Compatibility Collision

## Scope

Audit 122 proposed minimal sufficient operational memory as the next route. The branch already contains Audit 094, which proves that the complete future-equivalence quotient is a canonical minimal sufficient operational state and falsifies that quotient as standalone GC-II novelty by collision with Myhill–Nerode, causal states, predictive-state representations, bisimulation/state abstraction, and related minimal sufficient-state constructions. Audits 095 and 096 further show that generic typed realization regions and generic multiresource tradeoff laws are not novel by themselves.

This audit therefore attacks the surviving proposal from Audit 096: seek two finite operational systems whose coordinatewise and lower-dimensional typed-resource summaries match while their full joint feasible realization sets differ, and treat that mismatch as a new GC-II compatibility obstruction.

## Candidate

Let a feasible realization certificate be a tuple

c = (R, I, A, L) in {0,1}^4.

For a feasible relation F subset {0,1}^4, let pi_S(F) be its coordinate projection onto S subset {R,I,A,L}. A tempting novelty candidate is a pair F,G such that every proper projection agrees,

pi_S(F) = pi_S(G) for all proper S,

but F != G.

Such a pair would prove that all one-, two-, and three-coordinate resource views can be complete locally while failing to determine global joint realizability.

## Exact witness

Define

F_even = {x in {0,1}^4 : x_R + x_I + x_A + x_L = 0 mod 2},

F_odd  = {x in {0,1}^4 : x_R + x_I + x_A + x_L = 1 mod 2}.

Each relation contains eight tuples.

### Theorem 123.1 — Proper-projection indistinguishability

STATUS: PROVED.

For every proper coordinate set S subsetneq {R,I,A,L},

pi_S(F_even) = pi_S(F_odd) = {0,1}^{|S|}.

Proof. Fix any assignment y on a proper subset S. At least one coordinate j is omitted. Choose all omitted coordinates except j arbitrarily. The final omitted bit x_j can then be chosen uniquely to make total parity even, and oppositely to make it odd. Hence y extends to both F_even and F_odd. Therefore each proper projection is the complete binary cube on S. QED.

Yet F_even and F_odd are disjoint, so their full feasible sets differ maximally.

The executable checker verifies all 14 nonempty proper coordinate projections (4 one-dimensional + 6 two-dimensional + 4 three-dimensional): 0 mismatches.

## Collision result

STATUS OF `lower-dimensional typed-resource agreement but global feasible-set mismatch as standalone GC-II novelty`: FALSIFIED.

The construction is not new capability mathematics. It is the same local-to-global information-loss phenomenon already present in:

1. relational database projection/join theory: a relation is not generally determined by a family of projections unless an appropriate lossless join/dependency condition holds;
2. marginal problems: compatible or matching lower-order marginals/projections need not determine a unique global object;
3. contextuality/local-to-global obstruction frameworks: locally consistent data may fail to determine or admit a global section/model;
4. CSP/database decomposability and hypergraph acyclicity: structural conditions determine when local consistency suffices globally;
5. GC-I's own proper-projection parity witness: parity is exactly the canonical finite example where all strict coordinate projections erase the global distinction.

Thus moving GC-I parity from state coordinates to realization-resource certificates does not create a new theorem. It is a relabeling of the same projection irreducibility structure.

## Stronger no-go

### Proposition 123.2 — Static feasible-relation reduction

STATUS: PROVED.

Any finite typed realization problem whose scientific content is exhausted by a static feasible set F subset X_R x X_I x X_A x X_L is, after forgetting the meanings of the coordinate labels, an ordinary finite relation. Questions of whether lower-dimensional projections determine F, whether local certificates glue globally, or whether projection joins introduce spurious tuples are therefore instances of relational reconstruction/join problems.

Proof. The identity map from realization certificates to tuples of a finite relation preserves feasibility and every coordinate projection. Hence every theorem depending only on F and its projections is a theorem about finite relations. QED.

Consequently, a GC-II breakthrough cannot come merely from discovering a static higher-order interaction among R,I,A,L if the interaction is fully represented by the feasible relation itself.

## Edge and invariance checks

- Dimensions/domains: all coordinates are binary and dimensionless in this witness; no invalid heterogeneous arithmetic is used except parity on labels chosen specifically as binary indicators.
- Degenerate projections: the empty projection is trivially equal and carries no information; all 14 nonempty proper projections were checked.
- Monotonicity: not assumed. The parity relations are intentionally not upward closed, so this witness targets compatibility/reconstruction rather than free-wasting resource feasibility.
- Composition: no additive or multiplicative composition law is assumed.
- Relabeling invariance: permuting R,I,A,L leaves the parity construction unchanged up to isomorphism.
- Counterexample search: the witness itself is an exact counterexample to the claim that complete agreement of every proper coordinate projection determines the joint feasible set.
- Reduction to known theory: direct, via finite relations and projection/join reconstruction.

## Consequence for Omega_G

A quantity based only on discrepancy between a full feasible relation and a reconstruction from its proper projections is not a new Generative Novelty Gap. Depending on the chosen discrepancy it becomes a relational reconstruction loss, marginal incompatibility/nonuniqueness measure, contextuality-type obstruction, or projection irreducibility statistic.

STATUS: FALSIFIED as standalone novelty.

## What survives

The static-feasible-set route is exhausted. A surviving target must involve structure not preserved by the reduction to an unstructured finite relation. The next defensible target is **implementation-linked compositional realization**:

- certificates must refer to the same recursively executable implementation, not merely coexist as feasible tuples;
- sequential composition must impose a law on hidden implementation identity/state;
- the proposed obstruction must survive quotienting by full operational equivalence;
- it must not reduce to process algebra, automata/transducer composition, scheduling, dynamic programming, communication complexity, contextuality, or ordinary resource-theory composition;
- it must yield a quantitative theorem rather than a restatement of non-factorization.

This target is OPEN. No breakthrough is claimed.

## Status

- minimal sufficient operational state as standalone novelty: already FALSIFIED by Audit 094
- generic typed realization region: already FALSIFIED by Audit 095
- generic typed multiresource lower-bound form: already FALSIFIED by Audit 096
- all-proper-projections-equal/full-feasible-set-different witness: PROVED
- exact 14-projection checker: NUMERICALLY SUPPORTED / exact finite verification, 0 mismatches
- static higher-order resource compatibility as standalone GC-II novelty: FALSIFIED
- projection-reconstruction Omega_G as standalone novelty: FALSIFIED
- implementation-linked compositional realization obstruction beyond known process/resource theories: OPEN

## Reproduction

Run:

```bash
python experiments/gc2_full_projection_compatibility_audit.py
```

Frozen output summary is stored in:

`results/gc2_full_projection_compatibility_audit.json`
