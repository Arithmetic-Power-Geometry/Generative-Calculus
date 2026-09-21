# GC-II Audit 309 — Zero-safe junction-tree local-to-global stability

## Status

- Junction-tree TV stability theorem: **PROVED**.
- Structural-zero safety: **PROVED**.
- Bounded-task capability consequence: **PROVED**.
- Generic junction-tree / TV machinery: **IMPORTED/KNOWN**; no novelty claim is made for that machinery.
- Optimal constants: **OPEN**.

## Setup

Let `P` and `Q` be finite probability laws on the same variables and globally Markov with respect to the same decomposable graph. Fix a junction tree of maximal cliques `C_1,...,C_m`, root it at `C_1`, and for each non-root clique `C_j` let

`S_j = C_j ∩ C_parent(j)`

be its separator and `R_j = C_j \ S_j` its residual variables. Total variation is

`TV(P,Q) = (1/2) sum_x |P(x)-Q(x)|`.

No positivity or lower bound on separator probabilities is assumed.

## Lemma 309.1 — zero-safe conditional discrepancy

For any finite joint laws `P_UV,Q_UV`, choose arbitrary versions of the conditional laws on null conditioning events. Then

`sum_u Q_U(u) TV(P_{V|u},Q_{V|u}) <= TV(P_UV,Q_UV) + TV(P_U,Q_U)`.

### Proof

For every `u`, insert and subtract `P_U(u)Q_{V|u}` in the L1 difference between `P_U(u)P_{V|u}` and `Q_U(u)Q_{V|u}`. Rearranging the triangle inequality gives

`Q_U(u) ||P_{V|u}-Q_{V|u}||_1 <= ||P_U(u)P_{V|u}-Q_U(u)Q_{V|u}||_1 + |P_U(u)-Q_U(u)|`.

Sum over `u` and divide by two. If `Q_U(u)=0`, the left side is zero, so arbitrary null-event conditional versions are harmless. QED.

## Theorem 309.2 — junction-tree local-to-global TV bound

Under the setup above,

`TV(P,Q) <= TV(P_{C_1},Q_{C_1}) + sum_{j=2}^m [ TV(P_{C_j},Q_{C_j}) + TV(P_{S_j},Q_{S_j}) ].`

### Proof

The running-intersection property plus the global Markov property gives a rooted sequential factorization

`P(x)=P_{C_1}(x_{C_1}) product_{j=2}^m P_{R_j|S_j}(x_{R_j}|x_{S_j})`,

and analogously for `Q`, with arbitrary conditional versions on separator states of zero probability.

Replace the root law and then the residual kernels one at a time. The standard L1 telescoping inequality for sequential kernels yields

`TV(P,Q) <= TV(P_{C_1},Q_{C_1}) + sum_{j=2}^m E_{Q_{S_j}} TV(P_{R_j|S_j},Q_{R_j|S_j})`.

Apply Lemma 309.1 to `(U,V)=(S_j,R_j)`. Since `(S_j,R_j)=C_j`, each expectation is at most

`TV(P_{C_j},Q_{C_j}) + TV(P_{S_j},Q_{S_j})`.

Summation proves the claim. No division by a separator probability occurs. QED.

## Corollary 309.3 — uniform local error

If every clique and separator account appearing above is within TV error `epsilon`, then

`TV(P,Q) <= min(1,(2m-1) epsilon)`.

For a decomposable graph of treewidth `w`, every required clique account involves at most `w+1` variables and every separator at most `w` variables. Thus bounded-width structure converts local account accuracy into an explicit global guarantee without a minimum-probability assumption.

## Corollary 309.4 — capability accounting

For every independently fixed operational task `u:X->[0,1]`,

`|E_P u - E_Q u| <= TV(P,Q)`.

Therefore

`|E_P u-E_Q u| <= min(1, TV(P_{C_1},Q_{C_1}) + sum_{j=2}^m [TV(P_{C_j},Q_{C_j})+TV(P_{S_j},Q_{S_j})]).`

This is an interaction-aware quantitative accounting law for the decomposable class. It is not a marginal-only universal law: Audits 304–305 already rule that out without structural assumptions.

## Edge and degeneration audit

1. `m=1`: the theorem reduces exactly to `TV(P,Q)=TV(P_C1,Q_C1)`.
2. Identical clique accounts: the RHS is zero, recovering Audits 306–307 exact completeness.
3. Structural zeros: allowed; the proof never divides by `P_S` or `Q_S`.
4. Empty separators: their marginal TV is zero; independent components are handled normally.
5. Monotonicity: enlarging any certified local error bound cannot decrease the displayed upper bound.
6. Relabeling: TV and the bound are invariant under bijective state relabelings preserving clique/separator incidence.
7. Composition: for disjoint decomposable components the displayed certificate is subadditive; TV itself is at most the sum of component TVs.
8. Tree case: maximal cliques are edges (up to isolated/root conventions), recovering the mechanism of Audit 308.
9. Constant optimality: not asserted. Triangle-inequality slack can make `2m-1` non-sharp.

## Prior-art collision discipline

Junction-tree factorization, running intersection, total variation, kernel telescoping/coupling inequalities, and local graphical-model computation are established theory. They are **IMPORTED/KNOWN**. Audit 309's scientifically useful contribution inside the GC-II program is the explicit zero-safe decomposable-class capability-accounting consequence and the positive structural boundary it supplies after the unrestricted no-go results of Audits 304–305. No claim is made that the generic probabilistic inequality machinery is new.

## Next attack

Search for (i) a sharper certificate that avoids separately paying separator TV when clique errors already constrain it, (ii) a lower-bound family testing constant sharpness, and (iii) a convertibility/reversibility formulation on the same junction-tree operational object.
