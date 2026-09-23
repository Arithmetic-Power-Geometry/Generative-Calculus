# GC-II Audit 339 — Novelty-distance spectrum

## Scope

This audit sharpens Audits 335–338 without changing GC-I.  Work is restricted to the finite baseline-closed macro-transition model used in those audits.

## Setup

Let `Q` be a finite operational quotient with `q=|Q|`.  Let `B` be baseline reachability and let `M` be the Boolean adjacency relation for one newly admitted macro-step after baseline closure.  For ordered pair `(x,y)`, define

`d_M(x,y) = min { l >= 0 : (M^l)_{xy}=1 }`, with `d_M(x,y)=infinity` if no such walk exists.

Only pairs not already in `B` are counted as novel.  Define the novelty shell

`N_l = |{(x,y) notin B : d_M(x,y)=l}|`,  l>=1.

Define the novelty-distance polynomial

`P_G(z) = sum_{l=1}^{q-1} N_l z^l`.

This is a finite representation of the entire raw finite-horizon novelty profile.

## Theorem 339.1 — exact shell decomposition

For every horizon `h>=0`,

`Omega_pair^(h) = sum_{l=1}^{min(h,q-1)} N_l`.

Consequently the first-appearance increment is exactly

`Omega_pair^(h)-Omega_pair^(h-1) = N_h` for `1<=h<=q-1`,

and is zero for `h>=q`.

### Proof

By definition, a baseline-novel pair is reachable within `h` macro-steps iff its shortest macro-distance is at most `h`.  The sets of pairs with distinct finite shortest distances are disjoint, so counting their union gives the cumulative shell formula.  Audit 338's simple-witness argument gives `d_M(x,y)<=q-1` whenever the distance is finite.  The increment identity follows by subtraction.  QED.

## Corollary 339.2 — exact saturation horizon

Let

`H_* = max { d_M(x,y) : (x,y) notin B, d_M(x,y)<infinity }`,

with `H_*=0` if no novel pair exists.  Then `H_*<=q-1` and

`Omega_pair^(h)=Omega_pair^(infinity)` iff `h>=H_*` (except the trivial zero-novelty case, where equality holds for all h).

Thus Audit 338's universal `q-1` horizon is a worst-case bound; the exact system-specific reuse horizon is the largest finite shortest distance among baseline-novel pairs.

## Corollary 339.3 — equality of raw horizon profiles

Two finite macro-systems have identical raw pair-novelty curves for every horizon iff their novelty shell vectors `(N_1,...,N_{q-1})` agree (after zero-padding if their quotient sizes differ).  This is an accounting equivalence only: it does **not** imply graph isomorphism, equal resources, equal interfaces, or equal task semantics.

## Verification

`experiments/gc2_audit339_novelty_distance_spectrum.py` exhaustively enumerates every directed relation, with self-loops allowed, on `q=1,2,3,4` labelled states.  There are 66,066 relations in total.  For each relation it computes directed shortest distances by BFS and checks every horizon `0,...,q-1` against direct bounded reachability.  Independent execution produced 263,714 cumulative equalities and zero failures; maximum observed shortest macro-distance was 3, as required for q=4.

## Edge/invariance/composition audit

- `q=1`: polynomial is zero.
- Empty `M`: polynomial is zero.
- Self-loops do not create positive-distance novelty when identity is baseline-reachable.
- Cycles cannot delay first reachability beyond a simple shortest witness.
- Relabelling states permutes pairs but leaves every `N_l` invariant.
- Duplicating a syntactic rule without changing `M` leaves the spectrum invariant.
- The spectrum is monotone cumulatively in horizon, but shell counts themselves need not be monotone in `l`.
- Product/composition does not admit an additive shell law in general; mixed-coordinate paths can alter shortest distances. No additive claim is made.

## Prior-art boundary

Shortest-path distance, all-pairs shortest paths, BFS layers, distance distributions/histograms, Boolean transitive closure, and graph diameter are standard graph/network theory.  Therefore the distance-shell mechanism is **IMPORTED/KNOWN**.  No novelty claim is made for shortest-path histograms or their generating polynomial.  The GC-II contribution here is narrower: it supplies the exact accounting refinement of Audits 335–338 and identifies the system-specific saturation coordinate `H_*` without inventing an independent reuse parameter.

Collision classes explicitly checked conceptually: reachability/viability (direct collision), semiring transitive closure (direct collision), complexity/APSP (direct collision), resource theories/simulation preorders (convertibility interpretation only), information theory/thermodynamics/Blackwell–Le Cam/majorization/GPTs/contextuality/database decomposability/CSP width (no theorem novelty asserted from this graph identity).

## Status

- Exact novelty shell decomposition: **PROVED**.
- Exact saturation horizon `H_*`: **PROVED**.
- Shortest-path/distance-distribution machinery: **IMPORTED/KNOWN**.
- Claim that `q-1` is always the minimal saturation horizon: **FALSIFIED**; it is only worst-case sharp.
- Claim that the shell spectrum is a complete invariant of operational systems: **FALSIFIED**; it is complete only for the raw horizon-count curve.
- Bridge from charged `(Delta R,Delta I,Delta A,Delta L)` to constraints on the spectrum: **OPEN**.

## Scientific consequence

For finite raw pair novelty, the amplification object can now be represented exactly by a finite distance spectrum rather than an arbitrary horizon parameter.  This does not yet solve the Paper-II quantitative accounting problem: the unresolved theorem is a non-tautological bridge from charged operational deltas to restrictions on that spectrum or on a task-weighted analogue.
