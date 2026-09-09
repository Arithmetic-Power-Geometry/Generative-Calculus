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
- Endpoint-only reversibility accounting: **FALSIFIED as complete in a finite labelled-state specialization**. Two worlds have the identical directional endpoint-cost pair `(1,1)` and return to the same external endpoint label `X`, yet one preserves and the other destroys a one-step future capability after `f;r`. Any reversibility classifier depending only on `(Omega_G(X->Y),Omega_G(Y->X))` therefore fails on this class. Trace/future-capability residual remains OPEN; mechanism is KNOWN/IMPORTED neighborhood.
- Future label-set signatures: **FALSIFIED as complete**. Equal reachable label sets at every horizon can hide different action/interface identities; increasing horizon cannot repair the collision.
- Action/cost trace-set signatures under branching: **FALSIFIED as complete**. Audit 025 gives a finite nondeterministic pair with identical complete action/cost trace language `{epsilon,a,ab,ac}` but different robust post-`a` capability: delayed choice preserves `{b,c}`, early nondeterministic commitment guarantees neither. Whole-envelope equivalence must retain branching conditional structure, not only flattened traces. Mechanism is KNOWN/IMPORTED from the linear-time/branching-time spectrum and weighted-transition semantics.
- Budget-indexed branching relation on finite augmented `(s,B,I,A,L)` states: **FALSIFIED as a standalone novelty route / IMPORTED-KNOWN mechanism**. Under fixed finite augmented-state moves and integer vector updates it reduces to alternating simulation/refinement and/or multidimensional energy/resource-game structure.
- Dynamic structural augmentation (create/delete/rewrite future channels/actions/rules/game structure): **FALSIFIED as a standalone new-semantic-class route / IMPORTED-KNOWN mechanism**. Audit 027 proves exact compilation to a fixed meta-transition system over complete structural configurations; finite configuration sets compile to finite labelled graphs. The surviving target is a succinctness/representation-complexity separation, not mutability itself.
- Order-sensitive accounting: **PROVED boundary theorem / decisive falsification**. Equal aggregate augmentation vectors need not imply equal capability under noncommuting state-dependent transformations. Pairwise commutation plus path-independent accounting restores aggregate sufficiency. Mechanism is KNOWN/IMPORTED neighborhood.
- Exact finite-world experiments: ACTIVE; deterministic parity audit PASS through m=10
- Budgeted-closure audit: PASS; 729 exhaustive 3-state worlds, 6,561 singleton-start/budget cases, 59,049 lifted start-set monotonicity inclusion checks; 0 violations after lifted-state repair
- Omega_G audit: PASS; 576 three-state gated/resource worlds, 13,824 world/context cases; brute augmentation enumeration and exact path formula agree with 0 mismatches; zero-gap closure equivalence and context monotonicity show 0 violations
- Shared-translator audit: PASS by exhaustive source/target assignment enumeration for `n=1..4`, binary source alphabet, three-label target alphabet: 1,554 paired finite worlds; constructive sufficiency and lower-bound checks included
- Reachable-envelope transport finite audit: PASS; 20,000 randomized worlds, 11,441 reachable sampled pairs, 36,171 membership checks, 0 violations in the nonnegative additive path-cost specialization
- Composition-cost assumption audit: PASS; explicit superadditive counterexample shows subadditivity/control is necessary
- Prior-art status of finite Omega_G: **high collision risk / not a breakthrough claim** because the resource component reduces to mature resource-constrained shortest-path/minimum-augmentation structure; Le Cam deficiency is also a neighboring directed-gap precedent
- Prior-art status of global translator collision theorem: **KNOWN/IMPORTED mechanisms** (functional consistency, pigeonhole coding, repeated-feature classification error); GC-II novelty not established by this specialization alone
- Prior-art status of reversibility diagnostics: **KNOWN/IMPORTED neighborhood**; forward/reverse conversion asymmetry and irreversibility are mature in thermodynamics and resource theories. Endpoint equality also fails to guarantee future-behavior restoration; state equivalence/bisimulation/coarse-graining are neighboring mature mechanisms.
- Prior-art status of structural mutability: **KNOWN/IMPORTED neighborhood**; graph transformation, dynamic software reconfiguration and reconfigurable automata already model states whose topology/components/rules change. No novelty claim from structural rewriting alone.
- AI capability-accounting experiment: OPEN
- Robotics validation: OPEN
- Scientific-discovery validation: OPEN
- Breakthrough status: NONE YET

## Evidence rule
Nothing in this ledger may be upgraded to PROVED or BREAKTHROUGH CANDIDATE without a proof artifact or reproducible computational/empirical evidence plus prior-art collision review.

## Immediate test order
1. Fix a succinct structural-rewrite/translator representation model `M`; do not allow arbitrary explicit configuration expansion to count as a free representation.
2. Define representation-aware `Omega_G^struct` as minimum ordered R/I/A/L augmentation cost plus an explicit structural description/translator cost under `M`; verify units or use a Pareto/vector form rather than dimensionally invalid scalar addition.
3. Search finite parametric families where explicit configuration compilation has provable superpolynomial/exponential blow-up while a succinct structural description remains small, and where the separation is tied to whole-envelope task-scale-error-budget behavior rather than generic automata determinization.
4. Seek a closure-escape lower bound on minimum structural edit/translator description complexity; collision-check against graph-edit distance, minimum-cost graph rewriting, succinct games, planning and program synthesis.
5. Test whether low-order/taskwise capability summaries can agree while minimum whole-envelope structural rewrite programs provably differ asymptotically.
6. Collision-check any candidate against graph transformation, dynamic/reconfigurable systems, self-modifying transition systems, adaptive control, program synthesis, resource theories, Petri/process calculi, succinct-game complexity and algorithmic information before novelty upgrade.
7. Characterize commuting/path-independent subclasses where an aggregate `F(Delta)` theorem is valid.
8. Seek a finite/computable complete monotone family only for an explicitly structured translator class; otherwise seek an infinite separating family or dual/separation-oracle criterion.
9. Define natural resource-restricted translator models and test whether K_G reduces to known circuit, communication, database, CSP, extension-complexity or simulation-preorder measures.
10. Only after a structural theorem survives collision checks, build controlled AI capability-accounting experiments, then robotics/autonomous systems, distributed computation and endogenous scientific inquiry.

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
- `gc2/ENDPOINT_REVERSIBILITY_INSUFFICIENCY_AUDIT_019.md`
- `gc2/FUTURE_LABEL_SIGNATURE_INCOMPLETENESS_AUDIT_024.md`
- `gc2/BRANCHING_TRACE_INCOMPLETENESS_AUDIT_025.md`
- `gc2/BUDGETED_BRANCHING_COLLISION_AUDIT_026.md`
- `gc2/STRUCTURAL_AUGMENTATION_COMPILATION_AUDIT_027.md`
- `gc2/trace_reversibility.py`
- `gc2/branching_capability.py`
- `gc2/tests/test_gc2_trace_reversibility.py`
- `gc2/tests/test_gc2_branching_capability.py`
- `gc2/tests/test_gc2_order_sensitive_accounting.py`
- `gc2/tests/test_gc2_reversibility_gap.py`
- `gc2/LOCAL_TO_GLOBAL_AUDIT_002.md`
- `gc2/TEST_REPORT_003.md`
- `gc2/tests/test_gc2_finite_audit.py`
