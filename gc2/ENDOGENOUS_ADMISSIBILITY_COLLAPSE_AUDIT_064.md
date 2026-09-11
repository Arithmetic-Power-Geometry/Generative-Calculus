# GC-II Audit 064 — Endogenous Admissibility Collapse

Status date: 2026-09-11
Branch: `gc2-capability-accounting-lab`
Parent audit: 063

## Candidate attacked

Audit 063 proposed endogenous admissibility change as a possible escape from fixed-protocol resource tradeoffs: a system pays typed cost to install an interface/action/rule/model/evaluator, thereby changing which transformations are admissible later.

## Formal model

Let X be a finite operational state set and let L be a finite set of admissibility structures. For each l in L let A_l(x) be the actions admissible at x and let

    T_l(x,a) subseteq X

be the resulting transition relation. Installation/meta-actions u may change both ordinary state and admissibility structure:

    M((x,l),u) subseteq X x L,

with a typed charged cost

    c(u) = (Delta R, Delta I, Delta A, Delta L).

Ordinary actions may also carry typed cost. Tasks/evaluators are predicates or loss functions on finite histories of observable state/action/rule-index events.

Define Omega_G(q | x0,l0) as the Pareto-minimal total typed installation/execution cost among histories realizing q to its declared error tolerance.

## Finite Meta-State Collapse Theorem

**Theorem (PROVED).** Every finite explicit endogenous-admissibility system of the form above is exactly behaviorally representable as an ordinary fixed-action labelled transition system on augmented state

    Z = X x L.

Construct a fixed global action alphabet

    A* = U union (union_l A_l),

and define a fixed transition relation on Z. For ordinary action a,

    (x,l) --a--> (x',l)

iff a is in A_l(x) and x' is in T_l(x,a). For installation/meta-action u,

    (x,l) --u--> (x',l')

iff (x',l') is in M((x,l),u).

Attach exactly the original typed event cost to each corresponding transition. Preserve the original observable labels/evaluator on histories.

Then there is a cost-preserving bijection between admissible histories of the endogenous system and histories of the augmented fixed-transition system from (x0,l0). Consequently:

1. task realizability is identical;
2. error/loss on corresponding histories is identical;
3. every typed R,I,A,L path cost is identical;
4. the full Pareto capability/repair frontier is identical;
5. reversibility properties defined on histories are identical;
6. composition can be represented by the ordinary product/interaction construction once all rule indices are included in state.

**Proof.** Induct on history length. The base history is the same augmented initial state. For the induction step, an endogenous ordinary action is enabled exactly when the constructed fixed relation contains its same-l transition; an endogenous installation is enabled exactly when the fixed relation contains the corresponding cross-l transition. Conversely every constructed transition was introduced from one and only one admissible endogenous transition class. Labels and typed costs are copied transitionwise, so concatenation preserves traces, cumulative typed costs and evaluator values. Pareto minimization over identical cost-labelled realization histories therefore yields identical frontiers. QED.

## No-Free-Capability corollary

Within this finite explicit class, changing the future conversion law does not evade ordinary capability accounting. Any new reachable capability must be witnessed by a path in augmented state space containing either a charged installation transition or a declared-free transition. If an apparent capability appears without either, the model omitted an endowment/transition.

Status: PROVED for the declared finite explicit class. This is an accounting lemma, not a novelty claim.

## Edge/degenerate cases

- L singleton: reduces immediately to fixed-law reachability.
- Zero-cost installation: valid but the new rule is then a declared free transition; it cannot support a no-free theorem without an additional physical assumption.
- Cyclic rule changes: represented by cycles in Z with exactly preserved costs.
- Rule deletion/rollback: represented by cross-l transitions in the opposite direction; reversibility is not assumed.
- Stochastic transitions: the same construction works with a finite controlled Markov kernel on X x L; this is an MDP/meta-MDP representation rather than a deterministic LTS.
- Partial observability: hiding l yields a POMDP-style observation map; it does not prevent the underlying augmented-state representation.
- Nonadditive typed costs: history-dependent costs can be handled by augmenting state with the finite cost-relevant memory. If that memory is unbounded, the finite theorem no longer applies.
- Dimension audit: R,I,A,L remain separate typed coordinates. The theorem never adds unlike units.

## Prior-art collision

This collapse is structurally aligned with established metareasoning/meta-MDP formulations: computational/deliberation actions are treated as actions whose costs and consequences affect later object-level decisions. Russell-Wefald style metareasoning and later meta-MDP/meta-BAMDP formulations already optimize over such meta-actions. Self-modifying programs likewise treat executable descriptions/configurations as mutable machine state. Therefore 'pay to change what actions/rules are available later' is not sufficient novelty when the changed rule is finitely and explicitly state-encodable.

## Classification

- Endogenous admissibility as a useful GC modelling layer: VALID.
- Finite explicit meta-state collapse theorem: PROVED.
- No-free accounting corollary in this class: PROVED but elementary/structural.
- Endogenous rule installation alone as Omega_G breakthrough: FALSIFIED.
- Claim that changing a conversion law necessarily escapes MDP/reachability/resource models: FALSIFIED.
- Breakthrough-level generative invariant: OPEN.

## Stronger surviving target — representation-independent law-generation cost

The only surviving direction is not merely changing among an explicit finite family L. GC-II would need a theorem about *generating a previously unenumerated admissibility law* whose operational installation cost cannot be erased by moving the law description into augmented state.

A candidate must distinguish extensional law behavior from its description and charge only physically observable acquisition/installation events. The target quantity is therefore a representation-invariant lower bound on the cost of expanding the realizable law class, not the byte length of a program:

    Gamma_G(Q | L0) = inf typed cost of an admissible physical history that installs some law l with Q subseteq C_G(l),

where equivalent implementations of the same operational law must receive the same bound.

Immediate kill tests for Audit 065:

1. If Gamma_G is merely shortest program/description length, it collides with Kolmogorov/algorithmic information and is generally uncomputable.
2. If it is sample/query cost for identifying an unknown law, it collides with learning theory, active learning, experiment design and system identification.
3. If it is synthesis/search cost for constructing a law, it collides with program synthesis and computational complexity.
4. If it is communication required to acquire a remote law, it collapses to information/communication complexity.
5. If it is thermodynamic work to write/configure a controller, it must survive Landauer-style and physical-computation accounting.
6. If the law can be supplied as free advice/oracle, no positive universal no-free bound is possible.

Thus the next candidate must couple **operational novelty of the installed law** to **physically conserved acquisition/installation evidence** while remaining invariant under equivalent encodings. No such theorem is claimed here.
