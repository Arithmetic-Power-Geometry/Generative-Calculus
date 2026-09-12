# GC-II Audit 101 — Translation-Irreversibility Collision

## Question
Can GC-II obtain its breakthrough by defining a reversibility gap for translating between capability-equivalent presentations?

## Candidate
For a deterministic translator f:X->Y, define the exact collision multiplicity

m(f)=max_y |f^{-1}(y)|

and the information-loss lower bound

Gamma_rev(f)=log2 m(f).

If a forward translation f is many-to-one and an exact inverse translator must recover the original x from f(x) plus an auxiliary record z, then any exact recovery code requires at least

log2 m(f)

bits in the worst case. Proof: choose an output y attaining multiplicity m(f). Its m(f) distinct preimages must receive distinct auxiliary records; therefore at least m(f) records are required.

For composition g∘f,

m(g∘f) <= m(g)m(f),

so

Gamma_rev(g∘f) <= Gamma_rev(g)+Gamma_rev(f).

Equality need not hold because the maximally colliding fibers need not align. Thus this quantity has a clean composition law but is not additive in general.

## Stress tests
- bijection: m=1 and Gamma_rev=0.
- constant map on N inputs: m=N and Gamma_rev=log2 N.
- injection followed by a lossy map: only the lossy stage contributes.
- degenerate one-point domain: Gamma_rev=0.
- units: bits; unlike R/I/A/L physical coordinates, no dimensionally invalid summation is required.
- relabeling invariance: domain/codomain bijections preserve fiber cardinalities.

## Novelty collision
This is not a GC-II breakthrough. The lower bound is a direct pigeonhole/information-loss result. More importantly, logical irreversibility and reversible embeddings are established subjects in reversible computation and Landauer-style information thermodynamics. Representation translation/compilation also has established lower-bound machinery in knowledge compilation, automata/transducer descriptional complexity, communication complexity, and synthesis.

Therefore a reversibility gap defined only by information discarded by a many-to-one translator is IMPORTED/KNOWN in mechanism, even if expressed in GC notation.

## Consequence for Omega_G
Do not define Omega_G as Gamma_rev or as an arbitrary weighted combination of Gamma_rev with R,I,A,L. Such a definition would rename established information-loss/translation complexity rather than prove a new capability-accounting law.

A surviving candidate would need an operational theorem in which two translations have the same extensional semantics and the same ordinary information-loss/descriptional-complexity profile, yet differ in an independently derived joint capability-accounting obstruction. That obstruction must survive reductions to reversible computation, knowledge compilation, automata/transducer succinctness, communication/streaming complexity, and synthesis.

## Status
- worst-case auxiliary-record bound >= log2 m(f): PROVED.
- composition subadditivity: PROVED.
- relabeling invariance: PROVED.
- Gamma_rev as standalone GC-II reversibility invariant novelty: FALSIFIED.
- generic many-to-one translation loss as breakthrough source: FALSIFIED / IMPORTED-KNOWN.
- stronger joint typed translation obstruction after ordinary translation complexity is matched: OPEN.

## Prior-art boundary checked in this audit
Reversible computation / Landauer information loss; knowledge-compilation lower bounds and communication-complexity reductions; automata/transducer realization and minimization; synthesis/representation blow-up. The audit deliberately makes no novelty claim beyond the proved elementary statements above.
