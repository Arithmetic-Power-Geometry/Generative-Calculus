# Audit 093 — History-State Compilation No-Go

Status date: 2026-09-12

## Question
Can sequential/path-dependent capability closure, by itself, provide the missing GC-II breakthrough after static joint-cost completeness was exhausted in Audit 092?

## Result
**FALSIFIED as a standalone novelty source.** For finite-horizon finite/computably presented operational systems, arbitrary history dependence can be represented exactly by augmenting the operational state with a sufficient history statistic (in the worst case, the full history). Thus path dependence alone does not escape ordinary state-transition/dynamic-programming formalisms.

## Setup
Let an operational system have histories

\[
h_t=(x_0,u_0,o_1,c_0,\ldots,x_t),
\]

where `x` is physical/logical state, `u` an admissible intervention, `o` an observation, and

\[
c_t=(r_t,i_t,a_t,l_t)\in\mathbb R_{\ge 0}^4
\]

is a typed resource/information/action/rule ledger increment. Permit the admissible-action predicate, transition kernel, observation kernel, cost increment, error functional, and terminal task predicate to depend on the entire history:

\[
E_t(h_t,u),\quad P_t(x_{t+1},o_{t+1}\mid h_t,u),\quad c_t(h_t,u,o_{t+1},x_{t+1}),\quad e(h_T),\quad q(h_T).
\]

Budget feasibility is coordinatewise:

\[
\sum_{t<T} c_t \preceq B=(R,I,A,L).
\]

## Theorem 093.1 — Exact History-State Compilation
For every finite-horizon history-dependent operational system above, define augmented state

\[
z_t:=h_t.
\]

Then there exists a fixed state-transition model on `z_t` whose admissible actions, transition probabilities, observations, typed ledger trajectory, terminal task outcome, and error are exactly those of the original history-dependent model.

### Proof
At augmented state `z_t=h_t`, set the enabled-action predicate to `\tilde E_t(z_t,u)=E_t(h_t,u)`. Sample `(x_{t+1},o_{t+1})` from the original conditional kernel and append the realized tuple to the history to form `z_{t+1}`. Charge exactly `c_t(h_t,u,o_{t+1},x_{t+1})`. Define terminal error and task predicates by `\tilde e(z_T)=e(h_T)` and `\tilde q(z_T)=q(h_T)`. Induction on `t` gives equality of the probability of every finite history under every corresponding policy. Hence all reachable histories, task probabilities, errors, and typed budget trajectories coincide. QED.

## Corollary 093.2 — Closure Preservation
For every task `q`, scale `s`, error threshold `epsilon`, typed budget `B`, and finite horizon `T`,

\[
\mathcal C_{\rm history}(q,s,\epsilon,B,T)
=
\mathcal C_{\rm augmented}(q,s,\epsilon,B,T).
\]

Therefore history dependence alone cannot establish a Closure-Escape theorem.

## Corollary 093.3 — No novelty from path dependence alone
A construction whose only distinction from an ordinary operational model is that costs, actions, transitions, or success depend on past history is representationally reducible to an augmented-state model. A GC-II claim must therefore concern a quantity or theorem not removed by exact sufficient-state compilation.

## Important limitation
The theorem does **not** say history is cheap to represent. Full-history state can grow exponentially with horizon, and the smallest recursively updateable sufficient statistic can itself require substantial memory. That representation/minimal-memory cost is a legitimate quantitative target, but then the novelty collision moves to automata minimization, sufficient statistics, POMDP/MDP state construction, computational mechanics, communication/query complexity, and multi-time process resource theories.

## Candidate surviving residual
Define an operational equivalence relation on histories,

\[
h\sim h' \iff \text{for every admissible continuation policy and remaining typed budget, the attainable task/error law is identical}.
\]

The quotient `H/~` is a natural candidate for a minimal exact capability state. Its size/description/memory burden may be operationally meaningful. However, **no GC-II novelty is claimed**: this must first be collision-tested against Myhill–Nerode-style state minimization, predictive-state/sufficient-statistic constructions, bisimulation, POMDP information states, causal states/computational mechanics, and recent minimal-Markovization work.

A stronger candidate would require a theorem connecting the minimal exact capability-state burden to the typed closure geometry in a way not reducible to those theories, e.g. a defensible lower bound on a typed capability-accounting quantity that remains invariant under semantics-preserving state refinements and recompilations.

## Edge-case audit
- Horizon 0: compilation is identity; no cost is introduced.
- Deterministic dynamics: proof reduces to deterministic history append.
- Stochastic dynamics: equality holds pathwise in distribution by construction.
- Zero budgets: preserved exactly.
- Degenerate/no-op actions: preserved.
- Nonadditive history-dependent charges: preserve them by storing the history and evaluating the original charge rule; additive ledger accumulation is not assumed to explain the charge law.
- History-dependent action availability: preserved.
- History-dependent rules/interfaces: preserved when their effective state is encoded in history; this is consistent with Audits 086/088.
- Infinite horizon: full-history compilation remains conceptually available but may require an infinite/countable state representation; finite-state/computable/minimal representations require additional assumptions and are **OPEN**.
- Noncomputable history functionals: representational existence does not imply an effective compiler; importing noncomputability alone is not GC-II novelty.

## Prior-art collision notes
This result is deliberately conservative. Standard sequential-decision theory treats a Markov state as a sufficient statistic of history; history-dependent control can be Markovized by an adequate state statistic, with the full history as a trivial lossless choice. Resource theories of multi-time processes already treat temporal memory/process structure as operational resources. Recent work on minimal Markovization studies exact minimal recursively updateable history statistics in structured partially observable decision processes. Therefore GC-II must not claim either history augmentation or minimal-memory state construction as new without a sharper separation theorem.

## Status ledger
- Exact finite-horizon history-state compilation: **PROVED**.
- Preservation of typed budget/task/error closure under compilation: **PROVED**.
- Sequential/path dependence as standalone GC-II novelty: **FALSIFIED**.
- Minimal exact capability-state quotient: **OPEN / prior-art collision required**.
- Quantitative typed lower bound derived from minimal capability-state burden: **OPEN**.

## Next attack
Collision-test the quotient `H/~` against automata/Myhill–Nerode, bisimulation, predictive state representations, POMDP belief/information states, causal states, and minimal Markov sufficient statistics. Only if a residual remains should it be promoted into a candidate `Omega_G`; otherwise record another no-go and move to the reversibility-gap invariant.