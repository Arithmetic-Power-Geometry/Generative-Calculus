# GC-II Audit 198 — Acquisition-separation dichotomy

## Question
Audit 197 left a sharper gate: can two systems have matched extensional closure, matched compact-description complexity, the same interface and error budget, yet provably different minimum operational acquisition cost in a way that is not merely representation complexity?

## Formalization
Fix a task family T, interface/query alphabet Q, response kernel P(y|q,w), prior/uncertainty set W, error tolerance epsilon, and admissible policy class Pi. Define acquisition cost

    AC(T; Q,P,W,epsilon,Pi) = inf_{pi in Pi} sup_{w in W} E_w[cost(pi)]

subject to the terminal decision produced by pi meeting the task/error requirement.

This quantity is operational: it charges observations/actions rather than syntax size.

## Proposition — acquisition-separation dichotomy
If two systems agree on the complete acquisition experiment (T,Q,P,W,epsilon,Pi,cost), then their minimum acquisition costs are equal.

Proof: the feasible policy sets, response laws, objective and correctness constraints are identical. Hence the two infima are over the same optimization problem and are equal. QED.

Therefore a pair with equal closure and equal description complexity but unequal AC must differ in at least one acquisition-relevant structure omitted by those summaries: uncertainty/prior, response kernel, admissible queries, policy restrictions, costs, or error semantics.

## Exact finite witness for the omitted-information branch
Let hidden w=(w1,...,wn) in {0,1}^n, allow the same bit-query interface qi returning wi at unit cost, and require zero-error output of a Boolean target. Both targets have the same domain/codomain, the same interface, and O(n)-size descriptions.

For OR_n, on every input with a 1 there is a one-bit certificate, while the all-zero input requires n queried bits. For PARITY_n, every input requires all n bits in the deterministic zero-error model: if any bit is unqueried, flipping it preserves the transcript but changes parity.

This shows that acquisition cost can differ dramatically among compact tasks, but the mechanism is ordinary decision-tree/query/certificate complexity. It is not a new GC invariant.

More strongly, if one insists that the *exact task semantics* are also matched, then under the same acquisition experiment the proposition forces equal AC. To obtain unequal cost for the same task, one must change epistemic/interface structure (for example prior knowledge, observation noise, query permissions, or physical action costs); those changes are precisely established ingredients of statistical decision theory, active learning/experimental design, query complexity, POMDPs, and Blackwell comparison.

## Consequence for Omega_G
A scalar novelty gap defined as 'extra minimum acquisition cost after matching closure and compact description' has a dilemma:

1. Match the full acquisition experiment: the gap is identically zero.
2. Permit acquisition-relevant differences: the gap can be nonzero, but its source is an explicit change in information/interface/cost structure and must be compared to existing experiment-comparison and query-complexity theory.

Thus the Audit-197 gate is necessary for separating syntax from operation but is not sufficient for a GC-II breakthrough.

## Edge checks
- n=0: both tasks are constants and require zero queries.
- n=1: OR and parity coincide; separation begins only when n>=2.
- Zero-error deterministic parity lower bound: exact by transcript indistinguishability.
- OR worst-case deterministic query complexity is also n, so the distinction is certificate/instance-sensitive unless a distribution or promise is specified. This prevents falsely claiming a worst-case OR-vs-parity separation.
- With a distribution/prior, expected acquisition cost can differ, but then the prior is part of the acquisition experiment and must be reported explicitly.
- Randomization does not reduce exact parity below n in the zero-error worst-case model.
- Representation invariance: compiling the target predicate through a polynomial-overhead interpreter does not alter the query transcript argument.

## Status ledger
- Full-experiment equality => equal minimum acquisition cost: **PROVED**.
- Matched closure + matched description alone => equal acquisition cost: **FALSIFIED** (they omit acquisition-relevant structure).
- OR/PARITY certificate/query mechanisms: **IMPORTED/KNOWN**.
- Nonzero acquisition-gap as an intrinsic GC invariant without specifying epistemic/interface structure: **FALSIFIED**.
- A GC-specific law coupling *change in reachable operational closure* to a mandatory change in a complete acquisition experiment: **OPEN**.

## Prior-art collision
Decision-tree/query complexity already defines minimum adaptive observation cost for computing functions. Certificate complexity captures instance-specific evidence needed to certify an output. Blackwell comparison ranks experiments/information structures by decision usefulness. Hence acquisition cost becomes scientifically meaningful only after the experiment/interface is explicit, but that formalization alone is imported rather than GC-specific.

## Next gate
Do not search for arbitrary same-closure/different-acquisition pairs. Instead test a stronger coupling question: when a generative intervention enlarges operational closure from C to C', can one prove that every admissibility-preserving implementation must induce a nonzero change in at least one component of the *complete acquisition experiment* (response distinguishability, admissible probes/actions, physical cost, or prior uncertainty), with a quantitative lower bound that is not reducible to standard query/Blackwell deficiency? First attempt finite exact counterexamples; only promote a theorem if it survives them.
