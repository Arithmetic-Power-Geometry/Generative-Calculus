# GC-II Audit 324 — Closure-Escape Fixed-Point Characterization

## Scope
Finite deterministic branch-relative operational systems. This audit attacks the non-tautological Closure-Escape program after Audits 322–323 showed that static/root pairwise witnesses are insufficient and that BCSP is sufficient but not necessary.

## Operational model
Let `X` be a finite world set and `g:X->D` the required decision. An information cell is a nonempty `C subseteq X`. It is terminal when `g` is constant on `C`.

At each cell `C`, `Adm(C)` is the set of currently admissible actions/tests. For `u in Adm(C)`, each possible observation `y` induces the nonempty child

`C[u,y] = {x in C : Z_u(x)=y}`.

No heredity assumption is made: admissibility may change arbitrarily with the reached cell. Costs may be arbitrary nonnegative finite numbers; this audit concerns finite resolvability rather than optimal cost.

## Escape operator
For a set `W` of cells define

`T(W) = Terminal union { C unresolved : exists u in Adm(C) such that every nonempty child C[u,y] is in W and every child is a strict subset of C }`.

Starting with `W_0 = Terminal`, iterate

`W_{t+1}=T(W_t)`.

Because the finite cell lattice has at most `2^|X|-1` nonempty cells, the sequence stabilizes after finitely many additions. Write `W_*` for the least fixed point.

Define the escape rank

`rho(C)=min{t : C in W_t}`

for `C in W_*`, with terminals having rank 0.

## Theorem 324A — Closure-Escape equivalence
For every nonempty cell `C`, the following are equivalent:

1. **Operational:** there exists a finite admissible adaptive policy/tree resolving `g` from `C` on every observation branch.
2. **Fixed-point/geometric:** `C in W_*`.
3. **Ranking certificate:** there exists an integer-valued rank `r` on the cells reachable under some admissible policy, with `r=0` on terminal cells, and for every unresolved policy cell `C` an admissible action `u` such that every nonempty child satisfies `r(C[u,y]) < r(C)`.
4. **Computational:** the backward fixed-point algorithm above accepts `C`.

### Proof
(2=>1) Induct on `rho(C)`. Rank 0 is terminal. If `rho(C)=t+1`, by construction there is an admissible `u` whose every child is strict and belongs to `W_t`; apply the induction hypothesis independently to each child and attach the resulting resolving subtrees below `u`.

(1=>3) Take any finite resolving policy tree and assign each reached information cell the maximum remaining tree height among occurrences of that cell. A policy action at an unresolved node sends every branch to a subtree of strictly smaller remaining height, yielding the rank descent certificate. Repeated cells can be assigned the maximum occurrence height; if necessary prune non-progress repetitions, which cannot be required for deterministic observation refinement because cells never enlarge.

(3=>2) Induct on `r`. Terminal rank 0 cells are in `W_0`. If an unresolved cell has rank `q>0`, its witnessing action has all children of smaller rank; after at most `q-1` iterations all children have entered the fixed point sequence, so the cell enters at the next iteration.

(2<=>4) is exactly finite least-fixed-point iteration.

Thus the equivalence is exact, not a restatement in terms of an already-optimized value function.

## Dual obstruction: the closure trap kernel
Let `L` be the complement of `W_*` among nonempty cells. Then every unresolved `C in L` has the adversarial closure property

`for every u in Adm(C), either u has a non-progress child equal to C, or some nonempty child lies in L.`

Conversely any nonempty family of unresolved cells satisfying this adversarial closure property is contained in `L`.

Hence `L` is the greatest adversarially closed unresolved kernel. It is a finite certificate of impossibility: after every admissible move an adversary can select an outcome that remains trapped.

This gives the finite deterministic Closure-Escape dichotomy

`resolvable <=> admits a descending escape rank <=> outside the greatest unresolved trap kernel`.

## Relation to Audit 323
BCSP(P) implies membership in `W_*`, because its class-separating action strictly lowers the number of surviving decision classes on every child. But BCSP is not necessary: an action may reduce the information cell on every branch while every child still contains the same number of decision classes; subsequent branch-specific actions can nevertheless resolve. Therefore Audit 324 strictly separates the exact existence criterion from the stronger quantitative BCSP sufficient condition.

## Edge cases and audit
- Terminal cells are accepted at rank 0 even if no action is admissible.
- An unresolved cell with no admissible action is in the trap kernel.
- A self-loop/non-progress outcome prevents that action from being an escape witness, but another admissible action may still win.
- Zero-cost actions do not alter finite resolvability; they matter only for quantitative value bounds.
- Multiway observations are allowed.
- Arbitrary branch-relative/non-hereditary admissibility is allowed.
- The result is invariant under relabeling worlds, decisions, actions, and observations.
- Under restriction to a reached child, the same fixed-point criterion applies without any heredity assumption.

## Prior-art / novelty discipline
The mathematical mechanism is an AND-OR reachability / backward-attractor fixed point and well-founded ranking argument. Those mechanisms are established in reachability games, model checking, planning, diagnosis, and termination proofs. Therefore the fixed-point theorem machinery is **IMPORTED/KNOWN**, not claimed as a new mathematical invention.

The GC-II contribution retained here is narrower: it supplies the exact finite operational boundary required after the pairwise-accounting failures of Audits 319–323 and identifies the correct object that any Generative Novelty Gap or No-Free-Capability statement must dominate when admissibility is branch-relative.

## Status
- Finite deterministic Closure-Escape equivalence: **PROVED**.
- Greatest unresolved trap-kernel dual: **PROVED**.
- Exact finite algorithm: **PROVED / IMPORTED-KNOWN mechanism**.
- BCSP necessary for escape: **FALSIFIED**.
- Extension to stochastic/noisy observations with probabilistic success: **OPEN**.
- Quantitative cost theorem derived from escape rank alone: **OPEN** (rank ignores heterogeneous costs).
- Novelty of AND-OR/fixed-point mathematics: **IMPORTED/KNOWN; DO NOT CLAIM**.
