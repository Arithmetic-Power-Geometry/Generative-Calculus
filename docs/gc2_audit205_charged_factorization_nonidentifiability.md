# GC-II Audit 205 — charged factorization does not identify an intrinsic novelty gap

## Status

- Fixed-factor Möbius interaction: **IMPORTED/KNOWN**.
- Audit-204 unrestricted regrouping collapse: **PROVED**.
- Charging fusion/splitting can prevent the zero collapse for a fixed cost model: **PROVED**.
- Capability semantics alone uniquely determine the charged-factorization residual: **FALSIFIED**.
- Empirically grounded typed fusion/splitting cost as part of the operational system: **OPEN**.

## Setup

Let `N={R,I,A,L}` and let `Pi(N)` be its partition lattice. A partition `pi` is an operational factorization. For capability value `v`, let

`J_v(pi) = sum_{|T|>=2} |m_{v,pi}(T)|`,

where `m` is the Möbius transform on the blocks of `pi`. Starting from a distinguished fine factorization `pi0`, a natural charged residual is

`K_c(v;pi0) = inf_{pi in Pi(N)} [ J_v(pi) + c(pi0 -> pi) ]`.

Here `c` is the cost of admissible fusion/splitting/re-factorization.

## Proposition (cost-model nonidentifiability)

Assume `J_v(pi0)=j0>0` and the one-block coarsening `top` is semantics-preserving, so `J_v(top)=0`. Then the same capability semantics `v` admits cost models with different values of `K_c`.

**Proof.** Under `c_free(pi0->pi)=0` for every partition, `K=0` by choosing `top`. Under `c_locked(pi0->pi0)=0` and `c_locked(pi0->pi)=M` for every `pi != pi0`, where `M>j0`, the fine factorization costs `j0`, while every other candidate costs at least `M>j0`; hence `K=j0`. The capability function and regrouping semantics are unchanged; only the operational cost declaration changes. QED.

The same construction permits intermediate values by assigning suitable costs. Therefore charging regrouping fixes Audit 204 only *relative to a specified operational cost model*. It does not recover an intrinsic invariant from capability semantics alone.

## Edge checks

- If `j0=0`, both models can yield zero; this is a degenerate no-interaction case and does not rescue identifiability.
- Costs are nonnegative and have zero identity cost in both witnesses.
- No additivity assumption is used.
- The result does not say operational costs are arbitrary in a physical application. It says GC-II must measure/derive them rather than choose them to manufacture a residual.
- If fusion is physically forbidden, the admissible partition family itself becomes part of the system specification; the resulting invariant is operationally relative, not semantics-only.

## Prior-art boundary

General resource theories are defined relative to declared free operations and constraints; costs and monotones acquire operational meaning only after those choices are fixed. Audit 205 therefore does not claim that cost-relative convertibility is new. The possible GC-II novelty must instead lie in a testable coupling between typed capability generation and independently measurable resource/information/action/rule conversion costs.

## Next gate

Do not search for another purely formal quotient. Define a **typed operational atom** by an interventionally testable interface: two atoms may be fused for free only if every admissible task/probe/cost experiment is unchanged under the fusion. Then test whether this operational equivalence is itself nontrivial or simply behavioral equivalence/bisimulation. If it collapses to bisimulation, record the collision. If not, seek a lower bound on the minimum physical fusion cost and connect it to `Omega_G` without assuming additivity.

Exact verifier: `experiments/gc2_audit205_charged_factorization_nonidentifiability.py`.