# GC-II Audit 069 — Task-Relative Closure Deficiency and Duality Collision

Status date: 2026-09-11

## Verdict

**DECISIVE FALSIFICATION of the generic candidate from Audit 068.**

A task-relative closure deficiency together with an operational dual characterization is not, by itself, a GC-II breakthrough. In finite explicit models, once randomized mixtures are admissible and the performance/cost image is closed, the relevant achievable set is a compact convex set. Exact closure inclusion is then equivalent to a family of support-function inequalities. Approximate deficiency is a gauge/distance-to-inclusion problem whose dual witnesses follow from ordinary convex separation. In the statistical-experiment specialization this reduces to Blackwell/Le Cam randomization and deficiency; in channel/process specializations analogous simulability criteria and complete test/monotone families are already known.

This audit does **not** claim that every typed GC physical accounting model is a Le Cam experiment. It proves a narrower no-go: merely replacing scalar statistical loss by a finite task–scale–error–budget performance vector and then deriving a complete dual family does not establish novelty.

## 1. Finite operational object

Fix a finite task family Q, finite scale set S, finite admissible policy/augmentation family P, and an accounting model M. For each admissible implementation p define the vector

x(p) = (u_1(p),...,u_m(p), -c_1(p),...,-c_k(p)) in R^(m+k),

where u_i are bounded task-performance coordinates (equivalently negative errors) and c_j are typed charged coordinates such as R,I,A,L after choosing units **within each coordinate**. No addition of dimensionally unlike coordinates is assumed.

If randomized choice among implementations is admissible before the task instance is revealed, the achievable image is

K_G = cl conv{x(p): p admissible from G}.

For a finite explicit model K_G is compact. If randomization is not physically admissible, this convexification must not be performed; then the dual theorem below is not claimed.

## 2. Exact finite duality theorem

### Theorem 069-A — Support completeness for convex closure dominance

Let K_S,K_T be nonempty compact convex subsets of R^d. Then

K_T subseteq K_S

if and only if

h_T(w) <= h_S(w) for every w in R^d,

where h_K(w)=sup_{x in K} <w,x> is the support function.

**Status: PROVED / IMPORTED-KNOWN convex analysis.**

### Proof

The forward implication is immediate. Conversely, if y in K_T but y notin K_S, compact convexity of K_S and finite-dimensional strong separation give a w and alpha with <w,y> > alpha >= sup_{x in K_S}<w,x>. Hence h_T(w) >= <w,y> > h_S(w), contradicting the assumed inequalities. Therefore every y in K_T lies in K_S.

### Interpretation

Every failed finite convex closure inclusion has a scalar decision/test witness w. Thus a “complete dual family of task weights/monotones” is mathematically automatic after convexification; completeness alone cannot carry the GC-II novelty claim.

## 3. Approximate deficiency

For a norm ||.|| with unit ball B define the one-sided geometric deficiency

delta(K_T || K_S) = inf{eps >= 0 : K_T subseteq K_S + eps B}.

For compact convex sets,

delta(K_T || K_S)
 = sup_{||w||_* <= 1} [h_T(w)-h_S(w)]_+.

**Status: PROVED / IMPORTED-KNOWN convex duality.**

Reason: h_(K_S+eps B)(w)=h_S(w)+eps||w||_*; apply Theorem 069-A and minimize eps. This gives an exact operational witness family, but it is a support-function/Hausdorff-style construction, not a new generative theorem.

A typed Pareto augmentation vector Delta=(Delta R,Delta I,Delta A,Delta L) can be retained without scalar addition. For any nonnegative dual price vector lambda, scalarization <lambda,Delta> produces a supported Pareto witness. Unsupported points can occur without convexity; hence a universal finite scalar monotone list is not asserted.

## 4. Collision with Blackwell–Le Cam

When G is a statistical experiment, admissible conversion is a Markov kernel, tasks are bounded decision problems, and approximation is total variation/risk distortion, the preceding structure specializes to established experiment comparison. Blackwell comparison equates garbling/sufficiency with dominance over decision problems. Le Cam deficiency quantifies approximate simulation and is characterized through decision-risk loss/randomization criteria.

**Status: IMPORTED/KNOWN collision.**

Therefore the statement

“system S is within epsilon of T iff every bounded task loses at most epsilon (up to the loss-range normalization)” 

cannot be presented as a new GC-II theorem without additional structure not already captured by experiment/channel simulability.

## 5. Collision with process/channel/resource comparison

