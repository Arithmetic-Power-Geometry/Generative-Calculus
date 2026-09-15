# GC-II Audit 154 — process-equivalence no-go for typed path burden

## Candidate attacked
Audit 153 proposed a stronger gate: compare two systems after quotienting by their full reachable operational transition structure (or a defensible process equivalence), yet obtain different minimum typed capability-generation burden.

## Model
Let an operational system be a rooted labelled transition system

`M=(S,s0,A,->,G,c)`

where `G` is the goal/capability set and every transition `e=(s,a,s')` has a typed nonnegative cost

`c(e) in R^4_{>=0}`

with coordinates `(R,I,A,L)`. For a finite path `p=e1...ek`, let its accumulated typed burden be

`C(p)=sum_i c(e_i)`.

Let the attainable capability-cost set be

`K_M = { C(p) : p starts at s0 and ends in G }`,

and let `PF(M)=Min(K_M)` denote its coordinatewise Pareto-minimal frontier. Any scalar minimum derived from a fixed monotone scalarization `phi` is `V_phi(M)=inf_{v in K_M} phi(v)`.

## Theorem (cost-labelled process-equivalence invariance)
Suppose rooted systems M and N are related by a goal-preserving strong bisimulation B such that matched transitions have the same action label and the same typed cost vector. Then

`K_M = K_N`, hence `PF(M)=PF(N)`,

and therefore `V_phi(M)=V_phi(N)` for every scalarization phi for which the infimum is defined.

### Proof
Take any finite goal-reaching path in M. Starting from the related roots, repeatedly apply the forward bisimulation clause. At every step N has a matched transition with identical action label and identical typed cost, and successor states remain related. Goal preservation makes the matched terminal state a goal. Thus every vector in `K_M` belongs to `K_N`. Apply the symmetric bisimulation clause for the reverse inclusion. Equality of Pareto frontiers and all functions depending only on the attainable cost set follows immediately. QED.

**Status: PROVED.**

## Consequence for the Audit-153 gate
There are only two cases.

1. Process equivalence ignores some typed costs. Then bisimilar/unweighted-equivalent systems can trivially have different typed realization burdens, but the distinction is already a quantitative annotation omitted by the chosen equivalence.
2. Process equivalence preserves the typed costs relevant to the proposed burden. Then a different minimum path-based typed burden is impossible by the theorem.

Therefore the proposed gate cannot itself generate a new representation-invariant `Omega_G` when `Omega_G` is a function only of goal-reaching path costs.

## Edge cases and checks
- Zero-length goal path: preserved because roots are goal-equivalent; contributes zero to both attainable sets.
- Deadlock/unreachable goal: bisimulation plus goal preservation preserves absence of finite goal-reaching paths.
- Zero-cost transitions/cycles: harmless; finite path matching preserves accumulated vectors exactly.
- Nondeterminism: handled because bisimulation matches every outgoing transition in both directions.
- Multiple matched transitions: existence is sufficient for inclusion of attainable vectors; symmetry gives equality.
- Composition: any composition operator for which the chosen cost-preserving bisimulation is a congruence preserves the conclusion componentwise.
- Nonadditive/history-dependent burden: not covered unless history is augmented into state and the burden update is included in the matched transition annotation. This is an explicit boundary, not a claim of impossibility there.

## Prior-art collision
This is a direct specialization of quantitative/weighted behavioural equivalence. Weighted transition systems and cost-preserving bisimulations are designed precisely so equivalent processes preserve quantitative transition behaviour. Cost-preserving bisimulations for probabilistic automata additionally establish compositional quantitative abstractions. Therefore this invariance is not claimed as novel GC mathematics.

## Ledger
- Cost-labelled bisimulation preserves the complete attainable typed path-cost set: **PROVED**.
- Equality of Pareto capability frontiers under cost-labelled bisimulation: **PROVED**.
- Different path-based typed burden after full cost-preserving process equivalence: **FALSIFIED**.
- Difference after an equivalence that deliberately erases typed costs: **IMPORTED/KNOWN / insufficient novelty**.
- Weighted/cost-preserving behavioural equivalence mechanism: **IMPORTED/KNOWN**.
- History-dependent or endogenous burden not reducible to a fixed transition annotation: **OPEN**, subject to augmented-state compilation attacks.

## Revised breakthrough gate
Do not seek a path-cost residual after an equivalence that already preserves those costs. A viable `Omega_G` must instead be defined operationally before choosing an equivalence, then pass an invariance test under semantics-preserving refinements/compilations. The next candidate should target the minimum *change of operational model* required to make an unreachable task reachable under a restricted compiler class, and prove that this intervention distance is not reducible to ordinary weighted reachability, edit distance on transition systems, controller synthesis, or resource-theoretic conversion cost.