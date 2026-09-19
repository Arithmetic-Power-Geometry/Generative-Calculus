# GC-II Audit 246 — Goal-cost equivalence is exact for a fixed capability target, but not a dynamic congruence

Status: PROVED / IMPORTED-KNOWN boundary result; no novelty claim.

## Setup
Let a finite nonnegative-cost operational system be `(S,O,T,c,F)`, where `F` is the exact translator-capability set. Define

`V_F(x) = inf{ C(pi) : pi is an enabled finite execution from x to F }`,

with `V_F(x)=+infinity` if `F` is unreachable.

Define goal-cost equivalence

`x ~=_F y  iff  V_F(x)=V_F(y)`.

## Proposition 246.1 — coarsest scalar equivalence preserving the exact sequential gap
`~=_F` is the coarsest equivalence relation on `S` for which `Omega_seq(x,F)=V_F(x)` is constant on every equivalence class.

Proof: constancy is immediate from the definition. If an equivalence relation E preserves `V_F`, then `x E y` implies `V_F(x)=V_F(y)`, hence every E-class is contained in a `~=_F` class. QED.

This is deliberately a scalar preservation result, not a claim that the quotient preserves actions, plans, witnesses, typed accounting, or behavior under model extension.

## Proposition 246.2 — equal exact capability cost does not imply operational congruence
There exist finite states x,y with `V_F(x)=V_F(y)` but different enabled typed operations and nonmatching successors. Therefore `~=_F` need not be a bisimulation/congruence.

Minimal witness: x has only action a of cost 1 to goal; y has only action b of cost 1 to goal. Both have value 1, but enabled-action signatures differ.

## Proposition 246.3 — goal-cost equivalence is unstable under admissible extension
Take the witness above and conservatively add a new zero-cost operation q enabled only at x and leading to goal. Then the old states satisfy `V_F(x)=V_F(y)=1`, while in the extended system `V'_F(x)=0` and `V'_F(y)=1`.

Thus a quotient constructed only to preserve the current scalar novelty/capability cost can become unsound when GC-II enlarges rules/interfaces/actions. This is directly relevant to endogenous capability generation: future admissible transformations are part of the ontology, not merely an implementation detail.

## Consequence for the Paper-II program
There are now three distinct equivalence notions that must not be conflated:

1. static translator equivalence (Audit 244): preserves current translator feasibility/repair semantics;
2. fixed-target value equivalence (this audit): exactly preserves the scalar `Omega_seq` for the current operational system and target;
3. operational congruence (Audit 245): preserves enabled typed operations/costs and successor equivalence, hence supports sequential reasoning.

The first two are strictly too weak for unrestricted endogenous extension. Generic bisimulation/cost-preserving abstraction remains the prior-art baseline. Any GC-II novelty must therefore come from proving that the typed generative structure admits a *strictly smaller sufficient signature* than generic transition-system congruence, not from renaming value equivalence or bisimulation.

## Collision check
This audit intentionally collides with established shortest-path/value functions, planning abstractions, bisimulation, and cost-preserving behavioral equivalence. The scalar quotient theorem is elementary and IMPORTED/KNOWN in mechanism. No novelty claim is made.

## Ledger
- `~=_F` coarsest equivalence preserving the exact fixed-target scalar cost: PROVED.
- `~=_F` is an operational congruence in general: FALSIFIED.
- `~=_F` is stable under arbitrary additions of admissible operations/rules: FALSIFIED.
- cost-preserving bisimulation/abstraction mechanism: IMPORTED/KNOWN.
- GC-specific smaller signature complete for typed endogenous capability generation: OPEN.
