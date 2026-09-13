# GC-II Audit 125 — Budget-Coupled Endogenous Admissibility Compiles to Constrained Reachability

## Scope
Paper-II branch only: `gc2-capability-accounting-lab`. GC-I on `main` remains frozen.

Starting branch head inspected for this audit: `63ece324be9f41107bf7447edcf7c11abd10e6ba` (Audit 124).

## Target inherited from Audit 124
Test whether a *single finite budget shared across resources/information/interfaces/rule modification* can rescue endogenous admissibility from the augmented-state collapse. The hoped-for mechanism was that performing one capability changes the admissible future transformation set while simultaneously consuming a coupled budget, possibly yielding a non-tautological closure-escape invariant.

## Result
**FALSIFIED as a standalone GC-II novelty mechanism for finite/computably represented systems.** Once the remaining budget and every continuation-relevant rule/interface mode are included in operational state, budget-coupled endogenous admissibility is ordinary state-dependent constrained reachability / dynamic programming.

This is stronger than merely saying that a changing action set can be stored as state (Audit 086): the same compilation preserves the *coupled remaining budget* and therefore preserves exact budget-feasible histories, closure membership, and any endpoint predicate evaluated on those histories.

## Formal model
Let

- `x in X` be the ordinary operational state;
- `m in M` be the continuation-relevant rule/interface/admissibility mode;
- `b in B` be remaining budget, scalar or typed;
- `U` be a fixed finite or computably presented action universe;
- `E(x,m,b,u)` be the admissibility predicate;
- `T(x,m,u)=(x',m')` be the state/mode update;
- `c(x,m,u,x',m')` be nonnegative budget consumption.

An action is feasible iff

\[
E(x,m,b,u)=1,
\qquad
c(x,m,u,x',m')\preceq b.
\]

The budget update is

\[
b' = b-c(x,m,u,x',m').
\]

For a typed budget this is coordinatewise. More general finite bookkeeping can be included by replacing subtraction with an explicit budget-update map.

Define augmented state

\[
\boxed{z=(x,m,b)}.
\]

The compiled fixed-alphabet transition system admits `u in U` at `z` exactly when the original system admits it and maps

