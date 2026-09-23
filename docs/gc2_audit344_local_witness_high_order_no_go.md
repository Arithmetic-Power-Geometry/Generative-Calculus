# GC-II Audit 344 — Local witnesses do not imply low interaction order

## Scope
This audit attacks the open bridge after Audit 343: whether operational locality or uniformly small minimal witnesses can force a bounded-order capability-interaction expansion. GC-I on `main` is untouched.

Let `B` be baseline reachability, `E` the quotient-deduplicated newly grounded transitions, and `J_B(T)` Audit 342/343's Boolean-lattice Möbius interaction coefficient.

## Theorem 344.1 — Simple-path witness-size bound [PROVED / IMPORTED-KNOWN mechanism]
On a finite operational quotient with `q` states, every newly reachable ordered pair has an inclusion-minimal new-edge witness of cardinality at most `q-1`.

Proof. Any successful reachability witness has a directed walk in `B∪E`. Delete repeated-state cycles to obtain a simple path of at most `q-1` total edges. The subset of new edges used by that path is successful; an inclusion-minimal successful subset contained in it therefore has size at most `q-1`.

This is only a per-witness bound. It does not bound the union of alternative minimal witnesses.

## Theorem 344.2 — Bounded local witness size does NOT bound interaction order [PROVED]
For every integer `m>=1` there is a finite operational system in which every minimal witness for the distinguished capability `s->t` has size exactly 2, but its Möbius interaction coefficient is nonzero at order `2m`.

Construction. Use states `s,t,v_1,...,v_m`, identity baseline, and new grounded edges

`a_i=(s,v_i)`, `b_i=(v_i,t)`, `i=1,...,m`.

The minimal witnesses for `s->t` are exactly the pairwise-disjoint sets

`W_i={a_i,b_i}`.

Hence its reachability Boolean function is

`g(S)= OR_{i=1}^m [W_i subseteq S]`.

Let `T=union_i W_i`, so `|T|=2m`. By Audit 343's exact witness-union formula,

`j_{s,t}(T)=sum_{nonempty K subseteq {W_1,...,W_m}, union K=T} (-1)^(|K|+1)`.

Because the `W_i` are pairwise disjoint, the only subfamily whose union is `T` is the full family. Therefore

`j_{s,t}(T)=(-1)^(m+1) != 0`.

Thus interaction order is unbounded although every minimal witness has constant size 2.

## Corollary 344.3 — Naive locality-to-truncation bridge [FALSIFIED]
No universal implication of the form

`max minimal-witness size <= d  =>  J_B(T)=0 for |T|>F(d)`

can hold for any finite function `F` depending only on `d`, even at `d=2`.

Consequently, charging only the maximum number of newly admitted local operations needed by any single witness cannot justify a finite-order nonlinear capability-accounting law.

## What actually controls truncation
Audit 343's witness-union rank remains a valid sufficient coordinate:

`rho = max_p | union_{W in W_p} W |`.

Audit 344 separates it sharply from local witness size

`lambda = max_{p,W in W_p} |W|`.

The parallel-path family has `lambda=2` but `rho=2m`. Hence `rho/lambda=m` is unbounded.

This identifies **alternative-witness diversity/coverage**, not merely path locality, as an independent obstruction to low-order accounting.

## Edge, composition, and invariance checks
- `m=1`: order 2 coefficient is `+1`, consistent with a single two-edge composition.
- `m=2`: order 4 coefficient is `-1`; alternative routes create overlap rather than a new serial composition.
- Arbitrary `m`: sign alternates as `(-1)^(m+1)` and magnitude remains 1.
- State/edge relabelling preserves `lambda`, `rho`, interaction order, and coefficient magnitude.
- Duplicate syntax is excluded by quotient-deduplicating grounded transitions.
- The construction uses identity baseline, so the obstruction does not rely on hidden free baseline motion, cycles, resources, or information.
- Adding a resource/interface interpretation to each two-edge route does not remove the combinatorial obstruction unless it restricts the number/diversity of alternative witnesses.

## Exact verification
`experiments/gc2_audit344_local_witness_high_order_verifier.py` independently constructs the parallel-route family, enumerates all subsets for `m<=8`, computes reachability of `s->t`, evaluates the top Möbius coefficient directly, enumerates minimal witnesses, and compares against the closed form `(-1)^(m+1)`. The recorded artifact reports zero failures.

## Prior-art collision status
Minimal path sets, inclusion-exclusion, and multilinear/structure-function expansions are classical network-reliability machinery. In particular, exact reliability from multiple minimal path sets can require the full `2^n-1` inclusion-exclusion expansion. Therefore the high-order Boolean mechanism is **IMPORTED/KNOWN** and is not claimed as new mathematics. The GC-II advance is the no-go consequence for capability accounting: bounded operational witness locality alone cannot support bounded interaction order.

## Status
- simple-path bound on individual witness size: **PROVED / IMPORTED-KNOWN**
- constant witness size with arbitrarily high interaction order: **PROVED**
- bounded witness size implies bounded interaction order: **FALSIFIED**
- locality alone justifies fixed-order nonlinear Omega_G accounting: **FALSIFIED**
- witness-union rank as sufficient truncation coordinate: **PROVED in Audit 343**
- bridge from `(Delta R, Delta I, Delta A, Delta L)` to bounded alternative-witness diversity / witness-union rank: **OPEN**
- stronger structural conditions (bounded number of alternatives, laminarity, bounded overlap/incidence width, resource exclusivity) yielding compressible exact interaction spectra: **OPEN**
