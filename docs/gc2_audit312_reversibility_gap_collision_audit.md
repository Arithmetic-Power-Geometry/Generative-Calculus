# GC-II Audit 312 — reversibility-gap invariant: exact finite operational audit

## Purpose
This audit attacks Paper-II item (8): define and collision-test a reversibility-gap invariant. The objective is to retain only a mathematically defensible object and explicitly reject interpretations that fail.

## Setting
Let `Z` be a finite operational state space with admissible directed transformations `e : z -> z'` carrying nonnegative scalar cost `c(e) >= 0` in one fixed declared unit. Define the optimal directed conversion cost

`d(x,y) = inf_{pi:x->y} sum_{e in pi} c(e)`,

with `d(x,y)=+infinity` when no admissible path exists and `d(x,x)=0`.

For finite graphs the infimum is a minimum whenever a path exists. Nonnegative costs imply the directed triangle inequality

`d(x,z) <= d(x,y)+d(y,z)`.

This is a directed shortest-path/quasi-metric construction and is IMPORTED/KNOWN mathematics.

## Candidate invariant
For a pair with finite directed costs and positive round-trip cost, define the dimensionless normalized reversibility asymmetry

`Gamma_rev(x,y) = |d(x,y)-d(y,x)| / (d(x,y)+d(y,x))`.

If both directed costs are zero, set `Gamma_rev(x,y)=0` by convention. If exactly one direction is unreachable, set `Gamma_rev=1`. If both directions are unreachable, leave the pair **undefined** rather than pretending that mutual impossibility is perfect reversibility.

Also retain the dimensional round-trip burden

`B_rev(x,y) = d(x,y)+d(y,x)`.

The pair `(B_rev,Gamma_rev)` is the recommended accounting object. `Gamma_rev` alone is deliberately not claimed complete.

## Proposition 312.1 — basic invariant properties
Whenever defined:

1. `0 <= Gamma_rev <= 1`.
2. `Gamma_rev(x,y)=Gamma_rev(y,x)`.
3. Positive rescaling of all costs, `c -> lambda c` with `lambda>0`, leaves `Gamma_rev` unchanged.
4. Relabeling operational states and edges by an isomorphism preserving admissibility and edge costs leaves `Gamma_rev` unchanged.
5. `Gamma_rev=0` iff the two finite optimal directed costs are equal (including the zero/zero convention).
6. For finite nonnegative directed costs, `Gamma_rev=1` iff exactly one directed optimal cost is zero and the other is positive. With the extended convention it is also 1 when exactly one direction is unreachable.

**Status:** PROVED directly from the definition. No novelty claim.

## Proposition 312.2 — two-number completeness for a finite pair
Let

`a=d(x,y)`, `b=d(y,x)`, `B=a+b>0`, `G=|a-b|/B`.

Then the unordered pair of directed costs is recovered exactly as

`{a,b} = { B(1-G)/2, B(1+G)/2 }`.

If the orientation (which direction is cheaper) is additionally stored as one sign bit `sigma=sign(b-a)`, then `(B,G,sigma)` recovers the ordered pair `(a,b)` exactly.

**Status:** PROVED. This is elementary algebra, not a new theorem.

## Collision tests: what Gamma_rev does NOT mean

### Collision A — zero asymmetry is not free reversibility
System 1: `d(x,y)=d(y,x)=0`.

System 2: `d(x,y)=d(y,x)=100`.

Both have `Gamma_rev=0`, but their round-trip burdens are 0 and 200. Therefore

`Gamma_rev=0 => operationally free reversible conversion`

is **FALSIFIED**.

### Collision B — equal Gamma does not determine burden
Pairs `(1,3)` and `(10,30)` both give

`Gamma_rev = 1/2`,

while `B_rev` equals 4 and 40. Thus the normalized invariant intentionally removes absolute scale.

### Collision C — mutual impossibility is not reversibility
If `d(x,y)=d(y,x)=infinity`, a naive infinity/infinity normalization is indeterminate. Assigning zero would conflate disconnected states with freely interconvertible states. Therefore `Gamma_rev` is undefined on mutually unreachable pairs.

### Collision D — one-way reachability is qualitatively maximal
If `d(x,y)<infinity` and `d(y,x)=infinity`, the extended value `Gamma_rev=1` records maximal directional asymmetry. It does **not** quantify how costly the reachable direction is; `B_rev` is infinite in the extended sense.

### Collision E — pairwise symmetry does not imply zero cycle circulation
Even if one examines a larger directed system through pairwise values, a single scalar per pair cannot encode all path/cycle structure, alternative routes, or budget-dependent admissibility. `Gamma_rev` is therefore a pairwise invariant, not a complete invariant of an operational network.

