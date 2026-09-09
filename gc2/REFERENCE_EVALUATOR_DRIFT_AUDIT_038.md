# GC-II Audit 038 — Reference Evaluator Drift Boundary

## Purpose

Audit 037 isolated evaluator drift: endogenous changes to the judging standard can manufacture apparent closure escape. This audit formalizes the cleanest reference-preserving correction and asks whether the resulting drift gap is itself a GC-II breakthrough.

## Status summary

- Reference-preserving certification principle: **PROVED** for the finite model below.
- Naive endogenous-evaluator gain as certified capability gain: **FALSIFIED**.
- Drift gap as a standalone GC-II novelty invariant: **FALSIFIED**; it reduces to ordinary disagreement between a fixed reference criterion and a manipulable/current criterion.
- Reward/evaluator tampering mechanism: **IMPORTED/KNOWN**.
- Contract/refinement preservation mechanism: **IMPORTED/KNOWN**.
- Stronger GC-specific residual: **OPEN**.

## 1. Model

Let `X` be a finite operational state space, `P_B(x)` the set of policies/histories admissible from `x` under vector budget `B`, and let

\[
E^*:P_B(x)\to\{0,1\}
\]

be a conserved reference evaluator. Let `Sigma` be a finite set of endogenous evaluator states and

\[
E_\sigma:P_B(x)\to\{0,1\}
\]

the current/generated evaluator. Operations may alter `x` and `sigma`, but not `E*`.

Define the existential capability indicators

\[
C^*(x;B)=\max_{p\in P_B(x)}E^*(p),
\qquad
C^{endo}(x,\sigma;B)=\max_{p\in P_B(x)}E_\sigma(p).
\]

Both are dimensionless Boolean quantities. Define the pointwise evaluator-disagreement set

\[
D_\sigma=\{p:E_\sigma(p)\ne E^*(p)\}.
\]

## 2. Proposition 038.1 — evaluator-only escape is not certified capability

Suppose an admissible zero-cost operation changes only `sigma` to `sigma'`, leaves the physical/epistemic state and admissible policy set unchanged, and

