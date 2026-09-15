# GC-II Audit 155 — Model-edit novelty-gap no-go

Status date: 2026-09-15
Branch scope: `gc2-capability-accounting-lab` only. GC-I/main unchanged.

## Candidate tested

After Audit 154, a natural candidate was to define a Generative Novelty Gap as the minimum intervention needed to alter an operational model so that a previously unreachable target enters budgeted closure.

Let an operational model be `M`, let `C_b(M)` denote its closure under budget `b`, let target capability be `g`, let `E` be an admissible class of model edits/interventions, and let `kappa(e) >= 0` be an edit cost. Define

Omega_edit(M,g;b) = inf { kappa(e) : e in E and g in C_b(e(M)) }.

For finite E, replace inf by min when the feasible set is nonempty; use +infinity when no admissible edit makes g reachable.

## Basic properties

1. Nonnegativity: `Omega_edit >= 0` from `kappa >= 0`.
2. Degenerate case: if the identity edit is admissible with zero cost and `g in C_b(M)`, then `Omega_edit = 0`.
3. Impossibility: if no admissible edit reaches the target, `Omega_edit = +infinity`.
4. Edit-set monotonicity: if `E1 subseteq E2` with the same cost function, then `Omega_edit(E2) <= Omega_edit(E1)`.
5. Budget monotonicity: whenever closure is monotone in budget (`b <= b' => C_b(M) subseteq C_b'(M)`), `Omega_edit(M,g;b') <= Omega_edit(M,g;b)`.
6. Representation invariance is not automatic: it requires the admissible edit class and edit metric/cost to be transported under the chosen semantics-preserving representation equivalence. Otherwise syntactic refactoring can change the measured value without changing capability semantics.
7. Composition/additivity is not guaranteed. Shared edits, enabling edits, and nonlinear edit costs can make joint target cost subadditive or superadditive.

## No-go / reduction

The definition above is an instance of minimum-cost model repair whenever:

- the target `g in C_b(M')` is encoded as a reachability/specification property `phi` of the repaired model `M'`;
- admissible GC interventions correspond to the controllable model modifications allowed by the repair formalism; and
- `kappa` is the repair distance/cost.

Then

`Omega_edit(M,g;b) = min { kappa(M,M') : M' admissible and M' satisfies phi_g,b }`,

which is exactly the minimum-model-repair objective, up to the selected model class, property language, and edit metric.

This is not merely an analogy: under the stated encoding, the feasible sets and objective values coincide.

## Prior-art collision

Model repair for Kripke structures asks for a model satisfying a violated temporal-logic property while minimizing changes. Probabilistic model repair likewise minimizes modification cost subject to satisfying a probabilistic temporal property, including reachability properties. Therefore a GC-II novelty claim based only on “minimum intervention that changes the operational model until capability becomes reachable” collides with established model-repair optimization.

## Ledger

- `Omega_edit` well-defined under explicit edit class/cost: PROVED (definition plus extended-real convention).
- Nonnegativity / edit-set monotonicity / budget monotonicity under stated assumptions: PROVED.
- Automatic representation invariance: FALSIFIED; requires compatibility assumptions on edits and costs.
- Additivity across targets or edit types: FALSIFIED in general / not assumed.
- Minimum model-edit burden as independent GC-II breakthrough mechanism: FALSIFIED for the direct reachability/specification encoding.
- Minimum model repair: IMPORTED/KNOWN.
- A genuinely GC-II `Omega_G` must therefore depend on a structure not reducible to a fixed model plus admissible repair set plus fixed repair metric/objective: OPEN.

## Consequence for Paper II

Do not define `Omega_G` merely as minimum transition/state/rule/interface edits needed to make a target reachable. That is scientifically useful as an imported baseline, but not a breakthrough.

The next viable search direction is endogenous intervention semantics: the act of acquiring/creating an admissible model transformation must alter the transformation language or the criterion by which future transformations count, and the candidate must still be checked against meta-planning, program/model repair, self-modifying systems, mechanism design, and algorithmic-information descriptions. Any finite compilation back to a fixed repair search space should be treated as a reduction, not novelty.
