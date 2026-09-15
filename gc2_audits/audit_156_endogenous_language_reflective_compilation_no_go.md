# GC-II Audit 156 — Endogenous transformation-language compilation no-go

Status date: 2026-09-15
Branch scope: `gc2-capability-accounting-lab` only. GC-I/main unchanged.

## Candidate tested

Audit 155 left endogenous intervention semantics as a possible route: executing/acquiring a transformation may change the transformation language itself, so future admissible transformations are not fixed in advance.

Represent a configuration as

`z_t = (x_t, R_t, I_t, A_t, L_t, Lambda_t)`

where `x_t` is ordinary operational state, `(R_t,I_t,A_t,L_t)` are typed resources/information/interfaces/rules, and `Lambda_t` is the currently active transformation language (syntax/signature/rules or an effective code for them). An enabled meta-action `a_t` may change both ordinary state and the language:

`(x_{t+1}, R_{t+1}, I_{t+1}, A_{t+1}, L_{t+1}, Lambda_{t+1}) = F(z_t,a_t)`.

## Compilation theorem candidate

### Theorem (reflective-state compilation; conditional)

Suppose:

1. every reachable `Lambda_t` has a finite/effective representation `code(Lambda_t)`;
2. from the augmented state and candidate action, enabledness is computable;
3. successor ordinary state, typed quantities, and `code(Lambda_{t+1})` are computable;
4. capability acceptance/goal membership is determined from the augmented configuration (or a computable observation thereof).

Then endogenous modification of the transformation language can be represented as an ordinary transition system over augmented configurations

`Z = X x R x I x A x L x Codes(Lambda)`.

Proof: define one transition `z --a--> z'` exactly when the current encoded language admits `a` and the endogenous operational semantics computes successor `z'`. Every original execution induces the same augmented-state execution by induction on step number, and every augmented transition is admitted by the original semantics by construction. Thus reachability, traces, and any path cost included in the state/labels are preserved.

This is a representation/reduction theorem, not a claim that the compiled state space is finite or tractable.

## Edge cases and boundaries

- If the reachable language family is finite, the compilation is a finite augmented transition system.
- If it is countably infinite but effectively encoded, the compilation is an effective transition system; finite-state compilation is not implied.
- If enabledness or successor-language generation is noncomputable, assumption 2 or 3 fails. That may create a computability boundary, but noncomputability alone is not a GC novelty claim.
- If transformation semantics depends on an oracle/external process not represented in state, the state is not operationally sufficient; adding the oracle/interface state restores the reduction when that information is representable.
- Merely allowing a rule to rewrite itself therefore does not imply Closure-Escape.
- Description-size or complexity blow-up after compilation is a separate quantitative question and must be lower-bounded rather than inferred.

## Prior-art collision

Reflective Abstract State Machines explicitly place an updatable representation of the currently executed signature/rules inside the machine state and allow those rules to be changed during execution. Reflective programming and rewriting-logic systems likewise treat programs/rules as manipulable data. Planning-domain acquisition also learns action schemas/domain models from execution data. Therefore “actions can create/change the future action language” is not by itself an independent GC-II mechanism.

## Consequence for Omega_G

A candidate based only on endogenous language mutation reduces to ordinary reachability on the reflective augmented state under the assumptions above. Hence a nontrivial `Omega_G` cannot be defined simply as the amount of rule-language mutation.

A surviving quantitative direction must instead prove a lower bound on the *representation/translation burden* required to compile local endogenous descriptions into an operationally sufficient reflective state, while quotienting away arbitrary coding choices. Candidate quantity:

`Omega_repr(P) = inf_C cost(C)`

where `C` ranges over exact semantics-preserving compilers from the permitted local/endogenous representation class into a chosen operationally sufficient target class. This is only a research placeholder, not yet a novel invariant: it must survive Kolmogorov/description complexity, automata succinctness, knowledge compilation, communication/streaming complexity, reflective ASM simulation, and compiler lower-bound collisions.

## Ledger

- Endogenous transformation-language mutation alone implies non-compilability: FALSIFIED under effective sufficient-state assumptions.
- Reflective-state compilation theorem: PROVED under assumptions 1–4.
- Preservation of reachability/traces under the construction: PROVED by induction.
- Finite compiled state space: CONDITIONAL; only when the reachable augmented configuration family is finite.
- Reflective/self-modifying rule representation: IMPORTED/KNOWN.
- Planning-domain/action-schema acquisition: IMPORTED/KNOWN.
- A representation-independent lower bound on exact endogenous-to-operational compilation: OPEN.
- `Omega_repr` as a GC-II invariant: OPEN; no novelty claim.

## Breakthrough gate after Audit 156

Do not claim novelty from self-modification, meta-actions, rule creation, or a changing action alphabet alone. The next candidate must exhibit a family with a succinct permitted local/endogenous description for which every exact operationally sufficient compiler incurs a proved lower bound in a typed burden not removable by semantics-preserving recoding. The lower bound must then be compared directly with automata/state succinctness, knowledge compilation, communication and streaming complexity, reflective ASMs, algorithmic information, and program specialization/partial evaluation.