# GC-II Audit 079 — Typed Closure Integrability / Obstruction

Status: **PROVED finite exact criterion; FALSIFIED as standalone GC-II novelty; OPEN only beyond ordinary potential/cohomology and monotone theory**

Branch scope: `gc2-capability-accounting-lab` only. GC-I `main` is frozen.

## 1. Candidate under attack

Audit 078 left a candidate in which a finite complete operational quotient carries directed conversion edges and a typed accounting increment

`c(e) = (Delta R, Delta I, Delta A, Delta L) in R^4`.

The hoped-for GC-II statement was an equivalence among path-independent capability accounting, potential/dual representation, vanishing cycle defects, and a finite computable test.

## 2. Exact finite integrability theorem

### Theorem 079.1 (typed edge-potential criterion)

Let `G=(V,E)` be a finite directed graph. Let `c:E->R^d` be a typed edge increment. Assume the comparison is made on a connected component of the underlying graph and that a reversed traversal contributes the negative of the forward increment when forming signed path integrals. The following are equivalent:

1. there exists `Phi:V->R^d` such that for every edge `u->v`,
   `c(u,v)=Phi(v)-Phi(u)`;
2. the signed sum of `c` along every closed walk is zero;
3. the signed sum vanishes on any cycle basis of the underlying graph;
4. for one root `r`, assigning `Phi(v)` by the signed sum along any spanning-tree path from `r` to `v` reproduces every non-tree edge exactly.

**Proof.** (1)->(2) telescopes. (2)->(3) is immediate. (3)->(4): each non-tree edge plus the unique tree path closes a fundamental cycle, so zero cycle sum forces equality with the tree-induced potential difference. (4)->(1) holds on tree and non-tree edges. The vector result follows coordinatewise. QED.

### Corollary 079.1a

For a typed `R,I,A,L` ledger, exact additive path-independent accounting is decidable in finite time by one spanning-tree propagation plus edge checks. A failed edge produces an explicit fundamental-cycle certificate.

## 3. What this does and does not prove

This theorem is mathematically exact, but it is not a GC-II breakthrough. It is the finite-graph version of the standard fact that a discrete 1-form is exact iff all periods/cycle integrals vanish. In optimization language, related potential criteria are equivalent to absence of inconsistent cycle constraints. In differential language, path independence is exactness. The typed vector version is simply coordinatewise repetition.

Therefore the equivalence

`path independence <-> potential <-> zero cycle defect <-> finite test`

is **FALSIFIED as standalone novelty**.

## 4. Nonnegative consumed-resource ledgers expose an additional mismatch

Physical consumption charges usually satisfy `c(e) in R_+^d`. If the graph contains a directed cycle with any strictly positive total consumption, then no endpoint-difference potential can reproduce the consumed ledger around that cycle, because endpoint differences telescope to zero. This is ordinary dissipation/consumption, not a new obstruction.

Thus one must distinguish:

- **state-function change**: signed quantity that may admit a potential;
- **path cost/consumption**: nonnegative quantity that generally does not;
- **feasibility frontier**: a set-valued/Pareto object not determined by a single additive potential.

Conflating these would manufacture a false GC-II curvature.

## 5. Exact exhaustive finite-world experiment

`experiments/gc2_integrability_exhaustive.py` enumerates every edge labeling of complete bidirected graphs on `n=2,3,4` vertices with scalar labels in `{-1,0,1}`. For each labeling, it constructs the root-induced candidate potential and checks all directed edges.

Exact counts:

| n | directed edges | assignments checked | integrable assignments |
|---|---:|---:|---:|
| 2 | 2 | 9 | 3 |
| 3 | 6 | 729 | 7 |
| 4 | 12 | 531441 | 15 |

Across all `532179` assignments the implementation criterion and direct edge-potential consistency test agree exactly. The generated summary is stored in `results/gc2_integrability_exhaustive.csv`.

These counts are computational consistency checks of the finite theorem, not evidence of novelty.

## 6. Prior-art collision boundary

The mathematical skeleton already occurs in several established domains:

- exact differential/discrete forms: zero periods characterize exactness/path independence;
- graph potentials and difference constraints: cycle consistency characterizes feasible potentials;
- thermodynamics: state functions differ from path-dependent work/dissipation;
- resource theories: convertibility is commonly characterized by one or families of monotones, and complete families may be infinite or fail to admit finite additive descriptions;
- asymptotic spectra: suitable preordered algebraic structures can admit complete asymptotic families of monotone homomorphisms.

Hence a GC-II theorem must add structure not reducible to these.

## 7. Stronger no-go for a universal finite complete potential family

A universal claim that every completed operational theory admits a fixed finite family of scalar monotones that completely characterizes conversion is untenable. General resource theories may require infinite/discontinuous monotone families, and finite complete monotone families do not exist in broad quantum-resource settings. Therefore Paper-II cannot assume finite-dimensional integrability as a general law.

Status: **FALSIFIED as a universal premise**.

## 8. Surviving target

The remaining nontrivial target is not ordinary integrability. It is a **set-valued typed closure obstruction** for Pareto conversion frontiers:

`F(x,z) subseteq ParetoHull(F(x,y) + F(y,z))`

with equality generally failing because intermediate-state restrictions, catalysts, information release, approximation, or composition can change achievable frontiers.

A potentially meaningful GC-II object would have to quantify the minimal typed augmentation needed to repair a *frontier-composition defect* after quotienting ordinary path costs, convexification, catalysts, asymptotics, and known resource-theory monotones.

That candidate is **OPEN**. It must next be collision-tested against multiobjective shortest paths, set-valued dynamic programming, infimal convolution, network calculus, tropical/idempotent semirings, profunctor/enriched-category composition, and resource-theory catalysis.

## 9. Status table

| Claim | Status |
|---|---|
| finite typed edge ledger has a potential iff all signed cycle defects vanish | PROVED |
| a cycle-basis/spanning-tree test is complete in the finite exact case | PROVED |
| exhaustive n=2..4 enumeration matches the criterion | NUMERICALLY SUPPORTED / exact enumeration |
| the above equivalence is itself GC-II novelty | FALSIFIED |
| positive consumed-resource loop cost implies new closure curvature | FALSIFIED |
| every operational theory admits a finite complete monotone/potential family | FALSIFIED as universal premise |
| a genuinely set-valued typed frontier-composition obstruction remains | OPEN |

No breakthrough claim is made in Audit 079.