# GC-II Audit 355 — finite endogenous admissibility compiles to ordinary reachability

## Status

**PROVED / IMPORTED-KNOWN MECHANISM / DECISIVE NOVELTY BOUNDARY.**

GC-I on `main` is unchanged. This audit follows Audit 354 and tests the most immediate proposed escape from fixed monotone co-design: information-dependent admissibility and endogenous rule/interface activation.

## Model

Let an operational configuration be

`z = (x,m,r,q)`

where:

- `x in X` is the physical/logical state;
- `m in M` is the currently retained information/memory state;
- `r in R` is the resource state (remaining budget, inventory, or a finite resource ledger);
- `q in Q` is the currently active rule/interface/authorization state.

Let `A` be a finite action set. Admissibility may depend arbitrarily on the entire current configuration:

`Adm(z,a) in {0,1}`.

An admissible action may simultaneously change physical state, acquire/delete information, consume/replenish resources, and activate/deactivate rules or interfaces. Write the finite transition relation as

`T subseteq Z x A x Z`,  where `Z = X x M x R x Q`,

with `(z,a,z') in T` only when `Adm(z,a)=1` and `z'` is a permitted successor.

This includes deterministic and nondeterministic finite systems. A target capability is any target set `G subseteq Z` (or any projection condition on `x`, encoded as its inverse image in `Z`).

## Theorem — Finite Endogenous-Admissibility Compilation

For every finite system above, define the static directed graph

`G_T = (Z,E_T)`,

where

`(z,z') in E_T  iff  exists a in A : (z,a,z') in T`.

Then for every initial configuration `z0` and target set `G`,

`G is operationally achievable from z0`

iff

`there exists a finite admissible action sequence from z0 to some g in G`

iff

`some g in G is reachable from z0 in G_T`.

### Proof

Every admissible operational execution `z0 --a1--> z1 --...-- ak--> zk` induces the graph path `z0 -> z1 -> ... -> zk` by the definition of `E_T`. Conversely, every graph edge `(zi,zi+1)` has at least one witnessing action `ai` with `(zi,ai,zi+1) in T`; choosing one witness per edge reconstructs an admissible operational execution. Therefore the path sets coincide after forgetting action labels, and target reachability is identical. QED.

## Corollary — finite information-dependent admissibility is not by itself a new closure theory

If information acquisition changes which later actions are admissible, but all relevant information states, resource states, and rule/interface states are finite and explicitly representable, augmenting the operational state by `(m,r,q)` restores an ordinary static reachability problem.

Thus the slogan

`information changes admissibility`

is insufficient to distinguish GC-II mathematically from classical state augmentation / transition-system reachability.

## Corollary — exact budgeted closure

If a finite budget ledger is included in `R`, then budget feasibility is already encoded in the augmented state. The budgeted closure of `z0` is exactly the projection of its reachable set in `G_T`. No separate generative primitive is required for this finite explicit model.

## Corollary — finite endogenous rule/interface generation

Suppose actions can create, remove, or authorize rules/interfaces, but the set `Q` of possible active configurations is finite. Then this endogeneity also compiles into the augmented state graph. Merely allowing rules to change over time does not escape classical reachability.

## Size bound and where the difficulty moves

The explicit compiled state space has

`|Z| = |X| |M| |R| |Q|`.

So compilation can cause severe state explosion. If `M`, `R`, or `Q` are themselves factored descriptions, the explicit graph may be exponentially larger than the intensional specification. The theorem is therefore an exact semantic reduction, not a claim of efficient compilation.

This identifies the surviving GC-II frontier more sharply: a breakthrough must concern representation/complexity/irreducibility of the augmentation, unbounded or continuous sufficient state, endogenous creation of genuinely new state coordinates/types, semantic restrictions on permissible compilation, or local-to-global translator lower bounds. Finite explicit endogeneity alone is not enough.

## Edge and degeneration audit

- Empty action set: only the initial configuration is reachable; theorem is immediate.
- Empty target: both sides are false.
- Initial state already in target: zero-length execution/path satisfies both sides.
- Self-loops: harmless.
- Nondeterminism: represented by multiple outgoing edges; existential capability semantics is preserved.
- Information deletion or nonmonotone memory: allowed because `M` is an arbitrary state set.
- Resource replenishment/nonmonotone ledger: allowed because `R` is arbitrary and finite; no monotonicity assumption is used.
- Rule deactivation as well as activation: allowed because `Q` is an arbitrary state set.
- Composition: sequential composition is exactly graph-path concatenation.
- Relabelling: invariant under bijections of the component state sets.

## Prior-art collision

The compilation mechanism is classical. Finite-state transition systems encode behavior as states plus a transition relation, and planning/reachability uses paths in that state space. Under partial observability, classical POMDP theory similarly restores Markov structure by augmenting to an information/belief state; belief is a sufficient statistic for the action-observation history. Therefore this theorem is used as a **novelty boundary**, not claimed as new automata/planning mathematics.

Public anchors inspected 2026-09-24:

- MIT Underactuated, *Planning Under Uncertainty*: belief state as a sufficient statistic for POMDP history — https://underactuated.csail.mit.edu/belief.html
- Ross et al., *Online Planning Algorithms for POMDPs*: belief state summarizes action/observation history — https://pmc.ncbi.nlm.nih.gov/articles/PMC2748358/
- PMLR, Aberdeen, Buffet & Thomas, *Policy-Gradients for PSRs and POMDPs*: sufficient-statistic state representations for history-dependent control — https://proceedings.mlr.press/v2/aberdeen07a.html

## Classification

- Finite Endogenous-Admissibility Compilation theorem: **PROVED**.
- State-augmentation/reachability mechanism: **IMPORTED/KNOWN**.
- Claim that finite information-dependent admissibility alone supplies the GC-II breakthrough: **FALSIFIED**.
- Claim that finite rule/interface activation alone supplies the GC-II breakthrough: **FALSIFIED**.
- Efficient compilation in general: **NOT CLAIMED**.
- Representation-independent lower bound for an exact local-to-global translator: **OPEN; priority**.
- Unbounded/continuous/intensional endogenous capability state that resists finite explicit compilation: **OPEN; priority**.

## Consequence for Paper II

Do not build the central novelty claim on finite endogenous admissibility alone. The next attack should target the *cost or impossibility of sufficient-state compilation*: prove when any exact translator from local/factored descriptions to global capability closure must retain exponentially many distinguishable operational contexts, or identify a stronger GC-I projection-irreducibility condition that forces such a lower bound.
