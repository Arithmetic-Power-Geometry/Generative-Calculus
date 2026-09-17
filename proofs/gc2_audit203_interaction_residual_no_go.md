# GC-II Audit 203 — Coordinate Interaction Residual No-Go

## Target
Audit 202 left open whether an irreducible interaction residual among resource (R), information (I), action/interface (A), and rule (L) changes could define a GC-specific capability quantity not reducible to scalar simulation costs or ordinary monotones.

## Setup
Let N={R,I,A,L}. For a fixed operational task/error/budget semantics, let v:2^N -> R be any scalar capability-value functional after enabling the indicated typed changes. Normalize only when explicitly desired; no additivity is assumed.

The canonical full-order inclusion-exclusion residual is

J_N(v) = sum_{S subseteq N} (-1)^(|N|-|S|) v(S).

More generally the Möbius coefficient for T subseteq N is

m_v(T)=sum_{S subseteq T} (-1)^(|T|-|S|)v(S),

and v(S)=sum_{T subseteq S}m_v(T).

## Theorem 203.1 — Exact decomposition, but no novelty
For every finite set function v the Möbius coefficients exist uniquely and reconstruct v exactly.

Status: PROVED / IMPORTED-KNOWN mathematical mechanism.

Proof: Möbius inversion on the Boolean subset lattice.

Therefore a nonzero four-way residual is a valid descriptive interaction statistic, but existence of such a residual is not itself a GC theorem.

## Theorem 203.2 — Typed interaction residual is not representation invariant under regrouping
There exist two exactly equivalent descriptions of the same operational capability table for which the highest-order residual has different order and numerical attribution.

Witness: v(S)=1 iff {R,I} subseteq S, else 0, with A,L operationally irrelevant. In the four-coordinate description,

m_v({R,I})=1 and m_v(T)=0 for all other nonempty T.

Now replace the jointly required pair (R,I) by one admissible composite coordinate X whose presence means that the same joint package is available. The equivalent one-coordinate table is v'(empty)=0, v'({X})=1, hence m_v'({X})=1 and there is no interaction term at all.

Both descriptions induce the same two operational regimes (package unavailable / package available), same task outcome, same budget and same conversion behavior. Yet one calls the gain a second-order interaction and the other a first-order contribution.

Status: PROVED.

## Corollary 203.3 — Raw Omega based on coordinate synergy is not intrinsic
Any proposed Generative Novelty Gap Omega_G that depends on the order, sign, or magnitude of Möbius/PID-style interaction terms over a freely chosen R/I/A/L factorization is not invariant under admissible regrouping of jointly supplied primitives.

Status: PROVED conditional on allowing semantics-preserving regrouping as a representation change.

## Edge and stress checks
- Constant v: all nonempty coefficients vanish.
- Additive v: all coefficients of order >=2 vanish.
- Pure k-way threshold/conjunction: one k-way coefficient survives.
- Sign: interaction coefficients need not be nonnegative for arbitrary v.
- Monotonicity of v does not imply nonnegative interaction coefficients.
- Composition: Möbius coefficients are additive only when the underlying value functions add; GC-II cannot assume this.
- Units: every coefficient has the same units as v, so mixed physical resource units cannot be inserted into v without an explicit scalarization/valuation map.
- Coordinate refinement/coarsening changes interaction order, so the statistic fails the representation-invariance gate unless the factorization itself is declared operational structure.

## Prior-art collision ledger
- Boolean-lattice Möbius/inclusion-exclusion interaction decomposition: IMPORTED/KNOWN.
- Information synergy/redundancy and interaction-information/PID families: IMPORTED/KNOWN neighboring mechanisms.
- General resource theories already permit composite resources, catalysts, and nontrivial convertibility; nonadditivity alone is not a GC novelty claim.
- Raw R/I/A/L interaction residual as intrinsic Omega_G: FALSIFIED.

## Surviving gate
The factorization must itself be operationally identifiable rather than chosen by notation. A viable GC-II invariant would need to minimize or otherwise quotient over all admissible semantics-preserving factorizations/refinements, or be defined directly on the operational simulator category/preorder. The next test is therefore a factorization-quotiented interaction cost: determine whether its nonzero value survives reduction to ordinary minimum simulation/implementation cost and general resource theory.
