# GC-II Audit 376 — Task-advantage novelty-gap collision

**Scope.** GC-II branch only. GC-I foundations on `main` are unchanged.

## Candidate

For a fixed budget (b), let (B_b) and (A_b) denote baseline and augmented attainable outcome sets. For a normalized task family (mathcal T), with task payoff (u_t), the most natural operational novelty gap is

[
\Omega_{\mathcal T}(A_b,B_b)
=
\sup_{t\in\mathcal T}
\left[
\sup_{a\in A_b}u_t(a)-\sup_{x\in B_b}u_t(x)
\right]_+ .
]

For linear tasks (u_w(x)=\langle w,x\rangle) on a finite-dimensional outcome embedding and a compact normalized witness set (W),

[
\Omega_W(A,B)=\sup_{w\in W}[h_A(w)-h_B(w)]_+,
]

where (h_C(w)=\sup_{x\in C}\langle w,x\rangle) is the support function.

## Exact finite-dimensional facts

Assume nonempty compact attainable sets.

1. **Convex-hull invariance.**
   Linear tasks see only convex hulls:
   [
   h_A=h_{\operatorname{conv}A}.
   ]
   Hence this gap cannot detect purely nonconvex operational novelty.

2. **Faithfulness for convexified capability under a complete direction family.**
   If (W) contains all unit directions, then
   [
   \Omega_W(A,B)=0
   \iff
   \operatorname{conv}(A)\subseteq\operatorname{conv}(B).
   ]
   The reverse implication is immediate from support-function monotonicity. The forward implication follows from finite-dimensional separation: if some point of (operatorname{conv}(A)) lies outside the closed convex set (operatorname{conv}(B)), a separating linear functional gives a positive support gap.

3. **Monotonicity.**
   Enlarging (A) cannot decrease the gap; enlarging (B) cannot increase it.

4. **Degeneracy.**
   If augmentation creates a new attainable point already in (operatorname{conv}(B)), then the raw reachable-set escape is nonempty while every linear-task novelty gap is zero.

## Counterexample catalog

Baseline (B=\{(0,0),(2,0)\}); augmented (A=B\cup\{(1,0)\}).

The new point is genuinely new as a raw operational outcome, but ((1,0)\in\operatorname{conv}(B)). Therefore
[
A\setminus B\ne\varnothing
quad\text{while}\quad
\Omega_W(A,B)=0
]
for every linear task family (W).

Thus a linear task-advantage gap is not faithful to raw closure escape.

## Prior-art collision

The mechanism is classical convex separation/support-function geometry. More importantly, operational resource theories already characterize resources and convertibility by advantages over families of discrimination tasks. Takagi and Regula (Phys. Rev. X 9, 031053, 2019) show that discrimination tasks can form complete operational characterizations in general convex resource theories/GPTs. Subsequent robustness results identify maximal task advantage with established resource quantifiers, including extensions beyond convex free sets.

Therefore defining GC-II novelty merely as a supremum of task advantages is not, by itself, a novel mathematical mechanism.

## Status ledger

- task-relative gap definition: **VALID**
- convex-hull invariance for linear tasks: **PROVED**
- zero gap iff convexified augmented capability is contained in convexified baseline capability (complete normalized linear directions): **PROVED**
- faithfulness to raw closure escape: **FALSIFIED**
- generic supremum-of-operational-advantages mechanism as GC-II novelty: **IMPORTED/KNOWN**
- genuinely GC-specific novelty gap: **OPEN**

## Surviving target

A viable (Omega_G) must distinguish at least one pair that is invisible to the ordinary convex/task-advantage envelope while remaining operationally meaningful. The next decisive search should therefore target **matched operational models with identical convexified attainable outcome sets and identical standard task values, but different GC envelope/projection structure**, and ask whether a compositional GC-derived invariant separates them without encoding reachability by definition.

This is a stricter breakthrough criterion than merely constructing another witness or discrimination advantage.
