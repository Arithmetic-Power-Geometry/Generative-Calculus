# GC-II Audit 062 — Translator-Cost Separation Collision

Status date: 2026-09-11
Branch: `gc2-capability-accounting-lab`
Parent audit: 061

## Candidate attacked

Audit 061 left the following stronger target. Seek behaviourally equivalent systems S_n,T_n with the same declared task/evaluator family and external traces, but for which translating an implementation/controller from one realization formalism to the other while preserving typed R,I,A,L budgets requires an additional resource growing with n.

A natural candidate translator gap is

    Tau_K(S -> T) = inf { c_K(Phi) : Phi translates admissible S-implementations to T-implementations preserving declared behaviour },

where K is a physically declared cost coordinate or typed cost vector and Phi ranges only over admissible translators.

## Kill theorem for extensional finite-state behaviour

Suppose the declared behaviour is a regular input/output or acceptance behaviour and the target implementation class is deterministic finite state. Behavioural equivalence fixes a canonical residual equivalence: histories u,v are identified exactly when no future continuation distinguishes their declared behaviour. The quotient classes are the states of the unique minimal deterministic realization up to isomorphism (the Myhill-Nerode/minimal-machine architecture).

Therefore any lower bound that is only the number of states, transitions, bits, or description objects required when converting an equivalent representation to a deterministic finite-state realization is a representation/state-complexity lower bound. It is not a new GC invariant. In particular, exponential or larger blowups between nondeterministic/alternating/succinct and deterministic representations can occur while the external language/behaviour remains exactly the same; such blowups belong to established descriptional/state complexity.

Status: PROVED reduction for the stated finite extensional domain; collision IMPORTED/KNOWN.

## Why adding typed cost does not automatically escape

Writing a state blowup as Delta R, a communication transcript as Delta I, controller actions as Delta A, or installed rules as Delta L does not change the mathematical source of the lower bound. A GC-specific translator theorem requires the lower bound to be invariant under the declared physical equivalences and to depend on a conserved operational restriction not removable by choosing another representation formalism.

If arbitrary semantics-preserving encodings are allowed, Audit 053 already blocks exact nontrivial compiler-invariant structural/execution cost. If the encoding/implementation class is restricted, then the restriction itself must be physically justified; otherwise Tau_K measures the chosen representation language.

## Edge and degeneracy checks

- Equivalent minimal deterministic realizations: Tau based purely on state count vanishes up to isomorphism; no separation remains.
- NFA/AFA/succinct -> DFA: potentially large translator blowup exists, but this is standard state/description complexity.
- Same behaviour but different hardware energy/time: a positive physical gap can exist, but without a representation-independent admissibility law it is implementation engineering, not yet a universal GC theorem.
- Communication-limited distributed realization: lower bounds may become physical, but communication complexity already supplies representation-robust lower-bound methods for functions/protocols; collision must be tested there.
- Hidden internal state with no effect on any declared task/evaluator is operationally irrelevant and cannot support Omega_G.
- If a new evaluator is introduced solely to reveal the hidden state, the task family changed and behavioural equivalence was not conserved.

## Classification

- Translator cost as a typed operational definition: VALID.
- Growing conversion cost between equivalent finite representations: VALID.
- State/description blowup as standalone GC-II novelty: FALSIFIED.
- Universal exact translator cost invariant under arbitrary semantics-preserving representation: FALSIFIED by Audit 053 architecture.
- Physically restricted, representation-robust translator lower bound: OPEN.

## Surviving target: conserved bottleneck translator theorem

The next candidate must pin the translator to an explicit physical cut rather than to a representation language. Consider a distributed realization split by a conserved interface B. The two sides may perform arbitrary free local computation, but every cross-boundary symbol, bit, qubit, action, energy token, or installed rule is charged in its own declared coordinate. Seek a task family Q_n for which:

1. two realizations are extensionally equivalent on Q_n;
2. arbitrary local recompilation/state expansion is free, so ordinary state/succinctness complexity cannot create the bound;
3. any admissible translator/controller preserving Q_n must transmit or instantiate a boundary certificate of cost at least g(n);
4. an explicit construction achieves the same order, making the bound operationally tight;
5. the lower bound remains after representation changes because it is proved from distinguishable cross-boundary task instances, not code length;
6. the resulting quantity is then collision-tested against deterministic/randomized/quantum communication complexity, information complexity, network coding, distributed synthesis, and cut-set bounds.

The crucial kill-first question is severe: if the conserved bottleneck theorem is exactly a communication-complexity or cut-set lower bound under renamed GC coordinates, it is IMPORTED/KNOWN. GC-II survives only if simultaneous task-scale-error-budget closure imposes a new cross-coordinate law that is not obtainable by applying those established bounds coordinatewise.

No breakthrough is claimed in this audit.