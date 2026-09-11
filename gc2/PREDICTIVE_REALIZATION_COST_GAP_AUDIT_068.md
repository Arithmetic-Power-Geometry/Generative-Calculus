# GC-II Audit 068 — Predictive Realization Cost Gap: Realization/Thermodynamic Collision

Status: **PROVED no-go for generic candidate; IMPORTED/KNOWN collision; stronger target OPEN**

Date: 2026-09-11
Parent branch head inspected: `e27cb701de4345d7bf6d8bcef5087f20f1ce49b1` (Audit 067)

## 1. Candidate under attack

Audit 067 left open a Predictive Realization Cost Gap: systems with the same external predictive process might require different or growing physical Pareto costs `(R,I,A,L)` to realize that process through a fixed interface.

The question is whether this is a new GC-II mechanism rather than ordinary minimal-realization complexity plus implementation physics.

## 2. Operational realization class

Fix an external predictive process `P`, admissible interface `J`, evaluator family `Q`, and implementation model `M`. Let `Real_M(P,J)` be all admissible physical realizations whose input-output intervention law equals `P` through `J`. For a realization `rho`, let

`c_M(rho) = (R(rho), I(rho), A(rho), L(rho))`.

Define the realization frontier

`Phi_M(P,J) = Min_Pareto { c_M(rho) : rho in Real_M(P,J) }`.

This definition is operationally meaningful but explicitly model-relative: physical units cannot be inferred from the external process alone.

## 3. Realization-Cost Underdetermination Theorem

**Theorem (PROVED).** There is no nontrivial universal physical realization-cost vector determined solely by an external predictive process `P` without specifying an implementation model and accounting boundary.

**Proof.** Hold `P` fixed. Construct two admissible implementation models that expose exactly the same interface law. In model `M1`, the required predictive state is supplied as a free primitive/lookup component; in model `M2`, the same state must be stored, reconstructed, communicated, or recomputed using charged physical operations. The observable process is identical, while the charged `(R,I,A,L)` vectors differ. Therefore no function of `P` alone can determine the physical cost vector. QED.

This is not a claim that costs are arbitrary once physics is fixed; it is a no-go against extracting physical accounting from predictive behavior alone.

## 4. Minimal-realization collision

Once an implementation class is fixed, the purely structural part of the problem collides with established realization theory. In linear systems, minimal realization order is characterized by Hankel rank; in finite-state/stochastic families analogous realization/minimization problems characterize minimal hidden/predictive representations. Thus a theorem saying only that a predictive process needs at least `d` internal degrees of freedom is a realization/state-complexity theorem, not a new generative law.

Accordingly:

`same external process + different nonminimal implementation sizes`

is not a representation-independent novelty signal. Quotienting by admissible minimal realizations removes arbitrary implementation padding.

## 5. Thermodynamic-memory collision

Adding energetic cost also does not automatically rescue novelty. Existing thermodynamics-of-prediction results relate stored nonpredictive information to dissipation under explicit physical assumptions. Thus a GC-II result of the form "useless predictive memory has energetic cost" collides with established information thermodynamics.

The important lesson is that physical cost requires an explicit physical model; once supplied, known thermodynamic lower bounds may already apply.

## 6. Exact no-go boundary

The generic candidate splits into two cases:

1. **Cost inferred from external predictive behavior alone.** FALSIFIED by implementation underdetermination.
2. **Cost evaluated inside a specified implementation/physics class.** VALID, but structural minima collide with realization theory and energetic minima can collide with information thermodynamics, communication complexity, memory lower bounds, or ordinary constrained optimization.

Therefore the generic Predictive Realization Cost Gap is not by itself a source of `Omega_G` novelty.

## 7. Edge and reduction audit

- Zero-cost primitives: demonstrate why the accounting boundary must be explicit.
- Re-encoding: arbitrary state-coordinate changes cannot change `P`; a valid physical bound must survive them.
- Nonminimal padding: cannot establish novelty; remove by Pareto minimization.
- Deterministic processes: same underdetermination argument applies.
- Stochastic processes: same argument applies to equality of conditional intervention laws.
- Infinite predictive state: may make realization nonfinite, but does not remove model dependence of physical cost.
- Composition: independent composition can share implementation resources; additivity must not be assumed.
- Catalysts/shared memory: must be included in the physical boundary or explicitly declared free.
- Landauer-style arguments: require specified thermodynamic operations and cannot convert abstract state count directly into universal joules.
- Communication lower bounds: if the implementation is distributed, ordinary cut/information/communication bounds remain immediate collision tests.

## 8. Status table

| Candidate/result | Status |
|---|---|
| `Phi_M(P,J)` as model-relative Pareto realization frontier | VALID definition |
| Physical cost determined by `P` alone | FALSIFIED |
| Realization-Cost Underdetermination Theorem | PROVED |
| Minimal predictive/state realization complexity | IMPORTED/KNOWN architecture |
| Nonpredictive-memory thermodynamic penalty | IMPORTED/KNOWN architecture |
| Generic Predictive Realization Cost Gap as new `Omega_G` source | FALSIFIED |
| Universal conversion from predictive dimension/rank to `(R,I,A,L)` | FALSIFIED without physical assumptions |
| Cross-model invariant capability cost beyond structural/thermodynamic minima | OPEN |

## 9. Stronger surviving target

The next candidate must compare **capability closure rather than realization size** while fixing the physical accounting boundary. A sharper target is a **Task-Relative Closure Deficiency** between two systems that implement the same declared predictive interface but differ in the least charged augmentation required to simulate each other's *entire task-conditioned closure* under composition.

Define provisionally

`D_G(S -> T | Q,J,M) = Min_Pareto { Delta : C_Q(T) subseteq C_Q(Augment_Delta(S)) }`.

The candidate is not novel merely because this is directed or asymmetric: it must survive directed deficiency/Le Cam comparison, simulation preorders, approximate bisimulation, resource conversion distances, communication simulation, and ordinary reachability. The potentially interesting question is whether a typed physical deficiency over a task-scale-error-budget closure admits a nontrivial operational dual characterization that is not reducible to those theories.

Status of this stronger target: **OPEN**.

## 10. Novelty discipline

No breakthrough is declared. Audit 068 removes another broad candidate and narrows the search. Any future theorem must specify the implementation model and accounting boundary, prove invariance under admissible re-encoding, distinguish structural realization complexity from physical cost, and pass prior-art collision tests before being promoted.