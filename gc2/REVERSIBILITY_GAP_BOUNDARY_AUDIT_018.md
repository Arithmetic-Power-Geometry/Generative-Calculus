# GC-II Reversibility-Gap Boundary Audit 018

## Target
Stress-test step (8): define a reversibility-gap invariant without repackaging known forward/reverse conversion-cost asymmetry.

## Candidate
Let `Omega_G(x -> y)` be any already-defined directed GC-II augmentation cost on a fixed admissible operational model. Natural candidates are

`Gamma_sum(x,y) = Omega_G(x->y) + Omega_G(y->x)`

and

`Gamma_asym(x,y) = |Omega_G(x->y) - Omega_G(y->x)|`.

These quantities are well-defined when both directed costs are finite, but neither is automatically a new invariant of Generative Calculus.

## Exact structural checks
1. `Gamma_sum >= 0` and `Gamma_asym >= 0` whenever directed costs are nonnegative.
2. Both are symmetric under exchange of `x,y` by construction.
3. `Gamma_asym(x,x)=0`; `Gamma_sum(x,x)=2 Omega_G(x->x)`, so identity requires the normalization `Omega_G(x->x)=0`.
4. Zero `Gamma_asym` does **not** imply reversibility: it only says forward and reverse costs coincide. Both can be positive, or both can be infinite under an extended-real convention.
5. Zero `Gamma_sum` implies both directed costs vanish only under nonnegativity. Even then this identifies zero-cost operational equivalence, not literal state identity unless the theory is quotiented by zero-cost equivalence.
6. Because the current nonlinear Omega_G can violate the triangle inequality, neither candidate inherits a metric triangle inequality without extra composition/subadditivity assumptions.
7. Under rescaling or reparameterization of resource units, numerical values are not invariant unless the cost functional itself has a declared unit/covariance convention.

## Decisive novelty boundary
Forward/reverse conversion asymmetry, formation-vs-distillation gaps, work cost vs extractable work, and cost/irreversibility tradeoffs are established in thermodynamics and resource theories. Therefore a scalar built only from `Omega_G(x->y)` and `Omega_G(y->x)` is not defensibly a GC-II breakthrough without an additional theorem tied essentially to GC operational structure.

Status:
- symmetric round-trip diagnostic: **PROVED** as an elementary construction;
- metric interpretation under current nonlinear Omega_G: **FALSIFIED in general** (previous audit already supplies triangle failure);
- generic forward/reverse asymmetry as GC-II novelty: **FALSIFIED as a novelty route**;
- GC-specific reversibility invariant exploiting ordered endogenous R/I/A/L transformations and whole-envelope effects: **OPEN**.

## Stronger target
A credible GC-II invariant should compare not just endpoint costs but the operational trace languages (or future-capability quotient classes) of forward and reverse transformations. Candidate research direction:

`Gamma_trace(x,y) = inf_{sigma:x=>y, tau:y=>x} D_G(sigma o tau, id_x)`

where `D_G` must measure residual whole-envelope capability distortion after the round trip, including changes to future admissible actions/rules/interfaces and vector budgets. This is only a **DEFINITIONAL CANDIDATE / OPEN** object until invariance, composition behavior, degeneracies, computability, and prior-art collisions are resolved.

The key test for novelty is whether two systems can have identical endpoint directed costs but different residual future-capability distortion. If so, endpoint asymmetry is provably insufficient and a trace-sensitive invariant has operational content. If not, the construction collapses back to known conversion-cost asymmetry.

## Prior-art collision note
Resource theories already distinguish one-shot formation and distillation costs and study reversible/asymptotically reversible conversion; thermodynamics studies work/exergy loss and irreversibility; recent resource-theoretic work derives explicit resource-cost/irreversibility tradeoffs for channels. These neighborhoods must be treated as imported/known rather than GC-II novelty.

## Next exact experiment
Enumerate minimal finite endogenous-transition worlds with equal `(Omega_forward, Omega_reverse)` but distinct round-trip future-capability quotients. Search first over 3-5 operational states, 2 actions, binary information/rule flags, and bounded resource vectors. If a witness exists, minimize it and test invariance under state relabeling and zero-cost operational equivalence. If no witness exists in the model class, record the collapse theorem/counterevidence instead of forcing a new invariant.