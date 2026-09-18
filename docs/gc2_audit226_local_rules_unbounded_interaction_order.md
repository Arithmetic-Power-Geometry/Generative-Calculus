# GC-II Audit 226 — Local operational rules do not bound capability-interaction order

## Question
Audit 225 left open whether GC-I projection/local structure can force a non-generic restriction on the Möbius interaction spectrum of a capability valuation. The first candidate is a bounded-support theorem: if each admissibility/transition rule depends on at most k augmentation coordinates, must capability interactions above order k vanish?

## Result
**FALSIFIED, even for k=1.** Sequential composition of unary-gated transitions can generate an arbitrarily high-order capability interaction.

Let N={1,...,n} index augmentation coordinates and let the operational state space be Q={0,...,n}. State 0 is initial and n is the target. For i=1,...,n there is one forward transition

    i-1 -> i

which is admissible iff augmentation i is present. No other forward transition exists. Every augmentation-dependent gate therefore reads exactly one coordinate. Give every transition zero cost (or unit cost with budget B>=n; the conclusion is unchanged).

For S subseteq N define the target capability valuation

    v(S)=1[target n is reachable from 0 under augmentations S].

The unique path to n uses every gate, hence

    v(S)=1[N subseteq S].

Since S itself is a subset of N, this is simply the n-way conjunction: v(S)=1 iff S=N.

Its Möbius transform is

    m(T)=sum_{U subseteq T} (-1)^(|T|-|U|) v(U).

Therefore m(T)=0 for every proper T subset N, while

    m(N)=1.

So the interaction degree is n although every primitive augmentation gate has arity one. As n is arbitrary, there is no universal interaction-order bound in terms of primitive rule arity alone.

## Stronger statement
For every n>=1 and every k>=1, a system whose primitive augmentation-dependent rules have arity at most k can have nonzero Möbius interaction of order n. The unary construction already belongs to every class with arity bound k>=1.

## Why this matters
A tempting GC-II claim would be that local/proper-projection structure implies sparsity or bounded order in the capability-interaction spectrum. This construction blocks that claim unless additional assumptions control **composition topology**, path length/depth, reuse, or the aggregation semantics. Locality of primitive rules is not inherited by the extensional reachability indicator.

The mechanism is ordinary compositional reachability: serial prerequisites turn local gates into a global conjunction. Thus the separation is not evidence of GC-specific novelty.

## Prior-art collision boundary
The algebraic side is standard: k-additive capacities are exactly set functions whose Möbius coefficients vanish above order k, equivalently pseudo-Boolean functions of bounded polynomial degree. Factor graphs/CSPs likewise encode global functions from local factors. The present audit's point is negative: a locally factored **transition system** need not induce a k-additive **reachability valuation**, because existential/sequential composition can raise effective interaction order.

## Edge and degeneracy checks
- n=1: one unary gate, m({1})=1; no separation between local and global order, as expected.
- n=2: two unary gates in series produce the first strict separation: m({1,2})=1.
- Empty augmentation set: target is unreachable for n>=1.
- Zero-cost transitions: resource budget is irrelevant; the obstruction is structural rather than monetary.
- Unit-cost transitions: with B>=n the same valuation is obtained; with B<n the valuation is identically zero.
- Monotonicity: if S subseteq T then v(S)<=v(T).
- Relabeling invariance: coordinate permutations leave the construction isomorphic.
- Composition: serial composition is exactly what creates the high-order term.

## Status ledger
- Unary local gates with arbitrary n-way capability interaction: **PROVED**.
- Primitive-rule arity implies bounded Möbius interaction order: **FALSIFIED**.
- Generic high-order interaction as GC novelty: **FALSIFIED / IMPORTED-KNOWN boundary**.
- Bounded interaction order under stronger restrictions on compositional depth/topology: **OPEN**.
- A GC-I-specific spectral constraint surviving unrestricted serial composition: **OPEN**.

## Reproducibility
`experiments/gc2_audit226_local_rules_unbounded_interaction.py` exactly enumerates every augmentation subset for n=1,...,10, computes reachability, computes the full Möbius transform, and asserts that the sole nonzero coefficient is the full n-set with value 1.