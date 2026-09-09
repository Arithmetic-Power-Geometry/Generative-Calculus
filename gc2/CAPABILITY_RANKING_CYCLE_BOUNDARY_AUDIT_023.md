# GC-II Capability-Ranking Cycle Boundary Audit 023

## Scope

This audit attacks the next target from Audit 022: whether a GC-specific scalar Lyapunov/ranking functional can strictly decrease on every future-distinguishing transformation while allowing endogenous replenishment and coupled R/I/A/L changes. GC-I on `main` is untouched.

## Result

**Status: FALSIFIED as a universal strict-ranking route / PROVED finite-state boundary / IMPORTED-KNOWN mechanism.**

A scalar (or, more generally, well-founded) ranking that strictly decreases on *every* future-distinguishing admissible transition cannot exist in any reachable operational world containing a directed cycle whose edges are all required to be strict decreases. This remains true even if the ranking is allowed to depend on the complete GC-II state, residual vector budget, information, available actions/interfaces, rules, and whole task-scale-error envelope.

Thus endogenous replenishment is not the main obstruction. The decisive obstruction is recurrent future-distinguishing dynamics.

## Formal statement

Let `Q` be the reachable operational state set and let `E_* subseteq Q x Q` be the transitions on which a proposed capability ranking must strictly decrease. Let `(W,prec)` be any well-founded strict order. Suppose

`Psi : Q -> W`

satisfies

`q -> q' in E_*  =>  Psi(q') prec Psi(q)`.

Then the directed graph `(Q,E_*)` contains no directed cycle.

### Proof

If `q_0 -> q_1 -> ... -> q_{m-1} -> q_0` were a directed cycle in `E_*`, strict descent would give

`Psi(q_0) succ Psi(q_1) succ ... succ Psi(q_{m-1}) succ Psi(q_0)`.

By transitivity, `Psi(q_0) succ Psi(q_0)`, contradicting irreflexivity of a strict order. QED.

For finite `Q`, the converse also holds: if `(Q,E_*)` is acyclic, define `Psi(q)` as the length of a longest `E_*`-path starting at `q`. Then every `E_*` edge `q->q'` satisfies `Psi(q) >= Psi(q')+1`. Hence, in finite worlds,

`strict ranking on every E_* edge exists  <=>  (Q,E_*) is acyclic`.

This equivalence is graph-theoretic and not a GC-II novelty claim.

## Minimal GC-II counterexample with replenishment

Consider two operational states `u,v` with distinct future-capability signatures and two admissible transformations:

- `g : u -> v`, consuming one unit of resource R while enabling an information/interface capability;
- `h : v -> u`, replenishing that unit of R while removing that capability and restoring the original operational state.

Both transitions are future-distinguishing. Any proposed strict capability ranking would require

`Psi(v) < Psi(u)` from `g`,

and

`Psi(u) < Psi(v)` from `h`,

an immediate contradiction.

The contradiction is independent of whether `Psi` includes R/I/A/L interaction terms, nonlinear envelope statistics, history-independent capability values, or vector budgets. No state function into a well-founded order can strictly decrease around a genuine recurrent cycle.

## Stronger consequence for Audit 022's next target

The proposed search for a `Psi_G(state,budget,envelope)` that *strictly decreases on every future-distinguishing transformation* was too strong for general GC-II worlds. It silently excludes operationally reversible or recurrent capability dynamics. Therefore it cannot serve as the universal foundation for GC-II capability accounting.

This does **not** falsify more selective certificates. Three defensible directions remain:

1. **Cycle quotient:** require strict descent only between strongly connected recurrent classes, with nonincrease or a separate invariant inside each class.
2. **Dissipation/distortion functional:** measure irreversible loss or deviation over a completed trace/cycle rather than demand per-step descent.
3. **Conditional truncation:** identify a designated transient subrelation and rank only transitions in that subrelation; recurrent capability-preserving dynamics can remain outside it.

For a finite transition graph, SCC condensation is always a DAG, so a ranking of SCCs always exists. But this is again generic graph theory. A GC-II contribution would need a quantitatively informative quotient or cycle distortion tied essentially to whole-envelope R/I/A/L accounting.

## Relation to reversibility-gap work

This boundary aligns with Audits 019-020: endpoint costs alone do not characterize reversibility, and a future-capability distortion after a round trip is a stronger object. The present result explains why a universal strictly decreasing state potential is structurally incompatible with reversible capability cycles. Therefore the next serious target should be a **cycle-sensitive whole-envelope distortion/accounting law**, not a universal termination-style ranking.

A candidate object is

`D_cyc(sigma;q) = D_future(q, Phi_sigma(q))`

for feasible closed-observation traces `sigma` that return to the same coarse endpoint label. The immediate questions are whether `D_cyc` is invariant under operational equivalence, whether zero distortion composes, whether nonzero distortion admits a resource/information/action/rule lower bound, and whether any such bound survives prior-art collision with bisimulation metrics, thermodynamic irreversibility, resource theories, and dynamical-system cycle functionals. **Status: OPEN.**

## Edge cases

- A syntactic cycle whose states are future-equivalent need not be placed in `E_*`; it does not obstruct a ranking defined only on future-distinguishing transitions.
- A cycle containing at least one edge not required to decrease may coexist with a partial ranking. The impossibility concerns cycles entirely contained in the strict-decrease relation.
- Allowing a non-well-founded codomain avoids the contradiction only by abandoning the finite-horizon/termination guarantee that motivated the ranking.
- History-dependent trace functionals can decrease with elapsed steps even when the physical state cycles, but they are not state Lyapunov functions and do not prove that future operational behavior itself is acyclic.
- Randomized/stochastic worlds require a different notion (e.g. expected drift/supermartingale); the deterministic cycle obstruction still rules out pointwise strict descent on every realized cycle edge.

## Prior-art collision classification

The mechanism is standard: ranking functions certify termination through descent in a well-founded order, while directed cycles obstruct strict per-transition descent; SCC condensation produces an acyclic quotient. Consequently the theorem above is **IMPORTED/KNOWN in mechanism**. It is retained because it decisively prevents GC-II from making an overstrong or false universal Lyapunov claim.

## Status update

- Universal strict `Psi_G` decreasing on every future-distinguishing transition: **FALSIFIED** when recurrent future-distinguishing cycles are admissible.
- Finite-state existence iff strict-edge graph is acyclic: **PROVED / IMPORTED-KNOWN**.
- SCC-condensation ranking: **IMPORTED/KNOWN**, not a novelty target.
- Cycle-sensitive whole-envelope distortion with a nontrivial R/I/A/L accounting theorem: **OPEN**.
- GC-specific quantitative consequence that survives bisimulation/resource-theory/thermodynamic/dynamical-systems collision checks: **OPEN**.
