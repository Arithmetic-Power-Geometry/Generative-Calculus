# GC-II Audit 361 — Context-restoration reversibility: exact formulation and collision

## Scope

Audit 360 falsified reversibility measures determined only by the two endpoint distances `(kappa(x,y), kappa(y,x))` and proposed a stronger target: after a forward realization, measure the effort required to restore the original *capability context*, not merely the visible endpoint.

This audit formalizes that target and tests whether it escapes classical state-space reachability/reversible-computation theory.

## Operational state and capability equivalence

Let a complete operational state be

`z = (x,m,r,q)`

with visible/system state `x`, retained information `m`, resource ledger `r`, and active rule/interface/authorization state `q`. Let `~cap` be any fixed exact capability equivalence on complete states: `z ~cap z'` iff the two states have identical future capability semantics under the chosen observation model.

Let each admissible transition `e` have nonnegative restoration charge `c(e)`. For a set `C` of complete states define

`d_c(z,C) = inf { sum_{e in P} c(e) : P is an admissible path from z to some z' in C }`,

with value `+infinity` when no such path exists.

For a forward realization `P: z0 -> z1`, define its **context-restoration cost**

`rho(P) = d_c(z1, [z0]_cap)`.

This quantity correctly distinguishes endpoint return from restoration of operational capability context.

## Proposition 361.1 — Restoration is shortest path to an equivalence class

For every explicit operational transition system and every fixed capability equivalence `~cap`, `rho(P)` is exactly the shortest-path distance from the post-forward state `z1` to the target set `[z0]_cap` in the complete operational graph.

### Proof

By definition, a successful restoration witness is precisely an admissible path beginning at `z1` and ending in a state capability-equivalent to `z0`. Its charge is the sum of its transition charges. Minimizing over all such witnesses is therefore exactly the shortest-path-to-set problem. QED.

This remains valid with zero-cost transitions, multiple restoration targets in the equivalence class, irreversible transitions, resource replenishment, information deletion, and dynamic rule/interface state, provided those quantities are included in the complete state as in Audit 355.

## Corollary 361.2 — Zero restoration cost

If all nontrivial restoration transitions have strictly positive charge, then

`rho(P)=0 iff z1 is already in [z0]_cap`.

Without strict positivity this equivalence fails: a distinct context may be connected to `[z0]_cap` by a zero-cost restoration path. Thus the positivity assumption is necessary for this zero-test.

## Counterexample: visible return is not context restoration

Let complete states be `(x,b)` with visible state `x in {A,B}` and one retained capability bit `b in {0,1}`. Suppose the forward operation maps

`(A,1) -> (B,0)`

and a visible reverse operation maps

`(B,0) -> (A,0)`.

Assume future capability `Q` is available exactly when `b=1`, and there is no transition restoring `b=1`. Then the visible state returns to `A`, but `(A,0)` is not capability-equivalent to `(A,1)` and

`rho(P)=+infinity`.

Thus endpoint reversibility can coexist with irreversible capability loss.

## Proposition 361.3 — Context restoration does not yet escape classical compilation

If the complete operational state space is finite and explicitly represented, and `~cap` is computable, then exact context-restoration cost is reducible to ordinary nonnegative shortest path by adding a zero-cost sink connected from every state in `[z0]_cap` (or equivalently by a multi-target shortest-path computation).

Therefore the move from endpoint return to context restoration fixes the *semantic inadequacy* identified in Audit 360 but does not by itself create a new mathematical primitive.

## Prior-art collision

This formulation has two direct classical neighbors.

1. Reversible computation already distinguishes merely obtaining an output from restoring computational context. Bennett's compute-copy-uncompute construction preserves the input and reversibly disposes of intermediate history/garbage, returning scratch storage to its original blank condition.
2. Contextual/observational equivalence already identifies states or programs by indistinguishability under future contexts; reversible-process theory has explicitly studied back-and-forth contextual equivalence.

Accordingly, a claim that `rho` alone is a foundationally new GC-II invariant would be unsafe.

## Decisive boundary

The following candidate is **FALSIFIED**:

> Replacing reverse endpoint distance by minimum context-restoration distance, with the complete operational state explicitly available, is sufficient to produce a novel GC-II reversibility theory.

The surviving research target must involve something not compiled away by the complete-state graph, for example:

- lower bounds on the information/representation required to identify the correct restoration equivalence class;
- restoration when capability context is only partially observable or cannot be retained without consuming the resource being restored;
- history-sensitive admissibility that is not summarized by the declared finite state representation;
- a GC-I-derived obstruction showing that local projected data cannot determine whether restoration is possible;
- quantitative separation between endpoint recovery cost and *context identification + restoration* cost under restricted information interfaces.

The last two directions are the strongest candidates because they can connect GC-I projection irreducibility to GC-II operational reversibility rather than merely rename shortest-path machinery.

## Status

- context-restoration cost `rho`: **DEFINED**.
- `rho` equals shortest-path distance to `[z0]_cap`: **PROVED**.
- visible endpoint return implies capability-context restoration: **FALSIFIED**.
- zero-cost criterion under strictly positive nontrivial restoration charges: **PROVED / CONDITIONAL on positivity**.
- shortest-path reduction for explicit finite complete state: **PROVED / IMPORTED-KNOWN mechanism**.
- `rho` alone as a foundational GC-II novelty: **FALSIFIED by reduction/prior-art collision**.
- information-restricted context-identification/restoration gap: **OPEN / priority**.
- GC-I projection-irreducibility -> restoration-information lower bound: **OPEN / priority**.

## Next attack

Construct paired operational worlds with identical allowed local/projected observations but different restoration classes, and prove that every exact restoration policy must acquire a separating observation or fail on one world. Then test whether the resulting lower bound is genuinely stronger than standard partial-observation state-estimation, Blackwell sufficiency/deficiency, automata distinguishability, and active diagnosis results.