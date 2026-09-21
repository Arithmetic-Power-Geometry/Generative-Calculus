# GC-II Audit 292 — Interval-action tractability boundary

## Result

Audit 291 proves that unrestricted finite worst-case capability accounting is exactly SET COVER and is therefore NP-hard. This audit isolates a non-tautological operational subclass where the optimum is exact and polynomial-time computable.

Let the attainable states be a finite totally ordered set

\[
Y=\{y_1<\cdots<y_n\}.
\]

For tolerance \(\varepsilon\), every decoder action \(a\) has feasible set

\[
B_\varepsilon(a)=\{y\in Y:\ell(y,a)\le \varepsilon\}.
\]

Assume **interval feasibility**: for every action, \(B_\varepsilon(a)\) is empty or consecutive in the fixed order. Equivalently, each nonempty feasible set is \(\{y_i,\ldots,y_j\}\) for some \(i\le j\).

### Theorem 292.1 — Exact greedy accounting for interval-feasible actions

If all feasible-action sets are intervals in one common total order, the minimum number \(N_\varepsilon\) of decoder actions needed for worst-case \(\varepsilon\)-faithful accounting is computed exactly by:

1. take the leftmost uncovered state \(y_i\);
2. among all feasible actions containing \(y_i\), choose one whose interval has maximum right endpoint;
3. mark that interval covered and repeat.

If no action contains the current leftmost uncovered state, the instance is infeasible.

Hence, after interval endpoints are available, the problem is polynomial-time solvable (e.g. sorting plus a linear/near-linear scan, or a direct \(O(n|A|)\) implementation).

**Status: PROVED.**

### Proof

Let \(y_i\) be the leftmost uncovered state and let greedy choose interval \(G\), whose right endpoint is maximal among all intervals containing \(y_i\). Any feasible cover of the remaining states must contain some interval \(O\) covering \(y_i\). By greedy maximality, the right endpoint of \(G\) is at least that of \(O\). Because no state left of \(y_i\) remains to be covered, replacing \(O\) by \(G\) cannot uncover any still-required state: every still-required state covered by \(O\) lies between \(y_i\) and the right endpoint of \(O\), hence is also covered by \(G\). Thus there exists an optimum containing the greedy choice. Induction on the remaining uncovered suffix proves optimality. If no interval contains \(y_i\), no cover exists.

## Operational interpretation

The condition is not defined through the optimum cover number. It is an independently testable structural restriction on the loss/action interface: after ordering attainable states by a physically or operationally meaningful scalar coordinate, each decoder action is acceptable on one contiguous block and never becomes acceptable, unacceptable, then acceptable again.

Thus Audit 291's hardness is not universal. It is caused by unrestricted feasible-action hypergraph geometry; one-dimensional convexity/contiguity restores exact tractability.

## Edge and degeneracy audit

- Empty \(Y\): optimum is 0.
- Uncovered state: infeasible; greedy detects it at the first uncovered point with no containing action.
- Duplicate feasible intervals: harmless.
- Singleton intervals: allowed.
- Universal interval: optimum 1 for nonempty \(Y\).
- Nested intervals: exchange proof still applies.
- Ties in farthest right endpoint: arbitrary tie-breaking is safe.
- Empty action-feasible sets: irrelevant and may be discarded.
- Loss values need not be metric, symmetric, continuous, or additive; only the threshold sets at the chosen \(\varepsilon\) must have interval structure.
- The theorem is tolerance-specific: interval structure at one \(\varepsilon\) need not persist at another.

## Composition warning

Interval feasibility is not automatically preserved by arbitrary products, unions, projections, or action composition. In particular, two independently ordered interfaces generally produce rectangles rather than intervals. Therefore no closure-under-composition claim is made.

## Prior-art collision

The combinatorial theorem is classical one-dimensional interval covering / geometric set cover and is **IMPORTED/KNOWN**. It is not claimed as new. The GC-II contribution is the structural boundary it supplies immediately after Audit 291: unrestricted operational accounting is SET-COVER-hard, while an independently checkable common-order interval property makes the exact accounting number greedily computable.

## Consequence for Paper II

A structured complete criterion should not promise an efficient exact solver on unrestricted finite systems. A defensible route is instead:

\[
\text{operational restrictions}\to\text{feasible-action geometry}\to\text{algorithmic class}.
\]

Audit 292 supplies the first exact positive tractability island: common-order interval feasibility.

## Status ledger

- unrestricted finite exact lossy accounting: **NP-hard / Audit 291**;
- interval-feasible exact greedy criterion: **PROVED**;
- generic interval-cover theorem: **IMPORTED/KNOWN**;
- arbitrary product/composition preservation: **NOT CLAIMED / generally false without extra structure**;
- higher-dimensional or bounded-width generalization: **OPEN**.
