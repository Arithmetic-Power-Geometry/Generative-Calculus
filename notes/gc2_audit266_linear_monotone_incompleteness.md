# GC-II Audit 266 — Linear scalarisations are not a complete typed convertibility certificate

## Status

- Typed Pareto boundary kernel from Audit 265: **PROVED / IMPORTED-KNOWN mechanism**.
- Completeness of one fixed positive linear scalarisation: **FALSIFIED** (Audit 265).
- Completeness of the entire family of positive linear scalarisations for componentwise typed budgets: **FALSIFIED**.
- Full Pareto/upward-set certificate for finite additive nonnegative typed semantics: **PROVED** by Audit 265.
- Generic supported/unsupported Pareto-point mechanism: **IMPORTED/KNOWN** from multiobjective optimisation.
- Smaller GC-specific complete monotone basis under additional structural hypotheses: **OPEN**.

## Setting

Let a boundary transition have attainable nonnegative typed costs `Y subset R_+^d`.  The operational budget semantics accepts budget `b` iff there exists `y in Y` with `y <= b` componentwise.  Its canonical finite certificate is therefore the nondominated set `Min(Y)` (equivalently its upward closure).

A tempting compression is to retain every positive linear scalar value

`h_Y(w) = min_{y in Y} <w,y>`, for w in R_+^d \ {0}`.

This is much stronger than retaining one scalarisation, but it is still incomplete for discrete/nonconvex typed semantics.

## Exact counterexample

Take two-dimensional typed costs

`Y = {(0,3),(3,0)}`

and

`Z = {(0,3),(2,2),(3,0)}`.

The point `(2,2)` is nondominated in `Z`, so the budget `b=(2,2)` distinguishes the systems:

- `Z` is feasible under `(2,2)`;
- `Y` is not feasible under `(2,2)`.

Nevertheless every nonnegative linear scalarisation agrees:

`h_Y(w)=h_Z(w)=3 min(w_1,w_2)`.

Proof: for `w_1 <= w_2`, endpoint `(3,0)` has value `3w_1`, while `(2,2)` has value `2w_1+2w_2 >= 4w_1 >= 3w_1`.  The case `w_2 <= w_1` is symmetric.  Zero components are included.  Hence `(2,2)` is an unsupported nondominated point invisible to all positive weighted sums.

Therefore

`[forall w>=0: h_Y(w)=h_Z(w)]` does **not** imply equality of typed budget behaviour.

Equivalently, the support-function-like lower envelope of positive linear prices sees the lower convex hull, not the full discrete Pareto/upward set.

## Consequence for GC-II

A complete typed capability-accounting criterion cannot, without additional convexity/exchange assumptions, be reduced to any claim of the form “check all linear R/I/A/L prices”.  Audit 265's Pareto kernel is not merely an implementation convenience: discrete unsupported tradeoffs contain operational information that all linear prices can erase.

This blocks a superficially attractive route for item (6), a complete convertibility criterion via dual monotones.  Linear monotones become complete only after adding a defensible structural assumption (for example an appropriate convexification/randomisation/exchange semantics), or by enriching the separating family beyond linear weighted sums (componentwise budget/epsilon-constraint probes already suffice in the finite setting).

## Checks

The companion verifier checks exact integer weights on a large grid, exhaustive finite budget discrimination on `[0,4]^2`, nondominance of `(2,2)`, and the symbolic case split proving equality for every nonnegative real weight vector.  The finite grid is only a regression test; the all-weight statement is analytic.

## Prior-art boundary

The supported-versus-unsupported nondominated-point phenomenon is established multiobjective-optimisation theory.  Weighted sums generally recover supported efficient points and can miss unsupported efficient points in discrete/nonconvex feasible sets.  Accordingly this audit is a GC-II no-go/correctness boundary, not a claim that the underlying optimisation fact is new.

## Next target

Determine the weakest operational hypothesis under which the typed Pareto kernel admits a smaller complete certificate.  Candidate hypotheses to attack separately: convex closure via admissible randomisation, exact resource exchange rates, bounded treewidth/dependency width, and typed generator decomposability.  None is assumed here.
