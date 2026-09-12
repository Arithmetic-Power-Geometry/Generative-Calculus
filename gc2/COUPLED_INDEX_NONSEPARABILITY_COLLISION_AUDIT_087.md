# GC-II Audit 087 — Coupled-Index Nonseparability Collision

## Question
Can irreducible coupling among task, scale, error, and typed budget indices provide the breakthrough invariant for Generative Calculus II?

## Status
**Standalone novelty claim: FALSIFIED.**

**Reason:** on a finite product index domain, arbitrary scalar response surfaces admit an exact hierarchical interaction decomposition. For convexified set-valued closure frontiers, the same statement applies to every support-function direction; the support-function family already determines the closed convex frontier. Thus the mere existence of nonseparable task–scale–error–budget interactions is representationally ordinary. A GC-II result must establish an additional operational law or lower bound that is not equivalent to standard interaction decomposition, multiobjective tradeoff geometry, or constrained information/resource optimization.

---

## 1. Product-domain closure response

Let

\[
D = Q\times S\times E\times B
\]

be a finite index domain, where \(Q\) is task, \(S\) scale, \(E\) error tolerance, and \(B\) a typed budget domain. Let a scalar operational value be

\[
v:D\to \mathbb R.
\]

Choose reference levels \(q_0,s_0,e_0,b_0\). By repeated finite differencing / Möbius inversion on the product lattice, \(v\) can be represented exactly as

\[
v = v_\varnothing
+v_Q+v_S+v_E+v_B
+v_{QS}+v_{QE}+\cdots
+v_{QSEB}.
\]

The highest-order term records whatever remains after all lower-order effects have been removed. Therefore

\[
\boxed{v_{QSEB}\neq 0}
\]

is evidence of four-way nonseparability, but not evidence of a new calculus or a new operational law.

The decomposition is exact and allows arbitrary nonlinear interaction magnitude and sign. No additivity assumption is imposed on the original response.

---

## 2. Exact Boolean-cube version

For binary indices \(x\in\{0,1\}^m\), write the response in the Walsh basis

\[
f(x)=\sum_{A\subseteq[m]}\widehat f(A)(-1)^{\sum_{i\in A}x_i}.
\]

The coefficient 

\[
\widehat f(A)=2^{-m}\sum_x f(x)(-1)^{\sum_{i\in A}x_i}
\]

is an exact interaction coordinate. Every function has a unique expansion. The maximum |A| with nonzero coefficient is an exact interaction order.

Consequently, a response may be completely invisible to all lower-order interaction terms while possessing a pure highest-order term; this is still standard higher-order interaction structure.

---

## 3. Set-valued closure and Pareto frontiers

Suppose the GC-II closure at index \(d\in D\) is a closed convex attainable cost/outcome set \(C(d)\subseteq\mathbb R^k\). For every dual direction \(w\in\mathbb R^k\), define the support function

\[
h_w(d)=h_{C(d)}(w)=\sup_{c\in C(d)} w\cdot c.
\]

Each \(h_w:D\to\mathbb R\) has the exact hierarchical interaction decomposition above. Further, a closed convex set is determined by its support function. Hence the entire convexified coupled closure surface is encoded by the family

\[
\{\widehat h_w(A):w\in\mathbb R^k,\ A\subseteq\{Q,S,E,B\}\}.
\]

Thus introducing a "coupling coefficient" or "interaction tensor" for task–scale–error–budget dependence does not by itself escape classical multivariate or convex-analytic representation.

For nonconvex attainable sets, scalar support functions lose nonconvex detail, but that does not create GC novelty: one must then retain a richer set representation or discrete Pareto structure. The novelty burden shifts to a theorem about operational generation, not merely the presence of coupling.

---

## 4. Exact exhaustive experiment

Executable:

`experiments/gc2_coupled_index_walsh_exhaustive.py`

Generated output:

`results/gc2_coupled_index_walsh_summary.csv`

The script enumerates every Boolean response

\[
f:\{0,1\}^4\to\{-1,+1\},
\]

so exactly \(2^{16}=65{,}536\) functions.

It computes all Walsh coefficients using integer arithmetic, reconstructs all 16 function values exactly, and records the maximum interaction degree.

Results:

| quantity | exact value |
|---|---:|
| functions enumerated | 65,536 |
| reconstruction failures | 0 |
| maximum degree 0 | 2 |
| maximum degree 1 | 8 |
| maximum degree 2 | 212 |
| maximum degree 3 | 12,648 |
| maximum degree 4 | 52,666 |
| pure full-order functions | 2 |

The two pure full-order functions are the parity/anti-parity pair in ±1 coding. They have no nonconstant lower-order Walsh coefficients but a nonzero four-way interaction.

