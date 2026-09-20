# GC-II Audit 272 — Round-trip reversibility gap

## Scope
Finite nonnegative typed operational cost semantics inherited from Audits 265–271. No claim is made here for stochastic, catalytic, replenishing, or endogenous-rule systems.

## Directed operational dilation
For nonempty finite attainable cost sets X,Y subset R_+^d define

M(X|Y) = inf { alpha > 0 : for every y in Y there exists x in X with x <= alpha y },

with extended value +infinity when no finite alpha exists. Define the clipped directed novelty dilation

Omega(X,Y) = max{1,M(X|Y)},   d+(X,Y)=log Omega(X,Y).

For empty sets use the operational conventions d+(empty,empty)=0, d+(X,empty)=0 for X nonempty (there is no requested Y capability), and d+(empty,Y)=+infinity for Y nonempty.

Audits 269–270 established the directed triangle

d+(X,Z) <= d+(X,Y)+d+(Y,Z).

## Reversibility gap
Define

RG(X,Y) = d+(X,Y)+d+(Y,X)
        = log[Omega(X,Y) Omega(Y,X)].

Interpretation: RG is the minimum certified logarithmic round-trip dilation needed to translate the two operational capability sets into one another, after quotienting away dominated implementations.

### Theorem 272.1 — quotient metric
Let X ~ Y iff their upward closures agree (equivalently their Pareto kernels agree). On finite operational capability classes modulo ~, RG is an extended metric:

1. RG(X,Y) >= 0.
2. RG(X,Y)=RG(Y,X).
3. RG(X,Y)=0 iff X~Y.
4. RG(X,Z) <= RG(X,Y)+RG(Y,Z).

Proof. (1) and (2) are immediate. For (3), RG=0 iff both clipped directed dilations equal 1, i.e. every y in Y is dominated by some x in X and every x in X is dominated by some y in Y; this is exactly equality of the two upward closures. For (4), add the directed triangle inequality in both orientations. QED.

Status: PROVED for the stated finite semantics.

### Theorem 272.2 — coherent unit invariance
For any positive diagonal change of units D=diag(s_1,...,s_d), s_i>0,

RG(DX,DY)=RG(X,Y).

Proof. x<=alpha y iff Dx<=alpha Dy. Hence both directed dilations are unchanged. QED.

Status: PROVED.

### Theorem 272.3 — independent additive composition bound
For independent additive composition (Minkowski sum),

RG(X1+X2,Y1+Y2) <= RG(X1,Y1)+RG(X2,Y2).

Proof. Audit 269 gives Omega(X1+X2,Y1+Y2) <= max{Omega(X1,Y1),Omega(X2,Y2)}. Taking logs gives d+ of the composition <= max of the two forward d+ values <= their sum. Apply the same argument in reverse and add. QED.

This bound is safe but generally not asserted sharp in all dimensions.

Status: PROVED.

## Directionality is information, not noise
RG alone is symmetric and therefore deliberately forgets which system is harder to emulate. Retain the ordered pair

A(X,Y)=(d+(X,Y), d+(Y,X))

as the reversible accounting signature. RG is its L1 magnitude. A scalar signed difference d+(X,Y)-d+(Y,X) is representation-orientation dependent and is not proposed as an invariant of an unordered pair.

## Collision / prior-art audit
The algebraic mechanism is not new. Cone order gauges generate Hilbert and Thompson geometries; standard formulas use logarithms of reciprocal order-scaling factors. Therefore the generic facts “symmetrize directed order gauges” and “obtain triangle inequalities” are IMPORTED/KNOWN and must not be advertised as new mathematics.

The GC-II-specific content retained for Paper II is narrower: RG is attached to equivalence classes of operational Pareto capability kernels, with explicit empty/unreachable semantics and compatibility with the GC-II independent-composition operation.

## Edge cases
- X~Y: RG=0 even if X and Y contain different dominated implementations. This is required by implementation invariance.
- One side operationally impossible: RG=+infinity when a nonempty requested capability set has no finite translator from the other side.
- Zero coordinates: handled by the order definition rather than unsafe coordinate division.
- Common positive coordinate rescaling: invariant.
- Common scalar rescaling: invariant as a special case.
- Stochastic/catalytic/endogenous-rule extensions: OPEN.

## Ledger
- Round-trip RG definition: PROVED well-defined on finite Pareto-kernel equivalence classes.
- Identity of indiscernibles on quotient: PROVED.
- Symmetry and triangle inequality: PROVED.
- Positive unit invariance: PROVED.
- Independent additive composition upper bound: PROVED.
- Generic cone/order-gauge metric mechanism: IMPORTED/KNOWN.
- Claim that RG is a fundamentally new metric construction: FALSIFIED / not defensible.
- Operational usefulness as a GC-II reversibility diagnostic: CONDITIONAL candidate pending controlled application experiments.
