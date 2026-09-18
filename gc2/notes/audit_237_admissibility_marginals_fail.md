# GC-II Audit 237 — Admissibility marginals do not determine capability

Status: **PROVED / decisive falsification of marginal-only accounting**

## Question

Audit 236 showed that exact translation with per-world admissible message/action lists is equivalent to list coloring of the decision-conflict graph. Could a compressed capability account retain only marginal summaries of the admissibility incidence relation, rather than the full coupling?

## Counterexample

Take one projection fiber with three worlds `w0,w1,w2`, required decisions

`g = (0,1,0)`

and message alphabet `{0,1}`. Thus `w1` conflicts with both `w0` and `w2`, while `w0,w2` do not conflict.

System F (infeasible):

- `L(w0)={0}`
- `L(w1)={0}`
- `L(w2)={1}`

System T (feasible):

- `L(w0)={0}`
- `L(w1)={1}`
- `L(w2)={0}`

Both systems have exactly the same:

- number of worlds: 3;
- projection map and required-decision multiset;
- message alphabet size: 2;
- number of admissibility incidences: 3;
- sorted world-list-size sequence: `(1,1,1)`;
- sorted message-incidence-degree sequence: `(1,2)`;
- fiber ambiguity: 2.

Yet F is infeasible because the conflicting pair `(w0,w1)` is forced to the same message 0. T is feasible: decision-0 worlds use 0 and decision-1 world uses 1.

Therefore even preserving both sides' degree sequences of the admissibility bipartite graph does not preserve exact capability.

## Consequence

Any universal GC-II capability account that is a function only of cardinal increments, list-size marginals, action/message popularity marginals, and fiber ambiguity is incomplete. The missing information is the **joint alignment/coupling** between admissibility incidence and decision-conflict structure.

In particular, replacing the full incidence relation `E_L` by its row/column marginals loses capability-relevant information.

This is stronger than the count-only obstruction: even matched first-order marginals can conceal opposite operational feasibility.

## Novelty boundary

The counterexample is elementary combinatorics and is not claimed as a new list-coloring theorem. Its role is a GC-II model-selection falsification: it rules out a broad family of compressed accounting variables before a capability bound is proposed.

## Ledger

- Same cardinal accounting with opposite translator feasibility: **PROVED**.
- Same row and column admissibility degree sequences with opposite feasibility: **PROVED**.
- Marginal-only admissibility summary as complete GC capability invariant: **FALSIFIED**.
- Full joint incidence as sufficient together with `(p,g)` in the finite deterministic one-way translator model: **PROVED by Audit 236 / imported list-coloring mechanism**.
- A smaller GC-specific sufficient statistic preserving the relevant incidence/conflict coupling: **OPEN**.

## Next target

Search for a structured statistic that preserves the interaction between admissibility incidence and conflict fibers—e.g. neighborhood types, Hall-style obstructions in restricted generated families, or a width parameter forced by typed GC composition—while collision-checking against list coloring, matching/SDR theory, CSP width, database joins, contextuality/marginal problems, and communication complexity.
