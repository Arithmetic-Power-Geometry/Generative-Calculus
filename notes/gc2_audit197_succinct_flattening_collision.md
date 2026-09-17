# GC-II Audit 197 — Succinct-flattening gap collision

## Question
After Audit 196, can GC-II obtain a distinctive quantitative Closure-Escape theorem by proving that a compact reflective/generative operational description must expand enormously when flattened into an explicit admissibility transition system?

## Candidate family
For n >= 1, let complete configurations be n-bit words z in {0,1}^n. A compact transition generator is a Boolean circuit C_n(z,z') deciding whether the labelled transition z -> z' is admissible. Its description size may be poly(n), while the explicit flattened transition system has 2^n states and potentially exponentially many edges.

Define the explicit-flattening ratio

    Phi_exp(C_n) = |LTS_exp(C_n)| / |C_n|,

where the numerator is the size of an explicitly enumerated state/edge representation and the denominator is the bit size of the circuit description.

## Proposition — exponential explicit flattening is immediate but non-diagnostic
There are uniform families with |C_n| = poly(n) and 2^n reachable configurations. Therefore every explicit state enumeration requires at least 2^n state records, so Phi_exp is exponential up to polynomial factors.

Proof: take C_n to encode the n-bit increment transition z' = z+1 mod 2^n. The circuit is polynomial size, every one of the 2^n configurations is reachable from 0^n, and an explicit transition system preserving the distinct configurations must list at least 2^n states. QED.

## Why this does not survive the novelty gate
The separation is a representation-succinctness phenomenon, not a generative-calculus-specific capability law. Succinct graph representations classically encode exponentially large graphs by small circuits/decision diagrams; complexity can rise sharply when standard graph problems are posed on those succinct encodings. Automata/logical formalisms likewise have classical exponential and double-exponential succinctness separations. Therefore an explicit-flattening lower bound, even exponential, cannot by itself serve as Omega_G or a GC-II Closure-Escape theorem.

More strongly, if the target representation class is allowed to retain a universal interpreter/circuit predicate for the transition relation, the exponential state-table blow-up disappears at the description level. Thus the lower bound is representation-class dependent. Any invariant claiming intrinsic generative novelty from Phi_exp fails invariance under admissible changes of representation.

## Consequence for No-Free-Capability
A theorem of the form

    new closure => large explicit flattened representation

is false as an intrinsic resource law: the same closure can have a small intensional/circuit representation and a huge extensional table. Representation size is not itself acquired operational capability.

A defensible quantitative theorem must instead charge a representation-independent operational obligation (for example communication, observations, irreversible resource consumption, or certified distinctions) that every realization must pay, while conditioning on the same task-scale-error-budget interface. Merely requiring explicit enumeration bakes the lower bound into the chosen target syntax.

## Edge and reduction checks
- n=0: one configuration; no asymptotic gap.
- Reachability: the increment family reaches every configuration, preventing removal of unreachable states from the explicit representation.
- Composition: repeated application of the same compact transition generator traverses the entire cycle; no new rule description is required per step.
- Relabelling: explicit state count is unchanged, while circuit size can vary with encoding, reinforcing representation dependence.
- Semantics: compact and explicit systems have identical one-step relation and path closure.
- Budget dimensions: Phi_exp is dimensionless only after choosing concrete encoding-size units; it is not an operational resource quantity.

## Status ledger
- Exponential compact-circuit versus explicit-LTS flattening family: **PROVED**.
- Explicit flattening ratio as intrinsic GC-II novelty invariant: **FALSIFIED**.
- Succinct-representation blow-up mechanism: **IMPORTED/KNOWN**.
- Representation-independent lower bound for generating a capability under matched task-scale-error-budget interfaces: **OPEN**.

## Prior-art collision
Classical succinct graph work studies graphs represented by circuits/OBDDs and reports exponential complexity blow-ups relative to explicit representations. Classical automata theory contains exponential and double-exponential succinctness gaps between equivalent acceptance formalisms. These are direct collisions with the proposed compact-versus-flat separation.

## Next gate
Stop treating explicit state-space size as capability cost. Search for pairs of systems with matched extensional closure and matched compact-description complexity but provably different minimum *operational acquisition cost* under the same interface and error budget. A surviving Omega_G must separate acquisition/generation from mere representation succinctness and must remain invariant when both sides are compiled through polynomial-overhead universal interpreters.