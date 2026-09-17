# GC-II Audit 200 — Decision-critical coupling collapses to binary testing

## Candidate
Require a newly generated capability to make the correct one of two incompatible decisions in worlds w0,w1 that were confusable before generation. Let P0,P1 be the post-generation transcript laws induced by one admissible policy, and suppose its error is at most epsilon in each world.

## Exact theorem
For 0 <= epsilon <= 1/2,

TV(P0,P1) >= 1 - 2 epsilon.

Proof. The capability's terminal decision is a binary test phi. Its two errors obey
P0(phi=1) <= epsilon and P1(phi=0) <= epsilon. Hence their sum is <= 2 epsilon. The classical binary-testing identity says the minimum possible sum of the two errors over all tests is 1-TV(P0,P1). Therefore 1-TV(P0,P1) <= 2 epsilon.

The bound is tight: choose a binary transcript with P0(1)=epsilon, P1(1)=1-epsilon and decide phi(t)=t.

## Checks
- Domain: epsilon in [0,1/2]; TV is dimensionless in [0,1].
- epsilon=0 forces mutually singular transcript laws (TV=1).
- epsilon=1/2 gives only TV>=0 and is degenerate.
- Monotonicity: required distinguishability decreases linearly with allowed error.
- Post-processing: any terminal decision is a measurable post-processing of the transcript, so data processing cannot increase TV.
- Composition: the statement applies to the full joint transcript law; independent repeated observations can strengthen TV, but that is ordinary hypothesis-testing/sample-complexity theory.
- Counterexample boundary: if the new capability is not decision-critical for the pair, Audit 199's acquisition-orthogonal enlargement remains valid.

## Status ledger
- Decision-critical capability => TV(P0,P1) >= 1-2 epsilon: PROVED.
- Tightness: PROVED.
- This inequality as a GC-II novelty: IMPORTED/KNOWN (binary hypothesis testing / Le Cam two-point mechanism).
- Decision-critical coupling alone as a GC-II Closure-Escape breakthrough: FALSIFIED as a novelty route.
- A genuinely GC-specific bound must involve generative change in the admissible experiment family/cost geometry that is not reducible to a fixed post-generation testing experiment: OPEN.

## Reproducibility
`experiments/gc2_audit200_decision_critical_tv_bound.py` exhaustively checks all Bernoulli transcript pairs on the 1/20 grid and all deterministic binary decoders, including tight cases.
