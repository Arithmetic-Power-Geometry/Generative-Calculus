# GC-II Audit 112 — Interface-Locality Collision No-Go

## Question
Can the post-Audit-111 surviving route—fix an interface-locality/distributed-access boundary and prove a positive capability overhead after augmented-state compilation—supply a standalone GC-II breakthrough?

## Result
**Not merely from locality or distributed ownership.** Once the realization boundary fixes which component initially holds which data, the communication graph, bandwidth/message rules, and permitted local computation, the apparent GC capability obstruction is a distributed-computation/communication lower-bound problem unless an additional GC-specific operational quantity is shown not to reduce to those models.

Let global configuration be `z=(z_1,...,z_m)` distributed across interfaces/nodes. A target capability is a function/relation `f(z)` that some designated node(s) must realize. Suppose local computation is free and nonlocal information can cross interfaces only through messages. If there exist two global configurations `z,z'` that are indistinguishable to a node under its radius-`t` view (or under a transcript budget `b`) but require different valid outputs, no algorithm respecting that boundary can realize the capability within that locality/transcript budget.

This is the standard indistinguishability/communication mechanism, not a new capability law.

### Cut reduction
For a partition `V=L union R`, collect all nodes on each side into two super-parties. Any distributed protocol that realizes `f` induces a two-party protocol for the corresponding partitioned input problem. Hence

`communication across cut >= CC(f_LR)`

up to the exact conventions of the fixed communication model. With per-message/per-round bandwidth `B`, communication-complexity lower bounds induce message/round constraints under the usual simulation assumptions.

**Status: IMPORTED/KNOWN mechanism.** Communication-complexity reductions have long been used to obtain distributed-network lower bounds; later work derives message/time tradeoffs by simulation. Locality lower bounds in LOCAL/related models similarly formalize inability to distinguish sufficiently similar local neighborhoods.

## Consequence for Omega_G
A candidate such as

`Omega_G = minimum cross-interface information/communication/locality needed to realize a new capability`

is not standalone GC-II novelty if it is equivalent to communication complexity, local information cost, round locality, query complexity, or a standard distributed lower bound under the fixed boundary.

The same applies if `Delta I` is simply transcript information and `Delta A` is simply messages/actions across the interface. Repackaging them inside a nonlinear `F(Delta R,Delta I,Delta A,Delta L)` does not alter the reduction.

## Exact kill example
Two nodes hold bits `x` and `y`; the left node must output `x XOR y`. With zero cross-interface communication, left's local view is identical for `(x,0)` and `(x,1)` while the required outputs differ. At least one bit must cross the cut in the deterministic exact model. This is a genuine capability obstruction under the fixed interface—but it is ordinary communication complexity.

## Edge and domain checks
- Co-located inputs: obstruction disappears, confirming dependence on the independently fixed boundary.
- Unlimited bandwidth/global communication: locality obstruction can disappear.
- Shared randomness: may change randomized bounds but does not create a GC-specific invariant.
- Approximate/error-tolerant tasks: use randomized/information communication complexity or distributional bounds; exact one-bit example is not silently generalized.
- Quantum/non-signaling resources: require the corresponding stronger distributed model; locality remains a mature model-dependent subject.
- Aliased actions: action cardinality remains presentation-sensitive and is not used as an invariant.
- Augmented-state compilation: still exact semantically; the lower bound comes from the imposed realization boundary, not from endogeneity.

## Prior-art collision gate
Classical communication complexity studies minimum communication required when inputs are distributed. Distributed-network lower bounds explicitly reduce network computation to communication problems. Modern message lower-bound work transfers communication lower bounds into synchronous distributed settings. The LOCAL/CONGEST literature has extensive locality and bandwidth lower bounds, and local information cost has been introduced as a lower bound on distributed communication.

Therefore interface locality, distributed ownership, bandwidth, or causal access **alone** cannot be claimed as the GC-II breakthrough mechanism.

## Status ledger
- Fixed-interface indistinguishability obstruction: **PROVED / IMPORTED-KNOWN mechanism**.
- Cut-to-communication reduction: **IMPORTED/KNOWN**.
- Interface locality as standalone source of GC-II novelty: **FALSIFIED**.
- Nonlinear recombination of standard locality/communication costs as escape: **FALSIFIED**.
- Representation-independent positive overhead from endogeneity plus locality alone: **FALSIFIED unless a new invariant survives the standard reductions**.
- A capability quantity jointly sensitive to budgeted generative closure yet provably not determined by ordinary transcript/local-view/communication/query complexity: **OPEN**.

## Stronger surviving target
The next candidate must separate **capability-set deformation itself** from the cost of computing a fixed target function. Seek two operational systems matched under a fixed realization boundary for conventional communication, local information, computation, reachability, and observable trace semantics, yet whose *sets of subsequently realizable transformations under equal future budgets* differ. Any proposed separation must then survive reduction to dynamic distributed algorithms, reconfiguration, online algorithms, metacomputation/program synthesis, and resource theories.

A useful next finite-world kill test is to define a horizon-`h` future-capability set `K_h(z,B)` and search exhaustively for matched systems with equal current traces and equal conventional cut/transcript complexity but unequal quotient-invariant `K_h`. If every such difference is reconstructible by augmenting the task/state description, that route collapses as well.

No GC-II breakthrough is claimed by this audit.