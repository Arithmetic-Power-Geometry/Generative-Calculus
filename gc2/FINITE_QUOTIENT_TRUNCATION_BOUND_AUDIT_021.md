# GC-II Finite-Quotient Truncation Bound Audit 021

## Scope

This audit follows `FUTURE_HORIZON_REVERSIBILITY_AUDIT_020.md`. It asks whether a finite audit horizon can become complete once the reachable future-capability quotient is known to be finite. GC-I on `main` is not modified. No novelty claim is made here.

## Setting

Let a finite deterministic operational world induce a finite reachable quotient `Q` of future-relevant states. Let `N = |Q|`. Each quotient state has a Boolean success label `lambda(q)` and each admissible action `a` induces a partial deterministic successor `delta(q,a)`.

For `h >= 0`, define `q ~_h r` iff every feasible action word of length at most `h` has the same success outcome from `q` and `r` (with infeasibility treated as an observable outcome if the operational semantics exposes it). Let `P_h` be the partition into `~_h` classes.

Exact future equivalence is `~_infty = intersection_h ~_h`.

## Theorem — finite quotient truncation

**Status: PROVED / IMPORTED-KNOWN mechanism.**

For a deterministic reachable quotient with `N` states,

`~_{N-1} = ~_infty`.

Equivalently, if two quotient states are not future-equivalent, then there exists a distinguishing continuation of length at most `N-1`.

### Proof

`P_0` partitions states by their immediately observable success/infeasibility labels. Each refinement step forms `P_{h+1}` from the current labels together with the tuple of `P_h`-classes reached by every action. Hence `P_{h+1}` refines `P_h`.

Whenever refinement is strict, the number of blocks increases by at least one. Starting with at least one block and ending with at most `N` blocks, there can be at most `N-1` strict refinements. Once a step is stable, deterministic successor signatures cannot create a later split: the stable partition is a congruence for all actions and therefore equals exact future equivalence. Thus stability is reached by depth at most `N-1`.

The bound is safe rather than claimed tight for every labeling convention.

## Reversibility corollary

**Status: PROVED in this specialization.**

For a round trip taking `x` to `x'` inside a known finite reachable future quotient of size `N`,

`Gamma_{N-1}(x; sigma,tau) = 0`

is sufficient to conclude exact all-future equivalence of `x` and `x'` under the quotient semantics.

This repairs the negative statement from Audit 020: there is no *uniform fixed* horizon across growing worlds, but a world-dependent finite certificate exists once `N` is bounded.

## Edge and degenerate cases

- `N=1`: horizon zero is complete.
- Empty action alphabet: horizon zero is complete once immediate labels agree.
- Partial actions: either encode infeasibility as an observable sink/outcome or compare enabled-action sets explicitly; otherwise the theorem can certify the wrong operational equivalence.
- If costs, vector budgets, errors, or task scales are part of future behavior, they must be represented in quotient labels/transitions. Omitting them proves only language equivalence of the reduced model, not GC whole-envelope equivalence.
- Infinite reachable quotients: the theorem does not apply.
- Nondeterministic/probabilistic worlds require a different equivalence and cannot inherit this proof without additional assumptions.

## Composition and monotonicity

The depth relations are monotone: `~_{h+1}` refines `~_h`. Exact-equivalent states remain equivalent under every finite horizon. For deterministic quotient composition, replacing a state by an exact-equivalent state preserves all continuation signatures represented in the quotient.

## Novelty collision

The proof is standard finite-state partition-refinement / Myhill-Nerode-style distinguishability. It is therefore **not a GC-II breakthrough**. Generic finite-state size already yields a truncation certificate; claiming `N-1` itself as novel would be incorrect.

## Decisive consequence for the Paper-II target

The open target must be stronger than generic state counting. Seek a bound

`H_G <= Phi(B_R, B_I, B_A, B_L, structural parameters)`

that certifies whole-envelope future equivalence **without first enumerating the full reachable quotient**, and whose proof essentially uses coupled vector budgets, endogenous changes to information/interfaces/actions/rules, or GC envelope structure.

A useful result would show that operational constraints force a much smaller effective distinguishing horizon than `N-1`, or provide a computable upper bound on the relevant quotient size from GC accounting primitives. If the bound collapses to generic finite-state cardinality, classify it IMPORTED/KNOWN rather than novel.

## Status update

- Uniform fixed finite horizon across growing worlds: FALSIFIED (Audit 020).
- Finite reachable deterministic quotient horizon `N-1`: PROVED / IMPORTED-KNOWN.
- Exact reversibility certification at horizon `N-1` under represented quotient semantics: PROVED.
- GC-specific truncation bound from `R/I/A/L` budgets and envelope structure without quotient enumeration: OPEN.
