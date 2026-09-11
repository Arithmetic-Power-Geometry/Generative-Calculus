# GC-II Audit 081 — Budget-Indexed Closure-Complexity Collision

Status: **DECISIVE FALSIFICATION of the current candidate as standalone GC-II novelty; PROVED representation-invariance no-go; OPEN only for a capability-linked lower bound not reducible to ordinary representation/parametric complexity**

Branch scope: `gc2-capability-accounting-lab` only. GC-I `main` remains frozen.

## 1. Candidate under attack

Audit 080 left the following possible direction: two operational systems agree on ordinary endpoint convertibility and on fixed-budget Pareto accounting up to a declared scale, but differ in the minimal description/computation required to generate their entire task-scale-error-budget closure as scale/budget grows.

Write the closure family as

`C_S = { C_S(s, epsilon, B) }_(s,epsilon,B)`.

For a representation/computation model `L`, define

`K_L(C_S; n) = min{|p| : p in L generates C_S restricted to index domain D_n}`

and analogously a running-time/space measure `T_L(C_S;n)`.

The question is whether a separation in `K_L` or `T_L` supplies a new GC-II capability invariant.

## 2. Representation-invariance no-go

### Theorem 081.1 (identical closure, identical intrinsic complexity)

Fix the same representation language/machine model `L`, the same encoding convention, and the same finite index domain `D_n`. If two systems have exactly the same indexed closure object on `D_n`,

`C_S|D_n = C_T|D_n`,

then

`K_L(C_S;n) = K_L(C_T;n)`

and every intrinsic minimization over programs that generate that object is identical for S and T.

**Proof.** The admissible program set is defined by the generated mathematical object. Equality of the target closure objects implies equality of the sets of programs that generate them under the same language and encoding. Minimizing the same length/cost functional over equal feasible sets gives equal minima. QED.

The same statement holds for exact minimum circuit size, minimum automaton size, minimum extended-formulation size, or any other representation complexity defined solely as a minimum over representations of the closure object, provided the representation class and encoding are fixed.

Status: **PROVED**.

### Corollary 081.1a

A claimed complexity separation between systems having the same complete closure must come from one of:

1. different encodings or representation languages;
2. different access models/oracles;
3. different promises about the system;
4. different algorithms being compared rather than intrinsic minima;
5. hidden structure not included in the closure object.

Items 1-4 are model-relative computational complexity. Item 5 means the compared objects were not actually identical.

Therefore there is no architecture-independent closure-description gap attached to identical closure objects.

## 3. Finite-prefix agreement gives no nontrivial lower bound

### Theorem 081.2 (delayed-divergence construction)

For every finite index cutoff `n`, there exist closure families `C` and `D` such that

`C|D_n = D|D_n`

but their behavior beyond `D_n` differs arbitrarily, subject only to the chosen admissibility grammar.

**Construction.** Choose any valid closure family C. Define D to equal C on D_n and, outside D_n, splice any other admissible continuation H. Then finite-prefix agreement holds exactly while the future family can have different representation, decision, or enumeration complexity.

Thus agreement at all tested/fixed budgets up to a finite scale does not constrain untested asymptotic closure complexity unless additional regularity, compositionality, computability, stationarity, or finite-generation assumptions are imposed.

Status: **PROVED (elementary construction)**.

This kills a possible inference of the form

`same finite-budget capability + later complexity separation => new generative phenomenon`.

Without an independently justified cross-scale law, this is merely delayed divergence.

## 4. Complexity of the closure is not capability itself

Suppose two systems have different closure objects and one closure is exponentially harder to describe/optimize over. That can be scientifically important, but the separation is then a complexity property of a family of feasible sets/functions/relations. It does not by itself establish a new capability-accounting law.

A useful distinction is:

- **capability value:** which tasks/errors/budgets are achievable;
- **representation complexity:** size of a representation of that achievable set;
- **evaluation complexity:** cost of deciding membership or optimizing over it;
- **construction complexity:** cost of physically realizing a witness/policy.

These quantities can separate. GC-II must not identify them without a theorem.

## 5. Prior-art collision

The current candidate collides directly with established theories:

