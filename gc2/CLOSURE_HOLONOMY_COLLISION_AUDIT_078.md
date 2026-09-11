# GC-II Audit 078 — Closure Curvature / Holonomy Collision

Status: **PROVED no-go in the sufficient-state quotient; FALSIFIED as standalone GC-II novelty; OPEN only for a stronger typed accounting statement**

Branch scope: `gc2-capability-accounting-lab` only. GC-I `main` is frozen.

## 1. Candidate under attack

After Audit 077, consider a completed operational state space `X`, admissible transformations `A`, composition, and a typed nonnegative ledger `c(h) in R_+^4` for resources/information/actions/rules. A tempting candidate is a residual loop quantity or "closure holonomy" that remains after quotienting ordinary conversion equivalence.

For a loop `gamma = a_m ... a_1` based at state `x`, one might try to define a residual transformation

`H_x(gamma) = a_m o ... o a_1 |_fiber(x)`

or a scalar/vector loop defect from the difference between local increments and a putative endpoint potential.

## 2. Sufficient-state loop no-go theorem

### Theorem 078.1 (Future-capability invariance of closed loops)

Let `~` be an operational equivalence that is a congruence for every admissible continuation: `x ~ y` iff every admissible future task/protocol has the same achievable task-error-budget closure from `x` and `y`. Let `gamma` be an admissible history from `x` to `y` with `x ~ y`. Then no statistic defined solely by future operational capability can distinguish `x` from the endpoint of `gamma`.

**Proof.** This is immediate from the definition of the sufficient operational quotient: all admissible continuations have identical achievable closures from equivalent states. Therefore a claimed residual that changes future capability contradicts `x ~ y`. QED.

This is not presented as a deep new theorem; it is a bookkeeping/no-go lemma fixing what a GC-II invariant is allowed to mean.

### Corollary 078.1a

If a loop that is declared closed changes future task capability, then at least one of the following is true:

1. the chosen state was not operationally sufficient;
2. the chosen equivalence was not a congruence under continuation;
3. the loop did not actually close in the complete operational state;
4. an unaccounted reservoir, memory, catalyst, interface, or environment variable changed.

Thus endpoint capability holonomy cannot survive sufficient-state completion merely by renaming hidden path dependence.

## 3. What can survive

A closed loop may still act nontrivially on a **fiber/internal degree of freedom** while leaving the base state fixed. This is genuine holonomy/nonholonomy, but the mathematical architecture is already standard: parallel transport around loops, geometric phase, non-Abelian holonomy, nonholonomic control, and noncommuting transformation groups.

Accordingly, a GC-II claim of the form

`closed operational loop -> nontrivial residual transformation`

is **FALSIFIED as standalone novelty**. The residual must carry an additional GC-specific quantitative theorem, not merely be called generative curvature.

## 4. Exact finite countermodel

Take a finite state with base bit `b` and fiber bit `f`. Define two admissible operations

- `A(b,f) = (b xor 1, f)`
- `B(b,f) = (b, f xor b)`.

The commutator-like loop `gamma = B A B A` returns the base bit to its starting value but can change the fiber. Direct evaluation gives:

- `(0,0) -> (0,1)`;
- `(0,1) -> (0,0)`;
- `(1,0) -> (1,1)`;
- `(1,1) -> (1,0)`.

Hence the base projection reports a closed loop while the complete state does not close. This is an exact finite witness that apparent endpoint holonomy can be manufactured by coarse-graining.

If the fiber is included in the operational state, the apparent paradox disappears: the history is simply a nontrivial state transformation.

## 5. Integrability criterion for scalarized accounting

Let a finite strongly connected directed operational graph have scalarized edge charge `ell_w(e) >= 0`. There exists an endpoint potential `Phi_w` satisfying

`ell_w(x->y) = Phi_w(y) - Phi_w(x)`

for every directed edge iff every directed cycle has zero signed circulation (with the usual orientation convention when comparing paths). Therefore any nonzero loop circulation witnesses non-integrability of that edge assignment, but this is standard discrete potential/graph theory rather than a new GC invariant.

For the physically relevant nonnegative consumed-resource ledger, a positive round-trip cost is even less exotic: it is ordinary dissipation/consumption and does not imply geometric curvature.

## 6. Collision audit

### Differential/geometric holonomy

Holonomy is precisely the failure of transported internal data to return unchanged after a closed loop; curvature generates nontrivial holonomy. Non-Abelian holonomies can be matrix-valued and noncommuting.

### Quantum/geometric computation

Holonomic quantum computation deliberately uses cyclic control paths to implement nontrivial gates. Therefore `loop -> residual operator` is decisively prior art in operational physics.

### Nonholonomic control

Nonintegrable constraints and Lie-bracket-generated motions already turn loops in controls/shape variables into net state displacement. Thus loop-generated capability is not uniquely generative.

### Thermodynamic cycles

Positive cycle cost/entropy production is ordinary thermodynamic irreversibility when the ledger records consumed physical resources.

### Resource conversion

When transformations compose noncommutatively, loop words can yield nonidentity transformations. Again this is algebra of the allowed transformation monoid/group unless a new accounting theorem is proved.

## 7. Status table

| Claim | Status |
|---|---|
| closed loop cannot change future capability in the sufficient operational quotient | PROVED |
| apparent loop residual can arise from omitted hidden/fiber state | PROVED by exact finite construction |
| loop circulation detects failure of an endpoint potential | IMPORTED/KNOWN |
| nontrivial loop action/holonomy is itself GC-II novelty | FALSIFIED |
| positive physical cycle cost is itself GC-II curvature | FALSIFIED |
| a typed task-scale-error-budget theorem can couple loop obstruction to minimal augmentation cost | OPEN |

## 8. Surviving Paper-II target

The next candidate must not be generic holonomy. A defensible target is a **Typed Closure Integrability/Obstruction Theorem**:

Given a complete operational quotient and typed augmentation frontier `F(x,y)`, determine necessary and sufficient conditions for the existence of a finite family of potentials/monotones whose differences reproduce or tightly bound *all* task-scale-error-budget conversion frontiers. If integrability fails, quantify the smallest typed augmentation needed to remove the obstruction.

A breakthrough would require at least one result not reducible to ordinary graph circulation, thermodynamic entropy production, noncommutative holonomy, resource-theory monotones, or control Lie brackets. In particular, the target should seek an equivalence between:

1. path-independent typed capability accounting;
2. existence of a complete potential/dual-monotone representation;
3. vanishing of a precisely defined family of operational cycle defects;
4. a computable finite-world criterion;

plus a quantitative lower/upper bound when the conditions fail.

This target remains **OPEN**.

## 9. Prior-art boundary recorded in this audit

Relevant established domains to collide against before any novelty claim: differential holonomy/geometric phase; non-Abelian holonomic quantum computation; nonholonomic geometric control; cycle affinities/entropy production; simulation/resource preorders and complete monotones; discrete potential theory and graph circulation.

No claim of breakthrough is made in Audit 078.
