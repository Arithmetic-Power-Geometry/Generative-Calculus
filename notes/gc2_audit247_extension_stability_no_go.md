# GC-II Audit 247 — Unrestricted endogenous extension destroys every nontrivial positive-gap value quotient

Status: PROVED boundary/no-go result; generic mechanism, no novelty claim.

## Setup
Let `(S,O,T,c,F)` be a finite nonnegative-cost operational system and

`V_F(x)=inf{C(pi): x -> F}`,

with `+infinity` for unreachable `F`. Consider an equivalence `E` intended to preserve exact capability cost not only in the current system but under every **conservative endogenous extension** that retains all old states/transitions and may add admissible operations.

Call the extension language **state-separating on positive-gap states** if for every distinct non-goal states `x,y` with equal positive value `V_F(x)=V_F(y)=v>0`, it permits a conservative extension adding a zero-cost operation `q_x` from `x` to some state of `F`, without adding that operation at `y`.

## Theorem 247.1 — extension-stability no-go
If the extension language is state-separating on positive-gap states, then no equivalence class containing two distinct equal-positive-gap states can preserve `V_F` under all conservative extensions.

### Proof
Assume distinct `x E y` with `V_F(x)=V_F(y)=v>0`. By state separation, extend conservatively with `q_x` of cost zero from `x` to `F`, unavailable at `y`. Then `V'_F(x)=0`. Since all old transitions are retained and no new transition is added at `y`, `V'_F(y)=v>0`. Hence `E` is not value preserving in the extension. QED.

## Corollary 247.2 — why a universal smaller signature cannot exist without restricting generation
Any GC-II proposal for a nontrivial quotient/signature that is claimed complete for **arbitrary** future rule/interface/action generation is false whenever the generative language can target members of one signature class differently. A nontrivial complete signature therefore requires at least one substantive restriction:

1. extension operations must be class-uniform/equivariant;
2. the signature must already encode every distinction on which future enabling/effects may depend; or
3. the claim must be scoped to a fixed operation language/model rather than arbitrary endogenous extension.

This is stronger than Audit 246's single witness: it is a general impossibility statement for every positive-gap class under a state-separating extension language.

## Edge cases
- `x=y`: theorem does not apply.
- `v=0`: a nonnegative-cost extension cannot lower the scalar value below zero, so scalar value alone cannot separate two zero-gap states; operational congruence may still distinguish them.
- `v=+infinity`: a zero-cost edge at `x` makes `V'_F(x)=0`; if the extension adds nothing reachable from `y`, `V'_F(y)=+infinity`, so the same argument applies provided the selective extension is isolated from `y`.
- Negative costs are excluded; otherwise shortest-path value may be ill behaved.
- If the operation language is class-uniform, the theorem's state-separation premise fails; nontrivial quotients may then be sound.

## Consequence for GC-II
The open target after Audits 245–246 must be narrowed. We should **not** search for a signature complete under unrestricted endogenous generation. The scientifically meaningful target is the coarsest congruence induced by a declared typed generator language `G=(R,I,A,L, preconditions, effects, costs)`, followed by a proof that GC structure makes that congruence smaller/computable relative to generic transition-system bisimulation. The restriction is not cosmetic: without it, nontrivial compression is impossible on positive-gap states.

## Collision check
The proof mechanism is elementary and aligns with established congruence/bisimulation and abstraction principles: an abstraction is stable only against observations/actions admitted by its language. Therefore the no-go is a GC-II boundary theorem, not claimed as new generic mathematics.

## Ledger
- unrestricted state-separating extension + nontrivial positive-gap value quotient: FALSIFIED.
- Theorem 247.1: PROVED.
- need to restrict the endogenous generator language for nontrivial extension-stable compression: PROVED under the stated completeness objective.
- generic congruence/bisimulation mechanism: IMPORTED/KNOWN.
- GC-specific typed generator language yielding a strictly smaller complete congruence than generic bisimulation: OPEN.
