# GC-II Audit 382 — Marginal Accounting Cannot Bound Pure Synergy

## Target
Paper-II item (5): test whether a capability-novelty gap can be bounded from separate resource, information, action/interface, and rule increments without assuming additivity.

## Setup
Let intervention channels be indexed by N={R,I,A,L}. For any subset S⊆N, let v(S)≥0 denote the operational capability value attainable when exactly the channels in S are upgraded relative to a fixed baseline, with v(∅)=0. This is deliberately agnostic about the eventual GC-specific definition of capability value; the theorem applies to every monotone set function v.

Define singleton marginal increments
Δ_i = v({i})-v(∅), i∈N,
and total novelty
Ω = v(N)-v(∅).

## Theorem 382.1 — singleton-marginal impossibility
There is no universal function F of only the singleton increments (Δ_R,Δ_I,Δ_A,Δ_L) satisfying
Ω ≤ F(Δ_R,Δ_I,Δ_A,Δ_L)
for all monotone finite capability systems, with finite F(0,0,0,0).

### Proof
For arbitrary M>0 define
v_M(S)=0 for every proper subset S⊊N, and v_M(N)=M.
This is a monotone set function. Every singleton increment is zero, but Ω=M. Since M is arbitrary, any finite F(0,0,0,0) is violated. ∎

The same construction works for any k≥2 channels and can be realized operationally as an AND-gated capability: the target action is admissible iff every required channel is present. Therefore the obstruction is not numerical pathology.

## Corollary 382.2 — every bounded-order marginal summary can fail
Fix k channels and q<k. Any accounting rule that observes only v(S) for |S|≤q cannot universally upper-bound v(N): choose v_M(S)=0 for all S⊊N and v_M(N)=M.

Thus pairwise interaction corrections do not solve the generic problem for four channels; a pure four-way interaction can remain invisible.

## Exact interaction identity
For a finite set function v, define its Boolean-lattice Möbius coefficients
m(T)=Σ_{S⊆T}(-1)^{|T|-|S|}v(S).
Then
v(N)=Σ_{T⊆N}m(T),
so
Ω=Σ_{∅≠T⊆N}m(T)
when v(∅)=0.

This is exact but is NOT claimed as GC-II novelty: Möbius transforms/Harsanyi dividends are established set-function/cooperative-game machinery. It also does not by itself give a useful upper bound because interaction coefficients need not be nonnegative and obtaining all of them requires 2^k subset evaluations.

## Consequence for the requested bound
A defensible GC-II bound
Ω_G ≤ F(ΔR,ΔI,ΔA,ΔL)
cannot be universal if each Δ denotes only an isolated/single-channel marginal. At least one of the following must be supplied:
1. explicit higher-order interaction terms;
2. structural assumptions limiting interaction order;
3. submodularity/diminishing-returns or another inequality controlling unseen coalitions;
4. a GC-derived certificate that bounds higher-order synergy without enumerating it.

Nonlinear algebra in the four singleton numbers alone is insufficient: the all-zero vector cannot distinguish zero novelty from arbitrarily large pure synergy.

## Edge/degenerate checks
- k=1: obstruction disappears; Ω=Δ_1 exactly.
- M=0: degenerate zero-novelty system.
- monotonicity: v_M is monotone.
- nonnegative capability: satisfied.
- rescaling: M↦αM preserves the counterexample.
- composition: independent AND-gated copies preserve hidden higher-order interaction; no additivity claim is required.
- dimensions: Ω and v share capability-value units; singleton Δ_i have those same units. The impossibility is not a dimensional mismatch.
- negative interactions: Möbius coefficients may be signed even for monotone v; do not interpret all m(T) as positive costs.

## Prior-art collision
The generic mathematical mechanism is known. Möbius inversion/Harsanyi dividends decompose set functions into coalition interactions; information theory likewise has established notions of synergy, with XOR as a canonical example where joint information is present although individual sources reveal none. Therefore neither “interactions matter” nor Möbius decomposition is a GC-II novelty claim.

## Status ledger
- Universal singleton-only capability-accounting bound: **FALSIFIED**.
- Failure of every fixed q<k marginal-order summary in unrestricted k-channel systems: **PROVED**.
- Exact Boolean Möbius decomposition: **IMPORTED/KNOWN**.
- Pairwise-only correction as a universal four-channel repair: **FALSIFIED**.
- Bound under bounded interaction order: **CONDITIONAL**.
- GC-specific compact certificate controlling unseen high-order interactions: **OPEN**.
- Nontrivial Ω_G itself: **OPEN**.

## Next breakthrough gate
Seek a GC-I-derived structural condition C_G that forces either (i) interaction order ≤q, or (ii) a computable envelope on Σ_{|T|>q}m(T), while separating matched systems with identical low-order marginals. Such a result would convert this impossibility boundary into a genuinely predictive capability-accounting theorem.
