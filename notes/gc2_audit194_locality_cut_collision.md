# GC-II Audit 194 — locality-cut translator collision

Status: **PROVED / IMPORTED-KNOWN mechanism; proposed GC-specific route FALSIFIED**

## Question

Audit 193 left open whether a fixed reusable primitive basis becomes GC-II-specific once information must be transported through a locality graph. This audit tests the cleanest candidate: an operational local-to-global translator lower bound induced by a communication cut.

## Model

Let `G=(V,E)` be an interaction graph. Node `v` initially holds local datum `x_v`. A deterministic exact protocol may perform arbitrary local computation for free and may send finite binary strings only along edges. A designated sink must output a target `f(x)`. For a cut `(S,V\S)`, define `B_S(P,x)` as the total number of bits transmitted across cut edges by protocol `P` on input `x`.

The operational closure budget includes communication explicitly; no information may cross the cut except through these messages.

## Exact bridge witness

Take a path (or any graph with a bridge `e`) whose deletion separates nonempty sides `S,T`. Put one unknown bit `a` on `S`, one unknown bit `b` on `T`, and require a sink in `T` to output

`f(a,b)=a XOR b`.

### Theorem 194.1 — bridge parity translator lower bound

Every deterministic exact protocol has worst-case communication at least one bit from `S` to `T` across `e`.

**Proof.** Assume no bit from `S` reaches `T`. Fix `b`. The complete state/transcript available on side `T` is then identical for inputs `(0,b)` and `(1,b)`, because all local data and all messages available to `T` are independent of `a`. Exact parity differs on these inputs. Contradiction. Therefore at least one cross-cut bit is necessary. One bit is sufficient: transmit `a` across the bridge and XOR locally with `b`. Hence the exact optimum is one bit. QED.

The statement is invariant under renaming nodes, edges, symbols, and local state encodings. Degenerate cases behave correctly: if `f` is independent of `S`, zero cross-cut communication suffices; if the sink is moved to `S`, the symmetric statement applies to information originating in `T`.

## Collision

This is not a new GC-II lower-bound mechanism. It is a direct deterministic communication/distributed-computing cut argument. Communication-complexity reductions are a standard source of distributed lower bounds, and in-network function-computation literature explicitly develops topology-sensitive lower bounds for arbitrary functions. Therefore rebranding cut communication as a `local-to-global translator cost` would not survive the required prior-art collision test.

## Consequence

Locality can make a capability expensive, but **locality + fixed basis + exact global target is insufficient for a GC-specific breakthrough**. Any proposed translator invariant that is only the minimum information/messages/rounds crossing a separator remains, absent additional structure, an instance of communication/distributed complexity.

A surviving target must couple locality to *endogenous change of the admissible closure itself* in a way that cannot be compiled into a fixed distributed protocol instance. A candidate must be tested against dynamic distributed algorithms, communication complexity, network coding, circuit wire complexity, CSP/database width, and reachability before promotion.

## Ledger

- Bridge-parity cross-cut lower bound: **PROVED**.
- Tight one-bit upper bound: **PROVED**.
- Generic separator communication as a GC-specific translator invariant: **FALSIFIED**.
- Communication/distributed lower-bound mechanism: **IMPORTED/KNOWN**.
- Endogenous closure-changing locality invariant not reducible to a fixed protocol: **OPEN**.

## Reproducibility target

`experiments/gc2_audit194_bridge_parity_cut.py` exhaustively checks the zero-bit impossibility and one-bit construction for all four two-bit inputs. The script is intentionally finite and exact; it does not claim empirical novelty.
