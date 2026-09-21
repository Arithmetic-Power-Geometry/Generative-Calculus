# GC-II Audit 303 — Task-relative Generative Novelty Gap and Closure-Escape criteria

## Purpose

Audit 302 fixed the typed budgeted operational closure. This audit attacks the next priority: define a novelty quantity that is operationally testable, is not merely cardinality of a set difference, and admits exact operational/geometric/computational escape criteria. The separation machinery below is standard convex analysis/resource-theory territory; novelty is not claimed for support functions, separating hyperplanes, or operational task advantages.

## Common comparison frame

Compare a baseline typed system `S0` and an augmented system `S1` only after fixing independently of the comparison:

1. a common capability universe `Y`;
2. budgets `b0,b1` with stated units and accounting conventions;
3. a common capability map into `Y` (or a declared interoperability map);
4. a task family `U` of dimensionless utilities `u:Y->[0,1]`.

Let `K_j = Cap_{b_j}(S_j) subseteq Y`. Before comparison, saturate every system under all explicitly zero-charged admissible transformations. Thus mere revelation/exposure already available through zero-charge traces is part of its baseline closure rather than counted as generated novelty.

## Definition 303.1 — task-relative Generative Novelty Gap

For nonempty reachable capability sets define

`V_u(K)=sup_{y in K} u(y)`

and

`Omega_G^U(S1:S0)=sup_{u in U} [V_u(K1)-V_u(K0)]_+`.

`Omega_G^U` is dimensionless and lies in `[0,1]`. It measures maximal independently specified task advantage, not the number of newly named outputs.

Important: if `U` is chosen after inspecting `K0,K1`, the quantity can be gamed. The task family must therefore be fixed independently or justified externally.

## Basic properties

**Proposition 303.1 (PROVED).** `0 <= Omega_G^U <= 1`.

**Proposition 303.2 (PROVED).** If `K1 subseteq K1'`, then `Omega_G^U(K1:K0) <= Omega_G^U(K1':K0)`. If `K0 subseteq K0'`, then `Omega_G^U(K1:K0') <= Omega_G^U(K1:K0)`.

Both follow immediately from monotonicity of suprema. Type-preserving relabelings that transport `U` with the capability labels preserve `Omega_G^U`.

`Omega_G^U` is directional and generally asymmetric. It is not a metric and no triangle inequality is claimed.

## Exact set-escape specialization

For finite `Y`, take the independently fixed indicator family `U_ind={u_y:y in Y}`, where `u_y(x)=1[x=y]`.

**Theorem 303.1 (finite operational escape; PROVED).**

`Omega_G^{U_ind}(K1:K0)>0  iff  K1 not subseteq K0`.

Moreover the gap is binary: it equals 1 exactly when an augmented reachable capability escapes the baseline reachable set, and 0 otherwise.

**Proof.** If `y in K1\K0`, task `u_y` has augmented value 1 and baseline value 0. Conversely, if every augmented capability belongs to `K0`, every indicator task attainable by `K1` is also attainable by `K0`, so no positive advantage exists. QED.

This theorem is deliberately elementary; its role is to anchor the operational definition to exact closure escape.

## Geometric specialization

Fix independently a feature map `phi:Y->R^m`. Let `P_j=conv(phi(K_j))`. Use normalized linear tasks `u_d(y)=d dot phi(y)` with `||d||_*<=1`; if needed, apply a common affine normalization to a bounded feature domain. Define the support advantage

`Omega_lin(K1:K0)=sup_{||d||_*<=1} [h_{P1}(d)-h_{P0}(d)]_+`,

where `h_P(d)=sup_{p in P} d dot p`.

**Theorem 303.2 (Closure-Escape trichotomy; PROVED, separation mechanism IMPORTED/KNOWN).** For finite capability sets in finite-dimensional feature space, the following are equivalent:

1. `Omega_lin(K1:K0)>0`;
2. `P1 not subseteq P0`;
3. there exists a normalized linear task direction `d` for which the augmented system strictly outperforms the baseline system.

**Proof.** (3) is the definition of positive support advantage, so (1)<->(3). If `P1 subseteq P0`, support functions obey `h_P1(d)<=h_P0(d)` for every `d`, ruling out (1). If `P1` is not contained in the closed convex polytope `P0`, choose `p in P1\P0`; finite-dimensional strong separation gives a direction `d` with `d dot p > h_P0(d)`. Rescale `d` into the dual unit ball. Since `p in P1`, `h_P1(d)>=d dot p`, hence positive support advantage. QED.

