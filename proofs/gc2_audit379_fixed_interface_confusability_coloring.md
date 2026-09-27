# GC-II Audit 379 — Fixed-interface translator complexity collapses to confusability coloring

**Scope.** Paper-II capability-accounting branch only. GC-I foundations are unchanged.

## 1. Fixed interface model

Let (X) be a finite set of global states. The sender observes (x\in X). The receiver observes a fixed local projection (p(x)\in P). The receiver must output (g(x)\in Y) exactly. A deterministic one-way translator consists of an encoder (m:X\to[M]) and decoder (D:P\times[M]\to Y) satisfying

[
D(p(x),m(x))=g(x)\qquad\forall x\in X.
]

This deliberately fixes the interface that was underdetermined in earlier audits.

## 2. Confusability graph

Define the undirected graph (G_{p,g}) on vertex set (X) by

[
\{x,x'\}\in E(G_{p,g})
\iff
p(x)=p(x')\ \text{and}\ g(x)\neq g(x').
]

Two adjacent global states give the receiver identical side information but require different exact outputs.

## 3. Theorem — exact translator/coloring equivalence

**Theorem 379.1 (PROVED / IMPORTED-KNOWN mechanism).** A deterministic exact translator with (M) messages exists iff (G_{p,g}) is (M)-colorable. Consequently,

[
M_{\min}=\chi(G_{p,g}),
\qquad
b_{\min}=\left\lceil\log_2\chi(G_{p,g})\right\rceil
]

for worst-case fixed-length binary communication.

### Proof

**Necessity.** Suppose (m) is a valid encoder. If (x\sim x'), then (p(x)=p(x')) but (g(x)\ne g(x')). If (m(x)=m(x')), the decoder receives the same pair ((p,m)) for both states and would have to output two different values, impossible. Thus (m) is a proper coloring, so (M\ge\chi(G_{p,g})).

**Sufficiency.** Let (c:X\to[\chi]) be a proper coloring. For each pair ((u,k)) that occurs as ((p(x),c(x))), all states realizing that pair have the same (g)-value: otherwise two such states would be adjacent and could not share color (k). Define (D(u,k)) to be this common value (arbitrary on unused pairs). Taking (m=c) yields exact decoding. QED.

## 4. Edge and degenerate cases

- If (g) is constant on every fiber of (p), (G_{p,g}) has no edges, (\chi=1), and zero transmitted bits suffice.
- If (p) is injective, again (\chi=1): the receiver already knows the global state relevant to decoding.
- If a fiber of (p) contains (q) states with pairwise distinct (g)-values, it induces (K_q), hence at least (\lceil\log_2 q\rceil) fixed-length bits are necessary.
- Duplicate states with identical ((p,g)) create no edge and require no separation.
- The theorem concerns single-instance, deterministic, exact, one-way, fixed-interface translation. Randomized/error-tolerant, interactive, variable-length, block/asymptotic, quantum, or distribution-sensitive models require different quantities.
- Under relabelings of (X,P,Y), graph isomorphism preserves (\chi), so the bound is representation invariant.
- Independent parallel composition is not generally additive in (\log\chi); product-graph behavior must be specified rather than assumed.

## 5. Collision with prior art

This mechanism is classical zero-error coding/function-computation structure, not a GC-II novelty.

- Witsenhausen (IEEE TIT, 1976), *The zero-error side information problem and chromatic numbers*, establishes the graph-coloring equivalence for zero-error side information and notes possible block-coding gains.
- Zero-error source-channel coding with decoder side information uses a source confusability graph; the smallest zero-error source-code index set is its chromatic number.
- Functional compression with side information uses characteristic graphs and graph coloring/fractional coloring; asymptotic variants lead to graph-entropy quantities.
- Recent zero-error function-computation work continues to characterize classical communication using chromatic numbers of confusion graphs.

Therefore neither the graph nor its chromatic translator bound can be presented as a new GC theorem without an additional GC-specific separation.

## 6. Consequence for GC-II target (7)

The tempting implication

[
\text{GC-I projection irreducibility}
\Rightarrow
\text{positive translator cost}
]

becomes meaningful only after fixing an interface. Under the present natural exact one-way interface, its generic quantitative content is already captured by (G_{p,g}) and (\chi(G_{p,g})).

Thus:

| Candidate | Status |
|---|---|
| Exact translator iff proper coloring | PROVED / IMPORTED-KNOWN |
| (M_{\min}=\chi(G_{p,g})) | PROVED / IMPORTED-KNOWN |
| Fixed-length (b_{\min}=\lceil\log_2\chi\rceil) | PROVED / IMPORTED-KNOWN |
| Bare projection irreducibility gives unconditional numerical cost | FALSIFIED |
| Chromatic translator deficit as GC-II novelty | FALSIFIED AS NOVEL |
| GC-specific operational separation beyond full confusability graph | OPEN |

## 7. Stronger breakthrough gate

A surviving target must beat the entire confusability-graph description, not merely its chromatic number. Seek matched finite systems (S_1,S_2) with isomorphic (G_{p,g}) (hence identical single-instance exact translator complexity) and matched ordinary reachability/cost summaries, but different frozen GC-I envelope/projection structure. Then derive, without recomputing the target operational problem, a GC quantity that predicts a further operational separation.

Until such a matched-pair separation is found and prior-art checked, no translator lower bound should be claimed as a GC-II breakthrough.
