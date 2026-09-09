# GC-II Audit 027 — Structural Augmentation Compilation Boundary

## Status

**PROVED boundary theorem / FALSIFIED as a standalone novelty route / IMPORTED-KNOWN mechanism.**

This audit tests the post-Audit-026 proposal that GC-II might obtain a new semantic class merely by allowing admissible transformations to create, delete, or rewrite future information channels, interfaces/actions, rules, or transition structure.

## 1. Dynamic structural model

Let a GC structural configuration be

\[
C=(G,B,I,A,L,\Theta),
\]

where `G` is the current capability/transition structure, `B` is the residual vector budget, `I` is available information, `A` is the current interface/action family, `L` is the active rule family, and `Theta` contains the task-scale-error observations relevant to the accounting problem.

An admissible structural augmentation is a partial relation

\[
u:C\rightsquigarrow C'
\]

with an associated nonnegative vector cost `c(u,C,C')`. The transformation may change any component of `C`, including `G`, `I`, `A`, or `L`; therefore this formalization genuinely permits the future capability game itself to change.

## 2. Configuration-compilation theorem

### Theorem 027.1

For any structural augmentation system `(mathcal C,U)` as above, define the meta-transition relation

\[
C \xrightarrow{u,c} C'
\quad\Longleftrightarrow\quad
(C,C')\in u,
\]

with edge label `(u,c(u,C,C'))`.

Then every finite structural augmentation history is exactly a path in this fixed meta-transition system, and every path in the meta-transition system is exactly an admissible structural augmentation history. Consequently, any reachability, budget-feasibility, minimum ordered augmentation cost, or branching strategy property whose semantics depend only on the sequence of configurations and labelled structural updates can be evaluated on the compiled meta-transition system without loss.

If `mathcal C` is finite, the compilation is a finite labelled graph. If `mathcal C` is countable/effectively presented, it is a countable/effectively presented transition system.

### Proof

Create one meta-state for every complete structural configuration. For every admissible application of an update `u` from `C` to `C'`, insert exactly one labelled meta-edge. Induction on history length gives a bijection between admissible structural histories and meta-paths: length zero is the identical configuration; appending one admissible update corresponds exactly to appending its meta-edge, and conversely every meta-edge was inserted from an admissible update. Edge labels preserve ordered update identity and cost, so cumulative vector-budget feasibility and ordered cost functionals are preserved. Branching is also preserved because all admissible successors of each complete configuration occur as outgoing meta-edges. QED.

## 3. Consequence for GC-II novelty

Merely saying that an augmentation 'changes the game', creates an action, deletes an information channel, or rewrites a rule does **not** evade fixed-transition-system semantics when the complete structural configuration is admitted as state. The apparent dynamic arena becomes an ordinary transition system one level up.

Therefore the following claim is rejected:

> Dynamic structural augmentation, by itself, constitutes a new GC-II semantic class not reducible to fixed-state transition/rewrite semantics.

It does not.

This does **not** make structural augmentation useless. It changes the novelty question from semantic expressibility to one of structure, succinctness, observability, accounting, or computational separation.

## 4. Prior-art collision

The collision is direct. Algebraic graph transformation already treats graphs as states and rewrite rules as transitions between graphs; graph-transformation systems generate graph transition systems. Dynamic software reconfiguration has likewise been modeled by conditional graph productions that add/delete architectural components and links. Reconfigurable timed-automata work explicitly uses graph transformation to model changing system structure.

Thus 'the topology/rules can change' is not a defensible breakthrough claim by itself.

Representative collision sources checked in this run:

- König & Stueckrath, *Well-structured graph transformation systems*, Information and Computation (2016): graph transformation systems generate transition systems whose states are graphs and whose transitions are rule applications.
- Gadducci & Heckel, *An inductive view of graph transformation* (1997): graph transformations are formal rewrite dynamics.
- Wermelinger et al., graph-transformation treatment of dynamic reconfiguration: conditional productions can introduce/remove components and architectural connections.
- Dynamic Timed Automata for Reconfigurable System Modeling and Verification (2023): dynamic structural reconfiguration modeled using double-pushout graph transformation.

No novelty claim is made for Theorem 027.1; it is a compilation/semantic boundary observation.

## 5. Edge and degeneracy checks

1. **Zero-cost rewrites.** Compilation preserves them exactly; zero-cost cycles remain zero-cost cycles.
2. **Noncommuting rewrites.** Ordered paths remain distinct, so the Audit-014 order-sensitivity result is preserved rather than erased.
3. **Rule creation/deletion.** Put the active rule set `L` inside the configuration. Two identical underlying graphs with different active rules are distinct meta-states.
4. **Interface creation/deletion.** Put `A` inside the configuration; no information is lost.
5. **Information acquisition/loss.** Put `I` inside the configuration.
6. **Budget replenishment.** Put residual/current budget in `B`; replenishing transitions are ordinary labelled meta-edges.
7. **Nondeterminism/adversarial resolution.** Preserve ownership/resolution type in the complete configuration/edge labels; compilation does not flatten branching.
8. **Infinite configuration spaces.** The theorem still gives a transition-system semantics but no finite-state algorithm follows automatically.
9. **Uncomputable update relation.** Semantic compilation exists extensionally, but effective computation may fail; no decidability claim is made.
10. **Representation blow-up.** The explicit meta-graph can be exponentially or infinitely larger than a succinct rewrite description. This is not a defect of the theorem; it identifies the strongest surviving research direction.

## 6. Stronger surviving target

The viable Paper-II target is now a **succinct structural capability-accounting separation**, not mere structural mutability.

A useful candidate must prove something such as:

- a lower bound on the minimum description/augmentation cost required to escape a capability closure when the evolving arena is represented succinctly;
- a separation between local/taskwise summaries and the minimum structural rewrite program needed for whole-envelope convertibility;
- a theorem showing that two systems have identical ordinary start-state capability summaries yet differ in a GC-specific *structural edit/translator complexity* that cannot be removed by simply expanding the state space without incurring a quantified blow-up;
- or a dual certificate for non-convertibility whose size is controlled by task-scale-error/vector-budget structure.

The key quantity should therefore price not just a path in the explicit configuration graph, but the **representation/description complexity of the admissible structural transformation mechanism** or prove a lower bound under a specified succinct model.

A provisional research object is

\[
\Omega_G^{\mathrm{struct}}(X\to Y)
=\inf_{P:\,X\Rightarrow Y}
\bigl[\operatorname{Cost}_{RIAL}(P)+\lambda\,\operatorname{Desc}(P\mid\mathcal M)\bigr],
\]

where `mathcal M` is an explicitly fixed structural rewrite/translator model and `Desc` is a representation cost. This is **OPEN** and is not claimed as novel until collision-tested against graph-edit distance, minimum-cost graph rewriting, planning, program synthesis, Kolmogorov/description complexity, dynamic networks, and succinct-game complexity.

## 7. Status delta

- Dynamic structural augmentation as a new semantic class: **FALSIFIED as novelty route / IMPORTED-KNOWN mechanism**.
- Exact compilation to a configuration transition system: **PROVED boundary theorem**.
- Finite explicit compilation when the structural configuration set is finite: **PROVED**.
- Succinct structural capability-accounting separation: **OPEN; highest-priority next target**.
- Representation-aware `Omega_G^struct`: **OPEN**.
- Breakthrough status: **NONE YET**.
