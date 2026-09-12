# GC-II Audit 097 — Proper Resource-Projection Compatibility Is Incomplete but Known

## Status

- Proper-projection indistinguishability construction: **PROVED**.
- Exact Boolean exhaustive check for dimensions 3–7: **NUMERICALLY SUPPORTED / exact enumeration**.
- Claim that matching all proper R/I/A/L resource projections determines the full joint realization set: **FALSIFIED**.
- Claim that the residual incompatibility is by itself a GC-II breakthrough: **FALSIFIED**.
- Stronger operational obstruction surviving complete joint-realization information: **OPEN**.

## Question

Audit 096 left a candidate in which ordinary resource summaries agree but one implementation cannot jointly realize certificates that are individually compatible. Does agreement of every proper resource projection force agreement of the full realization set?

No.

## Exact separation theorem

Let n >= 2 and let the typed realization coordinates be binary. Define

E_n = {x in {0,1}^n : sum_i x_i = 0 (mod 2)},
O_n = {x in {0,1}^n : sum_i x_i = 1 (mod 2)}.

For every proper coordinate subset J ⊊ {1,...,n},

pi_J(E_n) = pi_J(O_n) = {0,1}^{|J|},

while E_n != O_n and E_n ∩ O_n = empty.

### Proof

Fix a proper J and any assignment y on J. At least one coordinate k is unobserved. Choose arbitrary values for every other unobserved coordinate. The final bit x_k can then be selected uniquely to make total parity even, and selected with the opposite value to make total parity odd. Hence y extends to an element of both E_n and O_n. Since y was arbitrary, both projections are the full cube. The global sets are disjoint because no binary vector has both even and odd parity. QED.

For GC-II's four typed axes, n=4 gives two systems with identical R, I, A, L singleton projections, identical pairwise projections, and identical three-coordinate projections, yet different complete joint realization sets.

Thus even the strengthened criterion

forall proper J: pi_J(M_A) = pi_J(M_B)

does not imply

M_A = M_B.

## Why this does not establish GC-II novelty

The obstruction is a projection/reconstruction phenomenon. Relational database theory formalizes exactly when a relation can be recovered losslessly from projections through join dependencies and projection-join normal form. Marginal/contextuality theory likewise studies whether locally compatible contexts admit a single global object. Therefore a GC theorem whose mathematical content is only that all proper projections fail to determine a global feasible relation is a relabeling of established local-to-global reconstruction structure.

The parity construction is particularly diagnostic because it is the same structural mechanism already encountered in GC-I projection irreducibility. Reinterpreting its coordinates as R/I/A/L does not create a new operational law.

## Novelty gate strengthened

A Paper-II breakthrough cannot be certified by any of the following alone:

1. different full realization sets with equal singleton resource summaries;
2. equal pairwise resource Pareto projections;
3. equal k-wise projections for every fixed k < n;
4. even equality of **all proper coordinate projections**.

Any claimed `Omega_G` based only on the discrepancy between a joint relation and reconstruction from its proper projections must first be treated as a join/marginal/contextuality defect, not as a new GC invariant.

## Consequence for the search program

The cross-model joint-compatibility route survives only if the obstruction uses additional operational structure not contained in a static feasible relation: for example, a typed implementation certificate with transformation/composition constraints whose failure cannot be represented merely as a missing global tuple, join dependency, marginal inconsistency, CSP compatibility condition, or standard multi-resource lower bound.

The next attack should therefore ask whether **composition-compatible realizability** can separate systems after their complete static realization relations are identical. If the complete operational composition law is also included, then an extensional equality theorem may again make separation impossible; that possibility should be tested before introducing a new invariant.

## Edge and reduction checks

- n=1: excluded from the nontrivial proper-projection claim; the only proper projection is empty.
- n>=2: proof works unchanged.
- Degenerate projections: empty projection agrees trivially.
- Monotonicity: no monotonicity assumption is needed; parity sets are intentionally non-upward-closed. If GC realization sets require free disposal/upward closure, this example must not be overclaimed for that subclass.
- Invariance: coordinate permutations preserve the construction.
- Composition: not addressed by this theorem; this is precisely why the result is a no-go for the static route rather than a breakthrough.
- Dimensions: coordinates are abstract binary realization indicators here; no physical unit equation is asserted.

## Prior-art collision notes

- Database lossless-join theory: a decomposition is lossless exactly when joining the projections reconstructs the original relation; projection-join normal form/join dependencies directly target this issue.
- Marginal/contextuality frameworks: existence of a global model compatible with local contexts is a central established question; 2026 contextuality work continues to formulate noncontextuality through existence of a joint distribution compatible with measurable contexts.
- Therefore the local-versus-global compatibility phenomenon is **IMPORTED/KNOWN structure**, although the explicit GC typed-coordinate restatement above is proved here for use as a falsification gate.

## Falsification decision

**Decisive:** matching every proper typed-resource projection is not enough to identify joint realizability, but the resulting residual is not a GC-II breakthrough because it reduces directly to established projection/join/marginal compatibility structure.
