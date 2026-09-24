# GC-II Audit 360 — Reversibility-gap collision and surviving target

## Scope

Audit 359 defines the minimum generated-operation order kappa(x,y). A natural Paper-II candidate is to define a reversibility gap from directional asymmetry, for example

`Gamma_kappa(x,y) = kappa(x,y) - kappa(y,x)`

when both quantities are finite, or an extended-valued variant when one direction is unreachable. This audit tests whether such a quantity is a genuinely new GC-II invariant.

## Proposition 360.1 — Directed-order asymmetry is a shortest-path quasimetric asymmetry

Assign cost 0 to baseline operations and cost 1 to generated operations. Then Audit 359 already proves that `kappa(x,y)` is the directed shortest-path cost in this weighted operational graph. Therefore any invariant determined only by the ordered pair

`(kappa(x,y), kappa(y,x))`

is determined entirely by the forward and reverse directed shortest-path distances.

In particular, `Gamma_kappa` is not a new primitive: it is an antisymmetrization of a directed shortest-path quasimetric.

### Proof

Audit 359 identifies `kappa(x,y)` with the minimum number of generated edges on an x-to-y path after assigning baseline edges weight 0 and generated edges weight 1. Reversing the ordered pair gives the corresponding reverse directed shortest-path value. Hence every function of those two scalars factors through the classical directed-distance pair. No additional operational information survives the factorization. QED.

## Decisive counterexample to completeness

Directional distance asymmetry cannot be a complete reversibility descriptor. Consider two operational systems on `{x,a,y}`.

System A:
- generated edges `x->y` and `y->x`.

System B:
- generated edges `x->y`, `y->x`, `x->a`, `a->x`, `a->y`, `y->a`.

For the focal pair `(x,y)`, both systems have

`kappa(x,y)=kappa(y,x)=1`, hence `Gamma_kappa(x,y)=0`.

Nevertheless their surrounding reversible capability structure differs: System B contains reversible access involving `a`, while System A does not. Thus zero pairwise gap does not imply equality of reversible operational closure, and the scalar cannot be complete for contextual reversibility.

The same obstruction applies to any scalar depending only on `(kappa(x,y),kappa(y,x))`: systems with the same focal directed-distance pair can have different contextual closures, resource alternatives, information requirements, or admissible interfaces.

## Prior-art collision

Directed shortest-path distance is classically asymmetric; the forward and reverse distances need not coincide. The literature treats such structures as directed/asymmetric distances or quasimetrics. Therefore a GC-II claim whose content is only forward-minus-reverse shortest-path cost would collide directly with known directed-distance theory.

Status:
- `kappa` as generated-operation distance: **PROVED / IMPORTED-KNOWN mechanism** (Audit 359).
- pairwise reversibility gap `Gamma_kappa`: **DEFINED but IMPORTED/KNOWN in mathematical content**.
- claim that `Gamma_kappa` is a new foundational invariant: **FALSIFIED**.
- claim that zero `Gamma_kappa` implies contextual operational reversibility: **FALSIFIED**.

## Surviving target

A nontrivial GC-II reversibility invariant must retain information that the two directed distances discard. Candidate requirements for the next audit are:

1. compare the *sets or antichains of forward and reverse witnesses*, not only their minima;
2. track resource/information/interface/rule restoration, not merely endpoint return;
3. distinguish returning to the same visible state from returning to the same operational closure/context;
4. test invariance under operationally equivalent refinements and sensitivity to irreversible context loss;
5. collision-check against resource-theoretic cost/yield irreversibility, thermodynamic irreversibility, directed deficiencies, simulation preorders, and reversible computation.

A promising GC-specific definition should therefore be context-restoration based: after a forward realization, ask for the minimum additional augmentation required to restore the original *capability context* (or its equivalence class), rather than merely finding a reverse path to the original visible state. That stronger object remains **OPEN** and is the priority after this no-go result.
