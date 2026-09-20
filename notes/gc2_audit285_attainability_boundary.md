# GC-II Audit 285 — Attainability is essential in the persistent-summary lower bound

## Status

- Internal-certificate persistent-summary lower bound from Audit 284: **PROVED under attainable decoding**.
- Same lower bound with arbitrary synthetic decoded representatives: **FALSIFIED**.
- Exponential separation between internal and external directed multiplicative certificate size: **PROVED**.

## Setup

Work in logarithmic/exponent coordinates. For `m >= 1`, let `d=2m`, choose a gap `g>0`, and define the attainable family

\[
Y_m=\{y^b:b\in\{0,1\}^m\},
\]

where each pair is

\[
(y^b_{2j-1},y^b_{2j})=
\begin{cases}
(g,0),&b_j=1,\\
(0,g),&b_j=0.
\end{cases}
\]

A center `s` covers target `y` at log-radius `rho` when

\[
s_i-y_i\le \rho\qquad\forall i.
\]

This is the logarithmic form of coordinatewise multiplicative coverage `s_i <= alpha y_i`, with `rho=log(alpha)` in a common log base.

Assume

\[
0\le \rho<g.
\]

## Internal certificate

If centers must be attainable (`s in Y_m`), every distinct pair of attainable vectors fails directed coverage in both directions: at a module where their bits differ, the candidate center has coordinate `g` while the target has `0`, hence `g>rho`.

Therefore every attainable center covers exactly itself and

\[
C^{\mathrm{int}}_\rho(Y_m)=|Y_m|=2^m.
\]

This is the Audit-280/Audit-284 obstruction.

## External certificate collapse

Now allow a decoded summary state to output a synthetic accounting vector not required to be attainable. Define the single center

\[
z=(\rho,\rho,\ldots,\rho).
\]

For every `y in Y_m` and every coordinate,

- if `y_i=0`, then `z_i-y_i=rho`;
- if `y_i=g`, then `z_i-y_i=rho-g <= rho`.

Hence `z` covers every target. Thus

\[
C^{\mathrm{ext}}_\rho(Y_m)=1.
\]

Consequently

\[
\frac{C^{\mathrm{int}}_\rho(Y_m)}{C^{\mathrm{ext}}_\rho(Y_m)}=2^m=2^{d/2}.
\]

The same statement in multiplicative coordinates uses pair values `(r,1)` and `(1,r)`, `r>alpha>=1`, with the synthetic center `(alpha,...,alpha)`. It covers every target although it need not be operationally attainable.

## Operational consequence

Audit 284's bit lower bound

\[
k\ge \lceil\log_2 C^{\mathrm{int}}_\alpha(Y)\rceil
\]

is valid only when a persistent summary must decode to an **attainable operational witness** (or to another class constrained tightly enough that its covering number is comparable to the internal one). If arbitrary synthetic accounting vectors are admissible, this family needs only one summary state even though the internal certificate requires `2^m` representatives.

Therefore capability accounting must distinguish at least two semantics:

1. **witness-preserving accounting** — decoded summaries correspond to executable/attainable capabilities;
2. **descriptive accounting** — decoded summaries may be synthetic abstractions.

Internal certificate complexity controls the first, not automatically the second.

## Edge cases and checks

- `m=0`: both certificate sizes are 1 by the empty-product convention; the exponential separation begins at `m>=1`.
- `rho=0`: the synthetic all-zero center already covers every nonnegative target under the one-sided directed relation. This exposes that one-sided coverage is deliberately permissive for external centers.
- `rho=g`: distinct attainable centers may begin covering other targets, so the internal `2^m` statement requires `rho<g`.
- Positive rescaling of the original multiplicative units leaves the ratio formulation unchanged.
- Composition over independent modules multiplies the internal certificate size (`2^m`) while the external synthetic cover remains one center.

## Novelty boundary

The abstract distinction between proper/internal covers and covers with unrestricted centers is standard metric/covering-set territory; no novelty is claimed for that generic phenomenon. The GC-II-specific consequence is a falsification boundary for the operational persistent-memory theorem: **attainability/executability of decoded witnesses is not cosmetic; removing it can erase an exponential lower bound.**

## Next target

Define a decoder class `D` between the two extremes and study

\[
C_{\alpha,D}(Y)=\min\{|S|:S\subseteq D,\; S\text{ alpha-covers }Y\}.
\]

Seek operational conditions on `D` (soundness, realizability gap, bounded deficiency, or verified refinement to attainable witnesses) under which `C_{alpha,D}` remains comparable to the internal certificate without making the theorem tautological.
