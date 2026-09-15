# GC-II Audit 151 — Typed realization-cost collision

## Candidate tested
After Audit 150, test whether two systems can have identical extensional capability / minimal residual-state semantics but different minimum typed realization cost under explicit interface restrictions.

For a Boolean target f and primitive library L, define

C_L(f) = min{|P| : P is a straight-line circuit over L and P computes f exactly}.

This is representation-invariant with respect to circuit syntax once L and the unit gate cost are fixed, because the minimum is over all realizations in that operational library.

## Exact finite witness
For XOR(x,y), exhaustive breadth-first synthesis over all intermediate two-input truth tables gives:

- L_N = {NAND}: C_L(XOR)=4.
- L_A = {AND, OR, NOT}: C_L(XOR)=4.
- L_X = {XOR, AND, NOT}: C_L(XOR)=1.

All three libraries synthesize all 16 two-input Boolean functions within the audited search depth. The target function is identical, so its extensional input/output relation and residual semantics are identical, while exact typed realization cost differs.

## Proof checks
The one-gate XOR realization in L_X is immediate. The BFS is exhaustive by gate count because each search state is the set of truth tables already available; adding one primitive gate produces every one-gate extension. Thus first discovery is minimum gate count. The checker verifies all 16 functions are reached in every library and the XOR minima above.

Degenerate targets and projections are included among the 16 truth tables. Composition is ordinary straight-line composition. Costs are dimensionless gate counts and nonnegative. Relabeling/syntactic rewriting does not change the minimum once the primitive library is fixed.

## Collision / novelty status
The separation is real but is not a new GC-II mechanism. Minimum exact realization relative to a primitive gate set is the subject of classical/quantum circuit synthesis and circuit complexity. Exact synthesis methods explicitly optimize gate count or expensive typed gates; recent exact synthesis work also uses exhaustive/SAT methods to prove optimality. Resource theories of processes likewise study implementation cost relative to free operations/resources.

Therefore merely defining Omega_G as a difference in minimum typed realization cost would repackage known synthesis/resource-cost machinery.

## Ledger
- Same extensional capability with different typed realization cost: **PROVED**.
- Exact exhaustive two-input regression: **PASS**.
- Typed gate/interface cost alone as independent GC-II novelty: **FALSIFIED**.
- Exact synthesis / circuit-resource mechanism: **IMPORTED/KNOWN**.
- Candidate requiring coupled R/I/A/L interaction that cannot be reduced to a fixed primitive library or ordinary process-resource implementation cost: **OPEN**.

## Next gate
Seek a pair with the same extensional capability and same costs under every single-axis restriction (R-only, I-only, A-only, L-only), but a provable difference under a coupled admissibility rule. Then test whether the separation is merely multi-resource/Pareto resource theory, constrained planning, or hardware-aware synthesis. A defensible Omega_G must capture irreducible interaction rather than gate-set choice.
