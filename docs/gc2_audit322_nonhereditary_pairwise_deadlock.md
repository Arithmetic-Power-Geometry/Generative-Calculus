# GC-II Audit 322 — Non-hereditary pairwise witnesses can coexist with joint deadlock

## Scope
This audit attacks the open boundary left by Audit 321. We retain a finite deterministic diagnostic model and nonnegative fixed test costs, but allow admissibility to depend on the current unresolved cell. The admissibility rule is therefore branch-relative and need not be hereditary under restriction.

## Definitions
Let `B` be the current cell and `Adm(C)` the tests authorized when the surviving cell is `C subseteq B`. For incompatible worlds `x,x' in B`, define the **root pairwise witness cost**

`p_B(x,x') = min{c(u): u in Adm(B), Z_u(x) != Z_u(x')}`,

and

`P_root(B)=max_{x != x'} p_B(x,x')`.

Let `V(B)` be the infimum worst-case cost of an adaptive policy that is admissible at every reached cell and ends in decision-homogeneous leaves; set `V(B)=+infinity` when no such policy exists.

These quantities have the same operational-cost units. `P_root` is deliberately a static root catalogue; `V` tests whether those witnesses compose into one executable policy.

## Theorem 322.1 — finite pairwise witnesses do not imply finite joint resolution without heredity
There exists a three-world deterministic system with unit test costs such that

`P_root(B)=1` but `V(B)=+infinity`.

### Construction
Take three worlds `B={0,1,2}` with three distinct required decisions. For each `i`, let singleton test

`u_i(x)=1[x=i]`, with `c(u_i)=1`.

Define the cell-relative admissibility rule

`Adm(B)={u_0,u_1,u_2}`

at the full root cell, but

`Adm(C)=emptyset`

for every unresolved proper cell `C` with `|C|>=2`.

Every incompatible pair `i != j` is separated at the root by `u_i` (and also by `u_j`), so every `p_B(i,j)=1` and therefore `P_root(B)=1`.

Now consider any admissible first move. It must be one singleton test `u_i`. Outcome `1` leaves the solved singleton `{i}`. Outcome `0` leaves the two-world cell `B\{i}`. That cell still contains two different required decisions but has no admissible test. Hence that branch is a deadlock. The same argument holds for each possible first move. Therefore no resolving admissible policy exists and `V(B)=+infinity`.

This proves the claim.

## Corollary 322.2 — Audit 321's finite distortion has a sharp structural boundary
There is no finite function `F(K,P_root)` satisfying

`V(B) <= F(K,P_root(B))`

for all finite deterministic branch-relative admissibility systems, even at the fixed values `K=3` and `P_root=1`.

Thus the Audit-321 bound `V <= (K-1)P` is not merely quantitatively weakened when heredity is removed: finite pairwise-to-joint comparability can disappear completely.

## Minimality
With `K=2`, any root test that separates the only incompatible pair immediately produces decision-homogeneous children, so finite `P_root` implies finite `V`. Therefore `K=3` is the smallest number of decision-critical classes permitting this deadlock mechanism.

## Why this is not a Closure-Escape breakthrough claim
The counterexample is elementary once branch-relative admissibility is allowed. Constrained/adaptive testing, test precedence, diagnosis policies, and state-dependent action availability are established neighboring ideas. In particular, classical adaptive diagnosis selects later tests conditional on earlier outcomes, while test-ordering literature also studies precedence constraints. The GC-II value is a boundary result: any pairwise novelty/capability certificate that ignores **persistence of admissibility along its own information branches** can certify finite local escape while global operational escape is impossible.

## Capability-accounting consequence
A defensible joint account must include at least one dynamic compatibility condition. One natural candidate is **hereditary witness persistence**: for every reachable unresolved cell `C`, every incompatible pair in `C` retains a finite admissible separator at `C`. Under finite cells and finite costs this restores the induction route; without such persistence, a root witness catalogue is not a capability certificate.

This suggests that a nontrivial `Omega_G` should distinguish static witness availability from dynamically composable availability, rather than counting or costing pairwise witnesses alone.

## Edge cases and checks
- Costs are unit positive, so the failure is not caused by zero-cost degeneracy.
- Outcomes are deterministic and binary; stochasticity is unnecessary.
- All three root witnesses are genuinely admissible before any test.
- The obstruction is not information insufficiency: every pair is root-separable. It is loss of future action admissibility after information acquisition.
- Relabeling worlds/tests preserves the construction.
- Uniform positive rescaling of costs preserves `P_root<infinity` and `V=infinity`.
- The construction is not hereditary: `u_j in Adm(B)` need not belong to `Adm(C)` after restriction.
- Composition behavior beyond this finite counterexample remains open.

## Exact verification
`experiments/gc2_audit322_nonhereditary_pairwise_deadlock.py` computes `P_root` and the exact Bellman value with `+infinity` for unresolved cells with no admissible split. It verifies every possible first move deadlocks on its negative two-world branch.

## Prior-art collision discipline
Adaptive decision trees/query complexity and diagnosis policy trees are **IMPORTED/KNOWN** mechanisms. Test ordering with precedence constraints is also established and can become computationally difficult. This audit therefore makes no novelty claim for constrained decision trees. Its role is to falsify an overstrong GC-II accounting implication and identify the exact assumption needed by Audit 321.

## Status ledger
- `P_root(B)=1` in the three-world construction: **PROVED**.
- `V(B)=+infinity`: **PROVED**.
- Finite root pairwise witnesses imply finite joint resolution without heredity: **FALSIFIED**.
- `K=3` minimal for this mechanism: **PROVED**.
- Audit-321 hereditary assumption is structurally necessary for any universal finite bound based only on `(K,P_root)`: **PROVED**.
- Adaptive/constrained decision-tree machinery: **IMPORTED/KNOWN**.
- Weakest dynamic persistence condition sufficient for a sharp quantitative bound: **OPEN**.
- Extension to stochastic observations, resource-replenishing actions, and endogenous rule changes: **OPEN**.
