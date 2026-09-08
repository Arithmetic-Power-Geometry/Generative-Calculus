# GC-II Status Ledger

## Branch
`gc2-capability-accounting-lab`

## Current state
- Operational closure: **PROVED finite formalization** via lifted cumulative-resource state; naive base-state budget closure **FALSIFIED** by budget-refresh idempotence failure
- Generative Novelty Gap: **PROVED finite single-target candidate** as minimum operational augmentation penalty; exact path-deficit reduction established; first whole-envelope/interface-only shared-translator specialization PROVED; general global-translator version OPEN
- Closure-Escape Criterion: **PROVED for the finite single-target Omega_G candidate** (`Omega_G=0` iff target lies in lifted budgeted closure under positive-definite monotone penalty); shared-translator zero-gap criterion PROVED in the finite collision specialization; stronger operational whole-envelope criterion OPEN
- No-Free-Capability Theorem: **PROVED restricted finite specialization**: a shared deterministic translator facing maximum collision multiplicity `m` requires at least `ceil(log2 m)` bits of auxiliary interface distinguishability when task identity is otherwise unavailable; universal theorem OPEN
- Quantitative Capability-Accounting Bound: finite candidate upper bound `Omega_G <= F(Delta R,Delta I,Delta A,Delta L)` remains valid for a specified sufficient augmentation under its hypotheses. **Universal aggregate-only exact accounting F(Delta R,Delta I,Delta A,Delta L) FALSIFIED** for state-dependent/noncommuting transformations: equal aggregate R/I/A/L increments can yield different capabilities. Ordered/path-dependent accounting or an operational trace quotient is required in general. Static aggregate accounting is restored for commuting/path-independent subclasses.
- Complete Convertibility Criterion: finite shared-deterministic-translator specialization PROVED via source-fibre functional consistency; **universal finite complete-monotone target FALSIFIED as a defensible general goal** by collision with known quantum-resource-theory impossibility; finite-preorder principal-lower-set indicators give a tautological complete family; structured compressed finite/computable or infinite/dual criterion OPEN
- Generative Order: OPEN (seeded by GC-I projection irreducibility)
- Proper-projection parity obstruction: PROVED mechanism / computationally reverified through m=10 / known mathematical mechanism
- Arity-only translator lower bound: FALSIFIED for unrestricted compositional translators
- Resource-accounted reconstruction complexity K_G: OPEN / highest-priority asymptotic route
- Global shared-translator obstruction: **PROVED finite specialization**; all taskwise gaps may vanish while one shared translator fails due source-fibre collisions
- Operational-trace lift: **PROVED restricted finite specialization** for full task/scale/error/vector-budget/I/A/L trace records; exact fibre criterion and `q_min=m`, `b_min=ceil(log2 m)` survive on a fixed feasible trace family. Mechanism remains KNOWN/IMPORTED; trace bookkeeping alone is not a breakthrough.
- Exact auxiliary-interface theorem: **PROVED** in the finite shared-translator model: minimum interface alphabet size equals maximum collision multiplicity; fixed-width bits equal `ceil(log2 m)`
- Reversibility Gap: **NAIVE METRIC ROUTE FALSIFIED** for the current nonlinear `Omega_G`; exact R/I cross-channel counterexample gives `Omega(x,z)=3 > Omega(x,y)+Omega(y,z)=2`. Symmetric round-trip cost remains a diagnostic only. Composition-compatible repair or explicit nonmetric interaction-surplus theory OPEN.
- Order-sensitive accounting: **PROVED boundary theorem / decisive falsification**. Equal aggregate augmentation vectors need not imply equal capability under noncommuting state-dependent transformations. Pairwise commutation plus path-independent accounting restores aggregate sufficiency. Mechanism is KNOWN/IMPORTED neighborhood (planning preconditions, affordances, transition dependence, partial-order reduction); no novelty claim.
- Exact finite-world experiments: ACTIVE; deterministic parity audit PASS through m=10
- Budgeted-closure audit: PASS; 729 exhaustive 3-state worlds, 6,561 singleton-start/budget cases, 59,049 lifted start-set monotonicity inclusion checks; 0 violations after lifted-state repair
- Omega_G audit: PASS; 576 three-state gated/resource worlds, 13,824 world/context cases; brute augmentation enumeration and exact path formula agree with 0 mismatches; zero-gap closure equivalence and context monotonicity show 0 violations
- Shared-translator audit: PASS by exhaustive source/target assignment enumeration for `n=1..4`, binary source alphabet, three-label target alphabet: 1,554 paired finite worlds; constructive sufficiency and lower-bound checks included
- Reachable-envelope transport finite audit: PASS; 20,000 randomized worlds, 11,441 reachable sampled pairs, 36,171 membership checks, 0 violations in the nonnegative additive path-cost specialization
- Composition-cost assumption audit: PASS; explicit superadditive counterexample shows subadditivity/control is necessary
- Prior-art status of finite Omega_G: **high collision risk / not a breakthrough claim** because the resource component reduces to mature resource-constrained shortest-path/minimum-augmentation structure; Le Cam deficiency is also a neighboring directed-gap precedent
- Prior-art status of global translator collision theorem: **KNOWN/IMPORTED mechanisms** (functional consistency, pigeonhole coding, repeated-feature classification error); GC-II novelty not established by this specialization alone
- Prior-art status of reversibility diagnostics: **KNOWN/IMPORTED neighborhood**; forward/reverse conversion asymmetry and irreversibility are mature in thermodynamics and resource theories. No novelty claim from a simple forward/reverse sum or difference.
- AI capability-accounting experiment: OPEN
- Robotics validation: OPEN
- Scientific-discovery validation: OPEN
- Breakthrough status: NONE YET

