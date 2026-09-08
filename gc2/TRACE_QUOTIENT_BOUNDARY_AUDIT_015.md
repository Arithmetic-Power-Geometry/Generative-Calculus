# GC-II Trace-Quotient Boundary Audit 015

## Question
After aggregate R/I/A/L accounting was falsified by noncommuting state-dependent augmentations, can ordered traces be compressed without losing capability information?

## Setup
Let `Sigma*` be finite augmentation words over admissible R/I/A/L primitives. Executing a feasible word `sigma` from operational state `s` yields `Phi_sigma(s)`. Let `Cap(s)` be the complete observable capability record relevant to the model and let `Cost(sigma;s)` be its accounting record. Continuations may themselves be state-dependent, so feasibility is part of the future behavior.

For a fixed start state `s0`, define two feasible prefixes `sigma,tau` to be **future capability-cost equivalent**, written `sigma ~_G tau`, iff for every continuation word `rho`:

1. `rho` is feasible after `sigma` iff it is feasible after `tau`; and
2. whenever feasible, both the resulting capability record and continuation-sensitive accounting agree:
   `Cap(Phi_{sigma rho}(s0)) = Cap(Phi_{tau rho}(s0))` and `Cost(sigma rho;s0)=Cost(tau rho;s0)`.

(If only capability, not cost, is to be preserved, drop the cost equality. The distinction must be explicit.)

## Theorem: coarsest exact right-congruent trace quotient
`~_G` is an equivalence relation and a right congruence on feasible prefixes. Moreover it is the coarsest right congruence under which future feasibility, capability, and cost are well-defined on trace classes.

### Proof
Reflexivity, symmetry and transitivity follow from equality of the complete future signatures. For right congruence, suppose `sigma ~_G tau` and primitive/action word `a` is feasible after both. For every continuation `rho`, the continuation `a rho` occurs in the defining universal quantifier for `sigma ~_G tau`; hence feasibility and the capability-cost records after `sigma a rho` and `tau a rho` agree. Therefore `sigma a ~_G tau a`.

Now let `approx` be any right congruence on feasible prefixes such that future feasibility, capability and cost are invariant on its classes. If `sigma approx tau`, repeated right-congruence gives `sigma rho approx tau rho` for every jointly feasible continuation `rho`; invariance gives equality of their future signatures, while feasibility invariance rules out a continuation feasible on only one side. Thus `sigma ~_G tau`. Hence every such `approx` refines `~_G`, so `~_G` is the coarsest exact quotient. QED.

## Consequence
The correct general accounting object need not retain the literal ordered word. It must retain at least its `~_G` class. Therefore a capability-accounting functional can be written on the quotient

`A_G : Sigma*/~_G -> accounting/capability records`,

without the information loss exhibited by aggregate `(Delta R,Delta I,Delta A,Delta L)` accounting.

Any proposed summary `S(sigma)` is exact only if

`S(sigma)=S(tau) => sigma ~_G tau`.

This gives a direct collision test for proposed accounting summaries.

## Minimal strictness witness
Let actions `A` and `I` have the same aggregate count vector in words `AI` and `IA`, but let `AI` reach `goal` while `IA` reaches `dead`. Then `AI` and `IA` have equal aggregate deltas but are not `~_G`-equivalent. Thus the aggregate vector quotient is strictly coarser than the exact future quotient in the noncommuting witness already recorded in Audit 014.

## Boundary / prior-art status
**IMPORTED/KNOWN mechanism, not a GC-II breakthrough.** The construction is a direct operational analogue of future-equivalence/right-congruence ideas underlying Myhill-Nerode minimization and behavioral equivalence. Its value here is architectural: it identifies the mathematically correct lossless compression target after aggregate accounting failed.

## Status
- Future capability-cost equivalence is an equivalence relation: **PROVED**.
- Right-congruence property: **PROVED**.
- Coarsest exact right-congruent quotient: **PROVED** under the stated deterministic trace semantics and explicit future-signature definition.
- Novelty of the quotient mechanism: **IMPORTED/KNOWN**.
- Efficient computation in general stateful GC-II worlds: **OPEN**.
- Finite-state computation by partition refinement/minimization: expected known territory; **IMPORTED/KNOWN target**, not a novelty claim.
- Breakthrough status: **NONE**.

## Research implication
Do not claim ordered traces themselves as irreducible. The scientifically meaningful question is whether natural GC-II worlds force the minimal exact quotient `Sigma*/~_G` to have large description/translation complexity even when all fixed-task or low-order projections agree. That is the appropriate bridge to the GC-I local-to-global reconstruction program.