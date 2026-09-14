# GC-II Audit 136 — Unbounded-memory compilation lower bound

## Target
Attack the post-Audit-135 escape gate: can every task/rule/history-dependent capability system be compiled into a finite augmented operational state without loss of exact future admissibility?

## Operational witness
Let the external action alphabet be `{0,1}` and let the terminal capability `ACCEPT` be available exactly after histories in

\[
L=\{0^n1^n:n\ge 0\}.
\]

The projected physical state may be a singleton; all relevant structure is in history-dependent future admissibility.

For histories `u,v`, define exact future equivalence

\[
u\equiv_L v \iff \forall z\in\{0,1\}^*,\; uz\in L \Leftrightarrow vz\in L.
\]

Any exact augmented-state compiler whose state alone determines all future capability/admissibility answers must map future-equivalent histories to the same compiled state and must map future-distinguishable histories to different compiled states.

## Theorem — No finite exact compiler for the witness
**Status: PROVED.**

The histories

\[
\epsilon,0,00,000,\ldots
\]

are pairwise future-distinguishable. For `i<j`, choose continuation `z=1^i`. Then

\[
0^i1^i\in L,
\qquad
0^j1^i\notin L.
\]

Therefore all prefixes `0^i` belong to distinct future-equivalence classes. Hence there are infinitely many exact continuation classes, so any state representation preserving future capability exactly requires infinitely many states.

Equivalently, for every finite `K`, choosing prefixes `0^0,...,0^K` forces at least

\[
K+1
\]

compiled states. Thus there is no horizon-independent finite augmented-state compiler for this operational family.

## Quantitative finite-horizon lower bound
Restrict attention to the witness set of prefixes `0^0,...,0^K`. Every pair is distinguished by one of the continuations above, so every exact compiler on this finite witness set requires at least `K+1` states, i.e. at least

\[
\lceil \log_2(K+1)\rceil
\]

bits of state label if fixed-length binary state identifiers are used.

This is a lower bound on exact continuation-sufficient memory, not on physical thermodynamic memory cost, information acquisition, or computational time.

## Exact regression
`experiments/audit136_unbounded_memory_compilation_lower_bound.py` directly checks every pair of prefixes for every `K=1,...,128` using the explicit distinguishing continuation `1^i`.

Frozen result:

- horizons checked: **128**;
- pairwise distinguishability checks: **357,760**;
- failures: **0**;
- largest checked exact state lower bound: **129 states**.

The finite regression is not the proof; the unbounded theorem follows analytically from the pairwise-distinguishable infinite prefix family.

## What this falsifies
The following universal claim is false:

> Every continuation-relevant task, rule, interface, budget, or history dependence can be absorbed into a finite augmented operational state while preserving exact future capability.

Audit 135 remains correct for finite/task-tagged reifiable state. Audit 122 remains correct for finite-memory path dependence. Audit 136 identifies the boundary: exact compilation is finite only when the induced future-equivalence relation has finite index.

## Prior-art collision gate
The mathematical core is the classical Myhill–Nerode future-equivalence principle: the minimal number of deterministic states needed for exact language recognition equals the number of continuation-equivalence classes; infinitely many such classes imply non-regularity. The witness language `{0^n1^n}` is a standard nonregular example.

Therefore:

- the existence of an unbounded-memory obstruction is **not** new GC mathematics;
- the exact lower bound mechanism is **IMPORTED/KNOWN** from automata/state-complexity theory;
- GC-II may use this only as a boundary theorem unless it derives a new capability-accounting consequence that cannot be restated as minimal automaton/predictive-state/communication/information complexity.

Collision classes to check next: Myhill–Nerode and syntactic congruence; predictive-state representations; computational mechanics causal states; POMDP/belief-state sufficiency; streaming/state-complexity lower bounds; communication complexity; process/resource theories with unbounded classical memory.

## Status ledger
- Finite augmented-state compilation for every history-dependent operational system: **FALSIFIED**.
- Infinite future-equivalence index of the witness: **PROVED**.
- `K+1` exact-state lower bound on prefixes through `0^K`: **PROVED**.
- 128-horizon / 357,760-pair regression: **NUMERICALLY SUPPORTED (exact finite regression)**.
- Myhill–Nerode mechanism: **IMPORTED/KNOWN**.
- Unbounded memory as standalone GC-II novelty: **FALSIFIED**.
- GC-specific quantitative capability law built from minimal continuation-sufficient memory: **OPEN**.

## Surviving breakthrough gate
The next candidate cannot merely be “history needs memory.” It must couple the minimum continuation-sufficient representation to GC's typed operational closure in a way that yields a new measurable theorem—for example a bound connecting capability novelty/escape to jointly constrained memory, action/interface access, and resource budgets—and must survive reduction to automata state complexity, predictive-state rank, communication complexity, and algorithmic/information complexity.
