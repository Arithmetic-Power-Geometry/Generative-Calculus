# GC-II Audit 147 — Proper-Projection Compiler No-Go

## Candidate attacked
Can an arbitrarily large exact augmented-state compiler recover the global operational world if its initial input consists only of all proper local coordinate projections?

## Construction
For integers q>=2 and n>=2 define q disjoint global worlds

R_r = {x in Z_q^n : sum_i x_i = r (mod q)},  r=0,...,q-1.

For every deleted coordinate j and every residue r,

pi_{-j}(R_r) = Z_q^(n-1).

Proof: given any assignment to the other n-1 coordinates, the deleted coordinate is uniquely chosen modulo q to make the total residue r. Hence every proper projection is full and, in particular, the complete family of proper projections is identical for all q worlds.

Yet R_r intersect R_s is empty for r != s. Therefore a compiler C whose initial input is any function solely of these proper projections receives exactly the same input on all q globally distinct worlds. No amount of internal finite or infinite state generated deterministically from that identical input can make exact reconstruction possible. Randomization cannot provide zero-error identification either, since the input distributions to the compiler are identical.

## Information lower bound
If an auxiliary tag Z is supplied and exact world identification is required, Z must distinguish q possibilities. Thus

H_0(Z) >= log2 q,

or at least ceil(log2 q) fixed binary bits are necessary. This is a lower bound on *new information supplied to the compiler*, not on its raw number of internal states.

## Join blow-up
Because every (n-1)-projection is the full cube, the natural join of the complete proper-projection family is Z_q^n, of size q^n, whereas each true R_r has size q^(n-1). The local reconstruction therefore has an exact spurious factor q.

## Status ledger
- Proper-projection indistinguishability theorem: **PROVED**.
- Auxiliary information lower bound log2 q: **PROVED**.
- Exhaustive q=2..6, n=2..7 regression: **PASS** (870 checks, 0 violations).
- Claim that arbitrarily large state augmentation can recover information absent from its inputs: **FALSIFIED**.
- Underlying local-to-global / projection-join obstruction: **IMPORTED/KNOWN**.
- This construction as independent GC-II novelty: **FALSIFIED**.
- GC-II-specific lower bound involving operationally generated translators under constraints not reducible to database joins, CSP/local consistency, contextuality/global-section obstruction, communication, or automata state complexity: **OPEN**.

## Prior-art collision boundary
The mathematical obstruction is not unique to GC. Database theory treats exact recovery from projections through lossless joins and join dependencies; lossy decompositions generate spurious tuples. CSP theory distinguishes local consistency from global satisfiability. Sheaf/contextuality frameworks formalize local compatible data that fail to determine or extend to an appropriate global object. Therefore Paper II must not claim the local/global obstruction itself as novel.

## Scientific consequence
The surviving route is not 'more augmented states.' State capacity cannot restore distinctions erased before compilation. A defensible GC-II theorem must make the missing global information arise from a specifically operational quantity—e.g. the minimum resource/action/interface cost required to *acquire* a separator not present in the local projections—and then prove a lower bound that cannot be rewritten as a standard query/communication/CSP/join width measure.
