# GC-II Audit 286 — Conservative synthetic summaries restore the capability-memory lower bound

## Status

- **PROVED:** conservative external multiplicative cover lower bound for the independent-deposition family.
- **PROVED:** witness attainability is sufficient but not necessary for the persistent-summary lower bound.
- **PROVED:** operationally sound (no false-feasibility) synthetic decoding is another sufficient condition.
- **IMPORTED/KNOWN:** approximate Pareto/dominance sets and inner/outer Pareto-front approximations are established neighboring machinery.
- **OPEN:** characterize the weakest decoder-soundness axiom under which internal and external capability-cover complexity are equivalent up to controlled factors.

## Motivation

Audit 285 showed that unrestricted synthetic centers can collapse an exponential internal directed cover to one center. That collapse is caused by a semantic loophole: a synthetic center may understate an unattainable combination of typed costs. Such a vector is descriptively close in the one-sided directed metric but can create false budget-feasibility claims if treated operationally.

This audit separates **attainability** from the weaker requirement actually needed for safe capability accounting: **conservativeness**.

## Definitions

Let `Y subset R_+^d` be attainable typed cost vectors and `alpha >= 1`.

An arbitrary synthetic vector `z in R_+^d` is a **conservative alpha-summary** of target `y in Y` when

`y_i <= z_i <= alpha y_i` for every coordinate `i`.

The lower inequality is the no-hallucination/no-false-feasibility condition for cost budgets: if the summary declares `z <= q`, then the true target also satisfies `y <= q`.

Let `C_cons_alpha(Y)` be the minimum number of arbitrary synthetic centers whose conservative alpha-balls cover `Y`.

This differs from the unrestricted directed external cover of Audit 285, which requires only `z_i <= alpha y_i` and therefore permits arbitrarily optimistic coordinates.

## Theorem 286.1 — Conservative external exponential lower bound

Fix `alpha >= 1` and choose `r > alpha`. For `m >= 1`, let `d=2m` and

`Y_m = { y^b : b in {0,1}^m }`,

where each module contributes `(r,1)` when `b_j=1` and `(1,r)` when `b_j=0`.

Then

`C_cons_alpha(Y_m) = 2^m = 2^(d/2)`.

### Proof

Every target covers itself conservatively, so `C_cons_alpha(Y_m) <= 2^m`.

Take distinct targets `y^b,y^c`. They differ on some module. Without loss of generality the corresponding pair is `(r,1)` in `y^b` and `(1,r)` in `y^c`. Suppose one synthetic center `z` conservatively alpha-summarized both. Conservativeness for `y^b` forces the second coordinate of that pair to satisfy `z_2 >= r` when read against `y^c`, while alpha-tightness against the coordinate equal to `1` forces `z_2 <= alpha`. Hence `r <= alpha`, contradicting `r>alpha`. Therefore no center can cover two distinct targets. At least `2^m` centers are necessary. QED.

The argument is symmetric and does not require centers to be attainable.

## Corollary 286.2 — Persistent-summary memory lower bound without attainable decoding

Suppose completed histories are discarded and each persistent summary state decodes to an arbitrary synthetic typed-cost vector. Require only:

1. **soundness:** decoded cost never understates the actual target coordinatewise; and
2. **alpha-tightness:** decoded cost is at most `alpha` times the actual target coordinatewise.

Then the number of persistent states is at least `C_cons_alpha(Y)`. For the family above,

`|Sigma| >= 2^m`, hence any fixed-length binary summary needs `k >= m=d/2` bits.

Thus Audit 285 does not eliminate the operational memory lower bound. It identifies exactly which semantics are required: either executable/attainable witnesses (Audit 284) or conservative synthetic certificates (this audit). Unrestricted optimistic synthetic descriptions are insufficient for safe budget decisions.

## Boundary and edge cases

- `alpha=1`: choose any `r>1`; the proof is unchanged.
- `r=alpha`: the strict contradiction disappears; a shared conservative center `(r,r)` can cover both local alternatives. The strict threshold is therefore necessary for this family.
- `m=0`: singleton empty product, certificate size one by convention; theorem stated for `m>=1`.
- No zero coordinates are used.
- Dynamic range is constant (`r`) for fixed `alpha,r`.
- The proof is coordinate-scale invariant under multiplication by positive coordinate-specific constants.
- Composition is exact: independent modules multiply the number of pairwise conservatively incompatible summaries.

## Prior-art collision note

The generic approximation language is not claimed as novel. Approximate Pareto sets under multiplicative dominance are classical, and the literature also studies lower/upper (inner/outer) approximations of Pareto fronts. The GC-II claim is narrower: in budgeted operational capability accounting, the semantic distinction between an optimistic synthetic description and a conservative synthetic certificate determines whether the exponential persistent-memory obstruction survives.

Relevant neighboring work includes Papadimitriou–Yannakakis approximate Pareto-set theory, Diakonikolas–Yannakakis minimum approximate Pareto sets, partially exact Pareto approximations, and upper-shell approximations of Pareto fronts.

## Next attack

Seek a decoder-soundness lattice between unrestricted directed description, conservative synthetic certification, and attainable witness preservation. Determine whether a weakest decision-relative condition can be expressed directly in terms of the permitted budget-query family rather than coordinatewise conservativeness. That would make the lower bound query-relative and avoid imposing stronger semantics than operational decisions require.
