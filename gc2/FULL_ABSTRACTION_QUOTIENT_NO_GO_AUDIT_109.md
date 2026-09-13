# GC-II Audit 109 — Full-Abstraction Quotient No-Go

## Scope

This audit attacks the post-Audit-108 target: define a nontrivial Generative Novelty Gap `Omega_G` on operational-equivalence classes at least as strong as true-concurrency/history-preserving semantics, while retaining a genuine capability consequence.

The result is a no-go constraint. It does **not** establish a GC-II breakthrough.

## Setup

Fix a realization boundary and let `Obs_B(X)` denote the complete family of task-relevant observations available from system `X` under budget/index `B`. The family may include, as declared by the model, typed resource use, information, interfaces/actions, rule-state, histories, probabilities, concurrency structure, errors, and horizons.

Let `~_B` be an operational equivalence that is **fully abstract** for this observation family:

`X ~_B Y  <=>  Obs_B(X) = Obs_B(Y)`.

Let the budgeted operational closure be any extensional functional of those observations,

`C_B(X) = F_B(Obs_B(X))`.

Let a proposed pairwise novelty gap `Omega_G^B(X,Y)` satisfy two minimal requirements:

1. **quotient invariance:** it depends only on `[X]_{~_B}` and `[Y]_{~_B}`;
2. **capability faithfulness:** if the complete budgeted operational observations coincide, the claimed capability novelty between the systems is zero.

## Theorem 109.1 — Full-Abstraction Quotient Collapse

If `~_B` is fully abstract for the complete observation family used to define budgeted capability, then

`X ~_B Y  =>  C_B(X) = C_B(Y)`.

Consequently, every capability-faithful quotient-invariant novelty gap obeys

`X ~_B Y  =>  Omega_G^B(X,Y) = 0`.

### Proof

From full abstraction,

`X ~_B Y => Obs_B(X)=Obs_B(Y)`.

Because `C_B` is a functional of `Obs_B`, substitution gives

`C_B(X)=F_B(Obs_B(X))=F_B(Obs_B(Y))=C_B(Y)`.

Capability faithfulness then forces `Omega_G^B(X,Y)=0`. Quotient invariance guarantees that replacing either presentation by another representative of the same operational class cannot change this conclusion. QED.

**Status: PROVED.**

## Corollary 109.2 — Separation Trilemma

Suppose a candidate `Omega_G` assigns a nonzero value to `X,Y` although `X ~_B Y`. Then at least one of the following is true:

1. `~_B` was not actually fully abstract for the capability observations;
2. `Omega_G` uses an additional observable not included in `Obs_B`;
3. `Omega_G` is presentation/intension sensitive rather than a capability invariant on the declared quotient.

There is no fourth option obtained merely by choosing a nonlinear formula in `Delta R, Delta I, Delta A, Delta L`.

**Status: PROVED.**

## Corollary 109.3 — No Breakthrough From “Stronger Quotient” Alone

Moving from path equivalence to bisimulation, history-preserving bisimulation, hereditary history-preserving bisimulation, HDA equivalence, or another stronger behavioral quotient cannot by itself create a new capability quantity. Once the chosen quotient is fully abstract for the declared observations, every extensional capability functional factors through that quotient and is constant inside each class.

A nonzero survivor therefore requires a **new independently justified observable or intervention context**, not merely a stronger equivalence relation.

**Status: PROVED as a logical consequence of Theorem 109.1; the adequacy/full-abstraction of any concrete chosen equivalence remains model-dependent.**

## Quantitative version

Let `d_B(X,Y)` be a behavioral pseudometric that is sound for the declared observations, with

`d_B(X,Y)=0 => Obs_B(X)=Obs_B(Y)`.

Any capability gap `Omega_G` that is Lipschitz through those observations,

`Omega_G^B(X,Y) <= L_B d_B(X,Y)`, `L_B < infinity`,

also satisfies