Interpretation: strong irreducible finite coupling is common and exactly representable. The experiment is a consistency/falsification audit, not novelty evidence.

---

## 5. Prior-art collision

The candidate collides with several established architectures.

### Functional ANOVA / HDMR / Sobol-type decomposition
Multivariate functions are decomposed into main effects and interaction terms of increasing order. This is exactly the structural role proposed for a generic GC coupled-index interaction.

### Möbius inversion
On finite partially ordered domains, inclusion–exclusion / Möbius transforms provide exact interaction coordinates. Higher-order structure can therefore be represented without assuming pairwise or additive behavior.

### Information-theoretic tradeoff regions
Rate–distortion and multiterminal problems already use coupled feasible regions under multiple rate, distortion, action, and cost constraints. Nonseparable tradeoff geometry is ordinary in this literature.

### Multiobjective optimization
Typed budget vectors and Pareto frontiers already permit nonlinear and nonseparable tradeoff surfaces. A curved or interaction-rich frontier is not a new invariant by itself.

Representative collision sources checked in this audit include classical HDMR/Sobol decomposition, Möbius inversion on finite posets, multiterminal rate–distortion–cost regions, and recent exact functional-ANOVA decompositions of information-geometric quantities.

---

## 6. Domain, edge-case, and invariance audit

### Domain correctness
The finite decomposition theorem requires a finite product domain or, more generally, a basis/decomposition appropriate to the chosen measurable/function space. It does not justify the same finite formula on arbitrary infinite domains without additional assumptions.

### Degenerate coordinates
If one coordinate has only one admissible value, every interaction term containing that coordinate vanishes. This is expected and not pathological.

### Monotonicity
Interaction coefficients need not preserve monotonicity termwise even when the full response is monotone. Therefore sign of an interaction term alone is not an operational monotone.

### Reparameterization
Raw interaction coefficients depend on coding/basis/reference choice. Any proposed GC invariant based directly on them must prove invariance under admissible reparameterization. No such invariant is established here.

### Composition
Exact decomposition of a response surface does not imply a law for composing operational systems. Composition must be proved separately.

### Convexification
Support functions characterize closed convex sets, not arbitrary nonconvex sets. Therefore the support-function reduction is complete only after convexification or when convexity is independently justified.

### Units
Task and scale labels are indices, error may be dimensionless or task-specific, and \(R,I,A,L\) are typed quantities. Interaction coefficients across heterogeneous physical coordinates are not automatically dimensionally meaningful. A physical accounting law must remain typed or explicitly normalized.

---

## 7. Consequence for Omega_G

A proposal of the form

\[
\Omega_G = \left|v_{QSEB}\right|
\]

or any norm of an interaction tensor is not presently defensible as the GC-II novelty gap because:

1. it is basis/coding dependent unless additional structure is imposed;
2. it records ordinary high-order nonseparability;
3. it is not automatically an operational monotone;
4. it has no architecture-independent physical units;
5. it does not itself imply closure escape, no-free-capability, or a convertibility obstruction.

Accordingly, **coupled-index nonseparability is FALSIFIED as a standalone breakthrough source.**

---

## 8. Surviving target

The next viable target is not "interaction exists" but an **operationally invariant boundary-lift law** that survives exact hierarchical decomposition.

A candidate must produce something like:

\[
\Omega_G(S\to T)>0
\]

while remaining invariant under admissible recodings and while proving a concrete consequence for reachability, witness size, translator cost, or capability generation that cannot be recovered by applying standard optimization/comparison theory to an enlarged state description.

The most immediate next attack is **endogenous rule/grammar modification**: determine whether changing the admissible transformation grammar itself can always be compiled into an augmented fixed-rule state machine when the rule universe is finite/computable. If yes, that candidate should also be marked imported/known or falsified; if not, isolate exactly which assumption fails and whether the residue is operationally nontrivial.

Status of this surviving target: **OPEN**.

---

## 9. Classification

| item | status |
|---|---|
| finite hierarchical interaction decomposition | **IMPORTED/KNOWN** |
| exact Walsh representation on Boolean product domains | **PROVED / IMPORTED** |
| exhaustive 4-index reconstruction check | **NUMERICALLY/EXACTLY SUPPORTED** |
| existence of pure highest-order coupled functions | **PROVED / EXACTLY VERIFIED** |
| generic coupled-index nonseparability as GC-II breakthrough | **FALSIFIED** |
| support-family encoding of convex closure interactions | **IMPORTED/KNOWN** |
| operationally invariant residual beyond standard decomposition | **OPEN** |
| endogenous rule/grammar modification escape | **OPEN** |
