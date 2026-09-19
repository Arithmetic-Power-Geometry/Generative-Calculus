# GC-II Audit 245 — Static quotient does not preserve sequential capability

## Status

**Decisive falsification / boundary result.** Audit 244's exact-clone quotient is sound for the static translator repair objective, but it is not in general a congruence for the sequential operational closure of Audits 240–243.

## Setup

A static translator state is `X=(W,p,g,M,L)`. Audit 244 identifies worlds by

`w ~0 w'  iff  (p(w),g(w),L(w))=(p(w'),g(w'),L(w'))`.

This preserves the current exact-translator feasibility predicate and makes the quotient repair gap replication invariant.

Sequential GC-II states additionally carry admissible typed operations with enabling conditions, costs, and transitions. A quotient used inside sequential closure must therefore commute with those operations (or, more generally, preserve all capability-relevant future traces and costs).

## Counterexample

Let `M={0,1}` and worlds `u,v,c` satisfy initially

- `p(u)=p(v)=p(c)=z`;
- `g(u)=g(v)=0`, `g(c)=1`;
- `L(u)=L(v)=L(c)={0}`.

Thus `u ~0 v` under Audit 244.

Introduce one unit-cost operation `o` whose only effect is

`L(u) <- {0,1}`,

while `L(v)` and `L(c)` remain `{0}`.

After executing `o`, the full system is still infeasible. If message 0 is assigned to decision 1 so that `c` is covered, world `v` has no decision-0 message. If message 0 is assigned to decision 0, `c` is uncovered. Hence this operation does not escape closure into exact capability.

But if `u` and `v` are first collapsed by the Audit-244 static quotient and `u` is retained as representative, executing the induced representative-level effect gives the quotient decision-0 world list `{0,1}` while `c` has `{0}`. The quotient is then feasible by assigning message 1 to decision 0 and message 0 to decision 1.

Therefore quotienting and operational evolution need not commute:

`Q0(T_o(X)) != Tbar_o(Q0(X))`

for the naive representative-induced transition, and static equivalence can identify worlds with different operational futures.

## Consequence

The Audit-244 quotient is a **static observational quotient**, not an operational quotient for sequential GC-II. Consequently a sequential Generative Novelty Gap cannot in general be defined by first quotienting only on `(p,g,L)` and then running budgeted closure.

Any sound sequential quotient relation `~op` must at minimum be stable under every admissible capability-relevant operation. A sufficient deterministic condition is:

1. equivalent states/world-configurations agree on the current capability observation;
2. they agree on enabled operation labels and costs; and
3. for every enabled operation `o`, their successors remain equivalent.

Under these conditions the quotient is a cost-preserving bisimulation/congruence, and minimum cost to a union of equivalence classes is preserved.

## Novelty boundary

The required repair is not claimed as new generic mathematics. Behavioral equivalence, bisimulation, lumpability, automata minimization, and exact abstractions in planning already formalize the principle that states may be merged only when relevant futures are preserved. The GC-II contribution sought after this audit must therefore lie in a more specific operational equivalence induced by generative capability semantics, not in renaming bisimulation.

## Ledger

- Audit-244 `(p,g,L)` quotient preserves current static translator feasibility: **PROVED / retained**.
- Audit-244 quotient preserves sequential capability under arbitrary state-dependent operations: **FALSIFIED**.
- Exact static clones may have different capability-relevant futures: **PROVED by counterexample**.
- Transition-stable cost-preserving bisimulation preserves minimum goal-reaching cost: **IMPORTED/KNOWN; applicable**.
- A canonical GC-specific operational quotient weaker than full transition-system bisimulation but complete for generative capability: **OPEN**.
- Replication-invariant sequential `Omega_G` should quotient only by a capability-relevant operational congruence, not by current `(p,g,L)` signatures alone: **CONDITIONAL design requirement**.

## Next attack

Define finite-horizon operational signatures recursively and collision-test whether the coarsest capability-preserving congruence can be computed by partition refinement. Then ask whether GC's typed `R/I/A/L` structure yields a smaller sufficient signature or a translator lower bound not already inherited from standard bisimulation/minimization theory.
