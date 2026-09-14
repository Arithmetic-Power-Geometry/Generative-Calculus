# GC-II Audit 146 — Dynamic Translator Shortest-Path No-Go

## Question

Does a translator become genuinely beyond static communication complexity merely because its actions consume resources, create/destroy interfaces, or otherwise change future admissibility while translation is occurring?

## Finite augmented-state model

Let the fully observed operational translator state be

\[
q=(x,r,i,\ell,\sigma)\in Q,
\]

where the coordinates may include physical/resource state, acquired information, enabled interfaces/actions, rule state, and any finite translator memory. At state \(q\), only actions in \(A(q)\) are admissible. Executing \(a\in A(q)\) produces

\[
q' = T(q,a)
\]

and incurs nonnegative additive cost \(c(q,a)\ge 0\). Let \(G\subseteq Q\) be the set of states in which the required global capability has been correctly realized.

The exact minimum dynamic translation cost is

\[
C^*(q_0)=\inf_{q_0\to q_1\to\cdots\to q_k\in G}
\sum_{t=0}^{k-1} c(q_t,a_t).
\]

## Theorem candidate tested

**Finite Dynamic Translator Compilation Theorem.** Under the assumptions above, construct the weighted directed graph

\[
\mathcal G=(Q,E,w),
\]

with an edge \(q\to T(q,a)\) of weight \(c(q,a)\) for every admissible pair \((q,a)\). Then

\[
\boxed{C^*(q_0)=d_{\mathcal G}(q_0,G)}.
\]

This is immediate in both directions: every admissible translator execution is a graph path with the same accumulated cost, and every graph path is an admissible execution by construction. With nonnegative costs, if a goal is reachable then an optimal path has a simple representative after removal of nonnegative cycles.

Therefore resource depletion, interface creation/destruction, and rule-dependent action availability do not by themselves escape ordinary weighted reachability once those effects are represented in the finite operational state.

## Exhaustive check

`experiments/gc2_audit146_dynamic_translator_shortest_path.py` enumerates every deterministic system with:

- 3 operational states;
- 2 state-dependent actions;
- each state-action pair either disabled or mapped to one of 3 successor states;
- edge cost in \(\{0,1\}\);
- start state 0 and goal state 2.

There are

\[
(1+3\times2)^{3\times2}=7^6=117649
\]

systems. Exact graph optimization was compared with exhaustive simple-sequence search. Frozen result:

- systems checked: **117,649**;
- reachable: **76,440**;
- unreachable: **41,209**;
- zero-cost reachable: **38,220**;
- minimum cost 1: **34,447**;
- minimum cost 2: **3,773**;
- mismatches: **0**.

## Edge and degenerate cases

- Empty admissible action sets become graph dead ends.
- Interface destruction is just deletion of outgoing actions in the reached state.
- Interface creation is just appearance of outgoing actions in the reached state.
- Resource exhaustion is represented by resource coordinates of \(q\) and corresponding disabled transitions.
- Zero-cost cycles do not improve the optimum; a simple optimal representative exists.
- Positive cycles cannot improve an additive nonnegative optimum.
- Negative costs are deliberately excluded; allowing them changes the optimization problem and can create negative-cycle pathologies, but does not establish a specifically GC-II phenomenon.
- Partial observability or stochastic transitions require belief-state/POMDP or stochastic-shortest-path machinery rather than this deterministic theorem.
- Infinite or noncomputable state spaces are outside this finite no-go.

## Prior-art collision

The reduction is standard state augmentation plus weighted reachability/shortest path. Finite-state transducers are represented by labeled transition graphs; weighted finite-state transducers attach transition weights. State-dependent action sets and accumulated-cost optimization are standard in Markov decision processes and stochastic shortest-path formulations. Thus the mechanism cannot be claimed as a new GC-II theorem merely by describing the state components as resources, interfaces, or rules.

Useful collision sources checked in this run:

- finite-state transducer / weighted finite-state transducer formalism;
- Markov decision processes with state-dependent actions;
- stochastic shortest path and dynamic programming;
- weighted reachability.

## Status ledger

- finite dynamic translator compilation: **PROVED**;
- exhaustive finite regression: **PASS**;
- closure-changing translator as novelty by itself: **FALSIFIED**;
- weighted reachability / state augmentation mechanism: **IMPORTED/KNOWN**;
- obstruction surviving finite fully observed state augmentation and ordinary weighted reachability: **OPEN**.

## Consequence for the breakthrough search

The next viable candidate must violate at least one premise in a scientifically substantive way rather than merely hiding state. Promising gates are: partial observability with task-relative information structure, distributed ownership of state with communication restrictions, nonlocal consistency/gluing constraints not capturable by independent local state, or a lower bound on the size/complexity of any exact augmented-state compiler. Any such candidate must still be collision-tested against POMDPs, communication complexity, distributed synthesis, CSP/database decomposability, automata minimization, and succinct-state planning.
