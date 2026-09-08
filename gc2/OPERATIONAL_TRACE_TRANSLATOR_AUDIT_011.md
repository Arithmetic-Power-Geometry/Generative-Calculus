# GC-II Operational-Trace Shared-Translator Audit 011

## Status
**PROVED — restricted finite specialization / KNOWN-IMPORTED mechanism.** This note does not assert novelty.

## Purpose
Lift the finite source-fibre obstruction from static task symbols to finite operational traces carrying task, scale, error, vector-resource, information, interface/action, and rule data, without changing GC-I on `main`.

## Model
Let `T` be a finite task index set. Each task `t` has a nonempty finite set of admissible traces `P_t`. A trace `p` carries

`sig(p)=(t,s,e,r,I,A,L,x,y)`

where `s` is scale, `e` is observable error, `r in R_+^d` is cumulative vector resource use, `I,A,L` are the information, interface/action, and rule sets actually used, `x` is the translator-visible operational observation, and `y` is the required target label/outcome.

For context `C=(B,I0,A0,L0)` define the feasible trace set

`P(C)={p : r(p)<=B componentwise, I(p) subseteq I0, A(p) subseteq A0, L(p) subseteq L0}`.

A deterministic shared translator is one function `h:X->Y` that must satisfy `h(x(p))=y(p)` for every trace in a specified required finite trace family `Q subseteq P(C)`.

## Theorem 1 — Operational trace fibre criterion
A deterministic shared translator exists on `Q` iff

`x(p)=x(q) => y(p)=y(q)` for all `p,q in Q`.

### Proof
Necessity: if one function `h` translates both traces and `x(p)=x(q)`, then `y(p)=h(x(p))=h(x(q))=y(q)`.

Sufficiency: on each observed fibre `Q_x={p in Q:x(p)=x}`, the hypothesis gives one required target label. Define `h(x)` to be that label on every nonempty fibre and arbitrarily elsewhere. Then `h(x(p))=y(p)` for every `p in Q`. QED.

This proof is independent of the numerical dimension of `r`; the budget only determines which traces enter `Q`.

## Corollary 1 — Taskwise feasibility does not imply whole-envelope translatability
It is possible that every trace is individually translatable while no single translator handles all traces: choose two feasible traces `p,q` with the same visible observation and distinct required labels. Each singleton admits a translator, but `{p,q}` fails Theorem 1.

## Theorem 2 — Exact auxiliary-interface lower bound on a fixed required trace family
Let

`m(Q)=max_x |{y(p): p in Q, x(p)=x}|`.

Suppose an added interface symbol `a(p)` from an alphabet of size `q` is made visible and the translator becomes `h(x,a)`. Then the minimum alphabet size allowing exact translation of all traces in `Q` is

`q_min(Q)=m(Q)`.

Hence the minimum fixed-width auxiliary interface information is

`b_min(Q)=ceil(log2 m(Q))` bits.

### Proof
Lower bound: on a fibre attaining `m(Q)`, traces demanding different target labels must receive different auxiliary symbols; otherwise two traces present the same pair `(x,a)` but demand different outputs. Thus `q>=m(Q)`.

Upper bound: independently within every `x`-fibre, enumerate its distinct demanded labels by symbols `1,...,m_x`, where `m_x<=m(Q)`, assign a trace the symbol of its demanded label, and define `h(x,a)` accordingly. QED.

## Proposition 3 — Budget monotonicity under observation-invariant trace inclusion
Fix `I0,A0,L0` and let `Q_B` contain all required traces feasible under vector budget `B`. If `B<=B'` componentwise and increasing budget only adds traces while leaving existing `(x,y)` pairs unchanged, then

`Q_B subseteq Q_B'` and `m(Q_B)<=m(Q_B')`.

Therefore `b_min(Q_B)<=b_min(Q_B')`.

This is a boundary result, not a universal resource/interface non-substitution theorem. If added resources refine `x`, create information, enable a new action/interface, change rules, or permit preprocessing before the shared translator, the conclusion need not hold.

## Degenerate and edge cases
- `Q=empty`: exact translation is vacuous; define `m(empty)=0`; no auxiliary symbol is operationally required.
- All fibres demand one label: `m=1`, so zero fixed-width auxiliary bits suffice.
- Vector resources: all inequalities are componentwise; no scalarization is assumed.
- Repeated traces and repeated tasks do not change the criterion; only distinct demanded labels within visible fibres matter.
- Error and scale matter only insofar as they alter feasibility, visibility, or the required output. Hiding them inside the trace while not exposing them to `h` can create collisions; exposing them can remove collisions.

## Composition warning
These theorems concern a single deterministic shared translator on a fixed feasible trace family. They do not imply a triangle inequality, compositional additivity, or a universal lower bound for general adaptive translators. In particular they do not repair the nonlinear `Omega_G` triangle-inequality falsification in Audit 010.

## Prior-art collision assessment
The proof mechanism is functional consistency plus pigeonhole distinguishability and therefore sits in mature neighborhoods including zero-error coding/confusability, deterministic functional compression, classification with repeated features, and communication complexity. The trace lift is useful GC-II bookkeeping but is not, by itself, a breakthrough.

## Consequence for the Paper-II program
The next nontrivial target must couple the translator-visible partition itself to admissible R/I/A/L transformations. A potentially meaningful theorem must price the cost of *refining a fibre* (by computation, acquired information, actions/interfaces, or rule changes), rather than merely count labels after the partition is fixed.
