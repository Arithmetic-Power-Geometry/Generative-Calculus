# GC-II Audit 250 — Exact boundary for type-separable capability accounting

Status: **PROVED for the stated independent asynchronous generator class; generic decomposition mechanism IMPORTED/KNOWN; GC-specific novelty OPEN.**

## Setup
Let the operational state factor as
\[
X=\prod_{j=1}^m X_j,
\]
where the coordinates may be read as typed GC coordinates (e.g. R/I/A/L, or any finer typed decomposition). Assume:

1. every primitive operation acts on exactly one coordinate j;
2. its enabling condition depends only on that coordinate;
3. its successor update changes only that coordinate;
4. its nonnegative cost depends only on that local transition;
5. operations on different coordinates may be interleaved arbitrarily (no shared prerequisite, budget, synchronization, or state-dependent cross-type effect).

Let d_j(x_j,S_j) be the minimum local cost to reach S_j subset X_j, with +infinity if unreachable.

## Theorem 250.1 — rectangular target sufficiency
If the capability target is a nonempty Cartesian rectangle
\[
F=F_1\times\cdots\times F_m,
\]
then the exact global minimum capability cost is
\[
\boxed{V_F(x)=\sum_{j=1}^m d_j(x_j,F_j).}
\]
(extended-real convention: any +infinity summand makes the sum +infinity.)

### Proof
Any global path ending in F must, after projection onto coordinate j, contain a valid local path from x_j to F_j. Since every primitive cost belongs to exactly one coordinate, the global path cost is at least the sum of the local optimum costs. Conversely, choose an optimal (or epsilon-optimal when minima are not attained) local path for every coordinate and concatenate/interleave them. Local enabling is unaffected by other coordinates, so this is a valid global path into F and its cost is the sum of local costs. Taking infima proves equality.

This also proves order invariance across distinct types under the stated assumptions.

## Theorem 250.2 — rectangle is necessary for universal nonnegative additive value factorization
Fix a nonempty target F subset X. Suppose that for **every** independent asynchronous generator system in the class above, including the degenerate system with no operations, its exact capability value admits a nonnegative extended-real additive factorization
\[
V_F(x)=\sum_j v_j(x_j),\qquad v_j:X_j\to[0,+\infty].
\]
Then F must be a Cartesian rectangle.

### Proof
Use the degenerate no-operation system. Then V_F(x)=0 exactly on F and +infinity outside F. For a sum of nonnegative local terms,
\[
V_F(x)=0 \iff v_j(x_j)=0\ \forall j.
\]
Hence its zero set is
\[
\prod_j Z_j,\qquad Z_j=\{a:v_j(a)=0\}.
\]
But the zero set is F. Therefore F=prod_j Z_j is rectangular.

Combining Theorems 250.1 and 250.2 gives an exact **universal separability boundary** for this restricted generator class:

\[
\boxed{\text{universal exact additive typed accounting}\iff\text{capability target is rectangular}.}
\]

This is stronger than Audit 249's single XOR/equality collision: it identifies the structural condition that rescues exact typed additivity, and proves that without it no theorem based solely on independent typed dynamics can be universally valid.

## Edge/degenerate cases
- Empty target: V=+infinity everywhere; exclude it from the nonempty rectangle theorem or handle it by a separate convention.
- Universal target: F=X is rectangular and V=0.
- Singleton target: rectangular iff it is the product of its singleton coordinate projections; exact additivity follows.
- Unreachable local target: corresponding d_j=+infinity, so both sides are +infinity.
- Zero-cost local operations: allowed; proof uses nonnegative rather than strictly positive costs.
- Negative costs: excluded; they can destroy the zero-set argument and minimum-cost well-posedness.
- Shared budgets, synchronized actions, cross-coordinate prerequisites/effects, or coupled costs: outside the theorem; they can destroy sufficiency even for rectangular F.

## Relation to GC-II accounting
Audit 249 showed that independent R/I/A/L dynamics are insufficient when the target couples types. Audit 250 now isolates the exact rescue condition for the ideal independent class. Therefore a defensible GC-II law must account for two logically distinct interaction sources:

- **generator coupling** (cross-type preconditions/effects/costs/shared budgets), and
- **target coupling** (failure of F to be rectangular in the proposed typed coordinates).

Any proposed Omega_G <= F(Delta R,Delta I,Delta A,Delta L) that claims exact separability must either prove both couplings absent or include an interaction term/structure that represents them.

## Novelty collision
The proof mechanism is a standard product/decomposition principle: factored planning/MDP literature exploits independent or weakly coupled dynamics and additive objectives, and generic dynamic-programming decomposition is established. Accordingly:

- rectangular-target sufficiency: **PROVED / generic mechanism IMPORTED-KNOWN**;
- necessity for universal nonnegative additive factorization: **PROVED**;
- the equivalence as a generic product-system fact: **not claimed as a GC novelty**;
- a GC-specific, computable interaction invariant that quantitatively controls departure from this boundary: **OPEN**.

## Next attack
Define a target-coupling quantity that is not merely a restatement of V_F, test invariance under typed relabeling and operational congruence, and ask whether it combines with generator-coupling structure to yield a quantitative lower/upper bound on Omega_G. Candidate constructions must be collision-tested against CSP/factor-graph width, communication complexity, database join/decomposability, contextuality/marginal problems, and factored planning before any novelty claim.
