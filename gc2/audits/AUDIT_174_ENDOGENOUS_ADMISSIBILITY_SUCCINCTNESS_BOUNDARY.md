# GC-II Audit 174 — Endogenous Admissibility: Succinctness/Reconfiguration Boundary

Status date: 2026-09-16
Branch scope: `gc2-capability-accounting-lab` only. GC-I/main unchanged.

## Objective

Attack Audit 173's surviving target: whether transformations that change the future admissible transformation set can force a growing compilation complexity that escapes fixed finite resource-game models.

## Formal endogenous-admissibility model

Let X be the externally visible capability state space and let E={e_1,...,e_n} be primitive actions. An endogenous admissibility configuration is a rule state c in C_n. At configuration c, only actions in A(c) subseteq E are admissible. Executing e updates both the visible state and the rule state:

    (x,c) --e--> (T_e(x,c), U_e(c)).

A static compilation is a transition system whose state contains enough information to reproduce exactly, after every history, (i) the visible behavior and (ii) which future actions are admissible.

## Exact compilation theorem

For every finite C_n, exact endogenous admissibility compiles into an ordinary finite transition system on X x C_n. Therefore finite rule change is not an expressiveness escape by itself.

Status: PROVED, elementary.

## Exponential family

Take n independently switchable action permissions. Let C_n={0,1}^n, where bit i records whether action a_i is currently enabled. Include toggle_i actions that flip bit i. From any configuration c, a probe_i action succeeds iff c_i=1 and otherwise is inadmissible.

All 2^n configurations are pairwise future-distinguishable: if c != c', choose an index i on which they differ; probe_i distinguishes them immediately. Hence every exact deterministic static compilation preserving admissibility requires at least 2^n distinct compiled states.

The endogenous description itself needs only n permission bits plus O(n) toggle/probe schemas. Thus a natural representation can be exponentially more succinct than its explicit finite-state unfolding.

Status: PROVED.

## Why this is not yet a GC-II breakthrough

The lower bound is a standard distinguishability/state-complexity argument. It is the same mechanism behind powerset-style determinization and many succinct-vs-explicit representation gaps. Reconfigurable transition-system formalisms also explicitly model changing transition structure and can be unfolded into behavior-preserving static systems when the reachable configuration set is finite. Dynamic timed automata, for example, are transformed to semantically equivalent timed automata by unfolding reachable configurations. Dynamic epistemic/action-schema formalisms likewise exhibit exponential succinctness relative to explicit event/action models.

Therefore:

    endogenous rule mutation + exponential static unfolding

is insufficient for GC-II novelty.

## Stronger no-go boundary

Suppose an endogenous-admissibility formalism has:

1. a finite reachable rule-configuration set C;
2. Markov sufficiency: future admissibility and updates depend only on current (x,c), current resources, and current action/environment input;
3. finite/effectively represented resource state after any required abstraction.

Then exact behavior is representable by the product state containing c and the other sufficient variables. Any lower bound on the number of explicit compiled states is consequently a representation/state-complexity lower bound, not by itself a new capability invariant.

This does not say the compilation is computationally cheap. C may be exponentially or worse larger than a succinct rule description. It says only that the proposed novelty must be more than the existence of that blow-up.

Status: PROVED under assumptions 1-3 / mechanism IMPORTED-KNOWN.

## Dimension/domain and edge-case checks

- n=0: one rule configuration; lower bound 1.
- n=1: two configurations, distinguished by probe_1.
- If probes are not admissible observations, some bit patterns may be observationally equivalent and the 2^n lower bound fails; quotient by future distinguishability is required.
- If toggles cannot reach all masks, replace 2^n by the number of reachable pairwise distinguishable masks.
- If rule configurations are infinite, the finite product theorem no longer yields a finite compiler; pushdown, counter/VASS, Petri-net, symbolic, graph-transformation, or other infinite-state models become the collision boundary.
- If rule updates depend on the full unbounded history but admit a finite sufficient statistic, the statistic restores finite compilation.
- If no finite sufficient statistic exists, this is ordinary infinite-state/nonregular behavior unless the GC operational restrictions produce an additional theorem not captured by the known model.
- Adding R/I/A/L costs to transitions does not alter the distinguishability proof; it may add energy/resource-game structure to the product.

## Composition behavior

Independent permission masks compose by Cartesian product, so explicit configuration counts multiply and log-state requirements add. Shared permissions/coupled rule updates can reduce or increase reachable configuration counts, but no universal additive scalar follows. The correct exact quantity is the number of reachable future-distinguishability classes of the augmented dynamics.

## Prior-art collision ledger

- finite-state compilation/minimization: automata/state complexity — IMPORTED/KNOWN;
- exponential explicit-state blow-up from succinct descriptions: descriptional/succinctness complexity — IMPORTED/KNOWN;
- changing transition structures: reconfigurable/dynamic transition systems — IMPORTED/KNOWN;
- action/rule schemas vs explicit events: dynamic epistemic/planning succinctness — IMPORTED/KNOWN;
- infinite rule state: pushdown/VASS/Petri nets/graph transformation/symbolic transition systems — must be treated as known boundaries before novelty claims;
- distributed endogenous rules: communication/distributed synthesis — collision check required.

## Consequence for GC-II

Audit 173's candidate, in its natural finite form, is FALSIFIED as an independent breakthrough. A growing static compilation requirement can be rigorously proved, but without additional GC structure it is classical succinctness/state complexity.

The surviving target must compare two systems that are equivalent under the relevant known sufficient-state/automata/resource representations yet differ under a GC-specific operational requirement, or establish a theorem tying GC's four-way budget/interface structure to a lower bound that is not merely the cardinality of a hidden configuration set.

A sharper candidate for Audit 175 is **distributed closure translation**: split the information required for admissibility across components so that no component has the global rule state, and measure the minimum communication needed to implement an exact local-to-global closure translator. The theorem target should connect GC-I proper-projection irreducibility to a communication lower bound only when projection fibers are pairwise separated by admissible future tasks. The immediate collision gate is deterministic/randomized communication complexity, distributed synthesis, CSP/database join width, and marginal/contextuality reconstruction. If the lower bound is simply equality/disjointness/indexing communication complexity under a renaming, mark it IMPORTED rather than novel.

## Status ledger

| Candidate | Status | Reason |
|---|---|---|
| Finite endogenous admissibility compiles into augmented state | PROVED | direct product construction |
| n independent permissions force 2^n explicit compiled states | PROVED | pairwise future distinguishability |
| Exponential endogenous-vs-static succinctness | PROVED / IMPORTED-KNOWN mechanism | classical descriptional complexity boundary |
| Endogenous admissibility blow-up as independent GC-II novelty | FALSIFIED in finite Markov-sufficient setting | reconfiguration/succinctness collision |
| Infinite/nonuniform endogenous rule state | OPEN but novelty unestablished | collides with infinite-state/symbolic models |
| Distributed local-to-global closure translator lower bound | OPEN | next high-value collision test |