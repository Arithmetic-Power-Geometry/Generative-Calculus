# Audit 033 — Exact action–information substitution frontier

## Question
Can Audit 032's free auxiliary-information lower bound be replaced by an explicit acquisition mechanism, so that missing global capability may be supplied either by information or by newly available sensing interfaces/actions?

## Result
Yes, for the linear coset witness family. The frontier is exact. The result is **PROVED**, but its mechanism is linear algebra / zero-error information theory and therefore **IMPORTED/KNOWN mechanism**, not by itself the Paper-II breakthrough.

Let the hidden global world be a syndrome

\[
S\in \mathbb F_2^k,\qquad k=n-d,
\]

uniform over the `2^k` cosets from Audit 032. The protected local observations have zero information about `S`. An augmentation may add:

1. a selected family `J` of sensing interfaces/actions; interface `j` returns a deterministic linear measurement `q_j S`, where `q_j` is a row vector over `F_2`;
2. an auxiliary message `M` generated with knowledge of `S`.

Let `Q_J` be the matrix of selected measurement rows and let

\[
r(J)=\operatorname{rank}_{\mathbb F_2}(Q_J).
\]

Then every zero-error exact translator must satisfy

\[
\boxed{H(M)\ge k-r(J)\ \text{bits}.}
\]

Moreover the bound is tight: for every selected interface family `J`, there exists an auxiliary message of exactly `k-r(J)` bits that, together with the interface outcomes, reconstructs `S` exactly.

Thus the exact information/interface Pareto frontier for this witness is

\[
\boxed{\Delta I_{\min}(J)=k-r(J).}
\]

If each newly created independent binary interface is charged one unit on the action/interface axis, then any exact augmentation obeys

\[
\Delta I+r(J)\ge k,
\]

with equality achievable. This last scalar-looking expression is only a count in compatible binary degrees of freedom; it does **not** identify physical action cost with bits.

## Proof — lower bound
The complete selected interface outcome is

\[
Y_J=Q_JS.
\]

For uniform `S`, `Y_J` has entropy `r(J)` bits and each realized `Y_J=y` leaves exactly `2^{k-r(J)}` syndromes compatible. Therefore

\[
H(S\mid Y_J)=k-r(J).
\]

Zero-error recovery from `(Y_J,M)` requires

\[
H(S\mid Y_J,M)=0.
\]

Hence

\[
k-r(J)=H(S\mid Y_J)=I(S;M\mid Y_J)\le H(M\mid Y_J)\le H(M).
\]

So `H(M) >= k-r(J)`.

The same conclusion follows by counting: after the selected interface outcomes, each fiber contains `2^{k-r(J)}` possible worlds, and an exact auxiliary message must distinguish all of them.

## Proof — achievability
Extend a basis of the row space of `Q_J` to a basis of the dual vector space `(F_2^k)^*`. Let the additional `k-r(J)` basis rows form `R_J`. Define

\[
M=R_JS.
\]

The stacked matrix `[Q_J;R_J]` has rank `k`, so `(Y_J,M)` uniquely determines `S`. Since `M` consists of exactly `k-r(J)` binary coordinates and is uniform conditional on the appropriate complement, the lower bound is attained.

## Resource-cost refinement
Suppose each interface `j` has a nonnegative resource-cost vector

\[
c_j\in \mathbb R_+^m.
\]

For a selected family `J`, define

\[
C(J)=\sum_{j\in J}c_j.
\]

The exact attainable accounting points include

\[
\boxed{(C(J),\;k-r(J))}
\]

and the nondominated points form a resource–information Pareto frontier. Redundant interfaces with rows already in `span(Q_J)` increase `C(J)` without reducing the information requirement and are therefore dominated when all resource costs are nonnegative.

This is a precise non-additive-safe formulation: resource vectors remain resource vectors; information remains bits; the frontier uses partial order rather than adding unlike units.

## Closure-escape interpretation
Let the original operational closure contain only the protected `< d_perp` local queries from Audit 032. The global syndrome task is outside exact zero-error closure. After augmentation `(J,M)`, exact closure escape occurs iff

\[
\operatorname{rank}\begin{bmatrix}Q_J\\R_M\end{bmatrix}=k,
\]

where `R_M` denotes a linear auxiliary-message map in the linear subclass.

Within this subclass, the following are equivalent:

1. **Operational:** the syndrome task is exactly solvable after augmentation;
2. **Geometric/algebraic:** the augmented measurement map has zero-dimensional kernel;
3. **Computational:** Gaussian elimination returns rank `k` and yields a decoder.

This is a genuine three-way equivalence, but it is **IMPORTED/KNOWN mechanism** because it is simply exact identifiability of a linear system. It must not be advertised as the GC-II Closure-Escape breakthrough.

