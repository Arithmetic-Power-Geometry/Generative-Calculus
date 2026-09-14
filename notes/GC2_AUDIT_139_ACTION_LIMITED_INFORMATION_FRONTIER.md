# GC-II Audit 139 — Action-Limited Information Frontier

## Question
Can merely adding an action/query budget to persistent memory and fresh side-information force a genuinely nonlinear GC-II capability-accounting law?

## Exact finite theorem
Let an exact capability/continuation task have `N` distinguishable classes. Suppose an agent has:

- `S` persistent internal states;
- `Q` possible fresh side-information transcripts available independently of its actions;
- at most `A` adaptive actions/queries; and
- each action has at most `b` observable outcomes.

Then the complete observation record can take at most

\[
S Q b^A
\]

distinct values. Therefore exact discrimination requires

\[
\boxed{N\le S Q b^A}.
\]

In bits,

\[
\boxed{\log_2 N\le \log_2 S+\log_2 Q+A\log_2 b}.
\]

### Proof
A depth-`A` adaptive decision tree with outcome branching bounded by `b` has at most `b^A` complete outcome transcripts. Pairing a transcript with one of `S` persistent states and one of `Q` independent side-information values yields at most `S Q b^A` distinguishable records. Exact discrimination among `N` continuation classes requires an injective assignment into those records, proving necessity.

The bound is tight as a capacity statement whenever all record combinations are realizable: index classes by mixed-radix tuples `(s,q,r_1,...,r_A)` with `s<S`, `q<Q`, and `r_i<b`.

## Consequence for GC-II
The bare combination of memory, side-information, and an action budget does **not** force a positive nonlinear interaction correction. Any proposed universal inequality stricter than

\[
\Omega_{\rm exact}\le M+I+A\log_2 b
\]

by subtracting an everywhere-positive interaction penalty is falsified by tight realizations of the product frontier.

Nonlinear terms remain possible only after adding independently specified structure that removes some transcript combinations: locality, causal constraints, restricted query families, noise, privacy, bounded communication topology, irreversible state updates, energetic charges, or other operational constraints.

## Regression
`experiments/audit139_action_limited_transcript_frontier.py` probes the exact boundary for
`S,Q=1..16`, `b=1..8`, `A=0..6`, including `b=1` and `A=0` degeneracies.

Frozen result:

- checks: 57,287
- feasible boundary probes: 42,951
- infeasible probes: 14,336
- exact tight cases: 14,336
- logarithmic/product criterion violations: 0
- largest tested capacity: 67,108,864

## Novelty / collision status
**IMPORTED/KNOWN mechanism.** This is standard decision-tree/query-complexity counting: bounded-answer queries generate a bounded number of transcripts, and exact-learning/query-complexity theory already derives lower bounds from the number and structure of possible answers. It must not be claimed as new GC mathematics.

## Ledger
- Product transcript frontier: **PROVED**.
- Logarithmic accounting form: **PROVED**.
- Tightness as a capacity statement: **PROVED**.
- Exact finite regression: **PASS**.
- Mandatory positive nonlinear memory–information–action penalty in the bare model: **FALSIFIED**.
- Underlying decision-tree/query-counting mechanism: **IMPORTED/KNOWN**.
- GC-specific nonlinear coupling under independently measurable structural restrictions: **OPEN**.

## Next gate
A viable GC-II breakthrough now requires a structural obstruction that makes only a strict subset of the nominal `S Q b^A` records operationally realizable, together with a quantitative deficit that cannot be reduced to standard query, communication, streaming, or automata complexity.
