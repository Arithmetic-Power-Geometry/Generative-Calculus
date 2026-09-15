# GC-II Audit 160 — Projection-to-global translator information bound

## Candidate
Strengthen GC-I proper-projection irreducibility into an operational local-to-global translator lower bound.

Let `X=[p]^n`, and let `pi_k:X->[p]^k` retain `k` coordinates. A deterministic exact translator receives the local view `pi_k(x)` plus a message `m(x)` and must reconstruct every `x in X`.

## Theorem (exact fiber translator bound) — PROVED
For every retained local view `y`, the fiber `pi_k^{-1}(y)` has cardinality `p^(n-k)`. Exact reconstruction forces `m` to be injective on each fiber. Hence the translator alphabet must contain at least `p^(n-k)` messages. Equivalently, any worst-case fixed-length binary translator needs

`b >= ceil(log2(p^(n-k)))`

bits. In ideal information units the missing information is `(n-k) log2 p` bits.

The bound is tight: transmit the omitted coordinates (or an index of the fiber element).

## Edge/degenerate cases
- `k=n`: fiber size 1 and the lower bound is 0.
- `k=0`: exact global reconstruction needs `ceil(n log2 p)` fixed binary bits.
- Relabeling coordinates or alphabet symbols preserves fiber cardinality.
- Independent product systems multiply fiber sizes, so ideal information lower bounds add.
- For nonuniform projections, the general exact bound is `ceil(log2 max_y |pi^{-1}(y)|)` for worst-case fixed-length messages.

## Collision / novelty boundary — DECISIVE
This is a clean operational strengthening of projection irreducibility, but the mechanism is not independently novel. It is the pigeonhole/information lower bound underlying one-way communication/source coding: a receiver that must distinguish `N` possibilities requires at least `log2 N` bits (up to integer coding conventions). Distributed-computation lower bounds likewise quantify information/communication required to recover global functions from local observations. Local-to-global consistency theory in databases also already characterizes when local views determine a global object.

Therefore the raw translator-information lower bound is **IMPORTED/KNOWN**, not a GC-II breakthrough.

## Ledger
- Exact fiber translator lower bound: **PROVED**.
- Tightness by transmitting omitted coordinates/fiber index: **PROVED**.
- Finite exhaustive fiber-cardinality regression: **PASS**.
- Raw missing-information quantity as `Omega_G`: **FALSIFIED as independent novelty**.
- Communication/information lower-bound mechanism: **IMPORTED/KNOWN**.
- GC-II residual requiring coupled capability-generation semantics beyond fixed reconstruction: **OPEN**.

## Next gate
A viable GC-II theorem must not merely ask how many bits reconstruct a hidden global state. It should seek a separation where the same local information and communication budget permit ordinary reconstruction/decision, yet fail to *generate an admissible new capability* because resource, interface/action, and law constraints jointly restrict which information can be operationalized. Any candidate must be collision-tested against interactive/multiparty communication complexity, distributed synthesis, proof-labeling/local verification, database/CSP width, and contextuality/marginal extension theory.
