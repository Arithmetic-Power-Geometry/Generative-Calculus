# GC-II Audit 289 — Decision-relative exact capability sufficiency

Status: PROVED (finite deterministic setting); IMPORTED/KNOWN at the generic decision-sufficiency level; GC-II specialization only.

## Setup
Let `Y` be a finite attainable capability set and let `Q` be any family of downstream binary operational decisions `D_q : Y -> {0,1}`. Define the decision signature

`sig_Q(y) = (D_q(y))_{q in Q}`

and decision equivalence

`y ~_Q y' iff D_q(y)=D_q(y') for every q in Q`.

An exact account is a deterministic map `L:Y->S`. It is Q-sufficient when every downstream decision factors through L: for each q there exists `d_q:S->{0,1}` with `D_q=d_q o L` on Y.

## Theorem 289.1 — exact decision-relative sufficiency
For finite Y, the following are equivalent:

1. L is Q-sufficient.
2. `L(y)=L(y') => y ~_Q y'`.
3. `sig_Q` factors through L.

Hence every Q-sufficient account obeys

`|L(Y)| >= |Y / ~_Q|`,

and equality is achieved by the quotient account `[y]_Q`. A fixed-length binary account therefore needs at least

`ceil(log2 |Y / ~_Q|)` bits,

and this is achievable up to the ceiling by indexing quotient classes.

### Proof
(1=>2) If L(y)=L(y'), every factorized decision d_q receives the same account state, hence D_q(y)=D_q(y') for every q.

(2=>3) Define h(L(y))=sig_Q(y). Condition 2 makes h well-defined on L(Y).

(3=>1) Project h(L(y)) onto its q coordinate.

The cardinality lower bound follows because distinct equivalence classes cannot share an account state. The quotient map attains exactly one state per class.

## Corollary 289.2 — Audit 288 as a maximal-separation case
For the complete coordinatewise typed-budget family `D_q(y)=1[y<=q]`, q ranging over all nonnegative typed budgets, distinct y,y' in Y are separated by q=y or q=y'. Therefore `~_Q` is equality and `|Y/~_Q|=|Y|`, recovering Audit 288.

## Corollary 289.3 — exact task restriction can collapse accounting exponentially
For the independent-deposition family with m modules, each local output `(r,1)` or `(1,r)`, the full typed-budget family has `2^m` equivalence classes. Under the singleton aggregate decision family `Q_sum={D_B(y)=1[sum_i y_i <= B] : B>=0}`, every attainable y has sum `m(r+1)`, so there is one equivalence class. Thus the exact decision-relative state requirement can change from `2^m` to 1 solely by changing the downstream interface.

## Composition behavior
For product systems Y=Y1 x Y2 and a separable decision family containing only lifted local decisions from Q1 and Q2, signatures factor as a Cartesian product and

`|Y/~_Q| = |Y1/~_Q1| |Y2/~_Q2|`.

This multiplicativity need not hold for arbitrary coupled downstream decisions; no such claim is made.

## Edge/degenerate cases
- Q empty: one equivalence class (when Y nonempty), zero bits.
- |Y|=1: one class for every Q.
- Duplicate/redundant decisions do not alter the quotient.
- Enlarging Q can only refine equivalence, so `|Y/~_Q|` is monotone nondecreasing under added decisions.
- Relabeling account states leaves sufficiency invariant.
- Infinite Y/Q require cardinal/measurability/topological qualifications and are OPEN here.
- Randomized/lossy accounts are not covered; their correct analogue belongs to rate-distortion/Blackwell-style decision theory.

## Prior-art collision audit
The generic theorem is a finite deterministic sufficient-statistic / task-equivalence quotient result and is not claimed as novel. It aligns with statistical sufficiency, Blackwell decision sufficiency, automata-style indistinguishability quotients, and task-oriented compression. The GC-II value is architectural: it identifies the exact object that resource/interface accounting must preserve and prevents the false inference that typed-vector dimension, scalar dimension, or numerical reconstruction error alone determines operational accounting complexity.

## Consequence for Omega_G
Any decision-relative Generative Novelty Gap that charges accounting complexity should depend on the quotient induced by the admissible downstream decision family (or an approximate/lossy analogue), not raw representation dimension alone. A candidate exact information charge is `K_Q(Y)=log2 |Y/~_Q|`; this is a definition/known-style complexity measure, not yet a novel theorem. The next nontrivial target is an approximate decision-relative distortion that yields a genuine operational rate-distortion bound and connects to resource/information/action/rule increments without becoming tautological.
