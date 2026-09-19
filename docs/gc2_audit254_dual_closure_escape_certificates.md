# GC-II Audit 254 — Exact dual certificates for budgeted operational closure

## Scope

This audit attacks Paper-II items (1), (3), (4), and (6) after the Audit-253 rectangle-mode boundary. It deliberately separates a useful exact theorem from novelty: the mathematical engine is finite shortest-path / linear-programming duality and is therefore **IMPORTED/KNOWN**. The contribution here is to pin down exactly what GC-II may use as a complete operational certificate without overclaiming a new generic theorem.

## 1. Finite operational model

Let `X` be a finite state set. An admissible typed operation instance is an edge

`e=(x,o,y)`

where `o` carries its R/I/A/L type, is enabled at `x`, produces `y`, and has cost `c(e) >= 0` in a declared common budget unit. State dependence, prerequisites, and sequential order are represented by which edges exist. Let `F subseteq X` be the capability target.

Define

\[
V_F(x)=\inf_{\pi:x\leadsto F}\sum_{e\in\pi}c(e),
\]

with `V_F(x)=+infinity` when `F` is unreachable. The budget-B operational closure is

\[
Cl_B(F)=\{x:V_F(x)\le B\}.
\]

This is a finite specialization of Audit 241's sequential closure.

## 2. Dual potential family

Call `phi:X -> R` a feasible capability potential when

\[
\phi(f)\le 0\quad(f\in F),
\]

and for every admissible transition `x -> y`,

\[
\phi(x)-\phi(y)\le c(x,y).
\]

Every such potential is dimensioned in the same budget unit as `c`.

### Proposition 254.1 — weak certificate bound — PROVED

For every feasible potential and every finite path from `x` to `f in F`, telescoping gives

\[
\phi(x)\le \sum_{e\in\pi}c(e).
\]

Hence

\[
\phi(x)\le V_F(x).
\]

This remains valid with zero-cost edges and cycles.

## 3. Exact duality

### Theorem 254.2 — exact finite operational dual — PROVED / IMPORTED-KNOWN mechanism

If `V_F(x)<+infinity`, then

\[
\boxed{V_F(x)=\max_{\phi}\phi(x)}
\]

where the maximum ranges over all feasible capability potentials.

### Proof

Weak duality is Proposition 254.1. For the reverse inequality choose

\[
\phi_*(u)=V_F(u)
\]

on states from which `F` is reachable. Bellman's inequality gives

\[
V_F(u)\le c(u,v)+V_F(v)
\]

for every admissible edge between reachable states, so `phi_*` is feasible there and `phi_*(f)=0` on the target. States not reaching `F` cannot have an edge into the backward-reachable region (otherwise they too would reach `F`). Assign them a sufficiently low common finite value to extend `phi_*` to all of `X` while preserving every edge inequality. Thus a feasible potential attains `V_F(x)`.

Equivalently this is the standard shortest-path LP dual/Bellman potential theorem; it is not a novel generic GC theorem.

### Proposition 254.3 — unreachable states have unbounded dual value — PROVED

If `V_F(x)=+infinity`, let `U` be the set of states not reaching `F`. There is no edge from `U` to `X\\U`. For any `M`, assign `phi=M` on `U` and `phi=0` on `X\\U`, then lower reachable values if needed to satisfy internal cost inequalities (zero already works because costs are nonnegative). All target constraints hold, all edges leaving `U` are absent, and internal `U` edges satisfy `M-M<=c`. Therefore feasible potentials exist with `phi(x)=M` for arbitrary `M`.

So

\[
V_F(x)=+infinity\iff \sup_\phi\phi(x)=+infinity.
\]

## 4. Closure-Escape equivalence

For finite `X`, nonnegative costs, and finite budget `B`, the following are equivalent:

1. **Operational:** an admissible execution from `x` reaches `F` with total cost at most `B`.
2. **Value:** `V_F(x)<=B`.
3. **Dual/geometric:** every feasible capability potential satisfies `phi(x)<=B`.
4. **Computational:** a nonnegative shortest-path computation on the reverse operational graph returns distance at most `B`.
5. **LP:** the corresponding unit-flow minimum-cost reachability LP has optimum at most `B`.

### Theorem 254.4 — exact finite Closure-Escape criterion — PROVED / generic mechanism IMPORTED-KNOWN

\[
\boxed{x\in Cl_B(F)\iff V_F(x)\le B\iff \sup_\phi\phi(x)\le B.}
\]

This is non-tautological only in the sense that an existential path condition is equivalent to a universal family of local edge inequalities; mathematically it is still standard shortest-path duality and must not be sold as a new theorem of optimization.

## 5. No-Free-Capability boundary

