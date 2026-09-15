# GC-II Audit 157 — Representation-independent compilation boundary

Status date: 2026-09-15
Branch: `gc2-capability-accounting-lab`
Parent inspected: `84e71649009d25e789e1c1c8043dc542cd54c249`

## Candidate under attack

Audit 156 left the following gate: seek a representation-independent lower bound on the minimum exact compiler from a succinct local/endogenous description to an operationally sufficient reflective representation.

## Result

**FALSIFIED as a generic novelty route.** A representation-independent lower bound cannot be stated without fixing at least (i) a source description class, (ii) a target representation/query class, and (iii) the operations/queries the compiled object must support. Once these are fixed, the proposed quantity becomes a standard succinctness / knowledge-compilation / data-structure / automata lower-bound problem.

Let `Sem(D)` be the operational semantics of description `D`, let `T` be an admissible target representation class, and let `Q` be the required exact query/operation family. Define

`K_{T,Q}(D) = min{|C| : C in T, C is Q-equivalent to Sem(D)}`.

This quantity is invariant under source re-encoding only when the minimization is over semantic equivalents, but it remains explicitly relative to `(T,Q)`. There is no nontrivial representation-independent scalar `K(Sem(D))` obtained by minimizing over unrestricted exact target languages: an unrestricted target may simply retain a succinct source description plus an interpreter, while tractability requirements reintroduce a target/query restriction.

Hence the dichotomy:

1. **Unrestricted target representation:** generic compilation blow-up is not forced; source + interpreter is an exact representation whenever the source semantics is effectively executable.
2. **Restricted target/query representation:** meaningful lower bounds exist, but they are language/query-relative and fall into established succinctness, knowledge compilation, automata, communication/cell-probe, or synthesis complexity.

## Proof note

Assume a source formalism `S` has an effective interpreter `U` for the required operational semantics. For description `D`, construct target object `C_D=(U,D)`. Then `C_D` exactly realizes `Sem(D)` and has size `|D|+|U|+O(1)`. Therefore no superlinear/exponential lower bound can hold uniformly over *all* exact target representations. Any stronger lower bound must prohibit this universal-interpreter representation by imposing target structure or required tractable operations. That restriction is precisely what makes the bound representation-class/query-relative.

## Prior-art collision

- Knowledge compilation explicitly studies transformations into restricted target languages, trading representation succinctness against supported tractable operations; modern 2025 work continues to compare compilation languages by succinctness and tractability.
- Known lower bounds show exponential intermediate or final compilation sizes for specified languages/algorithms, not for unrestricted semantic representations.
- Automata succinctness and communication-complexity reductions similarly establish lower bounds relative to particular machine models.
- Succinct data-structure/cell-probe lower bounds explicitly trade representation size against supported query cost.
- Functional synthesis complexity likewise depends on the specification and target/normal-form restrictions.

Fresh collision references checked in this audit:
- Nishino et al., AAAI 2025, “An And-Sum Circuit with Signed Edges That Is More Succinct than SDD”, DOI 10.1609/aaai.v39i14.33656.
- Illner, AAAI 2025, “New Compilation Languages Based on Restricted Weak Decomposability”, DOI 10.1609/aaai.v39i14.33643.
- de Colnet & Mengel, AAAI 2022, “Lower Bounds on Intermediate Results in Bottom-Up Knowledge Compilation”, DOI 10.1609/aaai.v36i5.20496.
- Göös, Kiefer & Yuan, ICALP 2022, “Lower Bounds for Unambiguous Automata via Communication Complexity”.
- Viola, SIAM J. Comput., “Bit-Probe Lower Bounds for Succinct Data Structures”, DOI 10.1137/090766619.
- Akshay et al., KR 2025, “Presburger Functional Synthesis: Complexity and Tractable Normal Forms”, DOI 10.24963/kr.2025/2.

## Status ledger

- Generic representation-independent exact compiler blow-up: **FALSIFIED** under effective executable source semantics and unrestricted exact targets.
- Universal-interpreter upper bound `|C_D| <= |D| + O(1)` for a fixed source formalism/interpreter: **PROVED under stated assumptions**.
- Restricted target/query compilation lower bounds: **IMPORTED/KNOWN** as a general mechanism.
- Treating target-relative succinctness alone as `Omega_G`: **FALSIFIED as independent GC-II novelty**.
- A GC-II invariant that is semantic yet nontrivial under unrestricted recodings: **OPEN**.

## Next surviving gate

Do not search for another representation-size scalar. Attack a different object: a **semantic intervention distance between capability closures**, defined through an explicitly fixed operational preorder/free-transformation class and then quotient by semantic equivalence. The candidate must produce a theorem not reducible to resource-theory conversion distance, simulation/alternating-simulation distance, directed deficiency, controller synthesis, or program/model repair. If all admissible interventions are fixed in advance, expect collision with resource theories/model repair; therefore test whether *constraints on admissible intervention generation* yield a genuinely new theorem rather than another representation artifact.
