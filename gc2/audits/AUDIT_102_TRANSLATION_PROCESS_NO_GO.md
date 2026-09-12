# GC-II Audit 102 — Translation-process obstruction no-go

## Scope
Branch-only Paper-II audit. GC-I foundations are not modified.

## Candidate attacked
After Audit 101, the surviving candidate was a joint typed lower bound on the process of translating between capability-equivalent presentations, after matching extensional semantics, ordinary information loss, realization size, and conventional descriptional complexity.

Let P,Q be presentation classes with the same extensional capability semantics on a family F. Let a translator T map a presentation p in P to an equivalent q=T(p) in Q. Attach typed implementation charges c(T,p)=(R,I,A,L).

## No-go proposition: embedding transfer
Assume there is an established translation model M and maps E_P,E_Q such that:

1. semantic equivalence is preserved by E_P,E_Q;
2. every admissible GC translator induces an M-translator between E_P(p) and E_Q(q);
3. the proposed GC resource coordinates are computable monotone functions of ordinary translation resources in M; and
4. the proof of a lower bound uses only properties preserved by this embedding.

Then any GC lower bound on translation cost obtained under these assumptions is a corollary of a lower bound in M. In particular, renaming ordinary description size, workspace, oracle/probe access, communication, or running time as R,I,A,L cannot establish a specifically generative theorem.

### Proof
Take any GC translator T. By (2), T induces an M translator T_M. By (3), a GC implementation violating the claimed bound would induce an M implementation violating the corresponding transported bound. Hence the GC bound is inherited from M. No additional generative obstruction has been established. QED.

## Collision check
The target collides with established descriptional/translation complexity. Meaning-preserving translations between equally expressive representation formalisms can require exponential, double-exponential, or even non-recursively bounded blow-up. Examples include regular-expression extensions to automata/regular expressions, logic-to-logic succinctness gaps, grammar descriptional complexity, and automata translations. Thus a large translation cost despite equal extensional semantics is not by itself novel.

## Stronger consequence
A proposed vector lower bound

    Phi(R,I,A,L) >= g(n)

is not protected from this collision merely because Phi is nonlinear or nonadditive. If the four coordinates are monotone re-encodings of standard resources and the proof transports through an established model, the theorem remains imported.

Likewise, requiring source and target presentations to have equal minimal realization size does not remove translation-complexity effects: translation difficulty may arise from representation syntax, determinization, normalization, compilation, verification, or construction complexity rather than from a new capability invariant.

## Status
- Embedding-transfer proposition: PROVED (conditional on explicit embedding assumptions).
- Translation cost as standalone GC-II novelty: FALSIFIED.
- Nonlinear typed relabeling of conventional translation resources: FALSIFIED as a novelty route.
- Breakthrough candidate surviving standard translation/descriptional complexity: OPEN.

## New surviving target
The next candidate must depend on an independently defined generative operation that changes the admissible operational universe itself, rather than merely translating two fixed equivalent descriptions. A defensible candidate would require all of the following:

1. source and target extensional closures fixed;
2. ordinary information-loss and representation-size invariants matched;
3. standard translation/compilation complexity controlled;
4. a formally specified endogenous admissibility update (the set of allowed future transformations changes as a consequence of the operation);
5. a theorem showing a quantitative closure consequence of that update that cannot be reproduced by compiling the update into ordinary state/process semantics without paying a proved additional cost.

This is OPEN. Before claiming novelty it must be collision-tested against self-modifying systems, reflective computation, dynamic games/MDPs, adaptive control, endogenous information acquisition, program synthesis, and resource theories with catalysts/side information.

## Kill test for the next audit
If the endogenous rule update can be compiled into an enlarged fixed transition system with polynomial/constant overhead while preserving the proposed typed charges, then it is not a GC-II breakthrough. The next audit should seek either (a) a rigorous lower bound on that compilation overhead under explicit restrictions, or (b) a proof that the candidate again collapses to established succinctness/translation theory.
