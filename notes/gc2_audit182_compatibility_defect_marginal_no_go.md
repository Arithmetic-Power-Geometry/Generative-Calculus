# GC-II Audit 182 — Compatibility-defect marginal no-go

Status date: 2026-09-16
Branch target: `gc2-capability-accounting-lab` only.

## Question

Can the sequential compatibility defect

\[
\Delta_C(\tau_1,\tau_2)=(C_{\tau_1}+C_{\tau_2})\setminus C_{\tau_1;\tau_2}
\]

be predicted from the two marginal attainable-cost sets alone?

## Exact counterexample

Let each task have one-dimensional cost 1, so

\[
C_{\tau_1}=C_{\tau_2}=\{1\}
\]

in both systems below.

System A has two witnesses for the first task, `a0,a1`, and two for the second, `b0,b1`. Every witness has cost 1. Its compatibility relation is

\[
K_A=\{(a_0,b_0),(a_1,b_1)\}.
\]

Therefore at least one compatible sequential witness exists and

\[
C^A_{\tau_1;\tau_2}=\{2\}.
\]

System B has the same witnesses and identical marginal costs, but

\[
K_B=\varnothing.
\]

Therefore

\[
C^B_{\tau_1;\tau_2}=\varnothing.
\]

The marginal attainable-cost sets are identical, but the composed attainable-cost sets differ. Hence no functional

\[
\Phi(C_{\tau_1},C_{\tau_2})=C_{\tau_1;\tau_2}
\]

exists over unrestricted operational systems.

The same conclusion holds even if the marginals retain witness multiplicities but discard the cross-task compatibility relation: A and B have two witnesses of cost 1 on each side, yet composition differs.

## Theorem (marginal insufficiency for composition)

For unrestricted finite operational systems, marginal attainable-cost sets are not sufficient statistics for sequential composability.

### Proof

Systems A and B above have equal marginal attainable-cost sets but unequal sequential attainable-cost sets. Any map depending only on the marginals must return the same value on A and B, contradiction. QED.

Status: **PROVED**.

## Stronger structural statement

If witnesses are retained, exact sequential composition is a relational join over the compatibility relation:

\[
W_{12}=\{(u,v):u\in W_1,\ v\in W_2,\ K(u,v)=1\},
\]

followed by cost aggregation and projection:

\[
C_{12}=\{c(u)+c(v):(u,v)\in W_{12}\}.
\]

Thus the missing datum is not a new scalar hidden inside the marginals; it is cross-witness relational structure. Any exact predictor must encode enough information to distinguish compatibility relations that induce different projected aggregate costs.

Status: **PROVED** as a finite relational representation.

## Collision / novelty boundary

This result is scientifically useful as a no-go boundary, but not by itself a GC-II breakthrough. The construction is an instance of the classical fact that marginals/projections do not determine a joint relation, while relational composition is naturally expressed by join plus projection. Related established territories include relational/database joins and decomposability, CSP compatibility/consistency, interface compatibility and synchronous composition, and contextual local-to-global obstruction.

Therefore:

- compatibility defect from marginal cost sets alone — **FALSIFIED**;
- marginal insufficiency theorem — **PROVED**;
- compatibility relation as missing joint datum — **PROVED / IMPORTED-KNOWN mechanism**;
- raw compatibility defect as independent GC-II invariant — **FALSIFIED as a breakthrough candidate**;
- minimum *operationally acquirable* information needed to identify the relevant compatibility class under explicit observation/action budgets — **OPEN**, but must be checked against communication/query/decision-tree complexity and active learning;
- higher-order compatibility not reconstructible from all lower-order compatibility projections — **OPEN as a GC-II route**, but must be collision-tested against database join dependencies, marginal problems, contextuality, CSP width and hypergraph acyclicity before any novelty claim.

## Edge-case audit

- Empty marginal: composition is empty; no defect surprise.
- Singleton witnesses: compatibility is a single Boolean; marginals still do not determine it.
- Zero costs: the separation persists (`{0}` versus empty composition), so it is not a positive-cost artifact.
- Vector costs: embed the scalar example in any coordinate; separation persists.
- Action subdivision: cost-preserving subdivision does not repair missing compatibility information.
- Monotonicity: enlarging compatibility can only enlarge the witness-level join and therefore can only enlarge the resulting attainable composed-cost set before upward closure.
- Associativity: binary compatibility data need not suffice for higher-order composition if admissibility depends on history/global context; any claimed higher-order defect must explicitly specify composition semantics.

## Next gate

Do not promote `Delta_C` itself. Test whether a family can have identical all k-wise observable closure data for fixed k yet different (k+1)-way capability, with a quantitative lower bound on the order/amount of compatibility information required for exact prediction. Before claiming novelty, reduce against database join dependencies and acyclicity, CSP width/local consistency, sheaf/contextuality obstruction, communication complexity, and marginal extension problems.
