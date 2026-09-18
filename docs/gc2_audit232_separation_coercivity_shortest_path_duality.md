# GC-II Audit 232 — Separation/coercivity boundary and shortest-path duality

Status date: 2026-09-18
Branch scope: `gc2-capability-accounting-lab` only. GC-I `main` remains frozen.

## Question
Audit 231 reduced intrinsic operational payload to the extended directed pseudometric

\[
d(x,y)=\inf_{\pi:x\to y} c(\pi).
\]

Can GC-I proper-projection irreducibility alone force `d(x,y)>0` for a genuine capability change, and can the desired closure-escape / complete-monotone theorem be obtained non-tautologically from this geometry?

## Result A — irreducibility does not imply metric separation

**Status: FALSIFIED (without an independent coercivity assumption).**

Take two behaviorally distinct quotient states `x != y`. For every integer `n>=1`, admit a direct translator `tau_n:x->y` with cost `1/n`. Suppose none is free. Then every individual translator has strictly positive cost and `x,y` remain distinct, yet

\[
d(x,y)=\inf_{n\ge1}1/n=0.
\]

Nothing in projection irreducibility by itself excludes such an operational family: irreducibility says that the global object is not recoverable from a stipulated proper projection, not that admissible recovery/translation mechanisms have a positive minimum cost. Thus

\[
\text{proper-projection irreducibility}\not\Rightarrow d(x,y)>0
\]

unless a further hypothesis links projection loss to the operational cost scale.

This remains true even if every nonidentity primitive has positive cost. Pointwise positivity is weaker than uniform positivity/coercivity.

## Result B — weakest clean finite coercivity lemma

Let the operational transition system be finite (or, more generally, assume a uniform lower bound `epsilon>0` on every non-free primitive transition after quotienting zero-cost reachability). Let path cost be nonnegative and at least the sum of primitive lower bounds. If `x` and `y` are not identified by zero-cost reachability and every path from `x` to `y` uses at least one non-free primitive, then

\[
d(x,y)\ge \epsilon>0.
\]

**Status: PROVED but generic.** This is a coercivity/discreteness assumption, not a consequence of GC-I.

Edge cases:
- unreachable `y`: `d(x,y)=+infinity`;
- zero-cost cycles: quotient them first or separation fails;
- infinitely many positive costs tending to zero: the lemma fails without uniform `epsilon`;
- nonadditive path costs: the conclusion needs an explicit lower-bound composition axiom;
- asymmetric systems: no claim is made about `d(y,x)`.

## Result C — finite closure escape has an exact dual, but it is shortest-path theory

For a finite directed graph with edge costs `c(u,v)>=0`, define operational budget closure

\[
C_B(x)=\{y:d(x,y)\le B\}.
\]

For fixed source `x`, shortest-path distance has the potential dual

\[
d(x,y)=\sup_{\phi}\{\phi(y)-\phi(x):\phi(v)-\phi(u)\le c(u,v)\ \forall(u,v)\in E\}.
\]

Therefore, for finite reachable `y`, the following are equivalent:

1. **Operational escape:** `y` is not in `C_B(x)`.
2. **Geometric distance:** `d(x,y)>B`.
3. **Dual certificate:** there exists a feasible potential `phi` with `phi(y)-phi(x)>B`.
4. **Computational criterion:** the shortest-path optimum from `x` to `y` exceeds `B`.

The proof is ordinary shortest-path LP duality. A feasible potential gives a lower bound on every path by telescoping. Taking `phi(v)=d(x,v)` (on the reachable finite component, with the usual handling of infinities) attains the bound because triangle inequality gives `d(x,v)-d(x,u)<=c(u,v)`.

**Status: PROVED / IMPORTED-KNOWN mechanism.** It supplies a rigorous operational/geometric/computational equivalence but is not a GC-II novelty claim.

## Consequence for Paper-II items (3), (4), and (6)

A Closure-Escape theorem based only on `y outside C_B(x) iff d(x,y)>B` is definitional; adding the potential certificate makes it computationally useful but places it squarely inside shortest-path/LP duality. Likewise, the family of feasible 1-Lipschitz directed potentials is a complete separator for finite budgeted reachability, but generic cost geometry already supplies it.

Thus a publishable GC-II theorem must add a specifically generative statement, for example a lower bound on **which dual potentials can be induced from proper projections** or a theorem forcing coercivity from an independently measurable projection defect. Neither is proved here.

## No-Free-Capability status

- `nonfree primitive => positive primitive cost`: insufficient.
- uniform positive primitive lower bound after zero-cost quotient: sufficient for finite/discrete systems, but assumed.
- GC-I proper-projection irreducibility alone => positive operational distance: **FALSIFIED**.
- projection defect `Delta_P` plus an operational regularity law implying `d(x,y)>=g(Delta_P)>0`: **OPEN**.

## Prior-art collision boundary

The infimal path-cost construction is an extended directed Lawvere/pseudoquasimetric. Separation is an additional property, not automatic. The potential characterization is standard shortest-path linear-program duality / difference constraints. Resource theories similarly begin by declaring free states/operations; non-free status alone does not canonically determine a positive quantitative cost.

Accordingly, none of Result A–C should be advertised as a new mathematical mechanism. The value of this audit is a decisive novelty boundary: GC-II needs a **projection-to-cost coercivity law with independently justified units/regularity**, not merely metricization or shortest-path duality.

## Ledger

| Candidate | Status |
|---|---|
| GC-I irreducibility alone forces `d>0` | **FALSIFIED** |
| positive cost of each nonfree primitive forces `d>0` | **FALSIFIED** in infinite/non-uniform systems |
| uniform post-quotient coercivity `epsilon>0` forces separation | **PROVED / generic** |
| budget closure escape iff shortest-path distance exceeds budget | **PROVED / definitional+known** |
| finite dual-potential certificate for escape | **PROVED / IMPORTED-KNOWN** |
| generic directed potentials as GC-specific complete monotones | **FALSIFIED as novelty** |
| GC-I projection defect forces a quantitative coercivity modulus | **OPEN** |

## Next attack

Define a projection defect without importing a metric by fiat, then test whether any natural axioms can imply a nonzero coercivity modulus. Immediately collision-test against data processing / Blackwell deficiency, reconstruction error, rate-distortion, communication complexity, marginal consistency, sheaf/contextuality obstructions, database joins, and CSP width. A candidate survives only if its positive residual cannot be reproduced by an ordinary estimation/communication/reconstruction problem with the same observable interface.
