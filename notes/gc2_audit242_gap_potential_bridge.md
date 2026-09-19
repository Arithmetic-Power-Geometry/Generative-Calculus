# GC-II Audit 242 — Exact gap-potential bridge for sequential capability cost

## Purpose
Bridge the exact finite translator repair gap of Audit 239 to the sequential typed operational closure of Audit 241 without assuming an arbitrary defect-to-cost calibration. The bridge is derived from how much an admissible operation can actually reduce the exact translator gap.

## Setup
For every finite operational state x, let Omega_add(x) be the exact minimum missing-incidence repair count from Audit 239 for the translator instance represented by x. Accepting states satisfy Omega_add(x)=0. Let an enabled typed operation o take x to x' with scalar execution cost c(o,x,x') >= 0.

Define its realized gap reduction

    delta_Omega(o;x,x') = [Omega_add(x)-Omega_add(x')]_+.

For a class of admissible executions define the operation efficacy envelope

    rho(o) = sup { delta_Omega(o;x,x') : o enabled at x, x' in T_o(x) }.

For positive-cost transitions define the global capability-efficiency constant

    eta = sup { delta_Omega(o;x,x') / c(o,x,x') : c(o,x,x')>0 }.

Zero-cost transitions that reduce Omega_add are treated separately; if one exists, eta is effectively infinite and no positive lower bound follows.

## Gap-potential lower bound — PROVED
For every finite admissible execution pi=(x0,o1,x1,...,on,xn) ending in an accepting state Omega_add(xn)=0,

    Omega_add(x0) <= sum_i delta_Omega(oi;x_{i-1},xi) <= sum_i rho(oi).

Proof. Write Di=Omega_add(x_{i-1})-Omega_add(x_i). Since sum_i Di=Omega_add(x0)-Omega_add(xn)=Omega_add(x0), and Di <= [Di]_+=delta_Omega_i termwise, the first inequality follows. The second is the definition of rho. Importantly, Omega_add need not be monotone along the path; temporary worsening is allowed.

If no zero-cost transition reduces Omega_add and eta<infinity, then

    Omega_add(x0) <= eta C(pi),

hence

    Omega_seq(x0,F) >= Omega_add(x0)/eta.

This is a calibrated lower bound because eta is measured in translator-gap units reduced per operational-cost unit, not inserted as an unrelated metric conversion.

## No-Free-Capability corollary — CONDITIONAL / PROVED under explicit assumptions
If Omega_add(x0)>0, every zero-cost admissible transition has delta_Omega=0, and eta<infinity, then every accepting execution has strictly positive cost and

    Omega_seq >= Omega_add(x0)/eta > 0.

Thus the earlier cost-rescaling objection is not evaded by fiat: rescaling operational costs rescales eta inversely and leaves the inequality dimensionally covariant.

## Discrete bounded-effect corollary — PROVED
Suppose every capability-relevant transition costs at least c_min>0 and can reduce Omega_add by at most k finite incidences. Then eta <= k/c_min and

    Omega_seq >= c_min * ceil(Omega_add(x0)/k)

when costs are charged per transition by at least c_min. The ceiling follows because at least ceil(Omega_add/k) positive-reduction transitions are necessary; nonreducing transitions only add cost.

Special case k=1: Omega_seq >= c_min Omega_add.

## Edge and degenerate cases
- Omega_add(x0)=0: bound gives zero, correctly allowing already-present capability.
- Unreachable F: Omega_seq=infinity, so the lower bound remains valid.
- A zero-cost gap-reducing operation destroys the positive-cost conclusion; this is an explicit falsifier, not hidden by the theorem.
- Unbounded gap reduction per unit cost gives eta=infinity and only the trivial lower bound zero.
- Temporary increases of Omega_add do not invalidate the proof because positive parts dominate the telescoping signed change.
- Nondeterministic transitions are covered by taking the efficacy supremum over all admissible realized edges; robust/worst-case execution semantics would require a separate quantifier convention.

## Composition and dimensions
Omega_add is dimensionless (incidence repairs). eta has units repairs/cost. Therefore Omega_add/eta has cost units. Concatenating paths preserves the telescoping argument. The bound is invariant under a common relabeling of worlds/messages that preserves Omega_add and transition costs. Under cost rescaling c -> alpha c, eta -> eta/alpha and Omega_add/eta -> alpha Omega_add/eta, exactly matching operational cost scaling.

## Exactness example
Let Omega_add(x0)=m. Provide an operation that at cost c removes exactly k independent missing incidences until the final residual, with no prerequisites beyond availability. Then the optimal cost is c ceil(m/k), attaining the discrete lower bound when each operation is charged c and has capacity k (with the final operation possibly partially used). Thus the bound is not intrinsically vacuous.

## Counterexample catalog
1. Zero-cost reducer: Omega_add=1 and a free operation adds the sole missing incidence. Omega_seq=0; positive No-Free-Capability fails.
2. Arbitrarily efficient reducer family: operations reduce one gap unit at cost 1/n. In an infinite model eta=infinity and infimum cost can be zero.
3. Prerequisite overhead: an operation of cost 1 reduces one gap unit but requires a cost-100 prerequisite. The lower bound gives 1 while true Omega_seq>=101; therefore the bridge is a lower bound, not generally complete.
4. Temporary damage: path gaps 2 -> 3 -> 1 -> 0 has positive reductions 0,2,1 whose sum 3 dominates net decrease 2; proof remains valid.

## Prior-art collision boundary
The proof is a potential/amortized or Lipschitz-style lower-bound argument over a weighted transition system. Such techniques are generic in optimization, algorithms, planning and shortest-path lower bounds. Therefore the telescoping inequality itself is IMPORTED/KNOWN in mechanism and is not claimed as a new mathematical paradigm.

The GC-II-specific value is narrower: Audit 239 supplies an exact operational translator feasibility potential rather than an arbitrary heuristic, while Audit 241 supplies typed generated transitions. Their bridge gives a defensible capability-accounting inequality and identifies exactly what additional structure would be required for a stronger novelty claim: a GC-derived non-generic upper bound on eta (or typed eta_R,eta_I,eta_A,eta_L and interaction terms) forced by projection/generation semantics rather than assumed from an operation table.

## Status ledger
- Exact telescoping gap-potential inequality: PROVED.
- Sequential lower bound Omega_seq >= Omega_add/eta: PROVED under finite eta and no zero-cost gap reducer.
- Discrete bound c_min ceil(Omega_add/k): PROVED under stated bounded-effect assumptions.
- Positive No-Free-Capability from nonzero exact gap plus bounded operational efficacy: CONDITIONAL / PROVED.
- Bound invariant/covariant under relabeling and cost rescaling as stated: PROVED.
- Bound generally equals true sequential cost: FALSIFIED by prerequisite-overhead counterexample.
- Potential/amortized proof mechanism: IMPORTED/KNOWN.
- GC-specific theorem forcing a finite eta from GC-I projection irreducibility alone: OPEN and unlikely without operational semantics, consistent with Audits 232–233.
- Typed nonlinear capability-accounting law constraining eta from R/I/A/L generation structure: OPEN; strongest next target.
