# GC-II Audit 173 — Budget-Constrained Admissible Realization: Energy-Game Boundary

Status date: 2026-09-16
Branch scope: `gc2-capability-accounting-lab` only. GC-I/main unchanged.

## Objective

Attack Audit 172's surviving target: whether a capability with small ordinary Nerode complexity can require large or impossible realization because quotient transitions must themselves obey GC resource budgets.

## Formal finite model

Let a capability specification be recognized by a deterministic quotient automaton Q with transition function delta. An implementation state is (q,r), where q is a quotient state and r in Z^d is a vector of available operational resources (R/I/A/L may be represented as coordinates after units are fixed). Each implementation of a quotient transition q --a--> q' chooses an admissible physical transition e with resource update w(e) in Z^d. A run is budget-admissible when every prefix resource vector remains in the permitted region, in the simplest energy case r >= 0 coordinatewise.

Define realizability under initial credit b as existence of a controller/strategy that implements every required capability transition while maintaining the resource invariant against the allowed environment choices.

## Separation from ordinary Nerode size

Ordinary state complexity and admissible realization are distinct quantities. A one-state capability language can be unrealizable under a finite resource budget.

Example: Sigma={a}, L=Sigma*. Its minimal DFA has one state. Suppose the only admissible implementation of each required a-transition consumes one unit of a nonrenewable resource: w(a)=-1. With finite initial credit B, after B+1 required a-actions the resource is negative. Hence no controller realizes the infinite capability, despite Nerode index 1.

Conversely, if an admissible self-loop has w(a)=0, the same one-state capability is realizable with zero initial credit.

Thus identical ordinary Nerode structure can have different operational realizability once admissible resource dynamics are included.

Status: PROVED, but not novel.

## Exact collision with energy games

Under the finite graph, additive vector-resource, prefix-nonnegativity semantics above, the GC admissible-realization problem is exactly an energy-game / multi-dimensional energy-game realization problem after taking the product of the capability automaton with the implementation graph.

Mapping:

- capability/implementation product state -> game vertex;
- controller/environment choices -> player choices;
- R/I/A/L additive resource changes -> edge weight vector;
- admissibility of every prefix -> energy objective;
- initial operational budget -> initial credit.

The mapping preserves runs, strategies, prefix resource vectors, and winning/realizability. Therefore a small ordinary Nerode index but large/infinite resource requirement is not by itself a GC-II breakthrough: resource-sensitive synthesis already studies exactly this separation.

Known energy-game results are stronger than the toy separation: multi-dimensional energy games model synthesis of resource-bounded processes; finite-memory strategies and nontrivial memory requirements are established. Energy parity games combine qualitative specifications with quantitative energy constraints and can require exponential memory. Energy timed automata additionally combine resource bounds with timing and controller synthesis.

## No-Free-Capability statement in this model

A valid but imported conditional theorem follows. If every implementation of each occurrence of a required action decreases a scalar resource by at least epsilon>0, and the specification requires arbitrarily many such occurrences with no admissible replenishment, then no finite initial budget realizes the specification.

Proof: after n occurrences the resource has decreased by at least n epsilon. For n > B/epsilon, prefix nonnegativity fails.

This is a direct energy accounting argument, not a new GC theorem.

## Dimension/domain checks

- Resource coordinates cannot be summed or compared before fixing compatible units or treating them as a vector/Pareto constraint.
- Additive integer weights are a modeling restriction, not a consequence of GC.
- Replenishment transitions can invalidate simple cumulative-consumption lower bounds.
- Zero-cost cycles permit indefinite behavior without additional budget.
- Negative cycles controlled by the environment can make finite-credit realization impossible; positive/recharging cycles can make it possible.
- If resources are continuous, timed, stochastic, path-dependent, or nonadditive, this exact reduction may fail, but richer resource-constrained control models must then be collision-checked.
- If information or interface constraints alter observations rather than merely edge costs, partial-observation games/synthesis become the relevant known boundary.

## Composition behavior

For independent additive resource systems, product implementation concatenates resource vectors and preserves coordinatewise safety. There is no universal scalar additive realization complexity unless a calibration is imposed. Shared resources create interaction terms; this does not escape energy/resource-game theory when represented in the joint weight vector.

## Prior-art collision ledger

- ordinary minimal state complexity: Myhill-Nerode — IMPORTED/KNOWN (Audit 172).
- finite additive resource-constrained realization: energy games / multi-dimensional energy games — IMPORTED/KNOWN.
- qualitative specification plus resource safety: energy parity/resource-aware synthesis — IMPORTED/KNOWN.
- timing plus bounded resources: energy timed automata — IMPORTED/KNOWN.
- partial observation: must be checked against partial-observation games and supervisory control.

## Consequence for GC-II

The naive `budget-constrained admissible Nerode complexity` route is FALSIFIED as an independent breakthrough whenever GC admissibility is encoded by finite-state additive resource updates and prefix resource constraints. A separation between ordinary state complexity and operational realization is real, but already classical resource-sensitive synthesis.

A surviving GC-specific target must use structure not reducible to a fixed finite resource-game product. The strongest candidate is **endogenous admissibility**: executing a transformation changes not only resource levels/state but the future set of admissible transformations, observation interfaces, or even the operational task/protocol family in a way that cannot be represented by a fixed finite sufficient-state augmentation of bounded size. The novelty burden is high: finite endogenous rule changes always compile into a larger game state, so a theorem must quantify an unavoidable growth/non-uniformity of the required augmentation, not merely exhibit history dependence.

Candidate target for Audit 174:

Construct a family G_n with a fixed/small external capability quotient but prove that every fixed finite-state compilation preserving exact budgeted closure requires augmentation size growing with n because admissibility rules themselves encode a dynamically generated context. Then compare the lower bound against succinct games, pushdown/VASS/Petri-net models, dynamic epistemic systems, partial-observation synthesis, reconfigurable transition systems, and communication complexity. If the construction simply stores a finite context label, it is not novel.

## Status ledger

| Candidate | Status | Reason |
|---|---|---|
| Small Nerode index but impossible finite-budget realization | PROVED / IMPORTED mechanism | one-state depletion example; energy games |
| Product reduction for finite additive R/I/A/L prefix constraints | PROVED under stated encoding / IMPORTED-KNOWN | exact energy-game mapping |
| No-free capability under uniform positive consumption and no replenishment | PROVED / IMPORTED-KNOWN | cumulative energy accounting |
| Budget-constrained admissible Nerode complexity as independent GC-II novelty | FALSIFIED for finite additive resource model | resource-sensitive synthesis collision |
| Endogenous/non-uniform admissibility requiring growing compilation | OPEN | must survive succinct/infinite-state/reconfigurable-system prior art |