\[
C^{endo}(x,\sigma;B)=0,\qquad C^{endo}(x,\sigma';B)=1,
\]

while

\[
C^*(x;B)=0.
\]

Then the operation creates endogenous-evaluator closure escape but creates no reference-certified capability.

### Proof

The operation leaves `x`, `B`, and `P_B(x)` unchanged. Since `E*` is conserved, `C*(x;B)` is unchanged and remains zero. The change from zero to one occurs solely in `C^endo`, hence is evaluator-relative rather than reference-certified capability acquisition. QED.

This is the precise version of the Audit-037 degeneracy.

## 3. Proposition 038.2 — exact criterion for evaluator-only false positive

Under the same evaluator-only operation, a false positive occurs iff

\[
\exists p\in P_B(x): E_{\sigma'}(p)=1\land E^*(p)=0
\]

and no reference-accepted policy exists in `P_B(x)`.

Equivalently,

\[
P_B(x)\cap E_{\sigma'}^{-1}(1)\ne\varnothing,
\qquad
P_B(x)\cap (E^*)^{-1}(1)=\varnothing.
\]

This is a set-intersection criterion, not a new GC theorem mechanism.

## 4. Minimal exact witness

Let `X={bad,good}` and assume budget `B=0`, so no physical transition is available. The initial state is `bad`. Let

\[
E^*(p)=1 \iff \text{terminal state is good}.
\]

Initially `E_sigma=E*`. Add a zero-cost evaluator action `relax` changing the current evaluator to

\[
E_{relaxed}(p)=1 \quad\text{for every terminal state}.
\]

Before `relax`, both indicators are zero. After `relax`,

\[
C^{endo}=1,\qquad C^*=0.
\]

Thus naive closure escape reports gain with `Delta R=Delta I=Delta A=0` in the physical task, while reference-certified capability does not change.

## 5. Drift quantity and its failure as a novelty invariant

For Boolean existential capability define

\[
\Gamma_{drift}(x,\sigma;B)=C^{endo}(x,\sigma;B)-C^*(x;B)\in\{-1,0,1\}.
\]

Interpretation:

- `+1`: current evaluator reports capability absent under the reference;
- `0`: indicators agree;
- `-1`: current evaluator is stricter on the attainable set.

This quantity is dimensionally sound, but it is not a GC-specific invariant. It is simply disagreement of two predicates after optimization over the same feasible policy set. It can be represented as ordinary specification mismatch/reward-channel mismatch. Therefore `Gamma_drift` is **FALSIFIED as a standalone breakthrough object**.

A richer probabilistic version, e.g. the difference between optimal success probabilities under `E_sigma` and `E*`, has the same collision unless additional GC structure is essential.

## 6. Reference-preserving refinement

A sufficient no-false-positive condition is

\[
E_\sigma(p)\le E^*(p)\quad\forall p\in P_B(x),
\]

for every reachable `sigma`. Then

\[
C^{endo}(x,\sigma;B)\le C^*(x;B).
\]

Hence endogenous acceptance cannot certify a policy rejected by the reference evaluator.

Conversely, if this implication fails on an attainable policy, a false positive is possible whenever the attainable set contains that policy but no reference-accepted policy. Thus, relative to a fixed attainable set, refinement of the acceptance predicate is the exact structural guard against evaluator-relaxation false positives.

This is mathematically useful for GC-II bookkeeping but belongs to established specification/refinement logic rather than constituting novelty.

## 7. Collision checks

### Reward tampering / specification gaming

Existing reward-tampering work explicitly separates changes to the reward function from changes to its inputs and studies designs that prevent an agent from benefiting by manipulating the reward process. The minimal witness above is the deterministic predicate analogue of reward-function tampering. Therefore evaluator drift cannot be claimed as a new mechanism merely by renaming reward/specification as an operational evaluator.

### Contract and specification refinement

Assume-guarantee/contract refinement already treats preservation of a higher-level contract under decomposition/refinement as a formal proof obligation. The implication `E_sigma <= E*` is a particularly simple predicate-level refinement condition. Therefore reference preservation alone is also occupied mathematics.

### Robust control / constrained optimization

A fixed reference constraint plus evolving auxiliary constraints compiles to an ordinary constrained feasible set whenever all evaluators are explicit. No residual follows from conjunction alone.

## 8. Edge and composition checks

- If `E_sigma=E*`, `Gamma_drift=0`.
- If `P_B(x)` is empty, both existential indicators require an explicit convention; using `max empty = 0` makes the formulas consistent.
- Tightening an endogenous evaluator can yield `Gamma_drift=-1`; drift is not intrinsically nonnegative.
- Sequential evaluator changes can make `Gamma_drift` oscillate; it is not monotone without refinement assumptions.
- Under parallel composition, Boolean `Gamma_drift` is not additive. This is expected and prevents unjustified scalar capability accounting.
- If references themselves are allowed to change, the conserved benchmark disappears and Proposition 038.1 no longer identifies genuine acquisition. A higher-level immutable reference or an explicit reference-change cost is required.
- If the system can tamper with the inputs to `E*`, fixing the function is insufficient; the observation/evidence channel must also be reference-preserved. This directly collides with known reward-input tampering.

## 9. Consequence for Omega_G and No-Free-Capability

Any `Omega_G` based on measured closure escape must quotient out evaluator-only changes or report them on a separate axis. Otherwise a zero-cost relaxation yields positive apparent novelty and immediately falsifies No-Free-Capability.

A defensible certified escape event must minimally require

\[
C^*(x';B')>C^*(x;B)
\]

under a conserved evaluator and conserved evidence semantics, rather than merely `C^endo` increasing.

But this correction alone is imported/known. It is a hygiene condition, not the breakthrough.

## 10. Stronger surviving target

The next candidate should not ask whether the evaluator changed. Instead hold fixed:

1. the reference evaluator `E*`;
2. its evidence/observation semantics;
3. the ordinary augmented transition graph;
4. all action preconditions and costs;
5. all individual task feasibility judgments.

Then search for two systems differing only in the **joint provenance constraints on admissible evidence/capability certificates**: which resource-, information-, action-, and rule-generating histories are allowed to jointly justify several reference obligations. The desired witness would have identical ordinary reachable states and identical per-task success, yet different ability to produce a simultaneously valid, provenance-consistent whole-envelope certificate under the same budget.

This is only **OPEN**. It must be collision-tested against proof-carrying code, proof-carrying data, provenance semirings, information-flow security, certificates in optimization/verification, cryptographic proof systems, and compositional contracts. If it compiles to an ordinary certificate-state augmentation with no new quantitative consequence, it must be rejected.

## 11. Paper-II status

No breakthrough is claimed. Audit 038 decisively removes evaluator drift/reference preservation as a standalone novelty route while establishing a mandatory semantic guardrail: GC-II capability must be measured against a conserved reference evaluator and conserved evidence semantics, otherwise closure escape can be manufactured for free by moving the judging standard.
