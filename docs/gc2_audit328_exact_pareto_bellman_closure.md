# GC-II Audit 328 — Exact Pareto Bellman budget closure

## Status

**PROVED** for finite deterministic information-state systems with branch-relative admissibility and nonnegative vector resource costs. The dynamic-programming mechanism is standard multiobjective/robust DP territory and is therefore **IMPORTED/KNOWN** as machinery; the point here is to close the GC-II operational accounting gap exposed by Audits 326–327 without illicit scalarization.

## Model

Let `C` be a finite information cell. A cell is terminal when the required decision is homogeneous on it. At unresolved `C`, an admissible action `u` has a nonnegative resource vector `c(C,u) in R_+^d` and finitely many nonempty outcome children `C_{u,y}`. After observing `y`, the policy may choose a different continuation.

For a complete resolving policy `pi`, define its robust resource reservation recursively by

`R(pi,C) = c(C,u) + max_y R(pi_y,C_{u,y})`,

where `max` is coordinatewise. This is simultaneous coordinatewise feasibility under adversarial outcomes; it does not assert that one realized trajectory consumes all coordinate maxima.

Let `F(C)` be the Pareto-minimal robust reservation vectors of all finite resolving policies from `C`. Write `Min(.)` for deletion of componentwise dominated vectors.

## Exact Pareto Bellman theorem

For terminal `C`,

`F(C) = {0}`.

For unresolved `C`,

`F(C) = Min union_{u in Adm(C)} { c(C,u) + max_y r_y : r_y in F(C_{u,y}) for every nonempty child y }`,

with an action contributing nothing if any child has empty frontier (no finite resolving continuation).

### Proof

**Soundness.** Pick an admissible `u` and one frontier continuation vector `r_y` for each outcome child. By definition of each `r_y`, a finite resolving continuation policy exists in that child. Combining those continuations after `u` yields a finite resolving policy. Its robust reservation is exactly `c(C,u)+max_y r_y`. Pareto minimization cannot create an infeasible vector.

**Completeness.** Take any finite resolving policy `pi` at `C`. Its root action is some admissible `u`; each outcome child has a finite resolving continuation with vector `q_y`. If `q_y` is dominated by a frontier vector `r_y in F(C_{u,y})`, replacing that continuation cannot increase any resource coordinate. Repeating over children yields a generated Bellman vector no larger than `R(pi,C)`. Hence every globally Pareto-minimal policy vector must occur in the displayed recurrence after `Min`.

Therefore the recurrence is exact.

## Budgeted Closure-Escape corollary

For a budget vector `b in R_+^d`, a finite resolving admissible policy exists within simultaneous robust budget `b` iff

`exists r in F(C) such that r <= b` componentwise.

Thus finite deterministic budgeted Closure Escape has an exact set-valued certificate: the Pareto frontier, not a canonical scalar cost.

The unbudgeted Audit-324 fixed-point result is recovered by replacing every nonempty frontier by Boolean TRUE. A scalar Bellman recurrence is recovered only after choosing a one-dimensional resource semantics (`d=1`) or an explicit scalarization whose loss is accepted. Audit 327 explains why scalarizing branch costs before adversarial aggregation is not generally equivalent.

## Composition and edge audit

- **Zero resources:** all-zero costs are allowed; Pareto deletion remains valid.
- **No admissible action:** unresolved cell has `F(C)=empty`.
- **Dead child:** an action with one child frontier empty is unusable for guaranteed resolution.
- **One resource:** recurrence reduces to ordinary minimax Bellman cost.
- **One outcome:** coordinatewise max is identity, giving serial vector addition.
- **Monotonicity in budget:** if `b <= b'`, feasibility at `b` implies feasibility at `b'`.
- **Resource relabeling:** permutation of coordinates permutes the frontier and preserves feasibility.
- **Positive coordinate rescaling:** diagonal positive rescaling commutes with addition, coordinatewise max, dominance, and the recurrence.
- **Serial prefix composition:** a deterministic prefix cost translates every continuation vector by that cost.
- **Branch composition:** outcome-conditioned continuations combine by coordinatewise max, not addition.
- **Cycles:** the displayed structural recursion is immediately executable on acyclic/well-founded information descent. General finite cyclic systems require a least-fixed-point formulation over upward-closed budget sets; no stronger cyclic claim is made here.

## Collision / novelty discipline

The recurrence is structurally a multiobjective robust dynamic program / AND-OR policy recursion. That general machinery is known. GC-II should not claim invention of Pareto DP. What is established here is the internally necessary exact accounting object for the operational closure model after the scalar no-go results: vector resource feasibility is represented by a Pareto frontier, and budgeted Closure Escape is exactly frontier domination in this finite deterministic subclass.

## Consequence for Omega_G

Any candidate bound `Omega_G <= F(Delta R, Delta I, Delta A, Delta L)` that intends exact native resource feasibility must treat `Delta R` as vector/set-valued (or explicitly state a scalarization). The recurrence supplies a reproducible operational definition of the resource component rather than an informal aggregate.

## Verification

`experiments/gc2_audit328_pareto_bellman_verify.py` independently compares the recurrence against direct enumeration of complete policies on many small exact integer AND-OR trees and checks budget-feasibility equivalence, scalar reduction, coordinate permutation, and positive diagonal rescaling.
