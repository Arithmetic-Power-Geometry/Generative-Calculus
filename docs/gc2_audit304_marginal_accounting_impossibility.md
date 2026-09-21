# GC-II Audit 304 — Marginal-only capability accounting is impossible under cross-channel coupling

## Purpose

Audit 303 fixed a task-relative Generative Novelty Gap. This audit attacks the requested quantitative law

`Omega_G <= F(Delta R, Delta I, Delta A, Delta L)`

without silently assuming additivity. The central question is whether four *marginal* channel deltas can universally control novelty when operational admissibility depends on cross-channel relations.

## Setup

Use the typed state `z=(x,r,i,a,l)` from Audit 302. A channel summary `M(z)` records the four declared marginal channel states `(r,i,a,l)` but discards their coupling/correlation structure. Let `Delta_R,Delta_I,Delta_A,Delta_L` be any nonnegative marginal discrepancy measures satisfying identity of indiscernibles on each recorded marginal: equal recorded marginals imply the corresponding delta is zero.

A proposed marginal-only accounting law is **faithful at zero** when

`F(0,0,0,0)=0`.

This is the weakest meaningful No-Free-Capability normalization: no declared change should imply no positive upper allowance.

## Theorem 304.1 — marginal-sufficiency impossibility

**PROVED.** There is no universal faithful-at-zero bound

`Omega_G <= F(Delta_R,Delta_I,Delta_A,Delta_L)`

for the full typed operational class if the four deltas depend only on separate channel marginals while admissibility/capability may depend on cross-channel coupling.

### Exact witness

Take two binary latent channel coordinates `R,I in {0,1}`. Keep the exposed action set and rule label identical in both systems: `A={probe}`, `L={same-rule-label}`. Give both systems exactly the same one-coordinate marginals:

`P(R=0)=P(R=1)=1/2`,

`P(I=0)=P(I=1)=1/2`.

Baseline `S0` has anticorrelated support

`C0={(0,1),(1,0)}`.

Augmented `S1` has correlated support

`C1={(0,0),(1,1)}`.

Define an independently fixed binary task capability

`u(r,i)=1[r=i]`.

Then

`V_u(S0)=0`, `V_u(S1)=1`, hence `Omega_G >= 1` (and equals 1 for the singleton task family `{u}`).

But every separately recorded marginal is identical, as are the exposed action set and rule label, so

`Delta_R=Delta_I=Delta_A=Delta_L=0`.

Any faithful-at-zero marginal law would require `1 <= F(0,0,0,0)=0`, contradiction. QED.

The construction is dimensionless and finite. No probability estimation or asymptotics are involved.

## Corollary 304.1 — interaction terms are not optional bookkeeping

**PROVED.** A valid universal quantitative law must do at least one of the following:

1. include a discrepancy of the **joint operational structure** (couplings/correlations/admissibility relation);
2. include explicit interaction coordinates such as `Delta_RI, Delta_RA, ...` sufficient for the declared model class;
3. impose an independently testable factorization/separability assumption under which the joint structure is determined by the marginals.

Merely allowing nonlinear algebraic terms such as `Delta_R Delta_I` does **not** repair the witness, because all marginal deltas are zero. A nonlinear function of zeros still receives no information about the changed coupling.

## Theorem 304.2 — repaired metric bound

Let `d_joint(S1,S0)` be any discrepancy on the full operational object, and suppose every declared task value is `L_U`-Lipschitz with respect to it:

`|V_u(S1)-V_u(S0)| <= L_U d_joint(S1,S0)` for all `u in U`.

Then

`Omega_G^U(S1:S0) <= L_U d_joint(S1,S0)`.

**PROVED**, immediately by taking the positive part and supremum. This is mathematically correct but is **not promoted as a breakthrough theorem**, because the substantive burden is proving a nontrivial independently checkable Lipschitz relation for a concrete operational class.

The useful conclusion is negative: the desired GC-II bound cannot be universal in four marginal deltas alone unless those deltas jointly encode all capability-relevant coupling or the system class forbids hidden coupling changes.

## Exact collision test

`experiments/gc2_audit304_marginal_coupling_counterexample.py` enumerates all nonempty supports on two binary coordinates and groups them by one-coordinate marginals. It searches pairs with identical marginals but different equality-task value. The explicit correlated/anticorrelated witness is asserted exactly using rational arithmetic.

The finite search is a counterexample finder, not evidence of theorem novelty.

## Edge and composition audit

- Degenerate one-point channels: no coupling ambiguity exists; the obstruction disappears.
- If the full joint relation is itself included in `L`, then `Delta_L` need not vanish; the witness correctly says that `L` was not marginal after all.
- If `Delta_I` is defined as a complete metric on the entire joint operational state, it is likewise not a marginal information delta and the theorem does not apply.
- Relabeling both binary coordinates consistently preserves the obstruction.
- Independent Cartesian composition does not remove it; a hidden coupling discrepancy can be tensored with arbitrary unchanged systems.
- Nonlinear functions of marginal deltas cannot detect a direction on which all marginal deltas vanish.
- The result concerns sufficiency of summaries, not conservation of physical resources.

## Prior-art collision status

The mechanism is closely related to classical facts that marginals do not determine a joint distribution, to coupling/marginal problems, contextuality, database join consistency, and graphical-model interaction structure. Therefore the generic fact that identical marginals can hide different correlations is **IMPORTED/KNOWN** and is not claimed as a GC-II invention.

The GC-II consequence is specific and important: a four-scalar marginal capability-accounting law is mathematically impossible for the typed closure class unless interaction structure is represented or excluded. This prevents Paper II from making an overstrong universal quantitative claim.

## Status

- Marginal-only universal bound with `F(0)=0`: **FALSIFIED**.
- Finite correlated/anticorrelated witness: **PROVED**.
- Necessity of joint/interaction accounting or separability assumptions: **PROVED**.
- Generic marginal/coupling phenomenon: **IMPORTED/KNOWN**.
- Lipschitz full-joint repair: **PROVED but structurally generic**.
- A sharp non-tautological `F` for a restricted operational class with measurable interaction deltas: **OPEN**.
- Weakest useful factorization assumptions yielding a four-channel bound: **OPEN**.

## Next attack

Define a minimal interaction-complete delta system for finite typed closures. Test whether Möbius/ANOVA-style interaction coordinates, hypergraph factorization, or bounded-order dependency assumptions yield a quantitative `Omega_G` bound whose constants are operationally measurable rather than defined from the conclusion.