**Status:** claims of completeness beyond a two-state directed-cost pair are REJECTED.

## Proposition 312.3 — round-trip symmetrization
Define

`D_sym(x,y)=d(x,y)+d(y,x)`

when both terms are finite. On each strongly connected finite-cost component:

- `D_sym >= 0`;
- `D_sym(x,y)=D_sym(y,x)`;
- `D_sym(x,z) <= D_sym(x,y)+D_sym(y,z)`.

Hence `D_sym` is a pseudometric. It becomes a metric exactly when no distinct pair has zero cost in both directions.

### Proof
Symmetry and nonnegativity are immediate. Apply the directed triangle inequality to `d(x,z)` and separately to `d(z,x)`, then add. Identity of indiscernibles can fail precisely under zero-cost mutual conversion. QED.

**Status:** PROVED; directed-metric symmetrization is IMPORTED/KNOWN mathematics.

## Composition audit
Suppose independent product systems have additive directed optimal costs:

`a = a1+a2`, `b=b1+b2`.

Then round-trip burden is additive:

`B = B1+B2`.

But normalized asymmetry is generally **not additive**:

`Gamma = |(a1-b1)+(a2-b2)|/(B1+B2)`.

Opposite directional asymmetries can cancel. Example:

- component 1: `(a1,b1)=(1,3)`, `Gamma1=1/2`;
- component 2: `(a2,b2)=(3,1)`, `Gamma2=1/2`;
- product/additive composition: `(a,b)=(4,4)`, `Gamma=0`.

Therefore `Gamma_rev` can decrease under independent composition and is not a monotone under arbitrary composition.

**Status:** additivity and monotonicity-under-composition claims — FALSIFIED by exact counterexample.

## Budget dependence
If admissibility itself depends on resource/information/interface/rule budgets, define `d_theta(x,y)` only after fixing the operational regime `theta`. Comparing `Gamma_rev` across regimes without fixing cost units and admissibility semantics is invalid. A capability upgrade may lower one directed conversion cost, raise another through changed constraints, or make a formerly impossible reverse path possible.

Thus reversibility accounting must be indexed by the same declared operational closure used elsewhere in GC-II.

## Prior-art collision audit
The construction collides with established work on:

- directed shortest-path distances and quasi-metrics;
- symmetrization of asymmetric distances;
- reversible/irreversible resource conversion;
- thermodynamic forward/reverse costs;
- resource-theoretic conversion rates and asymmetry.

Therefore:

- `d` as optimal directed conversion cost — IMPORTED/KNOWN;
- `d+d^op` as a symmetric pseudometric — IMPORTED/KNOWN mechanism;
- normalized directional asymmetry — elementary/known-style construction, NOT claimed novel;
- GC-II use as a typed operational diagnostic — DERIVED APPLICATION;
- a new universal reversibility theorem — REJECTED;
- a complete network-level reversibility invariant — OPEN.

## Dimensional/domain checks
- `d` and `B_rev` carry the declared cost unit.
- `Gamma_rev` is dimensionless.
- Costs from heterogeneous resources cannot be added until a scalarization/exchange rule is independently declared. For genuinely vector-valued costs, use Pareto/frontier objects rather than silently summing dimensions.
- Negative edge costs are excluded; otherwise shortest-path semantics and budget interpretation require a different treatment and negative cycles can destroy finiteness.
- Zero-cost cycles are allowed; they produce pseudometric equivalence classes.
- Unreachable states require the explicit extended-value conventions above.

## Status ledger
- Pairwise normalized reversibility asymmetry `Gamma_rev` — DEFINITION FIXED for scalar-cost regimes.
- Bounds, symmetry, scale invariance, relabeling invariance — PROVED.
- `(B_rev,Gamma_rev,orientation)` recovers finite ordered two-way conversion costs — PROVED.
- `Gamma_rev=0` as sufficient for free reversibility — FALSIFIED.
- `Gamma_rev` additive or composition-monotone — FALSIFIED.
- Round-trip symmetrization as pseudometric — PROVED / IMPORTED-KNOWN mechanism.
- Mutual-unreachability normalization — correctly left UNDEFINED.
- Vector-resource, stochastic, approximate, and dynamic reversibility invariants — OPEN.
- Novel universal GC-II reversibility theorem — OPEN.

## Paper-II consequence
The safe result is not to advertise `Gamma_rev` as a breakthrough theorem. The scientifically useful conclusion is that reversibility has at least two irreducible accounting coordinates even in the simplest scalar finite regime: absolute round-trip burden and directional asymmetry. A single normalized gap provably collides. This gives a disciplined invariant pair for subsequent AI/robotics/distributed-system experiments and prevents a false scalar-completeness claim.
