# GC-II Audit 225 — Higher-order capability-interaction boundary

Status: decisive falsification / prior-art boundary.

## Candidate under test

Audit 224 left open whether two systems can have the same baseline capability value and the same one-coordinate responses to resource (R), information (I), action/interface (A), and rule (L) augmentation, but different responses to combined augmentations, and whether that difference can define a GC-specific novelty gap.

## Finite operational response function

Let N={R,I,A,L}. Fix a behaviorally quotiented task universe Q and a scalar valuation V of the budgeted capability set (cardinality is enough for the finite witness). For each subset S of available augmentation coordinates define

v(S)=V(Cap_B(S_0 augmented by S)).

This is simply a set function v:2^N -> R. No additivity is assumed.

Define its Möbius coefficients

m(T)=sum_{U subseteq T} (-1)^(|T|-|U|) v(U).

Möbius inversion gives exactly

v(S)=sum_{T subseteq S} m(T).

Therefore every joint augmentation effect is already decomposed into baseline, first-order, pairwise, triple, and four-way interaction terms.

## Theorem 225.1 — singleton agreement does not constrain higher-order interaction

Equality of v(empty) and all singleton increments v({i})-v(empty) between two systems fixes only m(empty) and m({i}). It places no constraint on m(T) for |T|>=2.

Proof. By the Möbius formula, m(empty)=v(empty) and m({i})=v({i})-v(empty). Conversely, coefficients m(T), |T|>=2, can be selected independently for an arbitrary real-valued set function and inversion uniquely reconstructs v. QED.

## Exact separation witness

Use only coordinates R and I and define two monotone integer-valued capability-count functions:

v_A(S)=|S intersect {R,I}|,

v_B(S)=|S intersect {R,I}| + 1[{R,I} subseteq S].

Then

v_A(empty)=v_B(empty)=0,
v_A({R})=v_B({R})=1,
v_A({I})=v_B({I})=1,

but

v_A({R,I})=2 != 3=v_B({R,I}).

The unique pairwise Möbius coefficients are

m_A({R,I})=0,
m_B({R,I})=1.

Thus the Audit-224 separation exists, but it is exactly an ordinary second-order interaction/synergy coefficient of a set function.

A literal finite capability-set realization is immediate. Let Q={q_R,q_I,q_RI}. System A realizes q_R iff R is supplied and q_I iff I is supplied. System B has those same realizabilities and additionally realizes q_RI iff both R and I are supplied. Taking V=cardinality yields the two functions above. No GC-specific mechanism is needed.

## Corollary 225.2 — arbitrary higher-order separation

For any nonempty T subseteq N with |T|>=2 and any integer k>=0, adding k new tasks that become realizable iff every coordinate in T is present changes m(T) by k while leaving baseline and every response on proper subsets of T unchanged. Hence arbitrarily large positive higher-order capability interaction can be manufactured in an ordinary finite reachability system.

For signed scalar valuations, arbitrary positive or negative higher-order coefficients are possible. For literal capability-set cardinalities under monotone augmentation, the coefficients need not all be nonnegative; monotonicity of v constrains marginal sums, not the sign of every Möbius coefficient.

## Consequence for the proposed quantitative bound

A formula such as

Omega_G <= F(Delta R, Delta I, Delta A, Delta L)

cannot be inferred from coordinate magnitudes alone without structural assumptions: two systems can have identical individual coordinate increments and arbitrarily different joint capability gain by adding conjunction-gated tasks. Nonlinear interaction terms are necessary if a scalar response model is used, but their existence is not GC novelty.

A universal finite upper bound from only singleton gains is impossible in an unrestricted finite task universe: hold all singleton gains fixed and introduce k conjunction-only tasks; joint gain grows with k. Any finite F must therefore include interaction-sensitive structural data or assumptions that bound task universe/value, complementarity, description size, or admissible composition.

## Collision checks

- Set functions/pseudo-Boolean functions: Möbius transforms are an established exact representation.
- Cooperative games: Harsanyi/Möbius dividends and Shapley/Banzhaf-style interaction indices already quantify coalition interaction/synergy.
- Submodularity/supermodularity: pairwise complementarity/substitutability is standard structure on set functions.
- Resource theories: activation/catalysis already demonstrate that combined resources can enable conversions unavailable separately.
- Production/cooperative-game interpretations: complementarity alone is not mechanism-specific.
- Information theory: interaction-information analogies are not needed for the theorem and should not be used to claim novelty.

## Edge, invariance, composition, and degeneracy checks

- No augmentation: inversion includes m(empty)=v(empty).
- One coordinate: no higher-order term exists.
- Redundant coordinate: all Möbius coefficients containing only a genuinely null coordinate vanish when v is invariant to that coordinate.
- Relabeling R,I,A,L permutes Möbius coefficients equivariantly.
- Additive systems are exactly those with m(T)=0 for all |T|>=2.
- Monotone v does not imply nonnegative m(T); do not equate monotonicity with supermodularity or total monotonicity.
- Parallel composition can create or destroy scalar interaction depending on the valuation V; no composition law is assumed.
- Infinite Q requires a finite/measure-valued V before scalar Möbius analysis; the finite counterexample already falsifies universality.

## Status ledger

- existence of systems with equal baseline/singletons but unequal joint response: PROVED
- exact Möbius decomposition of finite coordinate response: IMPORTED/KNOWN mathematics, applied exactly here
- higher-order capability interaction as GC-specific Omega_G: FALSIFIED
- arbitrary conjunction-gated positive interaction in ordinary finite reachability: PROVED
- finite universal bound from singleton Delta R, Delta I, Delta A, Delta L alone: FALSIFIED without additional structural assumptions
- nonlinear interaction terms as necessary descriptive coordinates in unrestricted response functions: PROVED
- GC-specific structural restriction forcing a new inequality among interaction coefficients: OPEN
- finite/computable/dual convertibility criterion under such a restriction: OPEN

## Consequence for Paper II

Do not claim synergy, complementarity, or higher-order interaction itself as the breakthrough. The next defensible target is a structural theorem that GC-I imposes a constraint on the interaction tensor/Möbius spectrum that ordinary set functions do not satisfy automatically—for example a sign, support, rank, sparsity, projection-consistency, or realizability restriction derived from independently fixed generative operations. Any such restriction must be proved from GC axioms and collision-tested against k-additive capacities, hypergraphical games, CSP factorization/width, Fourier analysis of Boolean functions, and resource-theoretic activation before it is called novel.
