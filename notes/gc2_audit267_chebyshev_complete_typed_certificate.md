# GC-II Audit 267 — Complete nonlinear typed-budget certificate

## Status

- Weighted Chebyshev / max-ratio scalarization: **IMPORTED/KNOWN mechanism**.
- Exact completeness for GC-II finite typed additive nonnegative budget semantics: **PROVED**.
- Linear-price completeness: **FALSIFIED** (Audit 266).
- Finite smaller GC-specific basis without bounded/discretized budgets: **OPEN**.

## Setup

Let `Y` be the nonempty set of attainable nonnegative typed cost vectors for an operational task. Its upward feasibility set is

\[
U(Y)=\{b\in\mathbb R_+^d:\exists y\in Y,\ y\le b\},
\]

where inequalities are componentwise. For a strictly positive budget vector `b in R_{>0}^d`, define the max-ratio certificate

\[
\rho_Y(b)=\inf_{y\in Y}\max_i \frac{y_i}{b_i}.
\]

For zero budget coordinates use the extended convention `y_i/0 = 0` if `y_i=0`, and `+infinity` otherwise. This yields the same theorem on `R_+^d`.

## Theorem 267.1 — exact budget test

For every nonnegative budget `b`,

\[
\boxed{b\in U(Y)\iff \rho_Y(b)\le 1.}
\]

### Proof

If `b in U(Y)`, some attainable `y` satisfies `y_i<=b_i` for every coordinate. Under the extended zero-coordinate convention every ratio is at most one, hence `rho_Y(b)<=1`.

Conversely, for finite attainable sets (the present exact finite-world semantics), `rho_Y(b)<=1` is attained by some `y`, and `max_i y_i/b_i<=1` implies `y_i<=b_i` coordinatewise, including zero coordinates by the extended convention. Hence `b in U(Y)`.

For infinite sets the converse requires attainment/closure; without it, `inf<=1` at equality can be approached without a feasible point. Therefore the unrestricted infinite version is **CONDITIONAL** on attainment (or must be formulated using the closed upward hull).

## Corollary 267.2 — complete nonlinear scalar family

For finite attainable sets `Y,Z`,

\[
\boxed{U(Y)=U(Z)\iff [\rho_Y(b)\le1 \Longleftrightarrow \rho_Z(b)\le1\ \forall b\in\mathbb R_+^d].}
\]

Thus a family of nonlinear scalar tests is complete for typed operational convertibility even though Audit 266 proves that the entire family of nonnegative linear prices is incomplete.

Equality of the numerical functions `rho_Y=rho_Z` is sufficient but stronger than necessary; completeness needs only the threshold predicates at one. This distinction prevents an inflated claim.

## Corollary 267.3 — finite certificate on bounded integer budgets

If all relevant budgets lie in the finite grid `B=prod_i {0,...,M_i}`, then the bit-vector

\[
\chi_Y=(1[\rho_Y(b)\le1])_{b\in B}
\]

is a finite complete certificate for all budgeted-closure queries on that grid. This is exact but may be exponentially large in dimension/bit range, so it is not yet the sought compact GC-specific monotone basis.

## Edge and invariance audit

- Empty attainable set: define `rho=+infinity`; no finite budget is feasible.
- Zero vector attainable: `rho=0` for every nonzero budget and feasible for zero budget.
- Zero budget coordinates: handled by the extended ratio convention.
- Positive coordinate rescaling `y_i -> a_i y_i`, `b_i -> a_i b_i` leaves every ratio unchanged.
- Common positive global cost scaling also leaves `rho` unchanged when budget is scaled coherently.
- Adding a dominated attainable vector cannot improve `rho`; therefore the certificate descends to the Pareto quotient of Audit 265.
- Independent additive composition does not generally make `rho` additive; no such claim is made.
- Dimension/domain: `rho` is dimensionless because each numerator and denominator has the same typed unit.

## Audit-266 collision

For `Y={(0,3),(3,0)}` and `Z={(0,3),(2,2),(3,0)}`, all nonnegative linear minimum prices coincide, but at `b=(2,2)`:

\[
\rho_Y(b)=3/2>1,\qquad \rho_Z(b)=1.
\]

The nonlinear max-ratio family therefore detects the unsupported Pareto point missed by every linear price.

## Novelty boundary

Weighted Chebyshev / achievement scalarizing functions and their ability to recover nondominated solutions are established multiobjective-optimization machinery. The generic scalarization is not claimed as new mathematics. The GC-II result is the exact identification of a complete nonlinear certificate family for its typed operational budget semantics, together with the sharp contrast to Audit 266's linear-price no-go.

## Remaining target

The scientifically stronger open problem is a **compact structured** certificate whose size is controlled by operational structure (generator coupling, treewidth/acyclicity, interface width, or another intrinsic parameter), rather than by enumerating the full Pareto/upward set or all budgets.
