# GC-II Audit 357 — Aggregate-Delta Capability Bound No-Go

## Status

- Construction and theorem: **PROVED**.
- Graph reachability/transitive-closure mechanism: **IMPORTED/KNOWN**.
- Universal finite bound `Omega_G <= F(DeltaR,DeltaI,DeltaA,DeltaL)` with no baseline-size/geometry term: **FALSIFIED** for the closure-gain definition below.
- Bounds augmented by baseline component geometry / interface exposure: **OPEN**.

## Setup

Let the operational world be a finite directed graph. Its capability closure is reachability. For a baseline graph `G0=(V,E0)` and an extension `E+`, define the raw Generative Novelty Gap

\[
\Omega_G(G_0,E_+) := |TC(E_0\cup E_+)\setminus TC(E_0)|,
\]

where `TC` contains non-reflexive ordered reachable pairs. This is dimensionless.

For this audit, each added interface/action is one zero-information, unit-resource directed transition. Thus an extension containing one new transition has the same aggregate increment vector

\[
(\Delta R,\Delta I,\Delta A,\Delta L)=(1,0,1,0)
\]

for every member of the family below. Relabeling resource/interface coordinates does not change the result.

## Bridge family

For arbitrary positive integers `p,q`, take vertices

\[
L=\{\ell_1,\ldots,\ell_p\},\qquad R=\{r_1,\ldots,r_q\}.
\]

The baseline contains a directed chain through `L`, a directed chain through `R`, and no edge from `L` to `R`:

\[
\ell_1\to\ell_2\to\cdots\to\ell_p,
\qquad
r_1\to r_2\to\cdots\to r_q.
\]

Add exactly one unit-cost transition

\[
e^+=(\ell_p,r_1).
\]

Every pair `(ell_i,r_j)` becomes reachable, and no such cross pair was reachable before. Hence

\[
\boxed{\Omega_G=pq.}
\]

The aggregate increment vector remains exactly `(1,0,1,0)` for all `p,q`.

## Theorem — no aggregate-only finite universal bound

There is no finite-valued function

\[
F:\mathbb R_+^4\to\mathbb R_+
\]

such that for every finite operational graph and extension

\[
\Omega_G\le F(\Delta R,\Delta I,\Delta A,\Delta L),
\]

when the four deltas record only aggregate extension quantities as above and omit baseline geometry/size.

### Proof

Assume such a finite `F` exists. Set

\[
C=F(1,0,1,0)<\infty.
\]

Choose `p=q=n` with `n^2>C`. The bridge family has delta vector `(1,0,1,0)` but `Omega_G=n^2>C`, contradicting the bound. QED.

The same construction also rules out every linear, polynomial, nonlinear, or interaction-term expression that is solely a finite function of these four aggregate deltas. The obstruction is not nonlinearity of `F`; it is missing baseline coupling geometry.

## Exact geometry-aware identity for a bridge edge

For a general baseline directed graph, add one edge `u->v` that is absent from the baseline transitive closure. Define

\[
Pred_0(u)=\{x:x=u\text{ or }x\leadsto_0 u\},\qquad
Succ_0(v)=\{y:y=v\text{ or }v\leadsto_0 y\}.
\]

Every newly created reachable pair must use the new edge, so

\[
TC(E_0\cup\{(u,v)\})\setminus TC(E_0)
=
(Pred_0(u)\times Succ_0(v))\setminus TC(E_0).
\]

Therefore

\[
\boxed{\Omega_G=
|(Pred_0(u)\times Succ_0(v))\setminus TC(E_0)|.}
\]

For the bridge family there are no pre-existing left-to-right pairs, giving `Omega_G=pq`.

This identity identifies the missing accounting coordinate: **exposure/coupling of the new operation to the baseline closure**, rather than the operation's aggregate cost alone.

## Checks

- `p=1` or `q=1`: `Omega_G=pq`; no degeneracy.
- Empty extension: `Omega_G=0`.
- Added edge already in baseline closure: novelty is zero; this is why the identity explicitly subtracts `TC(E0)`.
- Monotonicity in bridge-family `p,q`: nondecreasing and strictly increasing in either positive coordinate.
- Relabeling invariance: vertex labels do not affect closure cardinality.
- Composition: two bridge edges can overlap in generated pairs, so novelty is not generally additive.
- Dimensions: `Omega_G`, `DeltaA`, `DeltaI`, and `DeltaL` here are counts/dimensionless; `DeltaR` is normalized to one resource unit. A dimensional resource vector can replace it without affecting the counterexample.

## Scientific consequence

A useful Paper-II capability-accounting inequality cannot depend only on aggregate `DeltaR, DeltaI, DeltaA, DeltaL` unless one of those quantities is redefined to encode baseline exposure. At minimum, a structural term such as predecessor/successor exposure, baseline closure geometry, state-space scale, or an equivalent semantic coupling measure is necessary.

This is a no-go result about the proposed GC-II accounting architecture, not a claim that edge insertion sensitivity of transitive closure is new graph theory.
