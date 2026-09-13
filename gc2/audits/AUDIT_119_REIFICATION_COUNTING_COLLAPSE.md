# GC-II Audit 119 — Reification Counting Collapse

## Target
Test the surviving Audit-118 route: whether optimizing over all admissible encodings can yield a representation-independent lower bound on the cost of reifying newly created schema/types that is distinct from established information/representation lower bounds.

## Setup
Let `S={s_1,...,s_M}` be a finite family of semantically distinguishable newly creatable schema/types. A lossless reifier is any injective binary encoding `e:S -> {0,1}*`. Let `L_max(e)=max_s |e(s)|`. If instantaneous/prefix-free decoding is required, impose the prefix-free condition; otherwise only injectivity is required.

## Theorem 119.1 — Finite Reification Counting Bound
**Status: PROVED.**

For any fixed-length lossless representation of M semantically distinguishable schema/types,

`L >= ceil(log2 M)`.

Proof: L bits provide at most `2^L` codewords. Injectivity requires `M <= 2^L`.

For variable-length prefix-free codes with lengths `l_s`, Kraft's inequality gives

`sum_s 2^{-l_s} <= 1`.

Consequently `max_s l_s >= ceil(log2 M)`. Under a probability law p, expected length is bounded below by Shannon entropy, up to the standard coding convention/rounding terms.

## Theorem 119.2 — Encoding Optimization Does Not Create a New Invariant
**Status: PROVED under the finite lossless model.**

Define the optimized worst-case reification burden

`R*(S)=inf_e max_s |e(s)|`

over all fixed-length lossless binary encodings. Then

`R*(S)=ceil(log2 |S|)`.

Thus optimizing away representation choice does produce a quotient-stable quantity, but in this model it is exactly the elementary information-theoretic counting bound. Calling it `Omega_G` does not make it a new capability law.

## Operational strengthening and collision
If reified objects must support operations without full decoding, the problem becomes a representation/data-structure problem: space, redundancy, query time, update time, preprocessing, word size, and randomization must be fixed. Strong lower-bound models such as the cell-probe model deliberately permit unusual representations while charging memory probes. Therefore a lower bound that survives broad encoding freedom is not by itself outside existing theory.

## Edge/degenerate checks
- `M=0`: no object is selected; reification cost is undefined or conventionally zero only after specifying the task. Do not apply the logarithm formula as a capability claim.
- `M=1`: bound is 0 bits when the sole semantic object is common knowledge.
- Non-injective encodings: invalid for exact semantic identification unless side information is included; that side information must be charged or conditioned upon.
- Shared side information `Z`: replace unconditional distinguishability by the residual family compatible with Z; probabilistically this leads to conditional information/coding quantities.
- Approximate/lossy reification: counting no longer suffices; a distortion/error model is required, moving toward rate-distortion/covering arguments.
- Interactive/oracular reification: transcript/query cost replaces static description length and collides with communication/query complexity.
- Computation time for decoding: not controlled by description length; requires a computational model.

## Consequence for GC-II
**DECISIVE FALSIFICATION:** “representation-independent reification cost after optimizing over all encodings” is not a standalone GC-II novelty mechanism in the finite exact case. Its strongest universal lower bound without additional operational structure is the counting/information bound. Adding supported operations moves the problem into succinct/data-structure and cell-probe lower-bound territory; adding interaction moves it into communication/query complexity; adding approximation moves it into lossy coding/rate-distortion territory.

## What survives
A viable GC-II theorem must couple capability closure to a constraint not erased by semantic relabeling and not reducible to description, storage, query, communication, or ordinary conversion cost. The next candidate should therefore be tested at the level of **joint closure geometry across a family of tasks/budgets**, asking whether there is an obstruction in the *shape of the attainable capability region* that is invariant under admissible resource-coordinate changes yet not merely a standard Pareto/resource-theory monotone. This is OPEN and must be collision-tested before any novelty claim.

## Status table
- Finite Reification Counting Bound: **PROVED**.
- Optimized fixed-length exact reification cost `ceil(log2 M)`: **PROVED**.
- Representation-independent reification cost as standalone GC-II novelty: **FALSIFIED**.
- Prefix-free/entropy strengthening: **IMPORTED/KNOWN**.
- Operation-supporting representation lower bounds: **IMPORTED/KNOWN framework**.
- Approximate/interactive variants: **IMPORTED/KNOWN neighboring frameworks; GC-specific residual OPEN**.
- Joint closure-geometry obstruction: **OPEN**.
