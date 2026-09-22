# GC-II Audit 311 — operational local-to-global translator lower bound

## Purpose
This audit attacks Paper-II item (7): strengthen GC-I projection irreducibility into an operational local-to-global translator lower bound. The goal is a correct restricted theorem, not a novelty claim.

## Setting
Fix a finite-dimensional polyhedral capability envelope

`P = conv{v_1,...,v_n} = {x : A x <= b}`.

Interpret an **exact linear local-to-global translator** as an extended formulation

`Q = {(x,z) : E x + F z <= g}`

whose projection onto the exposed/global capability coordinates is exactly `P`.

The latent coordinates `z` represent any auxiliary local summaries, hidden coordination variables, interface states, or intermediate certificates available to the translator. Its inequality budget is the number `r` of rows of `(E,F)`.

This deliberately studies exact linear/polyhedral translators only. It does not cover nonlinear, approximate, randomized-with-error, oracle, or unrestricted computational translators.

## Slack object
For facets/valid inequalities `a_i.x <= beta_i` and vertices `v_j`, define the nonnegative slack matrix

`S_ij = beta_i - a_i.v_j >= 0`.

Let `rank_+(S)` be its nonnegative rank.

## Theorem 311.1 — exact translator lower bound
Every exact linear local-to-global translator for `P` with `r` inequalities satisfies

`r >= rank_+(S_P) = xc(P)`.

Equivalently, if `rank_+(S_P) > r`, then no exact translator using at most `r` linear inequalities in any lifted latent dimension can reproduce the global capability envelope under projection.

### Proof
An exact translator `Q` as defined above is precisely an extended formulation of `P`. By the factorization theorem for polyhedral extensions, the minimum number of inequalities in any extended formulation of `P` equals the nonnegative rank of a slack matrix of `P`. Therefore every such `Q` has at least `rank_+(S_P)` inequalities. QED.

**Status:** PROVED, with the mathematical mechanism IMPORTED/KNOWN (Yannakakis factorization theorem).

## Corollary 311.2 — latent dimension alone cannot evade the obstruction
Allowing arbitrarily many auxiliary coordinates `z` does not by itself defeat the lower bound: if the translator remains an exact linear extended formulation, its inequality count is still at least `xc(P)`.

Thus a failure of direct projection cannot in general be repaired merely by introducing a small constraint interface in a high-dimensional latent space.

**Status:** PROVED / IMPORTED-KNOWN consequence.

## Corollary 311.3 — communication interpretation
For the slack matrix `S_P`, known factorization/communication results imply that

`log_2 rank_+(S_P)`

is the minimum communication complexity of an appropriate randomized protocol computing the nonnegative slack matrix in expectation.

Hence an exact linear global translator with extension complexity `r` carries a corresponding communication obstruction of logarithmic scale: families with large nonnegative rank cannot have simultaneously tiny exact linear extension descriptions and tiny exact-in-expectation slack protocols.

This is a bridge to distributed capability accounting, but the bridge is inherited from known extension-complexity/communication-complexity theory.

**Status:** IMPORTED/KNOWN mechanism; GC-II operational interpretation only.

## Corollary 311.4 — direct facets versus lifted translation
Let `f(P)` be the number of facets of a nonredundant direct H-description. Then

`xc(P) <= f(P)`.

The ratio or difference between direct facet complexity and extension complexity can therefore be large. Projection irreducibility must not be misstated as saying that every lifted representation is as large as the direct global description. The correct invariant for exact linear translators is extension complexity, not raw facet count in the exposed coordinates.

**Status:** PROVED / correction of an overstrong possible interpretation.

## Collision / falsification checks
1. **Arbitrary latent dimension defeats the bound?** FALSIFIED for inequality count: extension complexity already minimizes over all lifted dimensions.
2. **Direct facet count is a universal translator lower bound?** FALSIFIED in general; extended formulations can be much smaller than direct H-descriptions.
3. **Ordinary matrix rank suffices?** FALSIFIED as a complete measure. Slack matrices of a `d`-polytope have ordinary rank essentially `d+1`, while nonnegative rank/extension complexity can be much larger.
4. **Affine relabeling changes the obstruction?** No. Extension complexity is invariant under affine isomorphism of the represented polytope.
5. **Cartesian composition is automatically additive?** Not asserted. Product constructions give upper bounds, but exact additivity of extension complexity/nonnegative rank is not assumed here.
6. **Approximate translators obey the same theorem?** OPEN under this audit; approximate extension complexity requires a separately declared error model.
7. **Nonlinear translators obey the same theorem?** NOT IMPLIED.

## Relation to GC-I projection irreducibility
GC-I's projection irreducibility motivates asking when local/latent descriptions can recover a global envelope. Audit 311 identifies a rigorous operational lower-bound surrogate in the exact linear/polyhedral regime:

`local-to-global translator size >= extension complexity = nonnegative rank(slack)`.

This is stronger than merely observing that a particular projection loses information because it quantifies the minimum inequality budget over **all** exact linear lifts. It is nevertheless not a new polyhedral theorem.

## Prior-art collision audit
This result collides directly with:
- Yannakakis' factorization theorem;
- extended formulations and nonnegative factorization;
- deterministic/randomized communication complexity of slack matrices;
- polyhedral combinatorics and LP formulation complexity.

Therefore:
- equality `xc(P)=rank_+(S_P)` — IMPORTED/KNOWN;
- communication characterization — IMPORTED/KNOWN;
- GC-II interpretation as a capability translator lower bound — DERIVED CONSEQUENCE;
- claim of a new general local-to-global lower-bound theorem — REJECTED;
- extension to nonlinear/dynamic/budgeted operational translators — OPEN.

## Dimensional/domain checks
- `S_P` is dimensionless only after each facet inequality is normalized; nonnegative rank itself is invariant under positive row/column scaling, so the lower bound is representation-safe.
- Empty envelopes and singletons are degenerate cases and should be treated separately; the theorem is intended for nonempty polytopes with a conventional slack representation.
- Lower-dimensional polytopes are handled in their affine hull; redundant inequalities/vertices do not change the intrinsic extension-complexity conclusion when the standard slack-matrix formulation is used.
- The bound counts inequalities, not arithmetic operations, bits of coefficient precision, wall-clock time, energy, or physical resources. Those require separate accounting variables.

## Status ledger
- Exact linear translator lower bound by nonnegative rank — PROVED / IMPORTED-KNOWN mechanism.
- Arbitrary auxiliary dimension cannot lower inequality count below `xc(P)` — PROVED.
- Direct exposed facet count as the correct lower bound — FALSIFIED.
- Ordinary rank as complete translator complexity — FALSIFIED.
- Communication bridge — IMPORTED/KNOWN.
- New unrestricted GC-II local-to-global translator theorem — OPEN.
- Approximate/nonlinear/dynamic translator lower bounds — OPEN.
