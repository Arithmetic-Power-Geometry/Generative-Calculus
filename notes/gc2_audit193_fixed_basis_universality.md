# GC-II Audit 193 — Fixed reusable basis universality no-go

## Question
Does replacing Audit 192's one-witness-per-minimal-enabler construction by a fixed reusable primitive algebra create a strict representability boundary for finite monotone capability closure?

## Result
**No, not without an additional complexity/resource restriction.**

Let `E={e_1,...,e_n}` be acquired Boolean tokens and let `F:2^E -> 2^X` be any finite monotone set-valued closure map. For each capability `x in X`, define the monotone Boolean coordinate

`f_x(S)=1 iff x in F(S)`.

Let `M_x` be the inclusion-minimal subsets `T subseteq E` with `f_x(T)=1`. Then

`f_x(S) = OR_{T in M_x} AND_{e in T} 1[e in S]`.

The empty conjunction is TRUE and the empty disjunction is FALSE. Hence the same fixed reusable primitive basis `{AND, OR, TRUE, FALSE}` realizes every coordinate and therefore every finite monotone set-valued map. No capability-specific primitive transformation is required; only the wiring/program changes.

### Theorem — Fixed-Basis Monotone Universality
For every finite monotone `F:2^E -> 2^X`, there exists a finite acyclic circuit over the fixed basis `{AND, OR, TRUE, FALSE}` whose output vector is exactly the indicator vector of `F(S)` for every `S subseteq E`.

**Proof.** For each `x`, monotonicity implies that if `f_x(S)=1`, finite descent reaches an inclusion-minimal true set `T subseteq S`. Conversely if `T in M_x` and `T subseteq S`, monotonicity gives `f_x(S)=1`. Thus the displayed monotone DNF is exact. Parallel composition over `x in X` gives the set-valued result. QED.

## Consequences
1. Fixed reusable primitive vocabulary alone does **not** restrict finite monotone closure maps.
2. Bounded primitive arity alone also does not help: binary AND/OR suffice by tree composition.
3. Any strict GC-II boundary must constrain at least one of circuit/program size, depth, fan-out/reuse, uniformity, locality/topology, online memory, resource budget, admissible wiring/composition, or another operational quantity.
4. Once such restrictions are imposed, the immediate collision class is monotone circuit/formula/branching-program complexity. Therefore a GC-II translator lower bound must be stated operationally and then shown not to be merely a renamed standard circuit lower bound.

## Stress checks
- Constant-empty closure: represented by FALSE.
- Always-present capability: represented by TRUE (empty conjunction).
- Singleton enablers: represented directly by token wires.
- Higher-order synergy: represented by AND trees.
- Multiple alternative enablers: represented by OR of AND terms.
- Monotonicity: automatic under AND/OR.
- Composition: arbitrary finite fan-in is reducible to binary trees, so bounded arity 2 does not alter extensional universality.
- Degenerate `E=empty`: only constant coordinates occur and are represented by TRUE/FALSE.

## Exact experiment
`experiments/gc2_audit193_fixed_basis_universality.py` exhaustively enumerates every scalar monotone Boolean map for `|E|<=2` and verifies exact reconstruction from minimal true sets. Set-valued maps are coordinate products, so this covers every `F` for `|E|,|X|<=2`.

Expected scalar counts are 2, 3, and 6 for 0, 1, and 2 inputs respectively.

## Prior-art collision
The representation is classical monotone Boolean logic: AND/OR form a complete basis for monotone Boolean functions, and monotone circuit complexity studies the size required by this fixed basis. Thus the theorem is useful as a GC-II no-go boundary, not as an independent novelty claim.

## Ledger
- Fixed-Basis Monotone Universality: **PROVED / IMPORTED-KNOWN mechanism**.
- Fixed reusable primitive basis as a strict extensional GC-II representability boundary: **FALSIFIED**.
- Bounded primitive arity alone as a strict boundary: **FALSIFIED**.
- Quantitative lower bounds under bounded size/depth/locality: **OPEN for GC-II novelty; strongly collides with known monotone complexity**.
- Operational local-to-global translator bound escaping ordinary circuit complexity: **OPEN**.

## Next gate
Search for a restriction tied to GC's operational semantics rather than syntax: candidate target is **budgeted compositional realization with locality-constrained interfaces**, where the same local primitive library is available but global capability requires transporting/merging information across an interaction graph. Any claimed lower bound must then be collision-tested against monotone circuits, communication complexity, distributed computation, CSP width, and network coding before being promoted.
