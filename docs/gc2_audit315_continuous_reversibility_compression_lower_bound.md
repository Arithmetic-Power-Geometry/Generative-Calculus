# GC-II Audit 315 — Continuous reversibility-compression lower bound

## Status

- Local operational realization of an open cycle-space neighborhood: **PROVED** (from Audit 314, sharpened below).
- Exact continuous compression below cycle rank: **PROVED IMPOSSIBLE**.
- Linear-only restriction in Audit 314: **REMOVED**, under continuity.
- Invariance-of-domain mechanism: **IMPORTED/KNOWN**.
- Arbitrary discontinuous/set-theoretic encodings: **NOT RULED OUT** and not operationally claimed impossible.

## Question

Audit 314 proved that an exact *linear* summary of network directional irreversibility modulo state potentials needs at least

`beta = (n-1)(n-2)/2`

real coordinates on a complete `n`-state conversion network. Could a nonlinear but stable summary evade this lower bound?

## Operational setup

Let optimal directed conversion costs be `d(i,j)` and define the antisymmetric field

`A_ij = d(i,j)-d(j,i)`.

Two fields differing by a state potential gradient `h_j-h_i` have the same cycle circulations. Fix root `0`; the root-triangle circulation coordinates

`C_xy = A_0x + A_xy + A_y0`,  `1 <= x < y <= n-1`,

identify the quotient with `R^beta`, where `beta=(n-1)(n-2)/2`.

Audit 314's realizability construction is local and actually supplies an open neighborhood. Given any bounded antisymmetric field `a`, choose primitive directed costs

`c_ij = M + (lambda/2) a_ij`,  i != j,

with `M>0` and `lambda` sufficiently small. Direct edges are then strictly cheaper than every multi-edge path, so `d(i,j)=c_ij` and `A_ij=lambda a_ij`. Strict inequalities persist under sufficiently small perturbations. Consequently the realizable quotient contains a nonempty open set `U subset R^beta`.

## Theorem — continuous exact-summary lower bound

Let `S: U -> R^k` be a continuous summary of the directional-reversibility quotient on a nonempty open realizable set `U subset R^beta`. Suppose `S` is exact in the sense that distinct quotient points must have distinct summaries (equivalently, the summary permits exact recovery of the quotient on `U`). Then

`k >= beta = (n-1)(n-2)/2`.

### Proof

Exactness makes `S` injective. Assume `k<beta`. Compose `S` with the standard coordinate inclusion

`i: R^k -> R^beta`, `i(z)=(z,0,...,0)`.

Then `i o S: U -> R^beta` is continuous and injective. By Brouwer's invariance of domain, its image must be open in `R^beta`. But the image lies in the `k`-dimensional coordinate subspace `R^k x {0}^{beta-k}`, which has empty interior in `R^beta`. Contradiction. Therefore `k>=beta`.

## Tightness

The lower bound is attained by the `beta` root-triangle circulations themselves. They are linear, continuous, and complete for the quotient. Hence the minimum number of real coordinates for an exact **continuous** Euclidean summary is exactly

`beta = (n-1)(n-2)/2`.

## Consequences

1. Audit 314's `Theta(n^2)` barrier is not merely a linear-algebra artifact. It survives arbitrary nonlinear continuous encoders.
2. Any exact continuous scalar summary fails once `beta>1`, i.e. for `n>=4`.
3. Any exact continuous `O(n)`-coordinate summary fails asymptotically for unrestricted complete conversion networks.
4. The theorem concerns the irreducible directional quotient. The symmetric burden field is additional information and can only increase the requirements of a lossless full-cost representation.
5. Continuity is essential. Pure set cardinality does not forbid pathological discontinuous injections from higher-dimensional Euclidean spaces into `R`; therefore no stronger claim is made without finite-precision, robustness, measurability-plus-regularity, or algorithmic assumptions.

## Domain, edge, and composition checks

- `n=2`: `beta=0`; there is no cycle obstruction and the theorem is vacuous.
- `n=3`: `beta=1`; one signed triangle circulation is sufficient and necessary for the quotient.
- `n=4`: `beta=3`; no exact continuous one- or two-real-coordinate summary exists on an open realizable family.
- State relabeling changes the coordinate basis/sign convention but not `beta`.
- Positive coherent rescaling of costs rescales circulation coordinates and preserves the dimension obstruction.
- Adding a state-potential gradient leaves all root-triangle coordinates invariant.
- Under explicitly additive independent cost composition, signed circulation coordinates add; the dimension result itself is representation-theoretic and does not assume additivity of arbitrary physical compositions.
- Degenerate lower-dimensional model families can admit smaller summaries; the theorem requires an open `beta`-dimensional realizable family and therefore does not overclaim for constrained subclasses.

## Prior-art collision note

The topological obstruction is classical Brouwer invariance of domain: a nonempty open subset of `R^beta` cannot be continuously injected into `R^k` for `k<beta`. This mechanism is **IMPORTED/KNOWN**, not a GC-II novelty claim. The GC-II contribution is the operational bridge supplied by Audit 314: shortest-path conversion systems locally realize the full cycle-space quotient, so the classical topological dimension obstruction genuinely applies to exact continuous reversibility accounting rather than to an abstract unconstrained vector space.

## Scientific boundary after Audits 312–315

- One normalized scalar gap: **FALSIFIED as complete** (Audit 312).
- State-potential representation: **FALSIFIED universally** by cycle circulation (Audit 313).
- Exact linear compression below cycle rank: **IMPOSSIBLE** (Audit 314).
- Exact nonlinear continuous compression below cycle rank: **IMPOSSIBLE** (this audit).
- Finite-precision/robust approximate compression rates: **OPEN**.
- Structured sparse-network and constrained-model reductions: **OPEN**.

## Next target

Seek a quantitative robust version: under a specified metric and reconstruction error `epsilon`, lower-bound the number of bits or Lipschitz summary dimension needed to preserve all realizable cycle-space directions. This must be collision-checked against metric entropy, rate-distortion, Johnson-Lindenstrauss-type embeddings, communication complexity, and information-theoretic packing bounds before any novelty claim.
