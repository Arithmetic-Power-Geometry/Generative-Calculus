# GC-II Audit 067 — Path-Dependent Capability Hysteresis: Dichotomy No-Go

Status: **PROVED no-go for the generic candidate; IMPORTED/KNOWN collision; stronger target OPEN**

Date: 2026-09-11
Parent branch head inspected: `7156ecb79bd56de861dc14d62d4239126b138662` (Audit 066)

## 1. Candidate under attack

Audit 066 left open the possibility that two acquisition histories could end with equal task beliefs and equal endpoint budgets yet have different persistent future capability closures. Call histories `h` and `h'`, endpoint belief summary `b`, typed remaining budget `B=(R,I,A,L)`, and future capability closure `C^+(h,B)`.

The hoped-for signature was

`b(h)=b(h')`, `B(h)=B(h')`, but `C^+(h,B) != C^+(h',B)`.

This audit asks whether that signature can be representation-independent rather than an artifact of an insufficient endpoint state.

## 2. Operational predictive equivalence

Fix the admissible future intervention class `U`, future task/evaluator family `Q`, and cost/error semantics. Define

`h ~pred h'`

iff for every admissible future intervention policy `pi in U`, every finite future horizon, and every observable future event including task outcome and typed cost, the conditional outcome law after `h` equals that after `h'`.

This is deliberately representation-free: it is defined only by future operational experiments.

Define the predictive state `[h]pred` as the equivalence class of `h` under `~pred`.

## 3. Predictive-Closure Invariance Theorem

**Theorem (PROVED).** If `h ~pred h'` and the same future typed budget `B` is available, then

`C^+(h,B) = C^+(h',B)`.

**Proof.** Membership of a task point `(q,epsilon,B')` in the future closure is determined by existence of an admissible future policy whose observable task-error/cost law satisfies the evaluator and budget constraints. Predictive equivalence states that every such policy has the same future observable law from `h` and `h'`. Therefore every witness policy for membership from one history is a witness from the other, in both directions. QED.

No scalarization or additivity of `R,I,A,L` is used.

## 4. Hysteresis Dichotomy Corollary

**Corollary (PROVED).** Suppose two histories have equal reported belief and endpoint budget but different future capability closures. Then exactly the relevant conclusion is that the reported belief is not a sufficient operational endpoint state:

`C^+(h,B) != C^+(h',B)  =>  h !~pred h'`.

Hence some admissible future intervention/evaluator distinguishes the histories. The persistent difference is operational memory and belongs in the predictive state. Conversely, if no future admissible experiment distinguishes the histories, their future closures cannot differ.

This yields the no-go dichotomy:

1. **Future-distinguishable histories:** hysteresis is real, but the endpoint summary was incomplete; augment/quotient the state by predictive equivalence.
2. **Future-indistinguishable histories:** no capability-hysteresis difference exists for the declared operational task family.

Thus generic path dependence cannot by itself furnish a representation-independent `Omega_G`.

## 5. Relation to known theory

The result collides structurally with established sufficient-state constructions. In a POMDP, the belief state is a sufficient statistic for action-observation history when the model assumptions hold; predictive state representations likewise summarize history by predictions of future observable experiments. In non-Markovian quantum processes, process-tensor formalisms explicitly retain multi-time intervention memory. Therefore merely showing that a coarse endpoint variable misses history is not a new generative principle.

Important qualification: GC-II's typed physical costs and task/evaluator closure can still be useful bookkeeping, but they do not rescue novelty of the generic hysteresis mechanism.

## 6. Edge/degenerate-case audit

- `B=0`: theorem still holds; only zero-cost admissible policies are compared.
- Empty task family: both closures are trivially equal.
- Deterministic/stochastic systems: proof uses equality of observable future laws and covers both.
- Infinite histories: theorem is semantic; computability of the equivalence relation is a separate issue.
- Partial observability: absorbed into predictive equivalence; a coarse posterior is insufficient if it omits physically persistent latent variables relevant to future outcomes.
- Non-Markovian memory: does not violate the theorem; it makes predictive state richer.
- Nonlinear cross-resource costs: allowed because full typed cost outcome laws are compared.
- Re-encoding: invariant by construction because equivalence is operational, not syntactic.
- Composition: if the declared future experiment class includes composite interventions, the theorem applies to the composite predictive equivalence. Restricting interventions can merge states, but then capability is correspondingly relative to that restricted interface.

## 7. Status table

| Candidate/result | Status |
|---|---|
| Equal coarse belief + equal budget can coexist with different future capability | PROVED possible in principle, but indicates insufficient state |
| Predictive-Closure Invariance | PROVED |
| Hysteresis Dichotomy | PROVED |
| Generic path-dependent capability hysteresis as new `Omega_G` source | FALSIFIED |
| Belief/sufficient-state and predictive-state architecture | IMPORTED/KNOWN |
| Multi-time operational memory/process-tensor architecture | IMPORTED/KNOWN |
| Computable minimal predictive quotient with typed physical costs in unrestricted systems | OPEN |
| New quantitative law relating predictive-state complexity to unavoidable physical capability cost | OPEN |

## 8. Breakthrough consequence

The search must not continue by inventing another hidden history variable: the theorem will absorb any future-operationally relevant variable into predictive state. A surviving GC-II result must instead be a quantitative theorem **about the cost/complexity of realizing, maintaining, communicating, or reconstructing the minimal operational predictive state**, under explicit physical interfaces and typed budgets, with a lower bound not already equivalent to state complexity, sufficient statistics, communication/information complexity, predictive-state dimension/rank, process memory, or computational mechanics.

A precise next target is a **Predictive Realization Cost Gap**: among systems with the same external predictive process, characterize whether every physically admissible realization satisfying a fixed interface incurs a nonzero/growing Pareto cost in `(R,I,A,L)`, and determine whether any such bound survives minimal-realization, communication-complexity, thermodynamic-memory, and causal-state collisions.

## 9. Novelty discipline

This audit does **not** claim the predictive-equivalence theorem as historically novel; it is used as an internal no-go lemma. No breakthrough is declared. The next candidate remains OPEN until a theorem, counterexample search, exact finite experiment, and prior-art collision audit all survive.