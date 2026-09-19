# GC-II Audit 257 — Semantic atom-refinement no-go for reversibility defects

## Purpose
Audit 256 supplied a graph-reciprocity baseline and left open a semantic reversibility defect over resources, information, interfaces/actions, and rules. A tempting next step is to count semantic atoms destroyed by an operation. This audit proves that raw atom counts are not representation invariant: harmless refinement/duplication of the semantic vocabulary can scale the proposed defect arbitrarily without changing the operational transition system.

## Semantic annotation
Let `X` be a finite operational state space with admissible directed edges `E`. Let `C` be a finite set of semantic capability atoms and let

`S : X -> 2^C`

annotate which atoms are present at each state. The atoms may be typed R/I/A/L; the theorem applies within each type as well as to their union.

For an edge `e=(u,v)`, define raw semantic loss

`ell_S(e)=|S(u) \\ S(v)|`.

For a path `P`, let `L_S(P)=sum_{e in P} ell_S(e)`. For mutually reachable states define the round-trip loss defect

`D_S(x,y)=d_ell(x,y)+d_ell(y,x)`,

where `d_ell` is shortest-path distance with edge weights `ell_S`. If either direction is unreachable, set `D_S=+infinity`.

This is deliberately only a candidate baseline: it asks how many annotated capabilities must be crossed as losses along the least-loss round trip.

## Operationally neutral atom refinement
For integer `k>=1`, replace every atom `a in C` by aliases

`a^(1),...,a^(k)`

with identical state incidence: `a^(r) in S_k(x)` iff `a in S(x)`. No operational state, edge, admissibility condition, cost, observation, action, or target is changed. This is a representational refinement only.

## Theorem 257.1 — exact scaling under atom refinement
For every edge and path,

`ell_{S_k}(e)=k ell_S(e)` and `L_{S_k}(P)=k L_S(P)`.

Therefore, for every mutually reachable `x,y`,

`D_{S_k}(x,y)=k D_S(x,y)`.

### Proof
Each lost original atom contributes exactly `k` lost aliases, and each retained atom contributes zero lost aliases. Hence every edge weight is multiplied by `k`. Every path weight is consequently multiplied by `k`; multiplication by a positive constant preserves the minimizing paths and scales their minimum by `k`. Apply this in both directions. QED.

## Corollary 257.2 — raw semantic-loss count is not an intrinsic GC reversibility invariant
Whenever `0 < D_S(x,y) < infinity`, choosing arbitrarily large `k` makes `D_{S_k}(x,y)` arbitrarily large although the operational system is unchanged. Thus a reversibility invariant intended to depend only on operational capability cannot be a raw count of annotated R/I/A/L atoms unless the ontology fixes atom identity and granularity as part of the physical problem.

This is the semantic analogue of earlier multiplicity warnings in the GC-II audit trail: representation multiplicity must not masquerade as capability magnitude.

## Exact rescue 1 — weighted refinement conservation
Give each original atom a nonnegative weight `w(a)`. Define

`ell_w(u,v)=sum_{a in S(u)\\S(v)} w(a)`.

Under `k`-fold refinement assign every alias weight `w(a)/k`. Then every edge loss and hence every shortest-path and round-trip loss is exactly invariant:

`D_{w_k,S_k}(x,y)=D_{w,S}(x,y)`.

This rescue is exact, but the weights require an external operational justification; choosing them post hoc merely moves the representation problem into `w`.

## Exact rescue 2 — quotient duplicate semantic atoms
Define two atoms equivalent when they have the same incidence vector over all operational states:

`a ~ b iff [a in S(x)] = [b in S(x)] for every x in X`.

Counting equivalence classes rather than atom names is invariant under exact alias duplication. This removes literal duplicates, but it is not yet complete under more general logically or operationally equivalent refinements.

## Edge cases and checks
- If `D_S=0`, duplication leaves it zero.
- If a direction is unreachable, duplication leaves `+infinity` unchanged.
- Atoms present everywhere never contribute to loss.
- An atom absent everywhere never contributes to loss.
- The theorem holds separately per R/I/A/L type, so typed bookkeeping alone does not repair the problem.
- Nonuniform duplication scales different atoms differently and can change minimizing paths, making raw counts even less canonical.
- Weighted conservation requires weights to split additively across aliases; arbitrary alias weights do not preserve the defect.
- Quotienting by identical incidence is representation invariant only for exact duplicates; semantic equivalence relative to the generator language remains open.

## Collision / novelty audit
Representation dependence of raw feature counts and the need for operationally meaningful resource quantifiers are established ideas. General resource-theory work emphasizes operationally defined monotones/currencies rather than arbitrary coordinate counts. Therefore atom-refinement invariance is used here as a validity requirement, not claimed as generic mathematical novelty.

Status:
- exact `k`-fold scaling of raw semantic-loss defect: **PROVED**;
- raw atom-count semantic defect as representation-invariant GC quantity: **FALSIFIED**;
- weighted split conservation: **PROVED**;
- duplicate-incidence quotient invariance: **PROVED for exact aliases**;
- canonical weights derived from GC operational semantics: **OPEN**;
- canonical semantic quotient under all generator-language contexts: **OPEN**;
- GC-specific reversibility invariant surviving graph, cost, and ontology-refinement collisions: **OPEN**.

## Consequence for Paper II
The next semantic reversibility candidate must be invariant under operationally neutral refinements of the R/I/A/L vocabulary. The strongest route is not to count named capabilities, but to derive semantic units from operational distinguishability or regeneration cost under the fixed generator language. Any proposed `Omega_G`, reversibility gap, or R/I/A/L accounting law should be subjected to this refinement test before being interpreted quantitatively.
