# GC-II Audit 039 — Provenance-Certificate Boundary

## Purpose

Audit 038 left open a stronger candidate: hold fixed the conserved reference evaluator, evidence semantics, ordinary transition graph, costs, preconditions, and individual task feasibility, then ask whether joint provenance constraints on evidence/capability certificates produce a genuinely GC-specific whole-envelope separation. This audit tests that candidate before treating provenance as a new GC-II primitive.

## Status summary

- Finite explicit provenance-certificate compilation: **PROVED**.
- Provenance-sensitive closure escape as a standalone GC-II novelty mechanism: **FALSIFIED** for finite explicit certificate semantics.
- Joint/alternative derivation algebra: **IMPORTED/KNOWN** from provenance semirings and related certificate/proof systems.
- Provenance constraints as useful GC-II bookkeeping: **PROVED useful but not novel**.
- Residual requiring non-compilable or quantitatively irreducible generative structure: **OPEN**.

## 1. Finite provenance-aware operational model

Let `X` be a finite operational state space and let `A` be a finite set of admissible actions. A transition

\[
x \xrightarrow{a,c} x'
\]

has vector resource cost `c`. Let `P` be a finite set of provenance atoms (sources, observations, actions, rules, authorities, or certified transformations). Let `K` be a finite certificate domain and

\[
\kappa:K\times A\times P^*\to K
\]

be an explicit certificate-update rule. The current certificate state is `k in K`. A reference obligation `q` is accepted by a conserved verifier

\[
V_q:X\times K\to\{0,1\}.
\]

The verifier is part of the reference semantics and is not modifiable by the system.

A provenance-aware run is therefore a sequence

\[
(x_0,k_0)\to(x_1,k_1)\to\cdots\to(x_t,k_t),
\]

where each `k_{i+1}` is obtained by the declared update rule from the previous certificate and the provenance atoms generated/consumed by the transition.

## 2. Theorem 039.1 — exact finite certificate-state compilation

For every finite explicit provenance-aware system above, define the augmented state space

\[
Z=X\times K.
\]

For each admissible provenance-aware transition from `(x,k)`, create the ordinary augmented transition

\[
(x,k)\xrightarrow{a,c}(x',k').
\]

Then there is a cost-preserving bijection between provenance-aware runs and runs of the augmented transition system. Moreover, for every reference obligation `q`, terminal acceptance is identical because `V_q(x,k)` is evaluated on the same pair.

### Proof

Induct on run length. Length zero is identical by construction. Assume prefixes through `(x_i,k_i)` correspond. Every provenance-aware next step has a uniquely declared successor physical state and certificate update `(x_{i+1},k_{i+1})`; the construction includes exactly that augmented edge with the same action label and vector cost. Conversely every augmented edge was introduced from a legal provenance-aware step. Thus runs correspond step-for-step, cumulative vector costs are equal, and terminal verifier values are identical. QED.

### Corollary 039.1a — closure escape preservation

For any budget vector `B` and any conjunction of reference obligations `Q`,

\[
\exists\text{ provenance-valid run within }B\text{ satisfying }Q
\]

iff

\[
\exists\text{ augmented-state run within }B\text{ reaching }\{(x,k):\forall q\in Q,\ V_q(x,k)=1\}.
\]

Hence finite explicit provenance-sensitive closure escape is ordinary budgeted reachability on `X x K`.

## 3. Minimal joint-provenance witness and why it does not establish novelty

Take two obligations `q1,q2`. Suppose the physical terminal state `x*` satisfies both task predicates, but the reference verifier requires a common provenance atom `p_auth` plus task-specific evidence `p1,p2`. Individually, histories can produce valid certificates for each task; jointly, the available histories may fail to produce a certificate containing all required dependencies under the same budget.

This creates a genuine whole-envelope certificate gap while leaving ordinary physical terminal states unchanged. However, once certificate state is explicit, the gap is simply reachability of an accepting subset of `X x K`. The mechanism is therefore not rescued merely by saying that the physical transition graph is fixed: provenance itself is operational state when it changes future acceptance.

This is a decisive semantic point for GC-II:

\[
\boxed{\text{hidden provenance constraint}\neq\text{new capability mechanism}}
\]

if the hidden constraint can be made explicit as finite verifier-relevant state without changing the observable predictions.

## 4. Collision with provenance algebra

Classical provenance semirings already distinguish alternative derivations from jointly required dependencies: semiring addition collects alternatives and multiplication combines joint dependencies. Polynomial provenance records which source facts participate in derivations, and homomorphic evaluations can map the same provenance object to Boolean validity, counts, trust, cost, access-control-like annotations, and other interpretations.

Therefore a proposed GC-II certificate algebra of the form

\[
\text{alternative derivation}=\oplus,\qquad
\text{joint dependency}=\otimes
\]

is occupied mathematics unless GC-II proves a new theorem that essentially requires additional generative structure and cannot be obtained by choosing an appropriate provenance/annotation semiring or augmented verifier state.

Recent semiring-semantics work further emphasizes that preservation behavior depends on the algebraic properties of the semiring. Thus simply discovering that one certificate algebra composes and another fails to preserve a property is also insufficient without a GC-essential residual.

## 5. Dimension/domain checks

