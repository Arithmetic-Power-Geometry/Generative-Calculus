# GC-II Audit 129 — Bounded Interaction Order Boundary

Status date: 2026-09-14
Branch: `gc2-capability-accounting-lab` only

## Question

Audit 128 left bounded interaction order as a possible source of a substantially smaller complete intervention certificate. This audit tests that route before treating it as GC-II novelty.

Let the intervention ground set be `[m]`. A binary response `f:2^[m] -> {0,1}` is **monotone** when `S subseteq T` implies `f(S) <= f(T)`. Let `A_f` denote the antichain of minimal successful intervention sets. Define interaction order

`ord(f) = max{|A| : A in A_f}`,

with `ord(f)=0` for the identically-zero function.

Assume independently that `ord(f) <= k`.

## Theorem 129.1 — Exact bounded-rank certificate

**PROVED.** For every monotone binary response with `ord(f) <= k`, the minimal-success family `A_f` is a complete exact certificate and every member has size at most `k`:

`f(S)=1  <=>  exists A in A_f with A subseteq S`.

Consequently an explicit certificate contains at most

`sum_{i=0}^k binom(m,i)`

candidate subsets, and at most `binom(m,k)` minimal witnesses when `k <= m/2` (more generally its size is bounded by the largest available antichain layer among levels `<=k`). For fixed `k`, this is polynomial in `m`.

### Proof

Monotonicity gives the forward closure of every minimal successful set. Conversely, every successful finite set contains an inclusion-minimal successful subset. The interaction-order assumption places every such minimal subset at level at most `k`. Completeness follows immediately. The counting bound follows because all witnesses lie among subsets of sizes `0..k`; the sharper antichain bound is Sperner-type structure restricted to those levels.

## Why this is not a GC-II breakthrough

**FALSIFIED as standalone novelty.** The certificate is exactly a bounded-rank hypergraph / bounded-width monotone DNF representation: minimal successful sets are hyperedges (prime implicants), and `ord(f)<=k` is a rank/width bound. Enumeration of minimal sets for monotone properties and bounded-rank hitting-set/hypergraph problems is established combinatorial territory. Thus GC-II may use this representation, but cannot claim the mathematical compression principle itself as new.

The important scientific boundary is therefore:

`bounded interaction order` is useful only if GC-II derives it from independently stated operational closure axioms, rather than assuming it as a representation restriction.

## Exact finite stress test

The checker exhaustively enumerates every antichain drawn from all nonempty subsets of `[6]` of size at most 2. There are 21 candidate witnesses and 2^21 candidate families before the antichain filter.

Frozen result:

- `m=6`, `k=2`
- exact bounded-rank antichains: `40,069`
- maximum certificate size observed: `15 = binom(6,2)`
- every represented monotone response reconstructs exactly from its minimal-success family
- zero reconstruction failures
- zero interaction-order violations

The maximum is achieved by taking all 15 two-element subsets.

## Edge and composition checks

- `k=0`: only constant-zero, unless the empty intervention is admitted as a successful witness; conventions must be explicit.
- `k=1`: certificates are singleton-trigger OR functions, already elementary.
- `k>=m`: the restriction disappears and Audit 128's full monotone-antichain worst case returns.
- Degenerate redundant witnesses are excluded automatically by antichain minimality.
- Sequential/compositional closure does not preserve a fixed `k` without an additional theorem: composing mechanisms can create higher-order minimal enabling sets. Therefore `ord<=k` must not silently be assumed invariant under GC composition.

## Status ledger

- Minimal-success reconstruction for monotone response: **PROVED** (Audit 128).
- Polynomial explicit certificate for fixed bounded interaction order: **PROVED**.
- Exact finite exhaustive check at `(m,k)=(6,2)`: **NUMERICALLY SUPPORTED / EXHAUSTIVE**.
- Bounded-rank hypergraph / bounded-width monotone-DNF interpretation: **IMPORTED/KNOWN**.
- Bounded interaction order as standalone GC-II novelty: **FALSIFIED**.
- Derivation of bounded interaction order from GC operational axioms: **OPEN**.
- Preservation or controlled growth of interaction order under GC composition: **OPEN**.

## Next breakthrough gate

Do not proceed by merely assuming sparsity, low rank, submodularity, or bounded width. The next credible target is a theorem of the form

`operational locality + typed budget rules + admissible composition => ord(f_comp) <= G(local orders, interface width, budget)`

with a nontrivial `G`, followed by counterexample search and collision checks against hypergraph width, CSP/treewidth, circuit complexity, graphical models, communication complexity, and compositional resource theories. If no such operational derivation survives, bounded interaction order is only an imported modeling assumption, not a GC-II law.
