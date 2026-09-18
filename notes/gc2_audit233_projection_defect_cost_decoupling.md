# GC-II Audit 233 — Projection defect does not force operational cost without a bridge axiom

Status: decisive falsification / boundary result.

## Question
Can a positive GC-I projection defect alone force a positive lower bound on operational translator cost,

\[ d(x,y) \ge g(\Delta_P(x,y))>0? \]

## Decoupling theorem
Let a projection/reconstruction model have a pair `(x,y)` with a fixed positive defect `Delta_P(x,y)=delta>0`. Suppose the operational cost functional is constrained only by nonnegativity, zero-cost identity, and subadditivity under composition. Then for every `epsilon>0` there exists an admissible operational cost model on the same projection/reconstruction structure with

\[ d_\epsilon(x,y)=\epsilon, \qquad \Delta_P(x,y)=\delta. \]

Consequently no universal function `g` satisfying `g(delta)>0` can obey

\[ d(x,y)\ge g(\Delta_P(x,y)) \]

throughout this unrestricted class.

### Proof
Keep the projection/reconstruction structure fixed. Add/directly retain a translator `tau:x->y` and assign it cost `epsilon`; identities cost zero and path costs are sums (or any subadditive composition no larger than sums). Then `d_epsilon(x,y)<=epsilon`. In the two-state construction with no cheaper `x->y` path, equality holds. Projection defect is unchanged because its definition uses the fixed projection/reconstruction structure, not the freely rescaled operational cost. Since epsilon is arbitrary, for any proposed `g(delta)>0`, choose `0<epsilon<g(delta)`, contradicting the bound. QED.

The same argument survives pointwise-positive primitive costs: every epsilon is positive. It also survives normalization of the projection defect itself; the failure is the absence of a law coupling defect units to operational-cost units.

## Dimension/domain audit
`Delta_P` and `d` need not share units. A lower bound `d >= g(Delta_P)` is dimensionally meaningful only after `g` is supplied with a calibrated conversion law. Mere irreducibility/nonzero defect supplies no such calibration.

## Edge cases
- `delta=0`: no positive conclusion is sought.
- `epsilon=0`: not needed; the counterexample uses strictly positive epsilon.
- finite state space: two states suffice.
- finite primitive set: one nonidentity translator suffices.
- composition: vacuous beyond identities in the minimal construction; adding composable paths does not repair the missing bridge.
- rescaling: multiplying all nonidentity operational costs by any alpha>0 preserves reachability and projection structure while scaling `d` by alpha.

## Prior-art collision boundary
A decision-theoretic projection defect instantiated as Le Cam deficiency is already an established quantitative comparison of statistical experiments; zero deficiency corresponds to an informativeness/simulability relation. Data-processing inequalities similarly constrain information under post-processing. Neither, without an explicit operational cost model linking information loss to implementation resources, supplies a universal lower bound in arbitrary external cost units. Thus importing deficiency does not solve the GC-II bridge problem.

## Consequence for Paper II
The target `GC-I irreducibility => positive operational distance` is **FALSIFIED** under independent projection and cost structures. A valid No-Free-Capability theorem must add a nontrivial *bridge axiom/theorem*, for example a calibrated coercivity law tying admissible translator cost to reduction of a projection defect. If assumed, that law must not be presented as derived from irreducibility alone.

The scientifically interesting surviving question is whether a concrete GC operational semantics makes such a bridge derivable rather than stipulated. Candidate bridges must be checked against communication lower bounds, rate-distortion, Blackwell/Le Cam deficiency, reconstruction complexity, and representation rescaling.

## Ledger
- fixed positive projection defect with arbitrarily small positive translator cost: **PROVED**.
- projection irreducibility alone implies `d>0`: **FALSIFIED**.
- universal positive `d >= g(Delta_P)` without a defect-cost bridge: **FALSIFIED**.
- defect/cost rescaling invariance obstruction: **PROVED**.
- Le Cam/Blackwell deficiency as generic projection-information comparator: **IMPORTED/KNOWN**.
- GC-specific derivation of a calibrated bridge from concrete operational semantics: **OPEN**.
