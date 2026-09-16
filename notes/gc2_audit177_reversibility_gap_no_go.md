# GC-II Audit 177 — Reversibility-Gap No-Go and Surviving Boundary

## Question
Can a reversibility-gap invariant survive Audit 176's finite product-compilation no-go and provide independent GC-II novelty?

## Setup
Let a budgeted operational closure induce an extended directed minimum-cost function

\[
D(x,y)=\inf_{\pi:x\leadsto y} C(\pi),\qquad D(x,y)\in[0,\infty].
\]

Assume nonnegative path cost and sequential subadditivity, so `D(x,x)=0` and `D(x,z)<=D(x,y)+D(y,z)`.

Natural reversibility candidates include

\[
G_{\rm diff}(x,y)=|D(x,y)-D(y,x)|,
\]

\[
G_{\rm cyc}(x,y)=D(x,y)+D(y,x),
\]

and, when both directions are finite and positive,

\[
G_{\rm ratio}(x,y)=\max\{D(x,y)/D(y,x),D(y,x)/D(x,y)\}.
\]

The ratio is deliberately left undefined when a denominator is zero; assigning `+infinity` is possible when exactly one direction has zero cost, but this is a convention rather than new structure.

## Theorem — distance-determined reversibility no-go
**Status: PROVED.**

Let `G(x,y)=g(D(x,y),D(y,x))` for any deterministic function `g` on the extended nonnegative reals. If two operational systems have the same all-pairs directed minimum-cost matrix `D`, then they have identical `G` for every pair.

### Proof
Immediate by substitution: equality of the two directed cost arguments for every ordered pair forces equality of `g` on every unordered pair. QED.

This is elementary, but it closes an important GC-II route: no forward/reverse scalar computed only from minimum closure costs can recover witness geometry, hidden implementation structure, provenance, concurrency, or any other information already discarded by `D`.

## Structural consequences
1. `G_diff` measures only antisymmetry of the directed cost values. It can vanish for distinct states even when both directions have large equal cost.
2. `G_cyc` is a round-trip cost, not a pure irreversibility measure: it is positive even for perfectly symmetric nonzero costs.
3. `G_ratio` is scale-invariant under multiplication of all costs by a common positive scalar, but is singular at zero and does not solve the information-loss problem.
4. Unreachable reverse direction (`D(y,x)=+infinity`) already records topological irreversibility in the directed reachability/cost structure.
5. Zero-cost cycles can identify distinct states at zero directed distance; any `D`-only reversibility score inherits that degeneracy.
6. Under product composition with additive path costs, the candidate gaps obey only consequences of the component directed costs; no new interaction term appears without additional operational data.

## Prior-art collision boundary
The underlying object is directed path/reachability geometry. Forward-versus-reverse comparisons are also standard in thermodynamic irreversibility, stochastic path reversal, and resource theories where formation/cost and distillation/yield need not coincide. Therefore a scalar based only on forward and reverse closure costs is not an independent GC-II invariant.

Recent resource-theory work goes further and proves resource-cost/irreversibility tradeoffs for channels, so even a generic statement that more reversibility requires resource expenditure is not safe as a novelty claim without substantially different hypotheses and predictions.

## Stronger path-distribution escape also collides
If one replaces minimum costs by forward and reverse trajectory distributions and measures their discrepancy (for example by relative entropy), the construction enters established stochastic-thermodynamic/time-series irreversibility territory. This can be operationally useful, but it is not by itself a GC-II breakthrough.

## What survives
A candidate reversibility residual must depend on operational information not determined by either:

- the compiled finite transition/game semantics plus costs; or
- standard forward/reverse trajectory laws available to the observer.

A defensible surviving direction is **intervention-relative recoverability**: after executing a capability-generating transformation, ask what additional *newly enabled or disabled admissible intervention family* is required to restore not merely the state but the original future closure operator. However, under finite Markov sufficiency Audit 176 compiles this intervention family into state, so novelty requires a uniform restriction on the recovery interpreter/observer or a non-finitely-compilable family.

## Quantitative candidate to test next
For a restricted interpreter class `K`, define

\[
\mathcal R_K(x\to y)=\inf\{B:\exists k\in K\text{ that restores observational equivalence of the original closure from }y\text{ within budget }B\}.
\]

Then define an interpreter-relative asymmetry

\[
\Omega^{\rm rev}_{G,K}(x,y)=\mathcal R_K(x\to y)-D(y,x)
\]

when both terms are finite and dimensionally commensurate.

**Status: OPEN.** This is not claimed novel. It must first prove that `K` is scientifically motivated rather than chosen to manufacture separation, that the quantity is invariant under admissible recodings, and that it does not reduce to constrained planning, program synthesis, Kolmogorov/description complexity, logical depth, or resource-bounded recovery.

## Ledger
- any reversibility gap `g(D_forward,D_reverse)` is determined by directed closure cost — **PROVED**;
- such a gap as independent GC-II novelty — **FALSIFIED**;
- topological one-way irreversibility from infinite reverse distance — **IMPORTED/KNOWN**;
- trajectory forward/reverse divergence as generic novelty — **IMPORTED/KNOWN mechanism**;
- unrestricted recovery complexity under finite Markov semantics — **FALSIFIED by product compilation / known planning structure**;
- interpreter-relative closure recoverability `R_K` — **OPEN**;
- interpreter-relative excess recovery gap `Omega_rev_G,K` — **OPEN, novelty unestablished**.

## Next attack
Stress-test `R_K` on exact finite worlds using natural restricted interpreter classes (bounded-memory, bounded-interface, local, or fixed-description interpreters). Search for pairs with identical ordinary transition/cost semantics but different restricted recovery burden. For every separation, attempt explicit reductions to constrained planning, automata/state complexity, communication complexity, program synthesis, reversible computation, and algorithmic information before retaining it.