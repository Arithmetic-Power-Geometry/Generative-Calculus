# GC-II Audit 374 — projection deficit collision

Status: PROVED REDUCTION / IMPORTED-KNOWN / FALSIFIED AS NOVELTY.

Fix a projection transcript p and let H_p be all histories producing p. Quotient H_p by exact future-capability equivalence h ~ h' iff every admissible continuation has the same capability outcome. Let N_Pi(p) be the number of equivalence classes.

Any exact deterministic translator preserving all future-capability answers on H_p needs at least N_Pi(p) internal states: representatives of two inequivalent classes cannot map to the same translator state. Therefore any fixed-length binary state encoding needs at least ceil(log2 N_Pi(p)) bits.

This is not a new GC-II invariant. It is Audit 356's capability quotient restricted to a projection fiber, and the mechanism is the classical distinguishability/minimal-state argument underlying Myhill-Nerode theory. Thus D_Pi=log2 N_Pi is a useful diagnostic but, by itself, is not foundational novelty.

Edge audit: N=1 gives zero deficit; unreachable fibers make no operational claim; infinite quotients need a specified representation model; relabelling preserves N; randomized/approximate translators need a distribution and error criterion; nondeterminism needs explicit may/must semantics.

An unconditional implication from proper-projection irreducibility to positive charged translator cost is also false unless side information/global initialization/shared state is forbidden or charged. A translator supplied directly with the missing class label trivially defeats such a bound.

Classification: fiberwise quotient lower bound PROVED; fixed-length bit counting bound PROVED; minimization mechanism IMPORTED/KNOWN; D_Pi alone as novel GC-II invariant FALSIFIED; restricted communication/query/approximation lower bounds OPEN and require collision checks against communication/information complexity and predictive-state theory.

Paper-II consequence: do not pursue raw quotient cardinality or its logarithm as the breakthrough. The surviving route must couple GC-I projection structure to an explicit restricted operational interface and prove a lower bound in a resource not already identical to residual-state counting.
