# Audit 030 — Aggregate-only capability-accounting bound impossibility

## Question
Can a representation-aware whole-envelope novelty/translator cost be universally upper-bounded only by aggregate augmentation coordinates

\[
\Omega_G \le F(\Delta R,\Delta I,\Delta A,\Delta L)
\]

without also conditioning on system size, structural complexity, or a representation model?

## Result
**No, for any representation-aware cost that includes exact translator description complexity.** The obstruction already appears with all four aggregate augmentation coordinates equal to zero.

Status: **PROVED boundary theorem; FALSIFIED as a universal aggregate-only bound.** The counting mechanism is **IMPORTED/KNOWN** from description/circuit/information-complexity arguments; it is not claimed as GC-II novelty.

## Fixed representation model
Fix a deterministic exact translator language/model `M` with binary program descriptions. A program denotes at most one total map on a fixed finite source set. Let

\[
K_M(f)=\min\{|p|:p\text{ exactly computes }f\}.
\]

No prefix-free assumption is needed for the elementary counting bound below.

Consider an operational world with `N` distinguishable source states and the same `N` target states. Give every state identical resource vector, information budget/cardinality, action/interface cardinality, and rule cardinality. Let admissible target transformations be arbitrary permutations `pi` of the `N` state identities, interpreted as exact whole-envelope relabelling/translation requirements. The transformation changes no aggregate R/I/A/L coordinate:

\[
\Delta R=\Delta I=\Delta A=\Delta L=0.
\]

The target requirement nevertheless specifies which of the `N!` exact permutations must be realized.

## Counting theorem
### Theorem 030.1
For every `N >= 2`, some permutation `pi` of `N` states satisfies

\[
K_M(\pi)\ge \lceil\log_2(N!)\rceil-1.
\]

### Proof
There are `N!` distinct permutations. The number of binary strings of length strictly less than `k` is

\[
1+2+\cdots+2^{k-1}=2^k-1.
\]

If every permutation had a program shorter than `k`, these strings would have to denote all `N!` distinct exact maps, requiring `2^k-1 >= N!`. Therefore whenever `2^k-1 < N!`, at least one permutation has description length at least `k`. Taking `k=ceil(log2(N!))-1` gives the stated asymptotic lower bound; more precisely one may choose the largest integer `k` satisfying `2^k-1<N!`. Hence the worst-case exact translator complexity is `Omega(N log N)` bits by Stirling's formula. QED.

## Corollary 030.2 — no size-independent aggregate-only upper bound
Suppose a representation-aware GC-II quantity contains `K_M` as a coordinate or dominates it monotonically. There is no finite function

\[
F(\Delta R,\Delta I,\Delta A,\Delta L)
\]

independent of `N` and `M` such that

\[
K_M(\pi)\le F(\Delta R,\Delta I,\Delta A,\Delta L)
\]

for every finite world and exact translator. Indeed all examples above have input `(0,0,0,0)`, while the worst-case lower bound diverges with `N`.

Thus any valid quantitative theorem for representation-aware `Omega_G^struct` must expose at least one additional conditioning variable: system size/state count, source/target description size, translator model, structural entropy/complexity, restricted translator class, or a comparable operational complexity parameter.

## Why this matters for the Paper-II program
This is stronger than Audit 014's order-sensitivity counterexample. Audit 014 showed equal aggregate increments can lead to different capabilities under noncommuting transformations. Audit 030 shows that even when **nothing changes in aggregate R/I/A/L at all**, exact whole-envelope translation complexity can grow without bound with system size.

Therefore the requested accounting law cannot be universal in the four aggregate deltas alone once structural/translator complexity is part of the capability gap.

A defensible replacement has the form

\[
\Omega_G^{\rm struct}\preceq
F(\Delta R,\Delta I,\Delta A,\Delta L;\,\Xi_M(X,Y)),
\]

where `preceq` is componentwise/Pareto comparison unless dimensions are normalized, and `Xi_M` is an explicitly declared structural-complexity parameter. The scientific target is then to make `Xi_M` operational and GC-essential rather than hiding arbitrary description complexity inside it.

## Edge and degeneracy audit
- `N=1`: one permutation; lower bound is zero. No contradiction.
- Identity permutation: may have constant description. The theorem is worst-case/existential, not universal over every permutation.
- Unlimited hard-coded lookup tables: still require representation length proportional to the encoded table unless the representation model grants the target permutation as a free primitive. Hence `M` must be fixed before comparison.
- Model dependence: exact constants vary with `M`; the unbounded counting separation persists for any fixed binary-description model capable of denoting all permutations.
- If state identities are declared operationally irrelevant and all permutations are quotient-equivalent, the witness collapses. Therefore the theorem applies only when the whole-envelope target distinguishes the translated identities/behaviors. This is a required semantic condition, not optional bookkeeping.
- If `F` is allowed to depend on `N` or source/target structural descriptions, the impossibility no longer applies. That is precisely the repair.
- Physical units: `K_M` is measured in bits and must not be added directly to physical resource coordinates without normalization. Pareto/vector accounting remains the safe primitive.

## Prior-art collision check
The proof mechanism is a standard counting/incompressibility argument and therefore **IMPORTED/KNOWN**. It is adjacent to circuit/description complexity and algorithmic-information reasoning. The result is useful as a negative theorem delimiting GC-II, not as a novelty claim.

Dynamic epistemic logic, action/resource logics, situation/action calculi, and resource theories also reinforce that resources, information, actions, and rules are not uniquely GC primitives. Consequently the surviving positive theorem must derive a quantitative surplus from a specifically declared joint operational structure, not from the mere coexistence of these axes.

## Status delta
- Universal `Omega_G <= F(Delta R,Delta I,Delta A,Delta L)` for representation-aware whole-envelope accounting: **FALSIFIED**.
- Counting lower bound on worst-case exact translator description: **PROVED / IMPORTED-KNOWN mechanism**.
- Pareto-valued `Omega_G^struct=(Delta R,Delta I,Delta A,Delta L,K_M,...)`: **OPEN as a useful GC-II construction**, dimensionally coherent as a vector.
- Positive GC-essential quantitative accounting theorem with an explicit structural parameter: **OPEN**.

## Next attack
1. Hold `N`, the unlabelled transition graph, and translator language `M` fixed.
2. Vary only GC semantic annotations and exact whole-envelope target requirements.
3. Search for pairs with identical low-order/taskwise summaries but different minimum translator complexity.
4. Require the separation to disappear under a declared semantic ablation and then collision-test the surviving mechanism against circuit complexity, communication complexity, CSP/database decomposability, simulation/refinement, epistemic planning, and resource theories.
5. Do not promote any separation caused solely by arbitrary target permutation incompressibility.