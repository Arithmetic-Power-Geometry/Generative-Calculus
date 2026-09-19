# GC-II Audit 243 — Typed labels alone do not bound capability efficiency

## Purpose
Test the strongest open target from Audit 242: whether the mere R/I/A/L type of a generated operation can force a finite, size-independent upper bound on its capability efficiency eta. The answer is negative without explicit semantics limiting operational fan-out.

## Construction — PROVED
For each even n >= 2, let W={1,...,n}. Initially all worlds share one projection value p(w)=z. Let g(w)=0 for the first n/2 worlds and g(w)=1 for the remaining n/2. Let the message alphabet be M={0,1}, and let every world initially admit only message 0: L(w)={0}.

By the exact Audit-239 repair formula, the optimal fiber labeling assigns message 0 to one decision and message 1 to the other. Exactly one of the two decision classes is uncovered, hence

    Omega_add(x_n)=n/2.

Now define one typed INFORMATION operation r_n of cost 1 whose effect is to refine the observation/projection to p'(w)=w, leaving W,g,M,L unchanged. Every new projection fiber is a singleton. Since each singleton fiber contains only one required decision and its world admits message 0, each fiber is immediately translator-feasible. Therefore

    Omega_add(r_n(x_n))=0,
    delta_Omega(r_n;x_n,r_n(x_n))=n/2,
    eta(r_n)>=n/2.

Thus for every K there exists n>2K with a unit-cost operation carrying the same coarse type label INFORMATION but capability efficiency greater than K.

## Unbounded-type-efficiency theorem — PROVED
If the GC-II operational semantics permit a unit-cost typed operation whose projection/refinement fan-out is unbounded with system size, then no finite size-independent constant eta_I can be derived from the label INFORMATION alone. The analogous statement holds for any type whose one operation may modify an unbounded number of capability-relevant incidences/fibers.

This does not say information is literally free in physical systems. It says that a type name or operation count is not a resource calibration. A finite eta_t requires an explicit semantic constraint such as bounded support/fan-out, bounded description length, bounded communicated bits together with a model linking those bits to state refinement, locality, energy/time, or another operational capacity restriction.

## Stronger accounting consequence
The family falsifies any universal linear law of the form

    delta_Omega <= eta_I * Delta I

when Delta I merely counts one information-type operation and eta_I is claimed to be a fixed finite constant independent of instance size. More generally, scalar Delta R, Delta I, Delta A, Delta L totals cannot support a universal quantitative capability law unless their units encode the capability-relevant extent/effect of the generated transformation.

Even replacing operation count by the number of newly distinguished projection labels does not automatically create novelty: then the bound becomes an effect-size accounting convention. The scientific target is therefore to derive the relevant capacity measure from a concrete operational interface rather than choose it post hoc to dominate Omega.

## Exact footprint rescue — PROVED / generic
For fixed W,p,g,M, Omega_add as a function of admissibility incidence E_L is 1-Lipschitz under one incidence toggle. Audit 239 proved the augmentation direction; applying it in both directions to adjacent incidence sets gives

    |Omega_add(E)-Omega_add(E')| <= |E triangle E'|.

Hence an operation changing at most b capability-relevant admissibility incidences can reduce Omega_add by at most b. This yields eta <= b/c_min for positive cost c_min. This is a valid semantic bridge when bounded footprint is physically or computationally justified, but it is a generic distance/repair Lipschitz mechanism and is not claimed as GC novelty.

Projection refinements are different: one refinement operation can change the conflict/fiber structure globally, as the family above demonstrates. Therefore incidence-footprint bounds cannot simply be transferred to p,g-changing operations without charging their induced structural footprint.

## Edge cases and checks
- n=2 gives Omega_add=1 -> 0 after refinement.
- All g equal gives Omega_add=0 initially, so no generated novelty; decision incompatibility is essential.
- If all worlds already have L(w)={0,1}, Omega_add=0; refinement has no gap benefit.
- If refinement is restricted to at most b affected worlds per operation, this family no longer yields unbounded one-step efficiency; a support-sensitive bound becomes possible.
- Relabeling worlds, decisions, messages, or projection symbols preserves the argument.
- Composition of multiple bounded-support refinements may still create large total capability, but their charged support/number must accumulate; this is exactly what a defensible accounting measure must capture.

## Prior-art collision boundary
The negative lesson is consistent with established resource-theory and planning practice: operational monotones/currencies require meaningful conversion semantics, and planning potential bounds require operator-cost/effect constraints. General resource theories need not admit a finite complete monotone family, and cost/yield monotones need not be complete. Therefore neither the unbounded-fan-out observation nor the Lipschitz repair argument is claimed as a new generic mathematical paradigm.

The GC-II-specific surviving target is narrower: identify a natural GC operational capacity measure induced by projection/generation semantics (not a type label and not an arbitrary effect count), then prove that it controls the rate at which exact decision-incompatible projection ambiguity can be repaired.

## Status ledger
- Family Omega_add=n/2 with unit-cost information refinement to Omega_add=0: PROVED.
- Finite size-independent eta_I from INFORMATION label alone: FALSIFIED.
- Universal linear accounting from typed operation counts alone: FALSIFIED.
- 1-Lipschitz incidence-footprint bound for fixed p,g,M: PROVED / generic.
- Bounded semantic footprint implies finite efficacy: CONDITIONAL / PROVED.
- Type names/cardinal totals as intrinsic resource calibration: FALSIFIED.
- GC-derived non-generic capacity measure controlling projection-refinement efficacy: OPEN.