1. **Extension complexity.** A polytope can have an exponentially large minimum extended formulation. Rothvoss proved `2^{Omega(n)}` extension complexity for the perfect matching polytope. Thus exponential complexity of representing an operational feasible region is already a mature phenomenon.
2. **Communication complexity / nonnegative rank.** Extended-formulation lower bounds are deeply linked to communication-style lower bounds; independent-set and correlation-polytope results already exploit these connections.
3. **Automata/minimal realization.** Myhill-Nerode theory characterizes the minimum number of states needed to represent a regular language via continuation equivalence. A large minimal continuation-state representation is therefore not new merely because the represented object is called a capability closure.
4. **Parametric optimization.** The number/structure of optimal solutions as parameters vary is itself a studied complexity object. A July/August 2026 ECCC result, *Shortest Paths with Linear Edge Weights* (TR26-142), explicitly studies parametric shortest-path complexity for shared linear parameters.
5. **Succinct/description complexity.** Program, circuit, grammar, formula, decision-diagram, and other representation sizes are model-dependent unless a fixed universal encoding and invariance statement is supplied.

Accordingly, a large `K_L(C;n)` or `T_L(C;n)` is not defensible as standalone GC-II novelty.

## 6. Dimensional/domain audit

`K_L` is measured in representation symbols/bits under a declared encoding; `T_L` in machine steps (and optionally space). Neither has the physical dimensions of `R,I,A,L` unless an explicit implementation map converts computational resources into the typed physical ledger.

Therefore an equation such as

`Omega_G <= F(Delta R, Delta I, Delta A, Delta L, K_L)`

is dimensionally meaningless until `K_L` is either nondimensionalized or mapped to a physical resource coordinate. This blocks using raw description complexity as the missing term in the desired capability-accounting bound.

Status: **PROVED type/dimension constraint**.

## 7. Composition audit

For independently represented closure objects, description complexity is at most subadditive up to compiler/decoder overhead under a fixed universal description system:

`K(C tensor D) <= K(C) + K(D) + O(1)`.

But equality, additivity, and monotonicity need not hold. Shared structure can compress the joint object; a poor encoding can inflate it. Computational running time is even more representation- and algorithm-sensitive.

Hence no universal additive GC ledger law follows from description complexity.

Status: **CONDITIONAL/KNOWN complexity behavior; no GC novelty inferred**.

## 8. Falsification boundary

The following candidate is rejected:

> A difference in the minimal description/computation required to generate budget-indexed operational closures, after ordinary endpoint conversion is factored out, is by itself a new Generative Calculus capability invariant.

It is not. If the closures are identical under the same representation model, intrinsic representation complexity is identical. If only finite prefixes agree, arbitrary delayed divergence is possible. If the full closures differ, their representation/evaluation complexity is an ordinary complexity-theoretic property unless a new theorem couples it quantitatively to physical capability creation.

Status: **FALSIFIED as standalone novelty source**.

## 9. Stronger surviving target

The surviving target must couple computation to *physical capability creation* rather than merely to representation of a closure.

A sharper candidate is a **Capability-Witness Realization Lower Bound**. For a task query `q` and complete operational substrate `S`, define

`W_S(q,epsilon,B) = Pareto-min physical typed cost of producing and executing a verifiable witness/policy that realizes q within (epsilon,B)`.

The desired theorem would need a family for which:

1. achievability itself is nontrivial but explicitly defined;
2. the lower bound applies to physical witness realization, not just offline description of the feasible set;
3. the bound is invariant under admissible re-encodings/compilers up to declared simulation overhead;
4. free oracles/advice/interfaces are excluded explicitly;
5. the bound survives amortization, randomization, catalysts and composition when those are declared free;
6. a typed lower bound connects computational/informational necessity to `Delta R, Delta I, Delta A, Delta L` through an explicit implementation model;
7. the result is stronger than ordinary communication/query/circuit/decision-tree/space lower bounds after reduction.

This candidate is **OPEN**. It is not yet a breakthrough claim.

The next attack should try to prove that this too collapses to ordinary implementation complexity under a fixed substrate; if so, GC-II needs a different invariant. If it survives, the first useful exact test family should expose an unavoidable tradeoff between information acquisition, action/interface capacity, and physical resource budget rather than merely an exponential representation size.

## 10. Status table

| Claim | Status |
|---|---|
| identical indexed closure under same representation model has identical intrinsic minimum representation complexity | PROVED |
| finite-prefix closure agreement constrains arbitrary future complexity without extra cross-scale assumptions | FALSIFIED |
| raw description complexity can be inserted directly into typed R,I,A,L equations | FALSIFIED / dimensionally ill-typed without implementation map |
| exponential closure representation complexity is standalone GC-II novelty | FALSIFIED; collides with extension/communication/automata/parametric complexity |
| budget-indexed closure-complexity separation is standalone Paper-II breakthrough | FALSIFIED |
| capability-witness realization lower bound surviving standard complexity reductions | OPEN |

No breakthrough claim is made in Audit 081.
