# GC-II Audit 380 — Reversibility-gap boundary

## Scope
Branch-only Paper-II audit. GC-I foundations on `main` are unchanged.

## Setup
Let (X) be a finite operational state space and let (x\preceq y) denote exact admissible convertibility. Let (d_c(x,y)) be the infimum additive nonnegative cost of an admissible implementation from (x) to (y), with (+\infty) if none exists.

## Theorem 380.1 — structural reversibility is SCC equivalence
Define
[
x\sim_R y \iff (x\preceq y)\wedge(y\preceq x).
]
Then (\sim_R) is exactly mutual reachability. For a finite transition presentation its equivalence classes are precisely the strongly connected components (SCCs), and the quotient convertibility relation is the condensation DAG.

**Status:** PROVED / IMPORTED-KNOWN.

### Proof
Reflexivity and transitivity follow from the preorder. Symmetry is built into the definition. In a directed transition presentation, two vertices lie in one SCC iff each is reachable from the other. Therefore no binary invariant defined solely from mutual reachability contains information beyond the SCC partition/condensation.

## Proposition 380.2 — cost asymmetry is determined by the directed distance matrix
Whenever both directions are finite, quantities such as
[
A_c(x,y)=|d_c(x,y)-d_c(y,x)|,
qquad
T_c(x,y)=d_c(x,y)+d_c(y,x)
]
are functions of the directed optimal-cost matrix (D_c=(d_c(x,y))). Consequently two systems with identical (D_c) cannot be separated by any invariant that is only a function of forward/reverse optimal costs.

**Status:** PROVED; candidate GC novelty from these quantities: FALSIFIED.

## Proposition 380.3 — neither common scalarization is a faithful structural reversibility gap
1. (A_c(x,y)=0) can hold with (d_c(x,y)=d_c(y,x)=K>0) for arbitrary (K); hence zero asymmetry does not mean free or identity conversion.
2. (T_c(x,y)>0) can hold even when (x\sim_R y); hence positive round-trip cost does not mean structural irreversibility.
3. If exactly one direction is unreachable, ordinary finite scalar asymmetry is undefined/nonfinite unless an extra convention is imposed.

**Status:** PROVED.

## Proposition 380.4 — rescaling obstruction
For (c_\alpha=\alpha c), (\alpha>0),
[
d_{c_\alpha}(x,y)=\alpha d_c(x,y)
]
whenever the distance is finite. Thus numerical reversibility gaps derived from (D_c) rescale while reachability, SCCs, projection structure and undecorated GC-I envelope structure remain fixed.

**Status:** PROVED.

## Edge/degenerate audit
- (x=y): empty implementation gives (d(x,x)=0) under the standard convention.
- zero-cost cycles: mutual reachability may have zero round-trip cost; this does not invalidate SCC equivalence.
- positive-cost reversible cycles: SCC-equivalent states may have positive round-trip cost.
- one-way reachability: structural irreversibility is captured already by the condensation order.
- unreachable both ways: neither a forward/reverse conversion pair nor a finite cost-gap interpretation exists without an explicit convention.
- duplicate actions and self-loops do not change SCC structure; they may change decorated implementation data if costs/actions are retained.
- composition: no additivity of (A_c) or (T_c) is assumed or claimed.

## Prior-art collision
The generic constructions collide with established directed/quasi-metric shortest-path structure and with resource-theoretic notions of reversible/irreversible interconversion. In resource theories, forward/reverse conversion rates, distillation/formation costs, and asymptotic reversibility are established operational notions. Therefore SCC or directed-cost asymmetry is not claimed as GC-II novelty.

**Status:** IMPORTED/KNOWN mechanism; no novelty claim.

## Surviving breakthrough gate
A genuinely GC-specific reversibility invariant (\Gamma_G) must survive the matched-system test:

Construct systems (S_1,S_2) with identical
1. reachability preorder and SCC condensation,
2. full directed optimal-cost matrix,
3. translator confusability graph(s) from Audit 379,
4. ordinary task/output summaries,

but different frozen GC-I envelope/projection structure, and prove that (\Gamma_G(S_1)\ne\Gamma_G(S_2)) predicts an independently checkable operational consequence not recoverable from the matched classical summaries.

Until such a witness is found, target (8) remains **OPEN**.

## Status ledger
- mutual reachability = SCC equivalence: **PROVED / IMPORTED-KNOWN**
- binary reachability reversibility as GC-II novelty: **FALSIFIED**
- forward/reverse shortest-cost asymmetry as GC-II novelty: **FALSIFIED**
- round-trip cost as structural irreversibility: **FALSIFIED**
- positive absolute numerical gap from undecorated GC structure: **FALSIFIED by rescaling**
- GC-specific residual reversibility invariant beyond matched classical summaries: **OPEN**