Set `B=0`.

\[
\boxed{V_F(x)>0\iff \exists\text{ feasible }\phi\text{ with }\phi(x)>0.}
\]

Thus a positive dual potential is a complete certificate that zero-cost operations cannot generate the target capability.

But GC-I alone does **not** guarantee such a certificate: if a zero-cost admissible path reaches `F`, then every feasible potential has `phi(x)<=0` and `V_F(x)=0`. Therefore an unconditional No-Free-Capability theorem remains **FALSIFIED/UNAVAILABLE** without operational restrictions excluding free capability-producing paths.

This is weaker in novelty but stronger in correctness than assuming an arbitrary defect-to-cost conversion.

## 6. Complete convertibility criterion

For singleton target `{y}`, define `d(x,y)=V_{\{y\}}(x)`. Then for finite systems

\[
d(x,y)\le B
\iff
\phi(x)-\phi(y)\le B
\]

for every edge-feasible 1-Lipschitz potential `phi` satisfying

\[
\phi(u)-\phi(v)\le c(u,v)
\]

on every admissible edge.

Hence the full family of feasible directed-Lipschitz potentials is a **complete dual monotone family** for budgeted convertibility in the finite fixed-generator model.

Status: **PROVED / IMPORTED-KNOWN mechanism**. This satisfies Paper-II item (6) formally, but not as a novelty claim. A smaller GC-specific finite/computable basis remains OPEN.

## 7. Stress checks

- **Dimensions:** `phi`, `V`, `B`, and edge costs share the same budget unit.
- **Zero costs:** allowed; theorem remains valid.
- **Zero-cost cycles:** harmless; no negative cycles exist because costs are nonnegative.
- **Target state:** `V_F(f)=0`; dual constraints force `phi(f)<=0`; zero potential shows optimum 0.
- **Unreachable state:** primal value `+infinity`; dual objective is unbounded above.
- **Monotonicity in operations:** adding admissible edges can only decrease `V_F` and adds dual inequalities, so the dual supremum can only decrease.
- **Monotonicity in costs:** increasing edge costs can only increase or preserve `V_F` and relaxes the corresponding dual inequalities.
- **Budget monotonicity:** `Cl_B(F)` is nested in `B`.
- **Relabeling invariance:** graph isomorphisms preserving target and costs preserve `V_F` and transport feasible potentials bijectively.
- **Sequential prerequisites:** already encoded by the state graph; no commutativity assumption is used.
- **Composition:** no additive/product law is asserted; Audits 249–253 show target and mode coupling can obstruct naive separation.

## 8. Prior-art collision boundary

The core theorem collides directly with established shortest-path LP duality, Bellman inequalities, admissible potentials, and min-cost reachability. Related language also occurs in optimal control, planning heuristics, min-cost flow, and directed metric geometry. Therefore:

- finite shortest-path duality: **IMPORTED/KNOWN**;
- Bellman potentials / reduced-cost certificates: **IMPORTED/KNOWN**;
- complete dual characterization of finite budgeted reachability: **IMPORTED/KNOWN mechanism**;
- use as a GC-II audit discipline linking operational, geometric, and computational criteria: **PROVED specialization**, not claimed as foundational novelty;
- a strictly smaller GC-specific complete monotone basis induced by R/I/A/L semantics: **OPEN**;
- a new bound tying those dual potentials to GC-I projection irreducibility without arbitrary unit conversion: **OPEN**.

## 9. Ledger

| Claim | Status |
|---|---|
| finite budgeted operational closure model | PROVED / definition |
| every feasible potential lower-bounds capability cost | PROVED |
| `V_F(x)=sup_phi phi(x)` | PROVED / IMPORTED-KNOWN mechanism |
| unreachable iff dual objective unbounded | PROVED |
| operational/value/dual/computational Closure-Escape equivalence | PROVED / IMPORTED-KNOWN mechanism |
| positive dual potential completely certifies no free capability | PROVED |
| unconditional No-Free-Capability from GC-I alone | FALSIFIED/UNAVAILABLE |
| full directed-Lipschitz potential family complete for finite convertibility | PROVED / IMPORTED-KNOWN mechanism |
| smaller GC-specific complete basis | OPEN |
| projection-derived dual lower bound with intrinsic units | OPEN |

## 10. Consequence for the breakthrough program

This audit closes an important correctness gap but does **not** itself constitute the desired novel Paper-II breakthrough. It supplies an exact baseline that every future proposed `Omega_G`, R/I/A/L accounting bound, translator lower bound, or reversibility invariant must dominate or refine. Any proposed GC-specific monotone family that claims completeness can now be tested against the exact dual value and falsified whenever it misses a finite-state separation.
