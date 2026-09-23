# GC-II Audit 352 — Exponential exact-certificate barrier for two-resource capability accounting

## Status

- Exponential Pareto-frontier family: **PROVED**.
- Exponential lower bound for explicit exact all-budget certificate by listing Pareto-minimal resource vectors: **PROVED**.
- Impossibility of every polynomial-size implicit/symbolic representation: **NOT CLAIMED / OPEN**.
- Multiobjective shortest-path/Pareto-frontier mechanism: **IMPORTED/KNOWN**.
- GC-II consequence for Audit 351: **PROVED boundary statement**.

## Setup

Audit 351 showed that for nonnegative vector edge charges, the Pareto-minimal path-cost set

\[
\mathcal P^*(s,t)=\operatorname{Min}_{\le}\{c(P):P:s\leadsto t\}
\]

is a complete certificate for every componentwise budget query:

\[
t\in\mathrm{Cl}_b(s)\iff \exists p\in\mathcal P^*(s,t):p\le b.
\]

Audit 352 asks whether that exact certificate is necessarily compact when the resource dimension is fixed at two.

## Construction

For every integer \(k\ge1\), create vertices \(v_0=s,v_1,\ldots,v_k=t\). Between \(v_{i-1}\) and \(v_i\), provide two admissible operational choices with nonnegative two-resource charges

\[
a_i=(2^{i-1},0),\qquad b_i=(0,2^{i-1}).
\]

Every \(s\)-to-\(t\) path selects exactly one of \(a_i,b_i\) at each stage. Hence there are exactly \(2^k\) paths. For a subset \(S\subseteq\{1,\ldots,k\}\), choose \(a_i\) iff \(i\in S\). Its resource vector is

\[
p_S=\left(\sum_{i\in S}2^{i-1},\;\sum_{i\notin S}2^{i-1}\right).
\]

Let \(C_k=2^k-1\). Then every path vector has the form

\[
p_S=(x,C_k-x),\qquad x\in\{0,1,\ldots,C_k\}.
\]

Binary uniqueness makes all \(2^k\) vectors distinct.

## Theorem 352.1 — Exponential Pareto frontier in fixed dimension two

For the family above,

\[
|\mathcal P^*(s,t)|=2^k.
\]

### Proof

Take two distinct path vectors \(p=(x,C_k-x)\) and \(q=(y,C_k-y)\). If \(x<y\), then the first coordinate of \(p\) is smaller while its second coordinate is larger. Thus neither vector componentwise dominates the other. Since all \(2^k\) vectors are distinct, every path vector is Pareto minimal. Therefore \(|\mathcal P^*(s,t)|=2^k\). QED.

The graph uses \(k+1\) vertices and \(2k\) operational choices. Thus the explicit exact Pareto certificate can be exponential in graph size even for exactly two resources, a layered acyclic graph, nonnegative integer charges, and no information-dependent admissibility.

## Corollary 352.2 — Explicit-certificate lower bound

Any exact all-budget representation that explicitly enumerates every minimal feasible budget vector requires at least \(2^k\) vector records on this family. Therefore Audit 351's complete Pareto certificate is exact but not uniformly polynomial-size under explicit enumeration.

This is an output-size lower bound only. It does **not** imply that every implicit representation of the feasible-budget upper set requires exponential space. Indeed this particular constructed family has additional arithmetic structure and admits a compact generative description. No stronger representation lower bound is claimed.

## Corollary 352.3 — Scalar-threshold failure can be exponentially wide

Audit 351 proved that a single requirement vector exists iff \(|\mathcal P^*|=1\). Here \(|\mathcal P^*|=2^k\), so the failure of scalar/vector-single-threshold compression is not merely a two-point pathology: the antichain of minimal feasible budgets can grow exponentially while resource dimension remains fixed.

## Edge and invariance audit

- \(k=1\): frontier \(\{(0,1),(1,0)\}\); already non-singleton.
- Charges are nonnegative integers; no negative-cycle or cancellation issue occurs.
- The graph is a DAG, so every witness is finite and simple.
- Relabelling vertices or swapping the two resource coordinates preserves frontier cardinality.
- Adding a constant nonnegative vector common to every complete path translates the frontier and preserves its antichain structure.
- The construction is additive; therefore the blow-up does not depend on nonlinear resource aggregation.
- Dominance direction is minimization/componentwise budget consumption, matching Audit 351.
- Dimension is fixed at two for all \(k\); growth is not caused by increasing resource dimension.

## Prior-art collision classification

The mathematical mechanism is classical multiobjective shortest-path theory: exact Pareto sets can be exponentially large, motivating approximation and output-sensitive methods. Therefore **no novelty claim is made for the exponential Pareto-frontier fact itself**.

GC-II significance is architectural: Audit 350 found a complete scalar threshold in the one-resource additive model; Audit 351 replaced it by a Pareto antichain for vector resources; Audit 352 proves that the exact antichain certificate itself can have exponential output size already at two resources. A Paper-II breakthrough therefore cannot be claimed merely from Pareto accounting. The remaining target is a GC-specific structural restriction, semantic charge, dual certificate, or approximation theorem that compresses capability accounting without losing the operational distinctions GC-II intends to preserve.

## Next attack

Seek conditions stated in GC-II variables — resource increments, information increments, interface/action grounding, and rule structure — that provably bound Pareto width or permit a sound approximation. Separately test whether information-dependent admissibility destroys even the fixed feasible-upper-set geometry used by Audit 351.
