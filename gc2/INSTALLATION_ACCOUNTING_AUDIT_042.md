# GC-II Audit 042 — Installation-Aware Accounting Conservation Boundary

Status date: 2026-09-10
Branch: `gc2-capability-accounting-lab`
Parent audit: 041

## Question

Does charging installation of a reusable macro/interface/rule yield a genuinely new No-Free-Capability or capability-accounting theorem?

## Typed setup

Fix a physical substrate/basis B. Let Phi be an extensional capability. Let P be a baseline realization with per-use typed cost vector c(P). Let m be an installed reusable realization. Installation is itself an admissible B-process with typed cost k(m), and use j has typed cost u_j(m). For N uses define total typed costs

T_base(N) = C_B(P^N),
T_m(N) = k(m) \odot C_B(m^N),

where \odot is the declared typed composition law; no addition across incompatible units is assumed. In the additive special case,

T_base(N)=N c(P),
T_m(N)=k(m)+N u(m).

Define an installation advantage only after a common calibration/order exists:

Adv_N(m;P) = T_base(N) - T_m(N).

## Proposition 042-A — No universal `saving <= installation cost` law

The candidate inequality

implementation saving <= installation cost + reusable amortization term

has no non-tautological universal content without an independent restriction on the amortization term.

In the additive scalar special case, choose baseline per-use cost b>0, installed per-use cost u with 0<=u<b, and installation cost k>=0. Then

Adv_N = N(b-u)-k.

For every fixed k and every proposed constant bound Adv_N <= k, choose N > 2k/(b-u). Then Adv_N>k. Hence installation cost does not upper-bound reusable saving.

Status: **PROVED counterexample**.

## Proposition 042-B — Exact break-even law in the additive stationary case

Under stationary additive costs with b>u,

T_m(N) <= T_base(N)
iff
N >= k/(b-u).

Thus the break-even horizon is

N_* = ceil(k/(b-u))

for integer use counts, with the obvious zero-denominator conventions.

Status: **PROVED / IMPORTED-KNOWN mechanism (amortization)**.

## Proposition 042-C — Installation-aware free-macro repair

Audit 041's free-macro collapse is blocked if every added macro m must be constructed by an admissible substrate process and its installation cost k(m) is included. A macro cannot be made free merely by renaming an implementation unless the substrate accounting itself assigns zero construction cost.

This repairs a bookkeeping defect but does not establish a new conservation law: repeated use may legitimately produce arbitrarily large cumulative savings relative to recomputation.

Status: **PROVED methodological repair; not a novelty theorem**.

## Non-additive formulation

For a general typed composition law, the only universally valid comparison is the declared substrate-relative preorder

T_m(N) \preceq T_base(N)

or its Pareto analogue. A scalar difference is undefined unless a common calibration is supplied. Synergies, caching, parallelism, wear, learning, and congestion can make marginal use costs decrease or increase with N. Therefore no linear conservation inequality follows from installation-aware accounting alone.

## Edge and degeneracy checks

- k=0: a genuinely zero-cost installation is allowed only if justified by the frozen substrate; then Audit 041 collapse is physical rather than representational.
- b=u: installation never pays back for k>0; it is cost-neutral only for k=0.
- b<u: reuse worsens cost and there is no positive break-even horizon.
- Negative k or negative resource costs require explicit production/debt semantics and are excluded from ordinary resource accounting.
- Finite lifetime H: installation is advantageous only if some N<=H crosses the frontier.
- Vector costs: different components can cross at different N; use Pareto dominance rather than scalarization.
- Nonstationary u_j: replace N u by the declared composed sequence cost; no stationary threshold is implied.
- Composition: the accounting is invariant under semantics-preserving regrouping only if the substrate cost law is associative or an explicit parenthesization is part of the model.

## Collision / novelty assessment

The exact stationary result is ordinary setup-cost amortization/preprocessing: pay once, reduce later marginal costs. Offline/online computation, data structures, circuit compilation, advice/preprocessing, caching, hardware setup, and resource-theoretic simulation all contain neighboring versions of this tradeoff. Kolmogorov/program-description viewpoints also charge descriptions relative to a fixed universal substrate only up to representation-dependent constants.

Classification:

- Installation-aware accounting: **USEFUL / IMPORTED-KNOWN in mechanism**.
- Universal saving <= installation-cost conservation law: **FALSIFIED**.
- Additive break-even threshold: **PROVED / KNOWN amortization**.
- GC-II breakthrough from installation accounting alone: **FALSIFIED**.

## Consequence for Omega_G

Omega_G cannot be defined as cumulative saving minus installation cost: ordinary reuse can make that quantity arbitrarily large without creating a new kind of capability. Installation cost is necessary to prevent free-macro artifacts, but reuse benefit must be treated as an ordinary horizon-dependent resource tradeoff.

A defensible novelty gap must instead compare systems after matching the full substrate-relative amortized realization frontier for every declared reuse horizon N. If the frontiers differ only because one system has a cheaper reusable implementation, the difference is implementation/resource complexity, not yet generative novelty.

## Next attack

Move to a stronger invariant: **capability creation under matched amortized realization frontiers**. Seek two finite systems whose substrate, primitive costs, all single-task extensional maps, all horizon-indexed ordinary realization frontiers, and allowed compilers are matched, yet whose closure under admissible composition differs because an operation creates a new *type of admissible interface/action/rule* not simulable by the original closure.

The candidate must survive a strict compilation test: if the allegedly new type can be represented as an ordinary augmented state/action in the frozen substrate with its full installation and use costs preserved, classify it IMPORTED/KNOWN.

Potential next formal object: a typed closure operator Cl_B on admissible generators, and a quotient-sensitive escape witness g such that g is outside Cl_B(G) but inside Cl_B(G union Delta), with a lower bound on every substrate-realizing Delta. The novelty burden is to make this stronger than ordinary algebraic generation, reachability, resource-theoretic generation, circuit basis extension, or simulation preorder.
