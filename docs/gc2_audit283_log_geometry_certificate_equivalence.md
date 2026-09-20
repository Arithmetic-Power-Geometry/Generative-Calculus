# GC-II Audit 283 — Log-geometry equivalence for multiplicative capability certificates

## Scope

This audit does not claim a new metric-entropy theorem. It identifies the exact geometric object already implicit in Audits 273–282 and fixes the certificate language before further structural compression claims.

## Setup

Let `Y` be a finite set of strictly positive typed cost vectors in `R_{>0}^d`. For `alpha >= 1`, an attainable internal alpha-certificate is a subset `S subseteq Y` such that for every `y in Y` there is `s in S` with

` s_i <= alpha y_i  for every coordinate i. `

Write `C_alpha(Y)` for the minimum cardinality of such a certificate.

Define log coordinates `z = log y` componentwise and the directed max displacement

`delta_+(u,v) = max_i (u_i-v_i)`.

Then define the directed internal radius-`rho` cover relation

`u ->_rho v  iff  delta_+(u,v) <= rho`.

## Proposition 283.1 — exact equivalence

For `rho = log alpha`,

` s_i <= alpha y_i for all i`

if and only if

` delta_+(log s, log y) <= rho`.

Therefore

`C_alpha(Y) = N^int_{+,log alpha}(log Y)`,

where the right side is the minimum cardinality of an internal directed cover under `delta_+`.

### Proof

For every coordinate,

`s_i <= alpha y_i`

is equivalent, because all entries are positive, to

`log s_i - log y_i <= log alpha`.

Taking the maximum over coordinates gives exactly the stated directed-radius condition. Minimizing over attainable centers gives the equality of certificate and internal-cover cardinalities. QED.

## Proposition 283.2 — unit invariance

Independent positive changes of units `y_i -> c_i y_i`, `c_i>0`, translate all log vectors by the same coordinatewise vector `(log c_i)_i`. Hence every difference `log s_i-log y_i`, every directed radius, and `C_alpha(Y)` are unchanged.

Status: PROVED.

## Proposition 283.3 — composition inequality for product families

Let `Y subset R_{>0}^d` and `Z subset R_{>0}^k`. Under concatenated independent composition

`Y x Z = {(y,z): y in Y, z in Z}`,

one has

`C_alpha(Y x Z) <= C_alpha(Y) C_alpha(Z)`.

### Proof

Take minimum alpha-certificates `S` and `T`. For any `(y,z)` choose `s in S` alpha-covering `y` and `t in T` alpha-covering `z`. Then `(s,t)` alpha-covers `(y,z)` coordinatewise. Thus `S x T` is a certificate of the displayed size. QED.

The inequality can be strict; equality is not claimed.

Status: PROVED.

## Proposition 283.4 — monotonicity in tolerance

If `1 <= alpha <= beta`, then

`C_beta(Y) <= C_alpha(Y)`.

Status: PROVED.

## Boundary cases

* `alpha=1`: the construction reduces to exact coordinatewise domination by attainable centers. On a Pareto antichain every point must be retained.
* Empty `Y`: use certificate size zero by convention.
* Duplicate vectors: quotienting duplicates does not change the cover problem.
* Zero coordinates: logarithms are undefined. Audits 275–276 already show that exact zero support must be handled as a separate symbol/support stratum. The present theorem is deliberately restricted to the strictly positive stratum.
* Infinite coordinates: excluded from this finite positive audit.

## Consequence for Audits 277–282

The exponential families in Audits 277–282 are directed packings in log capability space: distinct attainable points lie outside each other's radius-`log alpha` directed balls. Their certificate lower bounds are therefore geometric packing obstructions, regardless of how local the generating operational graph appears.

This explains why gate arity, controller-state count, treewidth, and unary query arity did not suffice: none of those quantities bounds the directed metric entropy of the persistent typed output set.

## Novelty / collision status

Covering numbers, packing numbers, metric entropy, logarithmic conversion of multiplicative approximation to additive displacement, and epsilon-Pareto approximation are established mathematics. These ingredients are IMPORTED/KNOWN and must not be presented as GC-II inventions.

The GC-II-specific value is organizational: the operational multiplicative certificate problem is now exactly identified with an internal directed cover of the attainable log-capability set. Any future non-tautological compression theorem must derive a bound on this cover from independently measurable operational restrictions rather than define a new width to equal the cover number.

## Status ledger

- multiplicative certificate = directed internal log-cover: PROVED
- independent unit invariance: PROVED
- product-family submultiplicativity: PROVED
- tolerance monotonicity: PROVED
- generic covering/packing/metric-entropy machinery: IMPORTED/KNOWN
- zero-support extension through ordinary logs: FALSIFIED / outside domain
- non-tautological operational bound on directed metric entropy: OPEN

## Next attack

Search for an operational condition stated before observing the Pareto/output set that provably bounds directed log metric entropy. Candidate restrictions must survive the Audit-280 independent-bit deposition family; in particular, merely local control topology is insufficient. Promising quantities to collision-test are bounded total persistent write capacity, bounded communication transcript entropy, bounded output alphabet budget, and bounded description/branching complexity, with explicit comparisons to communication complexity, automata state complexity, algorithmic information, and multiobjective dynamic programming.
