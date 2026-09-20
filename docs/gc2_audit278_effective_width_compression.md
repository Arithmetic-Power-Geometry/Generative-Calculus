# GC-II Audit 278 — Effective-width compression under operational mode locality

## Status

- Mode-local effective-width compression theorem: **PROVED**.
- Replacement of ambient accounting dimension by active operational width under the stated locality hypothesis: **PROVED**.
- Claim that bounded witness/gate width alone implies this theorem: **NOT CLAIMED / OPEN**.
- Generic geometric epsilon-Pareto gridding: **IMPORTED/KNOWN**.
- GC-II interpretation as a structural escape from Audit 277's dimension barrier: **CONDITIONAL contribution**.

## Setting

Let `Y subset R_+^d` be a finite attainable typed-cost set and `alpha>1`. Partition `Y` into operational modes `Y_1,...,Y_M`. Mode `j` has an active coordinate set `A_j subseteq [d]`, with `|A_j|<=w`, such that every coordinate outside `A_j` is constant throughout that mode. Thus there is a vector `c^j` with `y_i=c^j_i` for every `y in Y_j` and every `i notin A_j`.

For each active coordinate `i in A_j`, allow exact zero and suppose all positive values occurring in that mode lie in `[m_ji,M_ji]`, where `0<m_ji<=M_ji`. Put

`K_ji = 2 + floor(log_alpha(M_ji/m_ji))`.

The first symbol is exact zero; the remaining symbols are multiplicative geometric bins for positive values.

An `alpha`-representative certificate is a subset `S subseteq Y` such that every `y in Y` has some `s in S` satisfying `s_i <= alpha y_i` for every coordinate.

## Theorem (mode-local effective-width compression)

Under the assumptions above, there exists an attainable alpha-representative certificate `S subseteq Y` with

`|S| <= sum_{j=1}^M prod_{i in A_j} K_ji`.

In particular, if every active coordinate in every mode has positive dynamic range at most `Gamma`, then

`|S| <= M (2 + floor(log_alpha Gamma))^w`.

The exponent is the active operational width `w`, not the ambient typed-accounting dimension `d`.

### Proof

Within a fixed mode `j`, assign every target `y` a signature on `A_j`: exact zero gets a distinguished zero symbol; each positive coordinate is assigned its geometric alpha-bin. Coordinates outside `A_j` need no signature because they are identical for all members of the mode. There are at most `prod_i K_ji` signatures.

For each nonempty signature class choose one attainable representative minimizing each coordinate is unnecessary: simply choose a member whose coordinatewise bin indices are the same as the target class. If `s_i` and `y_i` are positive and occupy the same geometric bin, then `s_i <= alpha y_i`; if `y_i=0`, the exact-zero symbol forces `s_i=0`. Outside `A_j`, `s_i=y_i=c^j_i`. Hence every member of the class is alpha-covered by every other member of that class. Taking one representative per nonempty class gives an alpha-certificate for `Y_j`. Union over modes proves the first bound. The uniform-range corollary follows from `|A_j|<=w`.

## Why this is nontrivial relative to Audit 277

Audit 277 constructs an exponential family whose vectors differ across all `d` coordinates. The present theorem identifies a sufficient structural condition under which that ambient-dimensional obstruction disappears: attainable tradeoffs decompose into modes in which only `w` coordinates can vary. Large `d` alone is then harmless; certificate size is exponential only in effective width (and linear in the number of modes).

This is deliberately weaker than claiming that Audit 271's gate arity or witness width automatically induces mode locality. Hidden guards, path multiplicity, or changing inactive-coordinate baselines can violate the hypothesis. Establishing a theorem from a causal/dependency decomposition to this mode-local form remains open.

## Edge cases and invariances

- `A_j=empty`: one representative suffices for the mode.
- Exact zeros are handled without a positive floor at zero.
- Singleton positive range `M_ji=m_ji` is valid.
- Coherent positive rescaling of any accounting coordinate preserves signatures up to translated log bins and preserves alpha-cover.
- Duplicate modes may be merged but need not be; the stated bound remains valid.
- The theorem gives an attainable representative certificate; it does not rely on synthetic unattainable vectors.
- Composition across modes is not assumed additive.

## Prior-art collision note

Geometric gridding and polynomial-size epsilon-Pareto sets for a fixed number of objectives are established multiobjective-optimization machinery. Bounded-width decompositions are also established algorithmic machinery. Therefore neither ingredient is claimed as new mathematics. The GC-II candidate contribution is the operational synthesis: Audit 277's ambient-dimension barrier can be replaced by an effective operational width only when a defensible locality/decomposition hypothesis is supplied.

## Next target

Derive mode locality, or a more general separator-local certificate theorem, from an explicit operational dependency graph/hypergraph. The desired statement is that separator width `w`, bounded positive log-scale range, and a bounded number of boundary states imply an alpha-certificate of size `poly(number of bags) * f(w,alpha,range,boundary states)`. This would connect Audit 271's translator lower bound to Audits 274–278 without assuming the mode partition by hand.
