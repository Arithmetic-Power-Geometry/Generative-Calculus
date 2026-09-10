# GC-II Audit 041 — Realization-Basis Dependence Boundary

Status date: 2026-09-10
Branch: `gc2-capability-accounting-lab`
Parent audit: 040

## Question

Can GC-II obtain a breakthrough by fixing the complete extensional capability map Phi and defining a Pareto realization cost over primitive resources/information/interfaces/rules?

## Setup

Let Phi be a fixed extensional map from admissible input/continuation histories to conserved-reference outcomes. Let B be a declared primitive realization basis (operations, sensors/interfaces, rules, memory/information primitives, and their typed cost maps). Define

C_B(Phi) = ParetoMin { c_B(P) : P implements Phi },

where c_B(P) is a typed/vector cost. Components with incompatible units are not summed unless an explicit conversion law is part of B.

For two bases B and B', define a comparison only after specifying a compiler/translator tau: B -> B' that preserves Phi. If tau has overhead map h_tau, then a defensible statement is a simulation inequality such as

C_B'(Phi) <= h_tau(C_B(Phi))

componentwise/Pareto-wise in the declared domains. Without tau or a common physical calibration, subtraction C_B(Phi)-C_B'(Phi) is generally undefined or representation-dependent.

## Proposition 041-A — Free-macro collapse

For any fixed Phi with at least one implementation P in B, construct B_P by adjoining P itself as a zero-cost primitive macro. Then

0 in C_B_P(Phi).

Therefore no positive realization gap based only on the choice of unrestricted primitive basis is invariant under conservative macro extension.

### Proof

B_P contains a primitive whose semantics is exactly Phi and whose declared cost is zero. The one-step implementation using that primitive realizes Phi at zero declared cost. Hence zero is attainable and Pareto-minimal. QED.

Status: **PROVED**.

## Proposition 041-B — Arbitrary padding

If a basis permits semantics-preserving no-op primitives carrying positive declared cost, any implementation can be padded to have arbitrarily larger cost without changing Phi. Thus raw implementation cost is not an extensional property of Phi.

Status: **PROVED**.

## Proposition 041-C — What survives

A meaningful realization theorem requires a restricted, independently justified basis class plus cost calibration and admissible compilers. Within such a class, lower bounds and Pareto frontiers may be substantive, but their novelty must come from a new invariant/lower-bound mechanism, not from the generic fact that implementations have costs.

Status: **PROVED as a methodological necessity; OPEN as a GC-II breakthrough route**.

## Edge/degenerate cases

- If Phi is already a free primitive, the frontier contains zero.
- If Phi is unrealizable in B, C_B(Phi) is empty; this is impossibility, not an infinite scalar cost unless infinity is explicitly added to the codomain.
- Duplicate primitives do not change the frontier when semantics and costs are identical.
- Zero-cost cycles require quotienting/normalization before interpreting path length as cost.
- Negative costs destroy ordinary resource monotonicity unless a debt/production semantics is explicitly modeled.
- Non-additive composition is allowed: the audit uses only an explicitly declared composition/cost law.
- Vector costs remain typed; no R+I+A+L scalar is assumed.

## Collision check

This route collides with established implementation/complexity ideas. Classical machine-independent complexity frameworks explicitly separate a computed function from the complexity of a particular program/model, and speedup/gap phenomena show that implementation complexity is subtle and measure-dependent. Resource theories of operations likewise study costs of simulating channels/operations. Consequently, `C_B(Phi)` is useful GC bookkeeping but is not by itself a novel scientific object.

Classification:

- Fixed-map Pareto realization cost: **IMPORTED/KNOWN in mechanism**.
- Positive basis-independent novelty gap without restrictions: **FALSIFIED** by free-macro collapse.
- Compiler-relative simulation inequalities: **KNOWN GENERIC MECHANISM**.
- A GC-specific calibrated invariant across physically justified primitive bases: **OPEN**.

## Consequence for Omega_G

Omega_G must not assign intrinsic novelty merely because the same Phi has different costs under arbitrarily chosen primitive vocabularies. A candidate must either:

1. fix a physically/operationally justified primitive basis and state dependence explicitly; or
2. quotient over an admissible class of semantics-preserving compilers with bounded overhead; or
3. derive a lower bound from an invariant that cannot be erased by conservative macro extension because macro installation itself is charged by the same physical accounting.

The third route is the strongest surviving target.

## Next attack

Define **installation-aware capability accounting**. A new primitive/macro cannot be declared free: its installation must be realized from a frozen physical substrate and charged for description/certificate, information acquisition, interface construction, and execution resources. Search for a conservation/lower-bound theorem of the form

implementation saving <= installation cost + reusable amortization term,

with typed nonlinear overheads and explicit repeated-use horizon N. Stress-test whether the apparent advantage survives universal-machine invariance, Kolmogorov description length, circuit preprocessing/advice, compilation, amortized analysis, resource-theoretic simulation cost, and hardware setup costs.

Kill condition: if installation-aware accounting reduces exactly to known compilation/preprocessing/advice/amortization theory after all GC structure is encoded, classify it IMPORTED/KNOWN and move on.
