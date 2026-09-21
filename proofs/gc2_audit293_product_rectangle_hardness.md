# GC-II Audit 293 — two interval dimensions restore hardness

## Scope

This audit tests the open composition question left by Audit 292. Audit 292 proves exact greedy tractability when every feasible-action set is an interval in one common operational order. The question is whether a small product extension preserves that tractability.

## Finite operational accounting model

Let the attainable states be a finite set `Y` embedded in an ordered product `X1 x X2`. For decoder action `a`, define its tolerance-feasible set

`B_e(a) = {y in Y : ell(y,a) <= e}`.

Assume every feasible set is a Cartesian product of two intervals:

`B_e(a) = Y intersect (I_a x J_a)`.

Thus each coordinate separately has exactly the one-dimensional interval structure used in Audit 292.

By Audit 290, minimum worst-case-e-faithful accounting is exactly the minimum number of feasible-action sets whose union covers `Y`. Under the displayed restriction, this is precisely discrete point cover by a supplied family of axis-aligned rectangles.

## Theorem 293A — product-interval hardness

For explicit finite incidence input, optimal worst-case capability accounting remains NP-hard even when every feasible-action set is a product of only two intervals.

### Proof

An instance of geometric set cover by a supplied family of axis-aligned rectangles consists of a finite point set `P` in the plane and a finite rectangle family `R`. Construct the accounting instance with `Y=P`, one decoder action `a_R` per rectangle, tolerance `e=0`, and binary loss

`ell(p,a_R)=0` iff `p in R`, and `1` otherwise.

Then `B_0(a_R)=P intersect R`, a product of an x-interval and a y-interval restricted to `Y`. By Audit 290, the accounting optimum equals the rectangle-cover optimum exactly. Therefore NP-hardness of the geometric rectangle-cover problem transfers immediately. QED.

A stronger imported result is known: minimum cover of planar points by a supplied family of axis-aligned fat rectangles is APX-hard (Chan and Grant, Computational Geometry 47(2), 2014, 112–124, DOI 10.1016/j.comgeo.2012.04.001). Hence the restriction above does not merely inherit arbitrary SET COVER through an unconstrained incidence encoding; hardness survives strong two-dimensional geometric structure.

## Corollary 293B — Audit-292 tractability is not closed under two-coordinate product extension

One common interval order is polynomially solvable by Audit 292. Replacing it by two ordered coordinates and rectangular feasible sets can already be NP-hard. Consequently no theorem of the form

`constant number of interval-structured interface coordinates => exact polynomial accounting`

can hold in full generality unless P=NP.

This is a composition obstruction: two individually simple ordered interface dimensions can jointly induce computationally hard capability accounting.

## Explicit greedy collision

The exact verifier includes a 3x3 grid with seven rectangular actions. A natural two-dimensional analogue of the Audit-292 rule — take the lexicographically first uncovered target and choose a containing rectangle covering the largest number of currently uncovered targets — uses five actions, while the exact optimum is three. This is not the hardness proof; it is a concrete warning that the one-dimensional exchange argument does not lift mechanically.

## Boundary / edge audit

- Dimension 1: Audit 292 greedy theorem applies; this audit does not weaken it.
- Dimension 2: hardness is imported through geometric rectangle cover.
- Empty target set: optimum is zero.
- Universal feasible rectangle: optimum is one for nonempty `Y`.
- Duplicate/nested rectangles: harmless; they do not affect the reduction.
- Binary loss and `e=0` suffice; approximation geometry is not required for the hardness.
- Each feasible set is independently interval-convex in both coordinates; coordinatewise convexity therefore does not imply global tractability.
- This audit does **not** claim hardness for every more restricted rectangle family (unit squares, anchored rectangles, bounded ply, etc.); those require separate collision checks.
- The generic geometric hardness is IMPORTED/KNOWN. The GC-II result is its exact operational consequence under the Audit-290 accounting equivalence.

## Status

- Audit-292 one-order interval tractability: **PROVED**.
- Two-interval-product accounting NP-hardness: **PROVED via reduction + IMPORTED/KNOWN geometric hardness**.
- Generic geometric rectangle-cover hardness: **IMPORTED/KNOWN**.
- Closure of Audit-292 tractability under unrestricted two-coordinate product composition: **FALSIFIED unless P=NP**.
- Natural lexicographic/max-new-coverage rectangle greedy: **FALSIFIED** by exact finite counterexample.
- Tractable product subclasses characterized by independently measurable operational structure: **OPEN**.

## Consequence for Paper II

The useful boundary is now sharper: low-dimensionality alone is not a sufficient capability-accounting resource. Paper II should distinguish (i) one common operational order, where interval feasibility yields an exchange theorem, from (ii) multiple jointly active ordered interface dimensions, where their interaction can restore hard covering geometry. Any positive compositional theorem must charge or constrain this interaction rather than merely count local dimensions.
