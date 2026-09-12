# GC-II Audit 098 — Composition-Law Residual Exists but Collapses to Established Process Semantics

## Status

- Equality of complete one-step/static realization data does **not** determine finite-horizon sequential closure: **PROVED** by explicit finite counterexample.
- Exhaustive two-state/two-action check: **NUMERICALLY SUPPORTED / exact enumeration**.
- Full reachable transition/composition law plus typed costs/outcomes determines every finite-horizon budgeted closure: **PROVED** by induction.
- Claim that the residual created by changing composition while holding static realization fixed is itself a GC-II breakthrough: **FALSIFIED**.
- A composition-compatible obstruction surviving established transition-system/process/resource-theory semantics: **OPEN**.

## Question

Audit 097 showed that even every proper R/I/A/L projection can miss a static joint-realization obstruction. The next stronger proposal was to hold the complete static realization information fixed and seek a separation caused only by composition-constrained realizability.

Such a separation certainly exists. The key question is whether it is new.

## Minimal exact counterexample

Let the state space be X={0,1}, initial state x0=0, and primitive actions be a and b. Give the two actions identical typed resource charges in both systems, for example

c(a)=c(b)=(1,0,0,0).

Define System A by

a_A: 0->0, 1->0,
b_A: 0->1, 1->0,

and System B by

a_B: 0->0, 1->0,
b_B: 0->1, 1->1.

From x0=0 the complete labelled one-step realization data are identical:

a sends 0 to 0,
b sends 0 to 1,

with the same typed costs. Hence any state-free static realization relation for the primitive actions is identical.

But after two steps the systems differ:

bb sends 0 to 0 in A,
bb sends 0 to 1 in B.

Therefore equality of static primitive realization information does not imply equality of sequential capability closure.

## Exact exhaustive check

The executable audit enumerates every deterministic two-state/two-action system. Each action is one of the four functions {0,1}->{0,1}, so there are 4^2=16 systems.

Systems are grouped by their complete labelled one-step signature at the initial state,

(delta(0,a), delta(0,b)).

There are 24 unordered system pairs with an identical one-step signature. Of these:

- 18 pairs have different length-2 labelled trace maps;
- 6 pairs remain identical at length 2;
- total exact pair checks: 24.

Thus the static-to-sequential incompleteness is not an isolated hand-built anomaly.

## Composition-completeness no-go theorem

Consider two deterministic finite operational systems A and B with the same initial state space representation, action alphabet, reachable transition function, typed edge-cost function, task/outcome evaluation, and error evaluation. More generally, suppose there is a reachable-state bijection phi preserving all of those objects and satisfying

phi(delta_A(x,a)) = delta_B(phi(x),a)

for every reachable x and admissible a, while also preserving typed costs and task/error labels.

Then for every finite horizon T and every typed budget B,

C_A(T,B) = C_B(T,B)

up to phi.

### Proof

At horizon 0 the initial reachable states and budget records agree. Assume all admissible histories of length t correspond under phi with identical accumulated typed costs and task/error labels. For any admissible next action a, transition preservation maps the A successor to the B successor, and cost preservation adds the same typed charge. Therefore admissibility under the remaining budget and all outcome/error labels are preserved at length t+1. Induction gives a cost- and outcome-preserving bijection between all finite histories, hence identical finite-horizon budgeted closures. QED.

The same argument extends to stochastic kernels by replacing state correspondence with equality/isomorphism of the relevant transition kernels and preserving the cost/observation structure.

## Why this falsifies the candidate as standalone novelty

The new residual appears only because static realization data omit the law of sequential composition/state transition. Once the transition/composition structure is supplied, the finite-horizon operational closure is determined.

That is standard territory:

1. labelled transition systems represent state-based behaviour through action-labelled transitions and compare systems by trace/bisimulation-style semantics;
2. deterministic automata generate transition monoids/semigroups by composing the transformations induced by primitive actions;
3. process calculi and coalgebraic trace semantics study precisely how operational composition determines observable behaviour;
4. resource theories formulated categorically already take sequential composition of transformations as primitive structure.

Therefore a GC-II theorem whose content is merely

"same static realizations, different sequential composition => different closure"

is a restatement of established process/automata/resource-theory structure.

## Stronger novelty gate

A surviving Paper-II candidate must not obtain its effect merely by omitting and then restoring any of the following:

- state-dependent transition law;
- action-enabledness relation;
- sequential composition operator;
- observation/output kernel;
- typed edge costs;
- history state that makes the process Markov;
- process equivalence information already captured by trace, simulation, bisimulation, transition-monoid, or standard resource-theory semantics.

If the claimed Omega_G disappears once those structures are represented, it is not a new GC invariant.

## Consequence for Closure Escape and No-Free-Capability

This audit blocks a tempting route to a non-tautological Closure-Escape theorem. A positive residual between static realization and sequential closure can always be explained here by omitted transition/composition information. Likewise, a No-Free-Capability theorem based only on the need to retain that information reduces to ordinary state/process realization complexity unless a stronger cross-structure obstruction is proved.

The next surviving target must therefore compare systems after quotienting by, or explicitly matching, the relevant standard process semantics. One possible hard target is a typed budget obstruction that survives ordinary trace equivalence and standard resource-preserving simulation/bisimulation summaries yet yields a new quantitative closure consequence. This remains **OPEN** and must be attacked against weighted/probabilistic bisimulation, costed transition systems, process resource theories, and multi-resource automata before any novelty claim.

## Edge and domain checks

- Horizon T=0: closures agree trivially.
- Horizon T=1: the constructed systems agree by design.
- Horizon T=2: separation occurs on trace bb.
- Degenerate one-state systems: no analogous state-mediated separation exists unless outputs/costs themselves differ.
- Typed dimensions: the counterexample does not depend on units; identical typed action costs can be assigned in any compatible R/I/A/L units.
- Monotonicity/free disposal: adding unused budget does not remove the trace separation.
- Invariance: renaming states or primitive actions preserves the argument.
- Composition: explicitly tested and is the source of the separation.
- Additivity: no additive resource law is assumed beyond accumulation of the chosen identical per-edge charges in the finite witness.

## Prior-art collision notes

- Labelled transition systems define behaviour through action-labelled transitions and traces; sequential differences after identical initial behaviour are standard process-semantic phenomena.
- Transformation semigroups/transition monoids are generated exactly by composition of action-induced state transformations.
- Symmetric-monoidal formulations of resource theories include sequential composition as part of the basic mathematical structure.
- Recent 2026 work on compositional coalgebraic trace semantics further confirms that compositionality of observable process behaviour remains an explicit established research framework.

## Falsification decision

**Decisive:** holding complete static primitive realization data fixed does not fix sequential closure, but the residual is generated by omitted transition/composition structure and therefore collapses to established automata/process/resource-theory semantics. It is not, by itself, the GC-II breakthrough.
