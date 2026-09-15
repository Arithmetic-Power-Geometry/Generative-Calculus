# GC-II Audit 153 — static Pareto equality versus prefix feasibility

## Candidate attacked
Audit 152 left the possibility that two systems can have the same complete static Pareto frontier of total `(R,I,A,L)` cost but differ because resources are released, converted, or made admissible sequentially.

## Exact separation
Let a resource stock be `s_t in Z^4_{>=0}` and a trace have increments `d_t in Z^4`. A trace is operationally admissible iff

` s_0 + sum_{k<=t} d_k >= 0 ` coordinatewise for every prefix `t`.

Its endpoint/net accounting vector is only

` D = sum_t d_t `.

For any typed axis j, compare two systems with initial stock zero and forced traces

- P_j: `(+e_j, -e_j)`
- C_j: `(-e_j, +e_j)`.

Both expose exactly the same action multiset and the same static endpoint/net frontier `{0}`. But P_j is feasible and C_j is not: C_j violates nonnegativity at its first prefix. Hence static total/net Pareto data is not a complete capability invariant once production/release and precedence are admitted.

### Proposition (prefix criterion)
For deterministic additive stock dynamics, a fixed trace is feasible from `s_0` iff every prefix stock `s_0 + sum_{k<=t} d_k` is coordinatewise nonnegative.

**Status: PROVED.** This follows directly from the admissibility definition and is not a novelty claim.

### Corollary
Endpoint/net cost, even the complete static Pareto frontier over endpoint vectors, cannot determine sequential capability.

**Status: PROVED for this model.**

## Exact regression
`experiments/gc2_audit153_prefix_resource_separation.py` checks all four typed axes and exhausts all 64 ordered two-step traces formed from the eight signed unit vectors in four dimensions. Frozen result: 64 traces, 8 witness assertions, 0 violations.

## Collision / novelty audit
This separation is not a GC-II breakthrough. Petri nets already impose enabledness at the current marking: a transition consumes input tokens and produces output tokens, so the order of firings can determine reachability even when aggregate incidence/net change agrees. Resource-constrained scheduling with consumption and production similarly requires storage stock never to fall below a bound while resources may be produced later. Thus the prefix-stock mechanism is standard dynamic-resource feasibility, not a new invariant.

## Ledger
- Prefix feasibility criterion: **PROVED**.
- Equal static net frontier but different sequential capability: **PROVED**.
- Exact finite regression: **PASS**.
- Complete static endpoint Pareto frontier as capability invariant under resource release/production: **FALSIFIED**.
- Prefix stock / token-enabledness mechanism: **IMPORTED/KNOWN**.
- Sequential-resource separation alone as `Omega_G`: **FALSIFIED**.
- A representation-invariant residual beyond the full reachable marking/state-transition structure: **OPEN**.

## Next gate
Do not promote trajectory/prefix feasibility itself. The next viable candidate must compare systems after quotienting by full reachable operational transition structure (or a defensible process equivalence) and still obtain a typed capability-accounting separation. Otherwise Petri-net reachability, vector-addition systems, inventory/resource scheduling, constrained planning, or process equivalence already captures the effect.
