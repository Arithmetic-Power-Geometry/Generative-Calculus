# GC-II Audit 130 — Local-to-Global Interaction-Order Blow-Up

## Question

Can GC-II derive a universal controlled-growth law of the form

\[
\operatorname{ord}(f_{\rm comp})\le G(k_{\rm local},w_{\rm interface},B)
\]

from bounded local interaction order, bounded interface width, and a typed budget, without also charging composition depth/network size or imposing stronger global structure?

## Result

**No, under the weakest admissible assumptions.** A serial chain of binary AND modules gives an exact counterexample whenever composition steps can have zero charged typed cost.

Let intervention bits be \(x_1,\ldots,x_n\in\{0,1\}\). Initialize a one-bit interface state \(s_0=1\) and compose

\[
s_i=s_{i-1}\wedge x_i,\qquad i=1,\ldots,n.
\]

Each local module has interface width one bit. As a Boolean function of its two inputs \((s_{i-1},x_i)\), its unique minimal successful witness is \(\{s_{i-1},x_i\}\), so its local interaction order is at most 2. Assign zero charged typed transition cost to every module.

The composite is

\[
s_n=\bigwedge_{i=1}^{n}x_i.
\]

Its unique minimal successful intervention set is \(\{1,\ldots,n\}\). Therefore

\[
\operatorname{ord}(f_{\rm comp})=n.
\]

Since \(n\) is arbitrary while \(k_{\rm local}=2\), \(w_{\rm interface}=1\), and the charged budget can remain \(B=0\), no finite bound depending only on those three quantities can upper-bound global interaction order for this class.

## Theorem — No depth-free local-to-global order bound

Consider a compositional operational class that contains the binary AND transducer above for arbitrary serial length and permits those composition steps at zero charged typed cost. Then there is no finite function \(G\) such that for every composite in the class

\[
\operatorname{ord}(f_{\rm comp})\le G(k_{\rm local},w_{\rm interface},B)
\]

when \(G\) is independent of serial depth/network size.

### Proof

Assume such a finite \(G\) exists. Evaluate it at the fixed tuple \((2,1,0)\) and write \(g=G(2,1,0)\). Choose \(n>g\). The length-\(n\) AND chain belongs to the class, has local interaction order at most 2, interface width 1, charged budget 0, and global interaction order \(n\). Thus \(n\le g\), contradiction. \(\square\)

## Domain and edge-case audit

- **Domains:** all intervention and interface variables are Boolean; interaction order is the maximum cardinality of a minimal successful intervention set.
- **Degenerate cases:** \(n=1\) has global order 1. The counterexample family uses \(n\ge2\).
- **Monotonicity:** every local module and the composite are monotone increasing.
- **Composition:** exact serial composition; no approximation or stochasticity is used.
- **Invariance:** renaming intervention coordinates or internal module labels does not change the interaction order.
- **Budget:** the impossibility result applies when the operational axioms permit zero-cost composition. If GC-II explicitly requires a strictly positive charge for every serial module/action/rule application, then budget can bound depth and this counterexample no longer establishes budget-independent blow-up. That stronger assumption must be stated and defended rather than smuggled into the theorem.
- **Reduction:** the construction is simply a bounded-fan-in Boolean circuit computing \(AND_n\). It is therefore not a new mathematical mechanism.

## Exact finite regression

`experiments/gc2_local_to_global_interaction_blowup_audit.py` exhaustively checks all Boolean assignments for \(n=2,\ldots,16\).

Frozen result:

- total assignments checked: **131,068**
- chain-vs-direct-AND mismatches: **0**
- maximum local interaction order: **2**
- interface width: **1 bit**
- charged typed transition cost: **0**
- maximum tested global interaction order: **16**

This computation is a regression check; the unbounded statement is established by the proof, not by extrapolating the finite experiment.

## Prior-art collision

The mechanism is standard bounded-fan-in circuit composition. In Boolean circuit complexity, fan-in bounds the number of direct inputs to each gate, while circuit depth measures the longest input-output path; bounded local fan-in does not imply bounded global input dependence as depth grows. Standard circuit-complexity treatments distinguish these parameters explicitly. See, e.g., Arora and Barak, *Computational Complexity: A Modern Approach* (2009), and the standard bounded-fan-in/NC formulation. A representative explicit statement is that a fan-in-2 circuit computing a function that depends on all \(n\) inputs requires depth at least \(\log n\); conversely, an AND tree/chain of fan-in-2 gates computes a globally \(n\)-input conjunction.

Related structural work also shows that tractability/compression for CSPs requires stronger global restrictions such as bounded treewidth, not merely bounded constraint arity; see Kolman and Koutecký (2015), *Extended Formulation for CSP that is Compact for Instances of Bounded Treewidth*, Electronic Journal of Combinatorics 22(4), P4.30, DOI 10.37236/5474.

## Status ledger

| Claim | Status |
|---|---|
| Serial binary modules can have local order 2 and global order \(n\) | **PROVED** |
| Width-1 interface prevents unbounded global interaction order | **FALSIFIED** |
| Monotonicity prevents the blow-up | **FALSIFIED** |
| A depth-free bound \(G(k_{local},w_{interface},B)\) under zero-cost composition exists | **FALSIFIED** |
| Exact finite regression through \(n=16\) | **NUMERICALLY SUPPORTED / EXHAUSTIVE OVER TESTED DOMAINS** |
| Bounded-fan-in circuit mechanism | **IMPORTED/KNOWN** |
| A controlled bound that also charges depth/size or assumes bounded global width/treewidth | **OPEN** |

## Consequence for GC-II

The next theorem attempt must include at least one independently justified global-control parameter. Plausible candidates are charged composition depth, network size, dependency-cone width/treewidth, or a conservation law that prevents repeated zero-cost aggregation. Without such an assumption, local bounded interaction order is not compositional.
