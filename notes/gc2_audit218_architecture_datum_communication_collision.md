# GC-II Audit 218 — architecture-as-datum does not by itself rescue translator novelty

## Question
Audit 217 left open whether making the projection/interface architecture part of the operational datum, rather than an analyst-chosen simulator class, forces a representation-invariant translator excess.

## Fixed operational datum
Let X and Y be finite local state sets attached to two physically/operationally specified interfaces. Let f:X×Y→{0,1} be a required global decision. The architecture datum fixes that the X-side initially has only x, the Y-side initially has only y, local computation is free, and the only cross-interface translator resource is a noiseless binary transcript. This is not an analyst-selected post-hoc restriction: it is part of the experiment specification.

Let T_A(f) be the minimum worst-case number of transmitted bits required by a deterministic exact translator respecting architecture A.

Define the communication matrix M_f by (M_f)_{xy}=f(x,y), interpreted over R.

## Proposition 218.1 — architecture-fixed rank lower bound
For every deterministic exact protocol of worst-case transcript length c,

    T_A(f)=c >= ceil(log2 rank_R(M_f)).

### Proof
A deterministic c-bit protocol partitions X×Y into at most 2^c monochromatic combinatorial rectangles. The indicator matrix of each rectangle has real rank at most one. M_f is a sum of at most 2^c such rank-one rectangle matrices (using only the 1-leaves; this can only reduce the count). Hence rank_R(M_f) <= 2^c, and c >= log2 rank_R(M_f). Integer-valued c gives the ceiling. QED.

## Edge cases
- Constant f: rank(M_f)=1, so the bound gives 0 bits and is tight.
- Empty domains are excluded; otherwise the communication matrix has no operational instance.
- Rank 1 does not imply zero communication for every nonconstant Boolean f, so rank is a lower bound, not a complete translator invariant.
- Relabeling rows/columns preserves rank and the bound.
- Duplicating a row or column preserves rank although it changes raw interface cardinality, showing why |X| or |Y| alone is not an invariant lower bound.
- Composition does not justify additivity: protocols can reuse transcripts or jointly encode tasks. No additive theorem is claimed.

## Exact witness family
For equality on n labels, M_f=I_n, so rank(M_f)=n and every deterministic exact translator needs at least ceil(log2 n) bits. The obvious protocol sending the binary label achieves ceil(log2 n), hence equality has exact translator cost ceil(log2 n).

## Novelty collision
This result is a standard deterministic communication-complexity/log-rank lower-bound mechanism. Once the interface partition and cross-interface transcript are operationally fixed, the proposed GC translator problem becomes an ordinary communication problem. Thus "make architecture part of the datum" removes Audit 217's arbitrariness objection but does not by itself create a GC-specific invariant.

The same boundary appears more broadly in distributed algebraic computation and distributed linear-algebra lower bounds: operationally fixed placement/network models are precisely what make communication lower bounds meaningful.

## Consequence for GC-II
A GC-II local-to-global theorem cannot claim novelty merely from:

1. fixed local projections/interfaces,
2. a global task not locally decidable, and
3. a positive communication/translator lower bound.

Those ingredients reduce to established communication complexity.

A surviving GC-specific target must use additional GC structure that is not erased by the communication matrix — for example a theorem linking *changes in generative closure under admissible composition* to a lower bound on translator complexity, while separating that lower bound from the communication complexity of the already-fixed input/output behavior.

A possible residual quantity is

    Xi_GC = T_GC - T_behavior,

but it is meaningful only if T_GC and T_behavior are measured under the same fixed architecture and Xi_GC can be proved positive from GC-specific closure/projection data rather than by changing the protocol class. This remains OPEN.

## Ledger
- Architecture-fixed deterministic translator rank bound: PROVED / IMPORTED-KNOWN mechanism.
- Equality witness with exact ceil(log2 n) translator cost: PROVED.
- Architecture-as-operational-datum removes arbitrary-K objection: PROVED.
- Positive architecture-fixed translator cost as intrinsically GC-specific novelty: FALSIFIED.
- GC-specific excess above matched behavioral communication complexity: OPEN.

## Prior-art boundary checked
Communication complexity/log-rank; distributed algebraic computation; distributed linear algebra; automata/Hankel minimal realization. The last comparison is important: Hankel rank already measures behavioral realization dimension, while communication rank bounds measure cross-interface transcript cost. Neither alone supplies the desired GC novelty gap.