\[
(x,m,b)\xrightarrow{u}(x',m',b').
\]

## Theorem — Budgeted Endogenous-Admissibility Compilation
**Status: PROVED.**

Assume all continuation-relevant admissibility/rule information and remaining budget are represented by `(x,m,b)`, and `U`, `E`, `T`, and the budget update are explicit. Then for every finite horizon `h`, initial configuration `(x0,m0,b0)`, and action word, the native endogenous-admissibility system and the compiled fixed-alphabet augmented-state system have exactly the same feasible prefixes and exactly the same terminal augmented states.

### Proof
Induct on prefix length.

Base case `h=0`: both systems start at the same augmented configuration `(x0,m0,b0)`.

Inductive step: suppose the two descriptions agree after a feasible prefix and are at the same `(x,m,b)`. They evaluate the same admissibility predicate `E`, the same budget-feasibility condition, the same transition `T`, and the same budget update. Hence they admit exactly the same next actions and produce exactly the same `(x',m',b')`. Therefore equality of feasible histories and terminal augmented states holds for all finite horizons. QED.

## Corollaries

### 1. Exact budgeted closure preservation — PROVED
For any task predicate `G` defined on terminal augmented states or full preserved histories,

\[
\mathcal C^{\mathrm{native}}_{\le b_0}(G)
=
\mathcal C^{\mathrm{compiled}}_{\le b_0}(G).
\]

Thus a novelty gap created solely by describing the action/rule set as endogenous instead of state-dependent cannot survive this quotient.

### 2. No-Free-Capability does not emerge automatically — FALSIFIED as a novelty source
If a capability becomes reachable only after paying for an action that modifies admissibility, that statement is simply a constrained reachability fact in the augmented model. A lower bound is scientifically interesting only if it adds structure not already expressible as ordinary path cost, resource constraint, or reachability certificate.

### 3. Coupling does not rescue the mechanism — PROVED under the model
Nonseparable dependence of admissibility on `(x,m,b)` is allowed. The theorem does not assume additive value functions, independent resources, convexity, or separable policies. The compilation uses the joint state directly.

## Exact finite exhaustive experiment
Artifact: `experiments/gc2_budget_coupled_endogenous_admissibility_audit.py`.

The test enumerates:

- 2 physical states;
- 2 admissibility modes;
- fixed alphabet of 2 actions;
- mode 0 permits only action 0; mode 1 permits both actions;
- all 16 deterministic physical transition tables;
- all 16 deterministic mode-transition tables;
- shared remaining budgets `{0,1,2,3}`;
- horizons `0..4`;
- all physical/mode starting states.

Total systems: **256**.

Systems in which an allowed action actually changes the future admissibility mode: **224**.

Native-vs-compiled start/budget/horizon comparisons: **20,480**.

Mismatches: **0**.

Frozen output: `results/gc2_budget_coupled_endogenous_admissibility_audit.json`.

This is exact enumeration, not stochastic simulation.

## Prior-art collision
The surviving mechanism reduces directly to established constrained-state/action control machinery.

- Standard MDP definitions already allow the available action set to depend on state (`A_s`).
- Viability theory explicitly treats state constraints together with state-dependent control constraints and asks whether admissible evolutions remain viable.
- Budget-limited MDP algorithms commonly augment state with remaining budget; exact dynamic-programming methods then operate on this enlarged state.
- Automaton/product-state constructions similarly compile history- or rule-dependent constraints into state before planning/control.

Therefore `endogenous admissibility + finite coupled budget` is not, by itself, a new mathematical object.

Useful collision references for this audit:

1. J.-P. Aubin, “A Survey of Viability Theory,” *SIAM Journal on Control and Optimization* — state and state-dependent control constraints.
2. Moreira, Delgado, de Barros, Mauá, “Efficient algorithms for Risk-Sensitive Markov Decision Processes with limited budget,” *International Journal of Approximate Reasoning* (2021) — algorithms over augmented states enumerating remaining budgets.
3. Standard MDP formalism with state-dependent action sets `A_s`.

## Edge-case audit
- **Zero budget:** no positive-cost action is feasible; both descriptions agree.
- **Zero-cost actions:** allowed; compilation still preserves them, but zero-cost cycles may make horizon-free reachability require ordinary cycle/fixed-point analysis.
- **Typed budget:** replace scalar order by coordinatewise or explicitly declared feasibility relation.
- **Nonadditive coupling:** if continuation-relevant bookkeeping is finite/computable, include it in state; theorem does not require additive scalarization.
- **Stochastic transitions:** same construction lifts to transition kernels; equality becomes equality of path distributions.
- **Infinite horizon:** finite-state cases reduce to standard fixed-point/reachability questions; unbounded memory may require infinite augmented state.
- **Hidden external state:** if it changes future feasibility, omission means the declared operational state was insufficient.
- **Open/noncomputable action universe:** outside theorem; remains OPEN, but failure of compilation alone is not novelty.
- **Resource replenishment:** represent budget update explicitly; state augmentation still applies if the update is continuation-sufficient.
- **Rule modification that changes semantics of old actions:** include the rule semantics/mode in `m`; if no sufficient representation exists, that stronger case requires separate analysis.

## Status ledger
| Candidate | Status |
|---|---|
| Finite/computable budget-coupled endogenous admissibility compilation | **PROVED** |
| Exact finite exhaustive native/compiled agreement | **NUMERICALLY SUPPORTED by exhaustive enumeration** |
| State-dependent action/control constraints | **IMPORTED/KNOWN** |
| Remaining-budget state augmentation / constrained DP | **IMPORTED/KNOWN** |
| Endogenous admissibility + finite shared budget as standalone GC-II breakthrough | **FALSIFIED** |
| Nonadditivity as an automatic escape | **FALSIFIED under sufficient-state representation** |
| Open/noncomputable boundary with no continuation-sufficient representation | **OPEN** |
| GC-II positive breakthrough | **NOT ESTABLISHED** |

## Consequence for Paper II
The next viable target cannot merely say that capability changes what becomes possible later while spending budget. That phenomenon is already a constrained transition system once continuation-relevant state is explicit.

A stronger surviving target is:

**Counterfactual capability accounting under intervention on the admissibility generator.** Seek two systems with identical complete factual reachable augmented-state graphs and identical typed path-cost sets, but different *counterfactual closure responses* under an independently specified family of admissibility-generator interventions. Any candidate invariant must then survive reduction to causal models, bisimulation under interventions, robust/control games, mechanism design, and parametric MDP sensitivity.

This target is **OPEN** and is not claimed as novel until those collisions are defeated.
