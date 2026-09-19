# GC-II Audit 251 — exact min-plus accounting for coupled targets

Status: PROVED where explicitly stated; generic rectangle-cover/min-plus machinery is IMPORTED/KNOWN. No novelty claim is made for Boolean rectangle covers, shortest paths, or min-plus dynamic programming.

## 1. Setting

Let the operational state factor as

\[
X=\prod_{j=1}^m X_j.
\]

Assume the independent asynchronous regime isolated in Audit 250:

1. every primitive operation acts on exactly one coordinate j;
2. its enabling predicate, successor and nonnegative cost depend only on that coordinate;
3. there are no cross-coordinate prerequisites, synchronization constraints, shared budgets, or state-dependent cross-costs;
4. arbitrary interleavings of enabled local operations are permitted.

Let \(d_j(a,b)\in[0,+\infty]\) be the local minimum cost from \(a\) to \(b\), and

\[
d_j(a,S)=\inf_{b\in S}d_j(a,b),\qquad d_j(a,\varnothing)=+\infty.
\]

For an arbitrary capability target \(F\subseteq X\), let \(V_F(x)\) be minimum operational cost to reach F.

## 2. Exact endpoint normal form

### Theorem 251.1 (endpoint min-plus form) — PROVED

For every finite product system satisfying the assumptions above,

\[
\boxed{V_F(x)=\min_{y\in F}\sum_{j=1}^m d_j(x_j,y_j).}
\]

The same statement holds with infima in an infinite system whenever the local distances and global value are defined as path-cost infima.

### Proof

Any global path from x to y projects to a local path from \(x_j\) to \(y_j\) in each coordinate. Because every global step belongs to exactly one coordinate and total path cost is the sum of primitive nonnegative costs, every x-to-y path costs at least \(\sum_j d_j(x_j,y_j)\).

Conversely, choose local paths whose costs approach the local infima. Independence permits arbitrary interleaving/concatenation of these paths, producing a global x-to-y path whose cost approaches their sum. Hence the product-state distance is the sum of local distances. Minimizing over \(y\in F\) gives the result. QED.

This is an exact nonlinear accounting law: target coupling appears through the outer minimum, even though the generators themselves are completely independent.

## 3. Rectangle normal form

A nonempty rectangle is

\[
R=R_1\times\cdots\times R_m,\qquad \varnothing\ne R_j\subseteq X_j.
\]

Suppose

\[
F=\bigcup_{r=1}^q R^{(r)}
\]

is an exact rectangle cover (every rectangle lies inside F and their union is F).

### Theorem 251.2 (min of additive modes) — PROVED

\[
\boxed{
V_F(x)=\min_{1\le r\le q}\sum_{j=1}^m d_j\!\left(x_j,R_j^{(r)}\right).
}
\]

Proof: minimum distance to a union is the minimum of distances to its members; Audit 250's rectangular decomposition applies inside each rectangle. QED.

Thus Audit 250 is exactly the q=1 boundary. Nonrectangular targets do not destroy exact accounting; they require multiple additive modes joined by a min-plus selector.

## 4. Target interaction rank

For finite F define

\[
\rho_\square(F)=\min\{q:F\text{ is the union of }q\text{ nonempty rectangles contained in }F\}.
\]

For \(F=\varnothing\), set \(\rho_\square(F)=0\).

### Proposition 251.3 — PROVED

For nonempty finite F,

\[
\rho_\square(F)=1\iff F\text{ is rectangular}.
\]

Every finite target has \(\rho_\square(F)\le |F|\) by its singleton cover. Therefore \(\rho_\square\) is a finite target-coupling complexity in the finite model, and Theorem 251.2 gives an exact representation with \(\rho_\square(F)\) additive modes.

Important: this is a structural representation count, not a physical resource, information, action or rule cost. It must not be inserted into R/I/A/L equations without an operational realization model.

## 5. Why this matters for GC-II

Audits 249–250 showed that arbitrary target coupling falsifies one-mode additive accounting. Audit 251 gives the exact replacement in the independent-generator regime:

\[
\boxed{\text{independent generators + coupled target}\Rightarrow\text{min-plus mixture of additive typed costs}.}
\]

This supplies a concrete nonlinear interaction term without pretending additivity. It also separates two questions that had been conflated:

- generator interaction: cross-coordinate prerequisites/effects/costs;
- target interaction: number/geometry of separable target modes.

The present theorem solves only the second under independent dynamics.

## 6. Edge cases and invariances

- Empty target: \(V_F=+\infty\); the nonempty-cover formula is not invoked.
- Starting state already in F: one covered rectangle contains x, all its local set-distances are zero, hence V=0.
- Unreachable local coordinate: corresponding distance is +infinity; extended-real min-plus arithmetic handles it.
- Zero-cost cycles: harmless because costs are nonnegative and distances are infima.
- Relabeling states or coordinates: preserves the formula and rectangle rank.
- Positive rescaling of all costs by alpha: rescales V and every d_j by alpha while leaving rectangle rank unchanged.
- Composition: adding independent coordinates preserves endpoint additivity; target rectangle rank need not multiply exactly and therefore no multiplicative law is claimed.
- Degenerate one-coordinate case: every target is rectangular and rho=1 when nonempty.

## 7. Prior-art collision boundary

Boolean rectangle covers/biclique covers, nondeterministic communication complexity, tropical/min-plus algebra, factored shortest paths and dynamic programming are established areas. Accordingly:

- rectangle cover number: IMPORTED/KNOWN;
- min-plus selection over alternatives: IMPORTED/KNOWN;
- product shortest-path additivity: IMPORTED/KNOWN;
- use as the exact target-coupling normal form inside the present GC-II audit chain: PROVED, but not by itself claimed as a new mathematical field result.

The remaining breakthrough target is stronger: derive an operationally justified bound when generator coupling is also present, and determine whether GC's projection/generation semantics constrain the number or cost of interaction modes more sharply than generic planning/CSP/communication-complexity theory.

## 8. Ledger

- Endpoint min-plus formula: PROVED.
- Rectangle-cover min-of-additive-modes formula: PROVED.
- rho_square=1 iff rectangular for nonempty finite F: PROVED.
- Universal one-mode additive accounting for arbitrary F: FALSIFIED by Audit 249/250.
- Rectangle cover / min-plus machinery as generic novelty: IMPORTED/KNOWN.
- Operational R/I/A/L cost of selecting or generating a rectangle mode: OPEN.
- Coupled-generator extension with a nontrivial GC-specific bound: OPEN.
