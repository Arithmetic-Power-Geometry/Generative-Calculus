# Audit 100 — Realization-Complexity Collision No-Go

## Question
After Audit 099 rules out a residual closure difference once complete typed process semantics is preserved, can GC-II obtain its Paper-II breakthrough merely from the size/complexity required to realize an equivalent semantics?

## Status
- Minimal deterministic exact realizer size = number of future/residual equivalence classes: **IMPORTED/KNOWN** (Myhill–Nerode family of results).
- Exponential exact-realizer family `L_n` below: **PROVED / exact construction**, but the mechanism is classical automata state complexity.
- Exact partition-refinement verification for `n=1..8`: **NUMERICALLY SUPPORTED / exact finite computation**.
- “Equivalent capability semantics may require a large finite-state realization” as standalone GC-II novelty: **FALSIFIED**.
- “Concise description -> exponentially larger exact operational realizer” as standalone GC-II novelty: **FALSIFIED / IMPORTED-KNOWN**.
- A genuinely typed lower bound on the *process of translation/construction* that is not reducible to automata/transducer/circuit/synthesis complexity: **OPEN**.

## Exact-realizer theorem boundary
Let an extensional finite-word capability specification be represented by a language `L subset Sigma*`. Define the standard future/residual equivalence

`u ~_L v  iff  for every w in Sigma*, uw in L <=> vw in L`.

For any deterministic exact finite-state realizer of `L`, two prefixes in different `~_L` classes must occupy different states: otherwise the shared state would force identical continuation behaviour and contradict the existence of a distinguishing suffix. Hence every exact deterministic realizer has at least `index(~_L)` states. The canonical quotient by `~_L` realizes `L` with exactly that many states when the index is finite.

Therefore, when GC-II “realization cost” is merely the number of deterministic semantic states required to preserve exact future capability, the lower bound is not a new GC theorem; it is the classical residual-state/minimal-automaton principle.

## Exponential witness family
For `n>=1`, define

`L_n = { w in {0,1}* : the n-th symbol from the end of w is 1 }`.

A deterministic exact realizer can store the last `n` input bits in an `n`-bit shift register, giving `2^n` states. These states are pairwise future-distinguishable: for two distinct `n`-bit suffixes `x != y`, choose a coordinate where they differ and append enough bits so that this coordinate becomes the `n`-th symbol from the end. Exactly one continuation is accepted. Hence all `2^n` suffix states lie in distinct residual classes.

Thus

`minimal_exact_states(L_n) = 2^n`.

This provides an exact exponential realization gap between a parameterized specification of size `O(n)` and its minimal deterministic operational realizer. The result is scientifically useful as a stress test but not GC-II novelty: exponential automata/synthesis blow-ups and residual-state lower bounds are established formal-language territory.

## Exact computation
`experiments/gc2_realization_complexity_collision.py` constructs the `2^n` suffix automaton for `L_n` and applies exact deterministic partition refinement. For `n=1..8`, the minimized state counts are

`2,4,8,16,32,64,128,256`,

matching `2^n` in every case. Results are written to `results/gc2_realization_complexity_collision.csv`.

This computation is not used as a substitute for proof. It is an executable finite check of the witness family and implementation.

## Dimension/domain checks
The state-count quantity is dimensionless. It should not be identified with any physical GC resource coordinate without an explicit implementation map. In particular, `log2(number of states)` may lower-bound bits needed by one encoding model, but that step requires representation assumptions and cannot silently be renamed `R`, `I`, `A`, or `L`.

## Edge and degenerate cases
- `n=1`: two residual states; the family already exhibits the theorem nontrivially.
- Unreachable states: excluded from the minimal-realizer statement.
- Nondeterministic realizers: the deterministic residual lower bound does not automatically transfer as a state-count lower bound; determinization can change size exponentially.
- Approximate semantics: residual equality must be replaced by a chosen approximate equivalence/metric and collisions with approximate automata/transducer theory rechecked.
- Infinite traces: finite-word Myhill–Nerode cannot simply be reused; canonical/minimal forms depend on the omega-automaton class.
- Weighted/stochastic semantics: exact state minimization requires the appropriate weighted/probabilistic equivalence, not the Boolean-language theorem by renaming.

## Composition/invariance checks
Renaming states does not affect the residual index. Adding unreachable states does not affect minimal exact-realizer size. Exact language-preserving quotients cannot identify distinct residual classes. Sequential composition of specifications can increase or decrease minimal state complexity; no additive law is assumed.

## Prior-art collision
The collision is decisive rather than cosmetic. Myhill–Nerode theory identifies the canonical minimal deterministic automaton through future/residual equivalence. Current automata-learning work still explicitly uses this canonical right-congruence construction. Weighted-automata minimization has corresponding morphism/minimal-quotient theory. Recent transducer work develops Myhill–Nerode-style minimization for restricted sequential transducer classes, and current synthesis literature continues to confront exponential or doubly-exponential operational realizations of compact temporal specifications.

Consequently, a GC-II theorem of the form

`same extensional capability + large minimal exact state representation => novelty`

fails the prior-art gate.

## Decisive consequence
Audit 099 moved the target from extensional closure to intensional realization. Audit 100 now removes the simplest intensional version: **minimal exact output representation size is already canonical automata/transducer/minimization territory**.

A surviving GC-II breakthrough candidate must charge something that is not merely the size of the minimal resulting machine. The strongest remaining target is a *typed translation-process obstruction*: two presentations with the same extensional semantics and comparable minimal realizers, but where every admissible translator/learner/verifier/synthesizer must incur a provable joint `(R,I,A,L)` cost or reversibility penalty that cannot be reproduced by ordinary state complexity, descriptional complexity, communication/streaming complexity, circuit complexity, or standard synthesis complexity.

That target remains **OPEN** and must not be claimed until an explicit model, lower bound, counterexample search, and prior-art collision audit are complete.
