# GC-II Audit 365 — Endogenous observation-generation collision boundary

## Scope

This audit attacks the surviving target after Audit 364: whether allowing the observation/test language itself to be generated during execution yields a GC-II-specific closure-escape or translator lower bound.

GC-I on `main` is treated as frozen. This note concerns only the GC-II capability-accounting branch.

## Model

Let a finite operational configuration be

\[
z=(x,m,r,q,G),
\]

where `x` is physical/logical state, `m` retained information, `r` the resource ledger, `q` active rules/interfaces, and `G` the currently available observation-generator set. An admissible operation may change any component, including `G`. A sensing operation chosen from the current `G` returns an outcome and updates the configuration. A restoration/capability decision is correct when its action belongs to the valid action set for every latent world compatible with the realized history.

The important restriction is that generated observations are not oracle partitions: they must arise through admissible operational transitions.

## Proposition 365.1 — finite endogenous-generator compilation

**Status: PROVED; mechanism IMPORTED/KNOWN.**

If the complete operational configuration space `Z` is finite and every admissible generator-creation, sensing, resource, rule and action update is represented in the transition relation, then endogenous observation generation is exactly representable as an ordinary finite partially observed sequential decision process on `Z`.

### Proof

At every history, the currently available generators are already a component of the complete state. For each state `z`, create one transition for every currently admissible generator-creation, sensing, or terminal action. A sensing transition is labelled by its observation outcome. Updating `G` is no different formally from updating any other state component. Thus every endogenous policy induces a policy on the augmented finite state process, and conversely every policy on that augmented process corresponds to the same admissible endogenous execution. The two systems have identical history trees and terminal correctness sets. QED.

This is a semantic equivalence, not an efficiency statement.

## Corollary 365.2 — endogeneity alone is insufficient

**Status: FALSIFIED as a foundational-novelty route.**

The claim

> dynamically generating new tests/interfaces is by itself outside classical sequential decision theory

is false for finite explicit operational state. The generated test menu can be carried as state.

The same conclusion survives state-dependent query availability: the admissible query set is simply a function of the current augmented state.

## Proposition 365.3 — adaptive decision-region recursion

Let `C` denote the current set of latent worlds consistent with the history and let `A(C)` be the actions common to all worlds in `C`. Let `Q(C)` be the sensing/generator actions currently admissible at that information state. For a query `q` and outcome `o`, let `C_{q,o}` be the surviving child uncertainty set.

For finite deterministic sensing, universal correctness satisfies the recursion

\[
V(C)=1 \iff A(C)\neq\varnothing
\quad\text{or}\quad
\exists q\in Q(C)\;\forall o\in O_q(C):V(C_{q,o})=1.
\]

**Status: PROVED; IMPORTED/KNOWN mechanism.**

This is the standard AND/OR decision-tree / contingent-planning structure. If generator creation changes the future query menu, include that generator state in `C` (or, equivalently, in the augmented information state) and apply the same recursion.

## Collision audit

The surviving construction collides with several established families rather than escaping them:

1. **POMDP / contingent planning:** state-dependent sensing and history-conditioned policies are native objects once the sufficient state is augmented.
2. **Active diagnosis / discrete function evaluation:** adaptive queries are chosen until enough information is available for the decision, not necessarily for full world identification.
3. **Adaptive submodular optimization:** adaptive selection under partial observations and even varying query sets has established theory.
4. **Decision trees:** minimum-cost adaptive evaluation of a decision function is classical.

Therefore no novelty claim is made for the recursion, finite state augmentation, state-dependent test availability, or dynamic test-menu generation by themselves.

## Important non-result

Endogenous generation can still be computationally expensive, but this audit does **not** prove a representation-independent lower bound. An exponential explicit history/state tree is not enough: a compact symbolic controller may represent it. Any GC-II theorem must specify the allowed representation/compiler language and prove a lower bound that survives compact symbolic encoding.

## Surviving target

The remaining scientifically defensible route is narrower:

> Couple GC-I proper-projection irreducibility to a restricted operational generator algebra and prove that every admissible decision-preserving translator/controller must pay a quantitative cost that cannot be removed by ordinary augmented-state compilation.

Candidate costs include communication across a fixed interface cut, query complexity under a fixed projection oracle family, circuit/formula size in a fixed representation class, or resource expenditure required to synthesize a separating observable. These must be collision-tested against communication complexity, decision-tree/query complexity, CSP/database width, automata minimization, Blackwell sufficiency/deficiency, and active diagnosis before any novelty claim.

## Status table

- finite endogenous observation-generator compilation — **PROVED / IMPORTED-KNOWN mechanism**
- state-dependent query availability as escape from classical theory — **FALSIFIED**
- adaptive decision-region recursion — **PROVED / IMPORTED-KNOWN mechanism**
- endogenous observation generation alone as Paper-II breakthrough — **FALSIFIED**
- representation-independent cost from GC-I projection irreducibility — **OPEN**
- fixed-language quantitative lower bound tied specifically to GC-I — **OPEN / PRIORITY**

## Prior-art boundary checked

This audit deliberately treats active diagnosis, decision-tree evaluation, POMDP/contingent planning, adaptive submodularity, and adaptive optimization with varying query sets as collision classes. No novelty is assigned to results reducible to those mechanisms.
