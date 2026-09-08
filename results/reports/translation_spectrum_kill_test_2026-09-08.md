# Translation-spectrum kill test — additive shift candidate

Status: **IMPORTED/KNOWN** for the uniform additive-shift sector. This note records a killed novelty route, not a breakthrough claim.

## Candidate examined

For two finite Pareto fronts `A,B` in a common resource space, consider the smallest scalar shift `delta` such that every point of `B` becomes weakly dominated by some point of `A` after adding the same `delta` to every resource coordinate:

`D(A <- B) = inf { delta : for every b in B there exists a in A with a_i <= b_i + delta for all i }`.

This is the most immediate scalar candidate for a GC translation deficit between two fixed task/resource frontiers.

## Exact collision

The expression is exactly the classical **binary additive epsilon indicator** `I_{epsilon+}(A,B)` from multiobjective optimization. In finite form,

`I_{epsilon+}(A,B) = max_b min_a max_i (a_i - b_i)`

(up to the harmless convention of clipping negative values at zero when one wants a nonnegative deficit).

Primary prior art: E. Zitzler, L. Thiele, M. Laumanns, C. M. Fonseca, and V. G. da Fonseca, “Performance assessment of multiobjective optimizers: an analysis and review,” *IEEE Transactions on Evolutionary Computation* 7(2), 117–132 (2003), DOI: 10.1109/TEVC.2003.810758. The additive epsilon indicator measures the minimum uniform translation required for one approximation set to weakly dominate another.

## Consequence for Generative Calculus

A GC “translation spectrum” is **not novel** if, after fixing one task, scale, error tolerance, and a common resource coordinate system, it reduces only to a uniform additive shift of Pareto fronts. Any claim based solely on that construction must be classified as imported/known.

A potentially GC-native route must therefore use structure absent from the ordinary epsilon indicator, for example one or more of:

1. coupled translation constraints across multiple task families rather than independent front comparisons;
2. composition-preservation constraints on translations;
3. scale/error-dependent overhead functions that must be jointly realizable by one operational map;
4. transition-dependent reachable envelopes with accumulated resource accounting;
5. invariants that remain nontrivial after every fixed-task Pareto-front epsilon indicator is matched.

## Strong falsification target for the next route

Construct worlds `W1,W2` for which all fixed-task additive epsilon indicators (and, where applicable, Blackwell/resource/GPT conversion data) agree, but a composition-coupled whole-envelope translation quantity differs. If no such finite example exists under the proposed axioms, the candidate should be rejected rather than promoted.

## Breakthrough decision

No breakthrough. This is a useful negative result because it prevents renaming a mature multiobjective quality indicator as a GC-native invariant.
