# GC-II Audit 270 — Staged novelty triangle and directed-gauge collision

## Scope
Finite nonnegative typed budget semantics from Audits 265–269. No change to GC-I/main.

## Definition
For finite attainable cost sets X,Y subset R_+^d, define

Omega(X,Y) = max{1, sup_{y in Y} rho_X(y)},

rho_X(y) = inf_{x in X} max_i x_i/y_i,

using the extended coordinate convention: 0/0=0 and x_i/0=+infinity for x_i>0. Equivalently, Omega(X,Y) is the least alpha>=1 such that every y in Y has some x in X with x <= alpha y componentwise. For conservative extensions X subset Y this is the Audit-269 Generative Novelty Gap.

## Theorem 270.1 — staged novelty triangle
For finite X,Y,Z,

Omega(X,Z) <= Omega(X,Y) Omega(Y,Z).

In particular, for staged conservative extensions B subset C subset E,

Omega_G(B,E) <= Omega_G(B,C) Omega_G(C,E).

### Proof
Let alpha>Omega(X,Y) and beta>Omega(Y,Z), with finite values. For each z in Z choose y in Y with y<=beta z, then choose x in X with x<=alpha y. Hence x<=alpha beta z, so rho_X(z)<=alpha beta. Taking the supremum over z and then alpha down to Omega(X,Y), beta down to Omega(Y,Z) proves the claim. Infinite-factor cases are immediate. In the finite attained setting one may choose minimizing witnesses directly.

## Corollary 270.2 — logarithmic directed triangle
Define D(X,Y)=log Omega(X,Y), with log(+infinity)=+infinity. Then

D(X,Z) <= D(X,Y)+D(Y,Z).

Thus sequential generative novelty accumulates additively in log scale, while the raw multiplicative gap accumulates at most multiplicatively.

## Corollary 270.3 — no hidden amplification across certified stages
If Omega_G(B,C)<=a and Omega_G(C,E)<=b, then Omega_G(B,E)<=ab. Therefore a chain of locally certified capability extensions has a global certificate given by the product of stage certificates. This is not an additive R/I/A/L assumption: each stage may contain arbitrary Pareto interactions already represented by its typed attainable set.

## Sharpness
The inequality is sharp already in one dimension. Let B={ab}, C={b}, E={1}, for a,b>=1. Then Omega(B,C)=a, Omega(C,E)=b, and Omega(B,E)=ab.

## Edge and invariance audit
- Degenerate X=Y=Z gives Omega=1 and D=0.
- Empty baseline with nonempty target gives +infinity; the extended inequality remains valid.
- Zero target coordinates are handled by the same extended ratio convention as Audit 269.
- Coherent positive coordinate rescaling leaves every ratio and hence Omega and D unchanged.
- Removing dominated attainable vectors does not change the upward feasibility relation or the least dilation certificate.
- The theorem does not require convexity, linear scalarization, or additivity across coordinates.

## Prior-art collision
The proof exposes Omega as a directed multiplicative order/cone gauge. Logarithms of order-scaling gauges are closely related in mechanism to established Thompson/Hilbert cone geometries, where order is compared through multiplicative scaling factors and logarithms. Therefore the abstract triangle mechanism is IMPORTED/KNOWN in spirit and must not be advertised as a new metric theorem. The GC-II-specific value is the staged capability-accounting interpretation for the exact typed operational closure developed in Audits 265–269.

## Status ledger
- Staged multiplicative bound: PROVED.
- Log directed triangle: PROVED.
- Sharpness: PROVED.
- Positive unit-rescaling invariance: PROVED.
- Generic cone/order-gauge triangle mechanism: IMPORTED/KNOWN.
- Claim that Omega_G itself is a fundamentally new mathematical distance: FALSIFIED / not defensible.
- Operational interpretation as a staged certificate inside GC-II: CONDITIONAL candidate contribution.
- Extension to coupled/catalytic/nonadditive composition: OPEN.

## Reproducibility
`experiments/gc2_audit270_staged_novelty_triangle.py` exhaustively checks all nonempty-baseline nested triples B subset C subset E on the 2D grid {1,2}^2, tests the multiplicative and logarithmic inequalities, coherent unit rescaling, and an exact sharpness family.
