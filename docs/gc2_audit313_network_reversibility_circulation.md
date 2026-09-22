# GC-II Audit 313 — network reversibility: circulation obstruction beyond pairwise normalized gaps

## Purpose
Audit 312 showed that a single normalized pairwise reversibility gap is incomplete. This audit asks for the next mathematically defensible network-level object. The goal is not to rename known graph theory, but to identify exactly what pairwise directional conversion costs contain that a scalar gap discards.

## Setting
Let `Z` be a finite operational state space in one fixed scalar cost regime. Let

`d(x,y)`

be the optimal nonnegative directed conversion cost. Restrict this audit to one finite-cost strongly connected component, so every ordered pair has finite `d`.

Define the symmetric burden and signed directional field

`B(x,y)=d(x,y)+d(y,x)`,

`A(x,y)=d(x,y)-d(y,x)`.

Then `B(x,y)=B(y,x)` and `A(x,y)=-A(y,x)`, and the ordered pairwise costs are recovered exactly by

`d(x,y)=(B(x,y)+A(x,y))/2`,

`d(y,x)=(B(x,y)-A(x,y))/2`.

Thus `(B,A)` is lossless for the complete directed distance matrix. This is elementary algebra and is not a novelty claim.

## Cycle circulation
For an oriented cycle `C=(v_0,v_1,...,v_k=v_0)`, define

`Circ_A(C)=sum_{i=0}^{k-1} A(v_i,v_{i+1})`.

This quantity has the declared cost unit. Reversing the cycle changes its sign. Positive rescaling of all costs rescales circulation by the same factor.

A nonzero circulation records directional inconsistency that cannot be represented by assigning a single scalar potential to states.

## Theorem 313.1 — exact potential/circulation criterion
For a finite strongly connected operational distance matrix, the following are equivalent:

1. There exists a potential `h:Z->R` such that `A(x,y)=h(y)-h(x)` for every pair.
2. `Circ_A(C)=0` for every cycle.
3. For one fixed root `r`, every triangle `r -> x -> y -> r` has zero circulation.

### Proof
`1 => 2`: a cycle sum of potential differences telescopes to zero.

`2 => 3`: immediate.

`3 => 1`: define `h(v)=A(r,v)`. Zero circulation on `r -> x -> y -> r` gives

`A(r,x)+A(x,y)+A(y,r)=0`.

Using antisymmetry, `A(y,r)=-A(r,y)`, hence

`A(x,y)=A(r,y)-A(r,x)=h(y)-h(x)`.

QED.

**Status:** PROVED. The mathematical mechanism is IMPORTED/KNOWN: exact 1-forms, cycle-space/coboundary criteria, and potential representations are standard graph/network mathematics. GC-II contributes only the operational interpretation for directed conversion costs.

## Corollary 313.2 — a finite complete obstruction basis
For `n=|Z|`, fixing a root requires only the `(n-1)(n-2)/2` unordered root-triangle tests to decide whether the entire antisymmetric conversion field is potential-generated.

If all tests vanish, `h(v)=A(r,v)` reconstructs `A`; together with `B`, this reconstructs every directed pairwise conversion cost exactly.

If any root-triangle circulation is nonzero, no state potential can explain all directional asymmetries.

**Status:** PROVED by Theorem 313.1. The cycle-space basis interpretation is IMPORTED/KNOWN.

## Decisive collision against state-only irreversibility scores
Consider three states with antisymmetric directional field

`A(0,1)=1`, `A(1,2)=1`, `A(2,0)=1`,

with reversed entries `-1`. Then the triangle circulation is `3`.

No scalar state potential `h` can satisfy `A(x,y)=h(y)-h(x)`, because potential differences telescope to zero around every cycle.

Therefore any reversibility account that assigns only a scalar state score and represents pairwise directionality solely by score differences is incomplete for general operational networks.

**Status:** universal state-potential completeness — FALSIFIED.

## Composition and invariance audit
If two independent regimes have additive directed costs pairwise, then

`A_total=A_1+A_2`, `B_total=B_1+B_2`,

and therefore

`Circ_total(C)=Circ_1(C)+Circ_2(C)`.

Unlike Audit 312's absolute normalized `Gamma_rev`, signed circulation is additive under this explicitly stated additive-cost composition. Opposite circulations may cancel, so absolute circulation is not additive and should not be advertised as a monotone.

Relabeling states preserves the multiset of oriented cycle circulations up to the corresponding orientation convention. Adding a potential field `g(y)-g(x)` to `A` leaves every circulation unchanged (a gauge invariance).

**Status:** PROVED algebraically under additive pairwise-cost composition.

## Exact finite exhaustive check
An independent verifier enumerates all `4^6=4096` complete directed three-state edge-cost assignments with each primitive edge cost in `{0,1,2,3}`. For each assignment it computes all-pairs shortest-path costs exactly, constructs `A=d-d^T`, and checks:

`triangle circulation = 0  <=>  A is representable as h(j)-h(i)`

with `h(v)=A(0,v)`.

All 4096 cases pass exactly; no floating-point tolerance is used.

**Status:** NUMERICALLY/EXHAUSTIVELY SUPPORTED finite audit of the proved theorem, not evidence of novelty.

## Prior-art collision audit
This construction collides directly with established material on directed distances/quasi-metrics, graph cycle spaces, circulations, exact discrete 1-forms/coboundaries, potential functions, and Hodge-type decompositions. Resource theories also already study directional conversion rates and reversibility. Therefore:

- directed optimal conversion distance — IMPORTED/KNOWN;
- cycle circulation/potential criterion — IMPORTED/KNOWN;
- use as a GC-II operational diagnostic — DERIVED APPLICATION;
- claim of a new graph-theoretic reversibility theorem — REJECTED;
- claim that one scalar per state universally captures network irreversibility — FALSIFIED.

## Edge/domain checks
- Heterogeneous resource dimensions must not be silently summed; this audit assumes one declared scalar cost or prior scalarization.
- Zero-cost cycles are allowed.
- Mutually unreachable pairs are excluded from this finite strongly connected formulation; extended/infinite costs require componentwise treatment.
- `B` has cost units, `A` and circulation have cost units. A normalized circulation would require an independently justified denominator and can reintroduce Audit-312-style collisions.
- The theorem concerns the optimal directed distance matrix, not hidden primitive edges that never affect any optimum.
- Potential representability does not imply free reversibility: `A=0` only says forward/reverse optimal costs are equal; the common burden can be positive.

## Status ledger
- `(B,A)` losslessly reconstructs finite directed pairwise costs — PROVED / elementary.
- Zero-cycle-circulation iff directional field is a state-potential difference — PROVED / IMPORTED-KNOWN mechanism.
- Root-triangle test is complete — PROVED.
- Universal scalar state-potential account — FALSIFIED by nonzero circulation.
- Signed circulation additive under explicitly additive directed-cost composition — PROVED.
- Absolute/normalized circulation as a universal monotone — NOT CLAIMED.
- Full invariant for primitive network structure, stochastic conversions, vector resources, and budget-changing admissibility — OPEN.

## Paper-II consequence
Audit 312's pairwise `(B_rev,Gamma_rev)` should not be promoted to a network-complete invariant. At network scale the signed orientation information matters, and its cycle component is irreducible to state-potential differences. A disciplined GC-II reversibility account therefore has at least two layers: symmetric conversion burden and a signed directional field, with cycle circulation diagnosing genuinely network-level directional obstruction. The mathematics is known; the value here is preventing a false scalar or state-potential completeness claim before application experiments.