## Evidence rule
Nothing in this ledger may be upgraded to PROVED or BREAKTHROUGH CANDIDATE without a proof artifact or reproducible computational/empirical evidence plus prior-art collision review.

## Immediate test order
1. Replace aggregate-only accounting by an ordered augmentation trace functional, then seek the coarsest operational equivalence relation on traces under which capability and cost are invariant.
2. Couple translator-visible fibre refinement to explicit admissible R/I/A/L transformations whose availability and effects may change with state. Price the minimum ordered cost required to split conflicting fibres.
3. Define a whole-envelope directed `Omega_G` requiring one globally realizable translator and test identity, monotonicity, composition behavior, invariance, degeneracies, and order sensitivity. Do **not** assume a triangle inequality under a superadditive interaction penalty.
4. Seek a nontrivial lower bound linking minimum dynamic fibre-refinement cost to vector-resource budgets and information/action/rule acquisition, with explicit cross-channel interaction and order terms.
5. Characterize commuting/path-independent subclasses where an aggregate `F(Delta)` theorem is valid; collision-check against trace monoids, partial-order reduction, planning, Petri nets and resource theories.
6. Seek a finite/computable complete monotone family only for an explicitly structured translator class; otherwise seek an infinite separating family or dual/separation-oracle criterion. Do not pursue a universal finite family.
7. Specify admissible world-transition operators before attempting a broader No-Free-Capability theorem.
8. Define natural resource-restricted translator models and test whether K_G reduces to known circuit, communication, database, CSP, extension-complexity or simulation-preorder measures.
9. Search whole-envelope matched pairs where fixed-task Pareto data and low-order summaries agree but global translation/reconstruction costs differ.
10. Audit all candidate quantities against mature neighboring concepts, including catalysis, irreversibility, directed deficiencies, planning, affordances and impossibility of finite complete monotone sets.

## Reproducible artifacts
- `gc2/BUDGETED_CLOSURE_AUDIT_004.md`
- `gc2/tests/test_gc2_budgeted_closure.py`
- `gc2/OMEGA_G_AUDIT_005.md`
- `gc2/omega_gap.py`
- `gc2/tests/test_gc2_omega_gap.py`
- `gc2/GLOBAL_TRANSLATOR_AUDIT_006.md`
- `gc2/global_translator.py`
- `gc2/tests/test_gc2_global_translator.py`
- `gc2/RESOURCE_INTERFACE_NONSUBSTITUTION_AUDIT_008.md`
- `gc2/COMPLETE_MONOTONE_BOUNDARY_AUDIT_009.md`
- `gc2/REVERSIBILITY_GAP_AUDIT_010.md`
- `gc2/OPERATIONAL_TRACE_TRANSLATOR_AUDIT_011.md`
- `gc2/FIBRE_REFINEMENT_CLOSURE_ESCAPE_AUDIT_012.md`
- `gc2/ENDOGENOUS_FEATURE_POLICY_AUDIT_013.md`
- `gc2/ORDER_SENSITIVE_ACCOUNTING_AUDIT_014.md`
- `gc2/tests/test_gc2_order_sensitive_accounting.py`
- `gc2/tests/test_gc2_reversibility_gap.py`
- `gc2/LOCAL_TO_GLOBAL_AUDIT_002.md`
- `gc2/TEST_REPORT_003.md`
- `gc2/tests/test_gc2_finite_audit.py`
