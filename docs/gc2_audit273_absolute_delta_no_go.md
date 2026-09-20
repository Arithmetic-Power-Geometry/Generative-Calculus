# GC-II Audit 273 — Absolute-delta no-go and normalized capability-accounting bound

## Scope
Finite nonnegative typed budget semantics from Audits 265–272.  Let `B` be a baseline attainable cost set and `E` an extension set.  Lower cost is better.  Let `P(E)` be the Pareto-minimal extension vectors and let

`Omega(B,E) = max(1, max_{e in P(E)} rho_B(e))`,

where, for strictly positive `e`,

`rho_B(e) = min_{b in B} max_i b_i/e_i`.

The extended zero-coordinate convention from Audit 267 applies outside the strictly-positive theorem below.

## Candidate target attacked
Can one universally bound multiplicative generative novelty using only absolute typed increments,

`Omega_G <= F(Delta_R, Delta_I, Delta_A, Delta_L)`,

without a baseline scale or positive floor?

## Theorem 273.1 — no scale-free finite absolute-delta bound
**Status: PROVED.**

Fix any `Delta>0`.  There is no finite function of that absolute delta alone that universally upper-bounds `Omega`.

Already in one active coordinate, for `epsilon>0`, take

`E_epsilon = {epsilon}` and `B_epsilon = {epsilon + Delta}`.

The baseline is within the fixed absolute additive allowance `Delta` of the extension, but

`Omega(B_epsilon,E_epsilon) = (epsilon+Delta)/epsilon = 1 + Delta/epsilon -> infinity`

as `epsilon -> 0+`.

The construction embeds into R/I/A/L by holding the other three coordinates equal and positive.  Thus the obstruction is not dimensional.

### Consequence
A universal claim of the form `Omega_G <= F(Delta R, Delta I, Delta A, Delta L)` is false when the Deltas are absolute additive quantities and `F` has no access to the operating scale.  Dimensional analysis already warns of this: `Omega_G` is dimensionless whereas absolute R/I/A/L increments generally carry their own units.

## Theorem 273.2 — normalized additive-delta bound
**Status: PROVED.**

Assume every `e in P(E)` is strictly positive coordinatewise.  Suppose there is a nonnegative allowance vector `Delta` such that for every `e in P(E)` there exists `b in B` satisfying

`b_i <= e_i + Delta_i` for every coordinate i.

Then

`rho_B(e) <= max_i (1 + Delta_i/e_i)`

and hence

`Omega(B,E) <= 1 + max_i Delta_i/m_i`,

where

`m_i = min_{e in P(E)} e_i > 0`.

### Proof
For the baseline witness `b` associated with `e`,

`b_i/e_i <= 1 + Delta_i/e_i`.

Taking the maximum over coordinates bounds the dilation of this witness; taking the minimum over baseline witnesses cannot increase it.  Then maximize over `P(E)` and use `e_i >= m_i`.  QED.

## Sharpness
**Status: PROVED.**

In one active coordinate, `E={m}`, `B={m+Delta}` gives

`Omega = 1 + Delta/m`,

so the normalized bound cannot be improved in general.

## Zero-coordinate boundary
**Status: PROVED as a no-go / CONDITIONAL for finite normalized bounds.**

If an extension vector has `e_i=0` while every relevant baseline witness has positive cost in coordinate i, the required multiplicative dilation is infinite.  Therefore a finite additive allowance at a zero operating scale does not imply finite multiplicative novelty.  Any finite theorem must either use the extended infinity semantics, impose positive floors, or replace multiplicative normalization with a different operational geometry.

## Monotonicity and invariance checks
- Enlarging `B` can only decrease `rho_B` and `Omega`.
- Enlarging the admissible additive allowance `Delta` weakens the bound monotonically.
- Under coherent positive coordinate rescaling `e_i,b_i,Delta_i,m_i -> s_i(e_i,b_i,Delta_i,m_i)`, every ratio `Delta_i/m_i` and `Omega` is unchanged.
- The theorem is dimensionally valid because only like-typed quantities are added and the final ratios are dimensionless.

## Composition note
The theorem is pointwise and does not assume additive decomposition of novelty.  For independent additive composition, Audit 269's max-composition law and Audit 270's staged multiplicative law remain the stronger compositional statements.  This audit supplies the missing scale condition for converting absolute typed improvements into an Omega bound.

## Exact verification
`experiments/audit273_absolute_delta_no_go.py` uses exact rational arithmetic and checks:

- 120,270 exhaustive finite 2-D positive-grid cases satisfying the additive-cover premise;
- 1,000 members of a fixed-Delta family with `Omega=n+1`, demonstrating unboundedness;
- 1,000 exact tightness instances for the normalized bound.

No floating-point tolerance is used.

## Prior-art collision
**Generic mechanism: IMPORTED/KNOWN.**  Multiplicative `(1+epsilon)` approximation of Pareto sets is established in multiobjective optimization; approximate Pareto-set theory explicitly uses coordinatewise multiplicative domination.  Weighted Tchebycheff/max-ratio scalarization is likewise established.  Therefore neither multiplicative normalization nor the elementary relative-error inequality is claimed as new mathematics.

The GC-II value is narrower: it decisively falsifies the scale-free absolute `F(Delta R,Delta I,Delta A,Delta L)` target inside the operational novelty calculus and states the weakest simple repair exposed by the counterexample — dimensionless relative increments or explicit positive operating floors.

Relevant prior-art anchors checked: Papadimitriou–Yannakakis approximate Pareto-set line as summarized in Herzel et al. (JGO 2021), Diakonikolas–Yannakakis (SIAM J. Comput. 2009), and weighted Tchebycheff literature.

## Ledger
- Universal finite `F(absolute Delta R, Delta I, Delta A, Delta L)` without scale: **FALSIFIED**.
- Fixed absolute delta with arbitrarily large `Omega`: **PROVED**.
- Positive-floor normalized bound `Omega <= 1 + max_i Delta_i/m_i`: **PROVED**.
- Sharpness: **PROVED**.
- Positive unit-rescaling invariance: **PROVED**.
- Zero-floor finite multiplicative bound: **FALSIFIED in general**.
- Multiplicative Pareto approximation / Tchebycheff mechanism: **IMPORTED/KNOWN**.
- Stronger bounds exploiting dependency structure, coupling, information generation, catalysts, or endogenous rules: **OPEN**.
