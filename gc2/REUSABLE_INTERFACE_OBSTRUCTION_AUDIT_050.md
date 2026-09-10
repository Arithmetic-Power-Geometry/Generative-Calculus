# GC-II Audit 050 — Reusable Whole-Family Interface Obstruction Collision

Status date: 2026-09-10
Branch: `gc2-capability-accounting-lab`
Parent audit: 049

## Question

Can GC-II obtain a new invariant from the cost of one reusable interface that serves an entire conserved obligation family, even when each obligation separately has matched extensional behavior and matched standalone cost?

## Formal candidate

Let X be a finite substrate state set and Q a conserved obligation family. Each q in Q is an extensional map q:X->Y_q. A reusable interface consists of an encoding/preprocessing map E:X->M and decoders D_q that recover q(x) from controlled access to M. Let C(E) be construction/storage cost and T_q(E,D_q) downstream translation/query cost. Define the whole-family frontier

J_X(Q) = ParetoMin { (C(E), (T_q)_{q in Q}) : D_q(E(x)) = q(x) for every x and q }.

The proposed GC-II mechanism would require a joint obstruction in J_X(Q) that is not reducible to ordinary preprocessing/data-structure/coding complexity.

Status: definition valid; novelty OPEN before collision test.

## Exact finite witness

Take X={0,1}^n and Q={q_i : q_i(x)=x_i, i=1,...,n}. Every obligation q_i separately has a one-bit standalone realization: construct/store x_i and answer q_i with one probe. Thus all individual obligation costs can be matched across descriptions.

For one exact reusable deterministic interface E that must support all q_i, E must be injective. If E(x)=E(x') for distinct x,x', choose a coordinate i with x_i != x'_i. Decoder D_i receives the same stored representation on x and x' and therefore cannot answer both correctly. Hence |M| >= 2^n, so any fixed-length binary representation requires at least n bits.

This gives an exact whole-family lower bound even though every member separately requires only one output bit.

Status: PROVED.

## Why this does not establish GC-II novelty

The witness is precisely static data-structure/encoding complexity. A static data structure preprocesses data x into a representation phi(x) and supplies query algorithms for a family f(x,q). The GC-II reusable interface E is phi; the conserved obligation index q is the data-structure query; and downstream translator cost is probe/query complexity. The injectivity proof is the elementary information-theoretic storage lower bound for supporting all coordinate-retrieval queries exactly.

More sophisticated joint construction-versus-query tradeoffs are also already a central subject of the bit-probe/cell-probe and succinct-data-structure literature. Thus replacing the n-bit witness by a harder query family or proving a superconstant redundancy/query tradeoff would strengthen the complexity result but would not, without another ingredient, produce a distinct generative law.

Status: reusable-interface obstruction as standalone Omega_G route FALSIFIED / IMPORTED-KNOWN mechanism.

## Compiler quotient does not rescue the witness

Suppose semantics-preserving compilers may change representation but must preserve exact support for every q_i. Any compiled reusable representation still induces an injective code for x, because the full answer vector (q_1(x),...,q_n(x)) equals x. Therefore representation changes cannot beat the n-bit information lower bound. This makes the obstruction representation-safe, but representation safety does not make it novel: data-structure lower bounds are already representation-independent within their declared computational model.

Status: PROVED.

## Stronger tradeoff form and collision

Let s be stored bits and t the worst-case number of bit probes needed for a query. The coordinate family has the trivial exact constraint s>=n, but nontrivial query families exhibit redundancy/query-time tradeoffs. Such tradeoffs are established in succinct data structures and locally decodable coding. Therefore a candidate of the generic form

    construction/storage burden * downstream query burden >= f(n)

is not sufficient for GC-II novelty.

Status: IMPORTED/KNOWN architecture.

## Dimension/domain/edge checks

- n=0 gives the empty family and zero information requirement.
- n=1 gives one bit, matching the standalone and reusable costs; there is no joint overhead.
- Variable-length lossless representations require a declared worst-case or expected-length convention; the fixed-length theorem above is n bits exactly.
- Approximate recovery changes the theorem and requires an error probability/distribution; no approximate claim is made here.
- Randomized exact decoders do not evade injectivity if correctness is required with probability one for every input.
- If only a strict subset of coordinate obligations must be supported, the information lower bound becomes the number of independent required coordinates.
- Correlated/restricted substrate states replace n by at least log2 of the number of equivalence classes induced by the complete answer vector; this is again sufficient-statistic/encoding structure.
- Typed physical construction, information, action, and rule costs cannot be added without conversion laws; the bit lower bound constrains only the information/storage component.
- Independent products multiply distinguishable answer classes, so log-cardinality lower bounds add; this is ordinary information composition.

## Consequence for Omega_G

The conjunction

1. identical extensional obligation maps,
2. matched standalone cost for every individual obligation,
3. one reusable interface required for all obligations,
4. a representation-safe superconstant joint lower bound

is still insufficient for generative novelty. It can be completely explained by static data-structure or coding complexity.

Therefore Omega_G must not be defined as a generic whole-family preprocessing/storage/query tradeoff.

## Stronger surviving target: endogenous obligation creation

Audits 040-050 have progressively removed fixed extensional maps, fixed bases, installation savings, closure expansion, expected-value shifts, complete value surfaces, intervention interactions, fixed-interface translator costs, and reusable fixed-query-family interfaces as standalone novelty mechanisms.

The remaining structural possibility is to stop treating Q as exogenously fixed.

Define a history-dependent obligation generator G that, after observing an admissible interaction history h, produces a new obligation q_h not necessarily named in the initial family Q_0. A system must both (i) construct/identify the obligation and (ii) realize it under the same accounted operational rules. The candidate object is therefore not a data structure for a fixed query set but an endogenous inquiry/capability process

    h -> q_h -> admissible realization of q_h.

A nontrivial GC-II theorem would need to prove a resource lower bound or closure-escape criterion for this coupled generation-realization process that cannot be compiled into a fixed enlarged query universe without paying the very resource being bounded.

This is NOT yet a breakthrough. It is the next severe target.

Immediate collision classes: online algorithms, adaptive data structures, active learning, adaptive query complexity, program synthesis, metareasoning, open-ended search, algorithmic information, proof search, endogenous scientific inquiry, and universal computation. The kill test is explicit: if q_h can be costlessly enumerated in advance into a fixed Q*, Audit 050 reduces the problem back to known data-structure/query complexity and Omega_G must vanish beyond those known costs.

Status: OPEN.

## Final classification

- Whole-family coordinate interface n-bit lower bound: PROVED.
- Compiler-invariant injectivity obstruction: PROVED.
- Reusable fixed-family interface obstruction as standalone GC-II novelty: FALSIFIED.
- Generic construction/query tradeoff: IMPORTED/KNOWN data-structure/coding architecture.
- Endogenous obligation generation coupled to realization: OPEN; next target, with a strict pre-enumeration kill test.
