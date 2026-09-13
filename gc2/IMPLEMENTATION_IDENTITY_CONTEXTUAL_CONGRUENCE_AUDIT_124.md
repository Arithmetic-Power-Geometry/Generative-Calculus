# GC-II Audit 124 — Implementation Identity and Contextual-Congruence No-Go

## Scope

Audit 123 left implementation-linked compositional realization as the next defensible route: two recursively executable implementations might be indistinguishable in isolation yet become distinguishable after sequential composition because hidden implementation identity/state affects later execution.

This audit tests that route before introducing any new Omega_G.

## Definitions

Let P be a set of implementations, O a set of observations, obs:P->O an observation map, and C a family of admissible one-hole implementation contexts containing the identity context. Define standalone observational equivalence

p ~obs q iff obs(p)=obs(q).

Define contextual equivalence

p ~ctx q iff obs(C[p])=obs(C[q]) for every C in C.

Assume C is closed under context composition whenever the corresponding compositions are admissible.

## Theorem 124.1 — Contextual closure absorbs implementation-identity witnesses

STATUS: PROVED.

If p ~ctx q, then no admissible context can distinguish p and q by the declared observations. In particular, if sequential composition with r is represented by an admissible context C_r[-], then

obs(C_r[p]) = obs(C_r[q]).

Therefore a claimed implementation-identity obstruction of the form

p and q are operationally equivalent, but some admissible composition distinguishes them

has only two possibilities:

1. the original equivalence was not contextual/congruential for the admitted composition operators; or
2. the distinguishing composition/context was excluded from the operational boundary used to define equivalence.

Proof. Immediate from the universal quantifier in the definition of ~ctx. If a context C distinguishes p and q, then p and q are not contextually equivalent. Conversely, if they are contextually equivalent, every admitted C preserves observational equality. QED.

This is a no-go result, not a GC-II breakthrough theorem: it is the standard contextual-equivalence/congruence move of programming-language and process semantics.

## Proposition 124.2 — Closure under context composition gives congruence

STATUS: PROVED under the stated closure assumption.

Let D be an admissible context. If p ~ctx q, then D[p] ~ctx D[q].

Proof. For every admissible C, closure gives C∘D in C. Since p ~ctx q,

obs((C∘D)[p]) = obs((C∘D)[q]).

Equivalently obs(C[D[p]])=obs(C[D[q]]) for every C, hence D[p] ~ctx D[q]. QED.

Thus quotienting implementations by the full admitted contextual equivalence makes every admitted composition well-defined on equivalence classes.

## Minimal exact witness against standalone equivalence

Take implementations P={p,q}, standalone observation obs(p)=obs(q)=0, identity context I, and a composition/reveal context R with

obs(R[p])=0, obs(R[q])=1.

Then p ~obs q but p is not ~ctx q. The apparent hidden-identity effect is exactly the failure of ~obs to be a congruence for R; it disappears as a paradox once the operational equivalence is strengthened to the admitted contexts.

The executable checker verifies this witness and the congruence implication for a finite context-composition model.

## Collision gate

STATUS of `implementation identity revealed only by composition` as standalone GC-II novelty: FALSIFIED.

The mathematical issue is already central in process algebra and programming-language semantics:

- contextual equivalence identifies programs/processes that cannot be distinguished in any admitted context;
- congruence is precisely preservation of equivalence by the language/process operators;
- bisimulation variants are routinely strengthened or restricted so that the resulting behavioral equivalence is a congruence;
- structural operational semantics studies rule formats ensuring congruence.

Accordingly, hidden implementation identity cannot support a GC-II invariant if the proposed identity effect is observable through an admitted composition: that observation must already enter contextual equivalence.

## Edge and invariance checks

- Domains: no arithmetic across heterogeneous resource coordinates is used.
- Degenerate context family: if C contains only identity, ~ctx reduces to standalone observational equivalence; then composition outside C cannot legitimately be used to refute it.
- Monotonicity: not assumed.
- Relabeling: implementation names are irrelevant; only observations and context action matter.
- Composition: Proposition 124.2 explicitly requires closure of admitted contexts under composition. Without closure, congruence need not follow and the operational specification is incomplete for recursive composition.
- Counterexample behavior: any purported pair that is equivalent yet distinguishable by an admitted context is automatically a counterexample to the claim that the starting equivalence was contextual.
- Full operational equivalence: if `full` means equality under every admitted observation in every admitted context, implementation identity has no remaining observable content by definition.

## Consequence for Omega_G

An Omega_G defined as the extra capability exposed by placing two otherwise equivalent implementations in an admitted context is not new: it measures failure of the weaker equivalence to be a congruence/contextual equivalence.

STATUS: FALSIFIED as standalone novelty.

A quantitative metric version also requires caution: contextual/program/process metrics and bisimulation pseudometrics already quantify distinguishability under contexts. A GC-II metric would need additional independently motivated structure and a theorem not reducible to those constructions.

## What survives

The implementation-identity route survives only if GC-II can identify a constraint that is not an ordinary observation of an admissible context. The next defensible target is **budget-coupled compositional closure under endogenous admissibility**: composition itself may change which future transformations are admissible because the same finite budget simultaneously constrains resources, information acquisition, interfaces/actions, and rule changes.

The target must be formulated without hiding history in state, without treating admissibility as an arbitrary oracle, and without reducing to constrained reachability/viability, dynamic programming, process algebra with resources, or ordinary multi-resource resource theory. It must yield a non-tautological bound or equivalence criterion.

STATUS: OPEN. No breakthrough claimed.

## Status ledger

- standalone operational equivalence preserved by all admitted contexts: not automatic
- contextual equivalence definition: IMPORTED/KNOWN
- contextual closure absorbs composition-revealed implementation identity: PROVED
- congruence under context-composition closure: PROVED
- implementation-identity compositional obstruction as standalone GC-II novelty: FALSIFIED
- quantitative context distinguishability as standalone novelty: IMPORTED/KNOWN family / not established as GC-II novelty
- budget-coupled compositional closure under endogenous admissibility: OPEN

## Reproduction

Run:

```bash
python experiments/gc2_contextual_congruence_audit.py
```

The checker writes no scientific claim beyond the exact finite witness; the proof above carries the general result.
