# GC-II Audit 131 — Charged Composition Support Bound

## Status

- **PROVED:** A positive lower charge on every nontrivial bounded-fan-in aggregation step converts a total composition budget into a global interaction-order bound.
- **NUMERICALLY SUPPORTED:** Exact regression over the parameter grid in `experiments/gc2_charged_composition_support_bound.py` has zero violations.
- **IMPORTED/KNOWN mechanism:** The combinatorial core is the classical relation between bounded fan-in, circuit/formula size, and number of source inputs. This is not claimed as new circuit-complexity mathematics.
- **OPEN:** Whether GC-II's typed operational semantics force a nonzero lower charge for every capability-expanding aggregation, and whether the resulting charge can be identified with an invariant not reducible to ordinary circuit size/cost.

## Setup

Consider an acyclic compositional realization whose terminal capability predicate is computed from primitive intervention variables. Each nontrivial internal aggregation node has fan-in at most `k >= 2`. Let `g` be the number of aggregation nodes in the ancestor subgraph of the terminal output. Assume each such aggregation carries a strictly positive charged operational cost at least `c > 0`, paid from one shared composition budget `B`.

Let `supp(y)` be the set of primitive intervention variables on which terminal output `y` can actually depend. Define global interaction order as `ord(y) = |supp(y)|` for the maximal-support witness class considered here.

## Theorem 131.1 — Charged Aggregation Support Bound

If every nontrivial aggregation node has fan-in at most `k` and costs at least `c`, then every feasible realization under total aggregation budget `B` satisfies

\[
 g \le \left\lfloor \frac{B}{c}\right\rfloor
\]

and

\[
\boxed{
 |\operatorname{supp}(y)|
 \le 1+(k-1)g
 \le 1+(k-1)\left\lfloor\frac{B}{c}\right\rfloor .
}
\]

Consequently, any monotone capability response whose unique minimal successful witness requires `q` distinct primitive interventions obeys the necessary budget condition

\[
\boxed{
B \ge c\,\left\lceil\frac{q-1}{k-1}\right\rceil .
}
\]

### Proof

Take the ancestor DAG of the terminal output and ignore primitive-input vertices not used by that output. Let it contain `g` internal aggregation vertices and `s` distinct primitive source vertices. Every internal vertex has indegree at most `k`.

Because every source contributing to the output must connect through this ancestor DAG to the terminal node, its underlying undirected graph is connected. A connected graph on `s+g` vertices has at least `s+g-1` edges. On the other hand, every edge enters an internal aggregation vertex, so the number of edges is at most `kg`. Therefore

\[
s+g-1 \le kg,
\]

hence

\[
s\le 1+(k-1)g.
\]

Since every aggregation node costs at least `c` and the total charged aggregation budget is at most `B`, `cg <= B`, giving `g <= floor(B/c)`. Substitution proves the displayed support bound. Rearranging the support inequality for a required witness size `q` gives the budget lower bound. QED.

## Tightness

The bound is tight for rooted full/partial `k`-ary aggregation trees. A tree with `g` internal nodes can have exactly

\[
1+(k-1)g
\]

leaves. Assign a distinct primitive intervention to each leaf and use monotone AND at every internal node. The terminal success predicate then has one minimal successful witness containing every leaf, so its interaction order reaches the bound exactly.

## Relation to Audit 130

Audit 130 proved that bounded local interaction order and interface width alone do **not** bound global interaction order when repeated aggregation is free. Audit 131 identifies the minimal repair: composition size itself must be charged or otherwise globally controlled. The earlier width-1 serial AND chain now obeys

\[
q=n,\qquad g=n-1,\qquad B\ge c(n-1),
\]

so unbounded global interaction requires unbounded charged budget.

## Edge and degenerate cases

- `g=0`: at most one primitive source can feed the output; the bound gives `s <= 1`.
- `B<c`: no charged aggregation node is feasible, again giving `s <= 1`.
- `k=1`: no genuine aggregation occurs; the theorem is stated for `k>=2` because the inverse lower bound divides by `k-1`.
- Zero-cost aggregation (`c=0`) destroys the bound and recovers Audit 130's counterexample.
- Sharing/sub-DAG reuse does not break the proof; sharing reduces or preserves edge count relative to the fan-in cap and cannot exceed the source bound for fixed `g`.
- The theorem concerns source-support/interaction order, not semantic difficulty, computational depth, or information content.

## Prior-art collision assessment

The graph-counting core is standard bounded-fan-in circuit/formula combinatorics: circuit **size**, **depth**, and **fan-in** are classical complexity measures, and size lower bounds based on the number of input dependencies are not novel in themselves. Therefore GC-II must not present Theorem 131.1 as a new theorem of circuit complexity.

The potentially GC-specific content, still **OPEN**, is semantic: whether the four typed capability accounts `(R,I,A,L)` imply a defensible positive lower charge `c` for each capability-expanding aggregation under admissible transformations, and whether that charge is invariant under implementation refinement and operational equivalence.

## Consequence for the Paper-II program

This is the first repaired quantitative accounting statement surviving Audit 130's zero-cost blow-up:

\[
\boxed{
\operatorname{ord}(f_{\rm comp})
\le
1+(k-1)\left\lfloor\frac{B_{\rm comp}}{c_{\min}}\right\rfloor .
}
\]

It is scientifically useful but **not yet a GC-II breakthrough**. The next gate is to replace the assumed positive aggregation charge by a theorem derived from explicit operational closure axioms, or to prove that such a universal positive charge is impossible by constructing arbitrarily capability-expanding zero-charge refinements under those axioms.
