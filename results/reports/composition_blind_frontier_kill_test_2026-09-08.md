# Composition-blind frontier kill test

Status: **IMPORTED/KNOWN mathematical skeleton; GC-scoped negative result**. This note records a falsification constraint, not a breakthrough claim.

## Question

Can a whole-envelope translation invariant be reconstructed from the collection of fixed-task Pareto frontiers alone when admissible translations are also required to preserve protocol composition?

## Finite counterexample

Take two four-protocol worlds with identical observable protocol labels, identical zero resource costs, and therefore identical fixed-task cost frontiers. Give the first protocol set the composition law of the cyclic group `C4 = Z/4Z`, and the second the composition law of the Klein four group `V4 = Z/2Z x Z/2Z`.

Every fixed-task resource summary can be made identical: same protocol count, same task labels, same costs, and the same one-point Pareto frontier `{0}` for each labelled primitive task. Nevertheless no faithful bijection can preserve the full composition law, because `C4` contains elements of order four whereas every non-identity element of `V4` has order two. A composition-preserving bijection would be a group isomorphism and would preserve element orders, which is impossible.

Hence any GC comparison quantity that depends only on independent fixed-task Pareto fronts is incomplete for composition-preserving whole-world translation.

## What this does and does not establish

The separation is rigorous, but its algebraic skeleton is elementary group theory and its process-composition interpretation lies close to established categorical/process-theoretic ideas. It must **not** be advertised as a historically new theorem merely because it is phrased in GC language.

Its value is as a kill test for proposed GC-native invariants: a candidate that assigns the same value to these two worlds while claiming completeness for composition-preserving translation is false or incomplete.

## Prior-art boundary

Symmetric monoidal/process theories already treat serial and parallel composition as first-class structure, and 2026 work formalising constructor theory as a process theory further raises the novelty bar for composition-aware operational frameworks. Therefore the mere addition of a composition table or functorial preservation requirement is not sufficient GC novelty.

Relevant recent reference: M. H. Waseem, *String Diagrams for Quantum Foundations, Computing and Natural Language Processing*, arXiv:2605.11417 (submitted 2026-05-12), including a process-theoretic formalisation of constructor theory and analysis of composition/locality constraints.

## Research consequence

A defensible translation-spectrum breakthrough must survive both of the following:

1. fixed-task Pareto/epsilon-indicator matching; and
2. ordinary algebraic/categorical composition invariants.

The strongest remaining target is therefore a quantity that couples **task family, scale/error, heterogeneous resource budgets, composition, and reachable-state dependence** in a way that is not reducible to a standard enriched/functorial process comparison.

## Breakthrough decision

No breakthrough. The result narrows the search space and supplies an exact falsification test for composition-blind GC metrics.