## No-free-capability corollary for the witness
If no new informative interface is added (`r(J)=0`) and no auxiliary information is supplied (`H(M)=0`), exact syndrome capability cannot appear for `k>0`.

More generally, if the selected interfaces have rank `r<k`, at least `k-r` auxiliary bits are necessary. Thus there is no free exact capability in this witness under the declared augmentation channels.

Classification: **PROVED / IMPORTED-KNOWN mechanism**. This is a controlled theorem, not a universal No-Free-Capability theorem.

## Edge and degeneracy checks
- `k=0`: one global world; frontier is `(0,0)` and all bounds vanish.
- `r(J)=0`: recovers Audit 032, `H(M)>=k`.
- `r(J)=k`: selected interfaces already identify the syndrome; zero auxiliary bits suffice.
- Duplicate or linearly dependent interfaces do not reduce the residual information requirement.
- Zero-cost informative interfaces can move the frontier at zero resource cost; this is not a contradiction but shows why interface availability/cost must be part of the operational model.
- Negative resource costs are excluded here; replenishing/generative actions require a path-dependent budget model rather than the static sum `C(J)`.
- Noisy interfaces are outside this exact theorem; rank must then be replaced by an appropriate zero-error/confusability or probabilistic information quantity.
- Approximate recovery is outside this exact theorem and needs a rate-distortion/Fano-type treatment.
- Nonuniform `S` changes `k-r(J)` into a conditional-information requirement and can destroy the simple rank formula.
- Adaptive linear queries do not beat `k` independent binary degrees of freedom in the zero-error worst case; however variable-cost adaptive policies can change the resource frontier and require a separate audit.
- If arbitrary nonlinear interfaces are allowed, rank is no longer complete; the correct primitive is the number/entropy of residual equivalence classes induced by the observations.

## Composition behavior
For independent blocks with syndromes `S_i in F_2^{k_i}` and block-separable interfaces, ranks and residual entropies add:

\[
H(S_1,\ldots,S_t\mid Y)=\sum_i(k_i-r_i).
\]

This is witness-family additivity only. Cross-block interfaces can change the rank decomposition, so no universal GC-II additivity is inferred.

## Prior-art collision
The proof is classical: linear measurements reduce uncertainty according to matrix rank; exact reconstruction is equivalent to full rank; weighted selection of informative linear measurements is closely related to matroid/basis optimization; sequential information acquisition and query-cost optimization are established topics. Therefore the mathematical frontier above is not claimed as novel GC mathematics.

The GC-II value of the audit is narrower and methodological: it supplies an exact finite-world benchmark in which two augmentation axes are substitutable without dimensionally adding them, and it gives a hard regression test for any proposed `Omega_G` or Closure-Escape theorem.

## Consequence for Omega_G
For this witness, a defensible novelty-gap object must retain at least the Pareto information

\[
\Omega_G \succeq_{\rm Pareto} \operatorname{Min}_{J}\{(C(J),\,k-r(J))\},
\]

under the declared interface library and resource costs. Any exact gap assigning zero cost to a point with `r(J)<k` and zero auxiliary information is falsified by the theorem.

This does **not** yet provide the desired four-axis universal bound `F(Delta R,Delta I,Delta A,Delta L)`.

## Status delta
- Explicit budgeted information-vs-interface substitution law: **PROVED** for the linear finite witness.
- Tight frontier `Delta I_min(J)=k-r(J)`: **PROVED**.
- Three-way operational/algebraic/computational closure-escape equivalence in the linear subclass: **PROVED / IMPORTED-KNOWN mechanism**.
- Witness-level no-free-capability corollary: **PROVED / IMPORTED-KNOWN mechanism**.
- Claim that this constitutes the Paper-II breakthrough: **REJECTED**.
- A genuinely GC-essential frontier requiring coupled changes in resources, information, interfaces/actions, and rules, with a quantitative surplus over neighboring theories: **OPEN**.

## Next attack
1. Generalize from fixed linear sensing interfaces to rule-gated interfaces whose availability depends on acquired information and residual resource budget.
2. Search exact finite worlds for **strict complementarity**: neither an information augmentation nor an interface/rule augmentation alone helps, while their combination causes closure escape.
3. Hold the unlabelled state graph fixed and enumerate all small rule-gated interface systems to isolate semantic interaction from generic graph complexity.
4. Define a dimensionless interaction witness only after declaring the operational deficit being measured; test whether it survives embeddings into decision-tree/query complexity, active sensing, communication complexity, resource theories, and epistemic/action logics.
5. Do not promote a candidate theorem until the same separation disappears under at least one essential GC-axis ablation and remains nontrivial after the strongest neighboring-theory reduction.
