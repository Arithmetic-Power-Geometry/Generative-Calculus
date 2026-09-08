# GC-II Reversibility-Gap Audit 010

## Status

- Naive claim that the current nonlinear single-target `Omega_G` is a directed metric/quasi-metric: **FALSIFIED**.
- Any reversibility invariant whose metric properties are inferred from a triangle inequality for this `Omega_G`: **FALSIFIED without additional assumptions on the augmentation penalty**.
- Symmetric round-trip cost `Gamma_G(x,y)=Omega_G(x->y)+Omega_G(y->x)`: **well-defined as a nonnegative symmetric diagnostic**, but **NOT promoted to a metric/invariant theorem** under the present penalty.
- Repair target: **OPEN**. Require either a subadditive composition-compatible penalty, or explicitly retain nonmetric interaction surplus as a separate quantity.

## Candidate under audit

The current finite `Omega_G` uses

\[
F(\Delta R,\Delta I,\Delta A,\Delta L)
= r+d+rd,
\]

where `r` is total added resource budget and `d` is the number of newly supplied information/action/rule gates. The `rd` term was intentionally introduced to permit nonlinear cross-channel interaction.

A tempting next step is to treat directed `Omega_G` as a quasi-metric and define a reversibility gap from forward and reverse distances. That step is invalid in general.

## Exact triangle counterexample

Take three operational states `x,y,z`, baseline context with zero resource budget and no information, and edges

- `x -> y`: resource cost 1, no gate requirement;
- `y -> z`: resource cost 0, requires information token `i`.

Then

\[
\Omega_G(x\to y)=F(1,0)=1,
\]

and, when the second conversion is considered from `y` under the same baseline convention,

\[
\Omega_G(y\to z)=F(0,1)=1.
\]

But the composed path `x -> y -> z` simultaneously requires one unit of resource augmentation and the information token, hence

\[
\Omega_G(x\to z)=F(1,1)=1+1+1=3.
\]

Therefore

\[
\Omega_G(x\to z)=3
>2
=\Omega_G(x\to y)+\Omega_G(y\to z).
\]

The triangle inequality fails exactly.

## Why the failure matters

The failure is not a coding bug. It is caused by the positive cross-channel term. In general, for disjoint resource and gate increments,

\[
F(r_1+r_2,d_1+d_2)-F(r_1,d_1)-F(r_2,d_2)
= r_1d_2+r_2d_1.
\]

Thus cross-channel complementarity can create a strictly positive **composition surplus**. A capability-accounting law that permits such complementarity cannot simultaneously inherit metric composition for free.

Define the path-composition surplus

\[
\Xi_F(a,b)=F(a\oplus b)-F(a)-F(b).
\]

For the current penalty, `Xi_F` can be positive. This quantity is presently a diagnostic, not a novelty claim.

## Consequence for reversibility

The symmetric round-trip quantity

\[
\Gamma_G(x,y)=\Omega_G(x\to y)+\Omega_G(y\to x)
\]

is always nonnegative and symmetric whenever both directed gaps are finite. However, without directed triangle behavior it must not be advertised as a metric. Moreover, zero round-trip cost identifies mutual zero-gap convertibility rather than literal state identity unless the operational equivalence classes are quotiented first.

A defensible metric-like construction therefore needs two explicit conditions:

1. **separation on operational equivalence classes**, and
2. **subadditivity under augmentation composition**, e.g.
   \[
   F(a\oplus b)\le F(a)+F(b).
   \]

The present nonlinear penalty deliberately does not satisfy condition 2.

## Prior-art collision boundary

Forward/reverse cost asymmetry and irreversibility are mature ideas in thermodynamics, resource theories, computation, and directed conversion theory. The mere difference or sum of forward and reverse conversion costs is therefore **IMPORTED/KNOWN territory**, not a GC-II breakthrough. GC-II should only claim additional content if the operational R/I/A/L coupling yields a theorem that is not a restatement of established irreversibility or directed-distance structure.

## Scientific consequence

This falsification sharpens the Paper-II program. There is a genuine design fork:

- impose a composition-compatible/subadditive penalty to obtain directed-distance and round-trip metric structure; or
- retain superadditive cross-channel interactions and explicitly study the resulting nonmetric composition surplus.

The second route is potentially more faithful to GC-II capability accounting because it preserves nonlinear R/I/A/L interaction, but its novelty remains **OPEN** pending prior-art and theorem-level separation.
