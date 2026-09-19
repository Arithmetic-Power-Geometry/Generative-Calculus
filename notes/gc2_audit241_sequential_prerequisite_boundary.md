# GC-II Audit 241 — Sequential prerequisite boundary

## Purpose
Advance Audit 240 from one-shot union-of-effects generators to genuinely sequential typed closure with prerequisites and state-dependent effects. The main question is whether the static typed-repair formula survives once operations can enable other operations.

## Finite sequential operational model
Fix a finite state space X, initial state x0, and accepting set F subseteq X consisting of states in which the exact translator criterion of Audits 236–240 is feasible. Let O be a finite family of typed operations. An operation o has type tau(o) in {R,I,A,L} or a product type, nonnegative cost vector c(o), an enabling predicate En_o(x), and transition relation T_o(x) subseteq X. Nondeterminism is allowed. For nonnegative scalarization theta, an execution pi=(x0,o1,x1,...,on,xn) is admissible when En_oi(x_{i-1}) and xi in T_oi(x_{i-1}) for every i. Its cost is C_theta(pi)=sum_i theta dot c(oi).

Define the sequential budget closure
Cl_B(x0)={x : there exists an admissible execution pi from x0 to x with C_theta(pi)<=B}.

Define the sequential novelty gap
Omega_seq(x0,F)=inf{C_theta(pi): pi admissible from x0 and final(pi) in F},
with infinity when F is unreachable.

## Sequential Closure-Escape theorem — PROVED / generic
For every B>=0,
F intersects Cl_B(x0) iff Omega_seq(x0,F)<=B.
Hence capability escapes the B-budget closure iff Omega_seq>B.

Proof is immediate from the two definitions. This is an exact operational/geometric/computational criterion (weighted reachability / shortest accepting path) but is generic transition-system/planning theory and is not claimed as GC novelty.

## Static-union reduction fails — PROVED
The Audit-240 one-shot representation L_S=L0 union union_{o in S}E(o) is not complete for sequential closure.

Counterexample. States carry tokens q,r and a target incidence e. Initially neither token is present and e is absent. Operations have unit cost:
- o_R: always enabled, creates q.
- o_I: enabled iff q is present, creates r.
- o_A: enabled iff r is present, creates e.
The accepting translator requires e. Sequentially, o_R;o_I;o_A reaches F at cost 3.

Now construct a second system with exactly the same operation names, types, costs, and nominal terminal effects, but change the prerequisite of o_A to an unavailable token s that no operation creates. The one-shot union of nominal effects is identical, as are all per-type cost totals and operation-effect cardinalities, yet F is unreachable and Omega_seq=infinity.

Therefore operation multisets, scalar DeltaR/DeltaI/DeltaA/DeltaL totals, and static unions of nominal effects do not determine capability once prerequisites are admitted. The enabling/transition structure is operationally essential.

## Order sensitivity — PROVED
Even when the same operations are all eventually executable in some contexts, state-dependent effects can make permutation matter. Example: o1 sets q=1; o2 creates target incidence e only when q=1 and otherwise consumes itself with no effect. Sequence o1;o2 succeeds while o2;o1 fails. Thus a set S of chosen operations is insufficient unless operations commute and their effects are state-independent.

## Exact condition recovering Audit 240 — PROVED
Audit 240 is recovered when all operations are always enabled, effects are inflationary and state-independent, and operations commute at the level relevant to translator feasibility: for every finite sequence using operation set S, the final admissibility incidence equals L0 union union_{o in S}E(o). Under these conditions execution order is irrelevant and Omega_seq equals the Audit-240 minimum subset cost (for nonnegative costs, repetitions can be deleted).

This identifies a precise boundary rather than treating the one-shot model as generally valid.

## No-Free-Capability status
Nonnegative operation costs alone still do not imply a positive novelty gap: a zero-cost enabled path can reach F, or positive path costs can have infimum zero in infinite/non-finite models. In the present finite model with a strictly positive lower bound epsilon on every capability-relevant transition cost, any nontrivial accepting path has Omega_seq>=epsilon. This is generic coercivity, not a GC-specific theorem.

## Composition behavior
Sequential composition obeys subadditivity of optimal reachability cost: if y is reachable from x and F is reachable from y, then Omega(x,F)<=d(x,y)+Omega(y,F), with the usual infinity conventions. Equality need not hold because an optimal x-to-F path need not pass through y.

## Prior-art collision boundary
The sequential model is a weighted transition system / shortest-path / planning formulation. Preconditions and effects are standard in classical planning; resource-constrained reachability and shortest accepting paths are established. Therefore neither the transition-system formalization nor the Closure-Escape equivalence is claimed as new.

The GC-II novelty target must lie in additional structure imposed by generative composition: e.g. a theorem connecting typed prerequisite creation, projection ambiguity, and translator feasibility that yields a non-generic invariant or lower bound not reducible to ordinary weighted reachability/planning.

## Status ledger
- Sequential typed budget closure: PROVED as a well-defined finite model.
- Sequential Closure-Escape equivalence: PROVED / IMPORTED-KNOWN generic reachability.
- Audit-240 static union remains complete with arbitrary prerequisites/state dependence: FALSIFIED.
- Same operation/effect/cost marginals determine sequential capability: FALSIFIED.
- Enabling/transition structure is necessary in the general sequential model: PROVED by counterexample.
- Audit-240 recovery under always-enabled, inflationary, state-independent commuting effects: PROVED.
- Nonnegative costs alone imply No-Free-Capability: FALSIFIED.
- GC-specific prerequisite/projection lower bound beyond generic planning: OPEN.
