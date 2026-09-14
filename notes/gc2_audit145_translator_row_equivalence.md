# GC-II Audit 145 — Local-to-global translator lower-bound collision

## Status

- Exact translator characterization below: **PROVED**.
- Finite exhaustive regression: **PASS** (see `experiments/gc2_audit145_translator_row_equivalence.py`).
- Claim that a bare deterministic local-to-global translator lower bound is new GC-II mathematics: **FALSIFIED**.
- Distinct-row / deterministic one-way communication mechanism: **IMPORTED/KNOWN**.
- Translator lower bound with genuinely GC-specific resource/interface/rule semantics not reducible to communication complexity: **OPEN**.

## Operational model

Let local side A observe `x in X`, local side B observe `y in Y`, and let the required globally correct operational decision be a finite-valued function

`f : X x Y -> Z`.

A deterministic one-way translator sends a message `m(x)` from A to B. B must recover `f(x,y)` exactly from `(m(x),y)` for every `x,y`.

Define residual functions

`r_x : Y -> Z`,  `r_x(y)=f(x,y)`.

Let

`R(f) = |{r_x : x in X}|`.

## Exact Translator Theorem

The minimum number of deterministic translator messages is exactly

`M*(f)=R(f)`, 

and the minimum fixed-length translator budget is

`B*(f)=ceil(log2 R(f))` bits.

### Necessity

If `r_x != r_x'`, some `y` satisfies `f(x,y) != f(x',y)`. If the translator assigned the same message to `x` and `x'`, B would receive the same `(message,y)` in both cases and could not output both required values. Thus distinct residual functions require distinct messages.

### Sufficiency

Send the equivalence-class index of `r_x`. B stores one representative residual function per class and evaluates it at `y`. Therefore exactly `R(f)` messages suffice.

The proof includes degenerate cases: constant functions have `R=1` and require zero bits; unused distinctions in X are automatically quotiented; arbitrary finite output alphabets Z are allowed.

## Consequence for GC-II

This is precisely the distinct-row characterization of deterministic one-way communication: the rows of the communication matrix are the residual functions `r_x`. Hence a GC-I projection-irreducibility witness translated into this bare model yields a valid operational lower bound, but not a novel mechanism. Rebranding row distinguishability as a `Generative Translator Gap` would overclaim novelty.

The surviving target must impose typed operational constraints not erased by the communication-matrix abstraction—for example coupled resource depletion, interface creation/destruction, rule-dependent admissibility, or translator actions that alter the future closure—and then prove a separation from the best communication-complexity representation.

## Verification obligations

- Domains: finite X,Y,Z; exact deterministic one-way translation.
- Monotonicity: refining residual equivalence can only increase R.
- Invariance: relabeling X,Y,Z preserves R.
- Composition: no additive law is asserted; composition can merge or split residual classes depending on the composed task.
- Edge cases: R=1 gives B*=0; R=|X| gives maximal row distinction.
- Prior-art boundary: deterministic one-way communication complexity already characterizes the cost by distinct communication-matrix rows (up to the ceiling/log convention for fixed-length messages).
