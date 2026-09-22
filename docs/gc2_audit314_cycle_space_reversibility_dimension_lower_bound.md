# GC-II Audit 314 — Cycle-space reversibility dimension lower bound

## Scope
This audit continues Audit 313. It asks whether the network-level directional asymmetry of finite scalar-cost operational conversion can be losslessly compressed, after removing state-potential effects, into fewer than cycle-rank many continuous linear coordinates.

## Setting
Let V={1,...,n}, n>=2. For finite directed optimal conversion costs d(i,j), define

A_ij = d(i,j)-d(j,i),

so A is antisymmetric. A state-potential field has the form

(grad h)_ij = h_j-h_i.

Potential fields are operationally circulation-free and have dimension n-1 (constants in h are irrelevant).

For the complete undirected support, the vector space of antisymmetric edge fields has dimension m=n(n-1)/2. Hence its quotient by gradients has dimension

beta = m-(n-1) = (n-1)(n-2)/2.

The issue is whether shortest-path realizability secretly collapses this quotient. It does not.

## Theorem 314.1 — Local realizability of every antisymmetric direction [PROVED]
For every antisymmetric edge field a on the complete graph, there exists lambda_0>0 such that for every 0<lambda<lambda_0 there is a positive directed primitive-cost network whose optimal shortest-path costs satisfy

A_ij = lambda a_ij

for every ordered pair.

### Proof
Let M>0 and set primitive directed edge costs

c_ij = M + (lambda/2) a_ij,  i != j.

Write K=max_{i<j}|a_ij|. If K=0 the claim is trivial. Choose lambda K < 2M/3. Then every direct edge has cost at most M+lambda K/2, while every path with at least two edges has cost at least 2(M-lambda K/2). The chosen inequality gives

M+lambda K/2 < 2M-lambda K,

so every direct edge is strictly cheaper than every path of length >=2. Therefore d(i,j)=c_ij and

d(i,j)-d(j,i)=lambda a_ij.

Thus an open neighborhood of the symmetric complete-cost point realizes every antisymmetric direction. QED.

Edge cases: n=2 gives beta=0; K=0 is already a gradient (zero field); all costs remain positive under the displayed bound.

## Theorem 314.2 — Exact linear compression lower bound modulo potentials [PROVED]
Consider any linear summary T of network asymmetry that is required to distinguish all locally realizable asymmetry fields modulo state potentials: T(A)=T(A') may occur only if A-A'=grad h. Then the output dimension k of T must satisfy

k >= beta = (n-1)(n-2)/2.

### Proof
By Theorem 314.1, every antisymmetric direction occurs locally in the operational shortest-path model. The antisymmetric edge space has dimension m. The gradient subspace has dimension n-1. A linear map that is injective on the quotient must have rank at least dim(E/Grad)=m-(n-1)=beta. Rank(T)<=k, hence k>=beta. QED.

## Theorem 314.3 — Root-triangle coordinates attain the bound [PROVED]
Fix root r. For every unordered pair x<y distinct from r, define

C_xy(A)=A_rx + A_xy + A_yr.

There are exactly beta such coordinates. They vanish simultaneously iff A is a gradient (Audit 313), so the map C is injective on the quotient. Therefore beta is both necessary and sufficient for exact *linear* representation of directional asymmetry modulo potentials.

This is a complete finite criterion, not merely a lower bound.

## Consequence for GC-II reversibility accounting
A single scalar reversibility gap is not merely incomplete by counterexample. For n-state complete scalar-cost networks, exact continuous linear accounting of directional irreversibility after quotienting state-potential effects has an intrinsic cycle-space dimension

(n-1)(n-2)/2 = Theta(n^2).

Accordingly, any proposed O(n)-sized family of linear state scores cannot be network-complete without additional structural restrictions. Sparsity changes beta to the usual cycle rank m-n+c for c connected components.

## Composition
Under explicitly additive independent cost composition, A fields add. Root-triangle circulation coordinates therefore add componentwise. This avoids the cancellation blindness of the absolute normalized scalar Gamma_rev, although opposite signed circulations can legitimately cancel in the composed field.

## Prior-art collision / novelty discipline
The incidence-space/cycle-space dimension formula, gradients versus circulations, and rank-nullity argument are IMPORTED/KNOWN graph-theoretic mechanisms. GC-II must not claim them as new mathematics. The validated operational consequence is narrower: shortest-path realizability does not remove the cycle-space degrees of freedom, so a network-complete linear reversibility account cannot generally be compressed below cycle rank after quotienting potential effects.

## Status
- Local realization of every antisymmetric direction by positive shortest-path conversion networks: PROVED.
- Cycle-rank lower bound for exact linear summaries modulo potentials: PROVED.
- Root-triangle coordinates attaining the bound: PROVED / underlying cycle-space mechanism IMPORTED/KNOWN.
- Universal one-scalar or O(n) linear network reversibility account: FALSIFIED for unrestricted complete networks as n grows.
- Nonlinear/discontinuous encodings: NOT COVERED; cardinality tricks are intentionally outside the operational compression claim.
- Lower bounds under finite precision, Lipschitz summaries, vector resources, stochastic convertibility, or restricted sparse operational classes: OPEN.
