# GC-II Future-Horizon Reversibility Audit 020

## Scope

This audit stress-tests the open trace-sensitive reversibility program after `ENDPOINT_REVERSIBILITY_INSUFFICIENCY_AUDIT_019.md`. It does not modify GC-I and does not claim novelty.

## Definitions

Let a finite deterministic operational world have states `S`, action alphabet `U`, partial transition map `delta`, and a task-success predicate on finite action words. For state `s` and horizon `h >= 0`, define the bounded future language

`L_h(s) = { w in U^* : |w| <= h and w is feasible from s and satisfies the designated success predicate }`.

Define bounded future distortion

`D_h(s,t) = 1[L_h(s) != L_h(t)]`.

For a round trip `sigma;tau` taking `x` to `x'`, define

`Gamma_h(x; sigma,tau) = D_h(x,x')`.

The all-horizon residual is

`Gamma_infty(x; sigma,tau) = sup_{h>=0} D_h(x,x')`.

These are dimensionless Boolean diagnostics. They are deliberately not called metrics.

## Proposition 1 — horizon monotonicity

**Status: PROVED (finite deterministic specialization).**

If `D_h(s,t)=1`, then `D_k(s,t)=1` for every `k >= h`. Equivalently, equality of future languages can only be lost, never recovered, as the observation horizon grows.

Proof: `L_h(s)` and `L_h(t)` are restrictions of `L_k(s)` and `L_k(t)` to words of length at most `h`. A distinguishing word of length at most `h` remains present at every larger horizon.

Edge cases: at `h=0`, states may be indistinguishable even when their nonempty futures differ. Empty action alphabets make every pair all-horizon equivalent under this diagnostic.

## Proposition 2 — finite-horizon false reversibility

**Status: PROVED (finite deterministic specialization).**

For every finite horizon `h`, there exists a pair of states `s_h,t_h` such that

`D_h(s_h,t_h)=0` but `D_{h+1}(s_h,t_h)=1`.

Construction: from both states expose the same unique action chain for `h` steps. At depth `h`, give only the continuation reached from `s_h` one additional success-producing action `g`; the corresponding continuation from `t_h` lacks it. No word of length at most `h` distinguishes the starts, while the length-`h+1` word does.

Therefore a round trip can appear capability-preserving at every preselected finite audit horizon while failing immediately beyond that horizon.

## Corollary — bounded tests cannot certify unrestricted reversibility

**Status: PROVED for the above class / KNOWN-IMPORTED mechanism.**

No fixed finite horizon `h` is a complete certificate for unrestricted future-capability restoration over an unbounded family of finite operational worlds. A GC-II experiment reporting `Gamma_h=0` must state the horizon and cannot silently promote that result to all-future reversibility.

## Finite-state positive boundary

**Status: PROVED/IMPORTED-KNOWN.**

For a fixed finite deterministic labelled transition system, all-future equivalence is decidable by standard partition refinement / language-equivalence methods. Thus the negative result is about a *uniform fixed audit horizon across growing worlds*, not undecidability in the finite model.

## Collision / novelty audit

The mechanism is classical finite-state distinguishability: bounded-depth observations can miss a later distinguishing continuation, while exact future equivalence is an automata/bisimulation-style notion. This audit therefore supplies a correctness boundary for GC-II but is **not** a breakthrough claim.

## Consequence for the open invariant

A defensible GC-II trace residual must either:

1. quantify the promised finite task/scale/error/budget horizon explicitly; or
2. compare exact future-equivalence classes on a finite reachable quotient; or
3. provide a proved truncation bound showing when a finite horizon is complete for the structured class under study.

The third option is the scientifically interesting target: seek a GC-specific truncation theorem whose bound depends essentially on vector budgets and endogenous coupled `R/I/A/L` transformations rather than generic finite-state size.

## Status update

- `Gamma_h`: PROVED useful bounded diagnostic, not a metric.
- Fixed-horizon certification of unrestricted reversibility: FALSIFIED.
- Exact finite-state all-future equivalence: IMPORTED/KNOWN machinery.
- GC-specific finite truncation bound under coupled capability accounting: OPEN.
