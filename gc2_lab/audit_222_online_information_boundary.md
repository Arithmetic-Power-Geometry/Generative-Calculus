# GC-II Audit 222 — Online-information boundary

Status: decisive falsification / prior-art boundary.

## Candidate under test

Audit 221 left open the possibility that an online generative mechanism, forced to act before future contexts/rules are revealed, could exhibit a GC-specific capability gap not captured by finite static unrolling.

## Operational model

Let an environment reveal a finite request/context sequence sigma=(z_1,...,z_H). At time t a causal generator chooses action a_t using only history h_t=(z_1,a_1,...,z_t); a clairvoyant comparator may depend on all of sigma. Let J(P,sigma) be any fixed operational cost and

C_on(sigma)=inf_{P causal} J(P,sigma),
C_off(sigma)=inf_{P clairvoyant} J(P,sigma).

The raw information-causal gap is G_info=C_on-C_off (or a competitive ratio where appropriate).

## Theorem 222.1 — behavioral identity collapse

If the GC online problem and a behavioral online problem have exactly the same histories, admissible causal policies, environment sequences, feasibility relation, and cost functional, then their online and offline optima are identical instance by instance. Hence any residual obtained solely from lack of future information is zero after subtracting the matched behavioral online/offline information gap.

Proof. The two optimization problems have identical feasible sets and identical objective values for every feasible policy. Therefore both infima agree for every sigma, separately in the causal and clairvoyant classes. Subtraction (or ratio, when denominators are positive) preserves equality. QED.

## Corollary 222.2

Temporal nonanticipativity, future-context uncertainty, irrevocable action, and clairvoyant-vs-causal separation alone cannot define an intrinsic Generative Novelty Gap Omega_G. Any positive raw gap from those ingredients is ordinary online-information hardness unless GC imposes an additional operational constraint not present in the matched behavioral problem.

## Prior-art collision

Competitive analysis explicitly compares causal online algorithms against offline optima with advance knowledge of the request sequence. Advice complexity goes further and measures how much information about the future an online algorithm needs to attain a target performance. Nonanticipative stochastic control likewise fixes policies by the information available up to each decision time. Therefore 'future information unavailable to the generator' is imported structure, not a GC-II novelty claim.

## What survives

A candidate must compare two systems with the SAME causal information pattern and SAME external behavioral task, yet differ because GC-specific projection/closure structure restricts which information can be operationally assembled or transported. A possible next object is an endogenous information-assembly deficit: minimum extra observations/messages needed to realize a global generative witness when each proper projection is insufficient, minus the minimum information needed for the matched external behavior. This must be collision-tested against communication complexity, distributed synthesis, Blackwell informativeness, decentralized control, and common-information theory.

## Status ledger

- finite-horizon static unrolling: PROVED (Audit 221)
- raw online-vs-offline information gap: IMPORTED/KNOWN
- advice/future-information complexity: IMPORTED/KNOWN
- GC novelty from nonanticipativity alone: FALSIFIED
- matched-behavior residual after subtracting ordinary online-information gap: PROVED ZERO under identical feasible policy/cost model
- projection-forced endogenous information-assembly excess under a matched causal architecture: OPEN

## Edge cases checked analytically

- zero horizon: both causal and clairvoyant problems coincide; residual zero.
- deterministic known future: causal information restriction disappears; no novelty follows.
- zero-cost feasible policies: additive gap remains defined; competitive ratios may be undefined and must not be used without positive denominator.
- infeasible instances: use extended cost +infinity; infinity-infinity is not a valid scalar gap, so feasibility separation must be reported separately.
- randomized policies: identity-collapse theorem still holds if both sides use the same randomization/adversary convention.
- nonadditive costs: proof does not require additivity, convexity, Markov structure, or finite state; it uses equality of feasible policy sets and objective functionals only.

## Novelty discipline

Do not claim the theorem itself as a new online-algorithm theorem. Its GC-II value is negative: it removes another false breakthrough route and sharpens the next admissible target.
