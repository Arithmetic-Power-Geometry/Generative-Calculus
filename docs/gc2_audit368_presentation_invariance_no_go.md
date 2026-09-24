# GC-II Audit 368 — Presentation-invariance no-go for raw generator-architecture metrics

## Question
Audit 367 leaves open a GC-native invariant computed from generator architecture rather than only from the terminal capability predicate. This audit tests a necessary condition: can a raw presentation metric lower-bound an operational quantity that is invariant under conservative refactoring?

## Operational boundary semantics
Let a finite operational presentation P have a distinguished boundary B and internal auxiliary states H. Write x =>_P y when y is reachable from x. Define its boundary semantics

S_B(P) = {(x,y) in B x B : x =>_P y}.

Two presentations P,Q are boundary-equivalent, P ≡_B Q, when S_B(P)=S_B(Q). Any operational quantity C that depends only on externally available boundary capabilities must satisfy P ≡_B Q => C(P)=C(Q).

## Conservative serial refinement
Take a primitive boundary transition s -> t. For any k >= 1 replace it by

s -> h_1 -> h_2 -> ... -> h_k -> t,

where h_i are fresh internal states inaccessible at the boundary. The refined presentation P_k has exactly the same boundary reachability relation as the original presentation P_0. Yet common raw architectural quantities change arbitrarily:

* number of generators increases by k;
* derivation/path depth increases by k;
* number of internal states increases by k;
* syntactic dependency-chain length increases by k.

The same argument works in reverse by contracting a semantically inert serial chain to a macro-generator whenever the operational language permits conservative macros.

## Theorem — presentation-invariance necessity
Let C be any boundary-semantic operational cost: P ≡_B Q implies C(P)=C(Q). Let M be a proposed structural quantity intended to satisfy a universal lower bound C(P) >= f(M(P)), where f is unbounded and nondecreasing. If M is unbounded on a single boundary-equivalence class, then no such bound can hold.

### Proof
Choose boundary-equivalent P_n with M(P_n) -> infinity. Boundary invariance gives C(P_n)=c for a fixed c. Unbounded monotone f gives f(M(P_n))>c for some n, contradicting C(P_n)>=f(M(P_n)). QED.

A dual statement holds for universal upper bounds if M can be driven arbitrarily downward within one equivalence class while C remains fixed.

## Concrete counterfamily
Let B={s,t}. P_0 contains one transition s->t. P_k replaces it by a chain through k fresh hidden states. For every k,

S_B(P_k)={(s,s),(t,t),(s,t)}

if reflexive reachability is used (or simply {(s,t)} under positive-length reachability). Thus every boundary-semantic capability quantity is constant across k, while generator count, hidden-state count and path depth diverge.

## Consequence for GC-II
A genuinely GC-native structural invariant cannot be merely a statistic of one chosen generator presentation. Before it can support a representation-independent capability-accounting theorem it must either:

1. be invariant under an explicitly declared class of conservative GC refactorings; or
2. be optimized over the equivalence class, e.g. M*(P)=inf{M(Q):Q ≡_B P}; or
3. make representation/implementation cost part of the operational semantics itself.

Option 2 immediately creates a new burden: computing the canonical/minimal presentation may collapse into established minimization, circuit, automata, grammar, database, CSP, or program-complexity problems. Therefore "computed from the presentation before solving the semantic problem" is not by itself enough.

## Collision / novelty status
The no-go mechanism is not claimed as novel. Representation dependence, conservative/definitional extension, state minimization, macro expansion and implementation-sensitive complexity are established themes across automata, logic, programming languages and complexity theory. The GC-II value is as a falsification filter on the surviving Audit-367 research route.

## Status
* Boundary-equivalence preservation under serial hidden-state refinement: **PROVED**.
* Raw generator count/depth/internal-state count as representation-independent lower bounds on boundary-semantic cost: **FALSIFIED**.
* Presentation-invariance necessity theorem: **PROVED** (elementary no-go).
* Mechanism as foundational novelty: **IMPORTED/KNOWN**.
* Quotient-invariant or equivalence-class-minimized GC structural invariant with a nonclassical operational lower bound: **OPEN**.

## Edge cases and checks
* k=0 recovers the primitive presentation.
* Positive-length versus reflexive reachability changes only diagonal pairs and does not affect the argument.
* Parallel unrelated transitions can be carried unchanged in every P_k.
* The theorem does not apply when internal latency, number of primitive steps, energy, memory, or implementation size is itself observable and charged; then P_k and P_0 need not be operationally equivalent.
* The result is a necessary-condition filter, not a claim that every quotient-invariant metric is useful or novel.

## Next target
Search for an invariant defined on a declared GC operational-equivalence quotient that remains computable/boundable from generator structure and yields a non-tautological lower bound after collision checks. In particular, distinguish semantic novelty from implementation cost explicitly rather than allowing hidden serial refinements to contaminate Omega_G.