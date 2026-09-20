# GC-II Audit 268 — Typed Closure-Escape theorem

## Scope
Finite operational systems with additive nonnegative typed costs in `R_+^d`. The baseline attainable path-cost set is `B`; an extension has attainable set `E`, with `B subseteq E` (the extension preserves all baseline transformations). Feasibility at budget `q` means some attainable vector is componentwise at most `q`.

## Theorem candidate: finite typed Closure-Escape equivalence

Let `P(E)` be the nondominated (Pareto-minimal) vectors of `E`. Under the scope above, the following are equivalent:

1. **Operational escape:** there exists a typed budget `q` feasible in the extension but infeasible in the baseline.
2. **Geometric escape:** there exists `e in P(E)` such that no `b in B` satisfies `b <= e` componentwise.
3. **Upper-image escape:** `Up(E)` strictly contains `Up(B)`, where `Up(S)={q : exists s in S, s <= q}`.
4. **Nonlinear-certificate escape:** there exists `q >= 0` with `rho_E(q) <= 1 < rho_B(q)`, using the extended max-ratio certificate of Audit 267.

Status: **PROVED (finite additive nonnegative typed semantics)**.

### Proof
`1 <=> 3` is the definition of the feasible upper image. `1 => 2`: choose an extension-feasible witness `x <= q` and descend in the finite set `E` to a Pareto-minimal `e <= x`. If some baseline `b <= e`, then `b <= q`, contradicting baseline infeasibility. `2 => 1`: choose budget `q=e`. It is extension-feasible, while any baseline-feasible vector at `q` would be a `b <= e`, excluded by hypothesis. `1 <=> 4` follows from Audit 267's exact finite identity `q feasible in S <=> rho_S(q)<=1`.

## Corollary: No-Free-Capability under conservative extension
If `E=B`, no typed budget can escape. More generally, if every new extension vector is dominated by a baseline vector, `Up(E)=Up(B)` and no new budgeted capability exists. Thus merely adding generators is not sufficient for generative novelty; at least one new nondominated operational tradeoff is necessary and sufficient in this semantics.

Status: **PROVED**, but the abstract monotonicity/dominance mechanism is **IMPORTED/KNOWN** from multiobjective/resource-constrained shortest-path theory. It must not be advertised as a generic mathematical novelty.

## Sharp witness
Baseline `B={(0,3),(3,0)}` and extension `E=B union {(2,2)}`. Budget `(2,2)` is an escape although Audit 266 proved that all nonnegative linear scalarizations give the same optimum on `B` and `E`. Audit 267's nonlinear certificate separates them: `rho_B(2,2)=3/2`, `rho_E(2,2)=1`.

This shows that the operational/geometric equivalence survives unsupported Pareto points and does not require convexity.

## Domain and edge audit
- Empty baseline: any nonempty extension creates an escape; handled by extended `rho=+infinity`.
- Empty extension with `B subseteq E`: forces empty baseline; no escape.
- Zero budget coordinates: handled by Audit 267's extended ratio convention.
- Degenerate extension `E=B`: no escape.
- Positive coordinate rescaling: componentwise dominance and escape are invariant under coherent unit changes.
- Composition: theorem applies to the composed attainable set, but no claim of additive escape magnitude is made.
- Infinite attainable sets: **CONDITIONAL/OPEN** without closure/attainment assumptions; the finite descent step must be replaced by suitable compactness/minimality assumptions.
- Nonadditive information, replenishable resources, labelled actions/rules, stochastic transitions: **OPEN**; this theorem does not silently cover them.

## Exact verification
`experiments/gc2_audit268_typed_closure_escape.py` exhausts all 81 nested baseline/extension pairs on the two-dimensional `{0,1}^2` cost grid and performs 972 exact assertions over budget feasibility, nonlinear threshold equivalence, and conservative-extension monotonicity. It finds 43 strict-escape systems and checks the Audit-266 unsupported-tradeoff witness separately.

## Prior-art collision boundary
Dominance labels, Pareto frontiers, and multidimensional resource-budget feasibility are standard in resource-constrained and multiobjective shortest-path optimization. The generic fact that nondominated labels determine budget feasibility is therefore **IMPORTED/KNOWN mechanism**. The scientifically defensible GC-II use is narrower: this theorem pins down the exact Closure-Escape criterion for the typed operational semantics developed in Audits 265–267 and identifies the witness that any nontrivial Generative Novelty Gap must measure.

## Ledger
- Conservative-extension feasibility monotonicity: **PROVED / IMPORTED-KNOWN mechanism**.
- Finite typed Closure-Escape equivalence (operational/geometric/upper-image/nonlinear certificate): **PROVED**.
- Adding generators alone implies novelty: **FALSIFIED**.
- New nondominated typed tradeoff iff budgeted escape: **PROVED**.
- Linear-price witness completeness: **FALSIFIED** (Audit 266).
- Nonlinear max-ratio threshold witness completeness: **PROVED finite** (Audit 267).
- Infinite-set closure/attainment generalization: **CONDITIONAL/OPEN**.
- Typed quantitative `Omega_G` magnitude satisfying useful composition bounds: **OPEN**.