Allowed-transformations theories already study exact and approximate simulability and complete operational test/monotone families. In finite-dimensional channel/resource settings, comparison can be characterized by families of guessing/test quantities under specified free transformations. Consequently, changing the nouns from experiments/channels/resources to “capability closures” does not create novelty.

**Status: IMPORTED/KNOWN collision.**

## 6. Kill tests

1. **Degenerate task family.** If Q is empty or all utilities are constant, every system is equivalent. PASS: deficiency is zero; no novelty.
2. **Identical systems.** K_S=K_T gives delta=0. PASS.
3. **Strict inclusion.** K_T subset K_S gives one-sided delta(T||S)=0 but reverse deficiency may be positive. PASS; direction matters.
4. **Unit changes.** Rescaling one physical coordinate changes numerical scalarizations unless the dual price is contragrediently rescaled. Therefore no dimensionless universal scalar Omega follows automatically. PASS as warning.
5. **Nonconvex admissibility.** If random mixtures are forbidden, support functions characterize convex hulls, not original sets. The dual criterion can then falsely identify distinct nonconvex closures. DECISIVE boundary condition.
6. **Free hidden augmentation.** If a required interface/resource is omitted from M, deficiency can spuriously vanish. Accounting-boundary completeness remains an assumption, not a theorem.
7. **Composition.** Support functions are additive only for Minkowski sums. Coupled composition need not be a Minkowski sum; no general additive GC law follows.
8. **Monotonicity.** Enlarging the source achievable set cannot increase one-sided geometric deficiency. PASS.
9. **Symmetry.** Directed deficiency is intentionally asymmetric. Symmetrizing changes the operational question. PASS.
10. **Finite monotone list.** A finite list suffices only for special polyhedral descriptions; arbitrary compact convex sets generally require an infinite direction family. No generic finite complete family is obtained.

## 7. Consequence for Omega_G

The following candidate is **FALSIFIED AS STANDALONE NOVELTY**:

Omega_G = “minimum task-relative closure repair needed to simulate another system, with a complete dual family of operational witnesses.”

Why: in finite convex models the duality is generic separation/support geometry; in statistical specializations it is Le Cam/Blackwell; in broader process/resource settings simulability and complete operational witnesses are established themes.

This does not invalidate GC’s use of a deficiency quantity as an engineering diagnostic. It only removes it as the foundational breakthrough claim.

## 8. Surviving target — nonconvex physically indivisible closure obstruction

The next candidate must exploit structure destroyed by convexification rather than merely decorate convex deficiency. Define the **indivisibility defect**

Xi_G(S,T) = 1{ conv(K_S) dominates conv(K_T) but K_S does not operationally dominate K_T },

with a quantitative version measuring the minimum charged physical mechanism required to implement the missing randomization/mixing/coordination rather than granting convex mixtures for free.

This is only **OPEN**, not a breakthrough claim.

The required kill test is immediate: determine whether Xi_G is merely integrality gap / mixed-versus-pure strategy gap / randomized-versus-deterministic complexity / nonconvex resource theory / shared-randomness cost / correlation complexity. A surviving GC-II result would need a theorem tying this obstruction specifically to the complete task–scale–error–budget closure and showing a representation-independent physical lower bound that is not one of those known gaps.

## 9. Prior-art checkpoints used in this audit

- Blackwell comparison: decision dominance, informativeness and garbling/sufficiency are equivalent under the appropriate hypotheses.
- Le Cam deficiency: approximate simulation of statistical experiments by randomization and maximal decision-risk loss.
- Finite-dimensional channel comparison: approximate simulability admits operational test/guessing characterizations and, under allowed transformation sets, complete monotone families.
- Quantitative behavioural theories: pseudometrics already generalize exact behavioural equivalence to approximate comparison.
- Convex analysis: support functions and separation characterize compact convex inclusion.

No novelty claim is made for these imported ingredients.

## 10. Status ledger

- Budgeted operational closure: **PROVED/FORMALIZED in earlier audits; model-relative.**
- Generic task-relative closure deficiency: **VALID diagnostic, FALSIFIED as standalone novelty.**
- Finite convex support-function completeness: **PROVED / IMPORTED-KNOWN.**
- Approximate support-function deficiency formula: **PROVED / IMPORTED-KNOWN.**
- Universal finite monotone family: **OPEN in general and false without extra structure.**
- Dimensionless universal Omega_G from typed costs: **NOT ESTABLISHED.**
- Nonconvex physically indivisible closure obstruction Xi_G: **OPEN; next attack.**
- Main GC-I foundations: **UNCHANGED.**
