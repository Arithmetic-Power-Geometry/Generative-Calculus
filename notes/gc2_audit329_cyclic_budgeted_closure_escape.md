# GC-II Audit 329 — Cyclic budgeted Closure-Escape via a least fixed point

## Scope
Finite deterministic operational systems with branch-relative admissibility, finite outcome sets, and nonnegative **integer** resource vectors. This extends Audit 328 beyond acyclic AND–OR trees. It does not claim novelty for fixed-point dynamic programming itself.

## Model
Let `S` be a finite set of information states/cells. `T ⊆ S` is the set of decision-homogeneous terminal states. At `s`, `Adm(s)` is a finite set of admissible actions. Action `u` has resource cost `c(s,u) ∈ N^d` and a nonempty finite successor set `Succ(s,u) ⊆ S` (one successor for each possible observation/outcome). A policy wins from `(s,b)` if every adversarial outcome path reaches `T` after finitely many actions while cumulative resource use is componentwise at most `b ∈ N^d`.

For a fixed finite budget box `B = {0,…,b_1}×…×{0,…,b_d}`, define the monotone operator on `Q ⊆ S×B`

`Phi(Q) = {(t,b): t∈T, b∈B} ∪ {(s,b): exists u∈Adm(s), c(s,u)≤b, and for every s'∈Succ(s,u), (s', b-c(s,u))∈Q}`.

Let `W = lfp(Phi)`, obtained by iteration from the terminal pairs.

## Theorem 329.1 — exact cyclic budgeted Closure-Escape
For every `(s,b) ∈ S×B`,

`(s,b) ∈ W` iff there exists a finite resolving admissible policy from `s` whose cumulative resource vector is at most `b` on every outcome path.

### Proof
**Soundness.** Give every pair its least fixed-point entry rank. Terminal pairs have rank 0. If `(s,b)` enters at rank `r+1`, it has a witnessing action `u` whose every successor pair `(s',b-c)` entered by rank at most `r`. Execute `u` and recursively use the lower-rank witnesses. Rank strictly decreases after each action, so every outcome path terminates after finitely many steps. The budget invariant follows because the successor is evaluated at the residual vector `b-c`.

**Completeness.** Let a finite winning policy tree have height `h`. Induct on `h`. Height 0 is terminal. At height `h+1`, the root action has cost `c≤b`; every outcome subtree is a winning policy of height at most `h` under residual budget `b-c`. By induction every successor pair belongs to `W`, hence the root pair is inserted by `Phi` and belongs to `W`.

Thus the least fixed point is exact. QED.

## Corollary 329.2 — zero-cost cycles require the *least* fixed point
An unresolved state with a zero-cost self-loop and no terminal escape satisfies the Bellman-looking self-consistency equation `X = X`, but is **not** in `lfp(Phi)`. Therefore solving only algebraic Bellman equations, or taking a greatest fixed point, can falsely certify capability. Finite resolution requires a well-founded progress certificate even when resource consumption does not decrease.

Minimal counterexample: one unresolved state `s`, one admissible action of cost `0`, `Succ(s,u)={s}`, no terminal state reachable. Then `(s,b)` never enters the least-fixed-point iteration for any budget `b`, so it is correctly classified as non-resolving.

## Corollary 329.3 — finite termination bound
Because `S×B` is finite, fixed-point iteration stabilizes after at most `|S||B|` strict insertion rounds. Entry rank supplies an explicit finite policy-height certificate bounded by that number.

## Corollary 329.4 — upward budget monotonicity
If `(s,b)∈W` and `b'≥b` componentwise (within the chosen budget box), then `(s,b')∈W`. The same policy remains feasible with slack. Hence the feasible budget set of each state is upward closed; its Pareto-minimal antichain is an exact finite representation inside a bounded integer box.

## Composition and edge audit
- `d=1`: reduces to scalar cyclic budgeted minimax reachability.
- `c=0`: allowed; termination is certified by fixed-point rank rather than budget decrease.
- terminal state: feasible at every nonnegative budget, including zero.
- no admissible action at unresolved state: losing for every budget.
- adversarial branching: universal successor condition is essential.
- branch-relative admissibility: fully allowed because `Adm` is state dependent.
- resource coordinates: no scalarization or exchange rate is assumed.
- coordinate permutation and positive integer unit rescaling preserve feasibility after the corresponding budget transformation.

## Status
- Exact cyclic integer-budget Closure-Escape criterion: **PROVED**.
- Least-fixed-point / finite-policy equivalence: **PROVED**.
- Zero-cost-cycle false-positive under non-well-founded Bellman self-consistency: **PROVED / decisive counterexample**.
- Generic least-fixed-point reachability machinery: **IMPORTED/KNOWN** (AND–OR games, strong planning, reachability games, dynamic programming).
- Unbounded real-valued resource domain with finite symbolic Pareto representation: **OPEN**.
- Stochastic/noisy outcomes and probabilistic guarantees: **OPEN**.
- Novelty claim for generic fixed-point machinery: **NOT MADE**.

## GC-II consequence
Audit 328's acyclic Pareto recursion is not the final closure object in the presence of operational cycles. The correct finite cyclic object is a least fixed point over state–residual-budget pairs (or an equivalent upward-closed-set formulation). Any GC-II capability account that admits zero-cost or resource-neutral transformations must retain an independent well-founded progress/rank condition; resource decrease alone cannot certify eventual capability realization.
