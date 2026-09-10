# GC-II Audit 061 — Counterfactual Coupling Equivalence Collision

Status date: 2026-09-11
Branch: `gc2-capability-accounting-lab`
Parent audit: 060

## Candidate

Audit 060 left a deliberately strong target: two finite explicit systems whose component closures, typed boundary-exchange traces, task/evaluator families, and coupling budgets agree under all allowed interventions up to some observational order, while their complete capability frontiers differ.

Define an intervention/test family T_k consisting of admissible experiments of interaction depth at most k. Write S ~=_k T when every test in T_k produces the same declared observation/cost outcome on S and T. A candidate distinguishing order is

    d(S,T) = min { k : S !~=_k T },

with d=infinity if no admissible finite test distinguishes them.

## Finite explicit theorem

For finite labelled transition systems with the complete conserved operational interface exposed, the sequence of depth-k observational equivalences is a descending partition refinement. If two initial states are not bisimilar, finite refinement eventually separates them; equivalently there exists a finite modal/test witness. Thus a finite pair can be indistinguishable at every bounded depth below d and differ at depth d, but this is ordinary finite-state behavioural equivalence/testing structure.

For deterministic finite automata the analogous k-equivalence refinement stabilizes after finitely many state partitions, and distinct minimal states admit finite distinguishing words. Hence growing distinguishing depth can be engineered by growing the state space, but the phenomenon is not by itself a GC-specific capability invariant.

Status: finite-state reduction PROVED/IMPORTED-KNOWN architecture.

## Collision

This candidate collides directly with established process semantics:

- trace, testing, simulation and bisimulation equivalences formalize indistinguishability under different observer powers;
- Hennessy-Milner style modal logics characterize bisimulation for image-finite/finite operational systems;
- bisimulation games and modern linear-time/branching-time spectroscopy construct distinguishing formulas/tests and measure the expressive resources needed to separate finite processes;
- contextual/testing equivalences already quantify over admissible observers/contexts, including systems whose interfaces evolve.

Therefore the statement "all lower-order interventions agree but a higher-order intervention distinguishes the systems" is not a novel GC-II mechanism unless GC contributes a physically typed quantity or theorem that cannot be represented as observer/test depth or ordinary behavioural equivalence.

## Exact kill condition

If the conserved GC operational model can be compiled to a finite labelled transition/game system and every allowed intervention corresponds to an observer/test/context over that system, then counterfactual coupling equivalence and its minimum distinguishing order reduce to behavioural testing/equivalence. In that domain they cannot establish a standalone Omega_G breakthrough.

## Edge checks

- If every finite-depth test agrees in a finite image-finite system under a bisimulation-characterizing test language, the states are behaviourally equivalent; no hidden finite-order breakthrough remains.
- If the observer language is deliberately restricted, separation after extending the language measures observer expressiveness, not automatically new physical capability.
- Hidden variables can create apparent separation only if the conserved interface permits an experiment that exposes their operational consequence; otherwise they are observationally irrelevant.
- Probabilistic systems require probability-aware trace/testing/bisimulation notions; adding randomness alone does not evade the collision.
- Infinite-state/non-image-finite systems may require infinitary logic or fail simple finite-depth characterizations, but infinitude alone is not novelty.
- Typed R,I,A,L costs can be attached to tests, but merely weighting a known distinguishing game does not establish a new theorem.

## Classification

- Counterfactual coupling equivalence as a definition: VALID.
- Finite minimum distinguishing depth: VALID and computable in finite models.
- Arbitrarily growing distinguishing depth with growing systems: VALID but IMPORTED/KNOWN mechanism.
- Higher-order intervention separation as standalone source of Omega_G: FALSIFIED for finite explicit systems.

## Surviving target

The next target must not be just *how many observational rounds are needed to tell systems apart*. A stronger possibility is a **translator-cost separation under conserved behavioural equivalence**:

1. S_n and T_n are behaviourally equivalent at the declared external interface (not merely k-equivalent);
2. both realize the same task/evaluator family and boundary traces;
3. converting an implementation/policy/controller for S_n into one for T_n while preserving typed budgets requires an additional physically declared resource whose lower bound grows with n;
4. the lower bound survives changes of representation and cannot be reduced to ordinary simulation overhead, communication complexity, state complexity, recompilation, or Kolmogorov description length.

This would connect directly to GC-I local-to-global projection irreducibility while avoiding the already-known observational-depth route. The immediate kill tests are bisimulation-up-to implementation, succinctness/state-complexity gaps, transducer synthesis, communication complexity, proof/knowledge compilation, and compiler invariance.

No breakthrough is claimed in this audit.