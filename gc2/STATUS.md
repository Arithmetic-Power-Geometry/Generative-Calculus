# GC-II Status Ledger

## Branch
`gc2-capability-accounting-lab`

## Current state
- Operational closure: **PROVED finite formalization** via lifted cumulative-resource state; naive base-state budget closure **FALSIFIED** by budget-refresh idempotence failure
- Generative Novelty Gap: OPEN / requires a nontrivial operational definition on the corrected lifted-closure domain
- Closure-Escape Criterion: OPEN
- No-Free-Capability Theorem: OPEN / admissible world evolution must be specified before a meaningful proof
- Quantitative Capability-Accounting Bound: OPEN
- Complete Convertibility Criterion: OPEN / high prior-art collision risk
- Generative Order: OPEN (seeded by GC-I projection irreducibility)
- Proper-projection parity obstruction: PROVED mechanism / computationally reverified through m=10 / known mathematical mechanism
- Arity-only translator lower bound: FALSIFIED for unrestricted compositional translators
- Resource-accounted reconstruction complexity K_G: OPEN / highest-priority surviving route
- Reversibility Gap: OPEN (seeded by GC-I cyclic reversal example)
- Exact finite-world experiments: ACTIVE; deterministic parity audit PASS through m=10
- Budgeted-closure audit: PASS; 729 exhaustive 3-state worlds, 6,561 singleton-start/budget cases, 59,049 lifted start-set monotonicity inclusion checks; 0 violations after lifted-state repair
- Reachable-envelope transport finite audit: PASS; 20,000 randomized worlds, 11,441 reachable sampled pairs, 36,171 membership checks, 0 violations in the nonnegative additive path-cost specialization
- Composition-cost assumption audit: PASS; explicit superadditive counterexample shows subadditivity/control is necessary
- AI capability-accounting experiment: OPEN
- Robotics validation: OPEN
- Scientific-discovery validation: OPEN
- Breakthrough status: NONE YET

## Evidence rule
Nothing in this ledger may be upgraded to PROVED or BREAKTHROUGH CANDIDATE without a proof artifact or reproducible computational/empirical evidence plus prior-art collision review.

## Immediate test order
1. Define a candidate directed operational deficiency / Generative Novelty Gap on the lifted cumulative-resource state space, preserving task identity, scale, error, vector resources, and one globally realizable translator.
2. Enumerate smallest finite worlds and search for pathological cases/counterexamples to identity, monotonicity, composition, and invariance properties of the candidate gap.
3. Attempt non-tautological closure-escape equivalences on the lifted closure object.
4. Specify admissible world-transition operators before attempting No-Free-Capability.
5. Define natural resource-restricted translator models and test whether K_G reduces to known circuit, communication, database, CSP, or extension-complexity measures.
6. Search whole-envelope matched pairs where fixed-task Pareto data and low-order summaries agree but global translation/reconstruction costs differ.
7. Audit all candidate quantities against mature neighboring concepts.

## Reproducible artifacts
- `gc2/BUDGETED_CLOSURE_AUDIT_004.md`
- `gc2/tests/test_gc2_budgeted_closure.py`
- `gc2/LOCAL_TO_GLOBAL_AUDIT_002.md`
- `gc2/TEST_REPORT_003.md`
- `gc2/tests/test_gc2_finite_audit.py`
