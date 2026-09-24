# GC-II Audit 371 — Composition Alone Does Not Rescue Complete Monotones

## Scope

This audit continues Audit 370. It tests whether requiring complete convertibility monotones to respect parallel composition yields a GC-II-specific structure.

## Setup

Let X be the operational-equivalence quotient. Assume a parallel-composition operation ⊗ and identity e such that:

1. (X,⊗,e) is a commutative monoid.
2. The operational preorder ≼ is compatible with composition:
   x ≼ y implies x⊗z ≼ y⊗z for all z.

Then (X,≼,⊗,e) is a preordered commutative monoid.

A real-valued quantity m is an additive operational monotone when

m(e)=0,
m(x⊗y)=m(x)+m(y),
x≼y => m(x)≤m(y).

Equivalently, m is an order-preserving monoid homomorphism from X to (R,+,≤).

## Proposition 371.1 — Exact structural reduction

Under assumptions 1–2, demanding additivity of scalar complete monotones introduces no additional GC-specific algebraic object: every such monotone is precisely an order-preserving monoid homomorphism.

### Proof

The displayed normalization and additivity identities are exactly the identity-preserving and operation-preserving conditions for a monoid homomorphism. The last implication is exactly order preservation. Conversely, every order-preserving monoid homomorphism satisfies all three displayed conditions. QED.

Status: PROVED.

## Consequence

Composition compatibility plus additive monotones is an ordered/preordered-commutative-monoid formulation. Therefore additivity by itself cannot distinguish a GC-II theory from the established abstract resource-convertibility framework.

Status of “additivity rescues Audit 370 as a foundational novelty”: FALSIFIED.

## Important non-result

This audit does NOT prove that no GC-II compositional invariant exists. It excludes only the unrestricted additive route. A surviving candidate must contain structure not recoverable merely by declaring ⊗ and asking for additive order-preserving maps.

In particular, a future candidate interaction law

M(x⊗y)=M(x)+M(y)+J(x,y)

is scientifically meaningful only if J is independently defined from admissible GC operational structure, invariant under conservative presentation changes, and not merely the residual
J := M(x⊗y)-M(x)-M(y).

Otherwise the “interaction” is tautological.

## Edge and degeneration checks

- Identity: m(e)=0 is required; an arbitrary additive constant is incompatible with homomorphism normalization.
- Trivial preorder: the reduction still holds.
- Operational equivalence: quotienting is required if the intended quantity is semantic rather than presentation-sensitive.
- Noncommutative composition: outside the proposition; use ordered monoids rather than commutative ones.
- Partial composition: outside the proposition; requires a partial/algebraic operational structure.
- Catalysts: x⊗c ≼ y⊗c does not alter the algebraic reduction and therefore does not by itself create novelty.
- Nonadditive monotones: not excluded.
- Endogenous generation of interfaces/actions: not excluded.

## Collision classification

The algebraic mechanism belongs to established ordered-monoid/resource-theory mathematics. Accordingly:

- preordered commutative monoid reduction — PROVED / IMPORTED-KNOWN framework;
- additive order-preserving homomorphisms — IMPORTED/KNOWN;
- additive-complete-monotone route as GC-II breakthrough — FALSIFIED;
- independently computable, presentation-invariant, operationally forced nonadditive interaction/transport law — OPEN.

## Next attack

Construct the smallest finite budgeted operational systems in which two individually closure-internal components jointly generate a capability outside the product of their separate budgeted closures. Define any candidate interaction term before observing the joint terminal capability table; then adversarially test invariance under conservative generator refinements and collision with activation/catalysis/superactivation/contextuality/synergy notions.
