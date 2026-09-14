# GC-II Audit 148 — Separator Acquisition Query Boundary

## Candidate attacked
After Audit 147, can the minimum operational cost of acquiring a separator absent from every permitted proper projection yield a new GC-II local-to-global lower bound?

## Exact model
For q>=2 and n>=2, an unknown global assignment x=(x_1,...,x_n) lies in exactly one residue world

R_r = {x in Z_q^n : sum_i x_i = r (mod q)}.

An acquisition policy may adaptively query coordinates x_i and must identify r with zero error for every x.

## Theorem — exact coordinate-acquisition cost
Every deterministic zero-error adaptive policy has worst-case query complexity exactly n.

Necessity: consider any root-to-leaf execution that terminates without querying coordinate j. Fix all queried answers. There remain two completions differing only in x_j, for example x_j=0 and x_j=1. Their residues differ modulo q while the complete observed transcript is identical. Therefore no leaf reached before all n coordinates have been queried can be zero-error. Adaptivity does not help because the argument applies to each terminating transcript.

Sufficiency: query all n coordinates and output sum_i x_i mod q.

Hence Q*(q,n)=n.

If coordinate i has strictly positive acquisition cost w_i and cost is additive over queried coordinates, the exact worst-case cost is

C*(q,n,w)=sum_i w_i.

The same indistinguishability argument forces every coordinate to be acquired on every zero-error terminating path; querying all coordinates attains the bound.

## Edge cases and checks
- q>=2 is required; q=1 is degenerate and needs no separator.
- n>=1 gives the same theorem; n>=2 is retained to align with Audit 147's local-projection construction.
- Zero-cost coordinates preserve the weighted equality but do not contribute positive resource cost.
- Repeated coordinate queries cannot improve a deterministic exact policy.
- Randomization cannot reduce zero-error worst-case acquisition: every random seed inducing a correct deterministic policy inherits the same lower bound.
- The theorem is invariant under coordinate permutation and residue relabeling.
- Under independent composition of two instances, the additive coordinate-query model gives the sum of the two coordinate costs; this is not evidence of a nonlinear GC interaction.

## Exhaustive finite regression
`experiments/gc2_audit148_separator_acquisition.py` checks q=2..5 and n=2..6. It enumerates every coordinate subset and every assignment in Z_q^n, verifying that every proper subset has a cross-residue collision and the full set separates residues.

Local execution result: 20 parameter cases, 496 subset checks, 476 proper-subset collision checks passed, 20 full-set separation checks passed, 0 violations.

## Prior-art collision boundary
This lower bound is a standard deterministic decision-tree/query-complexity phenomenon. The Boolean q=2 case is ordinary parity: changing any unqueried input bit changes the required output, so exact deterministic computation is evasive and requires all n coordinate queries. Decision-tree complexity explicitly models adaptive input queries and worst-case tree depth. More general parity/query decision-tree literatures already study exact and randomized query lower bounds. Therefore neither Q*=n nor the weighted additive variant should be presented as independent GC-II novelty.

## Status ledger
- Exact separator coordinate-query lower bound Q*=n: **PROVED**.
- Weighted additive acquisition cost C*=sum_i w_i: **PROVED** under the stated coordinate-query/additive-cost model.
- Exhaustive finite regression: **PASS**.
- 'Cost to acquire a missing separator' by ordinary coordinate queries as GC-II novelty: **FALSIFIED**.
- Decision-tree/query-complexity mechanism: **IMPORTED/KNOWN**.
- A GC-II separator-acquisition obstruction surviving reduction to standard query/communication/CSP/join/contextuality models: **OPEN**.

## Scientific consequence
Audit 147's missing-global-information obstruction remains valid, but attaching ordinary query cost to the missing separator does not create a new theory. A surviving GC-II candidate must couple acquisition to a changing operational closure in a way for which the query itself changes what can subsequently be queried or executed, and then prove that the resulting lower bound is not merely a decision tree over an augmented state. The burden is now an irreducibility result for the acquisition grammar, not another parity/projection lower bound.
