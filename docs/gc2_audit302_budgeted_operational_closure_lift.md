# GC-II Audit 302 — Budgeted operational closure as lifted-state reachability

## Purpose

This audit closes a formalization gap before further claims about novelty gaps or no-free-capability laws. It does **not** claim a new reachability theorem. The lifted-state construction is standard state augmentation; the contribution here is to pin GC-II quantities to an explicit typed operational object so later theorems cannot hide resources, information, interfaces, actions, or rules inside an undefined closure operator.

## Typed operational system

A finite budgeted operational system is

\[
\mathfrak S=(X,R,I,A,L,\mathcal T,\operatorname{Adm},c,\Phi,x_0,r_0,i_0,a_0,\ell_0),
\]

where:

- `X` is the physical/semantic state space;
- `R` is the resource-state space;
- `I` is the information-state space;
- `A` is the currently exposed interface/action state;
- `L` is the rule/policy state;
- `T` is the set of typed transformations;
- `Adm(t,z)` is the admissibility predicate for transformation `t` at lifted state `z=(x,r,i,a,l)`;
- `c(t,z) in R_+^d` is a nonnegative resource-cost vector;
- `Phi_t(z)` is the successor lifted state when admissible;
- `z0=(x0,r0,i0,a0,l0)` is the initial lifted state.

A budget is `b in R_+^d`. For a finite admissible trace `pi=(t1,...,tm)`, define accumulated cost componentwise by

\[
C(\pi)=\sum_{j=1}^m c(t_j,z_{j-1}).
\]

The trace is budget-feasible iff every transition is admissible at its actual predecessor state and `C(pi) <= b` componentwise.

## Budgeted operational closure

Define

\[
\operatorname{Cl}_b(z_0)=\{z_m:\exists\text{ budget-feasible admissible trace }z_0\to\cdots\to z_m\}.
\]

For an observable/capability map `g: X x R x I x A x L -> Y`, define

\[
\operatorname{Cap}_b(z_0)=g(\operatorname{Cl}_b(z_0)).
\]

This explicitly prevents a capability claim from silently changing information, exposed actions, or governing rules without charging or representing that change.

## Lifted graph theorem

Construct the budget-augmented graph with vertices `(z,q)` where `z in X x R x I x A x L` and `q in R_+^d` is accumulated cost with `q <= b`. Put an edge

\[
(z,q)\to(\Phi_t(z),q+c(t,z))
\]

iff `Adm(t,z)` and the new accumulated cost is at most `b`.

**Theorem 302.1 (exact lifted-state criterion; PROVED).** A lifted state `z` belongs to `Cl_b(z0)` iff there exists a path in the budget-augmented graph from `(z0,0)` to `(z,q)` for some `q <= b`.

**Proof.** Each feasible operational trace maps transition-by-transition to a graph path with identical accumulated cost. Conversely every graph edge exists only for an actually admissible transformation and records its actual state-dependent cost, so projecting a graph path gives a feasible operational trace. Induction on path/trace length proves both directions. QED.

This is an exact representation result, not a novelty claim; it is state augmentation / constrained reachability territory.

## Immediate invariants

**Budget monotonicity (PROVED).** If `b <= b'` componentwise, then

\[
Cl_b(z0) \subseteq Cl_{b'}(z0).
\]

**Zero-step inclusion (PROVED).** `z0 in Cl_b(z0)` for every nonnegative budget.

**Prefix closure (PROVED).** Every prefix state of a budget-feasible trace is itself in `Cl_b(z0)` because costs are nonnegative.

**Relabeling invariance (PROVED).** Type-preserving bijective relabelings preserving `Adm`, `c`, `Phi`, and `g` preserve closure and capability sets up to the corresponding bijection.

## Composition warning

For two independent systems with separate budgets, product reachability gives the expected product inclusion/equality only when admissibility, transition maps, and accounting factor componentwise. Shared resources, information revelation, cross-interface actions, or rule updates can destroy factorization. Therefore no product law is imported into GC-II merely from the static accounting results of Audits 298–301.

## No-free-capability sanity boundary

A universal statement of the form “capability cannot increase without positive resource cost” is **false** under this model without additional assumptions: a zero-cost admissible transition can expose a new action, reveal stored information, or change the rule/interface state and thereby enlarge `Cap_b`.

Minimal witness: two lifted states `z0,z1`, one zero-cost admissible transition `z0 -> z1`, and `g(z0) != g(z1)`. Then the new capability is reachable at zero charged resource cost.

Thus any defensible No-Free-Capability theorem must explicitly charge the relevant operational channels or impose a nonexpansion axiom on zero-charge transitions. Treating the conclusion as the axiom would be tautological and is rejected.

## Domain and edge-case audit

- Empty transformation set: closure is `{z0}`.
- Zero budget: zero-cost traces may still move; closure need not be `{z0}`.
- Multiple resource dimensions: inequalities are componentwise; no dimensional addition across heterogeneous coordinates is performed.
- State-dependent costs: retained exactly in the lifted edge relation.
- Cycles: harmless for set-valued reachability; zero-cost cycles may exist.
- Negative costs: excluded. Allowing them breaks prefix-budget reasoning and requires a different semantics.
- Information/rule/action changes: represented as state transitions, not treated as free hidden side effects.
- Degenerate capability map: constant `g` yields no observable capability growth despite potentially large closure.

## Status

- Explicit typed budgeted operational closure: **PROVED / DEFINITION FIXED**.
- Equivalence with budget-augmented reachability: **PROVED**, but mathematical mechanism **IMPORTED/KNOWN**.
- Budget monotonicity, prefix closure, relabeling invariance: **PROVED**.
- Universal positive-resource No-Free-Capability claim: **FALSIFIED** without additional assumptions.
- Non-tautological weakest assumptions for a No-Free-Capability theorem: **OPEN**.
- Dynamic Generative Novelty Gap built on this closure: **OPEN**.

## Next attack

Define novelty relative to two typed systems by capability-set difference or a task/value functional while separating (i) genuinely new reachable capability from (ii) mere relabeling and (iii) capability already latent behind a zero-cost interface/information/rule transition. Then search finite systems exhaustively for the weakest conditions under which a positive novelty gap forces a positive charged-channel delta.
