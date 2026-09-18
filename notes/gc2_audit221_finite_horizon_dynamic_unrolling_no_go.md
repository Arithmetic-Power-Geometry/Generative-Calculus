# GC-II Audit 221 — finite-horizon dynamic-context unrolling no-go

Status: **PROVED / FALSIFIED / IMPORTED-KNOWN boundary**

## Target

Audit 220 left open whether budgeted sequential generation/unlocking of intervention contexts can carry GC-specific information that is lost by a static context hypergraph.

## Model

Fix a finite horizon `H`. A dynamic operational specification is

`D=(S,A,E,T,K,c,s0,B)`

where `S` is a finite configuration set, `A` a finite action alphabet, `E(s) subseteq A` the actions/interfaces admissible at configuration `s`, `T(s,a)` the next configuration for admissible `(s,a)`, `K(s,a)` the local operational constraint/output relation exposed by that step, and `c(s,a)>=0` its resource cost. A length-`H` execution is admissible iff every selected action is enabled, every transition follows `T`, every exposed local relation is satisfied, and total cost is at most `B`.

## Theorem 221.1 — exact finite-horizon static unrolling

For every finite `D,H,B`, there is a finite static CSP (or weighted CSP when costs are retained) `U_H(D,B)` whose satisfying assignments are in bijection with admissible length-`H` executions of `D`.

Introduce time-indexed variables

`S_0,...,S_H`, `A_0,...,A_{H-1}`

(and witness/output variables required by each `K`). Add the static constraints

1. `S_0=s0`;
2. `(S_t,A_t)` belongs to the enabled relation `G_E={(s,a):a in E(s)}`;
3. `(S_t,A_t,S_{t+1})` belongs to the transition graph `G_T={(s,a,T(s,a))}`;
4. the time-indexed copy of `K(S_t,A_t)` is satisfied;
5. `sum_t c(S_t,A_t) <= B` (or retain the sum as the WCSP objective).

Mapping a dynamic execution to its time-indexed values gives a satisfying static assignment. Conversely, constraints 1–4 reconstruct exactly one legal dynamic trajectory (up to any explicitly retained local witnesses), and constraint 5 preserves the budget. These maps are inverse on execution variables. Therefore feasibility, exact trajectory set, step order, state-dependent unlocking, local outputs/witnesses, and additive path cost are preserved.

## Corollary 221.2 — finite-horizon unlocking alone is not an intrinsic novelty gap

Any proposed `Omega_G` that depends only on finite-horizon sequential unlocking, generated contexts, their observed relations, trajectory order, and additive budget factors through the static history-expanded encoding above. Consequently those ingredients alone cannot establish a representation-invariant separation from ordinary finite constraint/planning/weighted-constraint machinery.

This does **not** say that the compact dynamic representation and its unrolling have equal description size, treewidth, online information, locality, or computational complexity. Those quantities can differ dramatically. A GC-II theorem would need a restriction that is itself operationally fixed and then prove an excess not already identical to known succinct-representation, planning, dynamic-CSP, online, or width phenomena.

## Edge and degeneracy audit

- `H=0`: unrolling contains only `S_0=s0`; exact.
- no enabled action: both dynamic and static models have no positive-length execution.
- zero-cost actions: preserved exactly; no positivity assumption is used.
- unreachable configurations: may occur in the static domain but cannot satisfy the transition chain from `s0`.
- cycles/repeated contexts: represented by distinct time-indexed copies; no acyclicity assumption is used.
- irreversible unlocking and relocking: encoded by state-dependent enabled relations.
- multiple actions with the same next state: action variables preserve multiplicity/provenance.
- budget monotonicity: increasing `B` can only add feasible executions when costs are nonnegative.
- composition in horizon: `U_{H+K}` restricts on its first `H` layers to `U_H` subject to the same prefix budget accounting.
- nondeterminism: the theorem extends by replacing functional `T` with a transition relation and retaining `S_{t+1}` as a witness.

## Prior-art collision boundary

Dynamic CSPs are classically sequences of CSPs changed by additions/deletions/changes of constraints. Planning and situation-calculus formalisms already encode state-dependent action preconditions and transitions. Time expansion/unrolling is standard finite-horizon machinery. Weighted/valued CSPs already retain finite additive costs. Sequential contextuality also explicitly models state update between instruments. Therefore **finite-horizon dynamic context generation itself is not claimed as novel**.

## Ledger

- exact finite-horizon history-expanded reduction: **PROVED**
- preservation of state-dependent action/context unlocking: **PROVED**
- preservation of additive budget and zero-cost actions: **PROVED**
- finite sequential context generation alone as GC-specific `Omega_G`: **FALSIFIED**
- dynamic CSP / planning / sequential-state-update mechanisms: **IMPORTED/KNOWN**
- representation-size or width blow-up under an independently fixed GC projection architecture: **OPEN**
- unbounded/online endogenous generation where the future static instance is not available to the agent: **OPEN**, but must be collision-tested against online algorithms, planning under partial information, games/process semantics, and succinct/infinite-state systems

## Strongest next gate

Do not claim novelty from temporal order itself. The next defensible target is an **information-causal** separation: compare an online generator that must act before future contexts/rules are revealed with an offline static unrolling that is given those future contexts. Any positive gap must charge the information advantage explicitly; otherwise it is merely an online-vs-offline gap. A GC-specific survivor would have to derive the information restriction from GC-I projection structure rather than impose it ad hoc.
