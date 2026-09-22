# GC-II Audit 323 — Branchwise Pairwise Persistence

## Purpose
Audit 322 showed that finite pairwise separators at the root do not imply a finite joint resolving policy when admissibility may disappear after an observation. Audit 323 asks for a strictly weaker replacement for global/hereditary admissibility that is still sufficient for quantitative joint resolution.

## Finite operational model
Let `B` be a finite current uncertainty cell. Each world `x in B` has a required decision `g(x)`. An admissible test `u` at cell `C subseteq B` has nonnegative cost `c_C(u)` and a finite deterministic outcome map `Z_u:C -> Y_u`. The child after outcome `y` is

`C_{u,y}={x in C: Z_u(x)=y}`.

A cell is resolved when `g` is constant on it. Let `k(C)=|g(C)|`, the number of decision classes still represented.

The optimal worst-case resolving cost is

`V(C)=0` for resolved `C`, and otherwise

`V(C)=min_{u in Adm(C)} [ c_C(u) + max_{y:C_{u,y} nonempty} V(C_{u,y}) ]`,

with `V(C)=+infinity` if no finite resolving policy exists.

## Branchwise pairwise persistence (BPP)
Fix `P>=0`. BPP(P) holds on a family of reachable cells if, for every unresolved reachable cell `C` and every pair `x,x' in C` with `g(x)!=g(x')`, there exists a test `u in Adm(C)` such that

1. `Z_u(x)!=Z_u(x')`, and
2. `c_C(u)<=P`.

This condition is branch-relative. It does **not** require the same test to remain admissible after restriction, does **not** require `Adm(C')` to contain `Adm(C)` or vice versa, and allows the available test family and costs to change with the observation history.

## Theorem 323.1 — Dynamic pairwise-to-joint bound
Assume a finite deterministic model with nonnegative test costs. If BPP(P) holds at every unresolved cell reachable under the construction below, then for every such cell C,

`V(C) <= (k(C)-1) P`.

In particular, if the root has K decision classes,

`V(B) <= (K-1)P`.

### Proof
Induct on `k(C)`.

Base `k(C)=1`: C is resolved, so `V(C)=0`.

Induction step: let `k(C)=k>=2`. Pick any two worlds `x,x'` in different decision classes. By BPP(P), there is an admissible test u of cost at most P separating them. Therefore no nonempty child of u can contain all k decision classes: the classes containing x and x' occur in different children. Hence every child C_y satisfies `k(C_y)<=k-1`. BPP(P) is assumed on the reached unresolved children, so by induction `V(C_y)<=(k(C_y)-1)P <= (k-2)P`. Thus

`V(C) <= c_C(u)+max_y V(C_y) <= P+(k-2)P=(k-1)P`.

QED.

## Theorem 323.2 — Tightness
The coefficient K-1 is sharp even under BPP(P). For K singleton decision classes, let the only useful tests be singleton membership tests, each of cost P, and make them admissible at every unresolved cell where their queried class remains possible. An adversary can return the non-singleton outcome K-1 times. Hence

`V=(K-1)P`.

Thus no universal smaller coefficient can replace K-1 under BPP alone.

## Strict weakening of hereditary admissibility
BPP does not imply hereditary admissibility. Example with worlds {a,b,c}: at the root allow tests {u_ab,u_ac,u_bc}; after the first observation, remove every root test and introduce fresh branch-specific tests v_C that separate the remaining decision classes. The admissible sets are not hereditary, yet BPP(1) holds at every unresolved reached cell and Theorem 323.1 applies.

Conversely, Audit 322 violates BPP after the first negative singleton outcome: the unresolved two-class child has no admissible separator. This pinpoints the exact failure used by that deadlock construction.

## What is and is not established
- **PROVED:** BPP(P) is sufficient for finite joint resolution and gives `V <= (K-1)P`.
- **PROVED:** the coefficient K-1 is tight under BPP alone.
- **PROVED:** global/hereditary persistence of a fixed test catalogue is stronger than necessary.
- **FALSIFIED (Audit 322):** root-only pairwise separability is sufficient.
- **NOT CLAIMED:** BPP is necessary for finite resolution. A resolving policy may use a multiway test without supplying a cheap direct separator for every incompatible pair at every off-policy cell.
- **OPEN:** weakest policy-relative persistence condition yielding a nontrivial bound when costs/resources depend on accumulated history rather than only the current uncertainty cell.

## Edge and degenerate cases
- K=1 gives V=0 exactly.
- P=0 gives V=0 under BPP(0); this is consistent because the inductive policy uses only zero-cost tests.
- Empty outcome cells are ignored.
- Tests that do not reduce the number of decision classes in some child are allowed generally; the proof deliberately selects a separator of two distinct decision classes, which guarantees every child loses at least one of those two classes.
- Multiple worlds may share one decision class; the theorem depends on K=|g(C)|, not |C|.
- Costs may be cell-dependent; only the uniform branchwise upper bound P is used.

## Composition / invariance checks
The statement is invariant under relabeling worlds, decision labels, tests, and outcomes. Rescaling all costs by alpha>=0 rescales P and V by alpha. No additivity across independent systems is assumed. For product systems, a bound must be derived from the product admissibility rule; BPP is not automatically preserved by arbitrary coupling constraints.

## Prior-art collision note
The Bellman/decision-tree mechanism is imported/known. Costed adaptive diagnosis, discrete-function evaluation, and precedence/constrained sequential testing are established neighboring areas. Audit 323 therefore does not claim invention of adaptive decision trees or their recurrence. The GC-II use is narrower: it isolates the branchwise persistence assumption that repairs the precise root-pairwise failure exposed by Audit 322 while being strictly weaker than a hereditary fixed action catalogue.

## Paper-II consequence
Any proposed Generative Novelty Gap or closure-escape account that uses local witness costs must specify *where along information branches those witnesses remain available*. Root-only witness accounting is invalid. A defensible finite deterministic accounting layer can use a branchwise persistence certificate `(K,P)` to obtain the sharp worst-case envelope `(K-1)P`, while explicitly marking models without such a certificate as outside this bound.
