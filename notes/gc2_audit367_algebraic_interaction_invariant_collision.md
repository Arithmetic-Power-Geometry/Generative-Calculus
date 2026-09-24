# GC-II Audit 367 — Algebraic interaction invariant collision

## Scope

This audit attacks the surviving target after Audit 366: a GC-native structural projection/generation invariant that is independently computable and provably lower-bounds operational cost. GC-I on `main` remains frozen.

## Candidate invariant

For a Boolean capability predicate `f:{0,1}^n->{0,1}`, write its unique multilinear real representation

`f(x)=sum_{S subseteq [n]} a_S prod_{i in S} x_i`.

Define the highest nonzero interaction order

`Pi_alg(f)=max{|S|: a_S != 0}=deg(f)`.

This is attractive as a projection/generation invariant because it is representation-independent at the truth-table level, vanishes to zero exactly for constant predicates, and records the largest irreducible coordinate interaction appearing in the multilinear expansion.

## Proposition 367.1 — exact query lower bound

**Status: PROVED; mechanism IMPORTED/KNOWN.**

For deterministic coordinate-query complexity `D(f)`,

`D(f) >= Pi_alg(f)`.

### Proof

A deterministic decision tree of depth `d` computes a multilinear polynomial of degree at most `d`: recursively, a node querying coordinate `i` with child functions `g_0,g_1` computes `(1-x_i)g_0+x_i g_1`; induction on remaining depth bounds the resulting multilinear degree by `d`. The unique multilinear polynomial for `f` therefore has degree at most the depth of every exact decision tree. Hence `D(f)>=deg(f)`. QED.

## Edge and composition checks

- Constant predicate: `Pi_alg=0`, `D=0`.
- Literal: `Pi_alg=1`, and one exact coordinate query suffices.
- `AND_n`, `OR_n`, and parity all have real multilinear degree `n`; therefore the bound gives `D>=n`, which is tight under coordinate queries.
- Relabeling coordinates leaves `Pi_alg` invariant.
- Negating the output of a nonconstant Boolean predicate leaves its degree unchanged.
- Restriction cannot increase degree.
- For predicates on disjoint variable sets, multiplication satisfies `deg(fg)=deg(f)+deg(g)` when both leading products survive; arbitrary Boolean composition requires explicit hypotheses and is not assigned an additive law here.

## Prior-art collision

This candidate fails the novelty test decisively. Polynomial degree is a classical Boolean-function complexity measure, and the relationship between degree and decision-tree complexity is established theory. Nisan and Szegedy's work studies polynomial degree together with decision-tree and related Boolean complexity measures. Therefore renaming degree as a GC projection/generation invariant would add no foundational content.

## Proposition 367.2 — degree does not encode the full operational cost

**Status: PROVED.**

Even as a lower bound, `Pi_alg` is not a complete capability-accounting invariant. For example, for `f(x)=x_1`, `deg(f)=1` and `D(f)=1`, whereas for `g(x)=OR_n(x)`, `deg(g)=n` and `D(g)=n`; degree can track these examples, but classical theory already supplies the interpretation. More generally, Boolean degree and decision-tree complexity are distinct measures rather than definitions of one another; importing degree therefore cannot establish a new GC-specific accounting law.

The key scientific point is not that degree is useless; it is that a successful `Pi_G` cannot simply instantiate an already-known Boolean complexity measure.

## Consequence for the surviving search

Audit 366 required an independently computable structural invariant. Audit 367 adds a stronger novelty filter:

1. truth-table/Fourier/polynomial degree, sensitivity, block sensitivity, certificate complexity, rank, discrepancy, rectangle number, and standard query measures must be treated as imported when used directly;
2. a GC-native candidate must be derived from the *generator/closure architecture before the terminal capability predicate is fully expanded*;
3. it must predict a nontrivial operational cost or novelty quantity across systems having the same standard coarse complexity statistics;
4. the next exhaustive search should therefore enumerate small generator hypergraphs/closure rules and compare architecture-level quantities against exact capability novelty and exact synthesis/query costs, explicitly searching for collisions with all standard invariants.

This shifts the target from a property of the final Boolean function to a property of the generative presentation and its closure dynamics.

## Status table

- algebraic interaction order `Pi_alg=deg(f)` — **DEFINED / IMPORTED-KNOWN**
- `D(f)>=Pi_alg(f)` — **PROVED / IMPORTED-KNOWN mechanism**
- polynomial degree as GC-II foundational invariant — **FALSIFIED by prior-art collision**
- terminal-predicate-only standard complexity invariant as sufficient GC novelty — **FALSIFIED as a novelty route**
- generator-architecture invariant predicting operational cost beyond standard terminal measures — **OPEN / PRIORITY**
- exhaustive generator-hypergraph collision search — **OPEN / NEXT**

## Scientific guardrail

No novelty is claimed for polynomial representations of Boolean functions, degree lower bounds, sensitivity-style measures, decision-tree complexity, or their classical relationships. The surviving GC-II target must depend essentially on generative architecture/closure and survive reduction against these standard measures.