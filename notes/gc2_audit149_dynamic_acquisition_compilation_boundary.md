# GC-II Audit 149 — Dynamic Acquisition Grammar Compilation Boundary

## Candidate attacked
Audit 148 left open whether acquisition that changes what can subsequently be acquired or executed can escape ordinary decision-tree compilation.

## Operational model
Let W be a finite hidden-world set. At history h, the agent has an enabled query/action set E(h). Executing q in E(h) produces observation o and updates the future grammar E(hq o). Thus acquisition is allowed to create, destroy, or condition future acquisition interfaces.

For finite horizon H, define the information state B(h) as the set (or distribution, in a stochastic model) of hidden worlds compatible with h, together with every operational variable needed to determine E(h), costs, and transitions. The compiled state is z(h)=(B(h),E(h),r(h),h_eq), where h_eq is any finite sufficient history quotient required by the rules.

## Compilation theorem
If (i) hidden worlds and operational variables are finite, (ii) horizon is finite, (iii) the next observation law, enabled set, resource update and execution effects are determined by the current sufficient information state and selected action, then every dynamic-acquisition policy has an exactly behavior-equivalent contingent policy on the augmented information-state graph, and conversely.

Proof: map the empty history to its information state. Inductively, suppose a direct history h and compiled state z(h) agree. They expose exactly the same enabled actions by construction. For every enabled q and every possible observation o, both models apply the same observation/update rule, producing the same successor information state z(hqo). Induction through H establishes equality of admissible action-observation histories, terminal decisions, and additive path costs. Conversely, any policy on reachable compiled states defines a direct history policy by the same map.

Therefore changing the future query grammar is not, by itself, an irreducibility result. It becomes ordinary contingent planning / belief-state control after sufficient-state augmentation.

## Exact regression
`experiments/gc2_audit149_dynamic_acquisition_compilation.py` exhaustively enumerates a controlled binary family with two hidden worlds, two query names, binary answers, and answer-dependent future enabled-query masks. There are 16 answer maps and 256 grammar-update maps = 4,096 systems. Through horizon 3 it compared direct dynamic-grammar histories with augmented-state histories over 61,440 reached-history/state checks: 0 mismatches.

Frozen result: `experiments/results/gc2_audit149_dynamic_acquisition_compilation.json`.

## Edge cases
- Empty enabled set is represented as a dead-end state.
- Self-renewing, disabling, and newly enabling queries are included.
- Zero-information observations do not break compilation.
- Repeated queries are allowed whenever re-enabled.
- Deterministic finite models are exact; stochastic variants use belief distributions and the same sufficient-state argument.
- Infinite horizon does not invalidate state compilation when a sufficient Markov information state exists, but finiteness/computability questions can become nontrivial.
- If no finite/computable sufficient information state exists, this theorem does not establish a finite compiler; that is the surviving GC-II gate.

## Prior-art collision boundary
Contingent planning with sensing actions already treats action choice as history/observation dependent and is commonly translated to fully observable nondeterministic or belief-state planning. POMDPs and Bayes-adaptive POMDPs likewise augment state/belief to support simultaneous information acquisition and action. Active feature acquisition is also formulated as sequential partially observed control. Hence dynamic availability of queries/actions alone should not be claimed as GC-II novelty.

## Status ledger
- Finite dynamic-acquisition compilation theorem: **PROVED** under stated sufficient-state assumptions.
- Exhaustive finite regression: **PASS** (4,096 systems; 61,440 reached-history/state checks; 0 mismatches).
- 'Query changes future query grammar' alone as GC-II Closure-Escape: **FALSIFIED** for the stated finite sufficient-state class.
- Contingent/belief-state compilation mechanism: **IMPORTED/KNOWN**.
- Lower bound or impossibility for every finite/computable sufficient-state compiler: **OPEN**.
- GC-specific novelty gap surviving POMDP/contingent-planning/process-state augmentation: **OPEN**.

## Scientific consequence
The next viable target is no longer dynamic query availability itself. Paper II needs a family whose exact operational sufficient-state quotient provably grows superpolynomially/exponentially relative to the local description, or is not finitely/computably representable under the permitted compiler class, while the target capability remains succinctly specified. Any such result must then be collision-tested against automata minimization/Myhill-Nerode, communication and streaming lower bounds, POMDP belief-state complexity, planning, CSP/database width, and process equivalence before being treated as GC-II novelty.
