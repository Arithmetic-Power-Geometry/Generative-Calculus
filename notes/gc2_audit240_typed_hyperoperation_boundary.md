# GC-II Audit 240 — Typed hyperoperation boundary

## Purpose
Extend Audit 239 from unit incidence edits to typed operational generators without pretending that scalar resource totals determine capability.

## Restricted typed one-shot model
Fix finite W, projection p:W->Z, decision g:W->D, message alphabet M, and baseline admissibility L0(w) subseteq M.

Let O be a finite family of admissible one-shot generators. Each o in O has:
- a type tau(o) in {R,I,A,L} (or a product type),
- a nonnegative cost vector c(o) in R_+^k,
- an incidence effect E(o) subseteq W x M.

For S subseteq O, define
L_S(w)=L0(w) union {a:(w,a) in union_{o in S} E(o)}.

For scalarized nonnegative weights theta in R_+^k define C_theta(S)=theta dot sum_{o in S} c(o). This scalarization is explicit and is not claimed canonical.

Define
Omega_theta = min_{S subseteq O} C_theta(S)
subject to existence of an exact translator under L_S.
If no S repairs feasibility, Omega_theta=infinity.

Using the Audit-238 fiber labeling lambda_z, define a world w as covered by S under lambda when some a in L_S(w) has lambda_{p(w)}(a)=g(w). Then exactly

Omega_theta = min_{lambda} min_{S subseteq O} { C_theta(S) : every world is covered by S under lambda },

with lambda required to assign at least one message to every decision appearing in each fiber.

## Exact typed-repair theorem — PROVED (restricted model)
The displayed optimization equals the minimum typed one-shot generation cost required to cross the exact-translator feasibility boundary.

Proof: for any feasible generated translator, label each (fiber,message) by its decoded decision; its chosen S covers every world, giving the lower bound. Conversely, if S covers every world under a supported lambda, each world chooses an admissible correctly labeled message and lambda is the decoder, giving feasibility. Minimize over lambda and S.

## Nonadditive interaction is structural — PROVED
Typed generator costs need not decompose into independent DeltaR, DeltaI, DeltaA, DeltaL contributions. A single generator can create incidences for several deficient worlds, while two generators can have overlapping effects. Thus the marginal value of an operation depends on the current generated incidence set.

Example: two deficient worlds w1,w2. Operations o1,o2 individually repair one world each at unit cost, while o12 repairs both at cost 1. Then minimum generation cost is 1 although the unit-incidence Audit-239 gap is 2. Conversely, if only o1,o2 exist, cost is 2. The same number of missing incidences therefore does not determine typed generation cost.

## No universal Omega_add -> typed-cost calibration — FALSIFIED
For any fixed incidence system with Omega_add>0, rescale all generator costs by alpha>0 without changing effects. Feasibility and Omega_add remain fixed while Omega_theta scales by alpha. Therefore no positive universal function f can satisfy Omega_theta >= f(Omega_add) across unconstrained cost assignments. A calibrated theorem requires semantics tying costs to generator effects.

## Closure-Escape criterion — PROVED but generic
For budget B, target capability is outside the typed one-shot budget closure iff Omega_theta>B. Equivalently, for every supported fiber labeling lambda, every operation subset S that covers all worlds has C_theta(S)>B. This is an exact operational/combinatorial criterion, but it is definitional optimization duality rather than a novel GC theorem.

## Prior-art boundary
For fixed lambda the inner problem is a weighted covering/valued-CSP style optimization; optimizing jointly over lambda and S remains adjacent to weighted CSP, set cover, MaxSAT, list-coloring and planning. The generic optimization mechanism is IMPORTED/KNOWN territory. No novelty claim is made for it.

## What survives
The GC-specific target cannot be merely 'minimum repair cost'. It must constrain how typed generators are composed, what prerequisites they require, how information changes admissibility, and how effects propagate. A candidate theorem must derive a nontrivial invariant/bound from those semantics and survive arbitrary cost-rescaling by using calibrated physical/information/interaction units.

## Status ledger
- Exact typed one-shot repair formula: PROVED.
- Joint/nonadditive generator effects can beat incidence-edit count: PROVED.
- Omega_add alone determines typed generation cost: FALSIFIED.
- Universal positive calibration from Omega_add to arbitrary generator cost: FALSIFIED.
- Budget Closure-Escape equivalence in the restricted model: PROVED / generic.
- Weighted covering/CSP mechanism as GC novelty: IMPORTED/KNOWN / NOT CLAIMED.
- Sequential typed closure with prerequisites/state-dependent effects: OPEN.
- GC-specific No-Free-Capability/accounting inequality from calibrated semantics: OPEN.
