# GC-II Audit 310 — finite dual criterion for polyhedral capability convertibility

## Purpose
This audit attacks Paper-II item (6): a structured complete convertibility criterion. It deliberately separates the GC-II operational interpretation from standard convex/polyhedral machinery.

## Setting
Let a fixed, independently declared feature map be `phi:Y -> R^d`. For two finite budgeted operational closures define

`P = conv(phi(Cap_b(S)))`, `Q = conv(phi(Cap_c(T)))`.

The convertibility question studied here is the capability-containment preorder

`P <= Q  iff  P subseteq Q`.

This is a deliberately restricted structured class: finite-dimensional polyhedral capability envelopes. It is not claimed to decide arbitrary GC-II convertibility.

## Theorem 310.1 — finite complete facet monotones
Assume a nonredundant H-representation

`Q = {x in R^d : a_j . x <= beta_j, j=1,...,m}`.

Define target-relative monotones

`M_j(P;Q) = h_P(a_j) - beta_j`,

where `h_P(a)=max_{x in P} a.x` is the support function.

Then

`P subseteq Q  iff  M_j(P;Q) <= 0 for every j=1,...,m`.

### Proof
If `P subseteq Q`, every `x in P` obeys every defining inequality of Q, hence `h_P(a_j)<=beta_j`.
Conversely, if all inequalities hold at their maxima over P, every x in P satisfies all H-inequalities and therefore x is in Q. QED.

**Status:** PROVED. The polyhedral mechanism is IMPORTED/KNOWN.

## Corollary 310.2 — finite vertex test
If `P=conv{p_1,...,p_n}`, then

`P subseteq Q iff a_j.p_i <= beta_j for all i,j`.

Thus exact convertibility in this class is a finite rational-arithmetic decision problem whenever vertices/facets are rational.

**Status:** PROVED / IMPORTED-KNOWN mechanism.

## Corollary 310.3 — complete dual witness
If `P not subseteq Q`, at least one target facet j satisfies

`h_P(a_j) > beta_j >= h_Q(a_j)`.

Hence that facet normal is an explicit linear operational task witnessing closure escape. This is the finite target-adapted version of Audit 303's support-function separation criterion.

**Status:** PROVED.

## Proposition 310.4 — monotonicity and composition checks
For fixed Q and P1 subseteq P2,

`M_j(P1;Q) <= M_j(P2;Q)`.

Under Cartesian product and concatenated direction `(a,b)`, support functions satisfy

`h_{P x R}(a,b)=h_P(a)+h_R(b)`.

Therefore facet witnesses compose additively only when the comparison geometry itself factorizes compatibly. No general additivity claim is made for arbitrary target facets.

**Status:** PROVED; unrestricted additivity remains OPEN/FALSE without structural assumptions.

## Degenerate and invariance checks
- Empty capability envelopes are excluded from the support-function convention used here; they can be handled separately as the bottom element.
- Lower-dimensional Q is allowed only with a complete H-description including affine-hull equalities (represented as paired inequalities). Omitting affine-hull constraints can produce false positives.
- Duplicate/redundant facets do not affect completeness, only certificate size.
- Under an invertible affine coordinate change, containment is invariant and facet normals transform contragrediently; numerical values of raw normals are representation-dependent.
- Rescaling `(a_j,beta_j)` by a positive scalar preserves the sign test, so a normalized convention is required before comparing gap magnitudes.

## Novelty / prior-art collision audit
The theorem is standard convex/polyhedral containment expressed in GC-II capability language. It collides directly with support functions, separating hyperplanes, linear programming, polyhedral containment, convex resource theories, and finite witness/certificate theory. Therefore:

- finite facet completeness: IMPORTED/KNOWN mechanism;
- GC-II interpretation as a structured capability-convertibility certificate: DERIVED CONSEQUENCE, not claimed foundational novelty;
- arbitrary-system finite complete monotones: OPEN and not implied here.

## Scientific consequence
Paper II can state a precise positive boundary without overclaiming: once a finite operational closure is projected into a fixed finite-dimensional polyhedral capability envelope, convertibility has a finite complete dual certificate family determined by the target facets. Outside that structured representation, this audit supplies no finite-completeness theorem.

## Status ledger
- Polyhedral containment via target facets — PROVED / IMPORTED-KNOWN.
- Finite rational convertibility test — PROVED / IMPORTED-KNOWN.
- Escaping facet as operational linear witness — PROVED.
- Representation-independent finite universal monotone family for unrestricted GC-II systems — OPEN.
- Claim that this polyhedral criterion itself is novel — REJECTED.