This is a non-cardinality operational/geometric/computational criterion, but the separating-hyperplane theorem and support-function characterization are standard convex analysis and closely aligned with operational resource-theory witness constructions. Therefore the mathematical mechanism is **IMPORTED/KNOWN**.

## Computational criterion

For finite `K0,K1` and rational feature vectors, geometric escape is decidable by linear programming: for each augmented feature point, test membership in `conv(phi(K0))` using nonnegative convex weights summing to one. A failed membership test supplies an escape point; LP duality/separation can supply a witnessing task direction. This is polynomial-time in the explicit rational representation under standard LP assumptions. **IMPORTED/KNOWN algorithmic mechanism.**

## Why convexification matters

A raw new output need not constitute linear-task novelty. If `phi(y_new)` lies inside `conv(phi(K0))`, then no linear task in the declared feature representation can witness an advantage even though `y_new` is set-theoretically new. Thus:

`set escape` does not imply `linear operational escape`

unless the task family is rich enough (for example all indicators on finite `Y`). This prevents output relabeling or interpolation from automatically becoming positive geometric novelty.

## No-Free-Capability consequence

Audit 302 falsified a resource-only theorem. Audit 303 sharpens the necessary condition without making it tautological:

If all transformations newly available in `S1` are zero-charged across every declared channel and those transformations are already included in the baseline zero-charge saturation, then `K1 subseteq K0` and every task-relative novelty gap above is zero.

This statement is correct but structurally close to closure semantics, so it is **PROVED but NOT promoted as the desired No-Free-Capability breakthrough**. The open target remains a theorem deriving zero novelty from weaker independently checkable constraints on resource, information, interface/action, and rule deltas.

## Exact exhaustive collision test

`experiments/gc2_audit303_novelty_gap_exhaustive.py` exhausts all ordered pairs of nonempty capability subsets for universes of size 1 through 4 and all one-dimensional feature maps into `{-1,0,1}`. It checks:

- indicator-task positive gap iff exact set escape;
- normalized 1D linear-task positive gap iff the augmented feature set escapes the baseline convex hull.

Independent execution produced 284 subset-pair checks and 19,632 feature-map checks with no counterexample.

These experiments validate the finite implementation and edge cases; they are not evidence of theorem novelty.

## Edge/collision audit

- Empty reachable set: excluded from the value definition unless a bottom value convention is explicitly supplied.
- Constant task family: novelty is identically zero; task richness matters.
- Constant feature map: geometric novelty is identically zero even under set escape.
- Duplicate feature images: harmless; convex hull removes duplicates.
- Pure relabeling: invariant when tasks/features are transported with labels.
- Budget monotonicity: enlarging the augmented budget cannot decrease the gap; enlarging the baseline budget cannot increase it.
- Composition: no additivity is claimed. Supremum over tasks can create sub/super-additive behavior depending on the declared product task family.
- Units: utilities are dimensionless; heterogeneous physical resource coordinates are not added.
- Latent zero-cost exposure: absorbed by zero-charge saturation before novelty comparison.

## Prior-art collision status

Operational advantage over a restricted/free baseline, support-function witnesses, convex separation, resource monotones, and complete operational task families are established resource-theory ideas. Resource theories define free convertibility preorders and monotones, and recent work gives complete operational monotone families for broad dynamic resource theories. GC-II must therefore not claim those generic constructions as new.

The possible GC-II-specific contribution remains the joint typed accounting of physical resources, information, exposed interfaces/actions, and mutable rules together with budgeted closure, then proving bounds or impossibility results that genuinely depend on this multi-channel structure.

## Status

- Task-relative `Omega_G^U`: **DEFINITION FIXED / collision-aware**.
- Range, directional monotonicities, relabeling invariance: **PROVED**.
- Indicator-task set-escape equivalence: **PROVED**.
- Linear-task convex-hull Closure-Escape equivalence: **PROVED using IMPORTED/KNOWN separation theory**.
- LP computational criterion: **IMPORTED/KNOWN mechanism**.
- Claim that every set-theoretically new output is operationally novel: **FALSIFIED** for restricted task families.
- Generic operational advantage/support-function construction as GC-II novelty: **NOT CLAIMED**.
- Weak non-tautological No-Free-Capability theorem across DeltaR, DeltaI, DeltaA, DeltaL: **OPEN**.
- Quantitative multi-channel upper bound for `Omega_G`: **OPEN**.

## Next attack

Search for the weakest independently checkable channel-local assumptions under which a positive task-relative `Omega_G` forces at least one positive channel delta, without defining the channel charge by the capability conclusion itself. Then test whether any universal quantitative bound can survive channel synergies and zero-cost catalysts.