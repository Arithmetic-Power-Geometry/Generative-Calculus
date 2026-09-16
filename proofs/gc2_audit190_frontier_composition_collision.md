# GC-II Audit 190 — Closure-conditioned frontier composition collision

## Question
Can the correspondence `gain g -> attainable minimal cost frontier F_g` satisfy a composition law that is specifically generative and therefore escapes ordinary multiobjective optimization?

## Independent additive case
For two independently composable tasks with attainable cost sets C1 and C2 and additive resource vectors, sequential composition has

C12 = C1 + C2 = {c1+c2 : c1 in C1, c2 in C2}.

Therefore its nondominated frontier is

F12 = Pareto(C1 + C2).

Dominated points in either factor cannot create a nondominated sum: if a' <= a componentwise then a'+b <= a+b. Hence

F12 = Pareto(F1 + F2).

Status: **PROVED**, but the mechanism is the standard Pareto/Minkowski (Pareto-sum) construction, not a GC-II novelty.

## Compatibility counterexample
Let both marginal witness-cost sets be

C = D = {(0,2),(2,0)}.

System X permits only aligned witness pairs. Its composed frontier is

FX = {(0,4),(4,0)}.

System Y permits only crossed witness pairs. Its composed frontier is

FY = {(2,2)}.

The two systems have identical marginal attainable sets and identical marginal Pareto frontiers but different composed frontiers. Thus no universal composition functional of marginal frontiers alone can recover the operational composed frontier when compatibility/interface rules matter.

Status: **PROVED** by explicit finite counterexample; exact verifier in `experiments/gc2_audit190_frontier_composition_collision.py`.

## Novelty audit
The independent equality is ordinary multiobjective geometry: nondominated filtering of Minkowski sums is the Pareto-sum operation. It therefore cannot serve as the Paper-II breakthrough. Compatibility-sensitive failure also continues the joint-structure lesson from Audits 181–183 rather than creating a new invariant.

## Ledger
- `F12 = Pareto(F1 + F2)` under independent additive composition: **PROVED / IMPORTED-KNOWN mechanism**.
- Universal recovery of composed frontier from marginal frontiers under arbitrary compatibility: **FALSIFIED**.
- Compatibility counterexample with identical marginal frontiers and different global frontiers: **PROVED**.
- Generic `g -> F_g` composition as GC-II breakthrough: **FALSIFIED in the natural additive formulation**.
- Surviving target: a law on *frontier deformation under endogenous acquisition of compatibility/semantics* that cannot be represented as a fixed feasible-set change followed by ordinary Pareto filtering: **OPEN**.

## Next gate
Do not search for another static Pareto identity. Formalize an intervention that changes the operational feasibility relation itself and measure the induced set-valued derivative/finite difference of budgeted closure. Then collision-test that object against parametric/vector optimization, sensitivity analysis, viability kernels, resource monotones, and dynamic programming before assigning novelty.