Certificate state `k` is not itself a physical resource quantity. It must not be numerically added to resource vectors without a declared cost map. A certificate length, proof length, number of provenance atoms, or verification time may be measured, but each has its own units/domain.

If certificate acquisition consumes resources, define a vector cost on the generating actions. If certificate communication consumes bits, charge an information/communication coordinate explicitly. If verifier complexity matters, expose a computational resource coordinate or structural term rather than hiding it inside a dimensionless novelty score.

## 6. Edge and degenerate cases

- If `K` is a singleton, provenance has no operational effect and compilation reduces to `X`.
- If the verifier ignores `k`, provenance cannot change certified capability.
- If every physical history induces a unique certificate, certificate state is history compression; it remains compilable whenever the finite sufficient statistic is explicit.
- If two different certificates are verifier-equivalent for every future continuation, they should be quotiented; otherwise state size is artificially inflated.
- Zero-cost certificate rewrites are harmless only if they preserve every reference verifier. A rewrite that changes acceptance is an operational transition and cannot be treated as free relabeling.
- Parallel composition need not make certificate size additive: shared provenance atoms and alternative derivations create overlap. No scalar additivity assumption is justified.
- Randomized certificate generation does not change the exact finite-state compilation; probabilities can be carried on augmented transitions. Quantitative stochastic reachability then belongs to the corresponding probabilistic model.
- Cryptographic unforgeability is not captured by a purely extensional finite verifier unless computational assumptions/security parameters are modeled. Adding them may create computational lower bounds, but cryptographic proof/certificate complexity is established neighboring theory and is not automatically GC novelty.

## 7. Consequence for Omega_G

A candidate `Omega_G` that increases solely because a terminal state lacks an admissible provenance certificate is not intrinsically generative. In the finite explicit case it measures separation in an augmented reachability/certificate problem.

Accordingly, define no new scalar `Omega_G` from provenance in this audit. Doing so before identifying a residual would risk renaming known certificate complexity.

Any future nonzero GC novelty gap must survive the following compilation test:

1. augment state with every finite verifier-relevant provenance statistic;
2. preserve action labels, costs, budgets, reference evaluators, and evidence semantics;
3. allow standard provenance annotations/certificate predicates;
4. compare the resulting ordinary reachability/optimization problem;
5. reject the candidate if the claimed separation disappears or becomes a known certificate/proof/annotation complexity measure.

## 8. Consequence for No-Free-Capability

Provenance gives a useful hygiene theorem but not yet a new No-Free-Capability law. If a reference verifier requires a certificate and no admissible zero-cost transition can create a verifier-accepted certificate from the initial augmented state, then certified escape cannot occur at zero cost. This is ordinary reachability separation.

A genuinely stronger theorem would need to lower-bound required augmentation in GC primitive coordinates while proving that the bound is not merely proof length, communication complexity, cryptographic security, database provenance size, or augmented-state reachability.

## 9. Stronger surviving target: generative obligation closure over unbounded verifier-relevant structure

The finite-certificate route is closed. The next scientifically defensible target is not simply `more provenance`. It is to test whether GC's task-scale-error-budget envelope induces a **minimal sufficient operational quotient whose verifier-relevant state necessarily grows under generative composition**, and whether that growth has a quantitative lower bound not reducible to generic history/state complexity.

A concrete next protocol is:

- construct paired finite families with identical ordinary transition systems, costs, per-task feasibility, and all bounded-order provenance projections;
- let the number of jointly generated obligations grow with family size;
- compute the minimal verifier-congruence quotient (states equivalent iff every admissible future continuation gives identical reference-obligation outcomes);
- compare quotient growth against provenance-polynomial size, automaton/Myhill-Nerode state complexity, communication complexity, CSP/database width, and circuit/proof complexity;
- only if a residual remains, attempt a theorem linking that residual to a GC-specific `Omega_G` or translator lower bound.

The key quantity should be the **minimal operational sufficient state**, not an arbitrarily chosen certificate representation. Otherwise representation blow-up can be manufactured by encoding choices.

## 10. Novelty gate after Audit 039

A future candidate survives only if all are true:

1. **GC-essentiality:** removing a declared GC semantic ingredient destroys the theorem/witness.
2. **Minimal-state robustness:** the separation survives quotienting by future operational equivalence.
3. **Compilation robustness:** finite provenance/certificate augmentation does not remove the separation.
4. **Neighbor robustness:** the quantitative conclusion is not a direct theorem of provenance semirings, automata/state complexity, proof/certificate complexity, communication complexity, reachability, resource theories, or constrained optimization.
5. **Parametric consequence:** there is a nonconstant family-level bound or exact criterion, not only a renamed feasibility predicate.
6. **Reproducibility:** exhaustive finite instances and adversarial collision searches agree with the claimed domain.

## 11. Paper-II status

No breakthrough is claimed. Audit 039 decisively removes finite provenance-constrained certification as a standalone novelty route. Provenance remains useful as a mandatory certification layer, but in finite explicit systems it compiles exactly into ordinary augmented-state reachability and its joint/alternative derivation structure substantially overlaps established provenance algebra.

The next attack should compute minimal verifier-congruence quotients for controlled generative families and search for a GC-essential growth law after quotienting away representational artifacts.