`d_B(X,Y)=0 => Omega_G^B(X,Y)=0`.

Thus replacing Boolean equivalence by a behavioral distance does not evade the zero-class collapse. A genuinely new quantitative theorem would have to derive a nontrivial bound connecting **independently specified** observables, rather than define a new distance after the fact.

**Status: PROVED.**

## Collision check

This mechanism strongly collides with established semantic ideas rather than creating a new one:

- full abstraction identifies denotational/semantic equality with operational indistinguishability;
- contextual equivalence and resource transition systems already characterize program equality relative to declared observations/resources;
- bisimulation-invariant and quantitative behavioral theories already study exactly which properties/distances factor through behavioral equivalence or behavioral pseudometrics;
- true-concurrency semantics already supplies stronger equivalences when ordinary interleaving/path semantics omits causal structure.

Therefore the statement “define `Omega_G` on a sufficiently strong operational quotient” is a **methodological requirement**, not a GC-II breakthrough.

## Edge and degenerate cases

- **Empty observation family:** all systems are equivalent and every capability-faithful extensional gap is zero. This is degenerate, not novel.
- **Identity equivalence:** every presentation is its own class; arbitrary intensional quantities survive, but quotienting has provided no invariance.
- **Aliased actions / state refinements:** if observationally inert, they vanish under a fully abstract quotient; a candidate that changes under such refinements is presentation-sensitive.
- **Stochastic systems:** `Obs_B` must include the relevant probability laws, not only supports.
- **Concurrency:** if concurrency is capability-relevant, `Obs_B` must include the relevant causal/concurrent observations; otherwise the equivalence is too coarse.
- **Typed costs:** dimensions remain separate. The theorem does not add or compare unlike units; it only uses equality of the declared typed observation record.
- **Composition:** if `~_B` is a congruence for the allowed contexts, the collapse is context-stable. If it is not a congruence, contextual closure is required before claiming compositional capability invariance.

## Scientific consequence

Audit 108's surviving target must be narrowed again.

A GC-II breakthrough cannot be obtained merely by:

1. choosing a stronger true-concurrency/history-sensitive quotient;
2. defining a quotient-invariant scalar on it; or
3. applying a nonlinear `F(Delta R, Delta I, Delta A, Delta L)` to observables already preserved by that quotient.

The next admissible target is an **independently motivated intervention/observation extension** that changes the operational question itself, followed by a theorem showing a quantitative capability consequence not reducible to existing contextual equivalence, behavioral metrics, resource monotones, Blackwell deficiency, reachability/viability, thermodynamics, or standard computational/communication lower bounds.

A promising but still OPEN direction is **counterfactual intervention closure**: distinguish systems not by what they do under the current admissible contexts, but by the minimal typed cost of expanding the admissible context family so that a previously unavailable operational distinction becomes realizable. This must be collision-tested against testing equivalence, active learning/query complexity, experiment design, causal interventions, adaptive control, and resource theories before any novelty claim.

## Status table

| Claim | Status |
|---|---|
| Full-abstraction quotient collapse | PROVED |
| Zero novelty inside a complete operational equivalence class | PROVED |
| Stronger behavioral quotient alone yields GC-II novelty | FALSIFIED |
| Nonlinear weighting of already preserved typed observables escapes the collapse | FALSIFIED |
| Behavioral pseudometric zero-class escape | FALSIFIED under the stated soundness/Lipschitz assumptions |
| Concrete full abstraction of any chosen GC-II semantics | OPEN / model-dependent |
| Counterfactual intervention-closure gap | OPEN |

## Kill rule for subsequent audits

Before accepting any future `Omega_G`, ask:

> Does it distinguish two systems that the declared complete operational semantics identifies?

If **yes**, then either the semantics omitted a relevant observable/context or `Omega_G` is presentation-sensitive. If **no**, then the candidate must earn novelty through a new quantitative law **between distinct operational classes**, not from the act of quotienting itself.
