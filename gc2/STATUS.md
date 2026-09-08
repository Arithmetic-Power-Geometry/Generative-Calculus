# GC-II Status Ledger

## Branch
`gc2-capability-accounting-lab`

## Current state
- Operational closure: **PROVED finite formalization** via lifted cumulative-resource state; naive base-state budget closure **FALSIFIED** by budget-refresh idempotence failure
- Generative Novelty Gap: **PROVED finite single-target candidate** as minimum operational augmentation penalty; exact path-deficit reduction established; first whole-envelope/interface-only shared-translator specialization now PROVED; general global-translator version OPEN
- Closure-Escape Criterion: **PROVED for the finite single-target Omega_G candidate** (`Omega_G=0` iff target lies in lifted budgeted closure under positive-definite monotone penalty); shared-translator zero-gap criterion PROVED in the finite collision specialization; stronger operational whole-envelope criterion OPEN
- No-Free-Capability Theorem: **PROVED restricted finite specialization**: a shared deterministic translator facing maximum collision multiplicity `m` requires at least `ceil(log2 m)` bits of auxiliary interface distinguishability when task identity is otherwise unavailable; universal theorem OPEN
- Quantitative Capability-Accounting Bound: **PROVED finite candidate upper bound** `Omega_G <= F(Delta R,Delta I,Delta A,Delta L)` whenever the stated augmentation realizes the target; nonlinear interaction penalty implemented; exact interface lower bound PROVED in the shared-translator collision specialization; universal lower bounds OPEN
- Complete Convertibility Criterion: finite shared-deterministic-translator specialization PROVED via source-fibre functional consistency; **universal finite complete-monotone target FALSIFIED as a defensible general goal** by collision with known quantum-resource-theory impossibility; finite-preorder principal-lower-set indicators give a tautological complete family; structured compressed finite/computable or infinite/dual criterion OPEN
- Generative Order: OPEN (seeded by GC-I projection irreducibility)
- Proper-projection parity obstruction: PROVED mechanism / computationally reverified through m=10 / known mathematical mechanism
- Arity-only translator lower bound: FALSIFIED for unrestricted compositional translators
- Resource-accounted reconstruction complexity K_G: OPEN / highest-priority asymptotic route
- Global shared-translator obstruction: **PROVED finite specialization**; all taskwise gaps may vanish while one shared translator fails due source-fibre collisions
- Exact auxiliary-interface theorem: **PROVED** in the finite shared-translator model: minimum interface alphabet size equals maximum collision multiplicity; fixed-width bits equal `ceil(log2 m)`
- Reversibility Gap: **NAIVE METRIC ROUTE FALSIFIED** for the current nonlinear `Omega_G`; exact R/I cross-channel counterexample gives `Omega(x,z)=3 > Omega(x,y)+Omega(y,z)=2`. Symmetric round-trip cost remains a diagnostic only. Composition-compatible repair or explicit nonmetric interaction-surplus theory OPEN.
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
1. Lift the shared-translator collision theorem from static symbols to operational traces and full task-scale-error-vector-budget tuples, preserving explicit R/I/A/L augmentation costs.
2. Define a whole-envelope directed `Omega_G` requiring one globally realizable translator and test identity, monotonicity, composition behavior, invariance, and degeneracies. Do **not** assume a triangle inequality under a superadditive interaction penalty.
3. Separate composition-compatible directed-distance structure from nonlinear cross-channel composition surplus; test whether either yields a nontrivial operational theorem beyond known directed-cost/irreversibility theory.
4. Seek a finite/computable complete monotone family only for an explicitly structured translator class; otherwise seek an infinite separating family or dual/separation-oracle criterion. Do not pursue a universal finite family.
5. Couple translator distinguishability to explicit vector-resource budgets to seek a quantitative lower bound not reducible to pure coding or classification.
6. Specify admissible world-transition operators before attempting a broader No-Free-Capability theorem.
7. Define natural resource-restricted translator models and test whether K_G reduces to known circuit, communication, database, CSP, extension-complexity or simulation-preorder measures.
8. Search whole-envelope matched pairs where fixed-task Pareto data and low-order summaries agree but global translation/reconstruction costs differ.
9. Audit all candidate quantities against mature neighboring concepts, including catalysis, irreversibility, directed deficiencies, and impossibility of finite complete monotone sets.

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
- `gc2/tests/test_gc2_reversibility_gap.py`
- `gc2/LOCAL_TO_GLOBAL_AUDIT_002.md`
- `gc2/TEST_REPORT_003.md`
- `gc2/tests/test_gc2_finite_audit.py`
