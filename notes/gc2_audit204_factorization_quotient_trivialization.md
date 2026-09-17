# GC-II Audit 204 — Factorization-quotiented interaction trivialization

## Target
Audit 203 left open whether an intrinsic interaction invariant can be obtained by minimizing/quotienting higher-order R/I/A/L interaction over every semantics-preserving refinement and regrouping.

## Setup
Let N={R,I,A,L}. A presentation P consists of a partition pi={B1,...,Bk} of N together with the induced capability-value function v_pi on unions of blocks. Assume regrouping is semantics-preserving: replacing several primitive coordinates by their joint block does not alter the represented operational system, task, error criterion, or attainable capability values.

For a presentation pi, define its higher-order interaction mass

    J(pi) = sum_{T subseteq pi, |T|>=2} |m_pi(T)|,

where m_pi is the Boolean-lattice Mobius transform of v_pi. Consider the proposed quotient/minimized invariant

    J_* = inf_{pi in P_sem} J(pi),

where P_sem contains every semantics-preserving regrouping.

## Trivialization theorem
If P_sem contains the one-block coarsening pi_top={N}, then

    J_* = 0.

### Proof
J(pi)>=0 by definition. Under pi_top there is only one primitive block. Hence there exists no subset T of primitive blocks with |T|>=2. The defining sum for J(pi_top) is empty, so J(pi_top)=0. Therefore 0 <= J_* <= 0. QED.

The argument is independent of the numerical capability values, monotonicity, additivity, dimensions, and the particular four labels. It holds for every finite nonempty factor set.

## Stronger consequence
Any proposed intrinsic quantity that (i) is defined solely as a nonnegative penalty on interactions of order >=2 and (ii) minimizes over a semantics-preserving class containing unrestricted coarsening is identically zero. Therefore quotienting Audit-203 interaction order by *all* semantics-preserving regroupings destroys the very interaction signal it was intended to make invariant.

This is not repaired by replacing absolute Mobius mass with squared coefficients, positive-part synergy, maximum interaction order, or the count of nonzero higher-order coefficients: all vanish on a one-block presentation.

## Edge checks
- Single primitive initially: already zero.
- Constant v: zero in every presentation.
- Pure four-way AND: nonzero four-way coefficient in the fine presentation, zero higher-order coefficient after one-block coarsening.
- OR: signed pair/higher coefficients in the fine presentation, again zero after one-block coarsening.
- Monotone/nonmonotone v: proof unchanged.
- Composition: trivial invariant remains zero, hence cannot provide a nontrivial composition law.
- Units/dimensions: Mobius coefficients inherit the units of v; absolute/squared variants require consistent normalization, but trivialization does not depend on units.

## Exact finite verification
`experiments/gc2_audit204_factorization_quotient_trivialization.py` enumerates all set partitions of four factors and checks representative Boolean capability functions. It confirms that the partition with one block always has zero higher-order interaction mass and hence the minimum over all partitions is zero.

## Prior-art collision boundary
The theorem itself is elementary. More broadly, general resource theories formulate resources and convertibility relative to declared free processes, while operational complexity measures require a declared admissible implementation/cost model. Thus allowing arbitrary regrouping for free erases structural distinctions; forbidding regrouping requires extra operational structure rather than a notation-independent quotient.

## Ledger
- Exact Mobius decomposition: IMPORTED/KNOWN.
- Interaction order under a fixed factorization: well-defined but presentation-dependent — PROVED.
- Minimize higher-order interaction over all semantics-preserving regroupings: TRIVIAL (identically zero) — PROVED.
- Factorization-quotiented interaction residual as nontrivial Omega_G: FALSIFIED under unrestricted semantics-preserving coarsening.
- Operationally identifiable *indecomposable interface atoms* with nonzero cost to fuse/split: OPEN.
- Invariant based on a nontrivial lattice/category of admissible interface factorizations with charged refinement/coarsening: OPEN.

## Surviving gate
GC-II cannot obtain an intrinsic novelty gap by quotienting away factorization while simultaneously allowing free arbitrary regrouping. A viable next theorem must make factorization operational: primitive interfaces must have experimentally or computationally testable independence/composability constraints, and fusion/splitting must itself be an admissible transformation with explicit cost. The candidate invariant must then survive comparison with general resource theories, tensor-factorization dependence, communication complexity, contextuality/marginal compatibility, and implementation complexity.
