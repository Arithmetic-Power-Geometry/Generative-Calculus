# GC-II Audit 209 — unconditional closure-to-work lower bound fails

## Target
Audit 208 left open whether a strict change in budgeted generative closure can force a positive lower bound on experimentally measured translator work, robust to experiment-language enrichment and state augmentation.

## Definition
Let a finite operational system S=(X,G,c,B) have states/capabilities X, admissible generators G, measured nonnegative work c:G->Q_{>=0}, and budget B. Its budgeted closure C_B(x) is the set of capabilities reachable from x by finite generator words whose total measured work is at most B.

A proposed unconditional No-Free-Capability principle would require a function phi with phi(delta)>0 for every positive closure novelty delta such that strict/new capability generation implies measured work W >= phi(delta).

## Proposition 209.1 — strict budgeted closure escape need not require positive work
There exists a finite exact system with C_B^0(x) proper subset C_B^1(x), while the minimum measured work needed to realize every newly reachable capability is zero.

Construction: X={x,y}. Baseline G0={id}, with c(id)=0. Extended system G1={id,g}, where g(x)=y, g(y)=y and c(g)=0. For every B>=0,

C_B^0(x)={x},   C_B^1(x)={x,y},

but W_min(x->y)=0.

Therefore no universal strictly-positive lower bound can follow from closure enlargement alone.

**Status: PROVED by construction.**

## Proposition 209.2 — enrichment and state augmentation do not repair the implication
Include measured work itself in the experiment transcript. The new generator is then observed to consume exactly zero work, so enrichment does not create a positive lower bound. Augmenting the state with generator/mode labels likewise preserves the zero-cost transition. Hence the counterexample is not an artifact of hidden cost or omitted state.

**Status: PROVED for the construction.**

## Scope and weakest repair
This does not say physically interesting capabilities are free. It says a positive No-Free-Capability theorem requires an additional axiom excluding free capability-generating transformations. One possible axiom is closure-preservation of all zero-work operations:

c(g)=0 => g(C_B(x)) subseteq C_B(x) for the chosen baseline closure/resource structure.

But under that axiom, the statement 'strict escape requires nonzero work' is essentially built into the definition/free-operation boundary. Stronger GC-II novelty would require an independently justified quantitative continuity/coercivity law connecting measured resource expenditure to a representation-invariant capability distance.

## Exact witness
`experiments/gc2_audit209_no_free_capability_counterexample.py` checks the two-state construction for budgets 0,1,17; verifies strict closure enlargement; computes minimum work exactly; and verifies that adding cost to the observable transcript leaves the minimum at zero.

## Checks
- Domains: finite X and finite generator sets.
- Dimensions: closure novelty is set-valued; work is a separate nonnegative rational coordinate. No dimensionally invalid subtraction is used.
- Edge case B=0: escape already occurs and is the sharpest witness.
- Degenerate case: identity-only baseline is intentional; the same construction can be adjoined to any finite baseline by adding a fresh zero-work generator to a fresh capability.
- Monotonicity in B: both closures are monotone in budget; the separation persists for every B>=0.
- Invariance: renaming x,y or augmenting state labels does not alter reachability/work.
- Composition: nonnegative additive path work leaves a zero-cost generator word at zero.
- Experiment enrichment: explicitly measuring c(g)=0 cannot yield a positive lower bound.
- Reduction/prior-art boundary: resource theories define free operations precisely relative to a chosen resource structure; resource-destroying/free-operation frameworks already separate free from resource-generating transformations. Thus excluding zero-cost resource generation is an assumption of the operational resource model, not a consequence of closure enlargement alone.

## Ledger
- Strict budgeted closure enlargement => positive measured translator work: **FALSIFIED** without additional assumptions.
- Zero-work strict closure escape finite witness: **PROVED**.
- Robustness of witness to cost-observable enrichment/state augmentation: **PROVED**.
- 'Free operations do not generate resource' boundary: **IMPORTED/KNOWN resource-theory principle**.
- No-Free-Capability under explicit zero-work closure-preservation: **CONDITIONAL**, but risks tautology.
- Quantitative coercivity theorem W >= phi(Omega_G) from independently measurable physics/complexity: **OPEN**.

## Next gate
Do not attempt another unconditional positive work bound. Seek a non-tautological coercivity assumption derivable from a concrete substrate (communication cut, irreversible erasure, query lower bound, locality/translator constraint, or computational complexity) and ask whether one theorem schema transports such independently proved lower bounds into GC budgeted closure without reducing to the source theory itself.
