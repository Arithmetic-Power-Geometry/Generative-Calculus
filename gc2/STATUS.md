# GC-II Status Ledger

## Branch
`gc2-capability-accounting-lab`

## Current state
- Operational closure: **PROVED finite formalization** via lifted cumulative-resource state; naive base-state budget closure **FALSIFIED** by budget-refresh idempotence failure
- Generative Novelty Gap: **PROVED finite single-target candidate** as minimum operational augmentation penalty; exact path-deficit reduction established; whole-envelope/global-translator version OPEN
- Closure-Escape Criterion: **PROVED for the finite single-target Omega_G candidate** (`Omega_G=0` iff target lies in lifted budgeted closure under positive-definite monotone penalty); stronger whole-envelope criterion OPEN
- No-Free-Capability Theorem: OPEN / admissible world evolution must be specified before a meaningful proof
- Quantitative Capability-Accounting Bound: **PROVED finite candidate upper bound** `Omega_G <= F(Delta R,Delta I,Delta A,Delta L)` whenever the stated augmentation realizes the target; nonlinear interaction penalty implemented; universal/nontrivial lower bounds OPEN
- Complete Convertibility Criterion: OPEN / high prior-art collision risk
- Generative Order: OPEN (seeded by GC-I projection irreducibility)
- Proper-projection parity obstruction: PROVED mechanism / computationally reverified through m=10 / known mathematical mechanism
- Arity-only translator lower bound: FALSIFIED for unrestricted compositional translators
- Resource-accounted reconstruction complexity K_G: OPEN / highest-priority surviving route
- Reversibility Gap: OPEN (seeded by GC-I cyclic reversal example)
- Exact finite-world experiments: ACTIVE; deterministic parity audit PASS through m=10
- Budgeted-closure audit: PASS; 729 exhaustive 3-state worlds, 6,561 singleton-start/budget cases, 59,049 lifted start-set monotonicity inclusion checks; 0 violations after lifted-state repair
- Omega_G audit: PASS; 576 three-state gated/resource worlds, 13,824 world/context cases; brute augmentation enumeration and exact path formula agree with 0 mismatches; zero-gap closure equivalence and context monotonicity show 0 violations
- Reachable-envelope transport finite audit: PASS; 20,000 randomized worlds, 11,441 reachable sampled pairs, 36,171 membership checks, 0 violations in the nonnegative additive path-cost specialization
- Composition-cost assumption audit: PASS; explicit superadditive counterexample shows subadditivity/control is necessary
- Prior-art status of finite Omega_G: **high collision risk / not a breakthrough claim** because the resource component reduces to mature resource-constrained shortest-path/minimum-augmentation structure; Le Cam deficiency is also a neighboring directed-gap precedent
- AI capability-accounting experiment: OPEN
- Robotics validation: OPEN
- Scientific-discovery validation: OPEN
- Breakthrough status: NONE YET

## Evidence rule
Nothing in this ledger may be upgraded to PROVED or BREAKTHROUGH CANDIDATE without a proof artifact or reproducible computational/empirical evidence plus prior-art collision review.

## Immediate test order
1. Lift Omega_G from single-target reachability to a whole-envelope directed deficiency requiring one globally realizable translator across task, scale, error and resource profiles.
2. Enumerate smallest finite paired worlds and search for cases where all per-task reachability gaps vanish but no single global translator realizes the whole envelope.
3. Test identity, monotonicity, composition/triangle behavior and invariance of the translator-sensitive gap; falsify aggressively.
4. Specify admissible world-transition operators before attempting No-Free-Capability.
5. Define natural resource-restricted translator models and test whether K_G reduces to known circuit, communication, database, CSP, extension-complexity or simulation-preorder measures.
6. Search whole-envelope matched pairs where fixed-task Pareto data and low-order summaries agree but global translation/reconstruction costs differ.
7. Audit all candidate quantities against mature neighboring concepts.

## Reproducible artifacts
- `gc2/BUDGETED_CLOSURE_AUDIT_004.md`
- `gc2/tests/test_gc2_budgeted_closure.py`
- `gc2/OMEGA_G_AUDIT_005.md`
- `gc2/omega_gap.py`
- `gc2/tests/test_gc2_omega_gap.py`
- `gc2/LOCAL_TO_GLOBAL_AUDIT_002.md`
- `gc2/TEST_REPORT_003.md`
- `gc2/tests/test_gc2_finite_audit.py`
