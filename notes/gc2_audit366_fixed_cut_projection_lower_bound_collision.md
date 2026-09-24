# GC-II Audit 366 — Fixed-cut projection lower-bound collision

## Scope

This audit attacks the priority surviving after Audit 365: whether GC-I proper-projection irreducibility can yield a genuinely new quantitative lower bound by forcing a decision-preserving operational translator to communicate across a fixed interface cut.

GC-I on `main` remains frozen. No claim below changes GC-I.

## Candidate model

Split an operational world into two local descriptions `(x,y) in X x Y`. A terminal capability decision is a relation/function `f(x,y)`. A translator may inspect `x` on one side and `y` on the other, but information crossing the fixed cut is charged in bits. Let `C_cut(f)` be the minimum worst-case number of communicated bits required for exact deterministic capability preservation.

A proper-projection obstruction says that neither local projection alone determines the required global decision. The hoped-for GC-II strengthening was:

> proper-projection irreducibility forces a new operational local-to-global communication lower bound.

## Proposition 366.1 — rectangle reduction

**Status: PROVED; mechanism IMPORTED/KNOWN.**

Every deterministic fixed-cut translator of cost `c` induces at most `2^c` transcript classes, and every transcript class is a combinatorial rectangle `A x B` on which the terminal decision is constant (or relation-compatible). Hence any lower bound obtained solely by showing that local projections must be combined across this cut is a deterministic communication-complexity lower bound.

### Proof

Fix a deterministic protocol. At any transcript prefix, Alice's next message depends only on `x` and the prefix, and Bob's only on `y` and the prefix. By induction, the set of inputs producing any complete transcript factors as `A x B`. Correctness forces each leaf rectangle to be decision-compatible. A protocol communicating at most `c` bits has at most `2^c` binary transcripts/leaves. Therefore if every compatible rectangle partition needs at least `M` leaves, `c >= ceil(log2 M)`. QED.

## Proposition 366.2 — projection irreducibility is only a one-bit obstruction

**Status: PROVED.**

The statement that neither proper local projection determines `f` implies only that zero communication is impossible. It does **not** imply a growing lower bound.

### Separating family

Let `x,y in {0,1}^n` and

`f(x,y) = x_1 XOR y_1`.

Neither projection `x` nor `y` alone determines `f`, for every `n`. Yet one side can transmit the single relevant bit, after which the other computes `f`. Thus

`C_cut(f)=1`

for all `n` (under a one-way convention with the receiver holding the other input), despite persistent proper-projection irreducibility.

Therefore no theorem of the form

`proper-projection irreducible => C_cut(f) >= g(n)`

with unbounded `g` can hold without additional structural hypotheses.

## Corollary 366.3 — generic fixed-cut route is not GC-II novelty

**Status: FALSIFIED as a foundational-novelty route.**

Once the representation and cut are fixed, rectangle/fooling-set/rank/discrepancy/information-complexity methods already supply the classical language for translator lower bounds. A GC-II theorem that merely re-labels these as capability translation is not foundationally new.

## Important distinction

GC-I projection irreducibility may still be useful as a *semantic source* of hard capability relations, but it is not itself a quantitative complexity theorem. To obtain a GC-specific result one needs an additional bridge theorem that maps a GC-I invariant to a standard hardness measure and yields a nontrivial bound not already contained in the invariant's definition.

Candidate bridge forms include:

1. a quantitative projection-defect parameter `Pi_G` that lower-bounds rectangle partition number, discrepancy, information complexity, query complexity, or synthesis cost;
2. a compositional law showing how `Pi_G` amplifies under GC generation while ordinary local resource deltas remain bounded;
3. a separation family where `Pi_G` is computable from GC structure without solving the target communication problem itself.

Without item 3 the bridge is tautological: defining `Pi_G` to equal a known hardness measure adds no content.

## Prior-art collision boundary

Classical deterministic communication complexity partitions an input matrix into monochromatic rectangles; fooling-set, rank, rectangle-size and related methods lower-bound communication. Information complexity extends this to information revealed by randomized protocols. Therefore the fixed-cut translator problem is deliberately classified as imported unless a genuinely GC-derived structural invariant predicts those costs.

The contextuality/global-section literature also warns that local-to-global obstruction language is established in other settings; nonexistence of a global section is not by itself a new capability-accounting theorem.

## Consequence for Paper II

The target is narrowed again. The strongest defensible next attack is **not** another generic translator lower bound. It is to search for a GC-native, independently computable projection/generation invariant with all three properties:

- semantic: zero exactly on a meaningful locally reconstructible class;
- quantitative: provably lower-bounds an operational cost under explicit admissible interfaces;
- non-tautological: computable/bounded from GC generator structure without first computing that operational cost.

A promising falsification test is immediate: enumerate small generator systems, compute candidate structural projection defects and exact communication/query/synthesis costs, and search for equal-defect systems with different costs or low-defect/high-cost inversions. Any candidate failing this test should be rejected before theorem development.

## Status table

- deterministic fixed-cut translator -> rectangle protocol — **PROVED / IMPORTED-KNOWN**
- proper-projection irreducibility -> positive communication requirement — **CONDITIONAL / at most qualitative under the model**
- proper-projection irreducibility -> unbounded quantitative lower bound — **FALSIFIED**
- fixed-cut communication lower bound alone as GC-II breakthrough — **FALSIFIED**
- GC-native independently computable invariant lower-bounding operational cost — **OPEN / PRIORITY**
- small-world collision search for candidate GC-native invariants — **OPEN / NEXT**

## Scientific guardrail

No novelty is assigned here to rectangle protocols, fooling sets, rank/discrepancy methods, information complexity, global-section obstruction language, or communication lower bounds themselves. The only surviving novelty target is a non-tautological theorem connecting specifically GC generative/projection structure to operational capability cost.