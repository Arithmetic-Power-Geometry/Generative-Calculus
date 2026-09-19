# GC-II Audit 261 — Unary-effect locality does not bound capability-interaction order

Status: **PROVED no-go / prior-art mechanism known**

## Question
Audit 260 leaves open whether a simple generator-locality restriction can rescue a finite-order capability accounting law. The first candidate is bounded *effect arity*: every admissible action changes at most one visible capability atom.

## Construction
Let the visible capability universe be `U={a_1,...,a_m}`, `m>=2`, start state `s`, and let `K>=0`.

States contain a visible subset of `U` plus a hidden control mode. From `s`, zero-cost control-only actions choose one of `m` irreversible branches `b_i`. Within branch `b_i`, a zero-cost chain adds, one atom at a time, every atom except `a_i`. No branch switch is available. Separately, a control-only gate of cost `K` enters branch `g`; within `g`, a zero-cost chain adds all `m` atoms one at a time.

Every transition changes **at most one visible capability atom** (control-only transitions change zero). All costs are nonnegative.

For task-indexed regeneration cost

`C_s(T)=inf{cost(pi): pi starts at s and ends at z with T subseteq S(z)}`,

we have

* `C_s(T)=0` for every proper subset `T proper-subset U`: choose an omitted atom `a_i notin T`, enter branch `b_i`, and accumulate the atoms of `T` at zero cost.
* `C_s(U)=K`: no `b_i` contains all atoms; branch switching is impossible; the `g` branch reaches `U` with total cost `K`.

Replacing the finite-cost gate by no `g` branch gives `C_s(U)=+infinity` with the same complete proper-subset profile.

## Theorem (effect-arity no-go)
For every `m>=2` and every `K>=0`, there is a finite nonnegative-cost operational system in which each transition changes at most one visible capability atom, yet

`C_s(T)=0` for all `T proper-subset U`, while `C_s(U)=K`.

There is also such a system with `C_s(U)=+infinity`.

Therefore unary visible effects do **not** imply any bounded-order capability accounting theorem, do not bound the top-order Mobius interaction, and do not rescue a universal bound on the full task from lower-order regeneration costs.

## Why the obstruction survives
The high-order coupling is carried by **hidden control/precondition structure**, not simultaneous multi-atom effects. Effect arity and interaction order are different notions. Any positive GC-II locality theorem must constrain dependencies/guards/control flow (e.g. an explicit causal or interaction graph and an appropriate width/acyclicity condition), not merely the number of capability coordinates modified by one action.

## Checks
* Domains: finite state space; finite visible capability universe; costs in nonnegative reals.
* Degenerate `K=0`: all tasks cost zero; theorem still holds.
* `K>0`: top-order excess can be arbitrarily large despite unary visible effects.
* Unreachable variant: full task cost is infinite.
* Requirement monotonicity is preserved.
* Positive rescaling of costs maps `K` to `lambda K` without changing the structural conclusion.
* The construction uses irreversible hidden branch choice; this is intentional and isolates the missing hypothesis.

## Prior-art collision boundary
Unary operators are not by themselves a tractability/locality guarantee in classical planning. Brafman–Domshlak show that general unary-operator STRIPS planning remains as hard as general STRIPS planning and that tractability depends on causal-graph structure; later work also shows hardness for very simple chain causal graphs under suitable domains. Thus the broad lesson that unary effects can hide global dependency is **IMPORTED/KNOWN**. The GC-II contribution of this audit is a precise falsification of *effect arity as the missing hypothesis* for the task-indexed capability-accounting program, not a claim that unary-planning hardness is new.

## Ledger
* Unary visible-effect arity => bounded capability-interaction order: **FALSIFIED**.
* Arbitrary top-order regeneration cost with identical zero proper-subset profile under unary visible effects: **PROVED**.
* Effect arity alone as a sufficient locality hypothesis for `Omega_G <= F(Delta R,Delta I,Delta A,Delta L)`: **FALSIFIED**.
* Generic unary-planning/global-dependency mechanism: **IMPORTED/KNOWN**.
* Dependency-aware bounded-width/acyclicity condition yielding a quantitative GC-II accounting bound: **OPEN**.

## Next attack
Define an operational dependency hypergraph whose vertices are typed capability/control variables and whose hyperedges record action guards plus effects. Test whether bounded treewidth/acyclicity plus a no-hidden-control condition yields a dynamic-programming decomposition of `C_s(T)`, and determine whether the resulting statement is merely a direct import from factored planning/CSP or leaves a GC-specific quantitative residue.
