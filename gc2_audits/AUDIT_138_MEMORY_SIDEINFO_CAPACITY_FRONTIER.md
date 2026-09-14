# GC-II Audit 138 — Memory × Side-Information Capacity Frontier

## Question

After Audit 137 forced persistent continuation memory into the accounting variables, can exact continuation capability require an additional *universally positive nonlinear coupling penalty* between persistent memory and newly acquired information?

## Operational setup

Let a finite exact capability discrimination problem have `N` continuation-equivalence classes. A controller retains one of `S` persistent internal states and receives one of `Q` possible fresh side-information transcripts before the final decision. No hidden information is permitted outside this pair.

The terminal decision therefore has access to at most `S Q` distinct `(memory state, transcript)` pairs.

Define continuation complexity in bits

\[
\Omega_{\mathrm{cont}}=\log_2 N,
\]

persistent memory capacity

\[
M=\log_2 S,
\]

and fresh side-information capacity

\[
I=\log_2 Q.
\]

## Theorem — Exact product frontier

An injective exact representation of all `N` continuation classes by `(memory, side-information)` pairs exists **iff**

\[
\boxed{N\le SQ}.
\]

Equivalently,

\[
\boxed{\Omega_{\mathrm{cont}}\le M+I}.
\]

### Proof

Necessity: there are only `S Q` available ordered pairs, so exact discrimination of `N` classes requires `N <= S Q` by the pigeonhole principle.

Sufficiency: label the classes `c=0,...,N-1`. If `N <= S Q`, map

\[
c\mapsto \left(\left\lfloor c/Q\right\rfloor,\;c\bmod Q\right).
\]

This is an injection into `[S] x [Q]`.

### Tightness

Whenever `N = S Q`, every pair is needed and

\[
\log_2 N=\log_2 S+\log_2 Q.
\]

Therefore no theorem of the form

\[
\Omega_{\mathrm{cont}}\le M+I-\phi(M,I)
\]

with a universally positive `phi(M,I)>0` can hold under this bare model. More generally, no mandatory extra positive interaction charge can be inferred merely from the coexistence of persistent memory and side information; additional operational structure is required.

This does **not** rule out nonlinear terms produced by restrictions such as noisy channels, locality, causal order, bounded rounds, lossy memory, privacy constraints, energetic costs, action restrictions, or structured task families. It rules out claiming such a penalty universally from typed accounting alone.

## Exact regression

`experiments/audit138_memory_sideinfo_capacity_bound.py` checks all

- `N = 1,...,64`,
- `S = 1,...,64`,
- `Q = 1,...,64`.

Frozen result: `results/audit138_memory_sideinfo_capacity_bound.json`.

Results:

- parameter triples: **262,144**,
- feasible triples: **254,320**,
- infeasible triples: **7,824**,
- criterion violations: **0**,
- exact tight triples `N=S Q`: **280**,
- logarithmic-form violations: **0**.

The regression is a consistency check; the theorem is analytic.

## Prior-art collision

The mechanism is classical counting/coding, not new GC mathematics. It sits directly beside:

1. Myhill–Nerode/state complexity: exact continuation classes lower-bound required state memory.
2. Deterministic communication complexity: transcript counting yields lower bounds because a bounded transcript family can distinguish only boundedly many cases.
3. Automata with advice/side information: additional advice can trade against finite control state.
4. Streaming/space–communication reductions: retained state and communicated information are standard substitutable information-bearing resources in many lower-bound arguments.

Representative collision points checked in this audit include the Myhill–Nerode theorem, automata-with-advice extensions, and communication-complexity methods for automata lower bounds. Therefore the product/additive-log frontier must be labeled **IMPORTED/KNOWN** as a mathematical mechanism.

## Status ledger

- Exact product frontier `N <= S Q`: **PROVED**.
- Log form `log N <= log S + log Q`: **PROVED**.
- Tightness: **PROVED**.
- Exhaustive finite regression: **PASS**.
- Universal strictly positive nonlinear memory–information penalty under the bare model: **FALSIFIED**.
- Counting/coding/state-complexity mechanism: **IMPORTED/KNOWN**.
- GC-II breakthrough claim from this result alone: **FALSIFIED**.
- Structured coupling law under additional independently measurable operational constraints: **OPEN**.

## Consequence for Paper II

The next viable accounting target cannot obtain novelty merely by adding a generic nonlinear interaction term to persistent memory plus acquired information. A defensible GC-II term must arise from a separately specified operational obstruction—e.g. locality/causal/interface restrictions or action-limited information acquisition—and must survive reduction to standard communication, streaming, automata/advice, and process-resource formulations.
